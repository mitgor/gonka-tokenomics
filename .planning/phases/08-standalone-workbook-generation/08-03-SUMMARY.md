# Phase 8 Plan 3: What-If Toggle Wiring Summary

**One-liner:** IF()-wrapped buyback-burn and deploy-POL formulas in token_price.py and treasury.py, enabling Y/N toggle control from the Assumptions tab with zero regression at default Y.

## What Was Done

### Task 1: Add Buyback-Burn toggle to token_price.py
- Extracted `buyback_toggle_ref = param_refs["Buyback-Burn Active"]` at function top
- Wrapped column K (Buyback Burn GNK) formula in `IF(toggle="Y", existing_formula, 0)`
- Monthly periods (i<24) use `/12`, annual periods (i>=24) use `/1` -- unchanged
- Downstream columns L (Net Supply Change) cascade automatically (no changes needed)
- Added Y/N DataValidation calls for both what-if toggles in `build_assumptions_tab()` (workbook_base.py)

### Task 2: Add Deploy POL toggle to treasury.py
- Extracted `pol_toggle_ref = param_refs["Deploy POL Active"]` at function top
- Wrapped 5 POL-related formula locations:
  - **B3 (CP Balance period 0):** POL allocation deduction wrapped in `IF(toggle="Y", pol_alloc, 0)`
  - **C3 (CP Outflows period 0):** POL allocation outflow wrapped in `IF(toggle="Y", pol_alloc, 0)`
  - **D (POL Revenue, all periods):** Entire midpoint LP fee formula wrapped in `IF(toggle="Y", ..., 0)`
  - **M (Net Treasury GNK, all periods):** POL allocation addition wrapped in `IF(toggle="Y", pol_alloc, 0)`
  - **N (Net Treasury USD, all periods):** POL GNK value term wrapped in `IF(toggle="Y", pol_alloc*price, 0)`
- Cumulative POL Revenue (col E) cascades automatically from toggled D
- Non-POL columns (F buyback cross-ref, G-K defense/AI fund) left unchanged

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing Critical] Added Y/N DataValidation to build_assumptions_tab()**
- **Found during:** Task 1
- **Issue:** `build_assumptions_tab()` (master workbook path) did not call `_add_what_if_toggle()` for the two new toggle parameters. Without DataValidation, users could type arbitrary values into toggle cells, breaking the IF formulas.
- **Fix:** Added a loop calling `_add_what_if_toggle()` for both "Buyback-Burn Active" and "Deploy POL Active" in `build_assumptions_tab()`, matching the pattern already implemented in `build_filtered_assumptions_tab()`.
- **Files modified:** generators/workbook_base.py
- **Commit:** 14d6cee

## Verification Results

1. `python generate.py` produces master workbook without errors
2. Master workbook formula structure unchanged (default Y means IF always evaluates to existing formula)
3. Buyback column K in Token Price contains `IF(Assumptions!$B$89="Y",...)` wrapper
4. Treasury columns B, C, D, M, N contain `IF(Assumptions!$B$90="Y",...)` wrappers
5. Tail Emission Toggle (ON/OFF) in Fee Transition continues working unchanged
6. Y/N DataValidation present on both what-if toggle cells

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Only wrap POL-specific formula parts in treasury.py | Surgical approach avoids touching buyback, AI fund, defense calculations | Clean separation of concerns; each toggle controls only its mechanism |
| Wrap POL alloc in CP Balance/Outflows (not just revenue) | When POL is toggled off, no GNK should leave Community Pool for POL | CP balance higher when POL inactive (22M GNK stays in pool) |
| Add DataValidation to master build_assumptions_tab() | Consistency with filtered builder; prevents invalid toggle values | Both master and standalone workbooks have dropdown validation on toggles |

## Key Files

### Modified
- `generators/token_price.py` -- Buyback burn column K wrapped in IF() toggle
- `generators/treasury.py` -- 5 POL-related formula locations wrapped in IF() toggle
- `generators/workbook_base.py` -- Y/N DataValidation added for what-if toggles in master builder

## Metrics

- **Duration:** 3.3 min
- **Completed:** 2026-02-06
- **Tasks:** 2/2
- **Commits:** 2 task commits

## Commit Log

| Task | Commit | Description |
|------|--------|-------------|
| 1 | 14d6cee | feat(08-03): add buyback-burn toggle to token_price.py |
| 2 | 395e677 | feat(08-03): add deploy POL toggle to treasury.py |

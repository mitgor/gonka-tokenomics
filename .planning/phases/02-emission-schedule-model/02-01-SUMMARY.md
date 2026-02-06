# Plan 02-01 Summary: Chart Utils + Emission Data Table

**One-liner:** Chart rendering fix utility and 32-row emission schedule with closed-form EXP decay formulas referencing Assumptions tab via param_refs

## What Was Built

- `generators/chart_utils.py`: `fix_chart_rendering()` patches openpyxl 3.1.5 Application tag in docProps/app.xml so Excel renders charts; `col_to_num()` converts column letter to 1-based number. Only stdlib imports (zipfile, re, shutil, os).
- `generators/emission.py`: `build_emission_tab(wb, param_refs)` creates the "Emission Schedule" worksheet with 32 data rows, 10 columns, and 3 validation rows. Returns `emission_meta` dict for downstream tabs.

## Key Details

- 32 data rows: 24 monthly (Y1 M01 through Y2 M12, 30-day epochs) + 8 annual (Year 3 through Year 10, 365-day epochs)
- 10 columns: period label, start/end epoch, mining emission, CP unlock, founder vesting, total new supply, cumulative circulating, annualized inflation rate, ETH 0.5% benchmark
- Mining emission: `E0 * EXP(-r * start) * (1 - EXP(-r * days)) / (1 - EXP(-r))` using Assumptions references
- Community pool unlock: linear over 3650 days (`CP / 3650 * days`)
- Founder vesting: IF-based conditional formula covering full period, zero (post-vest), and partial period cases
- Validation rows (36-38): closed-form total vs SUM of periods vs absolute difference
- All formulas reference Assumptions tab via param_refs -- no hardcoded parameter values (323000, 0.000475, etc.)
- ETH 0.5% benchmark is a constant 0.005 per row for inflation comparison
- First-period inflation rate left blank (no prior circulating supply for meaningful annualization)

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Literal 48 for vesting months | Not available in parameters.py; whitepaper value used directly as structural constant |
| Literal 3650 for CP unlock period | 10-year linear unlock period, structural constant per plan specification |
| First-period inflation rate blank | No prior circulating supply exists for row 3; annualized rate would be undefined |
| Static epoch values in B/C columns | Start and end epochs are deterministic from period structure, not formula-dependent |

## Deviations from Plan

None -- plan executed exactly as written.

## Files Created

| File | Description |
|------|-------------|
| `generators/chart_utils.py` | Chart rendering fix + column number utility |
| `generators/emission.py` | Emission schedule model tab builder |

## Verification Results

- Meta dict: 32 data rows, 10 columns, validation at row 36
- Formula check: `=Assumptions!$B$11*EXP(-Assumptions!$B$12*B3)*(1-EXP(-Assump...` -- references Assumptions, uses EXP, no hardcoded values
- All 32 period rows populated with labels
- Validation row present: "Validation: Closed-Form Total"
- col_to_num('A') = 1, col_to_num('K') = 11
- Test file generated: output/gonka_test_emission.xlsx (11,783 bytes)

## Commits

| Hash | Message |
|------|---------|
| ef5eb1c | feat(02-01): add chart_utils.py with fix_chart_rendering and col_to_num |
| 5ee2624 | feat(02-01): add emission schedule data table with 32-row model |

## Metrics

- Duration: ~2 minutes
- Completed: 2026-02-06

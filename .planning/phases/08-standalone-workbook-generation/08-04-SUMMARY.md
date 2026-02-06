# Phase 8 Plan 4: Standalone Workbook Orchestrator & Integration Summary

**One-liner:** Standalone workbook orchestrator generating 4 focused .xlsx files with filtered assumptions, full model chains, glossary, cover sheets, and navigation -- integrated into generate.py for single-command output of 5 workbooks.

## Metadata

| Field | Value |
|-------|-------|
| Phase | 08 |
| Plan | 04 |
| Subsystem | standalone-workbook-generation |
| Duration | ~3 min |
| Completed | 2026-02-07 |
| Tags | openpyxl, standalone, orchestrator, integration, workbook-generation |

## What Was Built

### generators/standalone.py (new)
- `generate_standalone(config_key)` -- builds one standalone workbook from scratch:
  - Creates fresh Workbook, calls `build_filtered_assumptions_tab()` with config's param set
  - Calls same model builders as master in dependency order via `_build_model_tabs()`
  - Adds Definitions tab via `build_glossary_tab(wb, GLOSSARY_TERMS)`
  - Adds Documentation cover sheet via `build_cover_sheet()` at index 0
  - Asserts tab order: Documentation first, Assumptions second, Definitions last
  - Adds "Back to Documentation" navigation links on all non-Documentation tabs
  - Saves to output/ and applies `fix_chart_rendering()` post-processing
- `generate_standalones()` -- loops all 4 configs, prints summary, returns dict
- `_build_model_tabs()` -- dispatches builder calls based on config["builders"] list
- `_add_back_to_doc_links()` -- standalone-specific navigation with positions matching master

### generate.py (updated)
- Added `generate_standalones()` call after master workbook generation
- Added summary line: "Generated 5 workbooks total (1 master + 4 standalone)"
- Test mode (`--test`) unchanged

## Output Workbooks

| Workbook | Tabs | Assumptions Rows | Toggles |
|----------|------|------------------|---------|
| gonka_master_model.xlsx | 8 | 108 | Tail (ON/OFF), Buyback (Y/N), POL (Y/N) |
| gonka_token_price.xlsx | 5 | 35 | Buyback (Y/N), Scenario selector |
| gonka_fee_transition.xlsx | 6 | 49 | Tail (ON/OFF), Buyback (Y/N), Scenario selector |
| gonka_host_profitability.xlsx | 7 | 60 | Tail (ON/OFF), Buyback (Y/N), Scenario selector |
| gonka_treasury_pol.xlsx | 7 | 63 | Tail (ON/OFF), Buyback (Y/N), POL (Y/N), Scenario selector |

## Dependency Graph

| Direction | Items |
|-----------|-------|
| Requires | 08-01 (standalone_config.py, build_filtered_assumptions_tab), 08-02 (glossary.py, cover_sheet.py), 08-03 (IF-wrapped toggle formulas) |
| Provides | 4 standalone .xlsx files, single-command generation via `python generate.py` |
| Affects | Phase 9 (protection/polish may apply to standalones) |

## Tech Stack

| Category | Items |
|----------|-------|
| Added | None (no new dependencies) |
| Patterns | Builder dispatch pattern (config["builders"] list drives model tab construction) |

## Key Files

| Action | Files |
|--------|-------|
| Created | generators/standalone.py |
| Modified | generate.py |

## Commits

| Hash | Type | Description |
|------|------|-------------|
| 406fd73 | feat | Create standalone workbook orchestrator |
| ea717b9 | feat | Integrate standalone generation into generate.py |

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Definitions back-link at D1 (not C1) | C1 is a MergedCell within the A1:C1 title merge; D1 avoids conflict |
| _build_model_tabs helper for builder dispatch | Centralizes dependency-order logic; avoids duplicating builder call chain per standalone |
| Tab count printed from config (builders + 3) | Avoids loading saved workbook just for tab count; Documentation + Assumptions + Definitions = 3 fixed tabs |
| LINK_FONT redefined locally in standalone.py | Same module-local pattern as documentation.py and cover_sheet.py; avoids cross-module coupling |

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Fixed MergedCell collision on Definitions back-link**
- **Found during:** Task 1 verification
- **Issue:** Plan specified placing the Definitions back-link at C1, but glossary.py merges A1:C1 for the title. Attempting to write to C1 raises `AttributeError: 'MergedCell' object attribute 'value' is read-only`.
- **Fix:** Changed Definitions back-link position from C1 (column 3) to D1 (column 4), outside the merged range.
- **Files modified:** generators/standalone.py
- **Commit:** 406fd73

## Verification Results

1. `python generate.py` runs without errors, produces 5 .xlsx files
2. Token Price: 5 tabs (Documentation, Assumptions, Emission Schedule, Token Price, Definitions)
3. Fee Transition: 6 tabs (above + Fee Transition)
4. Host Profitability: 7 tabs (above + Host Profitability)
5. Treasury & POL: 7 tabs (Documentation, Assumptions, Emission Schedule, Token Price, Fee Transition, Treasury & POL, Definitions)
6. Master: 8 tabs, unchanged from Phase 7
7. All standalone Assumptions tabs have fewer rows than master (108)
8. All Documentation tabs have version v1.1, changelog, and scenario narratives
9. All Definitions tabs have 20 alphabetically sorted glossary entries
10. Toggle dropdowns verified: Y/N on what-if toggles, ON/OFF on tail emission, scenario selector
11. Back-to-Documentation navigation links present on all non-Documentation tabs

## Next Phase Readiness

- Phase 8 is now complete: all 4 plans delivered
- Phase 9 (Protection & Polish) can proceed with all 5 workbooks in output/
- No blockers or concerns

---
phase: 03-token-price-scenarios-model
plan: 01
subsystem: model
tags: [openpyxl, scenario-selector, data-validation, MATCH, CHOOSE, cross-sheet, linear-interpolation, buyback-burn, token-price]

# Dependency graph
requires:
  - phase: 01-foundation
    provides: param_refs dict with 60 base parameters, NamedStyles, workbook_base.py
  - phase: 02-emission-schedule
    provides: emission_meta dict with sheet coordinates, 32-period structure
provides:
  - Scenario selector pattern (DataValidation + MATCH + CHOOSE) on Assumptions tab
  - Active Price Low/High param_refs derived from dropdown selection
  - Token Price worksheet with 12-column data model (price trajectories, FDV, market cap, buyback-burn)
  - price_meta dict for downstream chart/tab consumption
  - Assumed Annual Fee Revenue placeholder parameter
affects:
  - 03-02 (charts + conditional formatting for Token Price tab)
  - 04-fee-transition (replaces fee revenue placeholder with actual model)
  - 05-host-profitability (uses price_meta for host economics calculations)
  - 06-treasury (uses scenario selector pattern for treasury projections)

# Tech tracking
tech-stack:
  added: [openpyxl.worksheet.datavalidation.DataValidation]
  patterns: [DataValidation+MATCH+CHOOSE scenario switching, cross-sheet references via quote_sheetname, linear price interpolation]

key-files:
  created:
    - generators/token_price.py
  modified:
    - models/parameters.py
    - generators/workbook_base.py
    - generate.py

key-decisions:
  - "Fee revenue placeholder at $1M/yr in BUYBACK PARAMETERS group; Phase 4 replaces with actual model"
  - "Active Price column uses CHOOSE-derived Low/High for scenario-responsive interpolation"
  - "All 4 price columns always visible (not hidden by dropdown); Active Price drives FDV/market cap/buyback"
  - "Buyback burn period-adjusted: /12 for monthly periods (i<24), /1 for annual periods (i>=24)"

patterns-established:
  - "Scenario selector: DataValidation dropdown + MATCH index + CHOOSE values on Assumptions tab"
  - "Cross-sheet references: quote_sheetname() + emission_meta coords for inter-tab formulas"
  - "price_meta dict: same structure as emission_meta for downstream consumers"

# Metrics
duration: 3min
completed: 2026-02-06
---

# Phase 3 Plan 01: Token Price Scenarios Model Summary

**Scenario selector (DataValidation + MATCH + CHOOSE) on Assumptions tab driving 12-column Token Price data model with 4 price trajectories, FDV, market cap, and buyback-burn calculations across 32 periods**

## Performance

- **Duration:** 3 min
- **Started:** 2026-02-06T18:03:30Z
- **Completed:** 2026-02-06T18:06:14Z
- **Tasks:** 2
- **Files modified:** 4

## Accomplishments

- Scenario selector pattern established: dropdown defaults to "Base", MATCH converts to index 1/2/3, CHOOSE derives Active Price Low/High from the three scenario ranges
- Token Price tab with 12 columns x 32 rows: Conservative/Moderate/Aggressive/Bitfury price interpolations, Active Price, Circulating Supply + Gross New Supply cross-refs, FDV, Circ Market Cap, Buyback Burn (period-adjusted), Net Supply Change
- param_refs expanded from 60 to 65 entries (Active Scenario, Scenario Index, Active Price Low/High, Assumed Annual Fee Revenue)
- price_meta dict returned for Plan 02 charts and downstream phases

## Task Commits

Each task was committed atomically:

1. **Task 1: Add fee revenue parameter and scenario selector to Assumptions tab** - `bff8981` (feat)
2. **Task 2: Create token_price.py with 12-column data table** - `107d3ad` (feat)

## Files Created/Modified

- `generators/token_price.py` - Token Price tab builder with build_token_price_tab() returning price_meta
- `generators/workbook_base.py` - Added _add_scenario_selector() with DataValidation dropdown, MATCH, CHOOSE formulas
- `models/parameters.py` - Added "Assumed Annual Fee Revenue" ($1M placeholder) to BUYBACK PARAMETERS
- `generate.py` - Wired token_price into generate_all() pipeline

## Decisions Made

- **Fee revenue placeholder approach:** Added $1M/yr "Assumed Annual Fee Revenue" to BUYBACK PARAMETERS rather than deferring buyback-burn entirely. Phase 4 will replace this with the actual fee transition model. This gives leadership an immediate sense of buyback impact.
- **All 4 price columns always visible:** Conservative, Moderate, Aggressive, and Bitfury columns are always shown regardless of dropdown selection. The "Active Price" column (driven by CHOOSE) is what FDV/market cap/buyback calculations use. This gives the comparison view (all scenarios) plus the detailed analysis (active scenario).
- **Period-adjusted buyback:** Monthly periods (Y1-Y2, i=0..23) divide annual fee revenue by 12; annual periods (Y3-Y10, i=24..31) use the full annual amount. This matches the emission schedule period structure.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- price_meta dict available for Plan 02 (charts + conditional formatting)
- Scenario selector pattern proven and ready for reuse in Phases 4-6
- generate.py pipeline now includes Token Price tab in master workbook
- All cross-sheet references verified working with quote_sheetname

---
*Phase: 03-token-price-scenarios-model*
*Completed: 2026-02-06*

---
phase: 06-treasury-pol-simulation
plan: 01
subsystem: treasury
tags: [openpyxl, treasury, pol, buyback, defense, ai-fund, excel]

# Dependency graph
requires:
  - phase: 01-foundation
    provides: param_refs dict, workbook_base, styles
  - phase: 02-emission-schedule
    provides: emission_meta with period labels (col A)
  - phase: 03-token-price-scenarios
    provides: price_meta with active price (col F) and buyback burn (col K)
  - phase: 04-fee-transition
    provides: fee_meta with AI fund share (col L)
provides:
  - generators/treasury.py with build_treasury_tab() returning treasury_meta
  - 14-column Treasury & POL data table (32 periods)
  - Time-to-X milestone callouts with IFERROR wrappers
  - Floor defense scenario table (3/6/12 month durations)
  - IL caveat label (REQ-M4-07)
  - TREASURY OPERATIONS parameter group (2 new parameters)
affects: [06-02-charts, 07-dashboard, 08-governance-scenarios, 09-finalization]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Treasury composition tab aggregating 3 upstream tabs via cross-sheet references"
    - "Below-data IFERROR-wrapped MATCH/INDEX for Time-to-X milestone detection"
    - "Defense scenario table using Year 2 baseline (L26) for adequacy assessment"

key-files:
  created:
    - generators/treasury.py
  modified:
    - models/parameters.py
    - generate.py

key-decisions:
  - "Community Pool waterfall starts at 120M minus POL (one-time) and defense (ongoing prorated)"
  - "POL revenue uses midpoint of low/high LP fee revenue minus rebalancing cost"
  - "Buyback burn cross-refs Token Price col K (not recalculated)"
  - "AI Fund balance tracks inflows from Fee Transition col L minus monthly expenses prorated to period"
  - "Defense treasury accumulates GNK-to-USD conversion; no active spending in main timeline"
  - "Net Treasury USD sums: CP balance in USD + POL GNK value + cumul POL fees + defense treasury + AI Fund balance"
  - "Defense scenario table uses L26 (Year 2 end) as baseline, tests 3/6/12 month spending against $2M target"

patterns-established:
  - "Treasury composition pattern: single tab consolidating multiple upstream tab cross-references"
  - "Year 2 baseline reference for scenario tables (row 26 = last monthly period)"

# Metrics
duration: 2min
completed: 2026-02-06
---

# Phase 6 Plan 1: Treasury & POL Data Model Summary

**14-column Treasury & POL simulation tab aggregating Community Pool waterfall, POL LP fee revenue, cumulative buyback burn, AI Fund balance, floor defense treasury, and net treasury value across 32 periods**

## Performance

- **Duration:** 2 min
- **Started:** 2026-02-06T21:30:15Z
- **Completed:** 2026-02-06T21:32:34Z
- **Tasks:** 1
- **Files modified:** 3

## Accomplishments
- Built generators/treasury.py with build_treasury_tab() following established generator pattern
- 14-column data table (A-N) with all formulas referencing param_refs and upstream tabs
- Community Pool waterfall showing 120M minus POL allocation and defense draws
- Cross-tab references for buyback burn (Token Price col K) and AI Fund inflows (Fee Transition col L)
- Time-to-X milestones: CP depletion, defense $2M target, 1% supply burn -- all IFERROR-wrapped
- Floor defense scenarios: 3/6/12 month spending against $2M target using Year 2 baseline
- IL caveat label matching REQ-M4-07 specification exactly
- 2 new parameters in TREASURY OPERATIONS group (AI Fund Monthly Expenses, Defense Active Duration)

## Task Commits

Each task was committed atomically:

1. **Task 1: Add TREASURY OPERATIONS parameters and build 14-column data model** - `819bddc` (feat)

## Files Created/Modified
- `generators/treasury.py` - NEW: build_treasury_tab() with 14-column data model + below-data sections
- `models/parameters.py` - Added TREASURY OPERATIONS group (AI Fund Monthly Expenses, Defense Active Duration)
- `generate.py` - Wired Phase 6 treasury tab into master workbook generation

## Decisions Made
- Community Pool waterfall deducts POL allocation (22M) at period 0 and defense (6M/yr prorated) ongoing -- no general grant modeling in main timeline
- POL revenue uses midpoint approach: (low + high)/2 prorated minus rebalancing cost per period
- AI Fund expenses prorated from monthly to period length: monthly periods = 1x, annual periods ~12.17x
- Defense treasury is accumulation-only in main data table; active spending scenarios in below-data table
- Net Treasury ($) sums all 5 asset components at scenario GNK price
- Defense scenario table references L26 (last monthly period = end of Year 2) as accumulation baseline

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness
- treasury_meta dict returned with all column coordinates for Phase 6 Plan 2 (charts + conditional formatting)
- All 14 data columns populated with Excel formulas for chart data sources
- Below-data sections positioned for chart placement at O1/O17/O33

---
*Phase: 06-treasury-pol-simulation*
*Completed: 2026-02-06*

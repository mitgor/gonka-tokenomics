# Roadmap

## Milestones

- **v1.0 Tokenomics Research & Optimization** -- Phase 1 (shipped 2026-02-05) -- [Archive](milestones/v1.0-ROADMAP.md)
- **v1.1 Economic Modeling** -- Phases 1-9 (complete)

## Overview

v1.1 delivers five professional-grade Excel workbooks (.xlsx) that model Gonka Network token economics for founder/leadership decision-making. The architecture follows a layered dependency model: shared infrastructure (parameters, styles, workbook base) feeds into independent Layer 1 models (emission, token price, treasury) which feed into dependent Layer 2 models (fee transition, host profitability) before everything rolls up into the master workbook dashboard and standalone deliverables. Each phase delivers a complete, verifiable capability building on the last.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Foundation & Shared Infrastructure** - Parameter system, styles, workbook base, CLI skeleton
- [x] **Phase 2: Emission Schedule Model** - First model validates formula-writing pattern with emission decay curve
- [x] **Phase 3: Token Price Scenarios Model** - Multi-scenario price trajectories with scenario selector pattern
- [x] **Phase 4: Fee Transition Crossover Model** - First cross-tab model with crossover analysis (Layer 2)
- [x] **Phase 5: Host Profitability Model** - Most complex cross-tab dependencies, sensitivity tables
- [x] **Phase 6: Treasury & POL Simulation** - Treasury depletion, POL revenue, buyback-burn (most parameters)
- [x] **Phase 7: Dashboard & Master Workbook Assembly** - Master workbook with linked tabs, dashboard, navigation
- [x] **Phase 8: Standalone Workbook Generation** - Four focused standalone workbooks with documentation
- [x] **Phase 9: Polish, Documentation & Validation** - Cell protection, audit trail, print layout, final testing

## Phase Details

### Phase 1: Foundation & Shared Infrastructure
**Goal**: All shared infrastructure exists so that any model module can be built against a working parameter system, consistent styles, and an Assumptions tab builder
**Depends on**: Nothing (first phase)
**Requirements**: REQ-F01, REQ-F02, REQ-F03, REQ-F04, REQ-F05, REQ-U02, REQ-U05, REQ-U06
**Success Criteria** (what must be TRUE):
  1. Running `python generate.py` produces a minimal .xlsx file with a correctly formatted Assumptions tab containing all ~50 v1.0 research parameters
  2. Every parameter value in the generated Assumptions tab traces to a specific v1.0 research document or recommendation number
  3. Blue-shaded input cells, black formula cells, and green cross-tab link cells are visually distinguishable when opening the .xlsx in Excel
  4. Number formatting is consistent: USD uses `$#,##0`, percentages use `0.0%`, token amounts use `#,##0` with commas
  5. The project has exactly one external dependency (openpyxl) and zero constants defined outside of `parameters.py`
**Plans**: 2 plans
Plans:
- [x] 01-01-PLAN.md -- Parameters and styles foundation (all ~50 research parameters + NamedStyle definitions)
- [x] 01-02-PLAN.md -- Workbook base, CLI entry point, and project scaffolding (Assumptions tab builder + generate.py)

### Phase 2: Emission Schedule Model
**Goal**: The emission decay curve is visualized over 10 years and the circulating supply schedule is computed, validating the core formula-writing pattern that all subsequent models will follow
**Depends on**: Phase 1
**Requirements**: REQ-M2-01, REQ-M1-03, REQ-M1-04, REQ-U07, REQ-U08
**Success Criteria** (what must be TRUE):
  1. Opening the generated workbook shows an emission decay curve chart plotting `323,000 * exp(-0.000475 * epochs)` over 10 years with a closed-form formula in each cell (not iterative references)
  2. A circulating supply schedule shows epoch emissions + Community Pool unlocks + founder vesting = total circulating at each time point, with monthly granularity for Year 1-2 and annual for Year 3-10
  3. Annualized inflation rate is displayed per period with labels showing comparison context (e.g., ETH ~0.5%)
  4. Changing the decay rate or initial emission on the Assumptions tab causes all emission and supply formulas to recalculate automatically in Excel
  5. A validation row confirms the geometric series sum matches the cell-by-cell cumulative total (difference < 1 GNK)
**Plans**: 2 plans
Plans:
- [x] 02-01-PLAN.md -- Chart utilities and emission data table with closed-form formulas, validation rows
- [x] 02-02-PLAN.md -- Charts (emission decay, supply composition, inflation rate) and CLI integration

### Phase 3: Token Price Scenarios Model
**Goal**: Leadership can compare 3-5 GNK price trajectories with market cap implications and see how buyback-burn affects net token supply across scenarios
**Depends on**: Phase 2
**Requirements**: REQ-M1-01, REQ-M1-02, REQ-M1-05, REQ-M1-06, REQ-U03
**Success Criteria** (what must be TRUE):
  1. The workbook displays 3-5 price trajectory curves (Conservative $0.50-$1.00, Moderate $1.00-$3.00, Aggressive $3.00-$10.00, Bitfury floor $0.60) on a single chart
  2. FDV and circulating market cap are calculated at each time point for every scenario
  3. A scenario selector dropdown on the Assumptions tab switches between Conservative/Base/Aggressive and all calculation cells update accordingly
  4. Net supply (gross emission minus buyback-burn) is shown per scenario, with conditional formatting flagging when net supply becomes deflationary
  5. A dual-axis chart overlays price curves with circulating supply over time
**Plans**: 2 plans
Plans:
- [x] 03-01-PLAN.md -- Scenario selector on Assumptions tab + Token Price data table (12 columns, 32 rows)
- [x] 03-02-PLAN.md -- Charts (price scenarios, dual-axis price/supply), conditional formatting, CLI integration

### Phase 4: Fee Transition Crossover Model
**Goal**: Leadership can see exactly when (and under what conditions) fee revenue exceeds emission value, with the crossover shown as a matrix across price and growth scenarios rather than a single misleading point
**Depends on**: Phase 2, Phase 3
**Requirements**: REQ-M2-02, REQ-M2-03, REQ-M2-04, REQ-M2-05, REQ-M2-06, REQ-M2-07, REQ-D02
**Success Criteria** (what must be TRUE):
  1. A 9-cell fee revenue projection matrix (3 growth rates x 3 price scenarios) shows fee revenue at each time point with formulas referencing the Assumptions tab
  2. Crossover points are highlighted with conditional formatting: green cells where fees > emissions, red where fees < emissions
  3. A revenue split waterfall (stacked bar) shows the 70/20/5/5 allocation (Host, AI Fund, Buyback, Yield Pool) at each revenue level
  4. Year 8-12 columns have red "danger zone" shading with annotations explaining the emission cliff risk
  5. A tail emission toggle (ON/OFF boolean on Assumptions) adds 10,000 GNK/day floor emission and all downstream calculations update
  6. Developer count is a visible input row that feeds directly into fee revenue projections
  7. Heat map conditional formatting makes crossover timing visually scannable across the entire matrix
**Plans**: 2 plans
Plans:
- [x] 04-01-PLAN.md -- Parameters, tail emission toggle, and fee transition data model (14 columns, 32 rows, 2 crossover matrices)
- [x] 04-02-PLAN.md -- Charts (waterfall, crossover timeline, fee vs emission), conditional formatting, danger zone

### Phase 5: Host Profitability Model
**Goal**: Leadership can evaluate whether hosting on Gonka is economically competitive with traditional GPU rental under varying prices, network sizes, and cost structures
**Depends on**: Phase 2, Phase 3
**Requirements**: REQ-M3-01, REQ-M3-02, REQ-M3-03, REQ-M3-04, REQ-M3-05, REQ-M3-06, REQ-M3-07, REQ-D01
**Success Criteria** (what must be TRUE):
  1. A stacked area chart shows host income from two sources (mining rewards declining, fee income growing) over the 10-year horizon
  2. Breakeven GNK price is calculated at each time point using `(Host_Cost - Fee_Income) / Daily_GNK_Earned`, with the $0.85-$3.30 reference range visible
  3. A side-by-side comparison shows Gonka income vs Lambda/CoreWeave traditional rental income at each price point
  4. A two-variable sensitivity table shows host ROI across GNK price (rows) and network GPU count (columns) with conditional formatting (green=profitable, red=unprofitable)
  5. Electricity cost sensitivity is modeled at $0.05, $0.08, $0.12/kWh with profitability impact visible per scenario
  6. GPU hardware cost input drives a months-to-breakeven and cumulative ROI calculation
  7. Host churn risk is flagged with red conditional formatting whenever Gonka income drops below traditional rental equivalent
**Plans**: 2 plans
Plans:
- [x] 05-01-PLAN.md -- Parameters, host profitability data model (13 cols x 32 rows), sensitivity matrix, electricity sensitivity, GPU amortization
- [x] 05-02-PLAN.md -- Charts (stacked area, Gonka vs traditional, breakeven price) and conditional formatting (churn risk, sensitivity heat map)

### Phase 6: Treasury & POL Simulation
**Goal**: Leadership can project treasury health across all components (Community Pool, POL, buyback-burn, AI Fund, floor defense) and see when critical depletion thresholds are reached
**Depends on**: Phase 1 (primarily), Phase 3 (for price scenarios)
**Requirements**: REQ-M4-01, REQ-M4-02, REQ-M4-03, REQ-M4-04, REQ-M4-05, REQ-M4-06, REQ-M4-07, REQ-D06
**Success Criteria** (what must be TRUE):
  1. A Community Pool waterfall shows: starting 120M GNK minus POL allocation minus dev grants minus floor defense = remaining per year
  2. POL LP fee revenue projections accept fee tier, utilization, and price range as inputs, with annual revenue and cumulative returns as outputs
  3. Cumulative buyback-burn is shown as a running total of tokens burned and as a percentage of total supply over time
  4. AI Training Fund balance tracks 20% revenue inflows minus expenses minus surplus distribution per period
  5. Floor defense scenarios show treasury balance after X months of active defense at configurable trigger price levels
  6. Net treasury value sums all assets (GNK + USDC + LP positions) in USD at the scenario's GNK price
  7. A clear label states "IL impact not modeled; see v2 for concentrated position risk analysis"
  8. Time-to-X callout cells display key milestones (e.g., "Community Pool depleted in: 8.3 years (Base scenario)")
**Plans**: 2 plans
Plans:
- [x] 06-01-PLAN.md -- Parameters (TREASURY OPERATIONS group) + Treasury data model (14 columns, 32 rows), Time-to-X callouts, defense scenarios, IL caveat
- [x] 06-02-PLAN.md -- Charts (treasury composition, CP depletion, cumulative burn) and conditional formatting (CP health, defense health, net treasury gradient)

### Phase 7: Dashboard & Master Workbook Assembly
**Goal**: A single master workbook links all models via shared assumptions with a dashboard summarizing cross-model KPIs, scenario comparisons, and navigation between the 8-tab structure
**Depends on**: Phase 2, Phase 3, Phase 4, Phase 5, Phase 6
**Requirements**: REQ-M5-01, REQ-M5-02, REQ-M5-03, REQ-M5-04, REQ-M5-05, REQ-U01, REQ-U04, REQ-D05
**Success Criteria** (what must be TRUE):
  1. The master workbook contains exactly 8 tabs in order: Documentation, Assumptions, Emission Schedule, Token Price, Fee Transition, Host Profitability, Treasury & POL, Dashboard
  2. Changing a single assumption on the Assumptions tab causes recalculation across ALL model tabs (no hardcoded values in any calculation tab)
  3. The Dashboard tab displays 6-8 cross-model KPIs with 2-3 summary charts pulling data from each model tab
  4. A scenario comparison matrix shows rows=metrics, columns=scenarios with color coding
  5. A cover/title sheet includes version, date, "For internal decision-making purposes only" disclaimer, and color convention legend
  6. A hyperlinked TOC provides navigation to every tab, with "Back to TOC" links on each tab
  7. Charts include horizontal breakeven reference lines at threshold values ($0.85, $3.30, etc.) where applicable
**Plans**: 2 plans
Plans:
- [x] 07-01-PLAN.md -- Documentation tab (cover sheet, color legend, hyperlinked TOC) and 8-tab workbook structure with navigation links
- [x] 07-02-PLAN.md -- Dashboard tab with 8 KPIs, scenario comparison matrix, 3 summary charts (price bar, breakeven with reference lines, treasury timeline)

### Phase 8: Standalone Workbook Generation
**Goal**: Four focused standalone workbooks can be shared independently, each containing only the relevant model with its own filtered assumptions, documentation, glossary, and scenario controls
**Depends on**: Phase 7
**Requirements**: REQ-U11, REQ-D03, REQ-D07, REQ-D08
**Success Criteria** (what must be TRUE):
  1. Running `python generate.py` produces 5 files: 1 master + 4 standalone workbooks (token price, fee transition, host profitability, treasury & POL)
  2. Each standalone has a filtered Assumptions tab containing ONLY the parameters relevant to that model (not all ~50)
  3. Each standalone includes a Definitions/Glossary tab with alphabetical entries for domain terms (TWAP, veGNK, POL, etc.)
  4. Scenario narratives provide 2-3 sentence plain-English interpretations per scenario per model
  5. What-if toggle switches (buyback-burn Y/N, tail emissions Y/N, deploy POL Y/N) ripple through relevant calculations
  6. Version number and changelog appear on each workbook's cover sheet
**Plans**: 4 plans
Plans:
- [x] 08-01-PLAN.md -- Foundation: toggle parameters, standalone_config.py, build_filtered_assumptions_tab()
- [x] 08-02-PLAN.md -- New tab builders: glossary.py and cover_sheet.py
- [x] 08-03-PLAN.md -- Toggle integration: IF() wrappers in token_price.py and treasury.py
- [x] 08-04-PLAN.md -- Standalone orchestrator and generate.py integration

### Phase 9: Polish, Documentation & Validation
**Goal**: All workbooks meet professional financial modeling standards with cell protection, source audit trails, print-ready layouts, and verified correctness in both Excel and Google Sheets
**Depends on**: Phase 8
**Requirements**: REQ-U09, REQ-U10, REQ-U12, REQ-D04
**Success Criteria** (what must be TRUE):
  1. All formula cells are locked; all input cells are unlocked -- attempting to edit a formula cell in a protected workbook shows a protection warning
  2. Every assumption has a "Source" column entry citing the specific v1.0 research document and recommendation number, plus a confidence level (HIGH/MED/LOW)
  3. Print areas are set on every tab with appropriate page breaks, headers, and footers -- printing any tab produces a readable document
  4. All 5 workbooks open correctly in Google Sheets with no `#NAME?` or `#REF!` errors and all charts render
  5. All 5 workbooks open correctly in Excel with charts displaying proper labels, legends, and formatting
**Plans**: 3 plans
Plans:
- [x] 09-01-PLAN.md -- Source audit enrichment (confidence levels + full citations in parameters.py and workbook_base.py)
- [x] 09-02-PLAN.md -- Cell protection + print layout (print_setup.py utility, generate.py and standalone.py integration)
- [x] 09-03-PLAN.md -- Cross-platform validation and human verification (regenerate all 5 workbooks, add protection notes, Excel + Google Sheets testing)

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1. Foundation & Shared Infrastructure | v1.1 | 2/2 | Complete | 2026-02-05 |
| 2. Emission Schedule Model | v1.1 | 2/2 | Complete | 2026-02-06 |
| 3. Token Price Scenarios Model | v1.1 | 2/2 | Complete | 2026-02-06 |
| 4. Fee Transition Crossover Model | v1.1 | 2/2 | Complete | 2026-02-06 |
| 5. Host Profitability Model | v1.1 | 2/2 | Complete | 2026-02-06 |
| 6. Treasury & POL Simulation | v1.1 | 2/2 | Complete | 2026-02-06 |
| 7. Dashboard & Master Workbook Assembly | v1.1 | 2/2 | Complete | 2026-02-06 |
| 8. Standalone Workbook Generation | v1.1 | 4/4 | Complete | 2026-02-07 |
| 9. Polish, Documentation & Validation | v1.1 | 3/3 | Complete | 2026-02-07 |

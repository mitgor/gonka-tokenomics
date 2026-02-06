# Requirements: v1.1 Economic Modeling

**Milestone:** v1.1 Economic Modeling
**Created:** 2026-02-05
**Source:** Research synthesis (SUMMARY.md, FEATURES.md, ARCHITECTURE.md, PITFALLS.md, STACK.md)

---

## Must Have (v1.1)

### Foundation & Shared Infrastructure

| ID | Requirement | Acceptance Criteria |
|----|-------------|-------------------|
| REQ-F01 | Single `parameters.py` with all ~50 v1.0 research parameters | Every hard-coded number traces to v1.0 research; no constants scattered in model files |
| REQ-F02 | `styles.py` with NamedStyles (currency, percent, header, input, formula) | Consistent formatting across all workbooks; blue=input, black=formula, green=cross-tab |
| REQ-F03 | `workbook_base.py` builds Assumptions tab and returns `param_refs` dict | All model tabs reference Assumptions cells via param_refs; no direct constants in formulas |
| REQ-F04 | CLI entry point (`generate.py`) to generate all workbooks | Single command produces all 5 workbooks in output directory |
| REQ-F05 | openpyxl as sole external dependency | No pandas, numpy, matplotlib, xlwings — stdlib only for computation |

### Universal Workbook Features (All Models)

| ID | Requirement | Acceptance Criteria |
|----|-------------|-------------------|
| REQ-U01 | Cover/title sheet with version, date, disclaimer | "For internal decision-making purposes only" disclaimer present |
| REQ-U02 | Centralized Assumptions tab (blue-shaded inputs) | All inputs on one tab; every formula references this tab only |
| REQ-U03 | 3 named scenarios (Conservative/Base/Aggressive) with cell-driven selector | Changing scenario selector updates all calculations |
| REQ-U04 | Executive summary tab with 3-5 KPIs and 2-3 charts | 1-page summary per model with key metrics |
| REQ-U05 | Color-coded cell convention documented on cover | Blue=input, black=formula, green=cross-tab link |
| REQ-U06 | Consistent number formatting | USD `$#,##0`, percentages `0.0%`, large numbers with commas, units labeled |
| REQ-U07 | Standardized time axis | Monthly for Year 1-2, annual for Year 3-10 |
| REQ-U08 | 2-3 chart visualizations per model | Line for trends, stacked area for composition, bar for comparisons |
| REQ-U09 | Cell protection on formula cells | Formula cells locked, input cells unlocked |
| REQ-U10 | Source references per assumption | "Source" column on Assumptions tab citing v1.0 research doc/rec number |
| REQ-U11 | Definitions/glossary tab | Alphabetical glossary of terms (TWAP, veGNK, POL, etc.) |
| REQ-U12 | Print-friendly layout | Print areas set, page breaks, headers/footers |

### Model 1: Token Price Scenarios

| ID | Requirement | Acceptance Criteria |
|----|-------------|-------------------|
| REQ-M1-01 | 3-5 price trajectories | Conservative ($0.50-$1.00), Moderate ($1.00-$3.00), Aggressive ($3.00-$10.00), Bitfury floor ($0.60) |
| REQ-M1-02 | Market cap calculations | FDV and circulating market cap at each time point per scenario |
| REQ-M1-03 | Circulating supply schedule | Epoch emissions + Community Pool unlocks + founder vesting = circulating per period |
| REQ-M1-04 | Annualized inflation rate | `Annual New Tokens / Circulating Supply` with benchmark comparison labels |
| REQ-M1-05 | Buyback-burn impact on net supply | Gross emission - burns = net supply; flag when net deflationary per scenario |
| REQ-M1-06 | Price x supply chart | Overlay price curves with circulating supply (dual-axis) |

### Model 2: Emission vs Fee Transition

| ID | Requirement | Acceptance Criteria |
|----|-------------|-------------------|
| REQ-M2-01 | Emission decay curve | `323,000 * exp(-0.000475 * epochs)` visualized with closed-form formula |
| REQ-M2-02 | Fee revenue projection matrix | 3 growth rates x 3 price scenarios = 9-cell matrix |
| REQ-M2-03 | Crossover point identification | Conditional formatting: green when fees > emissions, red when fees < emissions |
| REQ-M2-04 | Revenue split waterfall (70/20/5/5) | Stacked bar showing Host share, AI Fund, Buyback, Yield Pool at each revenue level |
| REQ-M2-05 | Danger zone flagging (Year 8-12) | Red shading on danger zone columns with annotation |
| REQ-M2-06 | Tail emission toggle | Boolean on Assumptions: ON/OFF for 10,000 GNK/day tail emission |
| REQ-M2-07 | Developer count as visible driver | Input row for developer count per year feeding into fee revenue |

### Model 3: Host Profitability

| ID | Requirement | Acceptance Criteria |
|----|-------------|-------------------|
| REQ-M3-01 | Dual income breakdown (mining + fees) | Stacked area chart showing emission income declining, fee income growing |
| REQ-M3-02 | Breakeven GNK price per time point | `(Host_Cost - Fee_Income) / Daily_GNK_Earned` with $0.85-$3.30 reference range |
| REQ-M3-03 | Traditional rental comparison | Side-by-side: Gonka income vs Lambda/CoreWeave rental at each price point |
| REQ-M3-04 | Network size sensitivity | Per-host reward at different total network GPU counts |
| REQ-M3-05 | Electricity cost sensitivity | Profitability at $0.05, $0.08, $0.12/kWh |
| REQ-M3-06 | GPU cost amortization | Hardware cost input, months-to-breakeven, cumulative ROI |
| REQ-M3-07 | Host churn risk indicator | Conditional formatting: red when Gonka income < traditional rental |

### Model 4: Treasury & POL Simulation

| ID | Requirement | Acceptance Criteria |
|----|-------------|-------------------|
| REQ-M4-01 | Community Pool depletion schedule | Waterfall: starting 120M - POL - dev grants - floor defense = remaining per year |
| REQ-M4-02 | POL LP fee revenue projection | Fee tier, utilization, price range inputs; annual revenue + cumulative returns |
| REQ-M4-03 | Buyback-burn cumulative impact | Running total tokens burned; shown as % of total supply |
| REQ-M4-04 | AI Training Fund balance | 20% revenue inflows - expenses - surplus distribution = fund balance |
| REQ-M4-05 | Floor defense treasury scenarios | Trigger price inputs; treasury balance after X months of active defense |
| REQ-M4-06 | Net treasury value | Sum all treasury assets in USD at GNK price per scenario |
| REQ-M4-07 | IL caveat (deferred) | Clear label: "IL impact not modeled; see v2 for concentrated position risk analysis" |

### Model 5: Master Unified Workbook

| ID | Requirement | Acceptance Criteria |
|----|-------------|-------------------|
| REQ-M5-01 | Linked assumptions across all sub-models | Single Assumptions tab drives all calculation tabs |
| REQ-M5-02 | Dashboard tab with cross-model KPIs | 6-8 key metrics pulled from each model with charts |
| REQ-M5-03 | Scenario comparison matrix | Rows = metrics, columns = scenarios, color-coded |
| REQ-M5-04 | Navigation (hyperlinked TOC) | TOC tab with hyperlinks; consistent "Back to TOC" links per tab |
| REQ-M5-05 | 8-tab structure | Documentation -> Assumptions -> Emission -> Token Price -> Fee Transition -> Host Profitability -> Treasury & POL -> Dashboard |

---

## Should Have (v1.1 Differentiators)

| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| REQ-D01 | Two-variable sensitivity tables | High | Host breakeven (price x network size); treasury runway (revenue x growth). Static/pre-calculated. |
| REQ-D02 | Conditional formatting heat maps | High | On crossover tables and profitability matrices |
| REQ-D03 | Scenario narratives | Medium | 2-3 sentence plain-English interpretation per scenario per model |
| REQ-D04 | Assumption audit trail | Medium | Source + date + confidence (HIGH/MED/LOW) per assumption |
| REQ-D05 | Breakeven reference lines on charts | Medium | Horizontal lines at threshold values ($0.85, $3.30, etc.) |
| REQ-D06 | Time-to-X calculations | Medium | "Community Pool depleted in 8.3 years" callout cells |
| REQ-D07 | What-if toggle switches | Medium | Buyback-burn Y/N, tail emissions Y/N, deploy POL Y/N |
| REQ-D08 | Version number and changelog on cover | Low | Track model evolution |

---

## Deferred to v2+

| ID | Feature | Reason |
|----|---------|--------|
| DEF-01 | Impermanent loss modeling | V3 concentrated liquidity IL math is complex; wrong estimate worse than none |
| DEF-02 | Tornado charts | Complex to implement in openpyxl; limited value vs sensitivity tables |
| DEF-03 | Competitive benchmark overlays | Requires additional research data beyond v1.0 |
| DEF-04 | Cross-model consistency checks | Implement after models stabilize |

---

## Out of Scope (Never Build)

| Feature | Reason |
|---------|--------|
| Monte Carlo / stochastic simulation | Leadership needs deterministic scenario comparison |
| Live API price feeds | Non-reproducible; breaks when APIs change |
| VBA macros | Not supported by openpyxl; breaks Google Sheets |
| Pivot tables | Not supported by openpyxl; requires user interaction |
| Interactive dashboards | Spreadsheets are the delivery format |
| Named ranges | Industry anti-pattern; debugging complexity; openpyxl limitations |
| Multiple fonts / decorative formatting | Single font (Calibri 10pt), minimal design |
| Embedded images / logos | Text-only branding |

---

## Technical Constraints

| Constraint | Detail |
|------------|--------|
| Stack | Python 3.10+ with openpyxl only (no pandas, numpy, matplotlib) |
| Computation | `math.exp()` for decay, `decimal.Decimal` for precision, stdlib only |
| Formula approach | Python writes Excel formulas (not computed values); workbooks self-calculate |
| Compatibility | Must work in Excel and Google Sheets |
| File size | Under 5MB per workbook (Google Sheets limit) |
| Granularity | Monthly Year 1-2, annual Year 3-10 |

---

## Key Risks & Mitigations

| Risk | Severity | Mitigation |
|------|----------|------------|
| Reflexivity trap (price as input/output) | Critical | Scenario consistency checks; label every price-dependent output |
| Exponential decay precision | Critical | `decimal.Decimal('0.000475')`; closed-form formula; validation row |
| openpyxl formulas not cached | Critical | Restrict to common formula subset; test in Google Sheets |
| openpyxl chart bugs (3.1.4+) | Moderate | Start 3.1.5, test charts, downgrade to 3.1.3 if needed |
| Hardcoded assumptions scattered | Moderate | Single `parameters.py`; Wall Street color coding |

---

## Requirement Count

- **Must Have:** 49 requirements (5 foundation + 12 universal + 6 model 1 + 7 model 2 + 7 model 3 + 7 model 4 + 5 model 5)
- **Should Have:** 8 differentiators
- **Deferred:** 4 items
- **Out of Scope:** 8 anti-features

---

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| REQ-F01 | Phase 1: Foundation & Shared Infrastructure | Done |
| REQ-F02 | Phase 1: Foundation & Shared Infrastructure | Done |
| REQ-F03 | Phase 1: Foundation & Shared Infrastructure | Done |
| REQ-F04 | Phase 1: Foundation & Shared Infrastructure | Done |
| REQ-F05 | Phase 1: Foundation & Shared Infrastructure | Done |
| REQ-U01 | Phase 7: Dashboard & Master Workbook Assembly | Pending |
| REQ-U02 | Phase 1: Foundation & Shared Infrastructure | Done |
| REQ-U03 | Phase 3: Token Price Scenarios Model | Done |
| REQ-U04 | Phase 7: Dashboard & Master Workbook Assembly | Pending |
| REQ-U05 | Phase 1: Foundation & Shared Infrastructure | Done |
| REQ-U06 | Phase 1: Foundation & Shared Infrastructure | Done |
| REQ-U07 | Phase 2: Emission Schedule Model | Done |
| REQ-U08 | Phase 2: Emission Schedule Model | Done |
| REQ-U09 | Phase 9: Polish, Documentation & Validation | Pending |
| REQ-U10 | Phase 9: Polish, Documentation & Validation | Pending |
| REQ-U11 | Phase 8: Standalone Workbook Generation | Pending |
| REQ-U12 | Phase 9: Polish, Documentation & Validation | Pending |
| REQ-M1-01 | Phase 3: Token Price Scenarios Model | Done |
| REQ-M1-02 | Phase 3: Token Price Scenarios Model | Done |
| REQ-M1-03 | Phase 2: Emission Schedule Model | Done |
| REQ-M1-04 | Phase 2: Emission Schedule Model | Done |
| REQ-M1-05 | Phase 3: Token Price Scenarios Model | Done |
| REQ-M1-06 | Phase 3: Token Price Scenarios Model | Done |
| REQ-M2-01 | Phase 2: Emission Schedule Model | Done |
| REQ-M2-02 | Phase 4: Fee Transition Crossover Model | Done |
| REQ-M2-03 | Phase 4: Fee Transition Crossover Model | Done |
| REQ-M2-04 | Phase 4: Fee Transition Crossover Model | Done |
| REQ-M2-05 | Phase 4: Fee Transition Crossover Model | Done |
| REQ-M2-06 | Phase 4: Fee Transition Crossover Model | Done |
| REQ-M2-07 | Phase 4: Fee Transition Crossover Model | Done |
| REQ-M3-01 | Phase 5: Host Profitability Model | Done |
| REQ-M3-02 | Phase 5: Host Profitability Model | Done |
| REQ-M3-03 | Phase 5: Host Profitability Model | Done |
| REQ-M3-04 | Phase 5: Host Profitability Model | Done |
| REQ-M3-05 | Phase 5: Host Profitability Model | Done |
| REQ-M3-06 | Phase 5: Host Profitability Model | Done |
| REQ-M3-07 | Phase 5: Host Profitability Model | Done |
| REQ-M4-01 | Phase 6: Treasury & POL Simulation | Done |
| REQ-M4-02 | Phase 6: Treasury & POL Simulation | Done |
| REQ-M4-03 | Phase 6: Treasury & POL Simulation | Done |
| REQ-M4-04 | Phase 6: Treasury & POL Simulation | Done |
| REQ-M4-05 | Phase 6: Treasury & POL Simulation | Done |
| REQ-M4-06 | Phase 6: Treasury & POL Simulation | Done |
| REQ-M4-07 | Phase 6: Treasury & POL Simulation | Done |
| REQ-M5-01 | Phase 7: Dashboard & Master Workbook Assembly | Pending |
| REQ-M5-02 | Phase 7: Dashboard & Master Workbook Assembly | Pending |
| REQ-M5-03 | Phase 7: Dashboard & Master Workbook Assembly | Pending |
| REQ-M5-04 | Phase 7: Dashboard & Master Workbook Assembly | Pending |
| REQ-M5-05 | Phase 7: Dashboard & Master Workbook Assembly | Pending |
| REQ-D01 | Phase 5: Host Profitability Model | Done |
| REQ-D02 | Phase 4: Fee Transition Crossover Model | Done |
| REQ-D03 | Phase 8: Standalone Workbook Generation | Pending |
| REQ-D04 | Phase 9: Polish, Documentation & Validation | Pending |
| REQ-D05 | Phase 7: Dashboard & Master Workbook Assembly | Pending |
| REQ-D06 | Phase 6: Treasury & POL Simulation | Done |
| REQ-D07 | Phase 8: Standalone Workbook Generation | Pending |
| REQ-D08 | Phase 8: Standalone Workbook Generation | Pending |

---
*Generated from v1.1 research synthesis on 2026-02-05*

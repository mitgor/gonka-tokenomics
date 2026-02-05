# Feature Landscape: Tokenomics Economic Modeling Workbooks

**Domain:** Financial modeling spreadsheets for crypto tokenomics (leadership-facing)
**Researched:** 2026-02-05
**Context:** 4 model areas + master unified model, generated as .xlsx via Python/openpyxl, targeting Gonka founders/leadership

---

## Table Stakes: Universal (All Workbooks)

Features leadership expects in any professional financial model. Missing any of these makes the model feel amateur or untrustworthy.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| **Cover/title sheet** with project name, version, date, disclaimer | First impression; signals professionalism | Low | Include "For internal decision-making purposes only" disclaimer |
| **Assumptions sheet** (separated from calculations) | Leadership needs to see what drives the numbers; core financial modeling standard | Low | All inputs blue-shaded, all formulas black. Every hard-coded number lives here. |
| **3 named scenarios** (Conservative / Base / Aggressive) | Leadership thinks in scenarios, not point estimates. Single-number models feel naive. | Medium | Use a scenario selector (cell-driven switch) that ripples through all calculations |
| **Executive summary tab** with key metrics and charts | Leadership reads summary first, digs into detail only if needed | Medium | 1-page printable: 3-5 KPIs, 2-3 charts, headline conclusion per scenario |
| **Color-coded cell convention** (inputs vs formulas) | Industry standard for auditability -- blue = input, black = formula, green = linked from another sheet | Low | Document the convention on the cover sheet |
| **Number formatting** (consistent currency, percentages, commas) | Sloppy formatting destroys credibility instantly | Low | USD with `$#,##0` or `$#,##0.00`, percentages with `0.0%`, large numbers with commas |
| **Time axis** (epoch/month/year columns) | All models are time-series; leadership needs to see evolution, not snapshots | Low | Standardize: monthly for Year 1-2, annual for Year 3-10 |
| **Chart visualizations** (at least 2-3 per model) | Numbers alone are insufficient for pattern recognition | Medium | Line charts for trends, stacked area for composition, bar for comparisons |
| **Print-friendly layout** | Leadership may print or export to PDF for board meetings | Low | Set print areas, page breaks, headers/footers |
| **Cell protection** on formula cells | Prevents accidental formula overwrites when leadership tweaks inputs | Low | Lock all formula cells, leave input cells unlocked |
| **Source references** per assumption | Leadership asks "where did this number come from?" for every key assumption | Low | Add a "Source" column next to each assumption (e.g., "v1.0 Research, Rec #2") |
| **Units labeled** on every column/row | Ambiguity about "is this GNK or USD?" erodes trust | Low | Always label: GNK, USD, %, GNK/day, USD/yr, etc. |
| **Definitions tab** | Non-technical leadership needs term definitions (TWAP, veGNK, POL, EIP-1559, etc.) | Low | Alphabetical glossary, keep concise |

---

## Table Stakes: Per-Model

### Model 1: Token Price Scenarios

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| **Multiple price trajectories** (3-5 curves) | Leadership wants to see bear/base/bull, not a single optimistic line | Medium | Conservative ($0.50-$1.00), Moderate ($1.00-$3.00), Aggressive ($3.00-$10.00), plus "Bitfury floor" ($0.60 flat) |
| **Market cap calculations** at each price point | Leadership thinks in market cap, not just price. "At $3 GNK, what's our FDV?" | Low | `Price x Circulating Supply` and `Price x Total Supply` side by side |
| **Circulating supply schedule** over time | Price without supply context is meaningless -- leadership needs to see dilution | Medium | Epoch emissions + Community Pool unlocks + founder vesting = circulating at each time point |
| **Inflation rate** (annualized) at each time point | Leadership compares inflation to ETH, BTC, SOL as mental benchmarks | Low | `Annual New Tokens / Current Circulating Supply` |
| **Buyback-burn impact** on net supply | With 5% revenue going to burns, leadership needs to see net issuance vs gross | Medium | Gross emission - burns = net supply change. Show when net deflationary under each scenario. |
| **Price x supply crossover chart** | The single most important visual: when does FDV reach $X under each scenario | Medium | Overlay price curves with circulating supply on dual-axis chart |

### Model 2: Emission vs Fee Transition

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| **Emission decay curve** (epochs to years) | Core of the transition story -- when do emissions become negligible? | Low | Already have formula: `323,000 * exp(-0.000475 * epochs)`. Visualize it. |
| **Fee revenue projection** under each growth scenario | The "other half" of the transition -- when does fee revenue compensate for declining emissions? | Medium | 3 dev growth rates (10%, 25%, 50%) x 3 price scenarios = 9-cell matrix |
| **Crossover point identification** (highlighted) | The moment fee revenue exceeds emission value is THE key decision point | Medium | Conditional formatting: green when fees > emissions, red when fees < emissions |
| **Revenue split waterfall** (70/20/5/5) | Leadership needs to see where money flows at each revenue level | Medium | Stacked bar or waterfall chart: Host share, AI Fund, Buyback, Yield Pool |
| **"Danger zone" flagging** (Year 8-12) | Research identifies Year 8-12 as critical when emissions are negligible but fees may not dominate | Low | Red shading or border on the danger zone columns with annotation |
| **Tail emission contingency** toggle | Leadership needs to model "what if we activate tail emissions?" | Medium | Boolean toggle on assumptions sheet: ON/OFF for 10,000 GNK/day tail emission |
| **Developer count assumptions** as driver | Fee revenue is a function of developer growth -- make this visible and adjustable | Low | Input row showing developer count per year, feeding into fee revenue calculation |

### Model 3: Host Profitability

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| **Dual income breakdown** (mining rewards + work fees) | Hosts earn from two sources; leadership needs to see relative contribution over time | Medium | Stacked area chart: emission income declining, fee income growing |
| **Breakeven GNK price** at each time point | "What price does GNK need to be for hosts to be profitable?" is the #1 host question | Medium | `(Host_Cost - Fee_Income) / Daily_GNK_Earned` = breakeven price. Already have $0.85-$3.30 range. |
| **Traditional rental comparison** ($/hr equivalence) | Leadership compares to "what if hosts just rented GPUs on Lambda/CoreWeave?" | Low | Side-by-side: Gonka income vs traditional rental income at each price point |
| **Network size sensitivity** (hosts x GPUs) | More hosts = less reward per host. Model needs to show dilution. | Medium | Input for total network GPUs, shows per-host reward at different network sizes |
| **Electricity cost sensitivity** | Electricity is 75-85% of operating costs -- small changes flip profitability | Low | Input for $/kWh, show profitability at $0.05, $0.08, $0.12/kWh |
| **GPU cost amortization** | H100 costs $25-40K; hosts need to see payback period | Medium | Input for hardware cost, show months-to-breakeven and cumulative ROI |
| **Host churn risk indicator** | When profitability index drops below 1.0x, hosts leave. Model this threshold. | Low | Conditional formatting: red when Gonka income < traditional rental |

### Model 4: Treasury & POL Simulation

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| **Community Pool depletion schedule** | 120M GNK pool with planned outflows (POL, dev grants, floor defense). When does it run out? | Medium | Waterfall: starting balance - POL allocation - dev grants - floor defense = remaining per year |
| **POL LP fee revenue projection** | 22M GNK deployed, $550K-$1.1M annual fees expected. Model across scenarios. | Medium | Input for fee tier, utilization, price range. Output: annual revenue, cumulative returns. |
| **Impermanent loss estimation** | Leadership needs to understand POL downside. IL is the #1 concern. | High | Model IL at different price movements: +-25%, +-50%, +-75% from deployment price |
| **Buyback-burn cumulative impact** | 5% of revenue to burns. Show cumulative tokens burned over 10 years. | Medium | Running total: tokens purchased and burned each period. Show as % of total supply. |
| **AI Training Fund balance** with surplus mechanism | Fund at 20% of revenue, surplus above 6-month runway distributed. Track balance. | Medium | Inflows (20% revenue) - outflows (expenses) - surplus distribution = fund balance |
| **Floor defense treasury** depletion scenarios | $2-5M USDC target. Model trigger activations and spend-down. | Medium | Inputs for trigger price levels. Output: treasury balance after X months of defense. |
| **Net treasury value** (GNK + USDC + LP positions) | Single number: "what is the protocol worth on its balance sheet?" | Medium | Sum of all treasury assets in USD at current GNK price per scenario |

### Model 5: Master Unified Workbook

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| **Linked assumptions** across all sub-models | Change GNK price once, all models update. This is the whole point of a master model. | High | Single assumptions tab drives all calculations via cell references |
| **Dashboard tab** with cross-model KPIs | Leadership needs the "one page" that summarizes everything | High | 6-8 key metrics pulled from each sub-model, with sparkline charts |
| **Scenario comparison matrix** | "Show me conservative vs aggressive side by side for ALL models" | Medium | Summary table: rows = metrics, columns = scenarios. Color-coded. |
| **Waterfall: token flow from supply to sinks** | The full token lifecycle: emission -> circulation -> staking/burning/treasury | High | Visual showing where tokens are at each time point across all categories |
| **Navigation** (hyperlinked table of contents) | 10+ tabs is disorienting without navigation | Low | TOC tab with hyperlinks to each sheet. Consistent "Back to TOC" links. |

---

## Differentiators

Features that elevate the model from "functional" to "trustworthy and genuinely useful." These separate professional-grade models from hobby projects.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| **Two-variable sensitivity tables** | Show how any output changes across two input variables simultaneously. E.g., "Host ROI at different GNK prices AND network sizes" | Medium | Use Excel Data Table format (row input + column input). 5-7 values per axis = 25-49 cell grid. Conditionally format green/yellow/red. |
| **Conditional formatting heat maps** | Instantly see where problems are. Green = healthy, red = danger. | Medium | Apply to crossover tables, profitability matrices, treasury balances. More informative than raw numbers. |
| **Tornado chart** (sensitivity ranking) | Shows which single variable has the biggest impact on a key output. Answers "what matters most?" | Medium | Rank variables by impact on host profitability or treasury runway. Leadership loves these for prioritization. |
| **Scenario narrative** on each summary tab | A 2-3 sentence plain-English interpretation of what the numbers mean under each scenario | Low | E.g., "Under conservative growth, host breakeven price reaches $3.30 by Year 6, making the network uncompetitive without tail emissions." |
| **Assumption audit trail** (source + date + confidence) | Each assumption cites its source document, research date, and confidence level (HIGH/MEDIUM/LOW) | Low | Extra columns on assumptions tab. Dramatically increases trust with technical leadership. |
| **Breakeven lines on charts** | Horizontal reference lines showing thresholds (breakeven price, profitability floor, danger zones) | Low | E.g., horizontal line at $0.85 GNK on host profitability chart with label "Host breakeven floor" |
| **Time-to-X calculations** | "How many months until Community Pool is depleted?" "When does fee revenue exceed $100M?" | Low | Clear callout cells: "Community Pool depleted in: 8.3 years (Base scenario)" |
| **Cross-model consistency checks** | Automated checks that verify inputs match across models (e.g., total supply in Model 1 = total supply in Model 4) | Medium | A hidden "Checks" tab with TRUE/FALSE flags. Surface any FALSE on the dashboard. |
| **Print-optimized chart formatting** | Charts that look professional in black-and-white print (patterns, not just colors) | Low | Use distinct line styles (solid, dashed, dotted) in addition to colors. Label directly on chart lines, not just legend. |
| **Version number and changelog** | Track model evolution. "v1.1 added tail emission toggle per leadership feedback" | Low | Small changelog on cover sheet. Builds institutional memory. |
| **Competitive benchmarks** embedded in charts | Show Gonka metrics alongside Akash, Render, Bittensor, ETH inflation rates | Low | Reference lines or secondary data series. E.g., "ETH inflation: ~0.5%/yr" as benchmark on Gonka inflation chart. |
| **What-if toggle switches** for policy decisions | Boolean inputs: "Enable buyback-burn? Y/N", "Activate tail emissions? Y/N", "Deploy POL? Y/N" | Medium | Each toggle ripples through the model. Leadership can "turn on" recommendations one at a time to see impact. |

---

## Anti-Features

Features to explicitly NOT build. Common mistakes in financial modeling that waste effort or actively harm the model's credibility and usability.

| Anti-Feature | Why Avoid | What to Do Instead |
|--------------|-----------|-------------------|
| **Monte Carlo / stochastic simulation** | Already out of scope per PROJECT.md. Deterministic scenarios are what leadership needs for decision-making. Probability distributions confuse non-technical audiences. | Use 3-5 named deterministic scenarios. Leadership needs "if X then Y," not "there's a 73% chance of Z." |
| **Live API price feeds** | Breaks the model when APIs change or are offline. Creates dependency management overhead. Makes the model non-reproducible ("it showed different numbers yesterday"). | Hard-code current prices as inputs. The point is scenario analysis, not live tracking. |
| **Named ranges for cells** | Seems helpful but creates phantom references that are nearly impossible to debug. Industry anti-pattern confirmed by ICAEW and Wall Street Prep. | Use standard cell references (e.g., `Assumptions!B12`) with clear column/row labels. |
| **Overly complex formulas** (>half the formula bar) | Long formulas are unauditable. Leadership will not trust numbers they cannot trace. Errors hide in complexity. | Break complex calculations into intermediate rows. Each row does one step. More rows is better than fewer clever formulas. |
| **Hard-coded constants inside formulas** | The classic financial modeling sin. Someone buries `0.05` in a formula instead of referencing the assumptions sheet. Changes get missed. | EVERY number lives on the assumptions sheet. Formulas only reference cells, never contain literal numbers (except 0 and 1). |
| **Circular references** | Some modelers use circular references for iterative calculations (e.g., interest on debt that affects cash that affects debt). Excel handles them poorly and they confuse users. | Use previous-period values to break circularity. Slightly less "accurate" but vastly more reliable and understandable. |
| **VBA macros** | Not supported in openpyxl-generated files. Also: macros trigger security warnings in Excel, break in Google Sheets, and are a maintenance nightmare. | Use Excel-native formulas (IF, CHOOSE, INDEX/MATCH) and openpyxl-generated structure. |
| **Too many scenarios** (>5) | Analysis paralysis. Every additional scenario dilutes attention. Leadership needs 3 clear choices, not 12 permutations. | 3 primary scenarios (Conservative/Base/Aggressive) + 1-2 special scenarios (e.g., "Bear market + tail emissions"). Max 5. |
| **Precise decimal places on projections** | Showing "$127,432,891.47" for a Year 5 projection implies false precision. Nobody knows Year 5 revenue to 11 significant digits. | Round to thousands or millions for projections beyond Year 1. Display as "$127.4M" not "$127,432,891.47". Use `$#,##0,K` or `$#,##0,,M` formatting. |
| **Pivot tables / dynamic features** | openpyxl has limited pivot table support. Even if possible, pivot tables require user interaction that breaks the "print and read" workflow. | Pre-calculate all summary views as static tables. Build the pivots into the Python generation logic. |
| **Multiple fonts / decorative formatting** | Every font change, gradient, or decorative element reduces the professional feel. Wall Street models use ONE font. | Single font (Calibri 10pt or Arial 10pt). Bold for headers only. Minimal borders. Let the data speak. |
| **Embedding images / logos** | Adds file size, breaks formatting on different screen sizes, distracts from data. | Text-only branding on cover sheet. Professional models are clean and minimal. |
| **Real-time dashboards / interactivity** | Already out of scope. Spreadsheets are not dashboards. Trying to make them interactive leads to fragile, unmaintainable models. | Static, well-designed charts that tell the story. If dashboards are needed later, that is a separate product. |

---

## Feature Dependencies

```
Assumptions Sheet (all models)
  |
  +---> Model 1: Token Price Scenarios
  |       |-- Circulating supply schedule
  |       |-- Price trajectories
  |       +-- Market cap calculations
  |
  +---> Model 2: Emission vs Fee Transition
  |       |-- Emission decay curve (from supply schedule)
  |       |-- Fee revenue projections (from dev growth assumptions)
  |       +-- Crossover analysis
  |
  +---> Model 3: Host Profitability
  |       |-- Mining rewards (from emission curve)
  |       |-- Fee income (from fee projections)
  |       |-- Traditional rental comparison
  |       +-- Breakeven calculations
  |
  +---> Model 4: Treasury & POL Simulation
  |       |-- Community Pool outflows
  |       |-- POL LP revenue (linked to price scenarios)
  |       |-- Buyback-burn (linked to fee revenue)
  |       +-- Floor defense spend
  |
  +---> Model 5: Master Unified
          |-- Links to all 4 models above
          |-- Dashboard (pulls KPIs from each)
          |-- Scenario comparison matrix
          +-- Consistency checks
```

**Key dependency insight:** Models 2, 3, and 4 all depend on the emission schedule from Model 1 and the fee revenue projection from Model 2. Build Model 1 and 2 first, then 3 and 4 can be parallelized, then the Master model links everything.

---

## MVP Recommendation

For the first deliverable, prioritize features that create the most decision-making value with the least implementation risk.

### Must-Have for First Release

1. **All table-stakes universal features** (assumptions sheet, 3 scenarios, color coding, number formatting, units, source references)
2. **Model 1: Token Price Scenarios** with circulating supply, 3 price trajectories, market cap, inflation rate
3. **Model 2: Emission vs Fee Transition** with crossover analysis, danger zone flagging, revenue waterfall
4. **Model 3: Host Profitability** with dual income breakdown, breakeven price, traditional rental comparison
5. **Model 4: Treasury & POL** with Community Pool depletion, POL revenue, buyback-burn cumulative
6. **Master: Dashboard tab** with linked assumptions and cross-model KPIs
7. **Sensitivity tables** (two-variable) for the highest-leverage decisions: host breakeven (price x network size) and treasury runway (revenue x growth rate)
8. **Conditional formatting** on crossover tables and profitability matrices

### Defer to Post-First-Release

- **Tornado charts** (nice-to-have, complex to implement in openpyxl)
- **Impermanent loss modeling** (high complexity, requires concentrated liquidity math)
- **Competitive benchmark overlays** (requires additional research data)
- **What-if toggle switches** for individual policy decisions (adds complexity to formula structure)
- **Cross-model consistency checks** (implement after models stabilize)

### Never Build

- Monte Carlo simulation
- Live API feeds
- VBA macros
- Pivot tables
- Interactive dashboards

---

## Specific Gonka Parameters That Must Be Modelable

These are the specific numbers from v1.0 research that leadership will want to adjust. Every one must be an input cell on the assumptions sheet, not hard-coded in formulas.

| Parameter | Default Value | Source | Used In |
|-----------|--------------|--------|---------|
| Initial epoch reward | 323,000 GNK/day | Whitepaper | Models 1, 2, 3 |
| Emission decay rate | -0.000475 per epoch | Whitepaper | Models 1, 2, 3 |
| Total supply | 1,000,000,000 GNK | Whitepaper | All models |
| Mining allocation | 680,000,000 GNK | Whitepaper | Models 1, 2 |
| Community Pool | 120,000,000 GNK | Whitepaper | Model 4 |
| Founder allocation | 200,000,000 GNK | Whitepaper | Model 1 |
| Revenue split: hosts | 70% | Rec #3 | Models 2, 3 |
| Revenue split: AI Fund | 20% | Rec #3 | Model 4 |
| Revenue split: buyback-burn | 5% | Rec #3 | Models 1, 4 |
| Revenue split: veGNK yield | 5% | Rec #3 | Model 4 |
| POL allocation | 22,000,000 GNK | Rec #2 | Model 4 |
| POL GNK/USDC split | 60% | Rec #2 | Model 4 |
| POL fee tier | 0.3% | Rec #2 | Model 4 |
| Expected LP fee revenue | $550K-$1.1M/yr | Rec #2 | Model 4 |
| Developer count (initial) | 2,200 | Network data | Models 2, 3 |
| Developer growth rates | 10%, 25%, 50% annual | Rec #4 | Model 2 |
| Host count (initial) | 448 | Network data | Model 3 |
| GPU count (initial) | 6,000 H100-eq | Network data | Model 3 |
| GPU pricing H100 current | $2.00-$2.50/hr | Rec #5 | Model 3 |
| GPU annual price deflation | 30-50% | Research | Model 3 |
| Electricity cost range | $0.05-$0.12/kWh | Industry | Model 3 |
| H100 hardware cost | $25,000-$40,000 | Market data | Model 3 |
| Tail emission rate (contingency) | 10,000 GNK/day | Rec #1 | Models 2, 3 |
| Floor defense trigger | 75% of 30-day TWAP | Rec #7 | Model 4 |
| Floor defense treasury target | $2-5M USDC | Rec #7 | Model 4 |
| Bitfury Schelling point | $0.60 | Strategic data | Models 1, 4 |
| veGNK lock rate (expected) | 35-50% | Rec #6 | Model 1 |
| Governance quorum | 33.4% | Whitepaper | Definitions only |

---

## openpyxl Feature Feasibility

Features confirmed available in openpyxl (verified via official documentation):

| Feature | openpyxl Support | Confidence | Notes |
|---------|-----------------|------------|-------|
| Conditional formatting (cell rules) | Full support | HIGH | CellIsRule, ColorScaleRule, DataBarRule, IconSetRule |
| Color-coded cells (fill, font) | Full support | HIGH | PatternFill for backgrounds, Font for text color |
| Charts (line, bar, area, scatter) | Full support | HIGH | LineChart, BarChart, AreaChart, ScatterChart |
| Dual-axis charts | Supported | HIGH | Secondary y-axis via series assignment |
| Number formatting | Full support | HIGH | cell.number_format = '$#,##0' etc. |
| Cell protection / sheet protection | Full support | HIGH | worksheet.protection, cell.protection |
| Data validation (dropdowns) | Full support | HIGH | DataValidation class with list type |
| Merged cells | Full support | HIGH | worksheet.merge_cells() |
| Hyperlinks | Full support | HIGH | cell.hyperlink |
| Print settings | Full support | HIGH | worksheet.print_area, page_setup |
| Freeze panes | Full support | HIGH | worksheet.freeze_panes |
| Column width / row height | Full support | HIGH | worksheet.column_dimensions |
| Named styles | Full support | HIGH | NamedStyle for reusable formatting |
| Data tables (What-If) | NOT supported | HIGH | Must pre-calculate in Python and output as static grid |
| Pivot tables | NOT supported | HIGH | Must pre-calculate in Python and output as static tables |
| Sparklines | NOT supported | HIGH | Use small embedded charts instead |
| VBA macros | NOT supported | HIGH | Not applicable; excluded as anti-feature |

**Key constraint:** Excel's native Data Table (What-If Analysis) feature cannot be generated by openpyxl. Sensitivity tables must be pre-calculated in Python and written as static formatted grids. This is actually an advantage -- the spreadsheet works identically in Google Sheets since it contains no Excel-specific compute features.

---

## Sources

- [InnMind Tokenomics Spreadsheet Template](https://innmind.com/downloads/tokenomics-spreadsheet/) -- Feature reference for tokenomics models
- [Foresight Token Distribution Model](https://foresight.is/token-distribution-model/) -- Model structure reference
- [FMI Financial Modeling Best Practices](https://fminstitute.com/modeling-resources/financial-modeling-best-practices/) -- Professional Excel standards
- [ICAEW Financial Modelling Code](https://www.icaew.com/-/media/corporate/files/technical/technology/excel/financial-modelling-code.ashx) -- Industry standards for model governance
- [Wall Street Prep: Sensitivity Analysis](https://www.wallstreetprep.com/knowledge/financial-modeling-techniques-sensitivity-what-if-analysis-2/) -- Two-variable data table best practices
- [DataCamp: Sensitivity Analysis Tutorial](https://www.datacamp.com/tutorial/sensitivity-analysis-in-excel) -- Practical implementation guidance
- [openpyxl Conditional Formatting Docs](https://openpyxl.readthedocs.io/en/3.1/formatting.html) -- Feature verification
- [Fortress Accounting: Tokenomics Financial Modeling](https://fortress-accounting.com/tokenomics-financial-modeling-web3-startups/) -- Web3 modeling best practices
- [Black Tokenomics: Monte Carlo in Tokenomics](https://blacktokenomics.com/monte-carlo-simulation-in-tokenomics/) -- Advanced simulation reference (excluded from scope)
- Gonka v1.0 Research: Fine-Tuning Recommendations (10 recommendations with specific parameters)
- Gonka v1.0 Research: Macro-Economic Research Synthesis v2.0
- Gonka v1.0 Research: Deep Tokenomics Analysis v3.0

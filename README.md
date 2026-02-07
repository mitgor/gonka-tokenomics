# Gonka Tokenomics

Economic modeling suite for the Gonka Network -- a decentralized AI infrastructure platform with ~98% productive compute and Sprint Consensus (2.3B-parameter Transformer-based PoW).

Generates **5 Excel workbooks** (1 master + 4 standalone) that model token emission, price scenarios, fee transition, host profitability, and treasury operations over a 10-year horizon. Built for Gonka leadership, investors, and economic stakeholders.

---

## Quick Start

```bash
pip install -r requirements.txt
python generate.py
```

Output: 5 `.xlsx` files in `output/`.

To generate a minimal test workbook (Assumptions tab only):

```bash
python generate.py --test
```

**Dependency:** Python 3.x + `openpyxl==3.1.5` (sole dependency).

---

## Workbooks

### Master Workbook

**`gonka_master_model.xlsx`** -- Complete model with all 5 economic models, executive dashboard, and full parameter set.

| Tab | Description |
|-----|-------------|
| Documentation | Cover sheet with table of contents and tab descriptions |
| Assumptions | All 70 input parameters, scenario selector, and what-if toggles |
| Emission Schedule | Mining reward decay curve and circulating supply over 10 years |
| Token Price | Multi-scenario price trajectories (Conservative/Base/Aggressive) and market cap |
| Fee Transition | Fee revenue vs. mining emission crossover analysis |
| Host Profitability | GPU host economics, income composition, and breakeven analysis |
| Treasury & POL | Community Pool, protocol-owned liquidity, buyback-burn, and floor defense |
| Dashboard | 8 cross-model KPIs, 3-scenario comparison matrix, and summary charts |

### Standalone Workbooks

Each standalone contains only the model tabs needed for its analysis, plus dedicated Documentation, Assumptions (filtered to relevant parameters), and Definitions tabs.

| Workbook | Tabs | Use Case |
|----------|------|----------|
| `gonka_token_price.xlsx` | 5 | Token price scenarios and market cap projections |
| `gonka_fee_transition.xlsx` | 6 | When fee revenue overtakes mining emission |
| `gonka_host_profitability.xlsx` | 7 | GPU host ROI, breakeven price, and churn risk |
| `gonka_treasury_pol.xlsx` | 7 | Community Pool runway, POL returns, buyback-burn impact |

---

## How to Use the Workbooks

This section is a hands-on guide for non-technical users opening the workbooks in Excel or Google Sheets.

### Opening and Navigating

- Open any `.xlsx` file from the `output/` folder.
- The **Documentation** tab (first tab) contains a table of contents with clickable links to every other tab.
- Each model tab has a **"Back to Documentation"** hyperlink in the top-right corner for easy navigation.

### Changing Scenarios

On the **Assumptions** tab, find the **Scenario Selector** section:

1. Click the **Active Scenario** cell (blue background).
2. Choose from the dropdown: **Conservative**, **Base**, or **Aggressive**.
3. The entire workbook recalculates automatically -- all price projections, fee estimates, host income, treasury balances, and dashboard KPIs update to reflect the selected scenario.

### What-If Toggles

Three toggles on the Assumptions tab let you model alternative futures:

| Toggle | Values | Effect |
|--------|--------|--------|
| **Buyback-Burn Active** | Y / N | Enables or disables the buyback-burn mechanism across all models |
| **Deploy POL Active** | Y / N | Enables or disables protocol-owned liquidity deployment from the Community Pool |
| **Tail Emission Toggle** | ON / OFF | When ON, enforces a 10,000 GNK/day emission floor to prevent mining rewards from reaching zero |

Change any toggle and all downstream tabs recalculate instantly.

### Reading the Dashboard

The Dashboard tab (master workbook only) provides an at-a-glance summary:

**8 Key Performance Indicators** (Year 10, active scenario):

| KPI | Source |
|-----|--------|
| Year 10 Circulating Supply | Emission Schedule |
| Year 10 Active GNK Price | Token Price |
| Year 10 Circ. Market Cap | Token Price |
| Year 10 Fee/Emission Ratio | Fee Transition |
| Year 10 Host Net Monthly Income | Host Profitability |
| Year 10 Net Treasury Value | Treasury & POL |
| Cumulative Buyback Burn (% Supply) | Treasury & POL |
| Host Churn Risk Periods (Total) | Host Profitability |

Below the KPIs, a **Scenario Comparison Matrix** shows 6 metrics side-by-side across Conservative/Base/Aggressive scenarios with color-coded cells (red-yellow-green).

### Cell Conventions

| Cell Color | Meaning |
|------------|---------|
| Blue background, dark blue text | **Input** -- editable by the user |
| Black text, no fill | **Formula** -- calculated automatically |
| Green text | **Cross-tab reference** -- pulls data from another sheet |
| Red text, light red fill | **Warning** -- flags danger zones (e.g., churn risk) |

### Cell Protection

All cells except inputs are **locked** to prevent accidental formula edits.

- **Password:** `gonka`
- To unlock: Review > Unprotect Sheet > enter `gonka`.
- **Google Sheets note:** XLSX sheet protection is not preserved when opening in Google Sheets. Formulas remain functional but are unprotected.

### Printing

All tabs are configured for print:

- Landscape orientation, fit-to-page width
- Margins optimized for A4/Letter
- Headers include tab name; footers include page numbers
- Charts are sized to print cleanly alongside data tables

---

## Models Overview

All models use a shared 32-period time axis: 24 monthly periods (Year 1-2) followed by 8 annual periods (Year 3-10). Each model builds on its predecessors in a dependency chain.

### Emission Schedule

Models the exponential decay of GNK mining rewards from the 680M mining allocation.

- Decay curve, cumulative mined supply, circulating vs. locked supply
- Inflation rate comparison with Ethereum
- 3 charts: emission decay, supply composition, inflation benchmark

### Token Price

Projects GNK price under three macro scenarios using the emission schedule as input.

- Conservative, Base, and Aggressive price bands
- Circulating market cap and fully diluted valuation
- Buyback-burn price floor effect
- 2 charts: scenario price trajectories, price vs. supply dual-axis

### Fee Transition

Analyzes the crossover point where network fee revenue exceeds mining emission value.

- Fee revenue from compute transactions vs. emission value
- Crossover ratio timeline (ratio > 1.0 = self-sustaining)
- Tail emission impact analysis
- 3 charts: revenue split, crossover ratio, fee vs. emission

### Host Profitability

Models the economics of running a GPU host node on the Gonka Network.

- Monthly income: mining rewards + fee share
- Operating costs: electricity, hardware depreciation, bandwidth
- Breakeven GNK price and ROI analysis
- Churn risk flagging (periods where hosting is unprofitable)
- 3 charts: income composition, Gonka vs. traditional cloud, breakeven price

### Treasury & POL

Simulates the Community Pool (12% of supply) and protocol-owned liquidity strategy.

- Community Pool inflows, outflows, and runway
- POL deployment returns and impermanent loss
- Buyback-burn cumulative impact on circulating supply
- Floor defense trigger analysis
- 3 charts: treasury composition, depletion timeline, buyback-burn impact

---

## Parameters

The model is driven by **70 parameters** organized into **15 groups**, defined in `models/parameters.py`.

| Group | Count | Examples |
|-------|-------|---------|
| Token Supply | 4 | Total supply (1B), mining allocation (68%), community pool (12%), founders (20%) |
| Emission Parameters | 4 | Epoch length, decay factor, initial reward, halvening schedule |
| Revenue Allocation | 4 | Fee split ratios between hosts, treasury, and burn |
| Price Scenarios | 7 | Conservative/Base/Aggressive price low and high bounds |
| Developer Growth | 4 | Developer adoption curve and compute demand multipliers |
| Fee Transition | 2 | Base fee rate, tail emission rate (10,000 GNK/day) |
| GPU Economics | 4 | Hash rate, power consumption, hardware cost |
| Host Economics | 11 | Electricity cost, bandwidth, maintenance, depreciation |
| POL Parameters | 7 | Deployment rate, target APR, IL assumptions |
| Buyback Parameters | 5 | Buyback rate, burn percentage, price floor trigger |
| Floor Defense | 6 | Defense trigger price, reserve ratio, intervention size |
| Treasury Operations | 2 | Operating budget, grant allocation |
| What-If Toggles | 2 | Buyback-Burn Active, Deploy POL Active |
| veGNK Parameters | 5 | Lock duration, boost multiplier, governance weight |
| Network Parameters | 3 | Node count growth, utilization rate, network capacity |

Each parameter carries a **confidence level**:

- **HIGH** -- derived from protocol constants or historical data
- **MED** -- informed estimates based on comparable networks
- **LOW** -- speculative projections requiring future validation

All parameters include **source citations** (whitepaper sections, comparable protocol data, or modeling assumptions) visible in the Assumptions tab.

---

## Project Structure

```
gonka-tokenomics/
  generate.py                  # CLI entry point (--test flag for quick validation)
  requirements.txt             # openpyxl==3.1.5
  models/
    parameters.py              # 70 parameters, 15 groups (single source of truth)
  generators/
    workbook_base.py           # Assumptions tab, scenario selector, what-if toggles
    styles.py                  # Named styles, color constants, number formats
    chart_utils.py             # Chart rendering fix for Excel compatibility
    emission.py                # Emission Schedule tab (32 rows, 10 cols, 3 charts)
    token_price.py             # Token Price tab (32 rows, 12 cols, 2 charts)
    fee_transition.py          # Fee Transition tab (32 rows, 14 cols, 3 charts)
    host_profit.py             # Host Profitability tab (32 rows, 13 cols, 3 charts)
    treasury.py                # Treasury & POL tab (32 rows, 14 cols, 3 charts)
    dashboard.py               # Dashboard tab (8 KPIs, scenario matrix, 3 charts)
    documentation.py           # Master workbook Documentation tab
    cover_sheet.py             # Standalone Documentation tab
    glossary.py                # Standalone Definitions tab (22 terms)
    standalone.py              # Standalone workbook generator
    standalone_config.py       # Per-standalone configs, glossary terms, narratives
    print_setup.py             # Print settings and cell protection
  output/                      # Generated workbooks (gitignored)
```

**17 charts** across 6 model/dashboard tabs. All charts use `fix_chart_rendering()` to patch the openpyxl application tag for reliable rendering in desktop Excel.

---

## Research Foundation

The economic models are grounded in four research documents produced during v1.0, plus five deep-dive analyses:

### Core Research (project root)

| Document | Description |
|----------|-------------|
| `Gonka_Macro_Tokenomics_Research.md` | Macro-level tokenomics analysis: supply dynamics, emission curves, market positioning |
| `Gonka_Tokenomics_Deep_Analysis.md` | Technical deep dive into all economic mechanisms and their interactions |
| `Gonka_Tokenomics_Explained.md` | Stakeholder-friendly explainer of the entire token economy |
| `Gonka_Tokenomics_Fine_Tuning_Recommendations.md` | 10 prioritized recommendations for optimizing the token economy (capstone) |

### Deep Research

Five specialized research reports in `.planning/phases/01-deep-macro-tokenomics-research/research/`:

1. **Protocol-Owned Liquidity** -- POL strategies, LP mechanics, IL mitigation
2. **Real Yield and Buybacks** -- Buyback-burn economics, sustainable yield models
3. **veToken and Governance** -- Vote-escrow mechanics, governance incentive alignment
4. **Fee Transition Stress Test** -- Crossover timing under adverse conditions
5. **GPU Economics and Developer Growth** -- Compute market dynamics, adoption curves

### Reference Materials

- `whitepaper.pdf` -- Gonka Network technical whitepaper
- `tokenomics.pdf` -- Original tokenomics specification

---

## Version History

### v1.1 -- Economic Modeling (2026-02-07)

- 5 Excel workbooks: 1 master (8 tabs, 17 charts) + 4 standalone
- 70 parameters with confidence levels and source citations
- Scenario selector (Conservative/Base/Aggressive) with full model chain recalculation
- 3 what-if toggles: Buyback-Burn, Deploy POL, Tail Emission
- Executive dashboard with 8 KPIs and scenario comparison matrix
- Cell protection, print-ready layout, cross-platform validated

### v1.0 -- Tokenomics Research and Optimization (2026-02-05)

- Comprehensive tokenomics research across 4 major documents
- 5 deep-dive analyses on POL, buybacks, governance, fees, and GPU economics
- 10 prioritized fine-tuning recommendations for the Gonka token economy

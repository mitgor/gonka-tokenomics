# Gonka Tokenomics

*Last updated: 2026-07-18*

Economic modeling and go-to-market research suite for the Gonka Network -- a decentralized AI infrastructure platform with ~98% productive compute and Sprint Consensus (2.3B-parameter Transformer-based PoW).

Generates **5 Excel workbooks** (1 master + 4 standalone) that model token emission, price scenarios, fee transition, host profitability, and treasury operations over a 10-year horizon, plus GTM research deliverables (v1.2-v1.4). Built for Gonka leadership, investors, and economic stakeholders.

**Network context (as of 2026-07-18):** Gonka has raised ~$80M total -- a $12M Bitfury strategic round (Nov 2025, entry ~$0.60/GNK) plus Bitfury's $50M commitment (Dec 2025, the first draw from its $1B ethical-AI fund). In 2026, the GAIB x Gonka partnership opened GNK mining rewards to the open market, with GAIB handling GPU procurement, node operations, and reward routing for H100/H200/B200 hardware. Live network size is far below the ~14,000 H100-equivalent GPUs announced Feb 2, 2026 (the announced peak): as of July 18, 2026, [joingonka.ai](https://joingonka.ai/en/)'s live counter shows ~1,178 GPUs active, consistent with [tracker.gonka.vip](https://tracker.gonka.vip/)'s ~1,214. Both the April 2026 figure of ~4,648 GPUs (~113 participants / ~582 MLNodes) and CoinMarketCap's static "~5,000 H100-equivalents" description are stale -- treat the live counters (~1,200 GPUs) as the active-mining denominator. The previously cited "448+ active hosts" does not match any current source. Real-time network data is available from independent explorers: [gonka.gg](https://gonka.gg/) (free public API), [gonkascan.com](https://gonkascan.com/), [gonkahub.com](https://gonkahub.com/), and [tracker.gonka.vip](https://tracker.gonka.vip/). Workbook adoption assumptions remain Feb-2026 estimates and predate these figures; note in particular that per-GPU mining share and host break-even were computed on the 14,000-GPU denominator -- at a ~1,200-GPU live network, per-GPU share is ~11-12x higher and host break-even GNK price is correspondingly lower (~4x lower than even a 5,000-GPU assumption).

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
  research-model-selection.md  # Open-model selection research (v1.2, re-baselined 2026-07-18)
  strategy-kimi-k25-agent-inference.md  # Kimi agent-inference strategy (v1.2, re-baselined 2026-07-18)
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
  output/                      # Generated workbooks (gitignored) + committed GTM docs
    gonka_*.md                 # 11 GTM research deliverables (v1.3-v1.4)
    pdf/                       # PDF renders of the GTM deliverables
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

## GTM Research (v1.2-v1.4)

Milestones v1.2-v1.4 added go-to-market research on top of the economic models:

- **v1.2 root docs:** `research-model-selection.md` (open-model landscape) and `strategy-kimi-k25-agent-inference.md` (agent-inference strategy)
- **v1.3-v1.4 deliverables** in `output/`: message house, developer personas, competitive feature matrix, provider landscape map, agent pricing analysis, agent-native pitch, objection playbook, channel strategy, partnership playbook, PLG growth model, and the v1.4 engineering backlog (PDF renders in `output/pdf/`)

**Freshness note (2026-07-18):** the two v1.2 root docs were originally written against **Kimi K2.5** (Feb 2026) and have since been **re-baselined to the July 2026 model landscape** (headers dated 2026-07-18; major claims audit-verified as current). The current landscape they reflect: Moonshot shipped K2.6, then **Kimi K2.7-Code** (June 2026: 1T MoE, 32B active, 256K context, Modified MIT, coding-agent-focused), and launched **Kimi K3** via app/API on July 16, 2026 (2.8T-param MoE, 896 experts with 16 active per token, 1M-token context, native multimodal, always-on thinking mode, $3/$15 per M tokens with $0.30 cached input; full open weights scheduled by July 27, 2026 -- the largest open-weight release to date). K3 debuted #1 in Frontend Code Arena (1,679), ahead of Claude Fable 5 (1,631) and GPT-5.6 Sol (1,618) -- the first open model at the closed-frontier tier. The v1.3-v1.4 GTM deliverables in `output/` still predate the ~$80M funding total and the GAIB partnership described above.

---

## Version History

### v1.4 -- GTM Engineering Execution (started 2026-04-02, in progress)

- Engineering backlog: 18 must-ship and 14 nice-to-have items (`output/gonka_v14_engineering_backlog.md`)

### v1.3 -- OpenClaw Go-To-Market Research (2026-04-01)

- 10 GTM deliverables in `output/` with PDF renders: positioning, personas, pricing, competitive analysis, channels, partnerships, and PLG growth model

### v1.2 -- Kimi K2.5 Integration & Agent Inference (2026-02-13)

- Open-model selection research and Kimi agent-inference strategy (re-baselined to the July 2026 landscape on 2026-07-18; see GTM Research freshness note)

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

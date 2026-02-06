# Phase 5: Host Profitability Model - Research

**Researched:** 2026-02-06
**Domain:** openpyxl stacked area charts, two-variable sensitivity tables with conditional formatting, cross-sheet references to Emission Schedule + Token Price + Fee Transition tabs, breakeven calculations, GPU cost amortization formulas, host churn risk indicators
**Confidence:** HIGH

## Summary

This phase builds the "Host Profitability" tab -- the most cross-tab-dependent model in the workbook. It must answer: "Is hosting on Gonka economically competitive with traditional GPU rental?" across varying GNK prices, network sizes, electricity costs, and hardware costs. The tab requires data from three upstream tabs (Emission Schedule, Token Price, Fee Transition) plus the Assumptions tab, making it the first model with triple cross-tab dependencies.

Research covered eight technical domains: (1) new parameters needed in `parameters.py` for traditional rental benchmarks, network size sensitivity, and GPU cost amortization; (2) dual-income breakdown (mining rewards + fee income) using cross-sheet references from Emission Schedule and Fee Transition; (3) breakeven GNK price calculation at each time point; (4) stacked area chart creation in openpyxl for income composition; (5) two-variable sensitivity table (GNK price rows x network GPU count columns) with ColorScaleRule heat map; (6) electricity cost sensitivity across three tiers; (7) GPU hardware cost amortization with months-to-breakeven and cumulative ROI; and (8) host churn risk indicator using CellIsRule conditional formatting when Gonka income drops below traditional rental.

All openpyxl features have been verified against the patterns established in Phases 2-4. The stacked area chart uses `AreaChart(grouping="stacked")`. The two-variable sensitivity table uses `ColorScaleRule` for heat map formatting (proven in Phase 4's crossover matrix). Host churn risk uses `CellIsRule` for red conditional formatting when Gonka income < traditional rental (proven in Phase 3 for deflationary flagging and Phase 4 for crossover ratios).

**Primary recommendation:** Build `generators/host_profit.py` following the established `build_*_tab()` pattern. Add 3-5 new parameters to `parameters.py` (traditional rental benchmarks, GPU wattage). Structure the tab with: (1) primary data table with 32 period rows showing dual income, breakeven price, and churn risk; (2) a sensitivity matrix below the data (GNK price x network GPU count); (3) electricity sensitivity section; (4) GPU amortization section; (5) charts to the right of data.

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| openpyxl | 3.1.5 | Excel generation (charts, formulas, conditional formatting) | Already installed; sole dependency; verified in Phases 1-4 |
| openpyxl.chart.AreaChart | 3.1.5 | Stacked area chart for dual-income breakdown | Built-in; `grouping="stacked"` verified in Phase 2 supply composition chart |
| openpyxl.chart.LineChart | 3.1.5 | Breakeven GNK price trend + traditional rental comparison | Already used in Phases 2-3 |
| openpyxl.formatting.rule.CellIsRule | 3.1.5 | Red/green conditional formatting for churn risk, profitability | Already used in Phase 3 (deflationary flag) and Phase 4 (crossover ratios) |
| openpyxl.formatting.rule.ColorScaleRule | 3.1.5 | Three-color heat map for sensitivity table | Already used in Phase 4 crossover matrix |
| openpyxl.utils.quote_sheetname | 3.1.5 | Cross-sheet references to Emission Schedule, Token Price, Fee Transition | Already used in Phases 3-4 |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| openpyxl.styles.PatternFill | 3.1.5 | Static fills for churn risk rows | Alongside conditional formatting for permanent column shading |
| openpyxl.chart.Reference | 3.1.5 | Data ranges for chart series | Every chart creation |
| openpyxl.chart.BarChart | 3.1.5 | Side-by-side bar chart for Gonka vs traditional rental comparison | REQ-M3-03 |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| AreaChart for income breakdown | Stacked BarChart | AreaChart shows continuous transition better; BarChart used in Phase 4 for waterfall |
| CellIsRule for churn risk | FormulaRule for cross-cell comparison | CellIsRule is simpler when comparing column to another column value; FormulaRule offers more flexibility but Phase 4 proved CellIsRule sufficient |
| Static sensitivity table | Dynamic with DataValidation inputs | Static table shows all combinations at once (leadership can scan); dynamic shows one-at-a-time |
| Single sheet for all content | Multiple sheets | Single sheet consistent with Phase 2-4 pattern; keeps cross-model comparison simple |

**Installation:**
```bash
pip install openpyxl==3.1.5  # Already in requirements.txt; no new dependencies
```

## Architecture Patterns

### Recommended Project Structure
```
models/
  parameters.py        # MODIFIED: Add HOST PROFITABILITY group (new parameters)
generators/
  host_profit.py       # NEW: build_host_profit_tab(wb, param_refs, emission_meta, price_meta, fee_meta) -> host_meta
  workbook_base.py     # NO CHANGES
  styles.py            # NO CHANGES: existing styles sufficient
  emission.py          # NO CHANGES
  token_price.py       # NO CHANGES
  fee_transition.py    # NO CHANGES
  chart_utils.py       # NO CHANGES
generate.py            # MODIFIED: Wire in host_profit.build_host_profit_tab()
```

### Pattern 1: Triple Cross-Tab Dependencies
**What:** This is the first tab referencing three upstream tabs (Emission Schedule, Token Price, Fee Transition) plus Assumptions. The function signature takes all four meta dicts.
**When to use:** Any model that synthesizes data from multiple prior analysis tabs.

**Function signature:**
```python
def build_host_profit_tab(wb, param_refs, emission_meta, price_meta, fee_meta):
    """Create the 'Host Profitability' worksheet.

    Args:
        wb: An openpyxl Workbook with styles already registered.
        param_refs: dict mapping parameter names to "Assumptions!$B$N".
        emission_meta: dict from build_emission_tab() with sheet coordinates.
        price_meta: dict from build_token_price_tab() with sheet coordinates.
        fee_meta: dict from build_fee_transition_tab() with sheet coordinates.

    Returns:
        dict: host_meta with sheet coordinates for downstream tabs.
    """
```

**Cross-sheet references needed:**
```python
es_sheet = quote_sheetname(emission_meta["sheet_name"])   # 'Emission Schedule'
tp_sheet = quote_sheetname(price_meta["sheet_name"])      # 'Token Price'
ft_sheet = quote_sheetname(fee_meta["sheet_name"])        # 'Fee Transition'

# From Emission Schedule:
es_mining_col = emission_meta["cols"]["mining_emission"]  # "D" - GNK per period
es_start_col = emission_meta["cols"]["start_epoch"]       # "B"
es_end_col = emission_meta["cols"]["end_epoch"]           # "C"
es_period_col = emission_meta["cols"]["period_label"]     # "A"

# From Token Price:
tp_active_col = price_meta["cols"]["active_price"]        # "F"

# From Fee Transition:
ft_host_share_col = fee_meta["cols"]["host_share"]        # "K" - 70% of base fee revenue
```

**IMPORTANT:** All three upstream tabs use the same period structure (32 rows, data_start_row=3, data_end_row=34). Row alignment is guaranteed by construction.

### Pattern 2: Primary Data Table Layout (32 rows x ~15 columns)
**What:** The main data table shows per-period host economics across 32 time periods.
**When to use:** Core time-series data for the host profitability model.

**Recommended column structure:**
```
A: Period Label                     (cross-ref from Emission Schedule)
B: Mining Emission per Host (GNK)   (total mining / network GPU count * GPUs per host)
C: Mining Income per Host ($)       (B * active price)
D: Fee Income per Host ($)          (host share from Fee Transition / host count)
E: Total Gonka Income per Host ($)  (C + D)
F: Electricity Cost per Host ($)    (wattage * electricity rate * hours per period)
G: Net Income per Host ($)          (E - F)
H: Traditional Rental Income ($)    (benchmark rate * hours per period)
I: Gonka vs Traditional ($)         (E - H, or G - H for net comparison)
J: Breakeven GNK Price ($)          ((Host_Cost - Fee_Income) / Daily_GNK_Earned)
K: Breakeven Low ($)                (reference line at $0.85)
L: Breakeven High ($)               (reference line at $3.30)
M: Churn Risk Flag                  (1 if Gonka < Traditional, 0 otherwise)
```

**Data sources per column:**
- Column A: `='Emission Schedule'!A{row}` (period label, crossref_cell style)
- Column B: `='Emission Schedule'!D{row} / network_gpus * gpus_per_host` (mining GNK per host)
- Column C: `=B{row} * 'Token Price'!F{row}` (mining income in USD)
- Column D: `='Fee Transition'!K{row} / host_count` (fee income per host in USD)
- Column E: `=C{row} + D{row}` (total Gonka income)
- Column F: Electricity cost formula using param_refs
- Column G: `=E{row} - F{row}` (net income after electricity)
- Column H: Traditional rental formula using param_refs
- Column I: `=E{row} - H{row}` or `=G{row} - H{row}` (income comparison)
- Column J: Breakeven GNK price formula
- Columns K/L: Static reference values
- Column M: `=IF(E{row}<H{row},1,0)` (churn risk flag)

**Column count rationale:** 13 columns keeps the tab manageable (Phase 4 has 14). Charts start at column O or P.

### Pattern 3: Breakeven GNK Price Formula
**What:** At each time point, calculate the GNK price at which Gonka hosting breaks even with traditional rental.
**When to use:** REQ-M3-02.

**Formula:** `Breakeven_GNK = (Host_Cost - Fee_Income) / Daily_GNK_Earned`

Where:
- `Host_Cost` = traditional rental income (opportunity cost benchmark)
- `Fee_Income` = inference fee host share per period
- `Daily_GNK_Earned` = mining emission per host per period

In Excel formula terms (for a monthly period with 30 days):
```
=(H{row} - D{row}) / B{row}
```

Where:
- `H{row}` = traditional rental income for the period
- `D{row}` = fee income per host for the period
- `B{row}` = mining emission GNK per host for the period

**Edge case:** When fee income exceeds traditional rental cost, breakeven is negative (already profitable from fees alone). Use `=MAX(0, (H{row}-D{row})/B{row})` or `=IFERROR(...)` to handle this gracefully.

**Reference range:** The $0.85-$3.30 range from v1.0 research should be displayed as static reference columns (K and L) so they appear on the breakeven chart as horizontal bands.

### Pattern 4: Two-Variable Sensitivity Table (REQ-D01)
**What:** A static, pre-calculated matrix with GNK price (rows) and network GPU count (columns), showing host ROI or monthly profit at each combination.
**When to use:** REQ-D01 and success criterion #4.

**Layout (below data table, starting ~row 37):**
```
Row 36: SECTION HEADER: "HOST ROI SENSITIVITY (GNK Price x Network GPUs)"
Row 37: Sub-header: "", "1,000 GPUs", "5,000 GPUs", "10,000 GPUs", "25,000 GPUs", "50,000 GPUs"
Row 38: "$0.50"     cell     cell     cell     cell     cell
Row 39: "$1.00"     cell     cell     cell     cell     cell
Row 40: "$2.00"     cell     cell     cell     cell     cell
Row 41: "$3.00"     cell     cell     cell     cell     cell
Row 42: "$5.00"     cell     cell     cell     cell     cell
Row 43: "$10.00"    cell     cell     cell     cell     cell
```

**Each cell formula computes monthly host profit:**
```
= (mining_emission_yr10_gnk / network_gpus * gpus_per_host * gnk_price
   + fee_host_share_yr10 / (network_gpus / gpus_per_host))
   - electricity_cost_monthly
   - traditional_rental_monthly
```

This is a Year 10 snapshot (worst case for emissions) since that is when profitability is most at risk.

**Conditional formatting:**
- Green (profitable): `CellIsRule(operator="greaterThan", formula=["0"])`
- Red (unprofitable): `CellIsRule(operator="lessThanOrEqual", formula=["0"])`

OR use `ColorScaleRule` for a gradient:
```python
ColorScaleRule(
    start_type="num", start_value=-5000, start_color="F8696B",    # Red (loss)
    mid_type="num", mid_value=0, mid_color="FFEB84",              # Yellow (breakeven)
    end_type="num", end_value=5000, end_color="63BE7B",           # Green (profit)
)
```

**Note on static vs formula approach:** The sensitivity table uses Year 10 data as a snapshot. Each cell references the emission rate at row 34 (Year 10) and the fee host share at row 34. The GNK price and GPU count values are hardcoded in each cell formula (not referencing param_refs for these axes). This is consistent with "static/pre-calculated" per REQ-D01.

However, the emission rate and fee revenue within each cell still reference the Emission Schedule and Fee Transition tabs via cross-sheet formulas, so if those tabs' assumptions change, the sensitivity table updates.

### Pattern 5: Electricity Cost Sensitivity (Three Tiers)
**What:** Show profitability impact at $0.05, $0.08, $0.12/kWh using the three existing parameters.
**When to use:** REQ-M3-05.

**Implementation approach:** A small 3-row section below the sensitivity matrix:

```
Row 45: SECTION HEADER: "ELECTRICITY COST SENSITIVITY"
Row 46: Sub-header: "Electricity Rate", "Monthly Cost/Host", "Net Monthly Profit", "ROI Impact"
Row 47: "$0.05/kWh"  =formula  =formula  =formula
Row 48: "$0.08/kWh"  =formula  =formula  =formula
Row 49: "$0.12/kWh"  =formula  =formula  =formula
```

Each row uses the corresponding parameter from Assumptions:
- `param_refs["Electricity Cost Low"]` ($0.05)
- `param_refs["Electricity Cost Mid"]` ($0.08)
- `param_refs["Electricity Cost High"]` ($0.12)

**Monthly cost formula:** `= electricity_rate * gpu_wattage * 24 * 30 / 1000 * gpus_per_host`

Where `gpu_wattage` is a parameter (H100 ~700W TDP, but use ~400W effective draw). The H100 specs show 700W TDP but typical inference workloads draw 300-400W. Use the value from research (400W for A100/H100 inference).

**GPU wattage parameter:** Need to add a "GPU Power Draw (W)" parameter to parameters.py. Value: 400W (inference workload average for H100-class GPU).

### Pattern 6: GPU Hardware Cost Amortization (REQ-M3-06)
**What:** Hardware cost input drives a months-to-breakeven and cumulative ROI calculation.
**When to use:** REQ-M3-06.

**Implementation approach:** A small section below electricity sensitivity:

```
Row 51: SECTION HEADER: "GPU HARDWARE AMORTIZATION"
Row 52: Sub-header: "Hardware Cost", "Monthly Net Income", "Months to Breakeven", "3-Year ROI", "5-Year ROI"
Row 53: "H100 Low ($25K)"  =formula  =formula  =formula  =formula
Row 54: "H100 High ($40K)" =formula  =formula  =formula  =formula
```

**Months to breakeven:** `= hardware_cost / monthly_net_income`
Where `monthly_net_income` = total Gonka income (Year 1 monthly average) minus electricity cost.

**Cumulative ROI:** `= (monthly_net_income * months - hardware_cost) / hardware_cost`
For 3-year: months=36. For 5-year: months=60.

**Existing parameters:** `param_refs["H100 Hardware Cost Low"]` ($25,000) and `param_refs["H100 Hardware Cost High"]` ($40,000) already exist in HOST ECONOMICS group.

### Pattern 7: Host Churn Risk Indicator (REQ-M3-07)
**What:** Red conditional formatting whenever Gonka income drops below traditional rental equivalent.
**When to use:** REQ-M3-07 and success criterion #7.

**Implementation:**
```python
# Red fill + font when Gonka income < Traditional rental
red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
red_font = Font(name="Calibri", size=11, color="9C0006")

# Apply to column I (Gonka vs Traditional difference)
cell_range = f"I{data_start_row}:I{data_end_row}"
ws.conditional_formatting.add(
    cell_range,
    CellIsRule(
        operator="lessThan",
        formula=["0"],
        fill=red_fill,
        font=red_font,
    ),
)
```

Also apply to the full row for periods where churn risk is flagged (similar to Phase 4 danger zone formatting). When Gonka income < traditional rental, the entire row could get a light red background fill to make it visually scannable.

### Pattern 8: Stacked Area Chart for Dual Income (REQ-M3-01)
**What:** A stacked area chart showing mining rewards declining and fee income growing over 10 years.
**When to use:** REQ-M3-01 and success criterion #1.

**Implementation:**
```python
from openpyxl.chart import AreaChart, Reference

chart = AreaChart()
chart.grouping = "stacked"
chart.title = "Host Income Composition (Mining Rewards + Fee Income)"
chart.y_axis.title = "USD per Host"
chart.x_axis.title = "Period"
chart.style = 13
chart.width = 20
chart.height = 12

# Two series: Mining Income (C), Fee Income (D)
for col_key in ("mining_income", "fee_income"):
    col_num = col_to_num(meta["cols"][col_key])
    data = Reference(ws, min_col=col_num, min_row=meta["header_row"],
                     max_row=meta["data_end_row"])
    chart.add_data(data, titles_from_data=True)

cats = Reference(ws, min_col=1, min_row=meta["data_start_row"],
                 max_row=meta["data_end_row"])
chart.set_categories(cats)

ws.add_chart(chart, "O1")  # Right of data columns
```

**Note:** No `overlap=100` needed for AreaChart (that is a BarChart-specific setting). AreaChart with `grouping="stacked"` stacks correctly by default.

### Pattern 9: Side-by-Side Comparison Chart (REQ-M3-03)
**What:** A bar or line chart comparing Gonka income vs traditional rental at each time point.
**When to use:** REQ-M3-03 and success criterion #3.

**Implementation:** Use a grouped bar chart (not stacked) with two series:
```python
chart = BarChart()
chart.type = "col"
chart.grouping = "clustered"  # Side-by-side bars
chart.title = "Gonka Income vs Traditional GPU Rental"
chart.y_axis.title = "USD per Host"
chart.x_axis.title = "Period"
chart.style = 13
chart.width = 20
chart.height = 12

# Series 1: Total Gonka Income (E)
# Series 2: Traditional Rental Income (H)
```

**Alternative:** A line chart with both series. Line chart may be cleaner for 32 periods. Use line chart consistent with Phase 2-3 patterns.

### Anti-Patterns to Avoid
- **Computing Python values instead of Excel formulas:** ALL values must be Excel formulas. Python computes nothing.
- **Duplicating fee data into the host tab:** Use cross-sheet references to `'Fee Transition'!K{row}` for host fee share.
- **Hardcoding GPU counts in formulas:** Network GPU count comes from `param_refs["Current GPUs"]` (6,000).
- **Using different period structure:** Host Profitability MUST use same 32 rows (24 monthly + 8 annual) as Emission/Price/Fee tabs.
- **Forgetting to divide by host count:** Fee Transition `host_share` column shows TOTAL host revenue. Must divide by host count for per-host values.
- **Ignoring the `days` variable for period costs:** Monthly periods = 30 days, annual periods = 365 days. Electricity costs and rental income must scale accordingly.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Stacked area chart | Manual cell coloring | `AreaChart(grouping="stacked")` | Native Excel chart; auto-updates |
| Sensitivity heat map | Manual color per cell | `ColorScaleRule(start, mid, end)` | Dynamic gradient; proven in Phase 4 |
| Churn risk flag | Python-computed boolean | `CellIsRule(operator="lessThan")` | Dynamic; updates when assumptions change |
| Breakeven reference lines | Manual values each row | Static columns K/L with constant refs | Excel charts can use these as flat-line series |
| Cross-tab income data | Re-compute fees in host tab | `='Fee Transition'!K{row}` | Single source of truth; auto-propagates |
| Monthly/annual cost conversion | Hardcoded multipliers | `days` variable (30 or 365) per period | Consistent with Phase 2-4 pattern |

**Key insight:** Phase 5 is primarily a synthesis tab. Its complexity is not in new calculations but in correctly referencing and combining data from three upstream tabs. The formulas are simpler than Phase 4's crossover matrix -- the challenge is getting the cross-sheet references and per-host division right.

## Common Pitfalls

### Pitfall 1: Dividing Total Network Values by Per-Host Values Incorrectly
**What goes wrong:** Fee Transition's Host Share column (K) shows TOTAL host revenue for the entire network. If you display this without dividing by host count, per-host income looks impossibly high.
**Why it happens:** Fee Transition tab was designed for network-level analysis, not per-host analysis.
**How to avoid:** Always divide fee revenue by host count: `='Fee Transition'!K{row} / host_count_ref`
Where `host_count_ref = param_refs["Current Hosts"]` (448).
**Warning signs:** Per-host monthly income showing millions of dollars instead of thousands.

### Pitfall 2: Mining Emission per Host Must Account for Network GPU Count
**What goes wrong:** Mining emission is for the ENTIRE network. Per-host share depends on how many GPUs the host runs vs total network GPUs.
**Why it happens:** Emission Schedule shows total network emission, not per-host.
**How to avoid:** Formula: `per_host_mining = total_mining * (gpus_per_host / total_network_gpus)`
Where:
- `total_mining = 'Emission Schedule'!D{row}` (GNK per period)
- `gpus_per_host = Current GPUs / Current Hosts` (6000/448 = ~13.4)
- `total_network_gpus = param_refs["Current GPUs"]` (6,000)

Simplification: `per_host_mining = total_mining / Current_Hosts` (since GPUs are assumed evenly distributed).
**Warning signs:** Per-host mining income that equals total network mining income.

### Pitfall 3: Period Duration Mismatch in Cost Calculations
**What goes wrong:** Electricity cost or rental income calculated for wrong period duration (using monthly rate for annual periods or vice versa).
**Why it happens:** The 32 periods have two different durations: 30 days (monthly, i=0..23) and 365 days (annual, i=24..31).
**How to avoid:** Use `days` variable per period (30 or 365) in all cost/revenue calculations:
```python
days = 30 if i < 24 else 365
electricity_formula = f"={elec_ref}*{wattage_ref}*24*{days}/1000*{gpus_per_host}"
rental_formula = f"={rental_ref}*24*{days}*{gpus_per_host}"
```
**Warning signs:** Annual periods showing 12x lower costs than expected, or monthly periods showing 12x higher.

### Pitfall 4: Breakeven Formula Division by Zero
**What goes wrong:** When mining emission approaches zero (later periods), dividing by daily GNK earned produces `#DIV/0!` error.
**Why it happens:** Emission decay means later periods have very small GNK values.
**How to avoid:** Wrap in `IFERROR`: `=IFERROR((H{row}-D{row})/B{row}, 99999)`. Use a large sentinel value (99999) to indicate "breakeven price unreachable" rather than displaying an error.
**Warning signs:** `#DIV/0!` errors in breakeven column for Year 8-10 periods.

### Pitfall 5: Sensitivity Table Formula Not Referencing Upstream Tabs
**What goes wrong:** Sensitivity table cells use hardcoded emission values instead of cross-sheet references, so changing Assumptions doesn't update the table.
**Why it happens:** Temptation to simplify by computing emission values in Python and embedding as constants.
**How to avoid:** Each sensitivity cell must reference `'Emission Schedule'!D34` (Year 10 emission) and `'Fee Transition'!K34` (Year 10 fee host share) via cross-sheet formulas. Only the GNK price and GPU count axes are hardcoded.
**Warning signs:** Changing decay rate on Assumptions tab doesn't change sensitivity table values.

### Pitfall 6: AreaChart Stacking Without titles_from_data
**What goes wrong:** Stacked area chart shows "Series 1", "Series 2" instead of "Mining Income", "Fee Income" in the legend.
**Why it happens:** Forgetting `titles_from_data=True` in `add_data()`.
**How to avoid:** Always include header row in the data Reference and use `titles_from_data=True`.
**Warning signs:** Chart legend shows generic series names.

### Pitfall 7: Network Size Sensitivity Ignoring Host Count Scaling
**What goes wrong:** Sensitivity table shows that more GPUs = less mining reward per host, but doesn't account for more hosts also meaning more fee revenue per host from larger network.
**Why it happens:** Assuming fee revenue is fixed when network size changes. In reality, larger networks attract more developers and generate more fee revenue.
**How to avoid:** For the sensitivity table, use Year 10 fee revenue from the Fee Transition tab as the base case, and note in annotations that fee revenue may scale with network size. The sensitivity table primarily shows mining reward dilution. A footnote should clarify: "Fee revenue held constant at base scenario; larger networks may generate proportionally more fees."
**Warning signs:** Sensitivity table showing all large-network scenarios as unprofitable when they may be viable with proportional fee growth.

## Code Examples

### New Parameters for parameters.py
```python
# Source: v1.0 research (05-gpu-economics-and-developer-growth.md)
# Most host economics parameters already exist. Need to add:

# In HOST ECONOMICS group, add:
{
    "name": "Traditional Rental Rate (Lambda)",
    "value": 2.49,
    "unit": "USD/hr",
    "source": "Lambda Labs Q1 2026",
    "format": "price_per_hour",
},
{
    "name": "Traditional Rental Rate (CoreWeave)",
    "value": 2.06,
    "unit": "USD/hr",
    "source": "CoreWeave 3yr reserved Q1 2026",
    "format": "price_per_hour",
},
{
    "name": "GPU Power Draw",
    "value": 400,
    "unit": "watts",
    "source": "H100 inference avg",
    "format": "integer",
},
```

**Existing parameters Phase 5 will reference:**
- `"Current Hosts"` (448) -- HOST ECONOMICS
- `"Current GPUs"` (6,000) -- HOST ECONOMICS
- `"Electricity Cost Low"` ($0.05) -- HOST ECONOMICS
- `"Electricity Cost Mid"` ($0.08) -- HOST ECONOMICS
- `"Electricity Cost High"` ($0.12) -- HOST ECONOMICS
- `"H100 Hardware Cost Low"` ($25,000) -- HOST ECONOMICS
- `"H100 Hardware Cost High"` ($40,000) -- HOST ECONOMICS
- `"Host Share"` (0.70) -- REVENUE ALLOCATION
- `"Active Price Low"` -- SCENARIO SELECTOR (derived)
- `"Active Price High"` -- SCENARIO SELECTOR (derived)

### Per-Host Mining Income Formula
```python
# Source: Follows Phase 3-4 cross-sheet reference pattern
es_sheet = quote_sheetname(emission_meta["sheet_name"])
tp_sheet = quote_sheetname(price_meta["sheet_name"])
hosts_ref = param_refs["Current Hosts"]
mining_col = emission_meta["cols"]["mining_emission"]       # "D"
active_price_col = price_meta["cols"]["active_price"]       # "F"

for i in range(32):
    row = 3 + i
    es_row = emission_meta["data_start_row"] + i
    tp_row = price_meta["data_start_row"] + i

    # B: Mining Emission per Host (GNK)
    # = total_mining_emission / host_count
    mining_gnk_formula = f"={es_sheet}!{mining_col}{es_row}/{hosts_ref}"
    ws.cell(row=row, column=2, value=mining_gnk_formula).style = "tokens"

    # C: Mining Income per Host ($)
    # = per_host_mining_gnk * active_price
    mining_usd_formula = f"=B{row}*{tp_sheet}!{active_price_col}{tp_row}"
    ws.cell(row=row, column=3, value=mining_usd_formula).style = "currency"
```

### Per-Host Fee Income Formula
```python
# Source: Cross-ref to Fee Transition host share column
ft_sheet = quote_sheetname(fee_meta["sheet_name"])
host_share_col = fee_meta["cols"]["host_share"]  # "K"
hosts_ref = param_refs["Current Hosts"]

for i in range(32):
    row = 3 + i
    ft_row = fee_meta["data_start_row"] + i

    # D: Fee Income per Host ($)
    # = total_host_share / host_count
    fee_formula = f"={ft_sheet}!{host_share_col}{ft_row}/{hosts_ref}"
    ws.cell(row=row, column=4, value=fee_formula).style = "currency"
```

### Breakeven GNK Price Formula
```python
# Source: v1.0 research breakeven formula
# Breakeven = (Host_Cost - Fee_Income) / Mining_GNK_per_host
# Where Host_Cost = traditional rental income for the period

for i in range(32):
    row = 3 + i

    # J: Breakeven GNK Price
    # = MAX(0, (traditional_rental - fee_income) / mining_gnk_per_host)
    breakeven_formula = f"=IFERROR(MAX(0,(H{row}-D{row})/B{row}),99999)"
    ws.cell(row=row, column=10, value=breakeven_formula).style = "currency_precise"

    # K: Breakeven Reference Low ($0.85)
    ws.cell(row=row, column=11, value=0.85).style = "currency_precise"

    # L: Breakeven Reference High ($3.30)
    ws.cell(row=row, column=12, value=3.30).style = "currency_precise"
```

### Electricity and Traditional Rental Cost Formulas
```python
# Source: Parameters from HOST ECONOMICS group
elec_mid_ref = param_refs["Electricity Cost Mid"]
gpu_power_ref = param_refs["GPU Power Draw"]  # NEW parameter (400W)
hosts_ref = param_refs["Current Hosts"]
gpus_ref = param_refs["Current GPUs"]
lambda_ref = param_refs["Traditional Rental Rate (Lambda)"]  # NEW

for i in range(32):
    row = 3 + i
    days = 30 if i < 24 else 365

    # F: Electricity Cost per Host ($)
    # = electricity_rate * gpu_watt * 24hrs * days / 1000 (W->kW) * gpus_per_host
    # gpus_per_host = Current GPUs / Current Hosts
    elec_formula = (
        f"={elec_mid_ref}*{gpu_power_ref}*24*{days}/1000"
        f"*({gpus_ref}/{hosts_ref})"
    )
    ws.cell(row=row, column=6, value=elec_formula).style = "currency"

    # H: Traditional Rental Income ($)
    # = rental_rate * 24hrs * days * gpus_per_host
    rental_formula = (
        f"={lambda_ref}*24*{days}*({gpus_ref}/{hosts_ref})"
    )
    ws.cell(row=row, column=8, value=rental_formula).style = "currency"
```

### Sensitivity Table (Year 10 snapshot)
```python
# Source: REQ-D01 - Two-variable sensitivity table
# Rows = GNK prices, Columns = Network GPU counts

yr10_row = 34  # Last data row (Year 10)
yr10_es_row = emission_meta["data_end_row"]

gnk_prices = [0.50, 1.00, 2.00, 3.00, 5.00, 10.00]
gpu_counts = [1000, 5000, 10000, 25000, 50000]

# Section header
ws.merge_cells(f"A36:F36")
ws.cell(row=36, column=1,
        value="HOST ROI SENSITIVITY (Year 10 Monthly Profit per Host)").style = "section_header"

# Column headers
ws.cell(row=37, column=1, value="GNK Price \\ GPUs")
for j, gpu_count in enumerate(gpu_counts):
    ws.cell(row=37, column=2+j, value=f"{gpu_count:,} GPUs").style = "header"

for p_idx, gnk_price in enumerate(gnk_prices):
    matrix_row = 38 + p_idx
    ws.cell(row=matrix_row, column=1, value=f"${gnk_price:.2f}")

    for g_idx, gpu_count in enumerate(gpu_counts):
        col = 2 + g_idx

        # Monthly profit per host at Year 10:
        # mining_income = emission_at_yr10 / gpu_count * gpus_per_host * gnk_price
        # fee_income = fee_host_share_yr10 / (gpu_count / gpus_per_host_ratio)
        # electricity = elec_rate * wattage * 24 * 30 / 1000 * gpus_per_host
        # profit = mining_income + fee_income - electricity

        gpus_per_host = f"({gpus_ref}/{hosts_ref})"

        formula = (
            f"=({es_sheet}!{mining_col}{yr10_es_row}/{gpu_count}*{gpus_per_host}*{gnk_price}"
            f"+{ft_sheet}!{host_share_col}{yr10_row}/({gpu_count}/{gpus_per_host}))"
            f"-{elec_mid_ref}*{gpu_power_ref}*24*30/1000*{gpus_per_host}"
        )
        cell = ws.cell(row=matrix_row, column=col, value=formula)
        cell.style = "currency"
```

### Churn Risk Conditional Formatting
```python
# Source: Phase 4 crossover formatting pattern (verified)

# Red when Gonka income < Traditional rental (column I negative)
red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
red_font = Font(name="Calibri", size=11, color="9C0006")

# Green when Gonka income >= Traditional rental
green_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
green_font = Font(name="Calibri", size=11, color="006100")

cell_range = f"I{data_start_row}:I{data_end_row}"

# Green when >= 0 (Gonka competitive)
ws.conditional_formatting.add(
    cell_range,
    CellIsRule(
        operator="greaterThanOrEqual",
        formula=["0"],
        fill=green_fill,
        font=green_font,
    ),
)

# Red when < 0 (churn risk)
ws.conditional_formatting.add(
    cell_range,
    CellIsRule(
        operator="lessThan",
        formula=["0"],
        fill=red_fill,
        font=red_font,
    ),
)
```

### Sensitivity Table Heat Map
```python
# Source: Phase 4 ColorScaleRule pattern (verified)
from openpyxl.formatting.rule import ColorScaleRule

# 6 rows x 5 cols of sensitivity data
matrix_range = f"B38:F43"

rule = ColorScaleRule(
    start_type="num", start_value=-5000, start_color="F8696B",    # Red (loss)
    mid_type="num", mid_value=0, mid_color="FFEB84",              # Yellow (breakeven)
    end_type="num", end_value=5000, end_color="63BE7B",           # Green (profit)
)
ws.conditional_formatting.add(matrix_range, rule)
```

### Complete host_meta Return Dict
```python
host_meta = {
    "sheet_name": "Host Profitability",
    "header_row": 2,
    "data_start_row": 3,
    "data_end_row": 34,
    "cols": {
        "period_label": "A",
        "mining_gnk_per_host": "B",
        "mining_income": "C",
        "fee_income": "D",
        "total_gonka_income": "E",
        "electricity_cost": "F",
        "net_income": "G",
        "traditional_rental": "H",
        "gonka_vs_traditional": "I",
        "breakeven_gnk": "J",
        "breakeven_ref_low": "K",
        "breakeven_ref_high": "L",
        "churn_risk_flag": "M",
    },
    "sensitivity_start_row": 37,
    "sensitivity_end_row": 43,
    "electricity_section_start_row": 46,
    "gpu_amortization_start_row": 52,
}
```

### generate.py Integration
```python
# In generate_all():
from generators.host_profit import build_host_profit_tab

# Phase 5: Host Profitability Model
host_meta = build_host_profit_tab(wb, param_refs, emission_meta, price_meta, fee_meta)
```

This replaces the existing comment `# Phase 5: host_profit.build_host_profit_tab(...)` on line 65.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Single profitability number | Two-variable sensitivity matrix | This phase | Shows full landscape of profitable/unprofitable conditions |
| Mining-only host income | Dual income (mining + fees) | This phase | Reflects actual Gonka dual-income model |
| Static cost assumptions | Three-tier electricity sensitivity | This phase | Captures geographic cost variation |
| No ROI timeline | GPU amortization with months-to-breakeven | This phase | Answers "when does my hardware pay for itself?" |
| Implicit churn risk | Explicit red formatting when Gonka < traditional | This phase | Leadership can see exactly when/if hosts become unprofitable |

**Deprecated/outdated:**
- Single-point host profitability estimates: Replaced by multi-variable sensitivity analysis
- Assumption that all hosts are identical: Model uses per-host averages based on Current Hosts/Current GPUs ratio (13.4 GPUs/host)

## Open Questions

1. **Per-Host vs Per-GPU Profitability Units**
   - What we know: Parameters define "Current Hosts" (448) and "Current GPUs" (6,000). The ratio is ~13.4 GPUs/host.
   - What's unclear: Should the data table show profitability per HOST (aggregate of ~13.4 GPUs) or per GPU (individual unit)?
   - Recommendation: Show per HOST, since hosts are the decision-making unit (a host decides to join/leave Gonka). Include GPUs/host as a derived value in column headers: "Mining Income per Host (~13 GPUs)". The sensitivity table can note GPUs/host assumption.

2. **Which Traditional Rental Rate for Comparison**
   - What we know: Lambda is $2.49/hr on-demand, CoreWeave is $2.06/hr (3-year reserved). Both are in the additional_context.
   - What's unclear: Which rate to use as the primary benchmark.
   - Recommendation: Use Lambda $2.49/hr as the primary benchmark (on-demand, no commitment required -- most comparable to Gonka's flexible hosting). Show CoreWeave $2.06/hr as a second reference line. Add both as new parameters to parameters.py.

3. **Network GPU Count in Sensitivity Table vs Assumptions**
   - What we know: The sensitivity table varies network GPU count (1K-50K). But the data table uses `param_refs["Current GPUs"]` (6,000) as fixed.
   - What's unclear: Should changing "Current GPUs" on Assumptions also affect the sensitivity table?
   - Recommendation: The sensitivity table hardcodes GPU count values per column (1K, 5K, 10K, 25K, 50K) since it is explicitly a sensitivity analysis. The data table uses the Assumptions value. This separation is standard for sensitivity analysis.

4. **Fee Revenue Scaling with Network Size**
   - What we know: The Fee Transition tab computes fee revenue independent of network GPU count. But in reality, more GPUs = more capacity = potentially more developers = more fee revenue.
   - What's unclear: Should the sensitivity table scale fee revenue with network size?
   - Recommendation: Do NOT scale fee revenue in the sensitivity table. Keep it constant at the base scenario value. Add an annotation: "Fee revenue held at base growth scenario. Larger networks may generate proportionally more fees." This avoids adding speculative scaling assumptions and keeps the table focused on the mining-dilution vs network-size trade-off.

5. **Electricity as Operating Cost vs Opportunity Cost**
   - What we know: The breakeven formula uses `(Host_Cost - Fee_Income) / Daily_GNK_Earned` where Host_Cost is traditional rental (opportunity cost).
   - What's unclear: Should electricity cost be subtracted from both Gonka and traditional sides, or shown separately?
   - Recommendation: Show electricity as a separate column (F) and compute net income (G = E - F). The comparison column (I) compares total Gonka income (E) to traditional rental (H), since traditional rental prices already include the provider's electricity costs. This way, leadership can see: "Gonka gross income vs what you'd earn renting to Lambda, and separately, what your electricity costs are."

## Sources

### Primary (HIGH confidence)
- Existing codebase: `generators/emission.py`, `generators/token_price.py`, `generators/fee_transition.py` -- established patterns for build_*_tab(), meta dicts, cross-sheet references, chart creation, conditional formatting
- Existing codebase: `models/parameters.py` -- HOST ECONOMICS group already contains 8 parameters (hosts, GPUs, electricity tiers, hardware costs, collateral rate)
- Existing codebase: `generators/styles.py` -- all required styles (currency, currency_precise, tokens, integer, crossref_cell, warning_cell) already defined
- Phase 4 research: Verified ColorScaleRule with fixed num anchors, CellIsRule patterns, stacked bar overlap=100 (not needed for AreaChart)
- Phase 4 implementation: fee_meta dict structure with host_share column confirmed at "K"

### Secondary (MEDIUM confidence)
- Phase 1 research: `research/04-fee-transition-stress-test.md` -- Host profitability deep dive (Section 5), breakeven GNK price calculations ($0.85-$3.30 range), host revenue sources
- Phase 1 research: `research/05-gpu-economics-and-developer-growth.md` -- GPU rental rates (Lambda $2.49, CoreWeave $2.06-$3.49), electricity costs, GPU pricing trends
- v1.0 research additional_context: H100 ~400W inference draw, RTX 4090 ~350W

### Tertiary (LOW confidence)
- GPU power draw (400W for H100 inference): Based on research estimates; actual power varies significantly with workload type (inference vs training), GPU utilization, and cooling configuration
- Traditional rental rate stability: Lambda/CoreWeave prices from Q1 2026 data; GPU deflation means these rates will decrease over time (not modeled in Phase 5, but noted)

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - All openpyxl features (AreaChart, CellIsRule, ColorScaleRule, cross-sheet refs) verified in Phases 2-4
- Architecture (tab layout): HIGH - Follows established Phase 2-4 patterns exactly; column structure proven manageable at 13-14 columns
- Architecture (sensitivity table): HIGH - ColorScaleRule and matrix layout proven in Phase 4 crossover matrix
- Parameters: HIGH for existing params; MEDIUM for new rental rates (market data, but single-point-in-time)
- Cross-tab references: HIGH - Three-tab dependency is novel for this project, but each individual cross-sheet pattern is proven
- Pitfalls: HIGH - Based on Phase 2-4 implementation experience and domain analysis
- Code examples: HIGH - All formula patterns follow verified codebase conventions

**Research date:** 2026-02-06
**Valid until:** 2026-03-06 (stable domain; openpyxl unlikely to change; GPU pricing data may need refresh)

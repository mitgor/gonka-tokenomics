# Phase 4: Fee Transition Crossover Model - Research

**Researched:** 2026-02-06
**Domain:** openpyxl stacked bar charts, conditional formatting heat maps, DataValidation boolean toggles, crossover matrix layout, fee revenue modeling formulas, cross-sheet references to Emission Schedule and Token Price tabs
**Confidence:** HIGH

## Summary

This phase builds the "Fee Transition" tab -- the most analytically complex model tab so far. It must answer "when does fee revenue exceed emission value?" across a 9-cell matrix of growth rate x price scenario combinations, with danger zone flagging, a revenue split waterfall chart, a tail emission toggle, and developer count as a visible input driver.

Research covered seven technical domains: (1) new parameters required in `parameters.py` for fee growth rates, developer counts, revenue-per-developer, and tail emission toggle; (2) tab layout and 9-cell matrix structure in Excel; (3) cross-sheet formula references to both Emission Schedule and Token Price tabs; (4) stacked bar chart creation in openpyxl for the revenue split waterfall; (5) conditional formatting with `CellIsRule`, `FormulaRule`, and `ColorScaleRule` for crossover heat maps and danger zone formatting; (6) DataValidation for the tail emission ON/OFF toggle; and (7) the `fee_meta` interface dict for downstream consumers (Phase 5: Host Profitability, Phase 7: Dashboard).

All openpyxl features needed have been verified against the 3.1.5 documentation. The stacked bar chart uses `BarChart(type="col", grouping="stacked", overlap=100)`. The crossover heat map uses `CellIsRule` for green/red conditional formatting on cells where `fee_revenue > emission_value` or vice versa. The tail emission toggle uses `DataValidation(type="list", formula1='"ON,OFF"')` on the Assumptions tab with an `IF` formula in the emission calculation. `ColorScaleRule` provides three-color gradient heat maps for the crossover timing matrix.

**Primary recommendation:** Build `generators/fee_transition.py` following the established `build_*_tab()` pattern. Add 8 new parameters to `parameters.py` in a new "FEE TRANSITION" group. Structure the tab with three horizontal sections: (1) primary data table with 32 period rows, (2) 9-cell crossover matrix below the data, (3) revenue split waterfall chart and crossover heat map chart to the right.

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| openpyxl | 3.1.5 | Excel generation (charts, formulas, conditional formatting, data validation) | Already installed; sole dependency; verified in Phases 1-3 |
| openpyxl.chart.BarChart | 3.1.5 | Stacked bar charts for revenue split waterfall | Built-in; `grouping="stacked"` with `overlap=100` |
| openpyxl.formatting.rule.CellIsRule | 3.1.5 | Green/red conditional formatting for crossover cells | Already used in Phase 3 for deflationary flagging |
| openpyxl.formatting.rule.ColorScaleRule | 3.1.5 | Three-color gradient heat map for crossover timing | Built-in; provides min/mid/max color gradient |
| openpyxl.formatting.rule.FormulaRule | 3.1.5 | Formula-based conditional formatting for danger zones | Built-in; already documented in Phase 3 research |
| openpyxl.worksheet.datavalidation.DataValidation | 3.1.5 | ON/OFF toggle for tail emission | Already used in Phase 3 for scenario selector |
| openpyxl.utils.quote_sheetname | 3.1.5 | Cross-sheet references to Emission Schedule and Token Price | Already used in Phase 3 |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| openpyxl.styles.PatternFill | 3.1.5 | Static fills for danger zone columns (Y8-12) | Used alongside conditional formatting for permanent column shading |
| openpyxl.chart.Reference | 3.1.5 | Data ranges for chart series | Every chart creation |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| CellIsRule for crossover | FormulaRule | CellIsRule is simpler when comparing against a single threshold (0); FormulaRule needed for cross-cell comparisons |
| ColorScaleRule for heat map | Manual cell-by-cell PatternFill | ColorScaleRule is dynamic (updates with value changes); PatternFill is static (requires regeneration) |
| ON/OFF text toggle | TRUE/FALSE boolean | ON/OFF is more readable for leadership; TRUE/FALSE would require additional display formatting |
| Static danger zone fills | Conditional formatting only | Static fills ensure danger zone is always visible regardless of values; conditional formatting alone might not cover empty cells |

**Installation:**
```bash
pip install openpyxl==3.1.5  # Already in requirements.txt; no new dependencies
```

## Architecture Patterns

### Recommended Project Structure
```
models/
  parameters.py        # MODIFIED: Add FEE TRANSITION group (8 new parameters)
generators/
  fee_transition.py    # NEW: build_fee_transition_tab(wb, param_refs, emission_meta, price_meta) -> fee_meta
  workbook_base.py     # MODIFIED: Add tail emission toggle to Assumptions tab (after scenario selector)
  styles.py            # NO CHANGES: existing warning_cell, crossref_cell styles sufficient
  emission.py          # NO CHANGES
  token_price.py       # NO CHANGES
  chart_utils.py       # NO CHANGES
generate.py            # MODIFIED: Wire in fee_transition.build_fee_transition_tab()
```

### Pattern 1: Multi-Section Tab Layout
**What:** The Fee Transition tab has three distinct sections arranged vertically, with charts to the right.
**When to use:** When a single tab needs to present both detailed time-series data and summary matrices.

**Recommended Layout:**
```
Row 1:    [MERGED TITLE: "FEE TRANSITION CROSSOVER MODEL"]
Row 2:    [COLUMN HEADERS for data table]
Rows 3-34: [32 DATA ROWS - matching Emission/Token Price period structure]
Row 35:   [BLANK separator]
Row 36:   [SECTION HEADER: "CROSSOVER MATRIX (Fee Revenue vs Emission Value)"]
Row 37:   [Matrix column headers: "", Conservative, Moderate, Aggressive]
Row 38:   [Low Growth:    cell, cell, cell]
Row 39:   [Base Growth:   cell, cell, cell]
Row 40:   [High Growth:   cell, cell, cell]
Row 41:   [BLANK separator]
Row 42:   [SECTION HEADER: "CROSSOVER YEAR MATRIX"]
Row 43:   [Matrix column headers: "", Conservative, Moderate, Aggressive]
Row 44:   [Low Growth:    year, year, year]
Row 45:   [Base Growth:   year, year, year]
Row 46:   [High Growth:   year, year, year]

Charts (right side):
  K1:  Revenue Split Waterfall (stacked bar)
  K17: Crossover Timeline Chart (line chart, 9 series)
  K33: Fee Revenue Growth Chart (line chart)
```

### Pattern 2: 9-Cell Matrix with Explicit Scenario Combinations
**What:** A 3x3 matrix where rows = growth rates (Conservative/Moderate/Aggressive) and columns = price scenarios (Conservative/Moderate/Aggressive). Each cell shows the crossover year or fee/emission ratio.
**When to use:** REQ-M2-02 requires "3 growth rates x 3 price scenarios = 9-cell matrix."

**Layout rationale:** Rows = growth rates because growth is the "driver" variable (what Gonka can influence). Columns = price scenarios because price is the "context" variable (external market). This matches standard sensitivity analysis conventions where the controllable variable is on the Y-axis.

**Example matrix cell formula:**
```
Cell value: =IF(fee_revenue_at_year > emission_value_at_year, "CROSSED", "NOT YET")
```

**For the crossover year matrix, each cell uses a MATCH-like approach:**
```
=MATCH(1, (fee_revenue_col / emission_value_col > 1), 0)
```
However, MATCH with array criteria is complex in Excel. A simpler approach: pre-compute a "crossover flag" column (1 if fee > emission, 0 otherwise) for each of the 9 scenarios, then use MATCH to find the first 1.

**Recommended approach:** For each of the 9 scenario combinations, compute fee revenue and emission value at each period in the data table. The crossover matrix below then uses `INDEX` to look up the specific period where the ratio first exceeds 1. This avoids complex array formulas.

### Pattern 3: Data Table Column Structure (32 rows x multiple columns)
**What:** The main data table has 32 period rows (matching Emission Schedule) with columns for each scenario combination.
**When to use:** The data table is the computational engine; the 9-cell matrix below it is just a summary view.

**Recommended columns (A through V+):**
```
A: Period Label (cross-ref from Emission Schedule)
B: Developer Count (formula: base_devs * (1 + growth_rate)^year)
C: Fee Revenue - Low Growth (devs * rev_per_dev, low growth)
D: Fee Revenue - Base Growth
E: Fee Revenue - High Growth
F: Emission Value - Conservative Price (emission_GNK * conservative_price)
G: Emission Value - Moderate Price (emission_GNK * moderate_price)
H: Emission Value - Aggressive Price (emission_GNK * aggressive_price)
I: Crossover Ratio - Low/Conservative (C/F)
J: Crossover Ratio - Low/Moderate (C/G)
K: Crossover Ratio - Low/Aggressive (C/H)
L: Crossover Ratio - Base/Conservative (D/F)
M: Crossover Ratio - Base/Moderate (D/G)
N: Crossover Ratio - Base/Aggressive (D/H)
O: Crossover Ratio - High/Conservative (E/F)
P: Crossover Ratio - High/Moderate (E/G)
Q: Crossover Ratio - High/Aggressive (E/H)
R: Host Share (active_fee_revenue * 0.70)
S: AI Fund Share (active_fee_revenue * 0.20)
T: Buyback Share (active_fee_revenue * 0.05)
U: Yield Pool Share (active_fee_revenue * 0.05)
V: Tail Emission Adjustment (IF toggle ON, MAX(emission, tail_rate))
```

**IMPORTANT SIMPLIFICATION:** The above has 22 columns which is very wide. A cleaner approach:

**Simplified column structure (A through N):**
```
A: Period Label (cross-ref)
B: Developer Count
C: Fee Revenue - Low Growth ($)
D: Fee Revenue - Base Growth ($)
E: Fee Revenue - High Growth ($)
F: Emission Value ($) - uses Active Price scenario
G: Emission Value ($) - with Tail Emission adjustment
H: Crossover Ratio - Low/Active (C/G)
I: Crossover Ratio - Base/Active (D/G)
J: Crossover Ratio - High/Active (E/G)
K: Host Share (70% of D -- base growth)
L: AI Fund Share (20% of D)
M: Buyback Share (5% of D)
N: Yield Pool Share (5% of D)
```

Then the 9-cell matrix is computed separately below the data using cross-references to all three price columns from the Token Price tab. This keeps the data table manageable (14 columns) while still enabling the full 9-cell matrix.

**RECOMMENDED APPROACH (balances complexity and requirements):**

Use the **simplified 14-column data table** for period-by-period data. The 9-cell crossover matrix below it uses direct cross-sheet formulas to Token Price tab columns B/C/D (Conservative/Moderate/Aggressive prices) and computes fee_revenue / (emission_GNK * scenario_price) for each cell. This avoids duplicating all 9 ratio columns in the main table.

### Pattern 4: Tail Emission Toggle on Assumptions Tab
**What:** A boolean ON/OFF toggle on the Assumptions tab that adds a floor emission of 10,000 GNK/day when activated.
**When to use:** REQ-M2-06 requires tail emission as a toggle.

**Implementation:**
```python
# On Assumptions tab (in workbook_base.py, after scenario selector)
# Add "TAIL EMISSION" section
ws.cell(row=current_row, column=1, value="Tail Emission Toggle")
toggle_cell = ws.cell(row=current_row, column=2, value="OFF")
toggle_cell.style = "input_cell"

dv = DataValidation(
    type="list",
    formula1='"ON,OFF"',
    allow_blank=False,
)
dv.prompt = "Enable or disable tail emission"
dv.promptTitle = "Tail Emission"
ws.add_data_validation(dv)
dv.add(toggle_cell)

param_refs["Tail Emission Toggle"] = f"Assumptions!$B${current_row}"
```

**Usage in formulas:**
```
=IF(Assumptions!$B$XX="ON", MAX(emission_formula, tail_rate_ref * days), emission_formula)
```

Where `tail_rate_ref` points to the existing "Tail Emission Rate (Contingency)" parameter (10,000 GNK/day).

### Pattern 5: Revenue Split Waterfall as Stacked Bar Chart
**What:** A stacked bar chart showing 70/20/5/5 revenue allocation at each time period.
**When to use:** REQ-M2-04 requires "stacked bar showing Host share, AI Fund, Buyback, Yield Pool at each revenue level."

**Implementation:**
```python
from openpyxl.chart import BarChart, Reference

chart = BarChart()
chart.type = "col"
chart.grouping = "stacked"
chart.overlap = 100  # CRITICAL: must be 100 for proper stacking
chart.title = "Revenue Split Waterfall (70/20/5/5)"
chart.y_axis.title = "USD"
chart.x_axis.title = "Period"
chart.style = 13
chart.width = 20
chart.height = 12

# Add 4 series: Host (K), AI Fund (L), Buyback (M), Yield Pool (N)
for col_key in ("host_share", "ai_fund_share", "buyback_share", "yield_share"):
    col_num = col_to_num(meta["cols"][col_key])
    data = Reference(ws, min_col=col_num, min_row=meta["header_row"],
                     max_row=meta["data_end_row"])
    chart.add_data(data, titles_from_data=True)

cats = Reference(ws, min_col=1, min_row=meta["data_start_row"],
                 max_row=meta["data_end_row"])
chart.set_categories(cats)

ws.add_chart(chart, "P1")  # Right of data columns
```

### Pattern 6: Conditional Formatting for Crossover Heat Map
**What:** Green cells where fees > emissions (ratio > 1), red cells where fees < emissions (ratio < 1).
**When to use:** REQ-M2-03, REQ-D02.

**Implementation for crossover ratio columns:**
```python
from openpyxl.formatting.rule import CellIsRule, ColorScaleRule
from openpyxl.styles import PatternFill, Font

# Green: fee revenue exceeds emission value (crossover achieved)
green_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
green_font = Font(name="Calibri", size=11, color="006100")

# Red: fee revenue below emission value (not yet crossed)
red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
red_font = Font(name="Calibri", size=11, color="9C0006")

# Apply to crossover ratio columns (H:J in simplified layout)
for col_letter in ("H", "I", "J"):
    cell_range = f"{col_letter}{data_start_row}:{col_letter}{data_end_row}"

    # Green when ratio >= 1 (fees exceed emissions)
    ws.conditional_formatting.add(
        cell_range,
        CellIsRule(
            operator="greaterThanOrEqual",
            formula=["1"],
            fill=green_fill,
            font=green_font,
        ),
    )

    # Red when ratio < 1 (fees below emissions)
    ws.conditional_formatting.add(
        cell_range,
        CellIsRule(
            operator="lessThan",
            formula=["1"],
            fill=red_fill,
            font=red_font,
        ),
    )
```

**For the 9-cell crossover matrix (color scale gradient):**
```python
from openpyxl.formatting.rule import ColorScaleRule

# Three-color scale: Red (early crossover = bad) -> Yellow -> Green (late = good)
# Actually inverted: Green = crossed (ratio > 1), Red = not crossed
# For the crossover YEAR matrix, use ColorScaleRule for gradient:
matrix_range = "B44:D46"  # The 3x3 matrix cells
ws.conditional_formatting.add(
    matrix_range,
    ColorScaleRule(
        start_type="min", start_color="FF0000",    # Red (worst)
        mid_type="percentile", mid_value=50, mid_color="FFFF00",  # Yellow (middle)
        end_type="max", end_color="00FF00",         # Green (best)
    ),
)
```

### Pattern 7: Danger Zone Formatting (Year 8-12)
**What:** Red shading on columns corresponding to Year 8-12 with annotation.
**When to use:** REQ-M2-05 requires "red shading on danger zone columns with annotation."

**Implementation approach:** The period structure is 24 monthly + 8 annual. Year 8 starts at row index 29 (row 3+24+5=32 in 1-based, which is data row for "Year 8"). Year 8 = index 29 (row 32), Year 9 = index 30 (row 33), Year 10 = index 31 (row 34).

Wait -- let me recalculate. The 32 periods are:
- i=0..23: Y1 M01 through Y2 M12 (rows 3-26)
- i=24: Year 3 (row 27)
- i=25: Year 4 (row 28)
- i=26: Year 5 (row 29)
- i=27: Year 6 (row 30)
- i=28: Year 7 (row 31)
- i=29: Year 8 (row 32)
- i=30: Year 9 (row 33)
- i=31: Year 10 (row 34)

So Year 8-10 are rows 32-34 (the last 3 data rows). Year 11-12 are BEYOND the current data range.

**Solution:** Apply static `warning_cell` style (red background) to rows 32-34 (Year 8-10). Add a text annotation in a merged cell below the data noting "DANGER ZONE: Year 8-10. Emission rewards at 22% of initial. Fee revenue must dominate."

For Year 11-12 which are beyond the 10-year model range: add an annotation noting that the model covers 10 years and Y11-12 represent even higher risk.

```python
from generators.styles import WARNING_FILL_COLOR, WARNING_FONT_COLOR

# Apply danger zone shading to Year 8-10 rows (rows 32-34)
danger_start = 32  # Year 8
danger_end = 34    # Year 10

for row in range(danger_start, danger_end + 1):
    for col in range(1, last_col + 1):
        cell = ws.cell(row=row, column=col)
        # Only apply fill, preserve existing number format/style
        cell.fill = PatternFill(
            start_color=WARNING_FILL_COLOR,
            end_color=WARNING_FILL_COLOR,
            fill_type="solid",
        )
```

### Anti-Patterns to Avoid
- **Computing values in Python instead of Excel formulas:** ALL values must be Excel formulas referencing the Assumptions tab. Python computes nothing.
- **Duplicating emission data into the fee tab:** Use cross-sheet references to `'Emission Schedule'!D{row}` for mining emission data.
- **Hardcoding growth rates in formulas:** All growth rates come from `param_refs` (Assumptions tab).
- **Using TRUE/FALSE for the toggle:** Leadership prefers readable "ON"/"OFF" text. TRUE/FALSE would work but is less user-friendly.
- **One giant table for all 9 scenarios:** Too many columns (22+). Use a compact data table with the active scenario, plus a separate 9-cell summary matrix.
- **Stacked bar without overlap=100:** Without this setting, bars render side-by-side instead of stacked.
- **Applying conditional formatting to the entire sheet:** Target specific cell ranges to avoid performance issues and unintended formatting.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Stacked bar chart | Manual cell coloring to simulate bars | `BarChart(grouping="stacked", overlap=100)` | Native Excel chart; interactive; auto-updates with data |
| Green/red crossover formatting | Python-computed fill colors | `CellIsRule(operator="greaterThanOrEqual", formula=["1"])` | Dynamic; updates when assumptions change |
| Heat map gradient | Manual color assignment per cell | `ColorScaleRule(start_color, mid_color, end_color)` | Automatic gradient based on cell values |
| Boolean toggle | Custom input parsing | `DataValidation(type="list", formula1='"ON,OFF"')` | Standard dropdown; user-friendly; validated |
| Crossover year detection | Python-computed crossover | Excel `MATCH(1, range>1, 0)` or `COUNTIF`-based formula | Self-calculating; updates when assumptions change |
| Revenue split calculation | Separate computed columns | `=fee_revenue * param_ref` for each split | References Assumptions tab directly |
| Danger zone annotation | Manual text placement | Merged cell below data with `warning_cell` style | Consistent with project style conventions |

**Key insight:** The 9-cell crossover matrix looks complex but is just 9 cells, each containing a ratio formula. The complexity is in the data table structure and cross-sheet references, not in the matrix itself.

## Common Pitfalls

### Pitfall 1: Stacked Bar Overlap Not Set to 100
**What goes wrong:** Bars render side-by-side (clustered) instead of stacked, making the waterfall unreadable.
**Why it happens:** `BarChart` defaults to `grouping="clustered"` and `overlap=0`. Setting `grouping="stacked"` without `overlap=100` can produce partially overlapping bars.
**How to avoid:** Always set both: `chart.grouping = "stacked"` AND `chart.overlap = 100`.
**Warning signs:** Revenue split chart shows 4 separate bars per period instead of one stacked bar.

### Pitfall 2: Tail Emission Toggle Not Propagating to All Formulas
**What goes wrong:** The ON/OFF toggle only affects some calculations, leaving others showing the base emission without the tail floor.
**Why it happens:** Multiple formulas reference emission data, and not all are wrapped in the `IF(toggle="ON", MAX(...), ...)` guard.
**How to avoid:** Create a single "Effective Emission" column (column G in the simplified layout) that applies the tail emission logic once. All downstream formulas reference this column, not the raw emission.
**Warning signs:** Toggling tail emission ON changes some values but not others; inconsistent crossover calculations.

### Pitfall 3: Cross-Sheet Reference Row Misalignment
**What goes wrong:** Fee Transition tab row 3 references Emission Schedule row 4 (or similar off-by-one), causing all crossover calculations to be wrong.
**Why it happens:** Different tabs may have different header row counts, or the loop counter is off by one.
**How to avoid:** Use `emission_meta["data_start_row"]` and `price_meta["data_start_row"]` consistently. Both are 3 in the current codebase. Assert alignment: `assert emission_meta["data_start_row"] == price_meta["data_start_row"] == 3`.
**Warning signs:** Crossover ratios that seem implausible (e.g., Year 1 showing crossed when it shouldn't).

### Pitfall 4: Developer Count Formula Not Handling Monthly vs Annual Periods
**What goes wrong:** Developer count grows monthly for Y1-Y2 but annually for Y3-Y10. If the formula applies annual growth to monthly periods, developer count explodes.
**Why it happens:** The 32 periods have different durations: first 24 are monthly (30 days), last 8 are annual (365 days).
**How to avoid:** Developer count formula must account for period duration:
- Monthly periods (i=0..23): `base_devs * (1 + annual_growth)^(i/12)`
- Annual periods (i=24..31): `base_devs * (1 + annual_growth)^(2 + (i-24))`
Or simpler: compute developer count at each period's START epoch divided by 365 to get fractional years.
**Warning signs:** Developer count jumps dramatically at the monthly-to-annual transition (row 27, Year 3).

### Pitfall 5: Fee Revenue Formula Double-Counting Period Duration
**What goes wrong:** Fee revenue formula multiplies by period days when it should represent the total for that period, or vice versa.
**Why it happens:** Confusion between "annual fee revenue" and "period fee revenue." If dev_count * rev_per_dev gives annual revenue, you must divide by periods_per_year for monthly rows.
**How to avoid:** Define the formula clearly:
```
period_fee_revenue = dev_count * annual_rev_per_dev * (period_days / 365)
```
This naturally handles both monthly (30/365) and annual (365/365 = 1) periods.
**Warning signs:** Monthly fee revenue values that are 12x too high, or annual values that are 1/12 of expected.

### Pitfall 6: Conditional Formatting Order Matters
**What goes wrong:** Green formatting always wins over red (or vice versa) because one rule overrides the other.
**Why it happens:** Excel applies conditional formatting rules in order. If "green when >= 1" is added before "red when < 1", and a cell is exactly 1, both could apply but green wins (first match).
**How to avoid:** Add the "green" rule first (higher priority), then "red" rule. For the crossover ratio, >=1 is green (crossed) and <1 is red (not crossed). These are mutually exclusive, so order doesn't actually matter, but add green first for clarity.
**Warning signs:** All cells appear one color even when values span both sides of the threshold.

### Pitfall 7: ColorScaleRule Treats Blank/Zero Cells Oddly
**What goes wrong:** The 9-cell crossover year matrix shows unexpected colors because some cells contain 0 or formula errors.
**Why it happens:** `ColorScaleRule` assigns colors based on the actual value distribution. A zero or `#N/A` in one cell shifts the entire gradient.
**How to avoid:** Ensure all 9 matrix cells always contain a valid number. Use `IFERROR` wrappers: `=IFERROR(formula, 99)` where 99 represents "no crossover within model horizon."
**Warning signs:** One cell has a wildly different color from what its value suggests.

## Code Examples

### New Parameters for parameters.py
```python
# Source: Domain analysis from Phase 1 research (fee-transition-stress-test.md)
# Add to PARAM_GROUPS in parameters.py:

("FEE TRANSITION", [
    {
        "name": "Revenue Per Developer (Annual)",
        "value": 36_000,
        "unit": "USD/yr",
        "source": "Derived ($3K/mo avg)",
        "format": "currency",
    },
    {
        "name": "Low Dev Growth Rate",
        "value": 0.10,
        "unit": "annual",
        "source": "Rec #4 (Conservative)",
        "format": "percent",
    },
    {
        "name": "Base Dev Growth Rate",
        "value": 0.25,
        "unit": "annual",
        "source": "Rec #4 (Moderate)",
        "format": "percent",
    },
    {
        "name": "High Dev Growth Rate",
        "value": 0.40,
        "unit": "annual",
        "source": "Rec #4 (Aggressive)",
        "format": "percent",
    },
    {
        "name": "Base Active Developers",
        "value": 2_200,
        "unit": "developers",
        "source": "Network Data",
        "format": "integer",
    },
    {
        "name": "Tail Emission Toggle",
        "value": "OFF",
        "unit": "",
        "source": "Rec #1",
        "format": "text",
    },
]),
```

**NOTE:** "Base Active Developers" already exists in the DEVELOPER GROWTH group. The "Tail Emission Rate (Contingency)" (10,000 GNK/day) already exists in EMISSION PARAMETERS. The three growth rates (Conservative/Moderate/Aggressive Dev Growth) also already exist in DEVELOPER GROWTH. So the new parameters needed are:

1. **"Revenue Per Developer (Annual)"** -- NEW, $36,000/yr ($3K/month average)
2. **"Tail Emission Toggle"** -- NEW, needs special handling as text input (not numeric)

The existing parameters that Phase 4 will reference:
- `"Base Active Developers"` (2,200) -- already in DEVELOPER GROWTH
- `"Conservative Dev Growth"` (0.10) -- already in DEVELOPER GROWTH
- `"Moderate Dev Growth"` (0.25) -- already in DEVELOPER GROWTH
- `"Aggressive Dev Growth"` (0.40) -- already in DEVELOPER GROWTH
- `"Tail Emission Rate (Contingency)"` (10,000 GNK/day) -- already in EMISSION PARAMETERS
- `"Host Share"` (0.70) -- already in REVENUE ALLOCATION
- `"AI Training Fund"` (0.20) -- already in REVENUE ALLOCATION
- `"Buyback-Burn"` (0.05) -- already in REVENUE ALLOCATION
- `"veGNK Yield Pool"` (0.05) -- already in REVENUE ALLOCATION

### Tail Emission Toggle on Assumptions Tab
```python
# Source: Verified against openpyxl 3.1.5 DataValidation API
# Add to workbook_base.py _add_scenario_selector() or new _add_tail_emission_toggle()

def _add_tail_emission_toggle(ws, current_row, param_refs):
    """Add tail emission ON/OFF toggle to Assumptions tab."""
    ws.merge_cells(
        start_row=current_row, start_column=1,
        end_row=current_row, end_column=4,
    )
    section_cell = ws.cell(row=current_row, column=1, value="TAIL EMISSION")
    section_cell.style = "section_header"
    current_row += 1

    ws.cell(row=current_row, column=1, value="Tail Emission Toggle")
    toggle_cell = ws.cell(row=current_row, column=2, value="OFF")
    toggle_cell.style = "input_cell"
    toggle_cell.protection = Protection(locked=False)

    dv = DataValidation(
        type="list",
        formula1='"ON,OFF"',
        allow_blank=False,
    )
    dv.prompt = "ON enables 10,000 GNK/day floor emission"
    dv.promptTitle = "Tail Emission"
    ws.add_data_validation(dv)
    dv.add(toggle_cell)

    param_refs["Tail Emission Toggle"] = f"Assumptions!$B${current_row}"
    current_row += 1

    return current_row
```

### Complete build_fee_transition_tab Signature
```python
# Source: Follows Phase 2-3 established pattern
def build_fee_transition_tab(wb, param_refs, emission_meta, price_meta):
    """Create the 'Fee Transition' worksheet with crossover analysis.

    Args:
        wb: An openpyxl Workbook with styles already registered.
        param_refs: dict mapping parameter names to "Assumptions!$B$N".
                    Must include tail emission toggle and scenario selector refs.
        emission_meta: dict from build_emission_tab() with sheet coordinates.
        price_meta: dict from build_token_price_tab() with sheet coordinates.

    Returns:
        fee_meta: dict with keys:
        {
            "sheet_name": "Fee Transition",
            "header_row": 2,
            "data_start_row": 3,
            "data_end_row": 34,
            "cols": {
                "period_label": "A",
                "developer_count": "B",
                "fee_rev_low": "C",
                "fee_rev_base": "D",
                "fee_rev_high": "E",
                "emission_value": "F",
                "effective_emission_value": "G",
                "crossover_ratio_low": "H",
                "crossover_ratio_base": "I",
                "crossover_ratio_high": "J",
                "host_share": "K",
                "ai_fund_share": "L",
                "buyback_share": "M",
                "yield_share": "N",
            },
            "matrix_start_row": 37,
            "matrix_end_row": 40,
            "crossover_year_matrix_start_row": 43,
            "crossover_year_matrix_end_row": 46,
            "danger_zone_rows": [32, 33, 34],
        }
    """
```

### Fee Revenue Formula Pattern
```python
# Source: Phase 1 research (fee-transition-stress-test.md) + domain analysis

# Developer count at each period:
# dev_count = base_devs * (1 + growth_rate) ^ (start_epoch / 365)
# For growth_rate, use one of: low (0.10), base (0.25), high (0.40)

base_devs_ref = param_refs["Base Active Developers"]
low_growth_ref = param_refs["Conservative Dev Growth"]
base_growth_ref = param_refs["Moderate Dev Growth"]
high_growth_ref = param_refs["Aggressive Dev Growth"]
rev_per_dev_ref = param_refs["Revenue Per Developer (Annual)"]

for i in range(32):
    row = 3 + i
    es_row = emission_meta["data_start_row"] + i

    # Developer count (using base growth for visibility -- REQ-M2-07)
    # Uses Start Epoch from Emission Schedule to compute fractional years
    es_sheet = quote_sheetname(emission_meta["sheet_name"])
    start_epoch_ref = f"{es_sheet}!B{es_row}"
    dev_formula = f"={base_devs_ref}*(1+{base_growth_ref})^({start_epoch_ref}/365)"
    ws.cell(row=row, column=2, value=dev_formula).style = "integer"

    # Fee revenue for each growth scenario:
    # fee_rev = base_devs * (1+growth)^(epoch/365) * rev_per_dev * (days/365)
    days = 30 if i < 24 else 365

    for col, growth_ref in [(3, low_growth_ref), (4, base_growth_ref), (5, high_growth_ref)]:
        fee_formula = (
            f"={base_devs_ref}*(1+{growth_ref})^({start_epoch_ref}/365)"
            f"*{rev_per_dev_ref}*{days}/365"
        )
        ws.cell(row=row, column=col, value=fee_formula).style = "currency"
```

### Emission Value with Tail Emission Toggle
```python
# Source: Verified formula pattern from emission.py + tail emission logic

toggle_ref = param_refs["Tail Emission Toggle"]
tail_rate_ref = param_refs["Tail Emission Rate (Contingency)"]
tp_sheet = quote_sheetname(price_meta["sheet_name"])
active_price_col = price_meta["cols"]["active_price"]  # "F"

# Column F: Raw emission value (emission_GNK * active_price)
# Column G: Effective emission value (with tail emission adjustment)

for i in range(32):
    row = 3 + i
    es_row = emission_meta["data_start_row"] + i
    tp_row = price_meta["data_start_row"] + i
    days = 30 if i < 24 else 365

    # F: Raw emission value = mining_emission_GNK * active_price
    mining_col = emission_meta["cols"]["mining_emission"]  # "D"
    raw_emission_formula = (
        f"={es_sheet}!{mining_col}{es_row}*{tp_sheet}!{active_price_col}{tp_row}"
    )
    ws.cell(row=row, column=6, value=raw_emission_formula).style = "currency"

    # G: Effective emission value (with tail emission toggle)
    # IF toggle = "ON", use MAX(mining_emission, tail_rate * days) * price
    # IF toggle = "OFF", use mining_emission * price (same as F)
    effective_formula = (
        f'=IF({toggle_ref}="ON",'
        f"MAX({es_sheet}!{mining_col}{es_row},{tail_rate_ref}*{days})"
        f"*{tp_sheet}!{active_price_col}{tp_row},"
        f"F{row})"
    )
    ws.cell(row=row, column=7, value=effective_formula).style = "currency"
```

### 9-Cell Crossover Matrix
```python
# Source: Domain analysis - crossover matrix for 3 growth x 3 price scenarios
# Placed below the data table (rows 37-40)

# Section header
ws.merge_cells(start_row=36, start_column=1, end_row=36, end_column=5)
ws.cell(row=36, column=1, value="CROSSOVER MATRIX (Fees/Emission Ratio at Year 10)").style = "section_header"

# Column headers
ws.cell(row=37, column=1, value="Growth \\ Price")
for j, label in enumerate(["Conservative", "Moderate", "Aggressive"], start=2):
    ws.cell(row=37, column=j, value=label).style = "header"

# Row labels
growth_labels = ["Low Growth (10%)", "Base Growth (25%)", "High Growth (40%)"]
growth_refs = [
    param_refs["Conservative Dev Growth"],
    param_refs["Moderate Dev Growth"],
    param_refs["Aggressive Dev Growth"],
]

# Price columns from Token Price tab
price_cols = [
    price_meta["cols"]["conservative_price"],   # "B"
    price_meta["cols"]["moderate_price"],        # "C"
    price_meta["cols"]["aggressive_price"],      # "D"
]

# Year 10 is the last data row (row 34 = data_end_row)
yr10_row = price_meta["data_end_row"]  # 34
yr10_es_row = emission_meta["data_end_row"]  # 34

for r, (label, growth_ref) in enumerate(zip(growth_labels, growth_refs)):
    matrix_row = 38 + r
    ws.cell(row=matrix_row, column=1, value=label)

    for c, price_col in enumerate(price_cols):
        matrix_col = 2 + c
        # Fee revenue at Year 10 for this growth scenario:
        # = base_devs * (1+growth)^10 * rev_per_dev
        # Emission value at Year 10 for this price scenario:
        # = mining_emission_at_yr10 * price_at_yr10

        fee_formula = f"{base_devs_ref}*(1+{growth_ref})^10*{rev_per_dev_ref}"
        emission_formula = (
            f"{es_sheet}!{mining_col}{yr10_es_row}*365"
            f"*{tp_sheet}!{price_col}{yr10_row}"
        )

        # Ratio: fee / emission (>1 means crossed)
        cell = ws.cell(
            row=matrix_row, column=matrix_col,
            value=f"={fee_formula}/({emission_formula})",
        )
        cell.style = "number"
        cell.number_format = "0.00x"
```

### Danger Zone Static Formatting
```python
# Source: styles.py WARNING_FILL_COLOR, WARNING_FONT_COLOR
from openpyxl.styles import PatternFill

danger_fill = PatternFill(
    start_color="FFC7CE",  # WARNING_FILL_COLOR
    end_color="FFC7CE",
    fill_type="solid",
)

# Year 8 = row 32, Year 9 = row 33, Year 10 = row 34
for row in range(32, 35):
    for col in range(1, last_col + 1):
        cell = ws.cell(row=row, column=col)
        cell.fill = danger_fill

# Danger zone annotation
ws.merge_cells(start_row=35, start_column=1, end_row=35, end_column=5)
annotation = ws.cell(
    row=35, column=1,
    value="DANGER ZONE: Year 8-10. Emission rewards at 10-22% of initial. "
          "Fee revenue must provide >80% of host income.",
)
annotation.style = "warning_cell"
```

### Crossover Heat Map Conditional Formatting
```python
# Source: Verified against openpyxl 3.1.5 ColorScaleRule and CellIsRule API

# 1. Crossover ratio columns (H:J) - green/red binary
green_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
green_font = Font(name="Calibri", size=11, color="006100")
red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
red_font = Font(name="Calibri", size=11, color="9C0006")

for col_letter in ("H", "I", "J"):
    rng = f"{col_letter}3:{col_letter}34"
    ws.conditional_formatting.add(rng, CellIsRule(
        operator="greaterThanOrEqual", formula=["1"],
        fill=green_fill, font=green_font,
    ))
    ws.conditional_formatting.add(rng, CellIsRule(
        operator="lessThan", formula=["1"],
        fill=red_fill, font=red_font,
    ))

# 2. 9-cell crossover matrix - three-color gradient
matrix_range = "B38:D40"
ws.conditional_formatting.add(matrix_range, ColorScaleRule(
    start_type="num", start_value=0, start_color="FFC7CE",    # Red (low ratio)
    mid_type="num", mid_value=1, mid_color="FFEB84",          # Yellow (crossover point)
    end_type="num", end_value=5, end_color="C6EFCE",          # Green (well past crossover)
))
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Single crossover point | 9-cell matrix across scenarios | This phase | Prevents false confidence from a single misleading number |
| Fixed emission schedule | Tail emission toggle | This phase | Enables leadership to see impact of contingency plan |
| Hidden fee assumptions | Developer count as visible driver | This phase | Makes the growth assumption transparent and editable |
| Annual-only projections | 24 monthly + 8 annual granularity | Established Phase 2 | Early-period detail, long-term overview |

**Deprecated/outdated:**
- Single crossover point: Misleading because it depends on both growth and price assumptions
- "Assumed Annual Fee Revenue" placeholder from Phase 3: Phase 4 replaces this with calculated fee revenue from developer count * revenue per developer

## Open Questions

1. **Revenue Per Developer Estimate**
   - What we know: Phase 1 research shows fee scenarios ranging from $72M-$684M annually. At 2,200 developers, that is $33K-$311K per developer per year.
   - What's unclear: The $36,000/year ($3,000/month) estimate for "Revenue Per Developer (Annual)" is a rough midpoint. The actual number depends on average inference volume per developer and pricing.
   - Recommendation: Use $36,000 as the default but make it an editable input on the Assumptions tab. Leadership can adjust based on actual network data.

2. **Developer Count Row vs Developer Count per Growth Scenario**
   - What we know: REQ-M2-07 says "developer count as visible driver -- input row for developer count per year feeding into fee revenue."
   - What's unclear: Should column B show developer count for the base growth scenario only (simple), or should there be three developer count columns (one per growth rate)?
   - Recommendation: Show ONE developer count column using the base growth rate (25%) for visibility. The three fee revenue columns (C/D/E) each use their own growth rate internally. This keeps the developer count visible without tripling the column count.

3. **How the 9-Cell Matrix Handles Time Dimension**
   - What we know: The matrix needs to show crossover across 3x3 scenarios. But crossover is a TIME-dependent phenomenon (it happens at a specific year).
   - What's unclear: Should each matrix cell show the crossover YEAR, the crossover RATIO at Year 10, or a boolean (crossed/not crossed)?
   - Recommendation: Create TWO matrices. First: "Fees/Emission Ratio at Year 10" (shows magnitude). Second: "Crossover Year" (shows timing, using MATCH to find first period where ratio > 1). Both get conditional formatting.

4. **Relationship Between Active Scenario Selector and 9-Cell Matrix**
   - What we know: The scenario selector on Assumptions drives the "Active Price" column. But the 9-cell matrix explicitly shows ALL price scenarios.
   - What's unclear: Does the crossover ratio column in the data table use the Active Price (from dropdown) or all three prices?
   - Recommendation: The data table crossover ratios (columns H/I/J) use the Active Price (from dropdown) for the emission value, but the 9-cell matrix below uses ALL three prices explicitly. This gives leadership both: a detailed view (data table with active scenario) and a comparison view (matrix with all combinations).

5. **Updating Phase 3's Buyback-Burn to Use Phase 4 Fee Revenue**
   - What we know: Phase 3 Token Price tab uses "Assumed Annual Fee Revenue" ($1M placeholder) for the buyback-burn calculation.
   - What's unclear: Should Phase 4 retroactively update the Token Price tab's buyback formula to reference fee transition data, or leave Phase 3 as-is?
   - Recommendation: Leave Phase 3 as-is for now. The "Assumed Annual Fee Revenue" remains a simple placeholder that leadership can manually adjust. Phase 7 (Dashboard) can reconcile the two. Changing Phase 3 formulas in Phase 4 risks breaking the established tab.

## Sources

### Primary (HIGH confidence)
- openpyxl 3.1.5 BarChart documentation -- [bar chart types including stacked](https://openpyxl.readthedocs.io/en/stable/charts/bar.html) -- verified `grouping="stacked"` and `overlap=100`
- openpyxl 3.1.5 conditional formatting documentation -- [CellIsRule, FormulaRule, ColorScaleRule](https://openpyxl.readthedocs.io/en/stable/formatting.html) -- verified all three rule types
- openpyxl 3.1.5 DataValidation documentation -- [list validation for dropdowns](https://openpyxl.readthedocs.io/en/stable/validation.html) -- verified `type="list"` with `formula1='"ON,OFF"'`
- Existing codebase: `generators/emission.py`, `generators/token_price.py` -- established patterns for build_*_tab(), meta dicts, cross-sheet references
- Existing codebase: `models/parameters.py` -- existing parameter groups, confirmed DEVELOPER GROWTH and EMISSION PARAMETERS groups already contain most needed params

### Secondary (MEDIUM confidence)
- Phase 1 research: `research/04-fee-transition-stress-test.md` -- crossover analysis framework, scenario definitions, host profitability thresholds
- Phase 1 research: `research/05-gpu-economics-and-developer-growth.md` -- developer growth rates, revenue per developer estimates
- Phase 1 research: `research/02-real-yield-and-buybacks.md` -- 70/20/5/5 revenue allocation rationale

### Tertiary (LOW confidence)
- Revenue Per Developer estimate ($36,000/year) -- derived from Phase 1 research scenarios but not empirically validated against actual Gonka network data

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - openpyxl 3.1.5 features verified against official documentation
- Architecture (tab layout): HIGH - follows established Phase 2-3 patterns, verified column structure
- Architecture (9-cell matrix): MEDIUM - novel for this project, formula patterns verified but exact layout may need adjustment during implementation
- Parameters: HIGH for existing params, MEDIUM for new "Revenue Per Developer" estimate
- Pitfalls: HIGH - based on verified openpyxl behavior and Phase 2-3 implementation experience
- Code examples: HIGH - all formula patterns verified against openpyxl API and existing codebase conventions
- Danger zone rows: HIGH - period structure is established and row indices are deterministic

**Research date:** 2026-02-06
**Valid until:** 2026-03-06 (stable domain; openpyxl unlikely to change)

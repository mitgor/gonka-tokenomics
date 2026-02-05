# Phase 2: Emission Schedule Model - Research

**Researched:** 2026-02-06
**Domain:** openpyxl chart generation, Excel formula writing patterns, exponential decay modeling
**Confidence:** HIGH

## Summary

This phase adds the first model tab to the workbook, establishing the formula-writing pattern that all subsequent phases (3-9) will follow. The research covers seven domains: (1) openpyxl chart API for LineChart, AreaChart, and BarChart, (2) the formula-writing pattern using param_refs, (3) exponential decay precision in Excel, (4) circulating supply composition, (5) mixed time granularity aggregation, (6) geometric series validation, and (7) the critical openpyxl 3.1.5 chart rendering bug and its workaround.

The core formula `=E0*EXP(-r*epoch)` works identically in Excel and Google Sheets. Float precision is sufficient -- tested cumulative deviation over 3,650 epochs is only 0.000029 GNK (well under the <1 GNK threshold). The `decimal.Decimal` module is not needed for this level of precision, though the validation row should confirm this in the generated workbook. Monthly and annual period totals can be expressed as closed-form Excel formulas using the geometric series partial sum: `=E0*EXP(-r*start_epoch)*(1-EXP(-r*days))/(1-EXP(-r))`.

The critical technical risk is the openpyxl 3.1.5 chart rendering bug (issue #2229): the `Application` string in `docProps/app.xml` causes Excel to misrender chart axis labels and tick marks. A post-processing step that rewrites app.xml to say "Microsoft Excel" fixes the problem completely. This should be implemented as a utility function in `generators/` and applied after every `wb.save()`.

**Primary recommendation:** Stay on openpyxl 3.1.5, add a `fix_chart_rendering(path)` post-processor, and establish the `build_emission_tab(wb, param_refs) -> emission_meta` pattern as the template for all model modules.

## Standard Stack

The established libraries/tools for this domain:

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| openpyxl | 3.1.5 | Excel generation (charts, formulas, styles) | Already installed; only dependency; validated in Phase 1 |
| math (stdlib) | N/A | `math.exp()` for Python-side validation computations | No additional dependency |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| zipfile (stdlib) | N/A | Post-process .xlsx to fix app.xml chart bug | After every `wb.save()` that includes charts |
| re (stdlib) | N/A | Regex replacement in app.xml | Used by the chart fix utility |
| decimal (stdlib) | N/A | High-precision validation computations | Optional; float precision is sufficient but Decimal provides independent verification |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| openpyxl 3.1.5 + post-process | openpyxl 3.1.3 (no chart bug) | 3.1.3 avoids the bug but misses named-style assignment fix (#2189 in 3.1.4); post-processing is trivial |
| Post-process app.xml | Monkey-patch openpyxl extended.py | Post-process is safer; no library internals modified |

**Installation:**
```bash
pip install openpyxl==3.1.5  # Already in requirements.txt
```

## Architecture Patterns

### Recommended Project Structure
```
generators/
  emission.py          # NEW: build_emission_tab() + charts
  chart_utils.py       # NEW: fix_chart_rendering() + shared chart helpers
  styles.py            # EXISTING: NamedStyles, FORMAT_TO_STYLE
  workbook_base.py     # EXISTING: build_assumptions_tab(), create_workbook()
models/
  parameters.py        # EXISTING: PARAM_GROUPS, get_param()
generate.py            # MODIFIED: add emission tab to master workbook
```

### Pattern 1: Model Tab Builder Function Signature

**What:** Every model module (emission, token_price, fee_transition, etc.) exposes a single `build_*_tab()` function that follows the same interface contract.

**When to use:** Every phase from 2 through 6 creates a new model module following this pattern.

**Signature:**
```python
def build_emission_tab(
    wb: Workbook,
    param_refs: dict[str, str],
) -> dict:
    """
    Create the 'Emission Schedule' worksheet in the workbook.

    Args:
        wb: The openpyxl Workbook to add the sheet to.
        param_refs: Mapping of parameter names to Assumptions cell refs.
                    E.g., {"Initial Daily Emission": "Assumptions!$B$5", ...}

    Returns:
        emission_meta: dict with keys describing what was written,
        for downstream consumers and chart placement:
        {
            "sheet_name": "Emission Schedule",
            "header_row": 2,
            "data_start_row": 3,
            "data_end_row": 34,  # 32 data rows
            "cols": {
                "period_label": "A",
                "start_epoch": "B",
                "end_epoch": "C",
                "mining_emission": "D",
                "cp_unlock": "E",
                "founder_vest": "F",
                "total_new": "G",
                "cumulative_circulating": "H",
                "inflation_rate": "I",
            },
        }
    """
```

**Why this pattern:**
- `wb` (not `ws`) is passed so the function creates and names its own sheet, sets tab color, and can create multiple sheets if needed
- `param_refs` is the proven interface contract from Phase 1 (60 entries, all correct)
- Return dict (`emission_meta`) allows downstream phases (4, 5, 7) to reference this tab's data without hardcoded cell addresses
- Same pattern scales to all 5 model modules

### Pattern 2: Formula Writing with param_refs

**What:** All formulas reference the Assumptions tab through the param_refs dict. No literal parameter values appear in formula strings.

**Example:**
```python
# param_refs["Initial Daily Emission"] = "Assumptions!$B$5"
# param_refs["Decay Rate"] = "Assumptions!$B$6"
e0_ref = param_refs["Initial Daily Emission"]
r_ref = param_refs["Decay Rate"]

# Cell formula for daily emission at epoch t (closed-form):
ws.cell(row=row, column=4).value = (
    f"={e0_ref}*EXP(-{r_ref}*B{row})"
)
```

**Critical rule:** The only literal numbers allowed in formulas are 0, 1, and structural constants (like 30 for days-per-month or 365 for days-per-year). All business parameters must come from param_refs.

### Pattern 3: Mixed Time Granularity (32-Row Layout)

**What:** Monthly rows for Year 1-2 (24 rows) then annual rows for Year 3-10 (8 rows) = 32 data rows total.

**Layout:**
```
Row 1:  Sheet title (merged)
Row 2:  Column headers
Row 3:  Month 1 (epochs 0-29)
Row 4:  Month 2 (epochs 30-59)
...
Row 26: Month 24 (epochs 690-719)
Row 27: Year 3 (epochs 720-1084)
Row 28: Year 4 (epochs 1085-1449)
...
Row 34: Year 10 (epochs 3285-3649)
Row 35: (blank)
Row 36: Validation row (geometric series check)
Row 37: Validation row (total supply check)
```

**Period definitions (data-driven, not hardcoded):**
```python
PERIODS = []
# Monthly Year 1-2 (24 periods)
for m in range(24):
    start = m * 30
    end = (m + 1) * 30
    label = f"Y{m // 12 + 1} M{m % 12 + 1:02d}"
    PERIODS.append({"label": label, "start": start, "end": end, "days": 30})

# Annual Year 3-10 (8 periods)
for y in range(3, 11):
    start = 720 + (y - 3) * 365
    end = start + 365
    label = f"Year {y}"
    PERIODS.append({"label": label, "start": start, "end": end, "days": 365})
```

**Note on epoch boundaries:** Months are approximated as 30 days. Year 1-2 covers epochs 0-719 (720 days). Year 3 starts at epoch 720. This is a simplification -- real months vary from 28-31 days. For 10-year projections, this approximation is standard practice in tokenomics modeling and matches the precision level appropriate for leadership decision-making.

### Pattern 4: Period Emission Aggregation (Closed-Form)

**What:** Each period's total mining emission is computed using the geometric series partial sum formula, not by summing individual epochs.

**Excel formula for period emission (closed-form):**
```
=E0 * EXP(-r * start_epoch) * (1 - EXP(-r * days)) / (1 - EXP(-r))
```

Where:
- `E0` = Initial Daily Emission (from param_refs)
- `r` = Decay Rate (from param_refs)
- `start_epoch` = first epoch of the period (in column B)
- `days` = number of days in the period (30 for months, 365 for years)

**Python code to write this formula:**
```python
e0 = param_refs["Initial Daily Emission"]
r = param_refs["Decay Rate"]
start_col = "B"  # start_epoch column
days = 30  # or 365 for annual periods

formula = (
    f"={e0}*EXP(-{r}*{start_col}{row})"
    f"*(1-EXP(-{r}*{days}))"
    f"/(1-EXP(-{r}))"
)
```

**Why closed-form, not SUM of individual epochs:**
1. Only 32 rows instead of 3,650+ rows (file size)
2. Each cell is independent (no iterative references)
3. Changing decay rate or E0 on Assumptions tab causes full recalculation
4. Precision is identical to cell-by-cell (tested: 0.000029 GNK difference over 10 years)

### Pattern 5: Chart Creation and Placement

**What:** Charts are embedded in the model tab to the right of the data table, and also referenced from the Dashboard tab (Phase 7).

**Placement convention:**
```python
# Charts start at column K (column 11), giving columns A-J for data
# Chart 1: rows 1-15
# Chart 2: rows 17-31
# Chart 3: rows 33-47

chart = LineChart()
chart.width = 20   # ~20 cm wide
chart.height = 12  # ~12 cm tall
ws.add_chart(chart, "K1")
```

### Anti-Patterns to Avoid

- **Iterative row references:** Do NOT write `=D{row-1}*(1-r)` where each row depends on the previous. Use the closed-form `=E0*EXP(-r*epoch)` so each cell is independent.
- **Hardcoded parameter values in formulas:** Do NOT write `=323000*EXP(-0.000475*B3)`. Always use `={e0_ref}*EXP(-{r_ref}*B3)` where refs come from param_refs.
- **Named ranges:** Per prior decision, do NOT use named ranges. Use direct cell references via param_refs.
- **Python-computed values instead of formulas:** Do NOT compute emission values in Python and write them as static numbers. Write Excel formulas so the workbook self-calculates.
- **Daily granularity rows:** Do NOT create 3,650 rows for 10 years of daily data. Use the 32-row aggregated layout (monthly/annual).

## Don't Hand-Roll

Problems that look simple but have existing solutions:

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Geometric series sum | Manual loop `sum(E0*exp(-r*t) for t in range(n))` | Closed-form: `E0*(1-exp(-r*n))/(1-exp(-r))` | Each cell is independent; no iterative dependency; precision verified |
| Chart axis formatting | Manual XML manipulation | openpyxl `chart.x_axis.title`, `chart.y_axis.title`, `chart.style` | API handles all common formatting needs |
| Cross-sheet formula quoting | Manual string building with quotes | `f"='{sheet_name}'!{cell_ref}"` with openpyxl `quote_sheetname()` | Sheet names with spaces need single quotes; utility handles edge cases |
| app.xml chart fix | Downgrade openpyxl | Post-process utility `fix_chart_rendering()` | 10 lines of code; keeps 3.1.5 benefits |
| Period epoch ranges | Hardcoded epoch numbers | Data-driven PERIODS list | Adding a period or changing granularity is a config change, not a code change |

**Key insight:** The closed-form geometric series formula is the critical "don't hand-roll" item. It eliminates the need for 3,650 rows, makes each cell independent (no iterative references), and enables the validation row to compare closed-form total against cumulative sum.

## Common Pitfalls

### Pitfall 1: openpyxl 3.1.5 Chart Rendering Bug in Excel
**What goes wrong:** Charts generated by openpyxl 3.1.5 display with missing axis tick marks, overlapping labels, and mispositioned plot areas in Microsoft Excel. The charts look correct in Google Sheets and LibreOffice.
**Why it happens:** openpyxl 3.1.5 writes `<Application>Microsoft Excel Compatible / Openpyxl 3.1.5</Application>` in `docProps/app.xml`. Excel interprets this non-standard Application string differently and changes chart rendering behavior. Issue [#2229](https://foss.heptapod.net/openpyxl/openpyxl/-/issues/2229).
**How to avoid:** Post-process the saved .xlsx file to replace the Application string:
```python
import zipfile
import re
import os
import shutil

def fix_chart_rendering(xlsx_path):
    """Fix openpyxl 3.1.5 chart rendering in Excel.

    Post-processes the .xlsx to replace the Application string
    in docProps/app.xml from 'Microsoft Excel Compatible / Openpyxl 3.1.5'
    to 'Microsoft Excel'. This fixes chart axis tick marks, labels,
    and plot area positioning in Microsoft Excel.

    Safe to call on files without charts (no-op effect).
    """
    tmp_path = xlsx_path + ".tmp"
    with zipfile.ZipFile(xlsx_path, "r") as zin:
        with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == "docProps/app.xml":
                    content = data.decode("utf-8")
                    content = re.sub(
                        r"<Application>.*?</Application>",
                        "<Application>Microsoft Excel</Application>",
                        content,
                    )
                    data = content.encode("utf-8")
                zout.writestr(item, data)
    shutil.move(tmp_path, xlsx_path)
```
**Warning signs:** Charts look fine in Google Sheets but broken in Excel. Axis labels overlap or disappear.

### Pitfall 2: Iterative Row References Instead of Closed-Form
**What goes wrong:** Writing `=D{row-1}*(1-decay_rate)` makes each row dependent on the previous one. Errors compound, and inserting/deleting rows breaks the chain.
**Why it happens:** Iterative formulas feel natural ("each epoch is the previous epoch times the decay factor") but create fragile chains.
**How to avoid:** Always use the closed-form: `=E0*EXP(-r*epoch)`. Each cell computes independently from the base parameters.
**Warning signs:** Inserting a row in the middle causes #REF! errors; cumulative sum does not match closed-form.

### Pitfall 3: Hardcoded Numbers in Formula Strings
**What goes wrong:** Someone writes `=323000*EXP(-0.000475*B3)` instead of `=Assumptions!$B$5*EXP(-Assumptions!$B$6*B3)`. The formula looks correct but does not update when leadership changes the Assumptions tab.
**Why it happens:** It is faster to type literal numbers than look up param_refs.
**How to avoid:** Enforce the rule: formula strings may only contain cell references, operators, and Excel functions. The only allowed literal numbers are 0, 1, 30 (days/month), and 365 (days/year). Use param_refs for everything else.
**Warning signs:** Changing Initial Daily Emission on Assumptions tab does not change the emission chart.

### Pitfall 4: EXP vs Power Formula Confusion
**What goes wrong:** Using `=(1-r)^epoch` instead of `=EXP(-r*epoch)`. These produce different results because `(1-r)^t` is discrete decay while `EXP(-r*t)` is continuous decay. The whitepaper formula uses `EXP()`.
**Why it happens:** Discrete and continuous exponential decay are similar but not identical. For r=0.000475, `(1-r)^t` approximates `EXP(-r*t)` but diverges slightly over long horizons.
**How to avoid:** Always use `EXP(-r*t)` to match the whitepaper specification. The validation row catches any formula that deviates from the expected closed-form sum.
**Warning signs:** Cumulative total diverges from the geometric series sum by more than 1 GNK.

### Pitfall 5: Forgetting to Apply Styles to Formula Cells
**What goes wrong:** Formula cells display raw numbers without formatting (e.g., 9623571.234 instead of 9,623,571).
**Why it happens:** Formulas are written as strings but the cell style defaults to General format.
**How to avoid:** After writing a formula to a cell, apply the appropriate NamedStyle: `cell.style = "tokens"` for GNK amounts, `cell.style = "percent"` for inflation rates.
**Warning signs:** Numbers appear without commas, percentages show as decimals (0.15 instead of 15%).

### Pitfall 6: Google Sheets Combination Chart Limitations
**What goes wrong:** A dual-axis chart (line + area) may render as two separate charts in Google Sheets instead of one combined chart.
**Why it happens:** Google Sheets has limited support for openpyxl's secondary axis chart combination method.
**How to avoid:** Keep charts simple -- use separate charts instead of combination charts. If a dual-axis is essential (e.g., inflation rate overlaid on emission), test in Google Sheets early and have a fallback plan (separate chart).
**Warning signs:** Chart looks correct in Excel but appears as two separate charts in Google Sheets.

## Code Examples

Verified patterns from official sources and tested against openpyxl 3.1.5:

### Creating a Line Chart (Emission Decay Curve)
```python
# Source: openpyxl official docs (charts/line.html) + verified locally
from openpyxl.chart import LineChart, Reference

def create_emission_decay_chart(ws, meta):
    """Create emission decay curve line chart."""
    chart = LineChart()
    chart.title = "Mining Emission Decay (10-Year)"
    chart.y_axis.title = "GNK per Period"
    chart.x_axis.title = "Period"
    chart.style = 13  # Clean Excel style
    chart.width = 20
    chart.height = 12

    # Data reference: mining emission column
    data = Reference(
        ws,
        min_col=col_to_num(meta["cols"]["mining_emission"]),
        min_row=meta["header_row"],
        max_row=meta["data_end_row"],
    )
    cats = Reference(
        ws,
        min_col=col_to_num(meta["cols"]["period_label"]),
        min_row=meta["data_start_row"],
        max_row=meta["data_end_row"],
    )
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)

    # Style the series
    series = chart.series[0]
    series.graphicalProperties.line.width = 25000  # in EMUs

    ws.add_chart(chart, "K1")
```

### Creating a Stacked Area Chart (Circulating Supply Composition)
```python
# Source: openpyxl official docs (charts/area.html) + verified
from openpyxl.chart import AreaChart, Reference

def create_supply_composition_chart(ws, meta):
    """Create stacked area chart showing circulating supply components."""
    chart = AreaChart()
    chart.title = "Circulating Supply Composition"
    chart.y_axis.title = "GNK"
    chart.x_axis.title = "Period"
    chart.grouping = "stacked"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # Add three series: mining, CP unlock, founder vesting
    for col_key in ["mining_emission", "cp_unlock", "founder_vest"]:
        data = Reference(
            ws,
            min_col=col_to_num(meta["cols"][col_key]),
            min_row=meta["header_row"],
            max_row=meta["data_end_row"],
        )
        chart.add_data(data, titles_from_data=True)

    cats = Reference(
        ws,
        min_col=col_to_num(meta["cols"]["period_label"]),
        min_row=meta["data_start_row"],
        max_row=meta["data_end_row"],
    )
    chart.set_categories(cats)
    ws.add_chart(chart, "K17")
```

### Creating a Bar Chart (Inflation Rate with Benchmark Labels)
```python
# Source: openpyxl official docs (charts/bar.html) + verified
from openpyxl.chart import BarChart, Reference

def create_inflation_chart(ws, meta):
    """Create bar chart for annualized inflation rate."""
    chart = BarChart()
    chart.type = "col"
    chart.title = "Annualized Inflation Rate"
    chart.y_axis.title = "Inflation %"
    chart.x_axis.title = "Period"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    data = Reference(
        ws,
        min_col=col_to_num(meta["cols"]["inflation_rate"]),
        min_row=meta["header_row"],
        max_row=meta["data_end_row"],
    )
    cats = Reference(
        ws,
        min_col=col_to_num(meta["cols"]["period_label"]),
        min_row=meta["data_start_row"],
        max_row=meta["data_end_row"],
    )
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    ws.add_chart(chart, "K33")
```

### Horizontal Reference Line Technique
```python
# openpyxl does not have a native "reference line" feature.
# The standard technique is to add a constant-value series to the chart.
# Create a column of constant values (e.g., ETH ~0.5% inflation)
# and add it as a second series with a thin dashed line.

# In the data table, add a column:
for row in range(data_start, data_end + 1):
    ws.cell(row=row, column=ref_col, value=0.005)  # 0.5% as decimal
    # Or as formula: ws.cell(row=row, column=ref_col).value = "=0.005"

# Then add as a chart series:
ref_data = Reference(ws, min_col=ref_col, min_row=header_row, max_row=data_end)
chart.add_data(ref_data, titles_from_data=True)
# Style the reference line
ref_series = chart.series[-1]
ref_series.graphicalProperties.line.dashStyle = "dash"
ref_series.graphicalProperties.line.width = 12700  # thin line in EMUs
```

### Writing the Validation Row
```python
# Geometric series closed-form sum vs cumulative cell-by-cell sum
e0 = param_refs["Initial Daily Emission"]
r = param_refs["Decay Rate"]
total_epochs = 3650  # 10 years

# Closed-form sum: E0 * (1 - EXP(-r * n)) / (1 - EXP(-r))
# Note: This is the continuous analog of the geometric series sum
val_row = meta["data_end_row"] + 2

ws.cell(row=val_row, column=1, value="Validation: Closed-Form Total")
ws.cell(row=val_row, column=2).value = (
    f"={e0}*(1-EXP(-{r}*{total_epochs}))/(1-EXP(-{r}))"
)

ws.cell(row=val_row + 1, column=1, value="Validation: Sum of Periods")
ws.cell(row=val_row + 1, column=2).value = (
    f"=SUM(D{meta['data_start_row']}:D{meta['data_end_row']})"
)

ws.cell(row=val_row + 2, column=1, value="Validation: Difference")
ws.cell(row=val_row + 2, column=2).value = (
    f"=ABS(B{val_row}-B{val_row+1})"
)

# The difference should be < 1 GNK
# Also add warning formatting if difference exceeds threshold
```

### The app.xml Post-Processing Fix
```python
# Source: openpyxl issue #2229, verified locally with openpyxl 3.1.5
import zipfile
import re
import shutil

def fix_chart_rendering(xlsx_path):
    """Fix openpyxl 3.1.5 chart rendering in Microsoft Excel.

    The Application string 'Microsoft Excel Compatible / Openpyxl 3.1.5'
    in docProps/app.xml causes Excel to misrender chart axes and labels.
    This function replaces it with 'Microsoft Excel'.

    Tested: Original file produces broken charts in Excel.
            Fixed file produces correct charts in Excel.
            Both versions work correctly in Google Sheets.
    """
    tmp_path = xlsx_path + ".tmp"
    with zipfile.ZipFile(xlsx_path, "r") as zin:
        with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == "docProps/app.xml":
                    content = data.decode("utf-8")
                    content = re.sub(
                        r"<Application>.*?</Application>",
                        "<Application>Microsoft Excel</Application>",
                        content,
                    )
                    data = content.encode("utf-8")
                zout.writestr(item, data)
    shutil.move(tmp_path, xlsx_path)
```

### Integrating into generate.py
```python
# In generate.py, after building all tabs:
from generators.emission import build_emission_tab
from generators.chart_utils import fix_chart_rendering

def generate_all():
    from generators.workbook_base import create_workbook

    wb, param_refs = create_workbook()

    # Phase 2: Emission Schedule
    emission_meta = build_emission_tab(wb, param_refs)

    output_path = Path("output") / "gonka_master_model.xlsx"
    wb.save(str(output_path))
    fix_chart_rendering(str(output_path))  # Fix chart rendering for Excel

    print(f"Generated: {output_path}")
    print(f"  Assumptions tab: {len(param_refs)} parameters")
    print(f"  Emission Schedule tab: {emission_meta['data_end_row'] - emission_meta['data_start_row'] + 1} periods")
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| openpyxl 3.1.3 (pinned for chart safety) | openpyxl 3.1.5 + post-process fix | Issue identified June 2024, workaround confirmed | Can use latest openpyxl with all fixes while getting correct charts in Excel |
| Named ranges for cross-tab refs | Direct cell refs via param_refs dict | Project decision (Phase 1) | Simpler debugging, no phantom reference issues |
| Daily granularity (3650 rows) | Aggregated periods (32 rows) | Requirement REQ-U07 | Manageable file size, appropriate precision for leadership |
| Iterative `=prev*(1-r)` formulas | Closed-form `=E0*EXP(-r*t)` | Research pitfall #2 | Independent cells, no error propagation |

**Deprecated/outdated:**
- openpyxl 3.1.3 pinning: No longer necessary with the post-process workaround
- Named ranges: Explicitly avoided per project decisions (FEATURES.md anti-pattern)
- `decimal.Decimal` for emission calculation: Not needed; float precision verified sufficient (0.000029 GNK deviation over 10 years vs <1 GNK threshold)

## Specific Mathematical Findings

### Emission Decay Verification (Tested in Python)

| Metric | Value | Source |
|--------|-------|--------|
| Formula | `323,000 * EXP(-0.000475 * epoch)` | Whitepaper |
| Half-life | 1,459 epochs (4.0 years) | Computed: `ln(2) / 0.000475` |
| Year 1 daily emission | 271,586 GNK | `323,000 * EXP(-0.000475 * 365)` |
| Year 5 daily emission | 135,745 GNK | `323,000 * EXP(-0.000475 * 1825)` |
| Year 10 daily emission | 57,049 GNK | `323,000 * EXP(-0.000475 * 3650)` |
| 10-year cumulative | 560,030,816 GNK | Closed-form sum |
| % of mining allocation | 82.36% | 560M / 680M |
| Float vs Decimal deviation | 0.000029 GNK | Over entire 10-year horizon |
| Closed-form vs cell-by-cell | 0.000029 GNK | Same as above |

### Monthly Aggregation Factor
For any period starting at epoch `s` with `d` days:
```
Period total = E0 * EXP(-r * s) * (1 - EXP(-r * d)) / (1 - EXP(-r))
```
- Monthly factor (d=30): 29.794337 (multiply by `E0 * EXP(-r * start)`)
- Annual factor (d=365): 335.190653

### Circulating Supply Components

| Component | Amount | Schedule | Excel Formula Approach |
|-----------|--------|----------|----------------------|
| Mining emissions | 680M GNK (allocated) | Exponential decay over ~15+ years | Closed-form per-period formula |
| Community Pool | 120M GNK | Unlock schedule TBD; model as linear for now | `=CP_total / unlock_months * period_months` |
| Founder vesting | 200M GNK | Linear over 48 months | `=IF(period_end<=48_months, Founder_alloc/48*days_in_period, 0)` |

### Inflation Rate Formula
```
Annualized Inflation = (Period New Tokens / Period Length * 365) / Previous Cumulative Circulating
```
Excel: `=(G{row}/C{row}*365)/H{row-1}` where G=total new tokens, C=period days, H=cumulative.

For the first period, use total supply minus uncirculated as denominator (or a reference starting supply).

### Benchmark Comparison Labels
Add a text annotation column or use chart reference lines:
- ETH annual inflation: ~0.5% (post-Merge)
- BTC annual inflation: ~1.7% (current halving era)
- SOL annual inflation: ~5-6%

## Open Questions

Things that could not be fully resolved:

1. **Community Pool unlock schedule**
   - What we know: 120M GNK total, used for dev grants, floor defense, POL allocation
   - What is unclear: The exact unlock schedule (linear? milestone-based? discretionary?)
   - Recommendation: Model as configurable linear unlock over a default period (e.g., 120 months / 10 years). Add "CP Unlock Period" as a parameter on Assumptions tab. This can be refined in Phase 6 (Treasury) when the full treasury model is built. For Phase 2, a simple linear approximation is sufficient for the circulating supply schedule.

2. **Google Sheets dual-axis chart behavior**
   - What we know: openpyxl supports secondary Y-axis via `c2.y_axis.axId = 200`; Excel renders correctly
   - What is unclear: Whether Google Sheets will render the dual-axis as one chart or split it into two
   - Recommendation: Use separate charts instead of dual-axis for the Phase 2 scope. A dedicated inflation rate bar chart is clearer than overlaying it on the emission decay line chart. Test dual-axis in Phase 3 when it is needed for price x supply overlay.

3. **Target Excel version for testing**
   - What we know: The app.xml fix works for modern Excel (2019+, Microsoft 365)
   - What is unclear: Whether older Excel versions (2016) have additional chart rendering quirks
   - Recommendation: Test with Excel 365 / Excel 2021 as the primary target. If leadership uses an older version, they should report issues and we will address in Phase 9 (Polish).

4. **Epoch definition: is epoch 0 the launch day or the day before?**
   - What we know: "Epochs Per Day" = 1, epoch duration = 1 day
   - What is unclear: Whether epoch 0 emission is 323,000 GNK (at t=0) or 323,000 * EXP(-0.000475 * 1) (after first epoch)
   - Recommendation: Treat epoch 0 as the first day of mining. `EXP(-0.000475 * 0) = 1.0`, so day 1 emission = 323,000 GNK exactly. The first month sums epochs 0 through 29.

## Sources

### Primary (HIGH confidence)
- [openpyxl 3.1.5 PyPI page](https://pypi.org/project/openpyxl/) -- version 3.1.5, released 2024-06-28
- [openpyxl Line Charts docs](https://openpyxl.readthedocs.io/en/stable/charts/line.html) -- LineChart API, Reference, series formatting
- [openpyxl Area Charts docs](https://openpyxl.readthedocs.io/en/stable/charts/area.html) -- AreaChart, stacked grouping
- [openpyxl Bar Charts docs](https://openpyxl.readthedocs.io/en/stable/charts/bar.html) -- BarChart, type/grouping, overlap for stacked
- [openpyxl Secondary Axis docs](https://openpyxl.readthedocs.io/en/stable/charts/secondary.html) -- dual-axis via `+=` operator and axId
- [openpyxl Simple Formulae docs](https://openpyxl.readthedocs.io/en/stable/simple_formulae.html) -- formula writing, English names required, FORMULAE list
- [openpyxl 3.1.5 Changelog](https://openpyxl.pages.heptapod.net/openpyxl/changes.html) -- #2198 version number fix attempt
- [Excel EXP function](https://support.microsoft.com/en-us/office/exp-function-c578f034-2c45-4c37-bc8c-329660a63abe) -- official EXP documentation
- [Excel floating-point precision](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/excel/floating-point-arithmetic-inaccurate-result) -- IEEE 754 15-digit precision
- Local Python verification (run in project) -- tested float vs Decimal precision, closed-form vs cell-by-cell sums

### Secondary (MEDIUM confidence)
- [openpyxl issue #2229](https://foss.heptapod.net/openpyxl/openpyxl/-/issues/2229) -- app.xml Application string chart bug; confirmed unresolved in 3.1.5
- [openpyxl users: chart problems 3.1.4+](https://groups.google.com/g/openpyxl-users/c/khC6BTqaH3Y) -- community confirmation of chart rendering issues
- [Google Sheets EXP compatibility](https://support.google.com/docs/table/25273) -- EXP function listed as compatible
- [Incompatible functions between Sheets and Excel](https://help.openasapp.com/incompatible-functions) -- EXP not listed as incompatible

### Tertiary (LOW confidence)
- Google Sheets dual-axis chart rendering behavior with openpyxl files -- no authoritative source found; needs testing
- openpyxl horizontal reference line support -- no native API; constant-value series technique is community pattern

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- openpyxl 3.1.5 verified, chart API confirmed via official docs
- Architecture patterns: HIGH -- formula-writing pattern proven in Phase 1; emission formulas verified mathematically
- Chart rendering fix: HIGH -- bug confirmed via issue tracker; workaround tested locally
- Pitfalls: HIGH -- precision tested numerically; chart bug documented with reproducible fix
- Circulating supply: MEDIUM -- mining emission is fully specified; CP unlock schedule requires assumption
- Google Sheets charts: MEDIUM -- basic charts confirmed compatible; dual-axis needs testing

**Research date:** 2026-02-06
**Valid until:** 2026-03-06 (openpyxl is stable; 3.1.5 is 18+ months old with no newer release)

# Technology Stack: Excel Financial Model Generation

**Project:** Gonka Tokenomics Economic Modeling (v1.1)
**Researched:** 2026-02-05
**Overall Confidence:** HIGH

---

## Recommendation: openpyxl (not XlsxWriter)

**Use openpyxl 3.1.5 as the sole Excel generation library.** Do not add XlsxWriter, pandas, or xlwings. The rationale is below.

---

## Recommended Stack

### Core Library

| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| **openpyxl** | 3.1.5 | Excel .xlsx generation | Read/write/modify, full chart support, conditional formatting, named ranges, data validation -- everything needed for financial models in one library |
| Python | 3.10+ | Runtime | Match project's existing environment; openpyxl requires >=3.8 |

### Supporting (Standard Library Only)

| Module | Purpose | Notes |
|--------|---------|-------|
| `math` | Exponential decay calculations (e^(-0.000475*t)) | Built-in, no install needed |
| `datetime` | Date handling for timeline projections | Built-in |
| `decimal` | Precision for financial calculations | Built-in; use for intermediate calcs, write as float to cells |
| `pathlib` | Output path management | Built-in |
| `typing` | Type hints for maintainability | Built-in |

### Installation

```bash
pip install openpyxl==3.1.5
```

That is the entire dependency. One library. Zero transitive dependencies that matter (et-xmlfile is pulled in automatically).

---

## openpyxl vs XlsxWriter: Decision Rationale

This was a close call. Both libraries produce valid .xlsx files. Here is why openpyxl wins for this specific project.

### Comparison Matrix

| Capability | openpyxl 3.1.5 | XlsxWriter 3.2.9 | Winner for This Project |
|------------|----------------|-------------------|------------------------|
| **Write new .xlsx** | Yes | Yes | Tie |
| **Read existing .xlsx** | Yes | No (write-only) | openpyxl -- enables template-based workflow later |
| **Modify existing .xlsx** | Yes | No | openpyxl |
| **Charts** | 10+ types (line, bar, area, scatter, pie, doughnut, radar, stock, bubble, surface) | 9 types (area, bar, column, line, pie, doughnut, scatter, stock, radar) | Tie (both cover financial chart needs) |
| **Conditional formatting** | CellIsRule, ColorScaleRule, FormulaRule, IconSetRule, DataBarRule | CellIsRule, ColorScale, DataBar, Formula, IconSet | Tie |
| **Named ranges** | Global + worksheet-scoped DefinedName | define_name() method | Tie |
| **Data validation** | List, whole, decimal, date, time, textLength, custom formula | List, whole, decimal, date, time, textLength, custom | Tie |
| **Formulas** | Write formula strings (not calculated) | Write formula strings (stores 0 as placeholder result) | openpyxl -- does not inject misleading 0 values |
| **Number formats** | Full Excel format codes + built-in named styles (Currency, Percent) | Full Excel format codes | openpyxl -- named styles reduce boilerplate |
| **Cell protection** | Sheet protection + per-cell lock/unlock | Sheet protection + per-cell lock/unlock | Tie |
| **Freeze panes** | ws.freeze_panes = 'A2' | worksheet.freeze_panes(1, 0) | Tie |
| **Performance (write)** | Slower for large datasets (~50x file size in memory) | Faster, lower memory | XlsxWriter -- but irrelevant here (small datasets) |
| **Write-only mode** | Available (under 10MB memory for huge files) | Default mode | Tie for this use case |
| **Dependencies** | et-xmlfile only | Standard library only | XlsxWriter (marginal advantage) |
| **Active maintenance** | Latest release: 2024-06-28 (3.1.5) | Latest release: 2025-09-16 (3.2.9) | XlsxWriter (more recent, but openpyxl is stable) |
| **License** | MIT | BSD-2-Clause | Tie (both permissive) |
| **Python version** | >=3.8 | >=3.8 | Tie |

### Why openpyxl Wins

1. **Read+Write matters for iteration.** During development, being able to load a generated workbook, inspect it programmatically, and modify it is invaluable for debugging. XlsxWriter cannot open files at all -- every change requires regenerating from scratch.

2. **Formula result handling is cleaner.** XlsxWriter stores `0` as the cached formula result. When opened in Google Sheets (which sometimes does not recalculate on open), users may see zeros instead of computed values. openpyxl does not inject a misleading cached result.

3. **Named styles reduce financial formatting boilerplate.** openpyxl's `NamedStyle` lets you define `currency_style`, `pct_style`, `header_style` once and apply across thousands of cells. XlsxWriter uses `Format` objects which are similar but less idiomatic.

4. **PROJECT.md already specifies openpyxl.** The project decision was made; this research validates it was the correct choice.

5. **Performance is irrelevant.** The tokenomics models have at most a few thousand rows. openpyxl's higher memory usage (50x file size) means a 1MB workbook uses ~50MB RAM. This is negligible on any modern machine.

### When XlsxWriter Would Have Won

- Generating reports with 100K+ rows (performance matters)
- No need to ever read files back
- Need for the latest maintenance cadence (XlsxWriter is more actively updated)
- Strict zero-dependency requirement

None of these apply to this project.

---

## openpyxl Capabilities Deep Dive

### Charts (HIGH confidence -- official docs verified)

Supported chart types relevant to financial modeling:

| Chart Type | Use Case in This Project | Google Sheets Compatible |
|------------|--------------------------|--------------------------|
| **LineChart** | Token price trajectories over time, emission decay curves | Yes -- renders correctly |
| **BarChart** | Revenue breakdown comparisons, fee vs emission bars | Yes -- renders correctly |
| **AreaChart** | Cumulative treasury balance, stacked revenue streams | Yes -- renders correctly |
| **ScatterChart** | ROI vs GNK price correlation, crossover point analysis | Yes -- renders correctly |
| **PieChart** | Revenue allocation split (70/20/5/5), token distribution | Yes -- renders correctly |

Chart types to AVOID for Google Sheets compatibility:
- **3D charts** -- rendering varies between Excel and Sheets
- **Surface charts** -- not supported in Google Sheets
- **Stock charts** -- limited support; use line charts with markers instead

Chart configuration capabilities:
- Titles, axis labels, legend positioning
- Multiple series per chart
- Secondary Y-axis (useful for dual-scale: price + emissions)
- Custom colors, line styles, markers
- Chart size: default 15cm x 7.5cm, fully adjustable via `width` and `height`
- Combination charts (e.g., line + bar on same plot)

### Conditional Formatting (HIGH confidence -- official docs verified)

| Rule Type | Use Case | Example |
|-----------|----------|---------|
| **CellIsRule** | Highlight negative values red, positive green | `CellIsRule(operator='lessThan', formula=['0'], fill=redFill)` |
| **ColorScaleRule** | Heat map for ROI across scenarios | 2-color or 3-color gradient (red-yellow-green) |
| **DataBarRule** | Visual bar for emission amounts in cells | In-cell bar proportional to value |
| **FormulaRule** | Highlight crossover year (fees > emissions) | `FormulaRule(formula=['$B2>$C2'], fill=greenFill)` |
| **IconSetRule** | Traffic light indicators for health metrics | 3TrafficLights, 3Arrows, 5Arrows |

**Google Sheets note:** Basic conditional formatting (cell-is, formula-based, color scales) imports reliably. Icon sets and data bars may not render identically -- test during development.

### Named Ranges (HIGH confidence -- official docs verified)

```python
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.utils import quote_sheetname, absolute_coordinate

# Global named range (accessible from any sheet)
ref = f"{quote_sheetname('Assumptions')}!{absolute_coordinate('B2:B20')}"
defn = DefinedName("assumptions_range", attr_text=ref)
wb.defined_names["assumptions_range"] = defn

# Use in formulas across sheets
ws['A1'] = '=VLOOKUP("emission_rate", assumptions_range, 2, FALSE)'
```

Named ranges are critical for this project:
- **Assumption cells** should be named (`gnk_price_base`, `emission_decay_rate`, `revenue_split_host`)
- **Cross-sheet references** use names instead of fragile cell addresses
- **Google Sheets** preserves named ranges on import

### Data Validation (HIGH confidence -- official docs verified)

```python
from openpyxl.worksheet.datavalidation import DataValidation

# Dropdown for scenario selection
scenario_dv = DataValidation(
    type="list",
    formula1='"Conservative,Moderate,Aggressive"',
    allow_blank=False
)
scenario_dv.prompt = "Select a scenario"
scenario_dv.promptTitle = "Scenario"
ws.add_data_validation(scenario_dv)
scenario_dv.add('B2')

# Numeric range for adjustable parameters
pct_dv = DataValidation(
    type="decimal",
    operator="between",
    formula1=0,
    formula2=1
)
pct_dv.error = "Enter a value between 0% and 100%"
ws.add_data_validation(pct_dv)
pct_dv.add('B5:B10')
```

### Financial Number Formats (HIGH confidence -- official docs verified)

```python
from openpyxl.styles import NamedStyle, Font, Border, Side, Alignment, numbers

# Define reusable financial styles
currency_style = NamedStyle(name="currency")
currency_style.number_format = '"$"#,##0.00'
currency_style.font = Font(name='Calibri', size=11)

pct_style = NamedStyle(name="pct")
pct_style.number_format = '0.00%'

token_style = NamedStyle(name="tokens")
token_style.number_format = '#,##0'

large_currency = NamedStyle(name="large_currency")
large_currency.number_format = '"$"#,##0.0,,"M"'  # Displays as $22.0M

# Register once, use everywhere
wb.add_named_style(currency_style)
wb.add_named_style(pct_style)
wb.add_named_style(token_style)
wb.add_named_style(large_currency)

# Apply
cell.style = "currency"
cell.style = "pct"
```

Key format codes for tokenomics:
- `'"$"#,##0.00'` -- currency with 2 decimals ($1,234.56)
- `'0.00%'` -- percentage (5.25%)
- `'#,##0'` -- whole number with thousands separator (1,000,000)
- `'"$"#,##0.0,,"M"'` -- millions shorthand ($22.0M)
- `'0.000000'` -- high-precision decimal for decay rates
- `'#,##0.00" GNK"'` -- token amounts with unit suffix

### Sheet Protection (HIGH confidence -- official docs verified)

```python
# Protect sheet but allow users to change specific input cells
ws.protection.sheet = True
ws.protection.password = 'readonly'

# Unlock input cells (everything else stays locked by default)
from openpyxl.styles import Protection
unlocked = Protection(locked=False)
ws['B2'].protection = unlocked  # User can edit this assumption
```

This pattern is essential: protect formula cells and structural elements while letting leadership adjust assumption inputs.

### Freeze Panes (HIGH confidence)

```python
ws.freeze_panes = 'B3'  # Freeze row 1-2 headers and column A labels
```

---

## What NOT to Add (and Why)

| Library | Why People Add It | Why NOT to Add It |
|---------|-------------------|-------------------|
| **pandas** | DataFrame operations, pivot tables | Overkill -- models are formula-driven, not data-driven. Adding pandas pulls in numpy (~30MB). Write formulas directly. |
| **xlsxwriter** | "Better charts" / "faster" | Not better for this use case. Adds confusion having two Excel libraries. Cannot read files. |
| **xlwings** | Live Excel integration | Requires Excel to be installed. Does not work headlessly. Not cross-platform reliable. |
| **numpy** | Math operations | All calculations are either done in Excel formulas or simple Python math. `math.exp()` handles decay. |
| **matplotlib** | Generate chart images | Embeds static images, not interactive Excel charts. Users cannot modify. Defeats the purpose. |
| **jinja2** | Template engine | Templating adds complexity. Generate workbooks programmatically with code, not templates. |
| **defusedxml** | XML attack protection | Only needed if reading untrusted .xlsx files. We generate our own files. |

---

## Formula Patterns for Scenario Modeling

### Pattern 1: Assumption-Driven Formulas

All models should reference a central Assumptions sheet via named ranges:

```python
# On Assumptions sheet
ws_assumptions['A1'] = 'Parameter'
ws_assumptions['B1'] = 'Value'
ws_assumptions['A2'] = 'Base GNK Price'
ws_assumptions['B2'] = 0.50  # User-editable

# Define named range
defn = DefinedName("gnk_price_base", attr_text="Assumptions!$B$2")
wb.defined_names["gnk_price_base"] = defn

# On calculation sheet -- formula references the named range
ws_calc['B5'] = '=gnk_price_base * (1 + B4)'  # B4 = growth rate
```

### Pattern 2: Scenario Toggle with INDEX/MATCH

```python
# Scenarios in a table
# A: Conservative, B: Moderate, C: Aggressive
# Row with dropdown selects which column to use

ws['B1'] = '=INDEX(scenarios_table, MATCH("growth_rate", scenario_params, 0), MATCH(scenario_selector, scenario_names, 0))'
```

### Pattern 3: Time-Series with Relative References

```python
# Emission decay: each period references previous period
for row in range(3, 103):  # 100 periods
    ws[f'B{row}'] = f'=B{row-1} * EXP(-$B$1)'  # $B$1 = decay rate (named range)
    ws[f'C{row}'] = f'=B{row} * gnk_price_base'  # Dollar value
```

### Pattern 4: Crossover Detection

```python
# Find where fees exceed emissions
for row in range(3, 103):
    ws[f'E{row}'] = f'=IF(AND(C{row}>D{row}, C{row-1}<=D{row-1}), "CROSSOVER", "")'
```

### Formula Complexity Limits

- **Maximum formula length:** 8,192 characters (Excel limit, not openpyxl limit)
- **Maximum nesting depth:** 64 levels of IF() nesting (Excel limit)
- **Circular references:** Not supported by openpyxl (and should be avoided in these models)
- **openpyxl does NOT calculate formulas.** It writes formula strings. Excel/Sheets calculates on open.
- **Array formulas:** Supported but use sparingly for Google Sheets compatibility

---

## Google Sheets Compatibility Matrix

Critical requirement: all workbooks must open and function in Google Sheets.

| Feature | Excel | Google Sheets | Compatibility Notes |
|---------|-------|---------------|---------------------|
| Basic formulas (SUM, IF, VLOOKUP) | Full | Full | No issues |
| Named ranges | Full | Full | Preserved on import |
| Data validation dropdowns | Full | Full | Works reliably |
| Conditional formatting (cell-is) | Full | Full | Colors preserved |
| Conditional formatting (formula) | Full | Mostly | Test custom formulas; some may need adjustment |
| Color scales | Full | Full | Works |
| Icon sets | Full | Partial | May not render; use color-based formatting as fallback |
| Data bars | Full | Partial | May not render identically |
| Line/Bar/Area/Scatter charts | Full | Full | Chart axis labels may shift; verify after import |
| Pie charts | Full | Full | Works |
| 3D charts | Full | Partial | Avoid -- inconsistent rendering |
| Stock charts | Full | No | Use line charts with markers instead |
| Surface charts | Full | No | Do not use |
| Combination charts | Full | Partial | May split into separate charts; test carefully |
| Secondary Y-axis | Full | Partial | Google Sheets has limited dual-axis support; test |
| Freeze panes | Full | Full | Works |
| Sheet protection | Full | Partial | Password protection not enforced in Sheets |
| Number formats | Full | Mostly | Custom format codes may need verification |
| Cell comments | Full | Converted | Become Google Sheets "notes" |
| Merged cells | Full | Full | Works |

### Safe Strategy for Dual Compatibility

1. **Stick to 2D charts:** Line, Bar, Area, Scatter, Pie only
2. **Use basic conditional formatting:** CellIsRule and FormulaRule with color fills
3. **Avoid icon sets and data bars** as primary indicators (use as enhancement only)
4. **Test every workbook in both Excel and Google Sheets** before delivery
5. **Use standard formula functions** (SUM, IF, VLOOKUP, INDEX, MATCH, EXP, LN) -- avoid Excel-only functions like XLOOKUP (not in older Google Sheets versions)
6. **Document any Google Sheets quirks** in a README tab within each workbook

---

## Project File Structure Recommendation

```
gonka-tokenomics/
  models/
    __init__.py
    styles.py          # Shared NamedStyles (currency, pct, header, etc.)
    utils.py           # Helper functions (add_chart, format_range, etc.)
    assumptions.py     # Shared assumptions sheet builder
    price_model.py     # Token price scenario workbook
    emission_model.py  # Emission decay + fee transition workbook
    host_model.py      # Host profitability ROI workbook
    treasury_model.py  # Treasury & POL simulation workbook
    master_model.py    # Unified workbook linking all models
  output/              # Generated .xlsx files (gitignored)
  requirements.txt     # openpyxl==3.1.5
  generate.py          # CLI entry point: python generate.py [--model=all]
```

### Why This Structure

- **styles.py** -- single source of truth for formatting; change once, all models update
- **utils.py** -- DRY helpers for chart creation, range formatting, header rows
- **assumptions.py** -- shared assumption sheet generator; each model imports this
- **Separate model files** -- each can be developed/tested independently
- **master_model.py** -- composes the others into a unified multi-tab workbook
- **generate.py** -- simple entry point for non-technical users to regenerate

---

## Version Pinning and Reproducibility

```
# requirements.txt
openpyxl==3.1.5
```

Pin the exact version. openpyxl 3.1.5 is production-stable (released 2024-06-28). There is no 3.2.x or 4.x to worry about. The library has been stable at 3.1.x for years.

No virtual environment tooling is prescribed here -- use whatever the team already uses (venv, poetry, etc.). The dependency is trivial enough that it does not matter.

---

## Sources

### HIGH Confidence (Official Documentation)
- [openpyxl PyPI -- version 3.1.5](https://pypi.org/project/openpyxl/)
- [openpyxl official documentation](https://openpyxl.readthedocs.io/en/stable/)
- [openpyxl charts documentation](https://openpyxl.readthedocs.io/en/stable/charts/introduction.html)
- [openpyxl conditional formatting](https://openpyxl.readthedocs.io/en/stable/formatting.html)
- [openpyxl defined names / named ranges](https://openpyxl.readthedocs.io/en/stable/defined_names.html)
- [openpyxl data validation](https://openpyxl.readthedocs.io/en/stable/validation.html)
- [openpyxl styles documentation](https://openpyxl.readthedocs.io/en/stable/styles.html)
- [openpyxl protection](https://openpyxl.readthedocs.io/en/stable/protection.html)
- [openpyxl optimized modes](https://openpyxl.readthedocs.io/en/stable/optimized.html)
- [XlsxWriter PyPI -- version 3.2.9](https://pypi.org/project/XlsxWriter/)
- [XlsxWriter chart class documentation](https://xlsxwriter.readthedocs.io/chart.html)
- [XlsxWriter known issues](https://xlsxwriter.readthedocs.io/bugs.html)
- [XlsxWriter changelog](https://xlsxwriter.readthedocs.io/changes.html)

### MEDIUM Confidence (Verified with Multiple Sources)
- [Google Sheets conditional formatting import behavior](https://support.google.com/docs/thread/204202052/importing-conditional-formatting-to-sheets)
- [Google Sheets chart axis compatibility issues](https://support.google.com/docs/thread/210590195/chart-axis-changes-when-importing-excel-file-into-google-sheets)
- [openpyxl vs XlsxWriter comparison](https://stringfestanalytics.com/how-to-understand-the-difference-between-the-openpyxl-and-xlsxwriter-python-packages-for-excel/)

### LOW Confidence (Single Source / Community)
- Google Sheets icon set and data bar rendering behavior (based on community reports, not official documentation)
- XlsxWriter formula cached result behavior in Google Sheets (based on known issues page inference)

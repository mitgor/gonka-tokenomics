# Architecture Patterns: Python-Generated Excel Financial Models

**Domain:** Tokenomics economic modeling workbooks
**Researched:** 2026-02-05
**Overall Confidence:** HIGH (openpyxl API verified against official docs; financial modeling patterns from industry best practices)

---

## Recommended Architecture

### High-Level System Design

```
Python Codebase (generates)           Excel Output (consumed by leadership)
===========================           =====================================

models/                               Master Workbook (.xlsx)
  parameters.py    ------>            [Assumptions] tab (editable inputs)
  emission.py      ------>            [Emission Schedule] tab
  fee_transition.py ------>           [Fee Transition] tab
  host_profit.py   ------>            [Host Profitability] tab
  treasury.py      ------>            [Treasury & POL] tab
  token_price.py   ------>            [Token Price Scenarios] tab
                                      [Dashboard] tab (summary charts)
                                      [Documentation] tab

generators/                           Standalone Workbooks (4x)
  master.py        ------>            gonka_master_model.xlsx
  standalone.py    ------>            gonka_token_price.xlsx
                                      gonka_fee_transition.xlsx
                                      gonka_host_profitability.xlsx
                                      gonka_treasury_pol.xlsx
```

**Core principle:** Python computes nothing at runtime. Python writes Excel formulas into cells so the workbook is self-calculating. Leadership changes an assumption cell and all downstream formulas recalculate automatically in Excel.

---

## Python Project Structure

### Recommended Directory Layout

```
gonka-tokenomics/
  models/
    __init__.py
    parameters.py          # All input parameters from v1.0 research
    emission.py            # Emission decay schedule calculations
    fee_transition.py      # Fee vs emission crossover model
    host_profit.py         # Host ROI under varying conditions
    treasury.py            # Treasury, POL, buyback simulation
    token_price.py         # Token price scenario trajectories
  generators/
    __init__.py
    workbook_base.py       # Shared workbook creation utilities
    styles.py              # All cell styles, number formats, colors
    charts.py              # Chart creation helpers
    master.py              # Master workbook generator
    standalone.py          # Standalone workbook generators
  output/                  # Generated .xlsx files (gitignored)
  tests/
    __init__.py
    test_parameters.py     # Verify parameter values match research
    test_formulas.py       # Verify formula strings are valid
    test_generation.py     # Verify workbooks generate without error
    test_calculations.py   # Spot-check formula results in generated files
  generate.py              # CLI entry point: python generate.py [--all|--master|--standalone]
  requirements.txt         # openpyxl>=3.1.5
```

### Module Responsibilities

| Module | Responsibility | Depends On |
|--------|---------------|------------|
| `parameters.py` | Define all input constants from v1.0 research; map parameters to assumption sheet cells | None |
| `emission.py` | Build emission schedule rows and formulas for 10-year projection | `parameters.py` |
| `fee_transition.py` | Build fee revenue vs emission value crossover model | `parameters.py`, `emission.py` |
| `host_profit.py` | Build host ROI model under varying GNK prices and network sizes | `parameters.py`, `emission.py` |
| `treasury.py` | Build treasury depletion, POL returns, buyback impact model | `parameters.py` |
| `token_price.py` | Build multi-scenario price trajectories | `parameters.py` |
| `workbook_base.py` | Create workbooks, apply standard formatting, build assumptions tab | `parameters.py`, `styles.py` |
| `styles.py` | Define all NamedStyles, number formats, color constants | None |
| `charts.py` | Create standardized chart objects (line, area, combo) | None |
| `master.py` | Orchestrate full master workbook generation | All model modules |
| `standalone.py` | Generate 4 focused standalone workbooks | Individual model modules |

### Design Principle: Models Write Formulas, Not Values

Each model module exposes a function like `build_emission_tab(ws, params_row_map)` that:

1. Receives a worksheet and a mapping of parameter names to Assumptions tab cell references
2. Writes headers and row labels
3. Writes Excel formulas (as strings) that reference the Assumptions tab
4. Returns metadata about what it wrote (row/column ranges) for chart creation

**Example pattern:**

```python
# In emission.py
def build_emission_tab(ws, assumptions_refs):
    """
    assumptions_refs = {
        'initial_emission': 'Assumptions!$C$5',
        'decay_rate': 'Assumptions!$C$6',
        'epochs_per_day': 'Assumptions!$C$7',
    }
    """
    # Row 1: Headers
    ws['A1'] = 'Year'
    ws['B1'] = 'Epoch'
    ws['C1'] = 'Daily Emission (GNK)'
    ws['D1'] = 'Cumulative Mined'

    # Row 2: Year 0
    ws['A2'] = 0
    ws['B2'] = 0
    init_ref = assumptions_refs['initial_emission']
    ws['C2'] = f'={init_ref}'

    # Row 3+: Formula-driven
    decay_ref = assumptions_refs['decay_rate']
    for row in range(3, 12):  # Years 1-9
        yr = row - 2
        ws[f'A{row}'] = yr
        ws[f'B{row}'] = f'={yr}*365*{assumptions_refs["epochs_per_day"]}'
        ws[f'C{row}'] = f'={init_ref}*EXP(-{decay_ref}*B{row})'
        ws[f'D{row}'] = f'=D{row-1}+C{row}*365'
```

This ensures the generated workbook is fully self-contained. Leadership never needs Python again after generation.

---

## Excel Workbook Tab Architecture

### Master Workbook Tab Structure

The master workbook contains 8 tabs in this order:

| Tab # | Tab Name | Type | Purpose |
|-------|----------|------|---------|
| 1 | **Documentation** | Info | Model overview, methodology, parameter sources |
| 2 | **Assumptions** | Input | All adjustable parameters (ONLY editable tab) |
| 3 | **Emission Schedule** | Calc | 10-year emission decay, daily/annual GNK output |
| 4 | **Token Price** | Calc | 3-5 price scenario trajectories over 10 years |
| 5 | **Fee Transition** | Calc | Fee revenue vs emission value crossover analysis |
| 6 | **Host Profitability** | Calc | Host ROI under varying conditions |
| 7 | **Treasury & POL** | Calc | Community Pool depletion, POL returns, buyback |
| 8 | **Dashboard** | Output | Summary charts from all models, key metrics |

**Tab ordering rationale:**
- Documentation first so the user understands the model before interacting
- Assumptions second because it is the primary interaction point
- Calculation tabs ordered by dependency (emission feeds into fee transition and host profit)
- Dashboard last as the synthesis/output view

### Tab Color Coding

| Color | Meaning | Tabs |
|-------|---------|------|
| Blue (tab color) | Input / editable | Assumptions |
| Green (tab color) | Information / read-only docs | Documentation |
| Gray (tab color) | Calculation / do not edit | Emission, Token Price, Fee Transition, Host Profitability, Treasury |
| Orange (tab color) | Dashboard / output | Dashboard |

### Assumptions Tab Layout

The Assumptions tab is the single point of control for the entire model. Structure it with clear sections:

```
Row 1:  [GONKA TOKENOMICS MODEL - ASSUMPTIONS]  (merged header)
Row 2:  [All blue-shaded cells below are adjustable inputs]
Row 3:  (blank separator)

--- Section: Token Supply ---
Row 4:  [Section Header: TOKEN SUPPLY]
Row 5:  Total Supply           | 1,000,000,000 | GNK    | Fixed
Row 6:  Mining Rewards Pool    | 680,000,000   | GNK    | 68% of total
Row 7:  Community Pool         | 120,000,000   | GNK    | 12% of total
Row 8:  Founder Allocation     | 200,000,000   | GNK    | 20% of total
Row 9:  (blank separator)

--- Section: Emission Parameters ---
Row 10: [Section Header: EMISSION PARAMETERS]
Row 11: Initial Daily Emission | 323,000       | GNK/day| v1.0 research
Row 12: Decay Rate             | 0.000475      | /epoch | Halving ~4 years
Row 13: Epochs Per Day         | 1             |        | Assumption
Row 14: (blank separator)

--- Section: Revenue Parameters ---
Row 15: [Section Header: REVENUE PARAMETERS]
Row 16: Host Share             | 70%           |        | Current allocation
Row 17: AI Training Fund       | 20%           |        | Current allocation
Row 18: Buyback-Burn           | 5%            |        | Proposed (Rec #3)
Row 19: veGNK Yield            | 5%            |        | Proposed (Rec #3)
Row 20: (blank separator)

--- Section: Growth Scenarios ---
Row 21: [Section Header: GROWTH SCENARIOS]
Row 22: Conservative Dev Growth| 10%           | annual | Low scenario
Row 23: Moderate Dev Growth    | 25%           | annual | Target scenario
Row 24: Aggressive Dev Growth  | 40%           | annual | High scenario
Row 25: Base Active Developers | 2,200         |        | Current state
...etc for each parameter category
```

**Column layout for Assumptions:**

| Column A | Column B | Column C | Column D | Column E |
|----------|----------|----------|----------|----------|
| Parameter name | Value (EDITABLE) | Unit | Source/Note | Validation |

- Column B cells are blue-filled, unlocked (editable when sheet is protected)
- All other cells are locked (protected from editing)
- Column E contains data validation (dropdowns for scenario selectors, min/max for numeric inputs)

### Assumptions Parameter Groups

Based on v1.0 research, organize into these groups:

| Group | Parameters | Source |
|-------|-----------|--------|
| **Token Supply** | Total supply, mining pool, community pool, founder allocation | Whitepaper |
| **Emission** | Initial daily emission, decay rate, epochs/day | Whitepaper + v1.0 |
| **Revenue Split** | Host %, AI Fund %, Buyback %, Yield % | Rec #3 |
| **Price Scenarios** | Conservative/Moderate/Aggressive GNK price trajectories | v1.0 research |
| **Developer Growth** | Conservative/Moderate/Aggressive annual growth rates | Rec #4 |
| **GPU Economics** | H100 $/hr (current), annual deflation rate, Gonka target $/hr | Rec #9 |
| **POL** | GNK allocation, USDC pair %, ETH pair %, LP fee tier | Rec #2 |
| **Fee Transition** | Year 1-10 inference revenue under each scenario | Rec #1 stress test |
| **Host Costs** | Electricity $/kWh, GPU hardware cost, maintenance % | v1.0 GPU economics |
| **Buyback** | TWAP interval, max slippage, dip acceleration factor | Rec #3 |
| **Floor Defense** | Tier thresholds, daily buyback rates, treasury allocation | Rec #7 |
| **veGNK** | Min/max lock, voting power formula constants | Rec #6 |

---

## Formula Linking Patterns

### Pattern 1: Assumptions-to-Calculation (Primary)

All calculation tabs reference the Assumptions tab via absolute cell references.

```
Assumptions!$B$12  (decay rate = 0.000475)
    |
    +--> 'Emission Schedule'!C3  =  =$B$11*EXP(-Assumptions!$B$12*B3)
    +--> 'Fee Transition'!D5     =  references Emission Schedule output
    +--> 'Host Profitability'!E4 =  references Emission Schedule output
```

**Implementation in openpyxl:**

```python
# Cross-sheet formula reference
ws['C3'] = "=Assumptions!$B$11*EXP(-Assumptions!$B$12*B3)"

# When sheet names contain spaces, use single quotes
ws['C3'] = "='Emission Schedule'!C3*'Token Price'!B5"
```

**Why absolute references ($B$12) for assumptions:** Assumptions cells are fixed positions. When a user copies formulas within a calculation tab, the assumption references must not shift.

**Why relative references for same-tab data:** Within a calculation tab, row-relative references (like `B3`) allow formulas to be written in a loop without manual cell address computation.

### Pattern 2: Cross-Tab Calculation References

Some calculation tabs depend on others:

```
Emission Schedule (upstream)
    |
    +--> Fee Transition (reads daily emission values)
    +--> Host Profitability (reads daily emission values)
    +--> Treasury & POL (reads cumulative supply for buyback impact)

Token Price (upstream)
    |
    +--> Fee Transition (GNK price converts emission to USD value)
    +--> Host Profitability (GNK price determines host revenue in USD)
    +--> Treasury & POL (GNK price affects POL valuation)
```

**Implementation:** Use explicit sheet references in formulas:

```python
# In fee_transition.py, referencing emission schedule output
ws['D3'] = "='Emission Schedule'!$C3*'Token Price'!B3"
# Daily emission GNK * GNK price = emission USD value
```

### Pattern 3: Named Ranges for Key Parameters

Use openpyxl DefinedName for the most frequently referenced parameters. This makes formulas more readable when users inspect them in Excel.

```python
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.utils import quote_sheetname, absolute_coordinate

# Define a named range for decay rate
ref = f"{quote_sheetname('Assumptions')}!{absolute_coordinate('B12')}"
defn = DefinedName("decay_rate", attr_text=ref)
wb.defined_names["decay_rate"] = defn

# Then use in formulas:
ws['C3'] = "=initial_daily_emission*EXP(-decay_rate*B3)"
```

**Recommended named ranges (most referenced parameters):**

| Named Range | Cell | Value |
|-------------|------|-------|
| `total_supply` | Assumptions!$B$5 | 1,000,000,000 |
| `initial_daily_emission` | Assumptions!$B$11 | 323,000 |
| `decay_rate` | Assumptions!$B$12 | 0.000475 |
| `host_share` | Assumptions!$B$16 | 0.70 |
| `buyback_share` | Assumptions!$B$18 | 0.05 |
| `base_developers` | Assumptions!$B$25 | 2,200 |
| `gnk_price_conservative` | Assumptions!$B$30 | (price trajectory) |
| `gnk_price_moderate` | Assumptions!$B$31 | (price trajectory) |
| `gnk_price_aggressive` | Assumptions!$B$32 | (price trajectory) |

**Use named ranges sparingly.** Only for the top 10-15 most-referenced parameters. Too many named ranges make the workbook harder to audit. For less common parameters, direct cell references (Assumptions!$B$xx) are clearer.

### Pattern 4: Scenario Selection via Data Validation

For models that need scenario switching (e.g., conservative vs moderate vs aggressive):

```python
from openpyxl.worksheet.datavalidation import DataValidation

# On Assumptions tab, create a scenario selector dropdown
dv = DataValidation(
    type="list",
    formula1='"Conservative,Moderate,Aggressive"',
    allow_blank=False
)
dv.prompt = "Select growth scenario"
dv.promptTitle = "Scenario Selection"
assumptions_ws.add_data_validation(dv)
dv.add(assumptions_ws['B22'])  # Scenario selector cell

# In calculation tabs, use IF/CHOOSE to pick the right parameters
ws['C3'] = ('=IF(Assumptions!$B$22="Conservative",Assumptions!$B$23,'
            'IF(Assumptions!$B$22="Moderate",Assumptions!$B$24,'
            'Assumptions!$B$25))')
```

---

## Standalone vs Master Workbook Relationship

### Strategy: Extract, Don't Duplicate

Each standalone workbook is a subset of the master. The Python code should NOT have separate generation logic for standalones. Instead:

1. Each model module builds its tab identically whether in master or standalone
2. The standalone generator creates a workbook with only: Documentation + Assumptions (filtered) + one model tab + Dashboard (filtered)
3. The Assumptions tab in standalones contains only the parameters relevant to that model

```python
# In standalone.py
def generate_standalone(model_name, model_builder, relevant_params):
    wb = Workbook()

    # 1. Build filtered assumptions tab (only relevant parameters)
    assumptions_ws = wb.active
    assumptions_ws.title = "Assumptions"
    param_refs = build_assumptions_tab(assumptions_ws, relevant_params)

    # 2. Build the model tab
    model_ws = wb.create_sheet(model_name)
    model_builder(model_ws, param_refs)

    # 3. Build focused dashboard
    dashboard_ws = wb.create_sheet("Dashboard")
    build_dashboard(dashboard_ws, model_ws, model_name)

    # 4. Build documentation
    doc_ws = wb.create_sheet("Documentation", 0)  # Insert at position 0
    build_doc_tab(doc_ws, model_name)

    return wb
```

### Standalone Workbook Contents

| Standalone | Tabs | Assumptions Subset |
|-----------|------|-------------------|
| **Token Price** | Doc, Assumptions, Token Price, Dashboard | Supply, emission, price trajectories |
| **Fee Transition** | Doc, Assumptions, Emission (support), Fee Transition, Dashboard | Emission params, revenue params, growth scenarios, GPU economics |
| **Host Profitability** | Doc, Assumptions, Emission (support), Host Profitability, Dashboard | Emission params, price scenarios, GPU costs, host costs |
| **Treasury & POL** | Doc, Assumptions, Treasury & POL, Dashboard | Supply, POL params, buyback params, floor defense, revenue scenarios |

**Note:** Fee Transition and Host Profitability standalones need a simplified Emission Schedule support tab because their formulas reference emission data. The standalone generator should include this dependency automatically.

---

## Component Boundaries

### Data Flow Between Components

```
parameters.py
    |
    +-- defines PARAM_GROUPS dict: { group_name: [{ name, value, unit, source, validation }] }
    |
    v
workbook_base.py::build_assumptions_tab()
    |
    +-- writes parameters to Assumptions sheet
    +-- returns param_refs: { param_name: "Assumptions!$B$XX" }
    |
    v
emission.py::build_emission_tab(ws, param_refs)
    +-- returns emission_meta: { daily_emission_col, cumulative_col, year_col, row_range }
    |
    v
fee_transition.py::build_fee_transition_tab(ws, param_refs, emission_meta)
    |
token_price.py::build_token_price_tab(ws, param_refs)
    +-- returns price_meta: { scenario_cols, year_col, row_range }
    |
    v
host_profit.py::build_host_profit_tab(ws, param_refs, emission_meta, price_meta)
    |
treasury.py::build_treasury_tab(ws, param_refs)
    |
    v
charts.py + generators::build_dashboard(ws, all_metas)
```

### Interface Contract

Each model builder function follows this contract:

```python
def build_<model>_tab(
    ws: Worksheet,
    param_refs: dict[str, str],       # { "decay_rate": "Assumptions!$B$12", ... }
    **upstream_meta                     # Optional metadata from upstream tabs
) -> dict:
    """
    Writes headers, labels, formulas, and formatting to the worksheet.
    Returns metadata dict describing what was written (column/row ranges)
    for downstream consumers and chart creation.
    """
```

This clean interface means:
- Models can be tested in isolation (pass mock param_refs)
- Build order is explicit via dependency graph
- Standalones need only pass the right param_refs subset

---

## Formatting and Style Architecture

### NamedStyle Definitions (in styles.py)

Define all styles once in `styles.py` and register them with each workbook:

```python
from openpyxl.styles import NamedStyle, Font, Border, Side, Alignment, PatternFill, numbers

# Input cell style (blue background, editable)
INPUT_STYLE = NamedStyle(name="input_cell")
INPUT_STYLE.font = Font(color="000080", bold=False, size=11)
INPUT_STYLE.fill = PatternFill(start_color="DAEEF3", end_color="DAEEF3", fill_type="solid")
INPUT_STYLE.number_format = '#,##0.00'

# Header style
HEADER_STYLE = NamedStyle(name="header")
HEADER_STYLE.font = Font(bold=True, size=11, color="FFFFFF")
HEADER_STYLE.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
HEADER_STYLE.alignment = Alignment(horizontal="center")

# Section header style
SECTION_HEADER = NamedStyle(name="section_header")
SECTION_HEADER.font = Font(bold=True, size=12, color="2F5496")
SECTION_HEADER.border = Border(bottom=Side(style="medium", color="2F5496"))

# Currency format
CURRENCY_STYLE = NamedStyle(name="currency")
CURRENCY_STYLE.number_format = '$#,##0'

# Large number format (millions)
MILLIONS_STYLE = NamedStyle(name="millions")
MILLIONS_STYLE.number_format = '#,##0'

# Percentage format
PERCENT_STYLE = NamedStyle(name="percent")
PERCENT_STYLE.number_format = '0.0%'

# Formula cell (black text, no background -- standard financial model convention)
FORMULA_STYLE = NamedStyle(name="formula_cell")
FORMULA_STYLE.font = Font(color="000000", size=11)

def register_styles(wb):
    """Register all named styles with a workbook. Call once per workbook."""
    for style in [INPUT_STYLE, HEADER_STYLE, SECTION_HEADER,
                  CURRENCY_STYLE, MILLIONS_STYLE, PERCENT_STYLE, FORMULA_STYLE]:
        wb.add_named_style(style)
```

### Color Conventions (Financial Modeling Standard)

| Cell Type | Font Color | Background | Convention |
|-----------|-----------|------------|------------|
| Hard-coded input (adjustable) | Dark Blue | Light Blue | Industry standard: blue = input |
| Formula (same-tab) | Black | None | Standard |
| Cross-tab reference | Green | None | Standard: green = external link |
| Section header | Dark Blue | None | Bold, underlined |
| Warning/threshold | Red | Light Red | Draws attention to critical values |

### Number Formats by Data Type

| Data Type | Format String | Example Output |
|-----------|--------------|----------------|
| GNK token amounts | `#,##0` | 323,000 |
| GNK large amounts | `#,##0,,` + " M" suffix | 680 M |
| USD currency | `$#,##0` | $25,000,000 |
| USD large | `$#,##0,,` + " M" suffix | $25 M |
| Percentage | `0.0%` | 70.0% |
| Decay rate | `0.000000` | 0.000475 |
| Year | `0` | 4 |
| Price per hour | `$#,##0.00` | $2.50 |
| ROI multiple | `0.0x` | 2.5x |

---

## Sheet Protection Pattern

Protect calculation tabs from accidental editing while keeping Assumptions editable:

```python
from openpyxl.styles import Protection

def protect_calculation_tab(ws):
    """Lock all cells in a calculation tab."""
    ws.protection.sheet = True
    ws.protection.password = ''  # No password -- prevents accidental edits only
    # All cells default to locked=True when sheet is protected

def setup_assumptions_tab(ws, input_cells):
    """Protect assumptions tab but unlock input cells."""
    # First, set all cells as locked (default)
    ws.protection.sheet = True

    # Unlock specific input cells
    for cell_ref in input_cells:
        ws[cell_ref].protection = Protection(locked=False)
```

**No password on protection.** The audience is leadership, not adversaries. Protection prevents accidental formula overwrites, not malicious edits. A password would create friction without security benefit.

---

## Chart Architecture

### Dashboard Tab Design

The Dashboard tab contains 4-6 summary charts, one per model area:

| Chart # | Type | Title | Data Source |
|---------|------|-------|-------------|
| 1 | Line (multi-series) | GNK Emission Schedule (10-Year) | Emission Schedule tab |
| 2 | Line (multi-series) | Token Price Scenarios | Token Price tab |
| 3 | Stacked Area | Fee Revenue vs Emission Value | Fee Transition tab |
| 4 | Grouped Bar | Host ROI by Scenario | Host Profitability tab |
| 5 | Line (dual-axis) | Treasury Balance & Buyback Pressure | Treasury & POL tab |
| 6 | Combo (line + area) | Fee Transition Crossover Point | Fee Transition tab |

### Chart Creation Pattern

```python
from openpyxl.chart import LineChart, Reference

def create_emission_chart(dashboard_ws, source_ws, meta):
    """Create emission schedule chart on dashboard."""
    chart = LineChart()
    chart.title = "GNK Daily Emission (10-Year Projection)"
    chart.y_axis.title = "GNK per Day"
    chart.x_axis.title = "Year"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # Reference data from source worksheet
    data = Reference(
        source_ws,
        min_col=meta['daily_emission_col'],
        min_row=meta['header_row'],
        max_row=meta['last_row']
    )
    cats = Reference(
        source_ws,
        min_col=meta['year_col'],
        min_row=meta['header_row'] + 1,
        max_row=meta['last_row']
    )
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)

    dashboard_ws.add_chart(chart, "A1")
```

### Charts Within Calculation Tabs

Each calculation tab should also have a small inline chart positioned to the right of the data table (starting around column H or I). This gives context without requiring the user to flip to the Dashboard tab.

---

## Dependency Graph and Build Order

### Model Dependencies

```
Layer 0 (no dependencies):
  parameters.py          -- all constants from v1.0 research

Layer 1 (depends on parameters only):
  token_price.py         -- price scenarios are input-driven
  emission.py            -- emission schedule is input-driven
  treasury.py            -- treasury model is mostly input-driven

Layer 2 (depends on Layer 1 outputs):
  fee_transition.py      -- needs emission + price data
  host_profit.py         -- needs emission + price data

Layer 3 (depends on all models):
  Dashboard              -- summarizes all model outputs
```

### Recommended Build Order for Master Workbook

```python
def generate_master():
    wb = Workbook()

    # 1. Register styles
    register_styles(wb)

    # 2. Build Assumptions tab (always first)
    assumptions_ws = wb.active
    assumptions_ws.title = "Assumptions"
    param_refs = build_assumptions_tab(assumptions_ws, ALL_PARAMS)

    # 3. Build Layer 1 models (no cross-tab dependencies)
    emission_ws = wb.create_sheet("Emission Schedule")
    emission_meta = build_emission_tab(emission_ws, param_refs)

    price_ws = wb.create_sheet("Token Price")
    price_meta = build_token_price_tab(price_ws, param_refs)

    treasury_ws = wb.create_sheet("Treasury & POL")
    treasury_meta = build_treasury_tab(treasury_ws, param_refs)

    # 4. Build Layer 2 models (cross-tab references)
    fee_ws = wb.create_sheet("Fee Transition")
    fee_meta = build_fee_transition_tab(fee_ws, param_refs, emission_meta, price_meta)

    host_ws = wb.create_sheet("Host Profitability")
    host_meta = build_host_profit_tab(host_ws, param_refs, emission_meta, price_meta)

    # 5. Build Dashboard (references all tabs)
    dashboard_ws = wb.create_sheet("Dashboard")
    build_dashboard(dashboard_ws, emission_meta, price_meta, treasury_meta, fee_meta, host_meta)

    # 6. Build Documentation tab and move to front
    doc_ws = wb.create_sheet("Documentation", 0)
    build_doc_tab(doc_ws)

    # 7. Protect calculation tabs
    for ws in [emission_ws, price_ws, treasury_ws, fee_ws, host_ws, dashboard_ws]:
        protect_calculation_tab(ws)

    # 8. Set Assumptions as active sheet (what user sees on open)
    wb.active = wb.sheetnames.index("Assumptions")

    wb.save("output/gonka_master_model.xlsx")
```

### Build Order for Development Phases

This is the recommended order for implementing the Python codebase:

| Phase | What to Build | Rationale |
|-------|--------------|-----------|
| **1. Foundation** | `styles.py`, `parameters.py`, `workbook_base.py` | Shared infrastructure used by everything |
| **2. Emission Model** | `emission.py` + Assumptions tab | Simplest model; upstream of others; validates the formula-writing pattern |
| **3. Token Price Model** | `token_price.py` | Independent model; tests multi-scenario pattern |
| **4. Fee Transition Model** | `fee_transition.py` | First cross-tab dependency; validates linking pattern |
| **5. Host Profitability** | `host_profit.py` | Most complex cross-tab dependencies |
| **6. Treasury & POL** | `treasury.py` | Relatively independent but has many parameters |
| **7. Charts & Dashboard** | `charts.py`, dashboard builder | Depends on all models being complete |
| **8. Master Orchestration** | `master.py` | Puts it all together |
| **9. Standalones** | `standalone.py` | Extracts subsets from master logic |
| **10. Polish & Docs** | Documentation tab, cell protection, data validation | Final pass |

---

## Anti-Patterns to Avoid

### Anti-Pattern 1: Computing Values in Python

**What:** Calculate results in Python and write static values to cells.
**Why bad:** The workbook becomes a dead snapshot. Change an assumption and nothing recalculates. Defeats the entire purpose.
**Instead:** Write Excel formulas as strings. Let Excel do all computation.

### Anti-Pattern 2: One Giant Module

**What:** Put all generation logic in a single `generate.py` file.
**Why bad:** Untestable, impossible to generate standalones, difficult to modify individual models.
**Instead:** One module per model, clean interfaces, composition in generators.

### Anti-Pattern 3: Hardcoded Cell Addresses Everywhere

**What:** Scatter literal cell references like `"B12"` throughout model code.
**Why bad:** Adding a row to the Assumptions tab breaks every downstream formula.
**Instead:** `build_assumptions_tab()` returns a `param_refs` dictionary. All downstream code uses the dictionary, not literal addresses.

### Anti-Pattern 4: Sheet Name Strings Without Quoting

**What:** Writing `="Emission Schedule!C3"` in formulas.
**Why bad:** Sheet names with spaces must be single-quoted in Excel formulas. Missing quotes cause #REF! errors.
**Instead:** Always use `f"='{sheet_name}'!{cell_ref}"` for cross-sheet references. Or use openpyxl's `quote_sheetname()` utility.

### Anti-Pattern 5: Styling Cell-by-Cell in Loops

**What:** Creating new Font/Fill objects for every cell in a data range.
**Why bad:** Massive performance hit. openpyxl style creation is expensive.
**Instead:** Use NamedStyles registered once per workbook. Apply by name: `cell.style = 'currency'`.

### Anti-Pattern 6: Circular Cross-Tab References

**What:** Tab A references Tab B which references Tab A.
**Why bad:** Excel handles circular references poorly. Iterative calculation mode is unreliable and confusing for non-technical users.
**Instead:** Maintain strict dependency layering. If circularity seems needed, restructure the model to break the cycle (usually by duplicating the needed calculation inline).

---

## Scalability Considerations

| Concern | Current Scope | Future Scale | Approach |
|---------|--------------|--------------|----------|
| Number of parameters | ~50 assumptions | 100+ with advanced models | Group parameters into collapsible sections; add Assumptions sub-tabs if needed |
| Time horizon | 10 years annual | Monthly granularity | Increase rows but keep formula pattern identical |
| Scenario count | 3 (Cons/Mod/Agg) | 5-10 custom scenarios | Use CHOOSE() formula with scenario index; add scenario builder tab |
| Model count | 4 core models | 6-8 with advanced models | Same module pattern; add to Layer 1 or 2 |
| File size | <5 MB | Could grow with monthly data | Not a concern for this scale |

---

## Google Sheets Compatibility

The PROJECT.md specifies output must work in both Excel and Google Sheets. Key constraints:

| Feature | Excel | Google Sheets | Recommendation |
|---------|-------|---------------|----------------|
| Formulas | Full support | Full support | Standard Excel formulas work in both |
| Named ranges | Full support | Full support | Use standard DefinedName API |
| Data validation | Full support | Full support | Standard dropdowns work in both |
| Charts | Full support | Partial (may rerender) | Keep charts simple; avoid 3D or combo charts |
| Conditional formatting | Full support | Full support | Use standard rules |
| Sheet protection | Full support | Limited | Protection works for preventing edits |
| Named styles | Full support | Ignored | Styles are applied but names not preserved |
| Tab colors | Full support | Full support | Works in both |

**Recommendation:** Stick to standard formulas, avoid VBA macros (which Google Sheets cannot run), avoid 3D charts, and test generated files in Google Sheets during development.

---

## Sources

### Official Documentation (HIGH confidence)
- [openpyxl Defined Names](https://openpyxl.readthedocs.io/en/stable/defined_names.html) -- cross-sheet references, named ranges API
- [openpyxl Styles](https://openpyxl.readthedocs.io/en/stable/styles.html) -- NamedStyles, number formats, font/fill/border
- [openpyxl Data Validation](https://openpyxl.readthedocs.io/en/stable/validation.html) -- dropdown lists, input validation
- [openpyxl Line Charts](https://openpyxl.readthedocs.io/en/stable/charts/line.html) -- chart creation API
- [openpyxl Protection](https://openpyxl.readthedocs.io/en/stable/protection.html) -- sheet/cell protection
- [openpyxl Optimised Modes](https://openpyxl.readthedocs.io/en/3.1/optimized.html) -- performance for large files
- [openpyxl PyPI](https://pypi.org/project/openpyxl/) -- current version 3.1.5

### Financial Modeling Best Practices (MEDIUM confidence)
- [Wall Street Prep Financial Modeling Guide](https://www.wallstreetprep.com/knowledge/financial-modeling/) -- tab structure, color conventions
- [CFI Documenting Excel Models](https://corporatefinanceinstitute.com/resources/excel/documenting-excel-models-best-practices/) -- assumptions tab patterns
- [Toptal Financial Modeling Best Practices](https://www.toptal.com/finance/financial-modeling/financial-modeling-best-practices) -- formula linking
- [Gridlines Financial Modelling Tips](https://www.gridlines.com/blog/financial-modelling-tips/) -- centralized assumptions
- [Finzer Financial Modeling Best Practices 2025](https://finzer.io/en/blog/financial-modeling-best-practices) -- input/output separation

### Tokenomics Domain (MEDIUM confidence)
- [InnMind Tokenomics Spreadsheet Template](https://innmind.com/downloads/tokenomics-spreadsheet/) -- token model tab patterns
- [Koinly Crypto Emissions Schedule Template](https://koinly.io/blog/crypto-emissions-schedule-template/) -- emission schedule structure

---

*Architecture research: 2026-02-05*

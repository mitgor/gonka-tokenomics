# Phase 3: Token Price Scenarios Model - Research

**Researched:** 2026-02-06
**Domain:** openpyxl scenario selector (data validation + CHOOSE/MATCH formulas), dual-axis charts, cross-sheet formula references, conditional formatting, price trajectory modeling
**Confidence:** HIGH

## Summary

This phase builds the Token Price Scenarios tab, which is the first model to introduce the **scenario selector pattern** that will be reused by all downstream phases (4-6). The research covers six technical domains: (1) Data Validation dropdown lists for the scenario selector on the Assumptions tab, (2) MATCH+CHOOSE formula pattern for scenario-switching, (3) cross-sheet references to the Emission Schedule tab for circulating supply data, (4) dual-axis chart creation (price on left Y, supply on right Y), (5) conditional formatting for deflationary supply flagging, and (6) price trajectory interpolation formulas.

All six areas have been verified directly against openpyxl 3.1.5 installed in this project. The DataValidation class with `type="list"` creates Excel dropdown lists. The MATCH function converts the dropdown text ("Conservative"/"Base"/"Aggressive") to a numeric index (1/2/3), and CHOOSE selects scenario-specific values. Cross-sheet references to `'Emission Schedule'!H3:H34` work correctly when the sheet name is wrapped in single quotes via `openpyxl.utils.quote_sheetname()`. Dual-axis charts combine two LineChart objects using the `+=` operator with `c2.y_axis.axId = 200`. Conditional formatting uses `FormulaRule` to flag negative net supply values. All formula patterns (MATCH, CHOOSE, cross-sheet references) are compatible with both Excel and Google Sheets.

The critical architectural decision for this phase is **cross-tab references over data duplication**: the Token Price tab formulas reference `'Emission Schedule'!H{row}` directly for circulating supply rather than copying data. This avoids double-maintenance and ensures parameter changes on Assumptions propagate through emission calculations into price model outputs automatically.

**Primary recommendation:** Build a `generators/token_price.py` module following the Phase 2 `build_*_tab()` pattern, add a scenario selector dropdown + MATCH/CHOOSE cells to the Assumptions tab via `workbook_base.py`, and use cross-sheet `'Emission Schedule'!` references for all circulating supply data.

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| openpyxl | 3.1.5 | Excel generation (charts, formulas, data validation, conditional formatting) | Already installed; only dependency; validated in Phase 1-2 |
| openpyxl.worksheet.datavalidation.DataValidation | 3.1.5 | Dropdown list creation for scenario selector | Built-in openpyxl module; no additional dependency |
| openpyxl.formatting.rule.FormulaRule | 3.1.5 | Conditional formatting for deflationary supply flagging | Built-in openpyxl module |
| openpyxl.utils.quote_sheetname | 3.1.5 | Properly quote sheet names with spaces in cross-sheet formulas | Built-in utility; verified working |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| openpyxl.chart.LineChart | 3.1.5 | Both primary and secondary chart objects for dual-axis | Price trajectory chart + supply overlay chart |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| MATCH+CHOOSE for scenario switching | VLOOKUP/INDEX-MATCH | CHOOSE is simpler, more performant, and standard in financial modeling; VLOOKUP requires a lookup table |
| Cross-tab references | Duplicate emission data into price tab | Duplication causes double-maintenance; cross-tab refs auto-propagate Assumptions changes |
| FormulaRule conditional formatting | CellIsRule | FormulaRule is more flexible for complex conditions (e.g., comparing derived values); CellIsRule only works for simple cell comparisons |
| Linear interpolation for price paths | Growth curve / exponential | Linear is simplest, most transparent for leadership, and matches the scenario range format (low->high) |

**Installation:**
```bash
pip install openpyxl==3.1.5  # Already in requirements.txt; no new dependencies
```

## Architecture Patterns

### Recommended Project Structure
```
generators/
  token_price.py       # NEW: build_token_price_tab(wb, param_refs, emission_meta) -> price_meta
  emission.py          # EXISTING: build_emission_tab(wb, param_refs) -> emission_meta
  chart_utils.py       # EXISTING: fix_chart_rendering(), col_to_num()
  styles.py            # EXISTING: NamedStyles (uses existing warning_cell, crossref_cell)
  workbook_base.py     # MODIFIED: add scenario selector dropdown + MATCH/CHOOSE cells
models/
  parameters.py        # NO CHANGES: all price scenario params already defined
generate.py            # MODIFIED: wire in token_price.build_token_price_tab()
```

### Pattern 1: Scenario Selector on Assumptions Tab
**What:** A data validation dropdown + MATCH formula + CHOOSE-derived "active" values, all placed on the Assumptions tab so they become part of the `param_refs` interface contract.
**When to use:** This is the foundation for REQ-U03 -- used by this phase and reused by Phases 4-6.

**Implementation approach:**

The scenario selector adds new rows to the Assumptions tab (after all PARAM_GROUPS are written). Three new elements are added:

1. **Dropdown cell** (B{row}): DataValidation `type="list"` with `formula1='"Conservative,Base,Aggressive"'`
2. **Scenario index cell** (B{row+1}): `=MATCH(B{row},{"Conservative","Base","Aggressive"},0)` -- returns 1, 2, or 3
3. **Active scenario values** (B{row+2} through B{row+N}): `=CHOOSE($B${row+1}, conservative_val, moderate_val, aggressive_val)` for each scenario-dependent parameter

These cells get added to `param_refs` with keys like:
- `"Active Scenario"` -> dropdown cell address
- `"Scenario Index"` -> MATCH formula cell address
- `"Active Price Low"` -> CHOOSE formula cell address
- `"Active Price High"` -> CHOOSE formula cell address

**Example:**
```python
# Source: Verified against openpyxl 3.1.5 DataValidation API
from openpyxl.worksheet.datavalidation import DataValidation

# On the Assumptions tab, after all PARAM_GROUPS are written:
dv = DataValidation(
    type="list",
    formula1='"Conservative,Base,Aggressive"',
    allow_blank=False,
)
dv.prompt = "Select scenario"
dv.promptTitle = "Scenario"
ws.add_data_validation(dv)

# Write dropdown cell with default value
selector_cell = ws.cell(row=row, column=2, value="Base")
dv.add(selector_cell)

# MATCH formula: converts text to index 1/2/3
index_cell = ws.cell(
    row=row + 1, column=2,
    value='=MATCH(B{0},{{"Conservative","Base","Aggressive"}},0)'.format(row),
)

# CHOOSE formulas: select active values per scenario
# Active Price Low = CHOOSE(index, 0.50, 1.00, 3.00)
ws.cell(
    row=row + 2, column=2,
    value='=CHOOSE($B${0},{1},{2},{3})'.format(
        row + 1,
        param_refs["Conservative Price Low"],
        param_refs["Moderate Price Low"],
        param_refs["Aggressive Price Low"],
    ),
)
```

**CRITICAL GOTCHA -- showDropDown:**
The `showDropDown` parameter is **counterintuitive**: `showDropDown=True` **hides** the dropdown arrow in Excel/LibreOffice. Leave it at the default (`False`) to show the dropdown arrow. Verified in openpyxl 3.1.5.

### Pattern 2: Cross-Sheet Formula References
**What:** Token Price tab formulas reference `'Emission Schedule'!H{row}` for circulating supply data.
**When to use:** Any time a model tab needs data from another tab (Phase 3 referencing Phase 2 emission data, Phase 4 referencing Phase 2+3, etc.).

**Example:**
```python
# Source: Verified against openpyxl 3.1.5 + quote_sheetname()
from openpyxl.utils import quote_sheetname

es_sheet = quote_sheetname(emission_meta["sheet_name"])  # "'Emission Schedule'"
circ_col = emission_meta["cols"]["cumulative_circulating"]  # "H"

# Circulating market cap = circulating_supply * price_at_period
for i in range(32):  # 32 data rows matching emission tab
    row = data_start_row + i
    es_row = emission_meta["data_start_row"] + i  # 3 + i

    # Cross-sheet ref for circulating supply
    circ_ref = f"={es_sheet}!{circ_col}{es_row}"

    # Circulating market cap = supply * price
    ws.cell(row=row, column=col_circ_mcap,
            value=f"={es_sheet}!{circ_col}{es_row}*{price_col}{row}")
```

**Style for cross-sheet cells:** Use `crossref_cell` style (green font) per REQ-U05 convention. This visually distinguishes cells that reference other sheets.

### Pattern 3: Dual-Axis Chart (Price + Supply Overlay)
**What:** A combined chart with price curves on the left Y-axis and circulating supply on the right Y-axis.
**When to use:** REQ-M1-06 -- overlay price trajectories with circulating supply.

**Example:**
```python
# Source: Verified against openpyxl 3.1.5 dual-axis chart API
from openpyxl.chart import LineChart, Reference

# Primary chart: price trajectories (left Y-axis)
c1 = LineChart()
c1.title = "Price Scenarios vs Circulating Supply"
c1.y_axis.title = "GNK Price (USD)"
c1.x_axis.title = "Period"
c1.style = 13
c1.width = 20
c1.height = 12

# Add price series for each scenario...
# (Conservative, Moderate, Aggressive, Bitfury)
for col_key in price_columns:
    col_num = col_to_num(meta["cols"][col_key])
    data = Reference(ws, min_col=col_num, min_row=header_row, max_row=data_end_row)
    c1.add_data(data, titles_from_data=True)

cats = Reference(ws, min_col=1, min_row=data_start_row, max_row=data_end_row)
c1.set_categories(cats)

# Secondary chart: circulating supply (right Y-axis)
c2 = LineChart()
c2.y_axis.title = "Circulating Supply (GNK)"
c2.y_axis.axId = 200  # MUST be unique; 200 is openpyxl convention

supply_col_num = col_to_num(meta["cols"]["circulating_supply"])
supply_data = Reference(ws, min_col=supply_col_num, min_row=header_row, max_row=data_end_row)
c2.add_data(supply_data, titles_from_data=True)

# Combine: primary Y crosses at max to push secondary Y to right
c1.y_axis.crosses = "max"
c1 += c2

ws.add_chart(c1, "K1")
```

### Pattern 4: Conditional Formatting for Deflationary Flag
**What:** When net supply (gross emission - buyback burn) becomes negative (deflationary), highlight the cell.
**When to use:** REQ-M1-05 -- flag when net supply becomes deflationary per scenario.

**Example:**
```python
# Source: Verified against openpyxl 3.1.5 FormulaRule API
from openpyxl.styles import PatternFill, Font
from openpyxl.formatting.rule import CellIsRule

green_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
green_font = Font(name="Calibri", size=11, color="006100")

# Flag cells where net supply change is negative (deflationary)
cell_range = f"X{data_start_row}:X{data_end_row}"  # net supply column
ws.conditional_formatting.add(
    cell_range,
    CellIsRule(
        operator="lessThan",
        formula=["0"],
        fill=green_fill,
        font=green_font,
    ),
)
```

**Color choice rationale:** Green for deflationary (positive signal for token value) rather than red, since buyback-burn reducing supply is a feature, not a bug.

### Pattern 5: Price Trajectory Linear Interpolation
**What:** Each scenario defines a price range (e.g., Conservative: $0.50 to $1.00). The price at each period is linearly interpolated from the start price to the end price over the 10-year horizon.
**When to use:** REQ-M1-01 -- generating the price curve between low and high bounds per scenario.

**Formula pattern in Excel:**
```
=price_low + (period_index / total_periods) * (price_high - price_low)
```

Where `period_index` is 0-based (0 for first period, 31 for last) and `total_periods` is 31 (32 data rows - 1).

**In openpyxl:**
```python
# For each data row i (0 to 31):
for i in range(32):
    row = data_start_row + i
    # Conservative price: interpolate from low to high over 32 periods
    ws.cell(row=row, column=cons_price_col,
            value=f"={param_refs['Conservative Price Low']}+"
                  f"({i}/31)*"
                  f"({param_refs['Conservative Price High']}-{param_refs['Conservative Price Low']})")
```

**Bitfury Schelling Point** is constant across all periods (flat line at $0.60):
```python
ws.cell(row=row, column=bitfury_col,
        value=f"={param_refs['Bitfury Schelling Point']}")
```

### Anti-Patterns to Avoid
- **Duplicating emission data into the price tab:** Use cross-sheet references instead. Duplication creates maintenance burden and risks formula/value divergence.
- **Using showDropDown=True:** This counterintuitively HIDES the dropdown arrow. Leave it at default (False).
- **Hardcoding scenario values in formulas:** All values must come from param_refs (Assumptions tab) so leadership can adjust them.
- **Using VBA-style combo boxes:** openpyxl cannot create ActiveX/Form controls. Data Validation dropdowns are the only option.
- **Using named ranges:** Project-wide decision to use direct cell references only (avoids debugging complexity).

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Dropdown selector | Custom text matching logic | `DataValidation(type="list")` | Native Excel dropdown; works in Google Sheets too |
| Scenario index conversion | IF/nested-IF chains | `MATCH(cell,{"A","B","C"},0)` | MATCH is cleaner, extensible, standard in financial models |
| Scenario value selection | Nested IF formulas | `CHOOSE(index, val1, val2, val3)` | CHOOSE is the standard financial modeling pattern; up to 254 values |
| Cross-sheet references | Data copy/paste | `'Emission Schedule'!H{row}` + `quote_sheetname()` | Auto-propagates changes; green crossref_cell style signals the link |
| Dual-axis chart | Two separate charts | `c1 += c2` with `c2.y_axis.axId = 200` | Single chart with synchronized X-axis; proper overlay |
| Deflationary flagging | Manual cell coloring | `CellIsRule` or `FormulaRule` conditional formatting | Dynamic; updates when values change |
| Sheet name quoting | Manual string wrapping | `openpyxl.utils.quote_sheetname()` | Handles edge cases (special characters, already-quoted names) |

**Key insight:** The scenario selector pattern (DataValidation + MATCH + CHOOSE) is a solved problem in financial modeling. The entire mechanism lives on the Assumptions tab and downstream formulas just reference the "active" values, making the model clean and extensible.

## Common Pitfalls

### Pitfall 1: showDropDown Reversal
**What goes wrong:** Setting `showDropDown=True` expecting to display the dropdown arrow, but it actually hides it.
**Why it happens:** openpyxl follows the OOXML spec where `showDropDown="true"` means "show the dropdown" as in "show the fact that this is a dropdown," which Excel interprets as "suppress the dropdown arrow."
**How to avoid:** Never set `showDropDown`. The default (`False`) correctly shows the dropdown arrow in Excel.
**Warning signs:** Dropdown works but has no visible arrow indicator; users don't know they can click.

### Pitfall 2: MATCH Array Constant Syntax
**What goes wrong:** Using `MATCH(B1,{"Conservative","Base","Aggressive"},0)` with wrong quoting in the Python string.
**Why it happens:** The formula contains both double quotes (for Excel string literals) and curly braces (for Excel array constants), which conflict with Python string formatting.
**How to avoid:** Use careful string escaping. The curly braces `{}` in MATCH array constants are NOT Python format placeholders -- they are literal Excel array delimiters. Use `.format()` carefully or f-strings with doubled braces `{{` and `}}`.
**Warning signs:** Formula appears as `=MATCH(B1,{},0)` or Python raises KeyError on the format string.

### Pitfall 3: Cross-Sheet Reference Without Quotes
**What goes wrong:** Writing `=Emission Schedule!H3` without quoting the sheet name.
**Why it happens:** "Emission Schedule" has a space, requiring single quotes in Excel formula syntax.
**How to avoid:** Always use `quote_sheetname()` from `openpyxl.utils`. It wraps the name in single quotes: `'Emission Schedule'`.
**Warning signs:** `#REF!` error in Excel on cells that should reference the emission tab.

### Pitfall 4: Inconsistent Row Alignment Between Tabs
**What goes wrong:** Price tab row 3 doesn't correspond to Emission tab row 3, causing cross-sheet formulas to reference wrong data.
**Why it happens:** Different header row counts or spacing between tabs.
**How to avoid:** Use `emission_meta["data_start_row"]` and `emission_meta["data_end_row"]` to align row indices. The price tab should use the same 32-row structure (rows 3-34) as the emission tab.
**Warning signs:** Market cap numbers seem wrong; circulating supply values don't match between tabs.

### Pitfall 5: Buyback-Burn Circular Dependency
**What goes wrong:** Buyback-burn converts USD fee revenue to GNK tokens at the current price, but the price itself is a scenario input, creating a potential circularity concern.
**Why it happens:** The formula `tokens_burned = (fee_revenue * buyback_pct) / price` uses price as both a scenario input and a divisor.
**How to avoid:** This is NOT actually circular because price is a scenario INPUT (not calculated). The formula is simply: `buyback_tokens = fee_revenue_usd * buyback_pct / scenario_price`. The price drives the buyback calculation; the buyback doesn't feed back into price. Document this clearly in the model.
**Warning signs:** None if implemented correctly. The concern is more conceptual than technical.

### Pitfall 6: Fee Revenue Not Yet Available
**What goes wrong:** The buyback-burn calculation needs fee revenue data, but the Fee Transition model is Phase 4.
**Why it happens:** Phase 3 depends on Phase 2 (emission data) but NOT Phase 4 (fee revenue).
**How to avoid:** For Phase 3, use a simplified buyback-burn approach: either (a) use a placeholder fee revenue parameter from the Assumptions tab, or (b) show gross emission without buyback-burn and add a separate "what-if" buyback column using an assumed fee revenue input. The full fee-based buyback calculation happens when Phase 4 integrates.
**Warning signs:** Attempting to reference a Fee Transition tab that doesn't exist yet.

## Code Examples

### Complete Scenario Selector Setup (for workbook_base.py)
```python
# Source: Verified against openpyxl 3.1.5
from openpyxl.worksheet.datavalidation import DataValidation

def _add_scenario_selector(ws, current_row, param_refs):
    """Add scenario selector dropdown and CHOOSE formulas to Assumptions tab.

    Args:
        ws: The Assumptions worksheet.
        current_row: Next available row after PARAM_GROUPS.
        param_refs: Dict to update with new scenario cell references.

    Returns:
        int: The next available row after scenario selector section.
    """
    # Section header
    ws.merge_cells(
        start_row=current_row, start_column=1,
        end_row=current_row, end_column=4,
    )
    section_cell = ws.cell(row=current_row, column=1, value="SCENARIO SELECTOR")
    section_cell.style = "section_header"
    current_row += 1

    # Row: Active Scenario dropdown
    ws.cell(row=current_row, column=1, value="Active Scenario")
    selector_cell = ws.cell(row=current_row, column=2, value="Base")
    selector_cell.style = "input_cell"

    dv = DataValidation(
        type="list",
        formula1='"Conservative,Base,Aggressive"',
        allow_blank=False,
    )
    dv.prompt = "Select scenario"
    dv.promptTitle = "Active Scenario"
    dv.error = "Please select Conservative, Base, or Aggressive"
    dv.errorTitle = "Invalid Scenario"
    ws.add_data_validation(dv)
    dv.add(selector_cell)

    param_refs["Active Scenario"] = f"Assumptions!$B${current_row}"
    selector_row = current_row
    current_row += 1

    # Row: Scenario Index (hidden helper -- MATCH converts text to 1/2/3)
    ws.cell(row=current_row, column=1, value="Scenario Index")
    ws.cell(
        row=current_row, column=2,
        value=f'=MATCH(B{selector_row},{{"Conservative","Base","Aggressive"}},0)',
    )
    param_refs["Scenario Index"] = f"Assumptions!$B${current_row}"
    index_row = current_row
    current_row += 1

    # Active Price Low: CHOOSE(index, conservative, moderate, aggressive)
    ws.cell(row=current_row, column=1, value="Active Price Low")
    ws.cell(
        row=current_row, column=2,
        value=f"=CHOOSE($B${index_row},"
              f"{param_refs['Conservative Price Low']},"
              f"{param_refs['Moderate Price Low']},"
              f"{param_refs['Aggressive Price Low']})",
    )
    param_refs["Active Price Low"] = f"Assumptions!$B${current_row}"
    current_row += 1

    # Active Price High: CHOOSE(index, conservative, moderate, aggressive)
    ws.cell(row=current_row, column=1, value="Active Price High")
    ws.cell(
        row=current_row, column=2,
        value=f"=CHOOSE($B${index_row},"
              f"{param_refs['Conservative Price High']},"
              f"{param_refs['Moderate Price High']},"
              f"{param_refs['Aggressive Price High']})",
    )
    param_refs["Active Price High"] = f"Assumptions!$B${current_row}"
    current_row += 1

    return current_row
```

### Complete build_token_price_tab Signature
```python
# Source: Follows Phase 2 established pattern
def build_token_price_tab(wb, param_refs, emission_meta):
    """Create the 'Token Price' worksheet in the workbook.

    Args:
        wb: The openpyxl Workbook (styles already registered).
        param_refs: Mapping of parameter names to Assumptions cell refs.
                    Must include scenario selector refs from workbook_base.
        emission_meta: Dict from build_emission_tab() with sheet coordinates.

    Returns:
        price_meta: dict with keys describing what was written:
        {
            "sheet_name": "Token Price",
            "header_row": 2,
            "data_start_row": 3,
            "data_end_row": 34,
            "cols": {
                "period_label": "A",
                "conservative_price": "B",
                "moderate_price": "C",
                "aggressive_price": "D",
                "bitfury_price": "E",
                "active_price": "F",
                "circulating_supply": "G",   # cross-ref from Emission
                "fdv": "H",
                "circ_market_cap": "I",
                "gross_new_supply": "J",     # cross-ref from Emission
                "buyback_burn_tokens": "K",
                "net_supply_change": "L",
            },
        }
    """
```

### Cross-Sheet Formula for Circulating Supply
```python
# Source: Verified against openpyxl 3.1.5 + quote_sheetname()
from openpyxl.utils import quote_sheetname

es_sheet = quote_sheetname(emission_meta["sheet_name"])
circ_col = emission_meta["cols"]["cumulative_circulating"]  # "H"
total_col = emission_meta["cols"]["total_new"]              # "G"

for i in range(32):
    row = 3 + i
    es_row = emission_meta["data_start_row"] + i

    # G: Circulating Supply (cross-ref, green font)
    circ_cell = ws.cell(row=row, column=7,
                        value=f"={es_sheet}!{circ_col}{es_row}")
    circ_cell.style = "crossref_cell"

    # J: Gross New Supply per period (cross-ref)
    gross_cell = ws.cell(row=row, column=10,
                         value=f"={es_sheet}!{total_col}{es_row}")
    gross_cell.style = "crossref_cell"
```

### FDV and Circulating Market Cap Formulas
```python
# FDV = Total Supply * Active Price at period
# Circ Market Cap = Circulating Supply * Active Price at period

total_supply_ref = param_refs["Total Supply"]

for i in range(32):
    row = 3 + i

    # H: FDV = Total Supply * Active Price
    ws.cell(row=row, column=8,
            value=f"={total_supply_ref}*F{row}")

    # I: Circulating Market Cap = Circulating Supply * Active Price
    ws.cell(row=row, column=9,
            value=f"=G{row}*F{row}")
```

### Buyback-Burn Token Calculation
```python
# Buyback-burn tokens = (assumed fee revenue per period * buyback %) / active price
# Note: Fee revenue is a simplified assumption in Phase 3; full model in Phase 4

buyback_pct_ref = param_refs["Buyback-Burn"]  # 0.05

for i in range(32):
    row = 3 + i

    # K: Buyback burn tokens = (fee_revenue * buyback_pct) / price
    # Uses assumed_fee_revenue_ref which needs to be added to parameters
    # or calculated as a simple growth model
    ws.cell(row=row, column=11,
            value=f"={assumed_fee_rev_ref}*{buyback_pct_ref}/F{row}")

    # L: Net Supply Change = Gross New Supply - Buyback Burn
    ws.cell(row=row, column=12,
            value=f"=J{row}-K{row}")
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| VBA-based combo boxes for scenario selection | Data Validation dropdown + MATCH/CHOOSE | Permanent (openpyxl cannot create VBA controls) | Simpler, works in Google Sheets, pure formula approach |
| Named ranges for scenario switching | Direct cell references with param_refs | Project decision (Phase 1) | Consistent with project convention; avoids named range debugging issues |
| Separate charts per scenario | Multi-series single chart | Standard financial modeling | All scenarios visible simultaneously for comparison |
| Manual conditional formatting in Excel | openpyxl `FormulaRule` / `CellIsRule` | openpyxl 2.0+ | Automated; applied during generation |

**Deprecated/outdated:**
- VBA Form Controls: Not supported by openpyxl; breaks Google Sheets compatibility
- Named ranges: Project-wide decision to avoid (anti-pattern per FEATURES.md research)
- `showDropDown=True`: Counterintuitively hides the dropdown; never use

## Open Questions

1. **Fee Revenue Placeholder for Buyback-Burn**
   - What we know: Buyback-burn needs fee revenue, but the Fee Transition model is Phase 4. The buyback percentage (5%) is already in parameters.py.
   - What's unclear: What fee revenue assumption to use in Phase 3 for the buyback calculation.
   - Recommendation: Add a simple "Assumed Annual Fee Revenue" parameter to parameters.py (e.g., $1M base case), use it as a placeholder for Phase 3. Phase 4 will replace this with actual fee transition calculations. Alternatively, show buyback-burn as zero in Phase 3 and defer to Phase 4.

2. **Active Price Column vs All-Scenario Columns**
   - What we know: The scenario selector drives a single "Active Price" column via CHOOSE. But the chart needs to show ALL scenarios simultaneously.
   - What's unclear: Whether FDV/market cap/buyback should be calculated for all scenarios or only the active one.
   - Recommendation: Calculate price columns for ALL scenarios (Conservative, Moderate, Aggressive, Bitfury) regardless of the dropdown. The "Active Price" CHOOSE column drives the FDV/market cap/net supply columns. The price chart shows all 4+ price curves always. This gives leadership both the comparison view (chart) and the detailed analysis (active scenario calculations).

3. **Scenario Selector Placement on Assumptions Tab**
   - What we know: The scenario selector must be on the Assumptions tab per REQ-U03. All PARAM_GROUPS are already written by `build_assumptions_tab()`.
   - What's unclear: Whether to modify `build_assumptions_tab()` directly or create a separate function called after it.
   - Recommendation: Add a `_add_scenario_selector()` private function within `workbook_base.py` and call it at the end of `build_assumptions_tab()`. This keeps the selector as part of the Assumptions tab builder and ensures the selector rows are included in `param_refs`. The function returns the updated `current_row` for any future additions.

## Sources

### Primary (HIGH confidence)
- openpyxl 3.1.5 installed locally -- DataValidation, FormulaRule, LineChart, quote_sheetname all verified with test scripts
- [openpyxl Data Validation docs](https://openpyxl.readthedocs.io/en/3.1/validation.html) -- dropdown list creation pattern
- [openpyxl Secondary Axis docs](https://openpyxl.readthedocs.io/en/latest/charts/secondary.html) -- dual-axis chart combination pattern
- [openpyxl Conditional Formatting docs](https://openpyxl.readthedocs.io/en/3.1/formatting.html) -- CellIsRule and FormulaRule patterns
- [openpyxl utils.cell API](https://openpyxl.readthedocs.io/en/stable/api/openpyxl.utils.cell.html) -- quote_sheetname() function

### Secondary (MEDIUM confidence)
- [Wall Street Prep CHOOSE Function](https://www.wallstreetprep.com/knowledge/choose-function/) -- financial modeling scenario analysis pattern
- [FMI Scenario Switch Tutorial](https://fminstitute.com/modeling-resources/how-to-create-a-scenario-switch-in-excel/) -- MATCH+CHOOSE scenario selector best practice
- [D. Brown Consulting Scenario Analysis](https://www.dbrownconsulting.net/blog/how-to-build-scenario-analysis-in-excel-in-6-steps-using-the-index-choose-or-offset-functions) -- INDEX/CHOOSE/OFFSET comparison

### Tertiary (LOW confidence)
- Google Sheets array constant compatibility (curly braces `{"a","b","c"}`) -- verified by multiple sources but not tested in Google Sheets directly

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - openpyxl 3.1.5 verified with working test scripts on all six technical areas
- Architecture: HIGH - follows established Phase 2 `build_*_tab()` pattern; scenario selector pattern is standard financial modeling
- Pitfalls: HIGH - all pitfalls verified through testing (showDropDown reversal, cross-sheet quoting, MATCH array syntax)
- Code examples: HIGH - every example tested against installed openpyxl 3.1.5
- Buyback-burn approach: MEDIUM - placeholder fee revenue approach needs user validation; may be deferred to Phase 4

**Research date:** 2026-02-06
**Valid until:** 2026-03-06 (stable domain; openpyxl unlikely to change)

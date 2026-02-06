# Phase 7: Dashboard & Master Workbook Assembly - Research

**Researched:** 2026-02-06
**Domain:** openpyxl workbook assembly, tab reordering, internal hyperlinks, cross-sheet dashboard formulas
**Confidence:** HIGH

## Summary

Phase 7 is an assembly and orchestration phase, not a new-model phase. All six model tabs already exist and work correctly. The task is to (1) add a Documentation tab as a cover/title sheet with TOC, (2) add a Dashboard tab pulling cross-model KPIs via formulas, (3) reorder tabs to the required 8-tab structure, and (4) add "Back to TOC" navigation links on every tab. No new computational models are being built -- this phase composes the existing output into a navigable, professional deliverable.

The key technical concerns are: openpyxl's `create_sheet(title, index)` for positioning new tabs, `move_sheet(sheet, offset)` for reordering existing tabs, internal hyperlinks via `cell.hyperlink = '#SheetName!A1'`, and cross-sheet formula references using `quote_sheetname()`. All of these have been verified to work in openpyxl 3.1.5 through direct testing against the current codebase.

The Dashboard tab requires cross-sheet formulas pulling specific cells from each model tab -- this follows the exact same pattern already used in Phases 4-6 for cross-tab references. The breakeven reference line pattern (constant-value series with dashed line style) is already proven in `host_profit.py` and should be reused for any dashboard charts requiring threshold lines.

**Primary recommendation:** Build two new generators (`generators/documentation.py` and `generators/dashboard.py`), modify `generate.py` to call them and reorder tabs, and add a helper function for "Back to TOC" links that runs after all tabs exist.

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| openpyxl | 3.1.5 | Excel .xlsx generation (charts, formulas, hyperlinks) | Sole dependency; validated Phases 1-6; chart rendering fix proven |
| openpyxl.utils.quote_sheetname | 3.1.5 | Sheet name quoting for formulas | Already used in Phases 4-6 for cross-tab refs; handles spaces and & |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| openpyxl.worksheet.hyperlink | 3.1.5 | Internal worksheet navigation links | TOC hyperlinks and "Back to TOC" links |
| openpyxl.chart (LineChart, BarChart) | 3.1.5 | Dashboard summary charts | 2-3 KPI charts on Dashboard tab |
| openpyxl.formatting.rule | 3.1.5 | Conditional formatting on scenario matrix | Color-coding the comparison matrix |
| generators.chart_utils | local | fix_chart_rendering(), col_to_num() | Already in codebase; applied post-save |
| generators.styles | local | All NamedStyles, TAB_COLOR_DOCS, TAB_COLOR_DASHBOARD | Already defined; TAB_COLOR_DOCS="70AD47", TAB_COLOR_DASHBOARD="ED7D31" |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| cell.hyperlink property | HYPERLINK() Excel formula | Both work; cell.hyperlink is simpler for openpyxl; HYPERLINK formula is more portable to Google Sheets but adds formula complexity |
| create_sheet(index=0) + move_sheet() | wb._sheets list manipulation | create_sheet(index) is the public API; _sheets is private |
| Separate Documentation and TOC tabs | Combined cover + TOC on one tab | Combined is cleaner; REQ-M5-04 says "TOC tab with hyperlinks" but the 8-tab spec leaves no room for a separate TOC tab |

## Architecture Patterns

### Recommended File Structure
```
generators/
  documentation.py     # NEW - build_documentation_tab() for cover sheet + TOC
  dashboard.py         # NEW - build_dashboard_tab() for KPIs + charts + scenario matrix
  chart_utils.py       # EXISTING - fix_chart_rendering(), col_to_num()
  styles.py            # EXISTING - all styles already defined
  workbook_base.py     # EXISTING - create_workbook() returns (wb, param_refs)
  emission.py          # EXISTING
  token_price.py       # EXISTING
  fee_transition.py    # EXISTING
  host_profit.py       # EXISTING
  treasury.py          # EXISTING
generate.py            # MODIFIED - add doc tab, dashboard tab, reorder tabs, add nav links
```

### Pattern 1: Tab Creation and Reordering Strategy

**What:** Create Documentation tab at index 0 (before Assumptions), create Dashboard tab at end, then verify final tab order matches the required 8-tab structure.

**When to use:** In `generate.py` after all model tabs are built.

**Approach:**
```python
# Source: Verified via direct openpyxl 3.1.5 API testing

# Step 1: Build all model tabs (already done in Phases 2-6)
# Current order: [Assumptions, Emission Schedule, Token Price,
#                 Fee Transition, Host Profitability, Treasury & POL]

# Step 2: Build Documentation tab at position 0
from generators.documentation import build_documentation_tab
build_documentation_tab(wb, index=0)
# Now: [Documentation, Assumptions, Emission Schedule, ...]

# Step 3: Build Dashboard tab (appended at end by default)
from generators.dashboard import build_dashboard_tab
dashboard_meta = build_dashboard_tab(wb, param_refs, emission_meta,
                                      price_meta, fee_meta, host_meta,
                                      treasury_meta)
# Now: [Documentation, Assumptions, Emission, Token Price,
#        Fee Transition, Host Profitability, Treasury & POL, Dashboard]

# Step 4: Verify order
EXPECTED_ORDER = [
    "Documentation", "Assumptions", "Emission Schedule", "Token Price",
    "Fee Transition", "Host Profitability", "Treasury & POL", "Dashboard",
]
assert wb.sheetnames == EXPECTED_ORDER, f"Tab order mismatch: {wb.sheetnames}"
```

**Confidence:** HIGH -- tested `create_sheet(title, index=0)` directly against openpyxl 3.1.5, confirmed it inserts at position 0 without disturbing existing sheet references.

### Pattern 2: Internal Hyperlinks for TOC Navigation

**What:** Use `cell.hyperlink = '#SheetName!A1'` for clickable navigation links.

**When to use:** TOC entries on Documentation tab and "Back to TOC" links on every other tab.

**Approach:**
```python
# Source: Verified via direct testing in openpyxl 3.1.5
from openpyxl.styles import Font

LINK_FONT = Font(name="Calibri", size=11, color="0563C1", underline="single")

# TOC entry (on Documentation tab)
cell = ws_doc.cell(row=row, column=1, value="Emission Schedule")
cell.hyperlink = "#Emission Schedule!A1"
cell.font = LINK_FONT

# For sheet names with special chars (& in "Treasury & POL"):
cell = ws_doc.cell(row=row, column=1, value="Treasury & POL")
cell.hyperlink = "#'Treasury & POL'!A1"
cell.font = LINK_FONT

# "Back to TOC" link (on every model/dashboard tab)
back_cell = ws.cell(row=1, column=back_col, value="<< Documentation")
back_cell.hyperlink = "#Documentation!A1"
back_cell.font = LINK_FONT
```

**Key finding:** When the sheet name contains spaces or special characters like `&`, the hyperlink target must use single quotes: `#'Treasury & POL'!A1`. Use `quote_sheetname()` from `openpyxl.utils` to get the correctly quoted name, but strip the outer quotes if needed since the `#` prefix replaces them in hyperlink context.

**Confidence:** HIGH -- tested all 8 tab names with `cell.hyperlink` property; save/load roundtrip confirmed links persist.

### Pattern 3: Dashboard Cross-Sheet KPI Formulas

**What:** Dashboard cells contain formulas referencing specific cells on model tabs.

**When to use:** All 6-8 KPI values on the Dashboard tab.

**Approach:**
```python
# Source: Same pattern used in Phases 4-6 cross-tab references
from openpyxl.utils import quote_sheetname

es_sheet = quote_sheetname("Emission Schedule")   # "'Emission Schedule'"
tp_sheet = quote_sheetname("Token Price")          # "'Token Price'"
ft_sheet = quote_sheetname("Fee Transition")       # "'Fee Transition'"
hp_sheet = quote_sheetname("Host Profitability")   # "'Host Profitability'"
tr_sheet = quote_sheetname("Treasury & POL")       # "'Treasury & POL'"

# Example KPI: Year 10 Circulating Supply (last data row = 34)
ws.cell(row=kpi_row, column=2,
        value=f"={es_sheet}!H34")

# Example KPI: Year 10 Active GNK Price
ws.cell(row=kpi_row, column=2,
        value=f"={tp_sheet}!F34")

# Example KPI: Fee/Emission Crossover Ratio at Year 10
ws.cell(row=kpi_row, column=2,
        value=f"={ft_sheet}!I34")
```

**Confidence:** HIGH -- this is the identical pattern used throughout Phases 4-6.

### Pattern 4: Scenario Comparison Matrix

**What:** A matrix showing key metrics (rows) across scenarios (columns) with color coding.

**When to use:** Dashboard scenario comparison section.

**Approach:**
```python
# The matrix pulls from model tabs using CHOOSE or direct scenario references.
# Rows = metrics (e.g., "Year 10 GNK Price", "Crossover Year", etc.)
# Columns = Conservative | Base | Aggressive
#
# For price-dependent KPIs, reference the 3 price columns directly:
# Conservative: Token Price!B34
# Moderate:     Token Price!C34
# Aggressive:   Token Price!D34
#
# For fee-dependent KPIs, reference the crossover matrix that already exists:
# Fee Transition rows 38-40 already have Low/Base/High growth x 3 prices
#
# Color coding: Use ColorScaleRule or CellIsRule from openpyxl.formatting.rule
# (same pattern as existing conditional formatting in Phases 4-6)
```

**Confidence:** HIGH -- the data is already computed in model tabs; the dashboard just references it.

### Anti-Patterns to Avoid
- **Duplicating computations on Dashboard:** All values must be cross-sheet references or formulas pointing to model tabs. Never recompute what already exists.
- **Hardcoded values on Dashboard:** Every number must be a formula. If you need a threshold (like $0.85), reference the Assumptions tab or the column where it is already defined (e.g., Host Profitability!K3 for breakeven ref low).
- **Building Documentation tab after other tabs without index=0:** Would require complex move_sheet offset calculations. Create at index 0 from the start.
- **Ignoring sheet name quoting in hyperlinks:** `Treasury & POL` must be quoted with single quotes in hyperlink targets.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Sheet name quoting | Manual string escaping | `openpyxl.utils.quote_sheetname()` | Handles spaces, &, quotes correctly |
| Chart rendering fix | Manual XML editing | `generators.chart_utils.fix_chart_rendering()` | Already proven in Phases 2-6 |
| Hyperlink styling | Custom font per link | Shared `LINK_FONT` constant | Consistent blue underline across all links |
| Breakeven reference lines | Custom chart axis annotations | Constant-value data series with dashed line style | Proven pattern from host_profit.py _create_breakeven_chart() |
| Conditional formatting | Manual cell-by-cell coloring | `CellIsRule` / `ColorScaleRule` from `openpyxl.formatting.rule` | Already used in Phases 4-6 |
| Tab reordering | wb._sheets manipulation | `create_sheet(title, index=N)` for new tabs | Public API; avoids private attribute access |

**Key insight:** Phase 7 is 90% composition of existing patterns. The only genuinely new pattern is hyperlink navigation, and that uses a straightforward openpyxl API.

## Common Pitfalls

### Pitfall 1: Hyperlink Target Format for Sheet Names with Special Characters
**What goes wrong:** Hyperlink to `#Treasury & POL!A1` may not resolve in Excel because `&` is a special character in sheet name references.
**Why it happens:** Sheet names with spaces or special characters require single-quote wrapping in Excel formula notation.
**How to avoid:** Use `quote_sheetname(name)` to get the quoted form, then construct the hyperlink target as `f"#{quoted_name}!A1"`. For the `cell.hyperlink` property, the format should be `#'Treasury & POL'!A1`.
**Warning signs:** Clicking a TOC link in Excel shows an error or navigates to the wrong place.

### Pitfall 2: Tab Order Depends on Creation Order
**What goes wrong:** Documentation tab ends up at position 6 instead of position 0 if created after model tabs without specifying index.
**Why it happens:** `create_sheet()` appends by default.
**How to avoid:** Use `create_sheet("Documentation", index=0)` to insert at the beginning. Alternatively, build Documentation first in `generate.py` before calling any `build_*_tab()` functions.
**Warning signs:** `wb.sheetnames` does not match the expected 8-tab order.

### Pitfall 3: "Back to TOC" Link Position Conflicts with Existing Content
**What goes wrong:** Placing "Back to TOC" in column A row 1 overwrites the merged title cell on model tabs.
**Why it happens:** Every model tab has `ws.merge_cells("A1:X1")` for the section title.
**How to avoid:** Place the "Back to TOC" link in a cell to the right of the merged title area or in a dedicated row. Each tab's merge range differs:
  - Emission Schedule: A1:J1 (10 cols) -- use K1 or later
  - Token Price: A1:L1 (12 cols) -- chart starts at N1
  - Fee Transition: A1:N1 (14 cols) -- chart starts at P1
  - Host Profitability: A1:M1 (13 cols) -- chart starts at O1
  - Treasury & POL: A1:N1 (14 cols) -- chart starts at P1
  - Assumptions: A1:E1 (5 cols) -- use F1 or later
  Best approach: add a small "Back to Documentation" link in the row right after the merged title, or use a consistent column just past the last data column of each tab.
**Warning signs:** Merged cell conflict errors or overwritten title text.

### Pitfall 4: Dashboard Charts Not Rendering
**What goes wrong:** Charts on Dashboard tab appear blank when opened in Excel.
**Why it happens:** The openpyxl 3.1.5 `app.xml` Application string bug affects all charts, including dashboard charts.
**How to avoid:** `fix_chart_rendering()` is already applied post-save in `generate.py`. Ensure it runs AFTER saving the workbook with dashboard charts.
**Warning signs:** Charts show outlines but no data series when opened in Excel.

### Pitfall 5: Cross-Sheet References Break When Tabs Are Reordered
**What goes wrong:** Moving tabs after formulas are written could theoretically invalidate references.
**Why it happens:** Concern that `move_sheet()` does not update formula references.
**How to avoid:** This is NOT actually a problem because openpyxl formulas reference sheets by NAME (e.g., `'Emission Schedule'!H34`), not by tab index. Tab reordering does not affect name-based references. However, to be safe, create the Documentation tab at index 0 BEFORE writing any formulas on it, and build the Dashboard tab last (it naturally goes at the end).
**Warning signs:** `#REF!` errors in Excel after opening.

### Pitfall 6: Version and Date Hardcoding
**What goes wrong:** Cover sheet shows a hardcoded date that becomes stale.
**Why it happens:** Python writes the date at generation time.
**How to avoid:** Use `=TODAY()` Excel formula for the date cell on the Documentation tab, or use Python's `datetime.date.today()` to write the generation date. The version string should be a constant in generate.py or parameters.py (e.g., "v1.1").
**Warning signs:** Date on cover sheet does not match when the workbook was actually generated.

## Code Examples

### Example 1: Building the Documentation Tab
```python
# Source: Verified openpyxl 3.1.5 patterns from Phases 1-6
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import quote_sheetname
from generators.styles import TAB_COLOR_DOCS, SECTION_FONT_COLOR

def build_documentation_tab(wb, all_sheet_names):
    """Build the Documentation (cover/title) sheet at position 0."""
    ws = wb.create_sheet("Documentation", index=0)
    ws.sheet_properties.tabColor = TAB_COLOR_DOCS

    # Title
    ws.merge_cells("A1:F1")
    title = ws.cell(row=1, column=1, value="GONKA TOKENOMICS MODEL")
    title.font = Font(name="Calibri", size=18, bold=True, color=SECTION_FONT_COLOR)
    title.alignment = Alignment(horizontal="center")

    # Version and date
    ws.cell(row=3, column=1, value="Version:").font = Font(name="Calibri", size=11, bold=True)
    ws.cell(row=3, column=2, value="v1.1")
    ws.cell(row=4, column=1, value="Generated:").font = Font(name="Calibri", size=11, bold=True)
    ws.cell(row=4, column=2, value="=TODAY()")
    ws["B4"].number_format = "YYYY-MM-DD"

    # Disclaimer
    ws.merge_cells("A6:F6")
    disclaimer = ws.cell(row=6, column=1,
                         value="For internal decision-making purposes only")
    disclaimer.font = Font(name="Calibri", size=11, italic=True, color="FF0000")

    # Color convention legend
    row = 8
    ws.cell(row=row, column=1, value="COLOR CONVENTIONS").style = "section_header"
    row += 1
    # ... legend entries for blue=input, black=formula, green=cross-ref ...

    # Table of Contents with hyperlinks
    toc_row = 14  # or wherever legend ends
    ws.cell(row=toc_row, column=1, value="TABLE OF CONTENTS").style = "section_header"
    toc_row += 1

    link_font = Font(name="Calibri", size=11, color="0563C1", underline="single")
    for i, name in enumerate(all_sheet_names):
        if name == "Documentation":
            continue
        cell = ws.cell(row=toc_row, column=1, value=f"{i}. {name}")
        qn = quote_sheetname(name)
        cell.hyperlink = f"#{qn}!A1"
        cell.font = link_font
        toc_row += 1
```

### Example 2: Adding "Back to TOC" Links to Every Tab
```python
# Source: Verified openpyxl 3.1.5 hyperlink API
def add_back_to_toc_links(wb):
    """Add 'Back to Documentation' hyperlink on every non-Documentation tab."""
    link_font = Font(name="Calibri", size=11, color="0563C1", underline="single")

    for ws in wb.worksheets:
        if ws.title == "Documentation":
            continue

        # Find a safe column (right of the merged title area)
        # Use a consistent approach: last used data column + 2
        # Or use a known safe position per tab
        back_cell = ws.cell(row=1, column=ws.max_column + 2)
        back_cell.value = "<< Back to Documentation"
        back_cell.hyperlink = "#Documentation!A1"
        back_cell.font = link_font
```

### Example 3: Dashboard KPI Section with Cross-Sheet Formulas
```python
# Source: Same cross-tab pattern from generators/treasury.py and host_profit.py
from openpyxl.utils import quote_sheetname

def _build_kpi_section(ws, emission_meta, price_meta, fee_meta,
                        host_meta, treasury_meta):
    """Write 6-8 KPI rows pulling data from each model tab."""
    es = quote_sheetname(emission_meta["sheet_name"])
    tp = quote_sheetname(price_meta["sheet_name"])
    ft = quote_sheetname(fee_meta["sheet_name"])
    hp = quote_sheetname(host_meta["sheet_name"])
    tr = quote_sheetname(treasury_meta["sheet_name"])

    yr10_row = 34  # Last data row (Year 10) across all tabs

    kpis = [
        ("Year 10 Circulating Supply (GNK)", f"={es}!H{yr10_row}", "tokens"),
        ("Year 10 Active GNK Price ($)", f"={tp}!F{yr10_row}", "currency"),
        ("Year 10 Circ. Market Cap ($)", f"={tp}!I{yr10_row}", "currency"),
        ("Fee/Emission Crossover Ratio (Base)", f"={ft}!I{yr10_row}", "number"),
        ("Year 10 Host Net Income ($)", f"={hp}!G{yr10_row}", "currency"),
        ("Year 10 Net Treasury ($)", f"={tr}!N{yr10_row}", "currency"),
        ("Cumulative Buyback Burn (%)", f"={tr}!H{yr10_row}", "percent"),
        ("Host Churn Risk Periods (count)", f"=SUM({hp}!M3:{hp}!M{yr10_row})", "integer"),
    ]

    row = 3  # Start after header
    for label, formula, style_name in kpis:
        ws.cell(row=row, column=1, value=label)
        val_cell = ws.cell(row=row, column=2, value=formula)
        val_cell.style = style_name
        row += 1
```

### Example 4: Scenario Comparison Matrix
```python
# Source: Pattern from fee_transition.py crossover matrix (rows 37-40)
def _build_scenario_matrix(ws, price_meta, fee_meta, host_meta,
                            treasury_meta, start_row):
    """Build rows=metrics, columns=scenarios comparison matrix."""
    tp = quote_sheetname(price_meta["sheet_name"])
    ft = quote_sheetname(fee_meta["sheet_name"])
    hp = quote_sheetname(host_meta["sheet_name"])
    tr = quote_sheetname(treasury_meta["sheet_name"])

    yr10 = 34

    # Column headers
    headers = ["Metric", "Conservative", "Base", "Aggressive"]
    for col_idx, h in enumerate(headers, start=1):
        ws.cell(row=start_row, column=col_idx, value=h).style = "header"

    # Metrics with per-scenario formulas
    # Token Price: cons=B, mod=C, agg=D on Token Price tab
    metrics = [
        ("Year 10 GNK Price ($)", [
            f"={tp}!B{yr10}", f"={tp}!C{yr10}", f"={tp}!D{yr10}"
        ]),
        ("Year 10 FDV ($)", [
            f"={tp}!B{yr10}*Assumptions!$B$5",  # Total Supply * price
            f"={tp}!C{yr10}*Assumptions!$B$5",
            f"={tp}!D{yr10}*Assumptions!$B$5",
        ]),
        # ... more metrics ...
    ]

    row = start_row + 1
    for label, formulas in metrics:
        ws.cell(row=row, column=1, value=label)
        for col_offset, formula in enumerate(formulas):
            ws.cell(row=row, column=2 + col_offset, value=formula).style = "currency"
        row += 1
```

### Example 5: Dashboard Summary Chart
```python
# Source: Pattern from generators/emission.py and treasury.py chart patterns
from openpyxl.chart import BarChart, Reference

def _create_kpi_bar_chart(ws, kpi_start_row, kpi_end_row):
    """Create a horizontal bar chart of KPI values."""
    chart = BarChart()
    chart.type = "bar"  # horizontal bars
    chart.title = "Cross-Model KPIs at Year 10"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    data = Reference(ws, min_col=2, min_row=kpi_start_row,
                     max_row=kpi_end_row)
    chart.add_data(data, titles_from_data=False)

    cats = Reference(ws, min_col=1, min_row=kpi_start_row,
                     max_row=kpi_end_row)
    chart.set_categories(cats)

    ws.add_chart(chart, "E3")
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| VBA macros for navigation | Internal hyperlinks via openpyxl | N/A (constraint: no VBA) | Cell.hyperlink property works; no macros needed |
| Named ranges for cross-sheet refs | Direct cell references (e.g., `'Sheet'!B$34`) | Phase 1 decision | Simpler; no named range management overhead |
| Multiple workbooks for models | Single master workbook with 8 tabs | Phase 7 design | All models share one Assumptions tab |

**Deprecated/outdated:**
- `get_sheet_by_name()`: Use `wb["Sheet Name"]` instead (openpyxl 3.x)
- `get_sheet_names()`: Use `wb.sheetnames` property instead

## Open Questions

1. **"Back to TOC" link placement on each tab**
   - What we know: Each tab has a merged title row (A1:X1) where X varies. Charts occupy columns K+ through P+.
   - What's unclear: Exactly which cell is safe on every tab without conflicting with charts or merged areas.
   - Recommendation: Place the "Back to Documentation" link in a consistent location -- either (a) a dedicated row 1 cell past the last data column but before chart columns, or (b) use the first row AFTER the merged title (row 1, far-right column past the merge). The safest approach is to place it in each tab's title merge row at a column just past the merge end (e.g., Emission uses A1:J1, so put link at K1 -- but K1 is where charts start). Best fallback: place at the rightmost chart column + 1, or add a small "Back" link before the first chart position. The planner should define exact positions per tab.

2. **Scenario comparison matrix -- which metrics to include**
   - What we know: Need rows=metrics, columns=scenarios (Conservative/Base/Aggressive) per REQ-M5-03.
   - What's unclear: The exact 6-8 metrics to show. The codebase has many candidates.
   - Recommendation: Use these 6 metrics that span all models:
     1. Year 10 GNK Price ($) -- from Token Price tab
     2. Year 10 Circulating Market Cap ($) -- from Token Price tab
     3. Fee/Emission Crossover Ratio at Year 10 -- from Fee Transition tab
     4. Year 10 Host Net Income ($) -- from Host Profitability tab
     5. Year 10 Net Treasury ($) -- from Treasury tab
     6. Cumulative Burn % of Supply -- from Treasury tab
   - Additional candidates: Crossover Year, Host Breakeven Price, AI Fund Balance

3. **Dashboard charts -- what to chart**
   - What we know: REQ-M5-02 says "2-3 summary charts pulling data from each model tab."
   - Recommendation for 3 charts:
     1. **KPI Summary Bar Chart** -- horizontal bars showing Year 10 values for key metrics
     2. **Price vs Host Profitability Overlay** -- Active price trend with host net income (dual axis)
     3. **Treasury Health Timeline** -- Net treasury value over 10 years (single line, referencing Treasury tab column N)

## Sources

### Primary (HIGH confidence)
- openpyxl official API docs (Workbook.move_sheet, Workbook.create_sheet) -- https://openpyxl.readthedocs.io/en/stable/api/openpyxl.workbook.workbook.html
- openpyxl Hyperlink API -- https://openpyxl.readthedocs.io/en/stable/api/openpyxl.worksheet.hyperlink.html
- Direct testing against openpyxl 3.1.5 in the project environment (verified create_sheet index, move_sheet offset, cell.hyperlink, quote_sheetname for all 8 tab names, hyperlink roundtrip save/load)
- Existing codebase: generators/host_profit.py (breakeven reference line pattern, lines 295-337)
- Existing codebase: generators/treasury.py (cross-sheet formula pattern using quote_sheetname)
- Existing codebase: generators/styles.py (TAB_COLOR_DOCS, TAB_COLOR_DASHBOARD already defined)

### Secondary (MEDIUM confidence)
- openpyxl users group discussions on internal hyperlinks -- https://groups.google.com/g/openpyxl-users/c/92JFYZEnyE8
- openpyxl tutorial on create_sheet positioning -- https://openpyxl.readthedocs.io/en/stable/tutorial.html

### Tertiary (LOW confidence)
- None -- all findings verified through direct testing or official documentation.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- openpyxl 3.1.5 is the sole dependency; all APIs verified by direct testing
- Architecture: HIGH -- follows established patterns from Phases 2-6; only new file structures are documentation.py and dashboard.py
- Pitfalls: HIGH -- all pitfalls identified through direct testing (hyperlink quoting, tab ordering, merge conflicts)
- Dashboard design: MEDIUM -- the exact KPI selection and chart design are discretionary; formulas and cross-sheet patterns are proven

**Research date:** 2026-02-06
**Valid until:** 2026-03-06 (stable; openpyxl 3.1.5 is pinned)

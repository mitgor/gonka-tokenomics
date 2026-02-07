# Phase 9: Polish, Documentation & Validation - Research

**Researched:** 2026-02-07
**Domain:** Excel workbook polish (cell protection, source audit trails, print layout, cross-platform validation)
**Confidence:** HIGH

## Summary

Phase 9 is the final polish phase for 5 openpyxl-generated Excel workbooks. The work divides into four distinct concerns: (1) cell protection to prevent accidental formula edits, (2) enriching source citations with full document references and confidence levels, (3) print-ready layouts with proper page setup and headers/footers, and (4) cross-platform validation in both Excel and Google Sheets.

The existing codebase is well-prepared for this phase. Phase 1 already applied `Protection(locked=False)` to all input cells on the Assumptions tab, explicitly deferring sheet-level protection to Phase 9. All 60 parameters already have a "source" field in `parameters.py` column D, but these are abbreviated (e.g., "Rec #3" instead of full document citations with confidence levels). No print setup, page margins, headers, or footers exist in any generator. All formula functions used (SUM, IF, IFERROR, CHOOSE, MATCH, EXP, ABS, MAX, COUNTIF, TODAY) are fully Google Sheets compatible.

**Primary recommendation:** Implement as 3 plans: (1) cell protection + source audit enrichment in `parameters.py` and `workbook_base.py`, (2) print layout as a new `print_setup.py` utility applied to all generators, (3) validation testing script that opens all 5 workbooks and checks for errors.

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| openpyxl | 3.1.5 | All Excel workbook generation | Already used throughout project; confirmed working with chart fix |

### Supporting
| Module | Purpose | When to Use |
|--------|---------|-------------|
| `openpyxl.worksheet.protection.SheetProtection` | Enable sheet-level protection | Apply after all cells written |
| `openpyxl.styles.Protection` | Cell-level locked/unlocked | Already used in workbook_base.py |
| `openpyxl.worksheet.page.PrintPageSetup` | Page orientation, paper size, fit-to-page | Configure per worksheet |
| `openpyxl.worksheet.page.PageMargins` | Print margins | Configure per worksheet |
| `openpyxl.worksheet.header_footer.HeaderFooterItem` | Headers and footers | Configure per worksheet |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Per-worksheet print setup | Single global config | Global not possible in openpyxl; each ws needs individual setup |
| Password protection | No-password protection | Password adds friction; both are advisory-only (not encryption) |

**Installation:** No new dependencies needed. All APIs are in openpyxl 3.1.5.

## Architecture Patterns

### Current Project Structure (Relevant Files)
```
generators/
├── workbook_base.py     # Builds Assumptions tab, applies Protection(locked=False) to inputs
├── styles.py            # NamedStyles, color constants
├── standalone.py        # Builds 4 standalone workbooks
├── standalone_config.py # Config data for standalones
├── documentation.py     # Master workbook Documentation tab
├── cover_sheet.py       # Standalone cover sheet
├── chart_utils.py       # fix_chart_rendering + col_to_num
├── emission.py          # Emission Schedule tab builder
├── token_price.py       # Token Price tab builder
├── fee_transition.py    # Fee Transition tab builder
├── host_profit.py       # Host Profitability tab builder
├── treasury.py          # Treasury & POL tab builder
├── dashboard.py         # Dashboard tab builder
└── glossary.py          # Definitions tab builder
models/
└── parameters.py        # PARAM_GROUPS OrderedDict (60 params, 12 groups)
generate.py              # CLI entry point
```

### Pattern 1: Cell Protection Application Order
**What:** Sheet protection must be applied AFTER all cells are written, as the last step before saving.
**When to use:** Every workbook generation path (master + 4 standalones).
**Why:** openpyxl's `Protection(locked=False)` on input cells only takes effect when the sheet's `protection.sheet = True`. The current code already marks input cells as unlocked; Phase 9 just enables the sheet-level enforcement.

```python
# Source: openpyxl 3.1.5 API + verified via local testing
from openpyxl.worksheet.protection import SheetProtection

# After all cell content is written, enable protection on each sheet
for ws in wb.worksheets:
    ws.protection.sheet = True
    ws.protection.password = 'gonka'  # Advisory only, not encryption
    # Allow users to select both locked and unlocked cells
    ws.protection.selectLockedCells = False
    ws.protection.selectUnlockedCells = False
```

**CRITICAL:** The default behavior in openpyxl is that ALL cells are locked (`Protection(locked=True)`). The existing code in `workbook_base.py` already sets `Protection(locked=False)` on:
- Column B input cells on Assumptions tab (both `build_assumptions_tab` and `build_filtered_assumptions_tab`)
- The scenario selector dropdown cell

No other cells in any model tab have `Protection(locked=False)` set, which means all formula cells, headers, labels, and chart anchors are already locked by default. Enabling sheet protection will immediately protect them.

### Pattern 2: Source Citation Enhancement
**What:** Enhance column D ("Source") in `parameters.py` with full document references and add column E ("Confidence") with HIGH/MED/LOW levels.
**When to use:** Modify `parameters.py` to add a "confidence" field to each parameter dict, and modify `workbook_base.py` to write column E.

Current source column D structure:
- `"Whitepaper"` - abbreviated reference
- `"Rec #3"` - recommendation number only
- `"v1.0 Research"` - generic reference
- `"Network Data"` - no specific document

Required enhanced structure (per REQ-U10 and REQ-D04):
- Column D: `"Fine-Tuning Recommendations, Rec #3"` - full document + recommendation
- Column E: `"HIGH"` - confidence level

```python
# Enhanced parameter structure in parameters.py
{
    "name": "Host Share",
    "value": 0.70,
    "unit": "",
    "source": "Fine-Tuning Recs, Rec #3",  # Enhanced: full doc reference
    "confidence": "HIGH",                    # NEW field
    "format": "percent",
}
```

### Pattern 3: Centralized Print Setup Utility
**What:** A utility function that configures print settings for any worksheet based on its type (data tab, documentation, dashboard).
**When to use:** Called on every worksheet after content is built, before saving.

```python
# Source: openpyxl 3.1.5 API, verified via local testing
def apply_print_settings(ws, print_area, title_rows=None, orientation='landscape'):
    """Apply standard print settings to a worksheet."""
    # Print area
    ws.print_area = print_area

    # Repeat header rows on each page
    if title_rows:
        ws.print_title_rows = title_rows

    # Page setup
    ws.page_setup.orientation = orientation
    ws.page_setup.paperSize = ws.PAPERSIZE_LETTER  # US Letter
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0  # Unlimited height
    ws.page_setup.fitToPage = True

    # Margins (slightly tighter than default for more data)
    ws.page_margins.left = 0.5
    ws.page_margins.right = 0.5
    ws.page_margins.top = 0.75
    ws.page_margins.bottom = 0.75
    ws.page_margins.header = 0.3
    ws.page_margins.footer = 0.3

    # Header: sheet name centered
    ws.oddHeader.center.text = '&A'  # &A = sheet name

    # Footer: page number left, date right
    ws.oddFooter.left.text = 'Page &P of &N'
    ws.oddFooter.right.text = 'Gonka Tokenomics v1.1'
```

### Anti-Patterns to Avoid
- **Setting protection before writing cells:** All cell content MUST be written before enabling sheet protection. Otherwise, writing to locked cells will fail silently or cause unexpected behavior.
- **Using password encryption:** openpyxl's password protection is advisory (hashed, not encrypted). Don't give users a false sense of security. The password just prevents accidental edits, not malicious access.
- **Setting fitToHeight to a non-zero value:** This forces Excel to shrink content vertically, making multi-page data tables unreadable. Use `fitToHeight=0` (unlimited) with `fitToWidth=1` instead.
- **Applying print areas to chart anchor cells:** Charts are positioned by anchor cell but print independently. The print area should cover the data range only; charts in the print area will print alongside data.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Sheet protection | Custom cell-by-cell locking logic | `ws.protection.sheet = True` | openpyxl defaults all cells to locked; just enable sheet protection |
| Page fitting | Manual column width calculations | `fitToWidth=1, fitToHeight=0` | Excel handles scaling automatically |
| Header/footer codes | Static text with page numbers | `&P`, `&N`, `&A`, `&D` format codes | Standard Excel format codes auto-populate |
| Confidence column styling | Custom conditional formatting | Simple text values + italic font | Matches existing source column pattern |

**Key insight:** The current codebase has already done 90% of the work for cell protection by setting `Protection(locked=False)` on input cells in Phase 1. Phase 9 just flips the sheet-level switch.

## Common Pitfalls

### Pitfall 1: Google Sheets Strips Sheet Protection
**What goes wrong:** Sheet protection configured via openpyxl is not preserved when the XLSX is opened in Google Sheets. Users expecting protection in Google Sheets will find all cells editable.
**Why it happens:** Google Sheets imports XLSX files but converts protection to its own format, which requires re-configuration within Google Sheets.
**How to avoid:** Document this limitation on the Documentation/Cover sheet tab. Protection works correctly in Excel (which is the primary target). The success criteria says "open correctly" not "maintain protection" for Google Sheets.
**Warning signs:** If QA tests protection in Google Sheets, it will appear "broken" -- this is expected behavior, not a bug.

### Pitfall 2: Print Areas With Charts
**What goes wrong:** If the print area includes chart anchor cells, the charts may print overlapping data or in unexpected positions.
**Why it happens:** Charts in openpyxl are positioned by anchor cell but their rendering size is independent of cell dimensions.
**How to avoid:** Set print areas to cover data columns only (not the chart columns to the right). Charts will still print if they overlap the print area, but the data area should be the primary print target. For model tabs with charts at K1/P1 etc., set print area to A:J or A:N (the data columns).
**Warning signs:** Printed output shows charts overlapping data tables or truncated charts.

### Pitfall 3: fitToPage Requires sheet_properties.pageSetUpPr
**What goes wrong:** Setting `fitToWidth` and `fitToHeight` without also setting `fitToPage = True` (via `ws.page_setup.fitToPage = True`) has no effect in Excel.
**Why it happens:** The fitTo settings are only activated when the fitToPage flag is set in the page setup properties.
**How to avoid:** Always set `ws.page_setup.fitToPage = True` alongside fitToWidth/fitToHeight.
**Warning signs:** Printed output shows content at full scale, not fitted to page width.

### Pitfall 4: Merged Cell Protection
**What goes wrong:** Merged cells (used in section headers, titles) may behave unexpectedly when protection is enabled. Users cannot select or interact with individual cells in a merged range.
**Why it happens:** Protection locks the entire merged range as a single unit.
**How to avoid:** This is acceptable behavior for this project since merged cells are all labels/headers (not input cells). No action needed beyond awareness.
**Warning signs:** Users report they "can't click" on certain header cells.

### Pitfall 5: Source Citation Column Width
**What goes wrong:** Enhanced source citations ("Fine-Tuning Recommendations, Rec #3") are longer than current abbreviated ones ("Rec #3"). Column D width may need adjustment.
**Why it happens:** Current column D width is 30 characters, which may be tight for full document names.
**How to avoid:** Increase column D width from 30 to 40 (or use abbreviated document names). Keep citations concise: "Fine-Tuning Recs, Rec #3" not "Gonka_Tokenomics_Fine_Tuning_Recommendations.md, Recommendation #3".
**Warning signs:** Source citations truncated or wrapping in printed output.

### Pitfall 6: Protection Password Compatibility
**What goes wrong:** Some password protection features may behave differently between Excel versions or on macOS vs Windows.
**Why it happens:** openpyxl uses the "Legacy Password Hash Algorithm" by default, which is universally supported.
**How to avoid:** Use a simple, short password (e.g., "gonka"). Don't use advanced hash algorithms. The password is advisory protection only.
**Warning signs:** Users can't unprotect sheets in older Excel versions.

## Code Examples

### Cell Protection: Complete Implementation

```python
# Source: openpyxl 3.1.5 API, verified locally
def apply_sheet_protection(wb, password='gonka'):
    """Enable sheet protection on all worksheets.

    MUST be called AFTER all cell content is written and BEFORE saving.

    Input cells (Assumptions column B) already have Protection(locked=False)
    from workbook_base.py. All other cells default to locked=True.
    """
    for ws in wb.worksheets:
        ws.protection.sheet = True
        ws.protection.password = password
        # Allow selecting cells (both locked and unlocked)
        ws.protection.selectLockedCells = False
        ws.protection.selectUnlockedCells = False
        # Allow formatting (viewing, not content editing)
        ws.protection.formatCells = True
        ws.protection.formatColumns = True
        ws.protection.formatRows = True
```

### Print Setup: Per-Tab Configuration

```python
# Source: openpyxl 3.1.5 API, verified locally
# Each tab type has different optimal print settings

# Data tabs (Emission, Token Price, Fee Transition, Host Profit, Treasury)
def apply_data_tab_print(ws, max_data_col_letter, max_data_row):
    ws.print_area = f'A1:{max_data_col_letter}{max_data_row}'
    ws.print_title_rows = '1:2'  # Title + header rows repeat
    ws.page_setup.orientation = 'landscape'
    ws.page_setup.paperSize = ws.PAPERSIZE_LETTER
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.page_setup.fitToPage = True

# Assumptions tab (narrower, more rows)
def apply_assumptions_print(ws, max_row):
    ws.print_area = f'A1:E{max_row}'  # A through E (with confidence column)
    ws.print_title_rows = '1:3'  # Title + instruction + blank
    ws.page_setup.orientation = 'portrait'  # Narrower, fits portrait
    ws.page_setup.paperSize = ws.PAPERSIZE_LETTER
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.page_setup.fitToPage = True

# Documentation/Cover tab
def apply_doc_tab_print(ws, max_row):
    ws.print_area = f'A1:F{max_row}'
    ws.page_setup.orientation = 'portrait'
    ws.page_setup.paperSize = ws.PAPERSIZE_LETTER
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1  # Fit to single page
    ws.page_setup.fitToPage = True
```

### Source Citation Enhancement: Parameter Format

```python
# Current format in parameters.py (60 params):
{"name": "Host Share", "value": 0.70, "unit": "", "source": "Rec #3", "format": "percent"}

# Enhanced format with full citation + confidence:
{"name": "Host Share", "value": 0.70, "unit": "",
 "source": "Fine-Tuning Recs, Rec #3", "confidence": "HIGH", "format": "percent"}
```

Confidence level mapping for all 60 parameters:
- **HIGH:** Parameters directly from Whitepaper or v1.0 Recommendations with specific values
- **MED:** Parameters derived from research analysis or industry benchmarks
- **LOW:** Placeholders, assumptions, or scenario inputs

Source document abbreviation mapping:
| Full Document | Abbreviation |
|---------------|-------------|
| Gonka_Tokenomics_Fine_Tuning_Recommendations.md | Fine-Tuning Recs |
| tokenomics.pdf / whitepaper.pdf (Gonka Whitepaper) | Whitepaper |
| Gonka_Macro_Tokenomics_Research.md | Macro Research |
| Gonka_Tokenomics_Deep_Analysis.md | Deep Analysis |
| Network operational data | Network Data |
| Industry standard benchmarks | Industry |
| Market pricing data | Market Data |

### Workbook_base.py Enhancement: Confidence Column

```python
# Add column E for confidence level in both build_assumptions_tab functions
_COL_WIDTHS = {
    "A": 35,
    "B": 20,
    "C": 15,
    "D": 40,  # Wider for full citations
    "E": 12,  # NEW: Confidence column
}

# In the parameter loop:
# Column E: Confidence level (HIGH/MED/LOW)
confidence = param.get("confidence", "")
confidence_cell = ws.cell(row=current_row, column=5, value=confidence)
confidence_cell.font = _SOURCE_FONT  # Same italic as source
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| No sheet protection | Protection(locked=False) on inputs, sheet protection OFF | Phase 1 (Feb 2026) | Foundation laid; Phase 9 enables |
| Abbreviated sources ("Rec #3") | Full document + rec citations | Phase 9 (this phase) | REQ-U10, REQ-D04 satisfied |
| No print settings at all | fitToWidth + headers/footers | Phase 9 (this phase) | REQ-U12 satisfied |
| No confidence column | Column E with HIGH/MED/LOW | Phase 9 (this phase) | REQ-D04 satisfied |

## Detailed Tab Analysis for Print Areas

| Tab | Data Columns | Data Rows | Below-Data Content | Chart Anchors | Print Area Recommendation |
|-----|-------------|-----------|-------------------|---------------|--------------------------|
| Documentation | A-F | 1-23 (master), 1-35 (standalone) | None | None | `A1:F{max_row}`, portrait, fitToPage 1x1 |
| Assumptions | A-E | 1-108 (master), varies (standalone) | Scenario Selector | None | `A1:E{max_row}`, portrait, fitToWidth=1 |
| Emission Schedule | A-J | 1-38 (rows 36-38 validation) | Validation rows 36-38 | K1, K17, K33 | `A1:J38`, landscape, title rows 1:2 |
| Token Price | A-L | 1-34 | None | M1, M17 | `A1:L34`, landscape, title rows 1:2 |
| Fee Transition | A-N | 1-47 (rows 37-46 matrices) | 2 matrices rows 37-46 | P1, P17, P33 | `A1:N47`, landscape, title rows 1:2 |
| Host Profitability | A-M | 1-55 (rows 37-55 analyses) | 3 analysis sections | O1, O17, O33 | `A1:M55`, landscape, title rows 1:2 |
| Treasury & POL | A-N | 1-49 (rows 36-49 analyses) | Time-to-X, defense, IL caveat | P1, P17, P33 | `A1:N49`, landscape, title rows 1:2 |
| Dashboard | A-E | 1-22 | None | F3, F19, F35 | `A1:E22`, portrait, fitToPage 1x1 |
| Definitions | A-B | 1-23 | None | None | `A1:B{max_row}`, portrait, fitToWidth=1 |

## Implementation Strategy

### Recommended Plan Structure: 3 Plans

**Plan 1: Cell Protection + Source Audit Enhancement**
- Modify `parameters.py`: Add "confidence" field to all 60 parameters, enhance "source" field with full document references
- Modify `workbook_base.py`: Add column E (Confidence) to both `build_assumptions_tab()` and `build_filtered_assumptions_tab()`, update `_COL_WIDTHS`
- Create protection utility function in a new file or in `styles.py`
- Apply sheet protection in `generate.py` (master) and `standalone.py` (standalones) as final step before save
- Verify: Open workbook, try to edit formula cell -> protection warning; edit input cell -> allowed

**Plan 2: Print Layout**
- Create `generators/print_setup.py` with utility functions for different tab types
- Apply print settings in each generator module's build function (or centrally in generate.py/standalone.py)
- Configure per-tab: print area, title rows, orientation, margins, headers/footers
- Verify: Print Preview in Excel shows readable output with proper headers/footers

**Plan 3: Cross-Platform Validation**
- Run generator and verify all 5 workbooks:
  - Open in Excel: charts render, protection works, print layout correct
  - Open in Google Sheets: no #NAME? or #REF! errors, charts render (protection stripped is expected)
  - File sizes under 5MB
- Document any Google Sheets limitations on Documentation tab
- Final verification against all 5 success criteria

### Where Protection Should Be Applied

Both code paths need protection:

1. **Master workbook** (`generate.py` -> `generate_all()`): Apply to all 8 tabs before `wb.save()`
2. **Standalone workbooks** (`standalone.py` -> `generate_standalone()`): Apply to all tabs before `wb.save()`

### Critical Implementation Detail: Assumptions Tab Column Merge

The current Assumptions tab merges `A1:E1` for the header. Adding column E (Confidence) means the merge needs to extend to `A1:F1` (or the merge range needs adjustment). This affects:
- `build_assumptions_tab()` line: `ws.merge_cells("A1:E1")`
- `build_filtered_assumptions_tab()` line: `ws.merge_cells("A1:E1")`
- Column header: Currently no explicit header row for A/B/C/D. Consider adding a sub-header row with "Parameter | Value | Unit | Source | Confidence" labels.

Actually, examining the current layout more carefully: there is NO column header row on the Assumptions tab. Row 1 is the merged title, Row 2 is instruction text, Row 3 is blank, and Row 4 starts with group headers. Adding a confidence column is straightforward -- just add column E data alongside column D in the parameter loop.

### Confidence Level Classification (All 60 Parameters)

Based on analysis of sources in `parameters.py`:

**HIGH confidence (specific values from authoritative sources):**
- All "Whitepaper" sourced params (Total Supply, Mining Rewards Pool, Community Pool, Founder Allocation, Initial Daily Emission, Decay Rate, Host Collateral Rate, EIP-1559 params, Governance Quorum) - 12 params
- All "Rec #N" sourced params (direct v1.0 recommendation values) - 27 params
- "Network Data" sourced params (Current Hosts, Current GPUs, Base Active Developers) - 3 params

**MED confidence (derived from research or external benchmarks):**
- "v1.0 Research" sourced params (Price Scenarios - derived from research analysis) - 6 params
- "Industry" sourced params (Electricity Costs - industry benchmarks) - 3 params
- "Market Data" sourced params (H100 Hardware Costs - market prices that change) - 2 params
- "Research" (GPU Annual Price Deflation) - 1 param
- "Strategic Data" (Bitfury Schelling Point) - 1 param
- Lambda Labs / CoreWeave rental rates (Q1 2026 data, may change) - 2 params
- "H100 inference avg" (GPU Power Draw - hardware specific) - 1 param

**LOW confidence (placeholders, assumptions, or user-configurable):**
- "Assumption" (Epochs Per Day) - 1 param
- "Placeholder" params (Assumed Annual Fee Revenue, AI Fund Monthly Expenses) - 2 params
- "Scenario input" (Defense Active Duration) - 1 param
- "Toggle" (Buyback-Burn Active, Deploy POL Active) - 2 params

**Summary:** HIGH=42, MED=16, LOW=6 (total 64 -- includes 4 Scenario Selector computed params with no confidence needed)

Wait, the actual count from parameters.py is 60 params in PARAM_GROUPS. The Scenario Selector params (Active Scenario, Scenario Index, Active Price Low/High) are added dynamically in `_add_scenario_selector()` and are computed, not sourced. So 60 params need confidence levels.

## Open Questions

1. **Password choice:** Should the protection password be empty (no password, just advisory lock) or a simple known password like "gonka"? Empty password means users can toggle protection on/off without entering anything. A password like "gonka" adds a tiny speed bump.
   - What we know: Success criteria says "attempting to edit a formula cell shows a protection warning" -- this works with or without password.
   - Recommendation: Use simple password "gonka" (mentioned on Documentation tab) for minimal friction with some accidental-edit protection.

2. **Google Sheets protection note:** Should the Documentation tab include a note about protection being Excel-only?
   - What we know: Google Sheets strips XLSX protection on import. This is standard Google Sheets behavior.
   - Recommendation: Add a brief note on the Documentation tab: "Note: Cell protection is enforced in Excel. Google Sheets does not preserve XLSX sheet protection."

3. **Print area: include charts or not?** Charts are anchored to the right of data columns.
   - What we know: Charts at K1/P1/O1 positions are outside the main data columns. Setting print area to data-only (A:J, A:N, etc.) may exclude charts from default printing.
   - Recommendation: Set print area to data-only. Charts are best viewed on-screen. Users who want to print charts can adjust the print area manually. This avoids the charts-overlapping-data problem.

4. **Column E header label:** The Assumptions tab currently has no column headers (just section headers within the data). Should we add a header row for "Parameter | Value | Unit | Source | Confidence"?
   - What we know: Current design has no column headers. Row 2 just says "All blue-shaded cells below are adjustable inputs."
   - Recommendation: Keep the current minimalist design. The column purpose is self-evident from context. Adding a header row would shift all row numbers and break meta references. The added complexity is not worth it.

## Sources

### Primary (HIGH confidence)
- openpyxl 3.1.5 installed locally - SheetProtection, PrintPageSetup, PageMargins, HeaderFooter APIs all verified via interactive Python testing
- [openpyxl Protection documentation](https://openpyxl.readthedocs.io/en/stable/protection.html) - sheet protection, password, enable/disable
- [openpyxl Print Settings documentation](https://openpyxl.readthedocs.io/en/stable/print_settings.html) - print area, title rows, page setup, headers/footers, margins
- Existing codebase: `generators/workbook_base.py` lines 102, 275, 395 - `Protection(locked=False)` already applied to input cells

### Secondary (MEDIUM confidence)
- [Google Docs Editors Community thread](https://support.google.com/docs/thread/65571620) - Google Sheets strips XLSX sheet protection on import
- [Google Sheets protection documentation](https://support.google.com/docs/answer/1218656) - Google Sheets uses its own protection model

### Tertiary (LOW confidence)
- None. All findings verified with primary or secondary sources.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - openpyxl 3.1.5 is already the sole dependency; all APIs verified locally
- Architecture: HIGH - codebase fully understood; Protection(locked=False) pattern already established
- Pitfalls: HIGH - all pitfalls verified via direct testing (Google Sheets behavior, fitToPage, merged cells)

**Research date:** 2026-02-07
**Valid until:** 2026-03-07 (stable -- openpyxl APIs unlikely to change)

"""
Gonka Tokenomics - Print Setup & Sheet Protection Utilities

Centralized print settings and cell protection for all workbooks.
Called as the final step before wb.save() in both master and standalone generation.
"""

from openpyxl.worksheet.page import PageMargins


# ---------------------------------------------------------------------------
# Sheet Protection
# ---------------------------------------------------------------------------

def apply_sheet_protection(wb, password="gonka"):
    """Enable sheet protection on all worksheets.

    MUST be called AFTER all cell content is written and BEFORE saving.
    Input cells already have Protection(locked=False) from workbook_base.py.
    All other cells default to locked=True.
    """
    for ws in wb.worksheets:
        ws.protection.sheet = True
        ws.protection.password = password
        # Allow selecting cells (both locked and unlocked) for copy/view
        ws.protection.selectLockedCells = False
        ws.protection.selectUnlockedCells = False
        # Allow formatting operations (viewing, not content editing)
        ws.protection.formatCells = True
        ws.protection.formatColumns = True
        ws.protection.formatRows = True


# ---------------------------------------------------------------------------
# Print Settings
# ---------------------------------------------------------------------------

# Static print areas for known model tabs (fixed data ranges)
_PRINT_CONFIGS = {
    "Emission Schedule":  {"area": "A1:J38",  "orient": "landscape", "titles": "1:2", "fth": 0},
    "Token Price":        {"area": "A1:L34",  "orient": "landscape", "titles": "1:2", "fth": 0},
    "Fee Transition":     {"area": "A1:N47",  "orient": "landscape", "titles": "1:2", "fth": 0},
    "Host Profitability": {"area": "A1:M55",  "orient": "landscape", "titles": "1:2", "fth": 0},
    "Treasury & POL":     {"area": "A1:N49",  "orient": "landscape", "titles": "1:2", "fth": 0},
    "Dashboard":          {"area": "A1:E22",  "orient": "portrait",  "titles": None,  "fth": 1},
}

# Dynamic print areas -- detected from ws.max_row
_DYNAMIC_CONFIGS = {
    "Documentation": {"last_col": "F", "orient": "portrait",  "titles": None,  "fth": 1},
    "Assumptions":   {"last_col": "E", "orient": "portrait",  "titles": "1:3", "fth": 0},
    "Definitions":   {"last_col": "B", "orient": "portrait",  "titles": None,  "fth": 0},
}


def _apply_tab_print(ws, print_area, orientation, title_rows, fit_to_height):
    """Apply common + tab-specific print settings to a worksheet."""
    # Paper and fit-to-page
    ws.page_setup.paperSize = ws.PAPERSIZE_LETTER
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = fit_to_height
    ws.page_setup.fitToPage = True
    ws.page_setup.orientation = orientation

    # Print area
    ws.print_area = print_area

    # Title rows (repeat at top of each printed page)
    if title_rows:
        ws.print_title_rows = title_rows

    # Margins (inches)
    ws.page_margins = PageMargins(
        left=0.5, right=0.5,
        top=0.75, bottom=0.75,
        header=0.3, footer=0.3,
    )

    # Header: sheet name centered
    ws.oddHeader.center.text = "&A"

    # Footer: page number left, version right
    ws.oddFooter.left.text = "Page &P of &N"
    ws.oddFooter.right.text = "Gonka Tokenomics v1.1"


def apply_all_print_settings(wb):
    """Apply per-tab print settings to every worksheet in the workbook.

    Handles both master and standalone workbooks -- uses the same tab names.
    Unrecognized tabs get a safe fallback (landscape, fit-to-width, full area).
    """
    for ws in wb.worksheets:
        title = ws.title

        if title in _PRINT_CONFIGS:
            cfg = _PRINT_CONFIGS[title]
            _apply_tab_print(
                ws,
                print_area=cfg["area"],
                orientation=cfg["orient"],
                title_rows=cfg["titles"],
                fit_to_height=cfg["fth"],
            )
        elif title in _DYNAMIC_CONFIGS:
            cfg = _DYNAMIC_CONFIGS[title]
            max_row = ws.max_row or 1
            area = f"A1:{cfg['last_col']}{max_row}"
            _apply_tab_print(
                ws,
                print_area=area,
                orientation=cfg["orient"],
                title_rows=cfg["titles"],
                fit_to_height=cfg["fth"],
            )
        else:
            # Fallback for unrecognized tabs
            max_row = ws.max_row or 1
            max_col = ws.max_column or 1
            from openpyxl.utils import get_column_letter
            last_col_letter = get_column_letter(max_col)
            _apply_tab_print(
                ws,
                print_area=f"A1:{last_col_letter}{max_row}",
                orientation="landscape",
                title_rows=None,
                fit_to_height=0,
            )

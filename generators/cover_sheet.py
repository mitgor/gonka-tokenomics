"""
Gonka Tokenomics - Standalone Cover Sheet (Documentation Tab)

Builds a "Documentation" worksheet at index 0 for standalone workbooks with:
  - Model-specific title and subtitle
  - Version number and generated date (REQ-D08)
  - Disclaimer in red italic
  - Protection compatibility note (Excel-only; Google Sheets strips it)
  - Changelog table (REQ-D08)
  - Scenario narratives (REQ-D03)
  - Hyperlinked Table of Contents
  - Color convention legend

This module is for STANDALONE workbooks only. The master workbook
continues using generators/documentation.py.

Public API:
    build_cover_sheet(wb, title, version_info, tab_names, scenario_narratives=None) -> None
"""

from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import quote_sheetname

from generators.styles import TAB_COLOR_DOCS, SECTION_FONT_COLOR


# ---------------------------------------------------------------------------
# Module-level constants
# ---------------------------------------------------------------------------

LINK_FONT = Font(name="Calibri", size=11, color="0563C1", underline="single")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def build_cover_sheet(wb, title, version_info, tab_names, scenario_narratives=None):
    """Build a Documentation (cover) sheet for standalone workbooks.

    Args:
        wb: openpyxl Workbook (styles already registered).
        title: Model-specific title (e.g., "Token Price Model").
        version_info: dict with ``"version"`` (str) and ``"changelog"``
            (list of ``(ver, date, desc)`` tuples).
        tab_names: List of tab names for the TOC (excluding Documentation).
        scenario_narratives: Optional dict of
            ``{"Conservative": "...", "Base": "...", "Aggressive": "..."}``.

    Returns:
        None -- modifies ``wb`` in-place.
    """
    ws = wb.create_sheet("Documentation", index=0)
    ws.sheet_properties.tabColor = TAB_COLOR_DOCS

    # =================================================================
    # Section 1: Title (rows 1-2)
    # =================================================================
    ws.merge_cells("A1:F1")
    title_cell = ws.cell(row=1, column=1, value="GONKA TOKENOMICS MODEL")
    title_cell.font = Font(
        name="Calibri", size=18, bold=True, color=SECTION_FONT_COLOR,
    )
    title_cell.alignment = Alignment(horizontal="center")

    ws.merge_cells("A2:F2")
    subtitle_cell = ws.cell(
        row=2, column=1,
        value=f"{title} \u2014 Standalone Workbook",
    )
    subtitle_cell.font = Font(name="Calibri", size=14, color=SECTION_FONT_COLOR)
    subtitle_cell.alignment = Alignment(horizontal="center")

    # =================================================================
    # Section 2: Version and Date (rows 4-5)
    # =================================================================
    ws.cell(row=4, column=1, value="Version:").font = Font(
        name="Calibri", size=11, bold=True,
    )
    ws.cell(row=4, column=2, value=version_info["version"])

    ws.cell(row=5, column=1, value="Generated:").font = Font(
        name="Calibri", size=11, bold=True,
    )
    date_cell = ws.cell(row=5, column=2, value="=TODAY()")
    date_cell.number_format = "YYYY-MM-DD"

    # =================================================================
    # Section 3: Disclaimer (row 7)
    # =================================================================
    ws.merge_cells("A7:F7")
    disclaimer_cell = ws.cell(
        row=7, column=1,
        value="For internal decision-making purposes only",
    )
    disclaimer_cell.font = Font(
        name="Calibri", size=11, italic=True, color="FF0000",
    )

    # =================================================================
    # Section 4: Protection Note (row 8)
    # =================================================================
    ws.merge_cells("A8:F8")
    protection_note = ws.cell(
        row=8, column=1,
        value=(
            "Note: Cell protection prevents accidental formula edits "
            "(password: gonka). Google Sheets does not preserve XLSX "
            "sheet protection."
        ),
    )
    protection_note.font = Font(
        name="Calibri", size=11, italic=True, color="FF0000",
    )

    # =================================================================
    # Section 5: Changelog (rows 10+)
    # =================================================================
    ws.cell(row=10, column=1, value="CHANGELOG").style = "section_header"

    # Column headers
    ws.cell(row=11, column=1, value="Version").font = Font(
        name="Calibri", size=11, bold=True,
    )
    ws.cell(row=11, column=2, value="Date").font = Font(
        name="Calibri", size=11, bold=True,
    )
    ws.cell(row=11, column=3, value="Description").font = Font(
        name="Calibri", size=11, bold=True,
    )

    current_row = 12
    for ver, date, description in version_info["changelog"]:
        ws.cell(row=current_row, column=1, value=ver)
        ws.cell(row=current_row, column=2, value=date)
        ws.cell(row=current_row, column=3, value=description)
        current_row += 1

    # =================================================================
    # Section 6: Scenario Narratives (if provided) -- REQ-D03
    # =================================================================
    if scenario_narratives:
        current_row += 1  # blank separator
        ws.cell(
            row=current_row, column=1, value="SCENARIO NARRATIVES",
        ).style = "section_header"
        current_row += 1

        for scenario in ["Conservative", "Base", "Aggressive"]:
            narrative = scenario_narratives.get(scenario)
            if narrative is None:
                continue

            ws.cell(row=current_row, column=1, value=scenario).font = Font(
                name="Calibri", size=11, bold=True,
            )
            ws.merge_cells(
                start_row=current_row, start_column=2,
                end_row=current_row, end_column=5,
            )
            narr_cell = ws.cell(row=current_row, column=2, value=narrative)
            narr_cell.alignment = Alignment(wrap_text=True, vertical="top")
            ws.row_dimensions[current_row].height = max(
                30, len(narrative) // 60 * 15 + 15,
            )
            current_row += 2  # blank row between scenarios

    # =================================================================
    # Section 7: Table of Contents
    # =================================================================
    current_row += 1  # blank separator
    ws.cell(
        row=current_row, column=1, value="TABLE OF CONTENTS",
    ).style = "section_header"
    current_row += 1

    for idx, name in enumerate(tab_names, start=1):
        cell = ws.cell(row=current_row, column=1, value=f"{idx}. {name}")
        quoted_name = quote_sheetname(name)
        cell.hyperlink = f"#{quoted_name}!A1"
        cell.font = LINK_FONT
        current_row += 1

    # =================================================================
    # Section 8: Color Convention Legend
    # =================================================================
    current_row += 1  # blank separator
    ws.cell(
        row=current_row, column=1, value="COLOR CONVENTIONS",
    ).style = "section_header"
    current_row += 1

    _legend_entries = [
        ("Blue cells = Editable inputs (Assumptions tab)", "input_cell"),
        ("Black text = Calculated formulas", "formula_cell"),
        ("Green text = Cross-tab references", "crossref_cell"),
        ("Blue headers = Column headers", "header"),
        ("Red shading = Danger zones / warnings", "warning_cell"),
    ]
    for description, style_name in _legend_entries:
        ws.cell(row=current_row, column=1, value=description)
        sample_cell = ws.cell(row=current_row, column=2, value="Example")
        sample_cell.style = style_name
        current_row += 1

    # =================================================================
    # Column widths
    # =================================================================
    col_widths = {"A": 35, "B": 25, "C": 20, "D": 15, "E": 15, "F": 15}
    for col_letter, width in col_widths.items():
        ws.column_dimensions[col_letter].width = width

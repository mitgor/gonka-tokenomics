"""
Gonka Tokenomics - Workbook Base (Assumptions Tab Builder)

Core function: build_assumptions_tab(wb) writes all parameters from PARAM_GROUPS
to a formatted Assumptions sheet and returns the param_refs dict.

The param_refs dict is THE critical interface contract: every downstream model
module (emission, token_price, fee_transition, etc.) receives this dict to
write Excel formulas referencing Assumptions!$B$N cells.

create_workbook() is the convenience entry point that creates a fresh workbook,
builds the Assumptions tab, and returns (wb, param_refs).
"""

from openpyxl import Workbook
from openpyxl.styles import Font, Protection
from openpyxl.utils import get_column_letter

from models.parameters import PARAM_GROUPS
from generators.styles import (
    register_styles,
    FORMAT_TO_STYLE,
    INPUT_FILL_COLOR,
    INPUT_FONT_COLOR,
    TAB_COLOR_INPUT,
)


# Column widths for the Assumptions tab
_COL_WIDTHS = {
    "A": 35,
    "B": 20,
    "C": 15,
    "D": 30,
}

# Font for source citations (italic)
_SOURCE_FONT = Font(name="Calibri", size=11, italic=True)


def build_assumptions_tab(wb):
    """Build the Assumptions tab with all parameters from PARAM_GROUPS.

    Takes an openpyxl Workbook (already created), writes the formatted
    Assumptions sheet, and returns a param_refs dict mapping every parameter
    name to its absolute cell reference (e.g., "Assumptions!$B$12").

    Args:
        wb: An openpyxl Workbook instance.

    Returns:
        dict: Mapping of parameter name -> "Assumptions!$B$N" cell reference.
    """
    # Register all named styles with this workbook
    register_styles(wb)

    # Get or create the active worksheet, rename to "Assumptions"
    ws = wb.active
    ws.title = "Assumptions"
    ws.sheet_properties.tabColor = TAB_COLOR_INPUT

    # --- Row 1: Main header (merged A1:E1) ---
    ws.merge_cells("A1:E1")
    cell_a1 = ws["A1"]
    cell_a1.value = "GONKA TOKENOMICS MODEL - ASSUMPTIONS"
    cell_a1.style = "section_header"

    # --- Row 2: Instruction text (merged A2:E2) ---
    ws.merge_cells("A2:E2")
    cell_a2 = ws["A2"]
    cell_a2.value = "All blue-shaded cells below are adjustable inputs"

    # --- Row 3: Blank separator ---
    current_row = 4  # Start data from row 4

    # --- Build param_refs dict as we write parameters ---
    param_refs = {}

    for group_name, params in PARAM_GROUPS.items():
        # Section header row
        ws.merge_cells(
            start_row=current_row, start_column=1,
            end_row=current_row, end_column=4,
        )
        section_cell = ws.cell(row=current_row, column=1)
        section_cell.value = group_name
        section_cell.style = "section_header"
        current_row += 1

        # Parameter rows
        for param in params:
            # Column A: Parameter name (locked by default)
            ws.cell(row=current_row, column=1, value=param["name"])

            # Column B: Parameter value (UNLOCKED input cell)
            value_cell = ws.cell(row=current_row, column=2, value=param["value"])
            value_cell.style = "input_cell"

            # Override number_format based on parameter's format type
            format_key = param["format"]
            if format_key in FORMAT_TO_STYLE:
                style_name = FORMAT_TO_STYLE[format_key]
                # Look up the number_format from the registered named style
                named_style = wb._named_styles[style_name]
                value_cell.number_format = named_style.number_format
            value_cell.protection = Protection(locked=False)

            # Column C: Unit string (locked by default)
            ws.cell(row=current_row, column=3, value=param["unit"])

            # Column D: Source citation (locked, italic)
            source_cell = ws.cell(row=current_row, column=4, value=param["source"])
            source_cell.font = _SOURCE_FONT

            # Record the cell reference for this parameter
            param_refs[param["name"]] = f"Assumptions!$B${current_row}"

            current_row += 1

        # Blank separator row after each group
        current_row += 1

    # --- Set column widths ---
    for col_letter, width in _COL_WIDTHS.items():
        ws.column_dimensions[col_letter].width = width

    # --- Freeze panes at A4 (header rows always visible) ---
    ws.freeze_panes = "A4"

    return param_refs


def create_workbook():
    """Create a new workbook with styles registered and Assumptions tab built.

    Returns:
        tuple: (wb, param_refs) where wb is the openpyxl Workbook and
               param_refs maps parameter names to Assumptions!$B$N addresses.
    """
    wb = Workbook()
    param_refs = build_assumptions_tab(wb)
    return wb, param_refs

"""
Gonka Tokenomics - NamedStyle Definitions and Color Conventions

Financial modeling color conventions:
  - Blue  = input (editable cells on Assumptions tab)
  - Black = formula (calculated cells)
  - Green = cross-tab link (references to other sheets)

Number formats per REQ-U06:
  - USD:         $#,##0
  - Percentages: 0.0%
  - Tokens:      #,##0

Single font throughout: Calibri 11pt (financial modeling convention).

Usage:
  from generators.styles import register_styles
  register_styles(wb)  # Call once per workbook creation
"""

from openpyxl.styles import (
    NamedStyle,
    Font,
    Border,
    Side,
    Alignment,
    PatternFill,
)


# =============================================================================
# COLOR CONSTANTS
# =============================================================================

# Cell type colors
INPUT_FILL_COLOR = "DAEEF3"       # Light blue background for editable cells
INPUT_FONT_COLOR = "000080"       # Dark blue font for input values
FORMULA_FONT_COLOR = "000000"     # Black font for formula cells
CROSSREF_FONT_COLOR = "006100"    # Green font for cross-tab references
HEADER_FILL_COLOR = "4472C4"      # Blue background for column headers
HEADER_FONT_COLOR = "FFFFFF"      # White font for headers
SECTION_FONT_COLOR = "2F5496"     # Dark blue for section headers
SECTION_BORDER_COLOR = "2F5496"   # Dark blue border under section headers
WARNING_FONT_COLOR = "FF0000"     # Red for warnings/thresholds
WARNING_FILL_COLOR = "FFC7CE"     # Light red background for danger zones

# Tab colors (for worksheet tab coloring)
TAB_COLOR_INPUT = "4472C4"        # Blue tab for Assumptions
TAB_COLOR_DOCS = "70AD47"         # Green tab for Documentation
TAB_COLOR_CALC = "A5A5A5"         # Gray tab for calculation sheets
TAB_COLOR_DASHBOARD = "ED7D31"    # Orange tab for Dashboard


# =============================================================================
# SHARED FONT
# =============================================================================

_FONT_NAME = "Calibri"
_FONT_SIZE = 11


# =============================================================================
# NAMED STYLE DEFINITIONS
# =============================================================================

# 1. input_cell -- Blue-shaded input cells on Assumptions tab (REQ-U02, REQ-U05)
INPUT_STYLE = NamedStyle(name="input_cell")
INPUT_STYLE.font = Font(
    name=_FONT_NAME,
    size=_FONT_SIZE,
    color=INPUT_FONT_COLOR,
    bold=False,
)
INPUT_STYLE.fill = PatternFill(
    start_color=INPUT_FILL_COLOR,
    end_color=INPUT_FILL_COLOR,
    fill_type="solid",
)
INPUT_STYLE.number_format = "#,##0.00"
INPUT_STYLE.alignment = Alignment(horizontal="left")

# 2. formula_cell -- Formula cells on calculation tabs (REQ-U05)
FORMULA_STYLE = NamedStyle(name="formula_cell")
FORMULA_STYLE.font = Font(
    name=_FONT_NAME,
    size=_FONT_SIZE,
    color=FORMULA_FONT_COLOR,
)
FORMULA_STYLE.number_format = "#,##0.00"

# 3. crossref_cell -- Cross-tab reference cells (REQ-U05)
CROSSREF_STYLE = NamedStyle(name="crossref_cell")
CROSSREF_STYLE.font = Font(
    name=_FONT_NAME,
    size=_FONT_SIZE,
    color=CROSSREF_FONT_COLOR,
)
CROSSREF_STYLE.number_format = "#,##0.00"

# 4. header -- Column headers
HEADER_STYLE = NamedStyle(name="header")
HEADER_STYLE.font = Font(
    name=_FONT_NAME,
    size=_FONT_SIZE,
    color=HEADER_FONT_COLOR,
    bold=True,
)
HEADER_STYLE.fill = PatternFill(
    start_color=HEADER_FILL_COLOR,
    end_color=HEADER_FILL_COLOR,
    fill_type="solid",
)
HEADER_STYLE.alignment = Alignment(horizontal="center", wrap_text=True)
HEADER_STYLE.border = Border(
    bottom=Side(style="thin"),
)

# 5. section_header -- Section headers on Assumptions tab
SECTION_HEADER_STYLE = NamedStyle(name="section_header")
SECTION_HEADER_STYLE.font = Font(
    name=_FONT_NAME,
    size=12,
    color=SECTION_FONT_COLOR,
    bold=True,
)
SECTION_HEADER_STYLE.border = Border(
    bottom=Side(style="medium", color=SECTION_BORDER_COLOR),
)

# 6. currency -- USD dollar amounts (REQ-U06: $#,##0)
CURRENCY_STYLE = NamedStyle(name="currency")
CURRENCY_STYLE.number_format = "$#,##0"
CURRENCY_STYLE.font = Font(
    name=_FONT_NAME,
    size=_FONT_SIZE,
    color=FORMULA_FONT_COLOR,
)

# 7. currency_precise -- USD with cents (for per-hour pricing)
CURRENCY_PRECISE_STYLE = NamedStyle(name="currency_precise")
CURRENCY_PRECISE_STYLE.number_format = "$#,##0.00"
CURRENCY_PRECISE_STYLE.font = Font(
    name=_FONT_NAME,
    size=_FONT_SIZE,
    color=FORMULA_FONT_COLOR,
)

# 8. percent -- Percentage values (REQ-U06: 0.0%)
PERCENT_STYLE = NamedStyle(name="percent")
PERCENT_STYLE.number_format = "0.0%"
PERCENT_STYLE.font = Font(
    name=_FONT_NAME,
    size=_FONT_SIZE,
    color=FORMULA_FONT_COLOR,
)

# 9. tokens -- Token amounts with commas (REQ-U06: #,##0)
TOKENS_STYLE = NamedStyle(name="tokens")
TOKENS_STYLE.number_format = "#,##0"
TOKENS_STYLE.font = Font(
    name=_FONT_NAME,
    size=_FONT_SIZE,
    color=FORMULA_FONT_COLOR,
)

# 10. decay_rate -- High-precision decimals (decay rates, small fractions)
DECAY_RATE_STYLE = NamedStyle(name="decay_rate")
DECAY_RATE_STYLE.number_format = "0.000000"
DECAY_RATE_STYLE.font = Font(
    name=_FONT_NAME,
    size=_FONT_SIZE,
    color=FORMULA_FONT_COLOR,
)

# 11. integer -- Whole numbers (years, counts, days)
INTEGER_STYLE = NamedStyle(name="integer")
INTEGER_STYLE.number_format = "#,##0"
INTEGER_STYLE.font = Font(
    name=_FONT_NAME,
    size=_FONT_SIZE,
    color=FORMULA_FONT_COLOR,
)

# 12. warning_cell -- Red warning/danger zone styling
WARNING_STYLE = NamedStyle(name="warning_cell")
WARNING_STYLE.font = Font(
    name=_FONT_NAME,
    size=_FONT_SIZE,
    color=WARNING_FONT_COLOR,
    bold=True,
)
WARNING_STYLE.fill = PatternFill(
    start_color=WARNING_FILL_COLOR,
    end_color=WARNING_FILL_COLOR,
    fill_type="solid",
)

# 13. number -- Generic numbers with 1 decimal (multipliers, etc.)
NUMBER_STYLE = NamedStyle(name="number")
NUMBER_STYLE.number_format = "#,##0.0"
NUMBER_STYLE.font = Font(
    name=_FONT_NAME,
    size=_FONT_SIZE,
    color=FORMULA_FONT_COLOR,
)


# =============================================================================
# ALL STYLES LIST (for registration)
# =============================================================================

_ALL_STYLES = [
    INPUT_STYLE,
    FORMULA_STYLE,
    CROSSREF_STYLE,
    HEADER_STYLE,
    SECTION_HEADER_STYLE,
    CURRENCY_STYLE,
    CURRENCY_PRECISE_STYLE,
    PERCENT_STYLE,
    TOKENS_STYLE,
    DECAY_RATE_STYLE,
    INTEGER_STYLE,
    WARNING_STYLE,
    NUMBER_STYLE,
]


# =============================================================================
# PUBLIC API
# =============================================================================

def register_styles(wb):
    """Register all named styles with a workbook. Call once per workbook creation.

    Safe to call multiple times on the same workbook -- duplicate registrations
    are silently ignored.
    """
    for style in _ALL_STYLES:
        try:
            wb.add_named_style(style)
        except ValueError:
            pass  # Style already registered


# Map from parameter format strings to NamedStyle names.
# Used by workbook_base to apply the correct style to each parameter cell.
FORMAT_TO_STYLE = {
    "currency": "currency",
    "percent": "percent",
    "tokens": "tokens",
    "decay_rate": "decay_rate",
    "integer": "integer",
    "price_per_hour": "currency_precise",
    "number": "number",
}

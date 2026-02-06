"""
Gonka Tokenomics - Emission Schedule Model Tab

Builds the "Emission Schedule" worksheet with 32 data rows:
  - 24 monthly periods (Y1 M01 through Y2 M12)
  - 8 annual periods (Year 3 through Year 10)

Every formula references the Assumptions tab via param_refs so that
changes to input parameters propagate automatically.

Public API:
    build_emission_tab(wb, param_refs) -> emission_meta dict
"""

from openpyxl.chart import LineChart, AreaChart, BarChart, Reference
from openpyxl.utils import get_column_letter

from generators.chart_utils import col_to_num
from generators.styles import TAB_COLOR_CALC


# ---------------------------------------------------------------------------
# Structural constants
# ---------------------------------------------------------------------------

# Founder vesting period in months.  Not on the Assumptions tab (no param_ref
# available), so we use the whitepaper value directly.
_VESTING_MONTHS = 48

# Column headers (A-J) in display order.
_HEADERS = [
    "Period Label",             # A
    "Start Epoch",              # B
    "End Epoch",                # C
    "Mining Emission (GNK)",    # D
    "Community Pool Unlock (GNK)",  # E
    "Founder Vesting (GNK)",    # F
    "Total New Supply (GNK)",   # G
    "Cumulative Circulating (GNK)",  # H
    "Annualized Inflation Rate (%)",  # I
    "ETH ~0.5%",                # J
]

# Column widths keyed by letter.
_COL_WIDTHS = {
    "A": 12,
    "B": 12,
    "C": 12,
    "D": 18,
    "E": 18,
    "F": 18,
    "G": 18,
    "H": 22,
    "I": 16,
    "J": 12,
}

# Style names applied to each column (by 1-based column index).
_COL_STYLES = {
    # A (period label) has no special numeric style -- left as General
    2: "integer",   # B  Start Epoch
    3: "integer",   # C  End Epoch
    4: "tokens",    # D  Mining Emission
    5: "tokens",    # E  Community Pool Unlock
    6: "tokens",    # F  Founder Vesting
    7: "tokens",    # G  Total New Supply
    8: "tokens",    # H  Cumulative Circulating
    9: "percent",   # I  Inflation Rate
    10: "percent",  # J  ETH benchmark
}


# ---------------------------------------------------------------------------
# Period construction
# ---------------------------------------------------------------------------

def _build_periods():
    """Return list of 32 period dicts (24 monthly + 8 annual).

    Each dict has keys: start, end, days, label.
    """
    periods = []

    # 24 monthly periods (m = 0 .. 23)
    for m in range(24):
        start = m * 30
        end = (m + 1) * 30
        year = m // 12 + 1
        month = m % 12 + 1
        label = f"Y{year} M{month:02d}"
        periods.append({"start": start, "end": end, "days": 30, "label": label})

    # 8 annual periods (years 3 .. 10)
    for y in range(3, 11):
        start = 720 + (y - 3) * 365
        end = start + 365
        label = f"Year {y}"
        periods.append({"start": start, "end": end, "days": 365, "label": label})

    return periods


# ---------------------------------------------------------------------------
# Chart helpers (private)
# ---------------------------------------------------------------------------

def _create_emission_decay_chart(ws, meta):
    """Add a line chart showing mining emission decay over 10 years."""
    chart = LineChart()
    chart.title = "Mining Emission Decay (10-Year)"
    chart.y_axis.title = "GNK per Period"
    chart.x_axis.title = "Period"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    d_col = col_to_num(meta["cols"]["mining_emission"])
    data = Reference(ws,
                     min_col=d_col, min_row=meta["header_row"],
                     max_row=meta["data_end_row"])
    chart.add_data(data, titles_from_data=True)

    a_col = col_to_num(meta["cols"]["period_label"])
    cats = Reference(ws,
                     min_col=a_col, min_row=meta["data_start_row"],
                     max_row=meta["data_end_row"])
    chart.set_categories(cats)

    # Line width: 25000 EMUs
    chart.series[0].graphicalProperties.line.width = 25000

    ws.add_chart(chart, "K1")


def _create_supply_composition_chart(ws, meta):
    """Add a stacked area chart showing circulating supply composition."""
    chart = AreaChart()
    chart.grouping = "stacked"
    chart.title = "Circulating Supply Composition"
    chart.y_axis.title = "GNK"
    chart.x_axis.title = "Period"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # Three series: Mining Emission (D), CP Unlock (E), Founder Vesting (F)
    for col_key in ("mining_emission", "cp_unlock", "founder_vest"):
        col_num = col_to_num(meta["cols"][col_key])
        data = Reference(ws,
                         min_col=col_num, min_row=meta["header_row"],
                         max_row=meta["data_end_row"])
        chart.add_data(data, titles_from_data=True)

    a_col = col_to_num(meta["cols"]["period_label"])
    cats = Reference(ws,
                     min_col=a_col, min_row=meta["data_start_row"],
                     max_row=meta["data_end_row"])
    chart.set_categories(cats)

    ws.add_chart(chart, "K17")


def _create_inflation_chart(ws, meta):
    """Add a bar chart showing annualized inflation vs ETH benchmark."""
    chart = BarChart()
    chart.type = "col"
    chart.title = "Annualized Inflation Rate"
    chart.y_axis.title = "Inflation Rate"
    chart.x_axis.title = "Period"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # Series 1: Inflation Rate (I)
    i_col = col_to_num(meta["cols"]["inflation_rate"])
    data1 = Reference(ws,
                      min_col=i_col, min_row=meta["header_row"],
                      max_row=meta["data_end_row"])
    chart.add_data(data1, titles_from_data=True)

    # Series 2: ETH Benchmark (J)
    j_col = col_to_num(meta["cols"]["eth_benchmark"])
    data2 = Reference(ws,
                      min_col=j_col, min_row=meta["header_row"],
                      max_row=meta["data_end_row"])
    chart.add_data(data2, titles_from_data=True)

    a_col = col_to_num(meta["cols"]["period_label"])
    cats = Reference(ws,
                     min_col=a_col, min_row=meta["data_start_row"],
                     max_row=meta["data_end_row"])
    chart.set_categories(cats)

    ws.add_chart(chart, "K33")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def build_emission_tab(wb, param_refs):
    """Create the Emission Schedule worksheet and populate formulas.

    Args:
        wb: An openpyxl Workbook with styles already registered.
        param_refs: dict mapping parameter names to "Assumptions!$B$N".

    Returns:
        dict: emission_meta with sheet coordinates for downstream tabs.
    """
    ws = wb.create_sheet(title="Emission Schedule")
    ws.sheet_properties.tabColor = TAB_COLOR_CALC

    # Resolve references we need
    e0_ref = param_refs["Initial Daily Emission"]
    r_ref = param_refs["Decay Rate"]
    cp_ref = param_refs["Community Pool"]
    founder_ref = param_refs["Founder Allocation"]

    # ------------------------------------------------------------------
    # Row 1: Merged title
    # ------------------------------------------------------------------
    ws.merge_cells("A1:J1")
    title_cell = ws.cell(row=1, column=1, value="EMISSION SCHEDULE MODEL")
    title_cell.style = "section_header"

    # ------------------------------------------------------------------
    # Row 2: Column headers
    # ------------------------------------------------------------------
    for col_idx, header_text in enumerate(_HEADERS, start=1):
        cell = ws.cell(row=2, column=col_idx, value=header_text)
        cell.style = "header"

    # ------------------------------------------------------------------
    # Rows 3-34: Data rows (32 periods)
    # ------------------------------------------------------------------
    periods = _build_periods()
    vest = _VESTING_MONTHS

    for i, period in enumerate(periods):
        row = 3 + i
        days = period["days"]

        # A: Period Label (plain text)
        ws.cell(row=row, column=1, value=period["label"])

        # B: Start Epoch (static integer)
        start_cell = ws.cell(row=row, column=2, value=period["start"])
        start_cell.style = "integer"

        # C: End Epoch (static integer)
        end_cell = ws.cell(row=row, column=3, value=period["end"])
        end_cell.style = "integer"

        # D: Mining Emission (GNK) -- closed-form exponential formula
        mining_formula = (
            f"={e0_ref}*EXP(-{r_ref}*B{row})"
            f"*(1-EXP(-{r_ref}*{days}))"
            f"/(1-EXP(-{r_ref}))"
        )
        d_cell = ws.cell(row=row, column=4, value=mining_formula)
        d_cell.style = "tokens"

        # E: Community Pool Unlock (GNK) -- linear over 3650 days
        cp_formula = f"={cp_ref}/3650*{days}"
        e_cell = ws.cell(row=row, column=5, value=cp_formula)
        e_cell.style = "tokens"

        # F: Founder Vesting (GNK) -- conditional formula
        #    IF end_epoch <= vest*30 => full period allocation
        #    ELIF start_epoch >= vest*30 => 0 (fully vested)
        #    ELSE => partial period (remaining months)
        vest_formula = (
            f"=IF(C{row}<={vest}*30,"
            f"{founder_ref}/{vest}*{days}/30,"
            f"IF(B{row}>={vest}*30,0,"
            f"{founder_ref}/{vest}*(({vest}*30-B{row})/30)))"
        )
        f_cell = ws.cell(row=row, column=6, value=vest_formula)
        f_cell.style = "tokens"

        # G: Total New Supply (GNK) = D + E + F
        g_formula = f"=D{row}+E{row}+F{row}"
        g_cell = ws.cell(row=row, column=7, value=g_formula)
        g_cell.style = "tokens"

        # H: Cumulative Circulating (GNK) -- running sum
        if i == 0:
            h_formula = f"=G{row}"
        else:
            h_formula = f"=H{row - 1}+G{row}"
        h_cell = ws.cell(row=row, column=8, value=h_formula)
        h_cell.style = "tokens"

        # I: Annualized Inflation Rate (%)
        if i == 0:
            # No prior circulating supply for first period
            ws.cell(row=row, column=9, value="")
        else:
            inf_formula = f"=(G{row}/(C{row}-B{row})*365)/H{row - 1}"
            inf_cell = ws.cell(row=row, column=9, value=inf_formula)
            inf_cell.style = "percent"

        # J: ETH ~0.5% benchmark (constant reference value)
        j_cell = ws.cell(row=row, column=10, value=0.005)
        j_cell.style = "percent"

    # ------------------------------------------------------------------
    # Row 35: Blank separator
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Rows 36-38: Validation rows
    # ------------------------------------------------------------------

    # Row 36: Closed-Form Total
    val_label_36 = ws.cell(row=36, column=1, value="Validation: Closed-Form Total")
    val_label_36.style = "formula_cell"
    val_formula_36 = (
        f"={e0_ref}*(1-EXP(-{r_ref}*3650))"
        f"/(1-EXP(-{r_ref}))"
    )
    val_cell_36 = ws.cell(row=36, column=2, value=val_formula_36)
    val_cell_36.style = "tokens"

    # Row 37: Sum of Periods
    val_label_37 = ws.cell(row=37, column=1, value="Validation: Sum of Periods")
    val_label_37.style = "formula_cell"
    val_cell_37 = ws.cell(row=37, column=2, value="=SUM(D3:D34)")
    val_cell_37.style = "tokens"

    # Row 38: Difference
    val_label_38 = ws.cell(row=38, column=1, value="Validation: Difference")
    val_label_38.style = "formula_cell"
    val_cell_38 = ws.cell(row=38, column=2, value="=ABS(B36-B37)")
    val_cell_38.style = "tokens"

    # ------------------------------------------------------------------
    # Column widths
    # ------------------------------------------------------------------
    for col_letter, width in _COL_WIDTHS.items():
        ws.column_dimensions[col_letter].width = width

    # ------------------------------------------------------------------
    # Freeze panes at A3 (headers always visible)
    # ------------------------------------------------------------------
    ws.freeze_panes = "A3"

    # ------------------------------------------------------------------
    # Build emission_meta for downstream tabs and charts
    # ------------------------------------------------------------------
    meta = {
        "sheet_name": "Emission Schedule",
        "header_row": 2,
        "data_start_row": 3,
        "data_end_row": 34,
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
            "eth_benchmark": "J",
        },
        "validation_row": 36,
    }

    # ------------------------------------------------------------------
    # Charts
    # ------------------------------------------------------------------
    _create_emission_decay_chart(ws, meta)
    _create_supply_composition_chart(ws, meta)
    _create_inflation_chart(ws, meta)

    return meta

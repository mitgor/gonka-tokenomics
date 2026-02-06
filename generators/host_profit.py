"""
Gonka Tokenomics - Host Profitability Model Tab

Builds the "Host Profitability" worksheet with 32 data rows (matching the
Emission Schedule period structure) and 13 columns:

  A  Period Label               (cross-ref from Emission Schedule)
  B  Mining GNK/Host            (total mining emission / host count)
  C  Mining Income/Host ($)     (mining GNK * active price)
  D  Fee Income/Host ($)        (fee host share / host count)
  E  Total Gonka Income ($)     (mining + fee income per host)
  F  Electricity Cost ($)       (mid-rate * GPU power * hours * GPUs per host)
  G  Net Income ($)             (total income - electricity)
  H  Traditional Rental ($)     (Lambda rate * hours * GPUs per host)
  I  Gonka vs Traditional ($)   (Gonka income - traditional rental)
  J  Breakeven GNK Price ($)    (price where Gonka matches traditional)
  K  Breakeven Ref Low ($)      (static $0.85 reference)
  L  Breakeven Ref High ($)     (static $3.30 reference)
  M  Churn Risk                 (1 if Gonka < traditional, else 0)

Plus three below-data analysis sections:
  - HOST ROI SENSITIVITY TABLE (rows 37-43): 6 GNK prices x 5 GPU counts
  - ELECTRICITY COST SENSITIVITY (rows 47-50): 3 tiers
  - GPU HARDWARE AMORTIZATION (rows 53-55): months-to-breakeven and ROI

Every formula references the Assumptions tab via param_refs or the Emission
Schedule / Token Price / Fee Transition tabs via their meta dicts, so changes
propagate automatically.

Public API:
    build_host_profit_tab(wb, param_refs, emission_meta, price_meta, fee_meta) -> host_meta dict
"""

from openpyxl.chart import AreaChart, BarChart, LineChart, Reference
from openpyxl.styles import Font
from openpyxl.utils import quote_sheetname

from generators.chart_utils import col_to_num
from generators.styles import TAB_COLOR_CALC


# ---------------------------------------------------------------------------
# Column layout
# ---------------------------------------------------------------------------

_HEADERS = [
    "Period",                           # A
    "Mining GNK/Host",                  # B
    "Mining Income/Host ($)",           # C
    "Fee Income/Host ($)",              # D
    "Total Gonka Income ($)",           # E
    "Electricity Cost ($)",             # F
    "Net Income ($)",                   # G
    "Traditional Rental ($)",           # H
    "Gonka vs Traditional ($)",         # I
    "Breakeven GNK Price ($)",          # J
    "Breakeven Ref Low ($)",            # K
    "Breakeven Ref High ($)",           # L
    "Churn Risk",                       # M
]

_COL_WIDTHS = {
    "A": 12, "B": 18, "C": 18, "D": 18, "E": 20,
    "F": 18, "G": 18, "H": 20, "I": 22, "J": 20,
    "K": 18, "L": 18, "M": 12,
}


# ---------------------------------------------------------------------------
# Below-data sections (private helpers)
# ---------------------------------------------------------------------------

def _build_sensitivity_matrix(ws, param_refs, emission_meta, fee_meta):
    """Build 6x5 host ROI sensitivity table at rows 36-44."""
    # Resolve refs
    gpus_ref = param_refs["Current GPUs"]
    hosts_ref = param_refs["Current Hosts"]
    elec_mid_ref = param_refs["Electricity Cost Mid"]
    gpu_power_ref = param_refs["GPU Power Draw"]

    # Cross-sheet references
    es_sheet = quote_sheetname(emission_meta["sheet_name"])
    ft_sheet = quote_sheetname(fee_meta["sheet_name"])
    es_mining_col = emission_meta["cols"]["mining_emission"]
    ft_host_share_col = fee_meta["cols"]["host_share"]

    # Year 10 rows (last data row = 34)
    yr10_es_row = emission_meta["data_end_row"]
    yr10_ft_row = fee_meta["data_end_row"]

    gpus_per_host = f"({gpus_ref}/{hosts_ref})"

    # Row 36: Section header
    ws.merge_cells("A36:F36")
    header_cell = ws.cell(
        row=36, column=1,
        value="HOST ROI SENSITIVITY (Year 10 Monthly Profit per Host)",
    )
    header_cell.style = "section_header"

    # Row 37: Sub-headers
    sub_headers = [
        "GNK Price \\ GPUs",
        "1,000 GPUs", "5,000 GPUs", "10,000 GPUs",
        "25,000 GPUs", "50,000 GPUs",
    ]
    for col_idx, text in enumerate(sub_headers, start=1):
        cell = ws.cell(row=37, column=col_idx, value=text)
        cell.style = "header"

    # Data: 6 GNK prices x 5 GPU counts
    gnk_prices = [0.50, 1.00, 2.00, 3.00, 5.00, 10.00]
    gpu_counts = [1000, 5000, 10000, 25000, 50000]
    price_labels = ["$0.50", "$1.00", "$2.00", "$3.00", "$5.00", "$10.00"]

    for p_idx, (gnk_price, label) in enumerate(zip(gnk_prices, price_labels)):
        row = 38 + p_idx
        ws.cell(row=row, column=1, value=label)

        for g_idx, gpu_count in enumerate(gpu_counts):
            # mining income: (total_emission_yr10 * 30/365) / gpu_count * gpus_per_host * gnk_price
            # fee income: (fee_host_share_yr10 * 30/365) / (gpu_count / gpus_per_host)
            # electricity: elec_mid * gpu_power * 24 * 30 / 1000 * gpus_per_host
            formula = (
                f"=({es_sheet}!{es_mining_col}{yr10_es_row}*30/365/{gpu_count}*{gpus_per_host}*{gnk_price}"
                f"+{ft_sheet}!{ft_host_share_col}{yr10_ft_row}*30/365/({gpu_count}/{gpus_per_host}))"
                f"-{elec_mid_ref}*{gpu_power_ref}*24*30/1000*{gpus_per_host}"
            )
            cell = ws.cell(row=row, column=2 + g_idx, value=formula)
            cell.style = "currency"

    # Row 44: Annotation
    note_cell = ws.cell(
        row=44, column=1,
        value="* Fee revenue held at base growth scenario. Larger networks may generate proportionally more fees.",
    )
    note_cell.font = Font(name="Calibri", size=10, italic=True)


def _build_electricity_sensitivity(ws, param_refs):
    """Build electricity cost sensitivity section at rows 46-50."""
    gpus_ref = param_refs["Current GPUs"]
    hosts_ref = param_refs["Current Hosts"]
    elec_low_ref = param_refs["Electricity Cost Low"]
    elec_mid_ref = param_refs["Electricity Cost Mid"]
    elec_high_ref = param_refs["Electricity Cost High"]
    gpu_power_ref = param_refs["GPU Power Draw"]

    gpus_per_host = f"({gpus_ref}/{hosts_ref})"

    # Row 46: Section header
    ws.merge_cells("A46:D46")
    header_cell = ws.cell(
        row=46, column=1,
        value="ELECTRICITY COST SENSITIVITY (Year 1 Monthly Average)",
    )
    header_cell.style = "section_header"

    # Row 47: Sub-headers
    sub_headers = ["Electricity Rate", "Monthly Cost/Host", "Yr 1 Monthly Net Profit", "vs Mid-Rate"]
    for col_idx, text in enumerate(sub_headers, start=1):
        cell = ws.cell(row=47, column=col_idx, value=text)
        cell.style = "header"

    # Row 48: $0.05/kWh (Low)
    ws.cell(row=48, column=1, value="$0.05/kWh")
    ws.cell(row=48, column=2,
            value=f"={elec_low_ref}*{gpu_power_ref}*24*30/1000*{gpus_per_host}").style = "currency"
    ws.cell(row=48, column=3, value="=E8-B48").style = "currency"
    ws.cell(row=48, column=4, value="=C48-C49").style = "currency"

    # Row 49: $0.08/kWh (Mid)
    ws.cell(row=49, column=1, value="$0.08/kWh")
    ws.cell(row=49, column=2,
            value=f"={elec_mid_ref}*{gpu_power_ref}*24*30/1000*{gpus_per_host}").style = "currency"
    ws.cell(row=49, column=3, value="=E8-B49").style = "currency"
    ws.cell(row=49, column=4, value=0).style = "currency"

    # Row 50: $0.12/kWh (High)
    ws.cell(row=50, column=1, value="$0.12/kWh")
    ws.cell(row=50, column=2,
            value=f"={elec_high_ref}*{gpu_power_ref}*24*30/1000*{gpus_per_host}").style = "currency"
    ws.cell(row=50, column=3, value="=E8-B50").style = "currency"
    ws.cell(row=50, column=4, value="=C50-C49").style = "currency"


def _build_gpu_amortization(ws, param_refs):
    """Build GPU hardware amortization section at rows 52-55."""
    hw_low_ref = param_refs["H100 Hardware Cost Low"]
    hw_high_ref = param_refs["H100 Hardware Cost High"]

    # Row 52: Section header
    ws.merge_cells("A52:E52")
    header_cell = ws.cell(
        row=52, column=1,
        value="GPU HARDWARE AMORTIZATION",
    )
    header_cell.style = "section_header"

    # Row 53: Sub-headers
    sub_headers = ["Hardware Cost", "Monthly Net Income", "Months to Breakeven", "3-Year ROI", "5-Year ROI"]
    for col_idx, text in enumerate(sub_headers, start=1):
        cell = ws.cell(row=53, column=col_idx, value=text)
        cell.style = "header"

    # Row 54: H100 Low ($25K)
    ws.cell(row=54, column=1, value="H100 Low ($25K)")
    ws.cell(row=54, column=2, value="=G8").style = "currency"
    ws.cell(row=54, column=3,
            value=f"=IFERROR({hw_low_ref}/B54,999)").style = "number"
    ws.cell(row=54, column=4,
            value=f"=IFERROR((B54*36-{hw_low_ref})/{hw_low_ref},0)").style = "percent"
    ws.cell(row=54, column=5,
            value=f"=IFERROR((B54*60-{hw_low_ref})/{hw_low_ref},0)").style = "percent"

    # Row 55: H100 High ($40K)
    ws.cell(row=55, column=1, value="H100 High ($40K)")
    ws.cell(row=55, column=2, value="=G8").style = "currency"
    ws.cell(row=55, column=3,
            value=f"=IFERROR({hw_high_ref}/B55,999)").style = "number"
    ws.cell(row=55, column=4,
            value=f"=IFERROR((B55*36-{hw_high_ref})/{hw_high_ref},0)").style = "percent"
    ws.cell(row=55, column=5,
            value=f"=IFERROR((B55*60-{hw_high_ref})/{hw_high_ref},0)").style = "percent"


# ---------------------------------------------------------------------------
# Charts
# ---------------------------------------------------------------------------

def _create_income_composition_chart(ws, meta):
    """Stacked area chart: Mining Income declining, Fee Income growing."""
    chart = AreaChart()
    chart.grouping = "stacked"
    chart.title = "Host Income Composition (Mining + Fee)"
    chart.y_axis.title = "USD per Host"
    chart.x_axis.title = "Period"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # Series 1: Mining Income (column C)
    mining_col = col_to_num(meta["cols"]["mining_income"])
    data1 = Reference(ws, min_col=mining_col, min_row=meta["header_row"],
                      max_row=meta["data_end_row"])
    chart.add_data(data1, titles_from_data=True)

    # Series 2: Fee Income (column D)
    fee_col = col_to_num(meta["cols"]["fee_income"])
    data2 = Reference(ws, min_col=fee_col, min_row=meta["header_row"],
                      max_row=meta["data_end_row"])
    chart.add_data(data2, titles_from_data=True)

    # Categories: Period labels (column A)
    cats = Reference(ws, min_col=1, min_row=meta["data_start_row"],
                     max_row=meta["data_end_row"])
    chart.set_categories(cats)

    ws.add_chart(chart, "O1")


def _create_comparison_chart(ws, meta):
    """Clustered bar chart: Gonka total income vs Lambda traditional rental."""
    chart = BarChart()
    chart.type = "col"
    chart.grouping = "clustered"
    chart.title = "Gonka Income vs Traditional GPU Rental (Lambda $2.49/hr, CoreWeave $2.06/hr)"
    chart.y_axis.title = "USD per Host"
    chart.x_axis.title = "Period"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # Series 1: Total Gonka Income (column E)
    gonka_col = col_to_num(meta["cols"]["total_gonka_income"])
    data1 = Reference(ws, min_col=gonka_col, min_row=meta["header_row"],
                      max_row=meta["data_end_row"])
    chart.add_data(data1, titles_from_data=True)

    # Series 2: Traditional Rental Income (column H)
    trad_col = col_to_num(meta["cols"]["traditional_rental"])
    data2 = Reference(ws, min_col=trad_col, min_row=meta["header_row"],
                      max_row=meta["data_end_row"])
    chart.add_data(data2, titles_from_data=True)

    # Categories: Period labels (column A)
    cats = Reference(ws, min_col=1, min_row=meta["data_start_row"],
                     max_row=meta["data_end_row"])
    chart.set_categories(cats)

    ws.add_chart(chart, "O17")


def _create_breakeven_chart(ws, meta):
    """Line chart: Breakeven GNK price trend with $0.85-$3.30 reference range."""
    chart = LineChart()
    chart.title = "Breakeven GNK Price for Host Profitability"
    chart.y_axis.title = "GNK Price (USD)"
    chart.x_axis.title = "Period"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # Series 1: Breakeven GNK Price (column J) - primary line
    be_col = col_to_num(meta["cols"]["breakeven_gnk"])
    data1 = Reference(ws, min_col=be_col, min_row=meta["header_row"],
                      max_row=meta["data_end_row"])
    chart.add_data(data1, titles_from_data=True)

    # Series 2: Reference Low $0.85 (column K) - flat reference line
    ref_low_col = col_to_num(meta["cols"]["breakeven_ref_low"])
    data2 = Reference(ws, min_col=ref_low_col, min_row=meta["header_row"],
                      max_row=meta["data_end_row"])
    chart.add_data(data2, titles_from_data=True)

    # Series 3: Reference High $3.30 (column L) - flat reference line
    ref_high_col = col_to_num(meta["cols"]["breakeven_ref_high"])
    data3 = Reference(ws, min_col=ref_high_col, min_row=meta["header_row"],
                      max_row=meta["data_end_row"])
    chart.add_data(data3, titles_from_data=True)

    # Categories: Period labels (column A)
    cats = Reference(ws, min_col=1, min_row=meta["data_start_row"],
                     max_row=meta["data_end_row"])
    chart.set_categories(cats)

    # Style reference lines as dashed
    s2 = chart.series[1]
    s2.graphicalProperties.line.dashStyle = "dash"
    s3 = chart.series[2]
    s3.graphicalProperties.line.dashStyle = "dash"

    # Cap Y-axis at a reasonable max to avoid the 99999 sentinel distorting the chart.
    chart.y_axis.scaling.max = 15
    chart.y_axis.scaling.min = 0

    ws.add_chart(chart, "O33")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def build_host_profit_tab(wb, param_refs, emission_meta, price_meta, fee_meta):
    """Create the 'Host Profitability' worksheet and populate formulas.

    Args:
        wb: An openpyxl Workbook with styles already registered.
        param_refs: dict mapping parameter names to "Assumptions!$B$N".
        emission_meta: dict from build_emission_tab() with sheet coordinates.
        price_meta: dict from build_token_price_tab() with sheet coordinates.
        fee_meta: dict from build_fee_transition_tab() with sheet coordinates.

    Returns:
        dict: host_meta with sheet coordinates for downstream tabs/charts.
    """
    ws = wb.create_sheet(title="Host Profitability")
    ws.sheet_properties.tabColor = TAB_COLOR_CALC

    # ------------------------------------------------------------------
    # Resolve param_refs
    # ------------------------------------------------------------------
    hosts_ref = param_refs["Current Hosts"]
    gpus_ref = param_refs["Current GPUs"]
    elec_mid_ref = param_refs["Electricity Cost Mid"]
    gpu_power_ref = param_refs["GPU Power Draw"]
    lambda_ref = param_refs["Traditional Rental Rate (Lambda)"]

    # ------------------------------------------------------------------
    # Cross-sheet references
    # ------------------------------------------------------------------
    es_sheet = quote_sheetname(emission_meta["sheet_name"])
    tp_sheet = quote_sheetname(price_meta["sheet_name"])
    ft_sheet = quote_sheetname(fee_meta["sheet_name"])

    es_mining_col = emission_meta["cols"]["mining_emission"]    # "D"
    es_period_col = emission_meta["cols"]["period_label"]       # "A"
    tp_active_col = price_meta["cols"]["active_price"]          # "F"
    ft_host_share_col = fee_meta["cols"]["host_share"]          # "K"

    # ------------------------------------------------------------------
    # Row 1: Merged title
    # ------------------------------------------------------------------
    ws.merge_cells("A1:M1")
    title_cell = ws.cell(row=1, column=1, value="HOST PROFITABILITY MODEL")
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
    data_start_row = 3
    num_periods = 32

    for i in range(num_periods):
        row = data_start_row + i
        es_row = emission_meta["data_start_row"] + i
        tp_row = price_meta["data_start_row"] + i
        ft_row = fee_meta["data_start_row"] + i

        # Determine days per period
        days = 30 if i < 24 else 365

        # A: Period Label (cross-ref from Emission Schedule)
        a_cell = ws.cell(
            row=row, column=1,
            value=f"={es_sheet}!{es_period_col}{es_row}",
        )
        a_cell.style = "crossref_cell"

        # B: Mining GNK per Host = total mining emission / host count
        b_cell = ws.cell(
            row=row, column=2,
            value=f"={es_sheet}!{es_mining_col}{es_row}/{hosts_ref}",
        )
        b_cell.style = "tokens"

        # C: Mining Income per Host ($) = mining GNK * active price
        c_cell = ws.cell(
            row=row, column=3,
            value=f"=B{row}*{tp_sheet}!{tp_active_col}{tp_row}",
        )
        c_cell.style = "currency"

        # D: Fee Income per Host ($) = total host share / host count
        d_cell = ws.cell(
            row=row, column=4,
            value=f"={ft_sheet}!{ft_host_share_col}{ft_row}/{hosts_ref}",
        )
        d_cell.style = "currency"

        # E: Total Gonka Income ($) = mining + fee income
        e_cell = ws.cell(
            row=row, column=5,
            value=f"=C{row}+D{row}",
        )
        e_cell.style = "currency"

        # F: Electricity Cost ($) = rate * power * 24hrs * days / 1000 * GPUs per host
        f_cell = ws.cell(
            row=row, column=6,
            value=f"={elec_mid_ref}*{gpu_power_ref}*24*{days}/1000*({gpus_ref}/{hosts_ref})",
        )
        f_cell.style = "currency"

        # G: Net Income ($) = total income - electricity
        g_cell = ws.cell(
            row=row, column=7,
            value=f"=E{row}-F{row}",
        )
        g_cell.style = "currency"

        # H: Traditional Rental ($) = Lambda rate * 24hrs * days * GPUs per host
        h_cell = ws.cell(
            row=row, column=8,
            value=f"={lambda_ref}*24*{days}*({gpus_ref}/{hosts_ref})",
        )
        h_cell.style = "currency"

        # I: Gonka vs Traditional ($) = Gonka income - traditional rental
        i_cell = ws.cell(
            row=row, column=9,
            value=f"=E{row}-H{row}",
        )
        i_cell.style = "currency"

        # J: Breakeven GNK Price ($) = MAX(0, (traditional - fee) / mining_GNK)
        j_cell = ws.cell(
            row=row, column=10,
            value=f"=IFERROR(MAX(0,(H{row}-D{row})/B{row}),99999)",
        )
        j_cell.style = "currency"

        # K: Breakeven Reference Low ($) = static $0.85
        k_cell = ws.cell(row=row, column=11, value=0.85)
        k_cell.style = "currency"

        # L: Breakeven Reference High ($) = static $3.30
        l_cell = ws.cell(row=row, column=12, value=3.30)
        l_cell.style = "currency"

        # M: Churn Risk Flag = 1 if Gonka income < traditional rental, else 0
        m_cell = ws.cell(
            row=row, column=13,
            value=f"=IF(E{row}<H{row},1,0)",
        )
        m_cell.style = "integer"

    # ------------------------------------------------------------------
    # Below-data sections
    # ------------------------------------------------------------------
    _build_sensitivity_matrix(ws, param_refs, emission_meta, fee_meta)
    _build_electricity_sensitivity(ws, param_refs)
    _build_gpu_amortization(ws, param_refs)

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
    # Build host_meta for downstream tabs and charts
    # ------------------------------------------------------------------
    host_meta = {
        "sheet_name": "Host Profitability",
        "header_row": 2,
        "data_start_row": 3,
        "data_end_row": 34,
        "cols": {
            "period_label": "A",
            "mining_gnk_per_host": "B",
            "mining_income": "C",
            "fee_income": "D",
            "total_gonka_income": "E",
            "electricity_cost": "F",
            "net_income": "G",
            "traditional_rental": "H",
            "gonka_vs_traditional": "I",
            "breakeven_gnk": "J",
            "breakeven_ref_low": "K",
            "breakeven_ref_high": "L",
            "churn_risk_flag": "M",
        },
        "sensitivity_start_row": 37,
        "sensitivity_end_row": 43,
        "electricity_section_start_row": 47,
        "gpu_amortization_start_row": 53,
    }

    # ------------------------------------------------------------------
    # Charts
    # ------------------------------------------------------------------
    _create_income_composition_chart(ws, host_meta)
    _create_comparison_chart(ws, host_meta)
    _create_breakeven_chart(ws, host_meta)

    return host_meta

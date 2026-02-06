"""
Gonka Tokenomics - Dashboard Tab (Executive Summary)

Builds the "Dashboard" worksheet as the executive summary of the entire
tokenomics model.  Leadership opens this tab first to see health indicators
across all dimensions.  It pulls live data from every model tab via
cross-sheet formulas so changes to assumptions cascade through instantly.

Sections:
  1. Title row with merged header and "<< Documentation" back-link at F1
  2. Key Performance Indicators (8 KPIs at Year 10, all cross-sheet formulas)
  3. Scenario Comparison Matrix (6 metrics x 3 scenarios with color coding)
  4. Three summary charts:
     - Year 10 GNK Price by Scenario (bar chart)
     - Host Breakeven GNK Price with Thresholds (line chart with $0.85/$3.30)
     - Net Treasury Value 10-Year Projection (line chart)

Every value on this tab is a formula referencing other model tabs.
No hardcoded numeric values (REQ-M5-01).

Public API:
    build_dashboard_tab(wb, param_refs, emission_meta, price_meta, fee_meta,
                        host_meta, treasury_meta) -> dashboard_meta dict
"""

from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Font, Alignment
from openpyxl.utils import quote_sheetname

from generators.chart_utils import col_to_num
from generators.styles import TAB_COLOR_DASHBOARD


def build_dashboard_tab(wb, param_refs, emission_meta, price_meta,
                        fee_meta, host_meta, treasury_meta):
    """Populate the existing 'Dashboard' worksheet with KPIs, matrix, and charts.

    The worksheet is already created as a placeholder by Plan 01.  This
    function fills it with cross-model KPIs, a scenario comparison matrix,
    and three summary charts.

    Args:
        wb: An openpyxl Workbook with styles already registered.
        param_refs: dict mapping parameter names to "Assumptions!$B$N".
        emission_meta: dict from build_emission_tab().
        price_meta: dict from build_token_price_tab().
        fee_meta: dict from build_fee_transition_tab().
        host_meta: dict from build_host_profit_tab().
        treasury_meta: dict from build_treasury_tab().

    Returns:
        dict: dashboard_meta with section coordinates.
    """
    ws = wb["Dashboard"]

    # Verify/set tab color
    ws.sheet_properties.tabColor = TAB_COLOR_DASHBOARD

    # ------------------------------------------------------------------
    # Quoted sheet names for cross-sheet formulas
    # ------------------------------------------------------------------
    es = quote_sheetname(emission_meta["sheet_name"])    # "'Emission Schedule'"
    tp = quote_sheetname(price_meta["sheet_name"])       # "'Token Price'"
    ft = quote_sheetname(fee_meta["sheet_name"])         # "'Fee Transition'"
    hp = quote_sheetname(host_meta["sheet_name"])        # "'Host Profitability'"
    tr = quote_sheetname(treasury_meta["sheet_name"])    # "'Treasury & POL'"
    yr10 = 34  # Last data row (Year 10) across all model tabs

    # ------------------------------------------------------------------
    # Column widths
    # ------------------------------------------------------------------
    ws.column_dimensions["A"].width = 40
    ws.column_dimensions["B"].width = 18
    ws.column_dimensions["C"].width = 18
    ws.column_dimensions["D"].width = 18
    ws.column_dimensions["E"].width = 18

    # ==================================================================
    # Section 1: Title and Back-to-Documentation link (row 1)
    # ==================================================================
    ws.merge_cells("A1:E1")
    title_cell = ws.cell(row=1, column=1,
                         value="DASHBOARD -- CROSS-MODEL SUMMARY")
    title_cell.style = "section_header"

    # "<< Documentation" back-link at F1 (Plan 01 excluded Dashboard from
    # _add_back_to_doc_links so we handle it here)
    link_font = Font(name="Calibri", size=11, color="0563C1",
                     underline="single")
    cell_link = ws.cell(row=1, column=6)
    cell_link.value = "<< Documentation"
    cell_link.hyperlink = "#Documentation!A1"
    cell_link.font = link_font

    # ==================================================================
    # Section 2: Key Performance Indicators (rows 3-12)
    # ==================================================================
    ws.cell(row=3, column=1,
            value="KEY PERFORMANCE INDICATORS (Year 10, Active Scenario)"
            ).style = "section_header"

    # Row 4: column headers
    for col_idx, text in enumerate(["Metric", "Value", "Unit"], start=1):
        ws.cell(row=4, column=col_idx, value=text).style = "header"

    # KPI definitions: (row, label, formula, unit, style_name)
    kpis = [
        (5,  "Year 10 Circulating Supply",
         f"={es}!H{yr10}", "GNK", "tokens"),
        (6,  "Year 10 Active GNK Price",
         f"={tp}!F{yr10}", "USD", "currency"),
        (7,  "Year 10 Circ. Market Cap",
         f"={tp}!I{yr10}", "USD", "currency"),
        (8,  "Year 10 Fee/Emission Ratio (Base)",
         f"={ft}!I{yr10}", "ratio", "number"),
        (9,  "Year 10 Host Net Monthly Income",
         f"={hp}!G{yr10}", "USD", "currency"),
        (10, "Year 10 Net Treasury Value",
         f"={tr}!N{yr10}", "USD", "currency"),
        (11, "Cumulative Buyback Burn (% Supply)",
         f"={tr}!H{yr10}", "%", "percent"),
        (12, "Host Churn Risk Periods (Total)",
         f"=COUNTIF({hp}!M3:{hp}!M{yr10},1)", "periods", "integer"),
    ]

    for row, label, formula, unit, style_name in kpis:
        a_cell = ws.cell(row=row, column=1, value=label)
        a_cell.style = "crossref_cell"
        b_cell = ws.cell(row=row, column=2, value=formula)
        b_cell.style = style_name
        ws.cell(row=row, column=3, value=unit)

    # ==================================================================
    # Section 3: Scenario Comparison Matrix (rows 14-22)
    # ==================================================================
    ws.cell(row=14, column=1,
            value="SCENARIO COMPARISON (Year 10)").style = "section_header"

    # Row 15: Headers
    for col_idx, text in enumerate(
            ["Metric", "Conservative", "Base", "Aggressive"], start=1):
        ws.cell(row=15, column=col_idx, value=text).style = "header"

    # Matrix definitions: (row, label, cons_formula, base_formula, agg_formula, style)
    matrix_rows = [
        (16, "GNK Price ($)",
         f"={tp}!B{yr10}", f"={tp}!C{yr10}", f"={tp}!D{yr10}",
         "currency"),
        (17, "Circ. Market Cap ($)",
         f"={es}!H{yr10}*{tp}!B{yr10}",
         f"={es}!H{yr10}*{tp}!C{yr10}",
         f"={es}!H{yr10}*{tp}!D{yr10}",
         "currency"),
        (18, "Fee/Emission Ratio",
         f"={ft}!H{yr10}", f"={ft}!I{yr10}", f"={ft}!J{yr10}",
         "number"),
        (19, "Host Net Income ($)",
         f"={hp}!B{yr10}*{tp}!B{yr10}+{hp}!D{yr10}-{hp}!F{yr10}",
         f"={hp}!G{yr10}",
         f"={hp}!B{yr10}*{tp}!D{yr10}+{hp}!D{yr10}-{hp}!F{yr10}",
         "currency"),
        (20, "Net Treasury ($)",
         f"={tr}!N{yr10}*{tp}!B{yr10}/{tp}!F{yr10}",
         f"={tr}!N{yr10}",
         f"={tr}!N{yr10}*{tp}!D{yr10}/{tp}!F{yr10}",
         "currency"),
        (21, "Cumulative Burn (%)",
         f"={tr}!H{yr10}", f"={tr}!H{yr10}", f"={tr}!H{yr10}",
         "percent"),
    ]

    for row, label, cons, base, agg, style_name in matrix_rows:
        ws.cell(row=row, column=1, value=label).style = "crossref_cell"
        ws.cell(row=row, column=2, value=cons).style = style_name
        ws.cell(row=row, column=3, value=base).style = style_name
        ws.cell(row=row, column=4, value=agg).style = style_name

    # Row 22: Annotation
    note_cell = ws.cell(
        row=22, column=1,
        value="* Scenario values approximate -- Host Income and Treasury "
              "scale linearly with price assumption",
    )
    note_cell.font = Font(name="Calibri", size=11, italic=True)

    # Conditional formatting: per-row ColorScaleRule (red/yellow/green)
    for row in range(16, 22):
        rule = ColorScaleRule(
            start_type="min", start_color="F8696B",       # red
            mid_type="percentile", mid_value=50,
            mid_color="FFEB84",                            # yellow
            end_type="max", end_color="63BE7B",            # green
        )
        ws.conditional_formatting.add(f"B{row}:D{row}", rule)

    # ==================================================================
    # Section 4: Charts
    # ==================================================================

    # ---- Chart 1: KPI Summary Bar Chart (anchor F3) --------------------
    _create_price_scenario_chart(ws)

    # ---- Chart 2: Host Breakeven Timeline (anchor F19) -----------------
    _create_breakeven_timeline_chart(ws, wb, host_meta)

    # ---- Chart 3: Treasury Health Timeline (anchor F35) ----------------
    _create_treasury_timeline_chart(ws, wb, treasury_meta)

    # ------------------------------------------------------------------
    # Return dashboard_meta
    # ------------------------------------------------------------------
    return {
        "sheet_name": "Dashboard",
        "kpi_start_row": 5,
        "kpi_end_row": 12,
        "matrix_start_row": 15,
        "matrix_end_row": 21,
    }


# ---------------------------------------------------------------------------
# Chart builders (private)
# ---------------------------------------------------------------------------

def _create_price_scenario_chart(ws):
    """Bar chart: Year 10 GNK Price by Scenario at F3."""
    chart = BarChart()
    chart.type = "col"
    chart.grouping = "clustered"
    chart.title = "Year 10 GNK Price by Scenario"
    chart.y_axis.title = "GNK Price (USD)"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # Data: row 16, columns B:D (three scenario prices)
    data = Reference(ws, min_col=2, min_row=15, max_col=4, max_row=16)
    chart.add_data(data, titles_from_data=True)

    # Categories: row 15 labels not needed for bar; the series names serve
    cats = Reference(ws, min_col=2, min_row=15, max_col=4, max_row=15)
    chart.set_categories(cats)

    ws.add_chart(chart, "F3")


def _create_breakeven_timeline_chart(ws, wb, host_meta):
    """Line chart: Breakeven GNK price with $0.85/$3.30 dashed thresholds at F19.

    CRITICAL: Data references point to the Host Profitability worksheet,
    NOT to the Dashboard.  The chart is added to the Dashboard ws.
    """
    ws_host = wb["Host Profitability"]

    chart = LineChart()
    chart.title = "Host Breakeven GNK Price with Thresholds"
    chart.y_axis.title = "GNK Price ($)"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # Series 1: Breakeven GNK Price (column J)
    be_col = col_to_num("J")
    data1 = Reference(ws_host, min_col=be_col,
                      min_row=host_meta["header_row"],
                      max_row=host_meta["data_end_row"])
    chart.add_data(data1, titles_from_data=True)

    # Series 2: $0.85 reference (column K)
    ref_low_col = col_to_num("K")
    data2 = Reference(ws_host, min_col=ref_low_col,
                      min_row=host_meta["header_row"],
                      max_row=host_meta["data_end_row"])
    chart.add_data(data2, titles_from_data=True)

    # Series 3: $3.30 reference (column L)
    ref_high_col = col_to_num("L")
    data3 = Reference(ws_host, min_col=ref_high_col,
                      min_row=host_meta["header_row"],
                      max_row=host_meta["data_end_row"])
    chart.add_data(data3, titles_from_data=True)

    # Categories: Period labels (column A)
    cats = Reference(ws_host, min_col=1,
                     min_row=host_meta["data_start_row"],
                     max_row=host_meta["data_end_row"])
    chart.set_categories(cats)

    # Dashed reference lines (REQ-D05)
    s2 = chart.series[1]
    s2.graphicalProperties.line.dashStyle = "dash"
    s3 = chart.series[2]
    s3.graphicalProperties.line.dashStyle = "dash"

    # Cap Y-axis at $15 (same pattern as host_profit.py)
    chart.y_axis.scaling.max = 15
    chart.y_axis.scaling.min = 0

    ws.add_chart(chart, "F19")


def _create_treasury_timeline_chart(ws, wb, treasury_meta):
    """Line chart: Net Treasury Value over 10 years at F35.

    Data references point to the Treasury & POL worksheet.
    """
    ws_treasury = wb["Treasury & POL"]

    chart = LineChart()
    chart.title = "Net Treasury Value (10-Year Projection)"
    chart.y_axis.title = "USD ($)"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # Series: Net Treasury USD (column N)
    net_col = col_to_num("N")
    data = Reference(ws_treasury, min_col=net_col,
                     min_row=treasury_meta["header_row"],
                     max_row=treasury_meta["data_end_row"])
    chart.add_data(data, titles_from_data=True)

    # Categories: Period labels (column A)
    cats = Reference(ws_treasury, min_col=1,
                     min_row=treasury_meta["data_start_row"],
                     max_row=treasury_meta["data_end_row"])
    chart.set_categories(cats)

    ws.add_chart(chart, "F35")

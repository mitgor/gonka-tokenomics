"""
Gonka Tokenomics - Fee Transition Crossover Model Tab

Builds the "Fee Transition" worksheet with 32 data rows (matching the Emission
Schedule period structure) and 14 columns:

  A  Period Label              (cross-ref from Emission Schedule)
  B  Developer Count           (compound growth from base developers)
  C  Fee Revenue - Low ($)     (low growth rate projection)
  D  Fee Revenue - Base ($)    (moderate growth rate projection)
  E  Fee Revenue - High ($)    (high growth rate projection)
  F  Emission Value ($)        (mining emission * active price)
  G  Effective Emission ($)    (tail-emission-aware emission value)
  H  Crossover Ratio (Low)     (fee revenue low / effective emission)
  I  Crossover Ratio (Base)    (fee revenue base / effective emission)
  J  Crossover Ratio (High)    (fee revenue high / effective emission)
  K  Host Share ($)             (70% of base fee revenue)
  L  AI Fund Share ($)          (20% of base fee revenue)
  M  Buyback Share ($)          (5% of base fee revenue)
  N  Yield Pool Share ($)       (5% of base fee revenue)

Plus two summary matrices:
  - 9-cell crossover RATIO matrix at Year 10 (rows 37-40)
  - Crossover YEAR matrix (rows 43-46) using INDEX/MATCH

Every formula references the Assumptions tab via param_refs or the Emission
Schedule / Token Price tabs via their meta dicts, so changes propagate
automatically.

Public API:
    build_fee_transition_tab(wb, param_refs, emission_meta, price_meta) -> fee_meta dict
"""

from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.utils import quote_sheetname

from generators.chart_utils import col_to_num
from generators.styles import TAB_COLOR_CALC


# ---------------------------------------------------------------------------
# Column layout
# ---------------------------------------------------------------------------

_HEADERS = [
    "Period",                       # A
    "Developer Count",              # B
    "Fee Revenue - Low ($)",        # C
    "Fee Revenue - Base ($)",       # D
    "Fee Revenue - High ($)",       # E
    "Emission Value ($)",           # F
    "Effective Emission ($)",       # G
    "Crossover Ratio (Low)",        # H
    "Crossover Ratio (Base)",       # I
    "Crossover Ratio (High)",       # J
    "Host Share ($)",               # K
    "AI Fund Share ($)",            # L
    "Buyback Share ($)",            # M
    "Yield Pool Share ($)",         # N
]

_COL_WIDTHS = {
    "A": 12, "B": 16, "C": 20, "D": 20, "E": 20,
    "F": 18, "G": 20, "H": 18, "I": 18, "J": 18,
    "K": 16, "L": 16, "M": 16, "N": 16,
}


# ---------------------------------------------------------------------------
# Charts
# ---------------------------------------------------------------------------

def _create_waterfall_chart(ws, meta):
    """Add a stacked bar chart showing the 70/20/5/5 revenue split."""
    chart = BarChart()
    chart.type = "col"
    chart.grouping = "stacked"
    chart.overlap = 100  # CRITICAL: without this, bars render side-by-side
    chart.title = "Fee Revenue Split (Base Growth)"
    chart.y_axis.title = "USD"
    chart.x_axis.title = "Period"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # 4 series: Host Share (K), AI Fund (L), Buyback (M), Yield Pool (N)
    for col_key in ("host_share", "ai_fund_share", "buyback_share", "yield_share"):
        col_num = col_to_num(meta["cols"][col_key])
        data = Reference(ws,
                         min_col=col_num, min_row=meta["header_row"],
                         max_row=meta["data_end_row"])
        chart.add_data(data, titles_from_data=True)

    # Categories: period labels (column A)
    a_col = col_to_num(meta["cols"]["period_label"])
    cats = Reference(ws,
                     min_col=a_col, min_row=meta["data_start_row"],
                     max_row=meta["data_end_row"])
    chart.set_categories(cats)

    ws.add_chart(chart, "P1")


def _create_crossover_timeline_chart(ws, meta):
    """Add a line chart showing crossover ratios over time for 3 growth scenarios."""
    chart = LineChart()
    chart.title = "Fee/Emission Crossover Ratio Over Time"
    chart.y_axis.title = "Ratio (Fee Revenue / Emission Value)"
    chart.x_axis.title = "Period"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # 3 series: Low (H), Base (I), High (J)
    for col_key in ("crossover_ratio_low", "crossover_ratio_base", "crossover_ratio_high"):
        col_num = col_to_num(meta["cols"][col_key])
        data = Reference(ws,
                         min_col=col_num, min_row=meta["header_row"],
                         max_row=meta["data_end_row"])
        chart.add_data(data, titles_from_data=True)

    # Categories: period labels
    a_col = col_to_num(meta["cols"]["period_label"])
    cats = Reference(ws,
                     min_col=a_col, min_row=meta["data_start_row"],
                     max_row=meta["data_end_row"])
    chart.set_categories(cats)

    # Line widths consistent with Phase 2-3 (25000 EMUs)
    for s in chart.series:
        s.graphicalProperties.line.width = 25000

    ws.add_chart(chart, "P17")


def _create_fee_vs_emission_chart(ws, meta):
    """Add a line chart comparing base fee revenue against effective emission value."""
    chart = LineChart()
    chart.title = "Fee Revenue vs Emission Value (Base Growth)"
    chart.y_axis.title = "USD"
    chart.x_axis.title = "Period"
    chart.style = 13
    chart.width = 20
    chart.height = 12

    # Series 1: Fee Revenue - Base Growth (D)
    d_col = col_to_num(meta["cols"]["fee_rev_base"])
    data1 = Reference(ws,
                      min_col=d_col, min_row=meta["header_row"],
                      max_row=meta["data_end_row"])
    chart.add_data(data1, titles_from_data=True)

    # Series 2: Effective Emission Value (G)
    g_col = col_to_num(meta["cols"]["effective_emission_value"])
    data2 = Reference(ws,
                      min_col=g_col, min_row=meta["header_row"],
                      max_row=meta["data_end_row"])
    chart.add_data(data2, titles_from_data=True)

    # Categories: period labels
    a_col = col_to_num(meta["cols"]["period_label"])
    cats = Reference(ws,
                     min_col=a_col, min_row=meta["data_start_row"],
                     max_row=meta["data_end_row"])
    chart.set_categories(cats)

    for s in chart.series:
        s.graphicalProperties.line.width = 25000

    ws.add_chart(chart, "P33")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def build_fee_transition_tab(wb, param_refs, emission_meta, price_meta):
    """Create the 'Fee Transition' worksheet and populate formulas.

    Args:
        wb: An openpyxl Workbook with styles already registered.
        param_refs: dict mapping parameter names to "Assumptions!$B$N".
        emission_meta: dict from build_emission_tab() with sheet coordinates.
        price_meta: dict from build_token_price_tab() with sheet coordinates.

    Returns:
        dict: fee_meta with sheet coordinates for downstream tabs/charts.
    """
    ws = wb.create_sheet(title="Fee Transition")
    ws.sheet_properties.tabColor = TAB_COLOR_CALC

    # ------------------------------------------------------------------
    # Resolve param_refs
    # ------------------------------------------------------------------
    base_devs_ref = param_refs["Base Active Developers"]
    low_growth_ref = param_refs["Conservative Dev Growth"]
    mod_growth_ref = param_refs["Moderate Dev Growth"]
    high_growth_ref = param_refs["Aggressive Dev Growth"]
    rev_per_dev_ref = param_refs["Revenue Per Developer (Annual)"]
    host_share_ref = param_refs["Host Share"]
    ai_fund_ref = param_refs["AI Training Fund"]
    buyback_ref = param_refs["Buyback-Burn"]
    yield_ref = param_refs["veGNK Yield Pool"]
    tail_toggle_ref = param_refs["Tail Emission Toggle"]
    tail_rate_ref = param_refs["Tail Emission Rate (Contingency)"]

    # ------------------------------------------------------------------
    # Cross-sheet references
    # ------------------------------------------------------------------
    es_sheet = quote_sheetname(emission_meta["sheet_name"])
    tp_sheet = quote_sheetname(price_meta["sheet_name"])
    es_mining_col = emission_meta["cols"]["mining_emission"]    # "D"
    es_start_col = emission_meta["cols"]["start_epoch"]         # "B"
    es_end_col = emission_meta["cols"]["end_epoch"]             # "C"
    es_period_col = emission_meta["cols"]["period_label"]       # "A"
    tp_cons_col = price_meta["cols"]["conservative_price"]      # "B"
    tp_mod_col = price_meta["cols"]["moderate_price"]           # "C"
    tp_agg_col = price_meta["cols"]["aggressive_price"]         # "D"
    tp_active_col = price_meta["cols"]["active_price"]          # "F"

    # ------------------------------------------------------------------
    # Row 1: Merged title
    # ------------------------------------------------------------------
    ws.merge_cells("A1:N1")
    title_cell = ws.cell(row=1, column=1, value="FEE TRANSITION CROSSOVER MODEL")
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

        # Determine days per period
        days = 30 if i < 24 else 365

        # A: Period Label (cross-ref from Emission Schedule)
        a_cell = ws.cell(
            row=row, column=1,
            value=f"={es_sheet}!{es_period_col}{es_row}",
        )
        a_cell.style = "crossref_cell"

        # B: Developer Count (compound growth from base, moderate rate)
        b_cell = ws.cell(
            row=row, column=2,
            value=(
                f"={base_devs_ref}*(1+{mod_growth_ref})"
                f"^({es_sheet}!{es_start_col}{es_row}/365)"
            ),
        )
        b_cell.style = "integer"

        # C: Fee Revenue - Low Growth
        c_cell = ws.cell(
            row=row, column=3,
            value=(
                f"={base_devs_ref}*(1+{low_growth_ref})"
                f"^({es_sheet}!{es_start_col}{es_row}/365)"
                f"*{rev_per_dev_ref}*{days}/365"
            ),
        )
        c_cell.style = "currency"

        # D: Fee Revenue - Base Growth
        d_cell = ws.cell(
            row=row, column=4,
            value=(
                f"={base_devs_ref}*(1+{mod_growth_ref})"
                f"^({es_sheet}!{es_start_col}{es_row}/365)"
                f"*{rev_per_dev_ref}*{days}/365"
            ),
        )
        d_cell.style = "currency"

        # E: Fee Revenue - High Growth
        e_cell = ws.cell(
            row=row, column=5,
            value=(
                f"={base_devs_ref}*(1+{high_growth_ref})"
                f"^({es_sheet}!{es_start_col}{es_row}/365)"
                f"*{rev_per_dev_ref}*{days}/365"
            ),
        )
        e_cell.style = "currency"

        # F: Emission Value ($) = mining_emission_GNK * active_price
        f_cell = ws.cell(
            row=row, column=6,
            value=(
                f"={es_sheet}!{es_mining_col}{es_row}"
                f"*{tp_sheet}!{tp_active_col}{es_row}"
            ),
        )
        f_cell.style = "currency"

        # G: Effective Emission ($) - tail emission aware
        g_cell = ws.cell(
            row=row, column=7,
            value=(
                f'=IF({tail_toggle_ref}="ON",'
                f"MAX({es_sheet}!{es_mining_col}{es_row},{tail_rate_ref}*{days})"
                f"*{tp_sheet}!{tp_active_col}{es_row},"
                f"F{row})"
            ),
        )
        g_cell.style = "currency"

        # H: Crossover Ratio (Low)
        h_cell = ws.cell(
            row=row, column=8,
            value=f"=IFERROR(C{row}/G{row},0)",
        )
        h_cell.style = "number"

        # I: Crossover Ratio (Base)
        i_cell = ws.cell(
            row=row, column=9,
            value=f"=IFERROR(D{row}/G{row},0)",
        )
        i_cell.style = "number"

        # J: Crossover Ratio (High)
        j_cell = ws.cell(
            row=row, column=10,
            value=f"=IFERROR(E{row}/G{row},0)",
        )
        j_cell.style = "number"

        # K: Host Share ($) = 70% of base fee revenue
        k_cell = ws.cell(
            row=row, column=11,
            value=f"=D{row}*{host_share_ref}",
        )
        k_cell.style = "currency"

        # L: AI Fund Share ($) = 20% of base fee revenue
        l_cell = ws.cell(
            row=row, column=12,
            value=f"=D{row}*{ai_fund_ref}",
        )
        l_cell.style = "currency"

        # M: Buyback Share ($) = 5% of base fee revenue
        m_cell = ws.cell(
            row=row, column=13,
            value=f"=D{row}*{buyback_ref}",
        )
        m_cell.style = "currency"

        # N: Yield Pool Share ($) = 5% of base fee revenue
        n_cell = ws.cell(
            row=row, column=14,
            value=f"=D{row}*{yield_ref}",
        )
        n_cell.style = "currency"

    # ------------------------------------------------------------------
    # Row 35: Blank separator
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Rows 36-40: 9-cell Crossover RATIO Matrix at Year 10
    # ------------------------------------------------------------------

    # Row 36: Section header
    ws.merge_cells("A36:D36")
    matrix_header = ws.cell(
        row=36, column=1,
        value="CROSSOVER MATRIX (Fees / Emission Ratio at Year 10)",
    )
    matrix_header.style = "section_header"

    # Row 37: Sub-header
    ws.cell(row=37, column=1, value="")  # empty corner
    ws.cell(row=37, column=2, value="Conservative Price").style = "header"
    ws.cell(row=37, column=3, value="Moderate Price").style = "header"
    ws.cell(row=37, column=4, value="Aggressive Price").style = "header"

    # Year 10 is row 34 (last data row, i=31, annual period)
    yr10_row = 34

    # Growth rate refs and labels for the 3 rows
    growth_rates = [
        ("Low Growth", low_growth_ref),
        ("Base Growth", mod_growth_ref),
        ("High Growth", high_growth_ref),
    ]
    # Price columns from Token Price tab
    price_cols = [tp_cons_col, tp_mod_col, tp_agg_col]

    for g_idx, (g_label, g_ref) in enumerate(growth_rates):
        matrix_row = 38 + g_idx
        ws.cell(row=matrix_row, column=1, value=g_label)

        for p_idx, p_col in enumerate(price_cols):
            # Fee revenue at Year 10 for this growth rate
            # = base_devs * (1 + growth)^(start_epoch/365) * rev_per_dev * 365/365
            # Emission value = IF(toggle="ON", MAX(mining, tail*365), mining) * price
            formula = (
                f"=IFERROR("
                f"({base_devs_ref}*(1+{g_ref})"
                f"^({es_sheet}!{es_start_col}{yr10_row}/365)"
                f"*{rev_per_dev_ref}*365/365)"
                f"/"
                f"(IF({tail_toggle_ref}=\"ON\","
                f"MAX({es_sheet}!{es_mining_col}{yr10_row},{tail_rate_ref}*365),"
                f"{es_sheet}!{es_mining_col}{yr10_row})"
                f"*{tp_sheet}!{p_col}{yr10_row})"
                f",0)"
            )
            cell = ws.cell(row=matrix_row, column=2 + p_idx, value=formula)
            cell.style = "number"

    # ------------------------------------------------------------------
    # Rows 41-46: Crossover YEAR Matrix
    # ------------------------------------------------------------------

    # Row 41: Blank separator

    # Row 42: Section header
    ws.merge_cells("A42:D42")
    year_header = ws.cell(
        row=42, column=1,
        value="CROSSOVER YEAR (First Year Fees > Emissions)",
    )
    year_header.style = "section_header"

    # Row 43: Sub-header
    ws.cell(row=43, column=1, value="")
    ws.cell(row=43, column=2, value="Conservative Price").style = "header"
    ws.cell(row=43, column=3, value="Moderate Price").style = "header"
    ws.cell(row=43, column=4, value="Aggressive Price").style = "header"

    # Rows 44-46: Crossover year for each growth rate
    # Uses INDEX/MATCH on columns H/I/J (crossover ratios using Active Price)
    ratio_cols = ["H", "I", "J"]
    for g_idx, (g_label, _g_ref) in enumerate(growth_rates):
        year_row = 44 + g_idx
        ratio_col = ratio_cols[g_idx]

        ws.cell(row=year_row, column=1, value=g_label)

        # Merge B:D since all use Active Price (single result per growth rate)
        ws.merge_cells(
            start_row=year_row, start_column=2,
            end_row=year_row, end_column=4,
        )

        formula = (
            f'=IFERROR(INDEX($A$3:$A$34,'
            f'MATCH(1,${ratio_col}$3:${ratio_col}$34,1)),"Never")'
        )
        cell = ws.cell(row=year_row, column=2, value=formula)
        cell.style = "formula_cell"

    # Row 47: Note
    note_cell = ws.cell(
        row=47, column=1,
        value="* Based on Active Price scenario (change on Assumptions tab)",
    )
    note_cell.style = "formula_cell"
    note_cell.font = note_cell.font.copy(italic=True)

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
    # Build fee_meta for downstream tabs and charts
    # ------------------------------------------------------------------
    fee_meta = {
        "sheet_name": "Fee Transition",
        "header_row": 2,
        "data_start_row": 3,
        "data_end_row": 34,
        "cols": {
            "period_label": "A",
            "developer_count": "B",
            "fee_rev_low": "C",
            "fee_rev_base": "D",
            "fee_rev_high": "E",
            "emission_value": "F",
            "effective_emission_value": "G",
            "crossover_ratio_low": "H",
            "crossover_ratio_base": "I",
            "crossover_ratio_high": "J",
            "host_share": "K",
            "ai_fund_share": "L",
            "buyback_share": "M",
            "yield_share": "N",
        },
        "matrix_start_row": 37,
        "matrix_end_row": 40,
        "crossover_year_matrix_start_row": 43,
        "crossover_year_matrix_end_row": 46,
        "danger_zone_rows": [32, 33, 34],
    }

    # ------------------------------------------------------------------
    # Charts
    # ------------------------------------------------------------------
    _create_waterfall_chart(ws, fee_meta)
    _create_crossover_timeline_chart(ws, fee_meta)
    _create_fee_vs_emission_chart(ws, fee_meta)

    return fee_meta

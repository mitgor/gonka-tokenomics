"""
Gonka Tokenomics - Standalone Workbook Generator

Generates 4 focused standalone workbooks from the same builders used
by the master workbook. Each standalone has filtered assumptions
containing only the parameters relevant to its model chain.

Public API:
    generate_standalones() -> dict  # generates all 4 standalones
    generate_standalone(config_key) -> str  # generates one standalone
"""

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font

from generators.workbook_base import build_filtered_assumptions_tab
from generators.emission import build_emission_tab
from generators.token_price import build_token_price_tab
from generators.fee_transition import build_fee_transition_tab
from generators.host_profit import build_host_profit_tab
from generators.treasury import build_treasury_tab
from generators.glossary import build_glossary_tab
from generators.cover_sheet import build_cover_sheet
from generators.chart_utils import fix_chart_rendering
from generators.standalone_config import STANDALONE_CONFIGS, GLOSSARY_TERMS, VERSION_INFO


# ---------------------------------------------------------------------------
# Module-level constants
# ---------------------------------------------------------------------------

LINK_FONT = Font(name="Calibri", size=11, color="0563C1", underline="single")

# Back-to-Documentation link positions per tab.
# Same positions as the master workbook where applicable.
_BACK_LINK_COL_ROW = {
    "Assumptions": (6, 1),          # F1 (after A1:E1 merge)
    "Emission Schedule": (11, 2),   # K2 (K1 is chart anchor; use row 2)
    "Token Price": (13, 1),         # M1 (after A1:L1 merge, before N1 chart)
    "Fee Transition": (15, 1),      # O1 (after A1:N1 merge, before P1 chart)
    "Host Profitability": (14, 1),  # N1 (after A1:M1 merge, before O1 chart)
    "Treasury & POL": (15, 1),      # O1 (after A1:N1 merge, before P1 chart)
    "Definitions": (4, 1),          # D1 (outside A1:C1 merge area)
}


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _add_back_to_doc_links(wb):
    """Add 'Back to Documentation' hyperlink on every non-Documentation tab."""
    for ws in wb.worksheets:
        if ws.title == "Documentation":
            continue
        if ws.title in _BACK_LINK_COL_ROW:
            col, row = _BACK_LINK_COL_ROW[ws.title]
        else:
            col, row = 1, 1
        cell = ws.cell(row=row, column=col)
        cell.value = "<< Documentation"
        cell.hyperlink = "#Documentation!A1"
        cell.font = LINK_FONT


def _build_model_tabs(wb, param_refs, builders):
    """Build model tabs in dependency order and return meta dict.

    Args:
        wb: openpyxl Workbook with Assumptions tab already built.
        param_refs: Parameter reference dict from filtered assumptions.
        builders: List of builder names in dependency order.

    Returns:
        dict: Mapping of builder name -> meta dict from each builder.
    """
    meta = {}
    for builder_name in builders:
        if builder_name == "emission":
            meta["emission"] = build_emission_tab(wb, param_refs)
        elif builder_name == "token_price":
            meta["token_price"] = build_token_price_tab(
                wb, param_refs, meta["emission"],
            )
        elif builder_name == "fee_transition":
            meta["fee_transition"] = build_fee_transition_tab(
                wb, param_refs, meta["emission"], meta["token_price"],
            )
        elif builder_name == "host_profitability":
            meta["host_profitability"] = build_host_profit_tab(
                wb, param_refs, meta["emission"], meta["token_price"],
                meta["fee_transition"],
            )
        elif builder_name == "treasury":
            meta["treasury"] = build_treasury_tab(
                wb, param_refs, meta["emission"], meta["token_price"],
                meta["fee_transition"],
            )
    return meta


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def generate_standalone(config_key):
    """Generate a single standalone workbook.

    Args:
        config_key: Key into STANDALONE_CONFIGS (e.g., "token_price").

    Returns:
        str: Path to the generated .xlsx file.
    """
    config = STANDALONE_CONFIGS[config_key]

    # 1. Create fresh workbook
    wb = Workbook()

    # 2. Build filtered Assumptions tab
    param_refs = build_filtered_assumptions_tab(
        wb,
        param_names=config["params"],
        include_scenario_selector=True,
        include_tail_toggle=config.get("include_tail_toggle", False),
        include_toggles=config.get("toggles", []),
    )

    # 3. Build model tabs in dependency order
    _build_model_tabs(wb, param_refs, config["builders"])

    # 4. Build glossary tab (Definitions)
    build_glossary_tab(wb, GLOSSARY_TERMS)

    # 5. Build cover sheet (Documentation tab at index 0)
    tab_names = [ws.title for ws in wb.worksheets if ws.title != "Documentation"]
    build_cover_sheet(
        wb,
        config["title"],
        VERSION_INFO,
        tab_names,
        config.get("narratives"),
    )

    # 6. Verify tab order: Documentation first, Assumptions second, Definitions last
    assert wb.worksheets[0].title == "Documentation", (
        f"Expected Documentation at index 0, got {wb.worksheets[0].title}"
    )
    assert wb.worksheets[1].title == "Assumptions", (
        f"Expected Assumptions at index 1, got {wb.worksheets[1].title}"
    )
    assert wb.worksheets[-1].title == "Definitions", (
        f"Expected Definitions at last index, got {wb.worksheets[-1].title}"
    )

    # 7. Add "Back to Documentation" links on non-Documentation tabs
    _add_back_to_doc_links(wb)

    # 8. Save workbook and fix chart rendering
    output_path = Path("output") / config["filename"]
    output_path.parent.mkdir(exist_ok=True)
    wb.save(str(output_path))
    fix_chart_rendering(str(output_path))

    return str(output_path)


def generate_standalones():
    """Generate all 4 standalone workbooks.

    Returns:
        dict: Mapping of config_key -> output_path for each standalone.
    """
    results = {}
    for config_key, config in STANDALONE_CONFIGS.items():
        path = generate_standalone(config_key)
        tab_count = len(Workbook().sheetnames)  # don't load; count from config
        expected_tabs = len(config["builders"]) + 3  # +3 for Documentation, Assumptions, Definitions
        print(f"  Generated: {path} ({expected_tabs} tabs)")
        results[config_key] = path

    return results

#!/usr/bin/env python3
"""
Gonka Tokenomics Model Generator

Generates Excel workbooks (.xlsx) for Gonka Network tokenomics modeling.
All parameters from v1.0 research are written to an Assumptions tab that
drives all downstream calculations via Excel formulas.

Usage:
    python generate.py              # Generate all workbooks
    python generate.py --test       # Generate minimal test workbook (Assumptions only)

Output directory: ./output/
"""
import sys
from pathlib import Path


def main():
    # Ensure output directory exists
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # Parse args
    test_mode = "--test" in sys.argv

    if test_mode:
        generate_test()
    else:
        generate_all()


def generate_test():
    """Generate a minimal test workbook with only the Assumptions tab."""
    from generators.workbook_base import create_workbook

    wb, param_refs = create_workbook()

    output_path = Path("output") / "gonka_test_assumptions.xlsx"
    wb.save(str(output_path))
    print(f"Generated: {output_path}")
    print(f"  Assumptions tab: {len(param_refs)} parameters")


def generate_all():
    """Generate the master workbook with all model tabs and charts."""
    from generators.workbook_base import create_workbook
    from generators.emission import build_emission_tab
    from generators.token_price import build_token_price_tab
    from generators.chart_utils import fix_chart_rendering
    from generators.fee_transition import build_fee_transition_tab
    from generators.host_profit import build_host_profit_tab

    wb, param_refs = create_workbook()

    # Phase 2: Emission Schedule Model
    emission_meta = build_emission_tab(wb, param_refs)

    # Phase 3: Token Price Scenarios Model
    price_meta = build_token_price_tab(wb, param_refs, emission_meta)

    # Phase 4: Fee Transition Crossover Model
    fee_meta = build_fee_transition_tab(wb, param_refs, emission_meta, price_meta)

    # Phase 5: Host Profitability Model
    host_meta = build_host_profit_tab(wb, param_refs, emission_meta, price_meta, fee_meta)

    # Phase 6+: Future model tabs
    # Phase 6: treasury.build_treasury_tab(wb, param_refs)

    output_path = Path("output") / "gonka_master_model.xlsx"
    wb.save(str(output_path))
    fix_chart_rendering(str(output_path))
    print(f"Generated: {output_path}")
    print(f"  Assumptions tab: {len(param_refs)} parameters")
    print(f"  Emission Schedule tab: {emission_meta['data_end_row'] - emission_meta['data_start_row'] + 1} periods, 3 charts")
    print(f"  Token Price tab: {price_meta['data_end_row'] - price_meta['data_start_row'] + 1} periods, 2 charts")
    print(f"  Fee Transition tab: {fee_meta['data_end_row'] - fee_meta['data_start_row'] + 1} periods, 14 columns, 2 matrices")
    print(f"  Host Profitability tab: {host_meta['data_end_row'] - host_meta['data_start_row'] + 1} periods, 13 columns, sensitivity matrix")


if __name__ == "__main__":
    main()

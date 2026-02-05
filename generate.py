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
    """Generate all workbooks. Currently generates master workbook skeleton."""
    from generators.workbook_base import create_workbook

    wb, param_refs = create_workbook()

    # Future phases will add model tabs here:
    # Phase 2: emission.build_emission_tab(ws, param_refs)
    # Phase 3: token_price.build_token_price_tab(ws, param_refs)
    # Phase 4: fee_transition.build_fee_transition_tab(ws, param_refs, emission_meta)
    # Phase 5: host_profit.build_host_profit_tab(ws, param_refs, emission_meta, price_meta)
    # Phase 6: treasury.build_treasury_tab(ws, param_refs)

    output_path = Path("output") / "gonka_master_model.xlsx"
    wb.save(str(output_path))
    print(f"Generated: {output_path}")
    print(f"  Assumptions tab: {len(param_refs)} parameters")
    print(f"  Model tabs: (none yet -- added in Phase 2+)")


if __name__ == "__main__":
    main()

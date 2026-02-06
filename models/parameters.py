"""
Gonka Tokenomics - Parameter Definitions (Single Source of Truth)

All input parameters from v1.0 research organized by group.
Every parameter includes: name, value, unit, source reference, and format.

This file has ZERO external dependencies (no openpyxl, no third-party imports).
It is pure Python data used by all downstream modules.

REQ-F01: All constants defined here. No business constants elsewhere.
"""

from collections import OrderedDict


PARAM_GROUPS = OrderedDict([

    # =========================================================================
    # TOKEN SUPPLY
    # =========================================================================
    ("TOKEN SUPPLY", [
        {
            "name": "Total Supply",
            "value": 1_000_000_000,
            "unit": "GNK",
            "source": "Whitepaper",
            "format": "tokens",
        },
        {
            "name": "Mining Rewards Pool",
            "value": 680_000_000,
            "unit": "GNK",
            "source": "Whitepaper (68%)",
            "format": "tokens",
        },
        {
            "name": "Community Pool",
            "value": 120_000_000,
            "unit": "GNK",
            "source": "Whitepaper (12%)",
            "format": "tokens",
        },
        {
            "name": "Founder Allocation",
            "value": 200_000_000,
            "unit": "GNK",
            "source": "Whitepaper (20%)",
            "format": "tokens",
        },
    ]),

    # =========================================================================
    # EMISSION PARAMETERS
    # =========================================================================
    ("EMISSION PARAMETERS", [
        {
            "name": "Initial Daily Emission",
            "value": 323_000,
            "unit": "GNK/day",
            "source": "Whitepaper",
            "format": "tokens",
        },
        {
            "name": "Decay Rate",
            "value": 0.000475,
            "unit": "per epoch",
            "source": "Whitepaper",
            "format": "decay_rate",
        },
        {
            "name": "Epochs Per Day",
            "value": 1,
            "unit": "epochs",
            "source": "Assumption",
            "format": "integer",
        },
        {
            "name": "Tail Emission Rate (Contingency)",
            "value": 10_000,
            "unit": "GNK/day",
            "source": "Rec #1",
            "format": "tokens",
        },
    ]),

    # =========================================================================
    # REVENUE ALLOCATION
    # =========================================================================
    ("REVENUE ALLOCATION", [
        {
            "name": "Host Share",
            "value": 0.70,
            "unit": "",
            "source": "Rec #3",
            "format": "percent",
        },
        {
            "name": "AI Training Fund",
            "value": 0.20,
            "unit": "",
            "source": "Rec #3",
            "format": "percent",
        },
        {
            "name": "Buyback-Burn",
            "value": 0.05,
            "unit": "",
            "source": "Rec #3",
            "format": "percent",
        },
        {
            "name": "veGNK Yield Pool",
            "value": 0.05,
            "unit": "",
            "source": "Rec #3",
            "format": "percent",
        },
    ]),

    # =========================================================================
    # PRICE SCENARIOS
    # =========================================================================
    ("PRICE SCENARIOS", [
        {
            "name": "Conservative Price Low",
            "value": 0.50,
            "unit": "USD",
            "source": "v1.0 Research",
            "format": "currency",
        },
        {
            "name": "Conservative Price High",
            "value": 1.00,
            "unit": "USD",
            "source": "v1.0 Research",
            "format": "currency",
        },
        {
            "name": "Moderate Price Low",
            "value": 1.00,
            "unit": "USD",
            "source": "v1.0 Research",
            "format": "currency",
        },
        {
            "name": "Moderate Price High",
            "value": 3.00,
            "unit": "USD",
            "source": "v1.0 Research",
            "format": "currency",
        },
        {
            "name": "Aggressive Price Low",
            "value": 3.00,
            "unit": "USD",
            "source": "v1.0 Research",
            "format": "currency",
        },
        {
            "name": "Aggressive Price High",
            "value": 10.00,
            "unit": "USD",
            "source": "v1.0 Research",
            "format": "currency",
        },
        {
            "name": "Bitfury Schelling Point",
            "value": 0.60,
            "unit": "USD",
            "source": "Strategic Data",
            "format": "currency",
        },
    ]),

    # =========================================================================
    # DEVELOPER GROWTH
    # =========================================================================
    ("DEVELOPER GROWTH", [
        {
            "name": "Conservative Dev Growth",
            "value": 0.10,
            "unit": "annual",
            "source": "Rec #4",
            "format": "percent",
        },
        {
            "name": "Moderate Dev Growth",
            "value": 0.25,
            "unit": "annual",
            "source": "Rec #4",
            "format": "percent",
        },
        {
            "name": "Aggressive Dev Growth",
            "value": 0.40,
            "unit": "annual",
            "source": "Rec #4",
            "format": "percent",
        },
        {
            "name": "Base Active Developers",
            "value": 2_200,
            "unit": "developers",
            "source": "Network Data",
            "format": "integer",
        },
    ]),

    # =========================================================================
    # FEE TRANSITION
    # =========================================================================
    ("FEE TRANSITION", [
        {
            "name": "Revenue Per Developer (Annual)",
            "value": 36000,
            "unit": "USD/yr",
            "source": "Rec #4 ($3K/mo avg)",
            "format": "currency",
        },
        {
            "name": "Tail Emission Toggle",
            "value": "OFF",
            "unit": "",
            "source": "Rec #1",
            "format": "text",
        },
    ]),

    # =========================================================================
    # GPU ECONOMICS
    # =========================================================================
    ("GPU ECONOMICS", [
        {
            "name": "H100 Current Price (Specialized)",
            "value": 2.50,
            "unit": "USD/hr",
            "source": "Rec #9",
            "format": "price_per_hour",
        },
        {
            "name": "H100 Current Price (Hyperscaler)",
            "value": 11.75,
            "unit": "USD/hr",
            "source": "Rec #9",
            "format": "price_per_hour",
        },
        {
            "name": "GPU Annual Price Deflation",
            "value": 0.40,
            "unit": "annual",
            "source": "Research",
            "format": "percent",
        },
        {
            "name": "Gonka Target Price",
            "value": 2.25,
            "unit": "USD/hr",
            "source": "Rec #5 (balanced)",
            "format": "price_per_hour",
        },
    ]),

    # =========================================================================
    # HOST ECONOMICS
    # =========================================================================
    ("HOST ECONOMICS", [
        {
            "name": "Current Hosts",
            "value": 448,
            "unit": "hosts",
            "source": "Network Data",
            "format": "integer",
        },
        {
            "name": "Current GPUs",
            "value": 6_000,
            "unit": "H100-eq",
            "source": "Network Data",
            "format": "integer",
        },
        {
            "name": "Electricity Cost Low",
            "value": 0.05,
            "unit": "USD/kWh",
            "source": "Industry",
            "format": "price_per_hour",
        },
        {
            "name": "Electricity Cost Mid",
            "value": 0.08,
            "unit": "USD/kWh",
            "source": "Industry",
            "format": "price_per_hour",
        },
        {
            "name": "Electricity Cost High",
            "value": 0.12,
            "unit": "USD/kWh",
            "source": "Industry",
            "format": "price_per_hour",
        },
        {
            "name": "H100 Hardware Cost Low",
            "value": 25_000,
            "unit": "USD",
            "source": "Market Data",
            "format": "currency",
        },
        {
            "name": "H100 Hardware Cost High",
            "value": 40_000,
            "unit": "USD",
            "source": "Market Data",
            "format": "currency",
        },
        {
            "name": "Host Collateral Rate",
            "value": 0.0625,
            "unit": "GNK/nonce",
            "source": "Whitepaper",
            "format": "decay_rate",
        },
        {
            "name": "Traditional Rental Rate (Lambda)",
            "value": 2.49,
            "unit": "USD/hr",
            "source": "Lambda Labs Q1 2026",
            "format": "price_per_hour",
        },
        {
            "name": "Traditional Rental Rate (CoreWeave)",
            "value": 2.06,
            "unit": "USD/hr",
            "source": "CoreWeave 3yr reserved Q1 2026",
            "format": "price_per_hour",
        },
        {
            "name": "GPU Power Draw",
            "value": 400,
            "unit": "watts",
            "source": "H100 inference avg",
            "format": "integer",
        },
    ]),

    # =========================================================================
    # POL PARAMETERS
    # =========================================================================
    ("POL PARAMETERS", [
        {
            "name": "POL GNK Allocation",
            "value": 22_000_000,
            "unit": "GNK",
            "source": "Rec #2",
            "format": "tokens",
        },
        {
            "name": "GNK/USDC Pool Share",
            "value": 0.60,
            "unit": "",
            "source": "Rec #2",
            "format": "percent",
        },
        {
            "name": "GNK/ETH Pool Share",
            "value": 0.40,
            "unit": "",
            "source": "Rec #2",
            "format": "percent",
        },
        {
            "name": "LP Fee Tier",
            "value": 0.003,
            "unit": "",
            "source": "Rec #2",
            "format": "percent",
        },
        {
            "name": "Expected LP Fee Revenue Low",
            "value": 550_000,
            "unit": "USD/yr",
            "source": "Rec #2",
            "format": "currency",
        },
        {
            "name": "Expected LP Fee Revenue High",
            "value": 1_100_000,
            "unit": "USD/yr",
            "source": "Rec #2",
            "format": "currency",
        },
        {
            "name": "POL Rebalancing Cost",
            "value": 900,
            "unit": "USD/yr",
            "source": "Rec #2",
            "format": "currency",
        },
    ]),

    # =========================================================================
    # BUYBACK PARAMETERS
    # =========================================================================
    ("BUYBACK PARAMETERS", [
        {
            "name": "TWAP Interval",
            "value": 15,
            "unit": "minutes",
            "source": "Rec #3",
            "format": "integer",
        },
        {
            "name": "Max Slippage Per Order",
            "value": 0.005,
            "unit": "",
            "source": "Rec #3",
            "format": "percent",
        },
        {
            "name": "Dip Acceleration Factor",
            "value": 3.0,
            "unit": "multiplier",
            "source": "Rec #3",
            "format": "number",
        },
        {
            "name": "Dip Threshold",
            "value": 0.20,
            "unit": "below 30d TWAP",
            "source": "Rec #3",
            "format": "percent",
        },
        {
            "name": "Assumed Annual Fee Revenue",
            "value": 1_000_000,
            "unit": "USD/yr",
            "source": "Placeholder (Phase 4 replaces)",
            "format": "currency",
        },
    ]),

    # =========================================================================
    # FLOOR DEFENSE
    # =========================================================================
    ("FLOOR DEFENSE", [
        {
            "name": "Tier 1 Trigger",
            "value": 0.75,
            "unit": "of 30d TWAP",
            "source": "Rec #7",
            "format": "percent",
        },
        {
            "name": "Tier 2 Absolute Trigger",
            "value": 0.45,
            "unit": "USD",
            "source": "Rec #7",
            "format": "currency",
        },
        {
            "name": "Tier 3 Crisis Trigger",
            "value": 0.30,
            "unit": "USD",
            "source": "Rec #7",
            "format": "currency",
        },
        {
            "name": "Defense Treasury Target Low",
            "value": 2_000_000,
            "unit": "USD",
            "source": "Rec #7",
            "format": "currency",
        },
        {
            "name": "Defense Treasury Target High",
            "value": 5_000_000,
            "unit": "USD",
            "source": "Rec #7",
            "format": "currency",
        },
        {
            "name": "Annual GNK Allocation for Defense",
            "value": 6_000_000,
            "unit": "GNK",
            "source": "Rec #7",
            "format": "tokens",
        },
    ]),

    # =========================================================================
    # TREASURY OPERATIONS
    # =========================================================================
    ("TREASURY OPERATIONS", [
        {
            "name": "AI Fund Monthly Expenses",
            "value": 50_000,
            "unit": "USD/month",
            "source": "Placeholder (leadership adjustable)",
            "format": "currency",
        },
        {
            "name": "Defense Active Duration",
            "value": 6,
            "unit": "months",
            "source": "Scenario input",
            "format": "integer",
        },
    ]),

    # =========================================================================
    # veGNK PARAMETERS
    # =========================================================================
    ("veGNK PARAMETERS", [
        {
            "name": "Min Lock Duration",
            "value": 30,
            "unit": "days",
            "source": "Rec #6",
            "format": "integer",
        },
        {
            "name": "Max Lock Duration",
            "value": 730,
            "unit": "days",
            "source": "Rec #6",
            "format": "integer",
        },
        {
            "name": "Max Boost Multiplier",
            "value": 2.5,
            "unit": "multiplier",
            "source": "Rec #10",
            "format": "number",
        },
        {
            "name": "Expected Lock Rate",
            "value": 0.425,
            "unit": "of circulating",
            "source": "Rec #6 (midpoint 35-50%)",
            "format": "percent",
        },
        {
            "name": "Governance Quorum",
            "value": 0.334,
            "unit": "of total supply",
            "source": "Whitepaper",
            "format": "percent",
        },
    ]),

    # =========================================================================
    # NETWORK PARAMETERS
    # =========================================================================
    ("NETWORK PARAMETERS", [
        {
            "name": "EIP-1559 Stability Zone Low",
            "value": 0.40,
            "unit": "utilization",
            "source": "Whitepaper",
            "format": "percent",
        },
        {
            "name": "EIP-1559 Stability Zone High",
            "value": 0.60,
            "unit": "utilization",
            "source": "Whitepaper",
            "format": "percent",
        },
        {
            "name": "EIP-1559 Adjustment Rate",
            "value": 0.02,
            "unit": "per block",
            "source": "Whitepaper",
            "format": "percent",
        },
    ]),
])


def get_all_params():
    """Return a flat list of all parameters across all groups."""
    return [p for group in PARAM_GROUPS.values() for p in group]


def get_param(name):
    """Look up a parameter by name. Returns the dict or raises KeyError."""
    for group in PARAM_GROUPS.values():
        for p in group:
            if p["name"] == name:
                return p
    raise KeyError(f"Parameter not found: {name}")

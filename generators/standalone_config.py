"""
Gonka Tokenomics - Standalone Workbook Configuration

Centralizes all per-standalone configuration data:
  - Parameter name sets (which PARAM_GROUPS entries each standalone needs)
  - Glossary terms and definitions
  - Scenario narratives for each standalone model
  - Version info and changelog
  - STANDALONE_CONFIGS master dict mapping standalone name -> config

Parameter sets are built compositionally: each standalone includes its own
params plus all upstream dependencies. The sets contain only names that
exist in PARAM_GROUPS (Active Price Low/High are computed by the scenario
selector, not stored in PARAM_GROUPS).

This file has ZERO external dependencies. It is pure Python data.
"""


# =============================================================================
# PARAMETER NAME SETS (frozenset for immutability)
# =============================================================================

EMISSION_PARAMS = frozenset({
    "Initial Daily Emission",
    "Decay Rate",
    "Community Pool",
    "Founder Allocation",
})

TOKEN_PRICE_PARAMS = EMISSION_PARAMS | frozenset({
    "Conservative Price Low",
    "Conservative Price High",
    "Moderate Price Low",
    "Moderate Price High",
    "Aggressive Price Low",
    "Aggressive Price High",
    "Bitfury Schelling Point",
    "Total Supply",
    "Assumed Annual Fee Revenue",
    "Buyback-Burn",
    "Buyback-Burn Active",
})

FEE_TRANSITION_PARAMS = TOKEN_PRICE_PARAMS | frozenset({
    "Base Active Developers",
    "Conservative Dev Growth",
    "Moderate Dev Growth",
    "Aggressive Dev Growth",
    "Revenue Per Developer (Annual)",
    "Host Share",
    "AI Training Fund",
    "Buyback-Burn",       # already in TOKEN_PRICE_PARAMS (no-op, explicit)
    "veGNK Yield Pool",
    "Tail Emission Toggle",
    "Tail Emission Rate (Contingency)",
})

HOST_PROFITABILITY_PARAMS = FEE_TRANSITION_PARAMS | frozenset({
    "Current Hosts",
    "Current GPUs",
    "Electricity Cost Low",
    "Electricity Cost Mid",
    "Electricity Cost High",
    "GPU Power Draw",
    "Traditional Rental Rate (Lambda)",
    "H100 Hardware Cost Low",
    "H100 Hardware Cost High",
})

TREASURY_POL_PARAMS = FEE_TRANSITION_PARAMS | frozenset({
    "POL GNK Allocation",
    "Expected LP Fee Revenue Low",
    "Expected LP Fee Revenue High",
    "POL Rebalancing Cost",
    "Annual GNK Allocation for Defense",
    "Defense Treasury Target Low",
    "AI Fund Monthly Expenses",
    "Deploy POL Active",
})


# =============================================================================
# GLOSSARY TERMS
# =============================================================================

GLOSSARY_TERMS = {
    "Breakeven Price": (
        "The minimum GNK token price at which a host's mining rewards cover "
        "their electricity costs. Below this price, hosts operate at a loss "
        "on mining alone."
    ),
    "Buyback-Burn": (
        "Protocol mechanism where a portion of fee revenue is used to purchase "
        "GNK tokens on the open market, which are then permanently removed "
        "from circulation (burned), creating deflationary pressure."
    ),
    "Community Pool": (
        "12% of total GNK supply (120M GNK) reserved for ecosystem grants, "
        "partnerships, and protocol-owned liquidity deployment."
    ),
    "Crossover Ratio": (
        "Fee revenue divided by emission value (in USD). When the ratio "
        "reaches 1.0, fee revenue fully offsets the cost of new token "
        "emissions -- the sustainability threshold."
    ),
    "Decay Rate": (
        "The exponential decay constant (0.000475 per epoch) that reduces "
        "daily mining emissions over time. Produces a halving approximately "
        "every 1,460 epochs (~4 years)."
    ),
    "EIP-1559": (
        "Ethereum Improvement Proposal 1559. A dynamic fee mechanism where "
        "a base fee adjusts automatically based on network utilization, "
        "maintaining fees within a stability zone (40-60% utilization)."
    ),
    "Epoch": (
        "A discrete time period in the Gonka network. The model assumes "
        "1 epoch per day. Emission decay is applied per epoch."
    ),
    "FDV": (
        "Fully Diluted Valuation. Total Supply (1B GNK) multiplied by the "
        "current token price. Represents the theoretical total market "
        "capitalization if all tokens were in circulation."
    ),
    "Floor Defense": (
        "A tiered price defense mechanism using treasury funds to support "
        "GNK price during severe downturns. Three tiers trigger at 75% of "
        "30-day TWAP, $0.45 absolute, and $0.30 crisis levels."
    ),
    "Impermanent Loss": (
        "The temporary loss of value that liquidity providers experience "
        "when the price ratio of pooled assets changes. Not modeled in v1 "
        "because an incorrect IL estimate is worse than none."
    ),
    "Mining Rewards": (
        "GNK tokens distributed to hosts who provide compute resources. "
        "Emissions start at 323,000 GNK/day and decay exponentially, with "
        "68% of total supply (680M GNK) allocated to mining."
    ),
    "Net Treasury Value": (
        "The total USD value of all treasury components: Community Pool "
        "balance, POL positions, accumulated LP fees, defense treasury, "
        "and AI Training Fund balance."
    ),
    "POL": (
        "Protocol-Owned Liquidity. Liquidity pool positions owned by the "
        "Gonka protocol treasury (22M GNK across GNK/USDC 60% and GNK/ETH "
        "40% pools on Uniswap v3) rather than third-party liquidity providers."
    ),
    "ROI": (
        "Return on Investment. For hosts, calculated as annual net profit "
        "divided by hardware cost. Expressed as a percentage indicating "
        "how quickly the hardware investment pays for itself."
    ),
    "Schelling Point": (
        "A focal price ($0.60) derived from Bitfury strategic data that "
        "serves as a natural coordination point for market expectations. "
        "Used as a reference in token price modeling."
    ),
    "Sensitivity Analysis": (
        "A technique that varies one input parameter at a time to measure "
        "its impact on outputs. Used in the model for breakeven prices, "
        "host profitability, and treasury scenarios."
    ),
    "Tail Emission": (
        "A minimum daily emission rate (10,000 GNK/day contingency) that "
        "can be activated when natural exponential decay falls below the "
        "threshold, ensuring ongoing host incentives."
    ),
    "TWAP": (
        "Time-Weighted Average Price. An average token price calculated over "
        "a fixed interval (e.g., 15 minutes) to smooth out short-term "
        "volatility and reduce manipulation risk in buyback execution."
    ),
    "veGNK": (
        "Vote-Escrowed GNK. GNK tokens locked for a period (30-730 days) "
        "to gain governance voting power and yield boost multipliers up to "
        "2.5x. Modeled after Curve's veCRV mechanism."
    ),
    "What-If Toggle": (
        "A Y/N dropdown switch on the Assumptions tab that enables or "
        "disables a specific protocol mechanism (e.g., Buyback-Burn, "
        "Deploy POL) for scenario analysis."
    ),
}


# =============================================================================
# SCENARIO NARRATIVES
# =============================================================================

TOKEN_PRICE_NARRATIVES = {
    "Conservative": (
        "Under conservative assumptions, GNK trades in the $0.50-$1.00 range "
        "over 10 years, reflecting cautious adoption and limited network effects. "
        "Market cap reaches approximately $900M by Year 10 with modest "
        "buyback-burn impact on circulating supply."
    ),
    "Base": (
        "The base scenario projects GNK price growth from $1.00 to $3.00, "
        "driven by steady developer onboarding and increasing network "
        "utilization. Buyback-burn meaningfully reduces circulating supply "
        "by Year 5-6, supporting price appreciation."
    ),
    "Aggressive": (
        "Aggressive adoption drives GNK from $3.00 to $10.00, assuming rapid "
        "GPU network expansion and strong compute demand. FDV exceeds $9B by "
        "Year 10 with significant deflationary pressure from buyback-burn."
    ),
}

FEE_TRANSITION_NARRATIVES = {
    "Conservative": (
        "With 10% annual developer growth, fee revenue grows slowly and the "
        "crossover point (where fees exceed emission costs) occurs around "
        "Year 10-12. The network remains heavily subsidy-dependent through "
        "most of the projection period."
    ),
    "Base": (
        "At 25% annual developer growth, fee revenue accelerates meaningfully "
        "and crossover occurs around Year 3-4. This represents the target "
        "trajectory where the network transitions to fee-sustainable "
        "operation within a reasonable timeframe."
    ),
    "Aggressive": (
        "With 40% annual developer growth, fee revenue ramps quickly and "
        "crossover occurs within Year 2. The network becomes self-sustaining "
        "early, but this scenario requires exceptional market conditions "
        "and rapid ecosystem adoption."
    ),
}

HOST_PROFITABILITY_NARRATIVES = {
    "Conservative": (
        "At conservative token prices ($0.50-$1.00), hosts face tight margins. "
        "Breakeven electricity prices are low, and only hosts with the cheapest "
        "power ($0.05/kWh or below) remain profitable after Year 3-4 as "
        "mining emissions decay."
    ),
    "Base": (
        "At moderate token prices ($1.00-$3.00), hosting is profitable for "
        "most operators with typical electricity costs. Fee revenue supplements "
        "mining rewards and extends profitability well beyond the initial "
        "high-emission period."
    ),
    "Aggressive": (
        "At high token prices ($3.00-$10.00), hosting is highly profitable "
        "across all electricity cost tiers. Mining rewards alone cover costs "
        "for most of the projection period, and fee revenue provides "
        "substantial additional income."
    ),
}

TREASURY_POL_NARRATIVES = {
    "Conservative": (
        "Under conservative pricing, treasury growth is modest. The Community "
        "Pool depletes more slowly in GNK terms but USD value remains limited. "
        "Defense treasury accumulation is adequate but floor defense deployments "
        "consume a larger share of reserves."
    ),
    "Base": (
        "At moderate prices, treasury health is strong. POL positions generate "
        "meaningful LP fee revenue, the defense treasury exceeds minimum targets "
        "by Year 2-3, and the AI Training Fund sustains planned operational "
        "expenses through the projection period."
    ),
    "Aggressive": (
        "High token prices drive substantial treasury appreciation. POL "
        "positions gain significant USD value, the defense treasury is "
        "well-capitalized, and net treasury value exceeds $200M by mid-period. "
        "Floor defense is rarely needed in this scenario."
    ),
}


# =============================================================================
# VERSION INFO
# =============================================================================

VERSION_INFO = {
    "version": "v1.1",
    "changelog": [
        (
            "v1.1",
            "2026-02-06",
            "Added standalone workbooks, glossary tabs, what-if toggles, "
            "scenario narratives, and versioned cover sheets",
        ),
        (
            "v1.0",
            "2026-02-06",
            "Initial release with master workbook containing all model tabs "
            "and dashboard",
        ),
    ],
}


# =============================================================================
# STANDALONE CONFIGS
# =============================================================================

STANDALONE_CONFIGS = {
    "token_price": {
        "title": "Token Price Model",
        "filename": "gonka_token_price.xlsx",
        "params": TOKEN_PRICE_PARAMS,
        "narratives": TOKEN_PRICE_NARRATIVES,
        "builders": ["emission", "token_price"],
        "toggles": ["Buyback-Burn Active"],
        "include_tail_toggle": False,
    },
    "fee_transition": {
        "title": "Fee Transition Model",
        "filename": "gonka_fee_transition.xlsx",
        "params": FEE_TRANSITION_PARAMS,
        "narratives": FEE_TRANSITION_NARRATIVES,
        "builders": ["emission", "token_price", "fee_transition"],
        "toggles": ["Buyback-Burn Active"],
        "include_tail_toggle": True,
    },
    "host_profitability": {
        "title": "Host Profitability Model",
        "filename": "gonka_host_profitability.xlsx",
        "params": HOST_PROFITABILITY_PARAMS,
        "narratives": HOST_PROFITABILITY_NARRATIVES,
        "builders": ["emission", "token_price", "fee_transition", "host_profitability"],
        "toggles": ["Buyback-Burn Active"],
        "include_tail_toggle": True,
    },
    "treasury_pol": {
        "title": "Treasury & POL Model",
        "filename": "gonka_treasury_pol.xlsx",
        "params": TREASURY_POL_PARAMS,
        "narratives": TREASURY_POL_NARRATIVES,
        "builders": ["emission", "token_price", "fee_transition", "treasury"],
        "toggles": ["Buyback-Burn Active", "Deploy POL Active"],
        "include_tail_toggle": True,
    },
}

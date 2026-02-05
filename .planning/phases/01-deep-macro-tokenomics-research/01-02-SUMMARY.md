---
phase: 01-deep-macro-tokenomics-research
plan: 02
subsystem: tokenomics-research
tags: [real-yield, buyback, burn, revenue-distribution, GMX, Hyperliquid, MakerDAO, Aave, veGNK, TWAP, AI-Training-Fund]

# Dependency graph
requires:
  - phase: 01-deep-macro-tokenomics-research
    provides: "Initial 10 recommendations from 01-RESEARCH.md (specifically Rec 2: Real Yield, Rec 4: Buyback)"
provides:
  - "12-protocol revenue distribution benchmark analysis"
  - "AI Training Fund surplus distribution design with runway-based threshold"
  - "Enhanced 20/70/5/5 revenue allocation model for Gonka"
  - "Continuous TWAP buyback-and-burn mechanism design"
  - "Comparative analysis table of 12 protocol revenue models"
  - "Revenue scenario modeling ($5M-$500M annual)"
affects: [01-06-synthesis, 01-07-synthesis, 01-08-capstone, veGNK-implementation, smart-contracts]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Surplus Buffer pattern (MakerDAO) for threshold-based distribution"
    - "Continuous TWAP buyback (Hyperliquid) for minimized market impact"
    - "Dual-mechanism value accrual (buyback-burn + staker-yield)"

key-files:
  created:
    - ".planning/phases/01-deep-macro-tokenomics-research/research/02-real-yield-and-buybacks.md"
  modified: []

key-decisions:
  - "Enhanced revenue split: 20% AI Fund / 70% hosts / 5% buyback-burn / 5% veGNK yield (from 20/70/10 unallocated)"
  - "AI Training Fund surplus threshold: 6-month runway-based (MakerDAO Surplus Buffer pattern)"
  - "Buyback mechanism: Continuous TWAP with 15-minute intervals, 0.5% max slippage"
  - "Burn all bought-back tokens (not redistribute) for regulatory safety and reflexive value"
  - "veGNK holders as exclusive real yield recipients (not all stakers or all holders)"
  - "Opportunistic dip-buying trigger: 3x rate when GNK >20% below 30-day TWAP"
  - "Gonka positioned as first decentralized AI compute network with genuine real yield"

patterns-established:
  - "Threshold-then-distribute: Maintain operational reserves before distributing surplus"
  - "Dual value accrual: Buyback-burn (universal) + direct yield (active participants)"
  - "Revenue-proportional deflationary pressure: Scales automatically with network adoption"

# Metrics
duration: 6min
completed: 2026-02-05
---

# Phase 01 Plan 02: Real Yield and Buybacks Summary

**12-protocol revenue benchmark analysis with enhanced 20/70/5/5 Gonka allocation model, continuous TWAP buyback-burn, and MakerDAO-inspired surplus distribution for AI Training Fund**

## Performance

- **Duration:** 6 min
- **Started:** 2026-02-05T20:57:14Z
- **Completed:** 2026-02-05T21:03:58Z
- **Tasks:** 1/1
- **Files created:** 1

## Accomplishments

- Analyzed 12 protocols' revenue distribution models (GMX, Gains Network, Aave, Synthetix, Lido, Hyperliquid, MakerDAO, BNB, Curve, Frax, SushiSwap, AI compute networks)
- Designed AI Training Fund surplus distribution with runway-based 6-month threshold following MakerDAO's Surplus Buffer pattern
- Proposed enhanced 20/70/5/5 revenue allocation model that transforms 10% unallocated revenue into 5% buyback-burn + 5% veGNK staker yield
- Defined continuous TWAP buyback-and-burn mechanism with opportunistic dip-buying trigger
- Created comprehensive 12-protocol comparative analysis table with revenue source, distribution %, mechanism, frequency, and eligibility
- Modeled revenue scenarios from $5M to $500M annual inference revenue with buyback impact analysis
- Identified Gonka as potentially first decentralized AI compute network with genuine real yield (vs. Akash, Render, Bittensor)

## Task Commits

Each task was committed atomically:

1. **Task 1: Research real yield models and buyback mechanisms** - `9dec65d` (feat)

## Files Created/Modified

- `.planning/phases/01-deep-macro-tokenomics-research/research/02-real-yield-and-buybacks.md` - Comprehensive research document (7,716 words, 43 source URLs, 12 protocols analyzed)

## Decisions Made

1. **Enhanced allocation: 20/70/5/5** -- Preserves host-first economics (70% unchanged) while reallocating the 10% unallocated to 5% buyback-burn + 5% veGNK yield. Percentages sum to 100%.

2. **Runway-based surplus threshold** -- AI Training Fund distributes surplus only after maintaining 6-month operating runway. More adaptive than fixed amount or percentage-of-supply thresholds. Modeled after MakerDAO's $50M Surplus Buffer.

3. **veGNK-exclusive yield** -- Real yield distributed only to veGNK holders (not all stakers or all holders). Creates maximum alignment: must lock tokens long-term to earn real yield, which also reduces circulating supply and strengthens governance.

4. **Burn over redistribute** -- All bought-back GNK is burned (not redistributed to stakers). Safer regulatory posture (not a dividend), creates reflexive value (supply reduction compounds), and avoids recycled supply. The 5% yield pool separately covers direct staker rewards.

5. **Continuous TWAP over periodic buyback** -- 15-minute interval TWAP reduces front-running and slippage vs. quarterly or monthly buybacks (BNB-style). Research shows 40-60% lower slippage for continuous vs. periodic.

6. **Opportunistic dip-buying** -- Accelerate buyback 3x when GNK drops >20% below 30-day TWAP. Creates counter-cyclical buy pressure during downturns.

## Deviations from Plan

None -- plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None -- no external service configuration required.

## Next Phase Readiness

- Real yield and buyback research complete, ready for synthesis with other Wave 1 research
- Revenue allocation model (20/70/5/5) needs governance approval proposal design
- Buyback smart contract specification depends on veGNK implementation timeline (Plan 03)
- AI Training Fund surplus threshold requires expense tracking infrastructure
- Research validated that no competing AI compute network has real yield -- competitive moat opportunity

---
*Phase: 01-deep-macro-tokenomics-research*
*Completed: 2026-02-05*

# Project State

## Current Position

**Current Milestone:** v1.0 Tokenomics Research & Optimization
**Current Phase:** Phase 1 - Deep Macro-Tokenomics Research & Gonka Recommendations
**Status:** PHASE 1 COMPLETE - All 3 waves finished (5 research + 2 synthesis + 1 capstone)
**Last activity:** 2026-02-05 - Completed 01-08-PLAN.md (Capstone Recommendations)

**Progress:** ████████ 100% (8 of 8 plans complete)

## Accumulated Context

### Roadmap Evolution
- Phase 1 added: Deep Macro-Tokenomics Research & Gonka Recommendations
- Phase 1 planned: 8 plans in 3 waves (5 parallel research + 2 synthesis + 1 capstone)
- Phase 1 COMPLETE: All 8 plans executed successfully

### Key Decisions
- Research covers all 10 recommendation areas from initial research
- Wave 1: 5 parallel deep research agents (POL, Real Yield, veGNK, Fee Transition, GPU Economics)
- Wave 2: 2 parallel synthesis agents (update existing docs)
- Wave 3: 1 capstone agent (final recommendations document)
- **POL allocation:** 20-25M GNK (16-21% of Community Pool) via Uniswap v3 concentrated liquidity
- **POL pair split:** 60% GNK/USDC (13.2M GNK) + 40% GNK/ETH (8.8M GNK) for stability and DeFi composability
- **POL parameters:** 0.3% fee tier, +-25-35% concentrated ranges, $44M target liquidity depth
- **LP fee revenue:** $550K-1.1M annually (3-6% APR), reinvest Years 1-2, distribute/burn Years 3+
- **POL cost efficiency:** $0.50 per $1 TVL vs $10 per $1 retained for mercenary liquidity mining
- **Fee transition crossover:** Conservative scenario 10-12 years, moderate 3-4 years (target trajectory)
- **Host profitability threshold:** GNK >= $0.85-$3.30 at critical decay points (scenario-dependent)
- **EIP-1559 optimization:** Current +-2% conservative; +-4% recommended for testing
- **Contingency triggers:** Activate if Year 4 fee revenue <$50M (vs $96.9M conservative baseline)
- **veGNK design:** 1 month - 2 year lock range (Phase 1), linear time-weighted voting, 2.5x max boost
- **Governance defense:** veGNK fully mitigates flash loan attacks (can't borrow locked tokens)
- **Quadratic voting:** Only viable for host-gated Community Pool decisions (GPU-based Sybil resistance)
- **veGNK separation:** Locked GNK does NOT count as host collateral (clean separation, easier slashing)
- **3-phase veGNK rollout:** Q2 2026 basic lock+voting, Q4 2026 boost+delegation, 2027 advanced features
- **Enhanced revenue split:** 20% AI Fund / 70% hosts / 5% buyback-burn / 5% veGNK yield (from 20/70/10 unallocated)
- **AI Training Fund surplus:** Runway-based threshold (6-month expenses) before surplus distribution (MakerDAO Surplus Buffer pattern)
- **Buyback mechanism:** Continuous TWAP (15-min intervals, 0.5% max slippage), burn all bought-back tokens
- **Opportunistic dip-buying:** 3x accelerated buyback when GNK >20% below 30-day TWAP
- **veGNK-exclusive yield:** Real yield from 5% pool + fund surplus only to veGNK holders (not all stakers)
- **Competitive moat:** No competing AI compute network (Akash, Render, Bittensor) has genuine real yield distribution
- **Oracle-based USD pricing:** Recommended over static GNK-denominated pricing to solve dual volatility (GPU deflation + GNK volatility)
- **Floor defense triggers:** 75% of 30-day TWAP (relative) and $0.45 absolute (25% below Bitfury Schelling point at $0.60)
- **Floor defense allocation:** Up to 5% Community Pool annually + 5-10% inference revenue for TWAP buybacks
- **Developer growth target:** 6K active (6mo) -> 15K (18mo) -> 25K (36mo), blended acquisition cost $150-500/dev
- **H100 pricing trajectory:** $1.50-2.99/hr (Q1 2026) -> $0.50-1.00/hr (2028), requiring continuous EIP-1559 adaptation
- **Hybrid oracle stack:** Pyth (speed, 400ms) + Chainlink (security, 1hr heartbeat) + UMA (flexibility, weekly benchmarks)
- **Document versioning:** Macro Research updated to v2.0 (1488 lines), Deep Analysis updated to v3.0 (2013 lines)
- **v3.0 inline annotations:** Used for traceability of new content within existing Deep Analysis document
- **Enhancement roadmap:** 10 prioritized recommendations with implementation timeline (Q2-Q4 2026 + 2027)
- **CAPSTONE: Recommendation priority ordering:** Fee Monitoring (CRITICAL) > POL (HIGH) > Revenue Restructure (HIGH) > Developer Growth (HIGH) > Oracle Pricing (HIGH) > veGNK (MEDIUM-HIGH) > Floor Defense (MEDIUM) > EIP-1559 (MEDIUM) > GPU Tracking (MEDIUM) > veGNK Advanced (LOW-MEDIUM)
- **CAPSTONE: Critical path:** Oracle integration is the key enabler -- buyback, floor defense, and USD pricing all depend on Pyth/Chainlink
- **CAPSTONE: Governance timeline:** 7 votes required across Months 1-10, with elevated quorum (50%) for tail emission

### Technical Notes
- Existing research files: Gonka_Tokenomics_Explained.md, Gonka_Tokenomics_Deep_Analysis.md, Gonka_Macro_Tokenomics_Research.md
- Codebase already mapped in .planning/codebase/
- Research output: 01-RESEARCH.md completed with 10 recommendations
- Plan verification: PASSED (all checks)
- **Wave 1 Research Outputs (ALL COMPLETE):**
  - 01-01: POL & Liquidity Management (10,487 words, 42+ sources) - Community Pool deployment strategy with $44M target liquidity
  - 01-02: Real yield & buybacks (7,716 words, 12 protocols) - Enhanced 20/70/5/5 allocation model, TWAP buyback design
  - 01-03: veToken & governance (10,882 words) - 6 protocols analyzed, veGNK design specified
  - 01-04: Fee transition stress test (8,839 words) - Critical economic modeling complete
  - 01-05: GPU economics & developer growth (8,306 words, 40+ sources) - GPU deflation model, competitive pricing, floor defense, oracle integration
- **Wave 2 Synthesis Outputs (ALL COMPLETE):**
  - 01-07: Stakeholder guide update (COMPLETE) - Gonka_Tokenomics_Explained.md updated with all 10 recommendations, economic outlook, Feb 2026 GPU data
  - 01-06: Deep analysis synthesis (COMPLETE) - Macro Research v2.0 (+495 lines) and Deep Analysis v3.0 (+484 lines) updated with all Wave 1 findings
- **Wave 3 Capstone (COMPLETE):**
  - 01-08: Final recommendations document (COMPLETE) - Gonka_Tokenomics_Fine_Tuning_Recommendations.md (1,111 lines, 8,506 words)

### Blockers & Concerns
- **POL paired asset shortage:** Gonka may lack $20-25M in USDC/ETH for pairing with GNK. Mitigation: Phased deployment with available assets, OTC sales, or Bitfury negotiation.
- **POL governance approval:** 33.4% quorum required for Community Pool allocation. Risk: Low engagement or host preference for direct distribution. Mitigation: Clear communication of POL benefits (100% retention vs 10-25% for liquidity mining).
- **Governance concentration risk:** Founder allocation (200M GNK) could control 67% of veGNK if locked for max duration while others lock shorter. Need voluntary lock caps or monitoring strategy.
- **veGNK lock rate uncertainty:** Projecting 35-50% lock rate based on ve protocol benchmarks, but requires strong boost incentives from AI Training Fund yield.
- **Developer adoption critical:** Fee transition analysis reveals 15-25% annual growth target needed to maintain host profitability as emissions decay.
- **Floor defense sustainability:** Treasury depletion possible in severe bear market (6+ months of -60%+ decline). Floor defense is speed bump, not wall. Revenue replenishment and governance recapitalization needed.
- **Oracle feed creation:** GNK/USD price feed does not yet exist on Pyth or Chainlink -- must self-fund or negotiate partnership. This is on the critical path.

## Session Continuity

Last session: 2026-02-05T21:39:00Z
Stopped at: Completed 01-08-PLAN.md (Phase 1 COMPLETE - all 8 plans finished)
Resume file: None

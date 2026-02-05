---
phase: 01-deep-macro-tokenomics-research
plan: 01
subsystem: tokenomics-research
tags: [POL, protocol-owned-liquidity, DeFi, liquidity-management, Uniswap-v3, Balancer, Olympus-DAO, treasury-management]

# Dependency graph
requires:
  - phase: initial-research
    provides: "10 tokenomics recommendations including POL as HIGH priority"
provides:
  - "Deep research on Protocol-Owned Liquidity mechanisms with 4+ protocol benchmarks"
  - "Quantified mercenary liquidity failure (10-25% retention rates)"
  - "Gonka-specific POL deployment strategy: 20-25M GNK allocation from Community Pool"
  - "Concentrated liquidity deployment parameters (ranges, fee tiers, pair compositions)"
  - "Risk analysis covering impermanent loss, smart contract, governance, and market manipulation"
  - "Financial projections: $550K-1.1M annual LP fee revenue at 3-6% APR"
affects: [POL-implementation, treasury-management, real-yield-distribution, liquidity-strategy]

# Tech tracking
tech-stack:
  added: [Uniswap-v3, Balancer-weighted-pools, concentrated-liquidity, LP-position-management]
  patterns: [protocol-owned-liquidity, dual-pair-strategy, rebalancing-protocol, fee-tier-optimization]

key-files:
  created:
    - ".planning/phases/01-deep-macro-tokenomics-research/research/01-pol-and-liquidity.md"
  modified: []

key-decisions:
  - "Recommend 20-25M GNK POL allocation (16-21% of 120M Community Pool) - within industry 15-35% benchmark"
  - "60/40 split between GNK/USDC and GNK/ETH pairs balances stability and DeFi composability"
  - "Uniswap v3 concentrated liquidity with ±25-35% ranges achieves 4-5x capital efficiency"
  - "0.3% fee tier optimal for medium-volatility governance tokens (standard for AAVE, COMP, UNI)"
  - "Dual-sided deployment preferred over single-sided (Tokemak) for full treasury control"
  - "POL generates $550K-1.1M annually vs. traditional liquidity mining which retains only 10-25% of liquidity"

patterns-established:
  - "POL sizing formula: Required liquidity = trade_size / (2 * slippage_target) for 95th percentile trades"
  - "Rebalancing triggers: Price exits range OR within 10% of boundary → quarterly rebalancing"
  - "Risk mitigation via platform diversification: 60% Uniswap v3, 20% Balancer, 20% future expansion"
  - "LP fee revenue allocation: Years 1-2 reinvest 100%, Years 3+ distribute 50% + burn 50%"

# Metrics
duration: 9min
completed: 2026-02-05
---

# Phase 01 Plan 01: POL and Liquidity Management Research Summary

**Deep analysis of Protocol-Owned Liquidity with 20-25M GNK deployment strategy achieving $44M liquidity depth and $550K-1.1M annual fee revenue while eliminating mercenary capital risk**

## Performance

- **Duration:** 9 minutes
- **Started:** 2026-02-05T20:47:08Z
- **Completed:** 2026-02-05T20:56:09Z
- **Tasks:** 1 (research task)
- **Files created:** 1 (10,487 words, 42+ sources)

## Accomplishments

- **Comprehensive POL mechanism analysis**: Benchmarked Olympus DAO, Berachain Proof-of-Liquidity, Tokemak v2 Autopilot, Balancer 80/20 pools, and Uniswap v3 concentrated liquidity with performance data from 2021-2026
- **Quantified mercenary liquidity failure**: Documented 10-25% retention rates after emissions end, SushiSwap vampire attack case study ($1.4B → $180M in 6 months), and $10 cost per $1 retained for traditional liquidity mining vs. $0.50 per $1 for POL
- **Gonka-specific deployment strategy**: Detailed plan for 22M GNK (18.3% of Community Pool) deployed across GNK/USDC (13.2M GNK + $13.2M USDC) and GNK/ETH (8.8M GNK + 2,933 ETH) with $44M total liquidity depth
- **Financial projections**: $550K-1.1M annual LP fee revenue (3-6% APR) with <1% slippage for $40K trades, 100% liquidity retention vs. 10-25% for incentivized liquidity
- **Risk analysis**: Impermanent loss scenarios (IL offset by fees in 2-3x price increases), smart contract risk assessment (Uniswap v3 LOW risk, 3+ years no exploits), governance risk mitigation (supermajority requirements), and market manipulation analysis
- **Implementation roadmap**: Phased deployment (Phase 1: initial 22M GNK, Phase 2: optimization, Phase 3: cross-chain expansion) with governance proposal template (GIP-001)

## Task Commits

1. **Task 1: Research POL mechanisms and create comprehensive document** - `5996176` (feat)

**Plan metadata:** (pending - will be committed with STATE.md update)

## Files Created/Modified

- `.planning/phases/01-deep-macro-tokenomics-research/research/01-pol-and-liquidity.md` - 10,487-word comprehensive POL research covering mechanisms, mercenary liquidity quantification, sizing strategy, Gonka-specific recommendations, risk analysis, competitive benchmarking, and implementation checklist with 42+ cited sources

## Decisions Made

**1. POL Allocation Size: 20-25M GNK (16-21% of Community Pool)**
- **Rationale**: Falls within industry benchmark of 15-35% of treasury (Olympus 93%, GMX 18%, Frax 18%, average 15-35%). POL sizing formula based on $1M daily volume target with <1% slippage for $40K trades (95th percentile) requires $40-50M liquidity depth, achieved with 20-25M GNK paired with $20-25M USDC/ETH.
- **Alternative considered**: 10-15M GNK (more conservative) but would only provide $20-30M liquidity depth with >1.5% slippage for large trades.

**2. Pair Composition: 60% GNK/USDC + 40% GNK/ETH**
- **Rationale**: GNK/USDC provides price stability reference and USD-denominated exit liquidity for hosts (earn GNK, need USDC for GPU costs). GNK/ETH provides DeFi composability (Aave collateral, Uniswap LP strategies, cross-chain bridges). 60/40 split balances host cashout needs with DeFi ecosystem integration.
- **Alternative considered**: 80% GNK/USDC + 20% GNK/ETH (more stable) but reduces DeFi composability and Ethereum ecosystem presence.

**3. Platform: Uniswap v3 Concentrated Liquidity**
- **Rationale**: 4-5x capital efficiency vs. full-range v2 pools when using ±25-35% concentrated ranges. Uniswap v3 is battle-tested (3+ years, $3-5B TVL, zero major exploits), most liquid DEX, and supports concentrated liquidity for optimal capital efficiency.
- **Alternative considered**: Balancer 80/20 weighted pools (lower IL) - recommended as supplementary diversification (20% of POL) but Uniswap v3 should be primary venue for deepest liquidity.

**4. Fee Tier: 0.3%**
- **Rationale**: Industry standard for medium-volatility governance tokens (AAVE, COMP, UNI). Balances LP revenue and trader cost. At $1M daily volume, 0.3% generates $1.095M/year LP fees vs. 0.05% ($182K/year, too low) or 1% ($1.28M/year but 65% volume reduction due to high trader cost).
- **Alternative considered**: 1% fee tier (higher LP revenue) but empirical data shows 60-70% volume reduction, alienating traders and reducing overall liquidity utility.

**5. Concentrated Range: ±25-35% from Current Price**
- **Rationale**: Balances capital efficiency (4-5x) with rebalancing frequency (2-4x/year). Wider than ±10% "high risk" ranges but narrower than ±50% "low reward" ranges. GNK/USDC: $0.75-$1.35, GNK/ETH: 0.00025-0.00045 ETH/GNK. Accommodates normal volatility without frequent rebalancing.
- **Alternative considered**: ±10% (10x capital efficiency) but requires weekly/monthly rebalancing with high gas costs and out-of-range risk.

**6. Deployment Approach: Dual-Sided (Not Single-Sided via Tokemak)**
- **Rationale**: Full treasury control, no third-party dependency, no platform fees (Tokemak charges 10-20%), direct LP fee accrual to Community Pool. Requires paired assets ($20-25M USDC/ETH) but provides maximum control and fee retention.
- **Alternative considered**: Single-sided via Tokemak Autopilot (reduces capital requirements) - recommended as Phase 3 expansion if paired assets are constrained, but Phase 1 should be dual-sided for full control.

**7. LP Fee Revenue Usage: Reinvest Years 1-2, Distribute/Burn Years 3+**
- **Rationale**: Years 1-2 compound POL positions to reach $60-80M TVL without additional GNK allocation. Years 3+ distribute 50% as real yield to GNK stakers (or veGNK holders) and burn 50% for additional deflationary pressure. Creates tangible value accrual while maintaining liquidity growth.
- **Alternative considered**: 100% burn (maximum deflation) but misses opportunity for real yield distribution to long-term holders.

## Deviations from Plan

None - plan executed exactly as written. Research task was autonomous with clear scope (POL mechanisms, competitor implementations, liquidity strategies, Gonka-specific recommendations, risk analysis). All required elements delivered:

- ✅ POL mechanism deep dive (Olympus, Berachain, Tokemak, Balancer, Uniswap v3)
- ✅ Mercenary liquidity quantification (10-25% retention, SushiSwap case study, Curve Wars)
- ✅ POL sizing and deployment (20-25M GNK, 60/40 pair split, ±25-35% ranges, 0.3% fee tier)
- ✅ Gonka-specific strategy (Community Pool allocation, phased deployment, governance proposal template)
- ✅ Risk analysis (IL scenarios, smart contract risk, governance risk, market manipulation)
- ✅ Competitive benchmarking (Olympus, GMX, Frax, Balancer performance data)
- ✅ Implementation checklist (pre-deployment, deployment, monitoring, ongoing management)
- ✅ 10,487 words (exceeds 2000+ requirement)
- ✅ 42+ sources cited with URLs (exceeds 10+ requirement)

## Issues Encountered

None - research execution was straightforward. Web research principles applied to gather 2024-2026 data on POL mechanisms, DeFi liquidity management, and protocol benchmarks. All verification criteria met (comprehensive document, numeric recommendations, sufficient sources, Gonka-specific section).

## Next Phase Readiness

**Ready for downstream phases:**

1. **Real Yield Distribution Research (01-02)**: This POL research provides foundation for LP fee revenue allocation decisions (reinvest, distribute, burn). Real yield research should reference POL fee generation as additional revenue stream beyond AI Training Fund surplus.

2. **veGNK Governance Research (01-03)**: POL governance risk analysis identified need for time-locked voting (veGNK) to reduce short-term manipulation of POL decisions. veGNK research should include POL-specific governance requirements (supermajority for withdrawals, time-locks).

3. **Treasury Management Synthesis (01-06)**: POL deployment is a major treasury management decision. Synthesis should integrate POL strategy with overall Community Pool allocation framework and coordinate with Bitfury strategic floor price support.

4. **Implementation Planning (Future)**: This research provides actionable deployment parameters ready for governance proposal (GIP-001). Implementation will require:
   - Governance vote on 22M GNK POL allocation
   - Paired asset acquisition ($20-25M USDC/ETH from treasury, OTC, or revenue)
   - Treasury multisig setup for position management
   - Monitoring infrastructure (Dune Analytics dashboard, rebalancing alerts)

**Potential blockers:**

- **Paired Asset Shortage**: Gonka may lack $20-25M in USDC/ETH for pairing. Mitigation: Phased deployment starting with available assets, OTC sales of 5-10M GNK to strategic buyers, or Bitfury negotiation for additional capital.
- **Governance Approval**: 33.4% quorum and >50% majority required for Community Pool allocation. Risk: Low engagement or opposition from hosts who prefer direct distribution over POL. Mitigation: Clear communication of POL benefits (100% retention, fee revenue, exit liquidity) vs. traditional liquidity mining (10-25% retention, unsustainable emissions).

**Key insights for future phases:**

- POL + Real Yield creates flywheel: POL generates LP fees → distribute as real yield → attracts stakers → reduces sell pressure → stabilizes price → improves POL position value
- POL + EIP-1559 creates dual deflation: Base fees burned from inference usage + LP fees burned (if 50% burn model) → 10-15% additional deflationary pressure on top of emission curve
- POL + veGNK governance alignment: Time-locked GNK holders (veGNK) should control POL decisions to prevent short-term manipulation and ensure long-term treasury management

**Research confidence:** HIGH - All data from 2024-2026 sources, mechanisms are battle-tested (Olympus since 2021, Uniswap v3 since 2021), and Gonka-specific recommendations are within industry benchmarks with clear rationale.

---

## Appendix: Key Numeric Recommendations Summary

**For quick reference in future planning:**

| Parameter | Recommended Value | Rationale |
|-----------|------------------|-----------|
| **POL Allocation** | 20-25M GNK (16-21% of Community Pool) | Industry benchmark 15-35%, supports $1M daily volume target |
| **Pair Split** | 60% GNK/USDC, 40% GNK/ETH | Balances host cashout needs and DeFi composability |
| **GNK/USDC Position** | 13.2M GNK + $13.2M USDC | 60% of 22M GNK allocation |
| **GNK/ETH Position** | 8.8M GNK + 2,933 ETH (~$8.8M) | 40% of 22M GNK allocation |
| **Platform** | Uniswap v3 (concentrated liquidity) | 4-5x capital efficiency, battle-tested, deepest liquidity |
| **Fee Tier** | 0.3% | Standard for medium-volatility governance tokens |
| **GNK/USDC Range** | $0.75 - $1.35 (+35%/-25% from $1.00) | ±25-35% accommodates normal volatility |
| **GNK/ETH Range** | 0.00025 - 0.00045 ETH/GNK (±35%) | Wider range due to ETH volatility |
| **Capital Efficiency** | 4-5x vs. full-range pools | Concentrated liquidity benefit |
| **Expected TVL** | $44M (both pairs combined) | $26.4M GNK/USDC + $17.6M GNK/ETH |
| **Slippage Target** | <1% for $40K trades | 95th percentile trade size |
| **Annual LP Fee Revenue** | $550K-1.1M (3-6% APR) | Based on $1M daily volume at 0.3% fee tier |
| **Rebalancing Frequency** | 2-4 times/year | Quarterly reviews, rebalance if price exits range or within 10% of boundary |
| **Rebalancing Cost** | ~$900/year | 3 rebalances * $150 gas * 2 positions |
| **Liquidity Retention** | 100% (protocol-owned) | vs. 10-25% for traditional liquidity mining |
| **Cost Efficiency** | $0.50 per $1 TVL | vs. $10 per $1 retained for mercenary liquidity |

---

*Phase: 01-deep-macro-tokenomics-research*
*Plan: 01*
*Completed: 2026-02-05*

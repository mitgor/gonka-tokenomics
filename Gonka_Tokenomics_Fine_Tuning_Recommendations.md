# Gonka Network: Tokenomics Fine-Tuning Recommendations

**Version:** 1.4 (Updated)
**Date:** July 18, 2026 (original: February 5, 2026)
**Status:** Decision-Ready
**Prepared by:** Phase 1 Deep Macro-Tokenomics Research Program

---

## July 2026 Update Note

This document was written in February 2026 against Q1-2026 market assumptions. Key facts have changed materially and are corrected inline throughout:

- **GNK price:** GNK now has a live tracked price of ~$0.13 (July 17-18, 2026; market cap ~$13.9M, ~106M of 1B circulating), after an all-time high of $2.61 (January 16, 2026) and all-time low of $0.1258 (July 17, 2026) -- a ~95% drawdown. GNK is still not listed on a major CEX; it trades OTC on HEX Exchange, on SafeTrade (GNK/USDT), and as wrapped GNK. All $1.00-GNK-anchored figures in this document are modeling assumptions, not market prices.
- **Market regime:** Crypto is in a pronounced bear phase (total market cap ~$2.26T, down ~43% from the October 2025 high; BTC ~$64,000 with sustained ETF outflows). The "severe bear" contingency scenario in Recommendation 7 is approximately the live base case.
- **Competitive moat:** Akash activated Burn-Mint Equilibrium (March 23, 2026) and io.net's Incentive Dynamic Engine went live (June 11, 2026) -- though independent analysis of io.net's own explorer indicates its burn is currently emission-funded rather than the marketed revenue buyback, with demand-driven emissions still switched off. Buyback-and-burn is no longer a marketing differentiator, but *revenue-funded* value return -- and especially yield distribution to lockers -- still is.
- **GPU market:** B200 shipped at the start of 2025, not Q3 2026, and H100 rental deflation stalled and partially reversed in 2026 (AI memory supercycle). The supercycle is decelerating from Q2's ~60% QoQ pace but the deceleration is being revised upward: TrendForce raised its Q3/Q4 forecasts on July 8-9, 2026 (PC DRAM Q3 now +15-20% QoQ, up from 8-13%; server DRAM +13-18% with US CSP long-term agreements capping increases), and module maker ADATA reportedly sees Q3 DRAM up 20-30% and NAND up 35-40%. The 13-18% figure is now the conservative end, not the consensus -- GPU-hardware-cost relief in 2027 looks less likely. GPU pricing sections are corrected inline.
- **Network size:** Live ecosystem sources now publish real-time network stats (gonka.gg with a free public API, gonkascan.com, gonkahub.com, tracker.gonka.vip). As of July 18, 2026, joingonka.ai's live counter shows ~1,178 GPUs active, consistent with tracker.gonka.vip's ~1,214 -- far below the April 2026 snapshot of ~4,648 GPUs (~113 participants, ~582 MLNodes) and CoinMarketCap's static "~5,000 H100" project description (stale marketing text; the announced February 2026 peak was ~14,000). The ~1,200 live figure is the correct active-mining denominator. The February 2026 figures used in this document's baseline modeling (6,000 GPUs, 448 hosts) match no live source; per-GPU emission share at ~1,200 GPUs is ~5x the 6,000-GPU baseline, which lowers host break-even GNK price by the same factor.
- **Protocol security:** A security hotfix, v0.2.13-post7 (July 6, 2026), patched a PoC-v2 weight-validation vulnerability; per the official network-updates feed, host gonka1w7s4pharl5qs2lupxkuw2c0gzcls8chehwafg3 was detected exploiting the flaw before the fix deployed -- the network's first publicly disclosed live exploit attempt. The v0.2.14 chain upgrade is still an open PR (since July 8, 2026) and is not just "in preparation": it adds PoC duplicate-artifact protection and deprecates the classic API -- disabling billing on /v1/chat/completions -- routing all paid inference through the devshard/broker path, which changes the fee-infrastructure picture modeled here (see Appendix, Network Parameters).
- **Regulatory:** The 2026 SEC "Project Crypto" posture (staff taxonomy statement, token safe-harbor direction) materially lowers the securities-risk differential assigned to direct veGNK yield. The SEC's "Regulation Crypto" proposal is confirmed for its July 2026 rulemaking slot -- a time-limited "Innovation Exemption" allowing raises up to $75M in any 12-month period, a 12-36 month safe harbor, and an exit-from-securities mechanism -- but it is still under White House OIRA review, and an operative rule is quarters away (proposal, comment period, final rule, compliance dates). Reported eligibility criteria target early-stage projects (valuation under $5M within the first four years), which Gonka (mcap ~$14M, launched 2025) may not satisfy. The CLARITY Act sits at Senate Calendar No. 423 with no cloture motion and, as of July 17-18, no floor vote actually scheduled: bipartisan talks on ethics/law-enforcement provisions collapsed, prediction-market odds of passage fell from the low 70s to roughly 43%, and the July 17 event was only a House Financial Services field hearing (messaging, not legislation). The bill still needs ~7 Democratic votes for cloture, with Aug 7 the final session day before recess -- treat passage as a coin-flip, not imminent. Separately, July 18, 2026 was the statutory deadline for six federal agencies (OCC, FDIC, Treasury, FinCEN, et al.) to finalize stablecoin implementing rules under the GENIUS Act -- relevant to treasury/POL planning (USDC pairing legality and yield treatment) and to the stablecoin-yield dispute that is one of the blocks on CLARITY.
- **Timelines:** Calendar targets set in February 2026 (e.g., "Q2 2026") that have passed without implementation should be read as offsets from adoption, not fixed dates.

---

## 1. Executive Summary

This document delivers 10 prioritized, parameterized recommendations for fine-tuning Gonka Network's tokenomics. The recommendations synthesize findings from five parallel deep research investigations covering protocol-owned liquidity, real yield mechanisms, vote-escrowed governance, fee transition stress testing, and GPU market economics -- drawing on 50+ sources, 12 protocol analyses, and academic research originally current to February 2026, with market facts updated to July 18, 2026.

**Top 3 Critical Recommendations:**

1. **Fee Transition Monitoring & Contingency Framework** (CRITICAL, immediate) -- Deploy a real-time dashboard tracking the emission-to-fee crossover ratio and host profitability. Under conservative growth (10% annual developer growth), fee revenue does not exceed emission value until Year 4 at a modeled $1.00 GNK; at the actual July 2026 price of ~$0.13, hosts earn well below the document's own ~$0.85 breakeven estimate (a Feb 2026 figure computed on a 6,000-GPU baseline; the live network runs ~1,200 active GPUs as of July 18, 2026, so per-GPU emission share is ~5x higher and breakeven correspondingly lower -- roughly ~$0.17 on the same math -- meaning ~$0.13 GNK sits only modestly below breakeven for active hosts, though still short of rental parity). If Year 4 fee revenue falls below $50M, activate tail emission contingency. This is the single largest existential risk to network sustainability.

2. **Protocol-Owned Liquidity Deployment** (HIGH, upon adoption) -- Allocate 22M GNK (18.3% of Community Pool) to Uniswap v3 concentrated liquidity positions, 60% GNK/USDC and 40% GNK/ETH. The original sizing (13.2M GNK paired with $13.2M USDC; $40-45M total depth) assumed $1.00 GNK; at ~$0.13 GNK (July 2026), 22M GNK is worth ~$2.9M and all dollar targets, paired-asset amounts, and price ranges must be rebased to the live price before the governance vote. The structural case is unchanged: <1% slippage at the 95th-percentile trade size and cost efficiency of $0.50 deployed per $1 TVL versus $10 spent per $1 retained under traditional liquidity mining.

3. **Enhanced Revenue Allocation with Real Yield** (HIGH, upon adoption) -- Restructure the current 10% unallocated inference revenue into 5% continuous TWAP buyback-and-burn plus 5% real yield distribution to veGNK stakers. At $25M annual inference revenue, this generates $1.25M in buyback pressure and $1.25M+ in staker yield. Buyback-and-burn is no longer unique among AI compute networks -- Akash activated Burn-Mint Equilibrium in March 2026 and io.net's IDE buyback-and-burn went live in June 2026 (though io.net's burn is currently emission-funded, not revenue-funded) -- but direct distribution of real revenue to lockers remains rare, and is now the moat to emphasize.

**Decision Framework:** Implement Phase A (quick wins) immediately to establish monitoring and demand-side growth. Phase B (core enhancements) requires smart contract development and governance votes. Phase C (advanced features) builds on Phase B infrastructure. Calendar targets from the February 2026 draft have slipped; read phase timelines as offsets from adoption.

**Fee Transition Risk Summary:** Gonka's exponential emission decay (halving every ~4 years) means epoch rewards drop from 323,000 GNK/day at launch to 71,929 GNK/day by Year 8. Under conservative growth, fee revenue crosses over epoch reward value at Year 4 (modeled $1 GNK) to Year 8-9 (modeled $5 GNK); at the actual ~$0.13 GNK (July 2026), the crossover sits beyond even the conservative case. The critical danger zone is Year 8-12 when emissions become negligible but fee revenue may not yet dominate. Mitigation: aggressive developer onboarding (targeting 25% annual growth), oracle-based USD pricing to stay competitive, and governance-activated tail emissions as a backstop.

---

## 2. Methodology

**Research Program:** Five parallel deep research investigations executed February 2026:

| Investigation | Scope | Output |
|---|---|---|
| POL & Liquidity Management | Olympus, Berachain, Tokemak, Balancer, Uniswap v3; mercenary liquidity quantification | 10,487 words, 42+ sources |
| Real Yield & Buybacks | GMX, Gains, Aave, Synthetix, Lido, Hyperliquid, MakerDAO, BNB, Curve, Frax, Sushi; 12 protocols | 7,716 words, 12 protocol analyses |
| veToken & Governance | Curve, Convex, Velodrome, Balancer, PancakeSwap, Frax; quadratic voting, Sybil resistance, governance attacks | 10,882 words, 6 protocol deep-dives |
| Fee Transition Stress Test | Bitcoin, Ethereum, Bittensor, Filecoin, Akash; 3-scenario modeling, EIP-1559 sensitivity | 8,839 words, academic papers |
| GPU Economics & Developer Growth | GPU deflation modeling, competitive pricing, developer acquisition, floor defense, oracle integration | 8,306 words, 40+ sources |

**Synthesis:** Findings integrated into three updated reference documents (Macro Research v2.0, Deep Analysis v3.0, Stakeholder Guide v3.0) before distillation into these recommendations.

**Date of Research:** February 2026, with a fact-check pass on July 18, 2026. GNK price, GPU market pricing, competitor tokenomics, regulatory posture, and protocol-version facts are updated to July 2026 where verified; modeled figures (crossover years, POL sizing at $1.00 GNK, budget estimates) remain February 2026 estimates and are labeled as such.

---

## 3. Recommendation Matrix

| # | Recommendation | Priority | Complexity | Impact | Timeline | Dependencies |
|---|---|---|---|---|---|---|
| 1 | Fee Transition Monitoring & Contingency | CRITICAL | LOW | HIGH | Immediate | None |
| 2 | Protocol-Owned Liquidity (POL) | HIGH | MEDIUM | HIGH | Q2 2026 | Governance vote, paired assets |
| 3 | Enhanced Revenue Allocation (Buyback + Yield) | HIGH | MEDIUM | HIGH | Q3 2026 | Smart contract, veGNK (partial) |
| 4 | Developer Onboarding Acceleration | HIGH | LOW | HIGH | Immediate | Marketing budget |
| 5 | Oracle-Based USD Pricing | HIGH | MEDIUM | HIGH | Q2-Q3 2026 | Pyth/Chainlink integration |
| 6 | veGNK Governance (Phase 1) | MEDIUM-HIGH | HIGH | HIGH | Q3-Q4 2026 | Smart contract audit |
| 7 | GNK Floor Price Defense | MEDIUM | MEDIUM | MEDIUM | Q3 2026 | Oracle, treasury USDC |
| 8 | EIP-1559 Parameter Optimization | MEDIUM | LOW | MEDIUM | Q3 2026 | Testnet validation |
| 9 | GPU Pricing Competitive Tracking | MEDIUM | LOW | MEDIUM | Immediate | Off-chain infrastructure |
| 10 | veGNK Advanced Features (Phase 2-3) | LOW-MEDIUM | HIGH | MEDIUM | 2027 | veGNK Phase 1 live |

**Reading the matrix:** Priority reflects urgency and risk mitigation value. Complexity reflects implementation effort. Impact reflects expected effect on network health, token value, and sustainability. Timeline entries are the original February 2026 calendar targets; those already passed (Q2 2026) should be re-planned as offsets from adoption.

---

## 4. Detailed Recommendations

---

### Recommendation 1: Fee Transition Monitoring & Contingency Framework

**Priority:** CRITICAL | **Timeline:** Immediate | **Complexity:** LOW

#### Current State

Gonka's emission schedule decays exponentially at rate 0.000475 per epoch from 323,000 GNK/day initial. Live explorers now publish real-time participant/GPU counts (gonka.gg with a free public API, gonkascan.com, gonkahub.com, tracker.gonka.vip), but no monitoring infrastructure exists to track the emission-to-fee crossover ratio, host profitability thresholds, or early warning indicators. The network has no contingency plan if fee revenue growth lags projections. The proposed dashboard should build on the existing explorer APIs rather than new data collection.

#### Proposed Enhancement

**Deploy a real-time monitoring dashboard and governance-activated contingency framework.**

**Dashboard Metrics (deploy within 30 days):**

| Metric | Formula | Warning Threshold | Critical Threshold |
|---|---|---|---|
| Fee Revenue Ratio | `Annual_Fee_Revenue / (Annual_Fee_Revenue + Annual_Emission_Value)` | <40% at Year 4 | <25% at Year 6 |
| Host Profitability Index | `(Emission_Revenue + Fee_Revenue) / Traditional_Rental_Revenue` | <1.5x | <1.0x |
| Developer Growth Rate | `New_Active_Devs / Prior_Period_Active_Devs - 1` | <10% annual | <5% annual |
| Network Utilization | `Active_GPU_Hours / Total_Available_GPU_Hours` | <30% | <15% |
| GNK Breakeven Price | `(Host_Cost - Fee_Income) / Daily_GNK_Earned` | >$2.00 | >$5.00 |

**Contingency Triggers (governance-approved thresholds):**

- **Trigger A** -- Year 4 fee revenue < $50M (vs. $96.9M conservative baseline): Activate enhanced developer subsidies (8M GNK/year from Community Pool)
- **Trigger B** -- Host churn > 20% annually for 2 consecutive quarters: Activate host efficiency programs and consider tail emissions
- **Trigger C** -- Fee growth < 5% annually for 2 consecutive years after Year 6: Governance vote on tail emissions (10,000 GNK/day, ~0.36% annual inflation)

**Tail Emission Design (contingency only):**

- Rate: 10,000 GNK/day (3.1% of initial emission rate)
- Duration: 5-year activation, then re-vote
- Distribution: Same PoC-weighted allocation as mining rewards
- Inflation: 0.36% annually at 1B supply -- below Ethereum PoS (~4-6%)

#### Expected Impact

- Early detection of fee transition risks 12-24 months before they become critical
- Governance has pre-approved contingency actions, reducing reaction time from months to days
- Host confidence increases when they can see profitability projections on-chain

#### Implementation Complexity

- Dashboard: Off-chain analytics (Dune Analytics or equivalent), 2-4 weeks development
- Contingency framework: Governance proposal document, no smart contract required initially
- Tail emission: Smart contract modification if activated, estimated 4-6 weeks development + audit

#### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Dashboard data inaccurate | Low | Medium | Cross-validate with on-chain data, multiple data sources |
| Contingency triggers too conservative | Medium | Low | Governance can adjust thresholds via standard vote |
| Tail emission creates moral hazard | Low | Medium | Time-limited activation, declining rate, requires supermajority |

#### Success Metrics

| KPI | Target | Measurement |
|---|---|---|
| Dashboard live | Within 30 days | Deployment confirmation |
| Contingency proposal approved | Within 60 days | Governance vote passed |
| Fee Revenue Ratio at Year 2 | >30% | Dashboard metric |
| Developer Growth Rate | >15% annual | Active developer count |

---

### Recommendation 2: Protocol-Owned Liquidity (POL)

**Priority:** HIGH | **Timeline:** Q2 2026 | **Complexity:** MEDIUM

#### Current State

Gonka has a 120M GNK Community Pool with no protocol-owned liquidity. All market liquidity depends on external market makers and exchange listings. Traditional liquidity mining retains only 10-25% of incentivized liquidity after emissions cease and costs $10 per $1 of retained TVL.

#### Proposed Enhancement

**Allocate 22M GNK from Community Pool to concentrated Uniswap v3 positions.**

> **July 2026 recalibration:** The pair structure below was sized at a modeled $1.00 GNK. At the live ~$0.13 GNK price, 22M GNK is worth ~$2.9M, so the dollar amounts of paired assets, the absolute price ranges, and the depth/fee-revenue targets in this recommendation must be rebased to the prevailing price before the governance vote. The allocation percentages, fee tiers, and range widths (relative +-25/+35%) remain the recommendation.

**Pair Structure (February 2026 sizing at $1.00 GNK):**

| Pair | Allocation | GNK Amount | Paired Asset | Fee Tier | Range | Capital Efficiency |
|---|---|---|---|---|---|---|
| GNK/USDC | 60% | 13,200,000 GNK | $13,200,000 USDC | 0.3% | -25%/+35% around spot ($0.75-$1.35 at $1.00) | 4.2x vs. full range |
| GNK/ETH | 40% | 8,800,000 GNK | ~2,933 ETH (~$8.8M) | 0.3% | +-35% from current ratio | 3.8x vs. full range |

**GNK/USDC rationale:** Primary pair for price discovery and host cashouts. Hosts earn GNK and need USDC to cover GPU electricity and hardware costs. Lower IL exposure for the protocol treasury.

**GNK/ETH rationale:** DeFi composability pair. Enables GNK use as collateral on Aave/Compound, cross-chain bridge liquidity, and attracts Ethereum-native liquidity providers.

**Rebalancing Parameters:**

- Frequency: Quarterly or when price exits range (estimated 2-4 times/year)
- Cost: ~$900/year in gas (0.16% of LP fee revenue -- negligible)
- Trigger: Price within 10% of range boundary or price exits range
- Execution: Treasury multisig with governance oversight

**Paired Asset Sourcing Strategy:**

| Source | Amount | Timeline | Mechanism |
|---|---|---|---|
| Protocol revenue (first 6 months) | $2-5M | Months 1-6 | Accumulate from early inference fees |
| OTC negotiation with Bitfury | $5-10M | Pre-deployment | Negotiate USDC/ETH from strategic partner |
| Governance-approved Community Pool sale | $5-10M | If needed | Sell 5-10M GNK OTC for paired assets; the SEC's Innovation Exemption (raises up to $75M per 12 months) might eventually open a compliant public-sale route, but the rule is still at OIRA (operative rule quarters away) and reported eligibility limits (valuation under $5M within four years) may exclude Gonka -- do not plan around it |
| Phase 1 partial deployment | Deploy with available assets | Immediate | Start with whatever paired assets exist |

**Governance Proposal (GIP-001) Structure:**

- Quorum: 33.4% of total supply
- Majority: >50% approval
- Vote period: 7 days
- Execution: Within 30 days of approval

#### Expected Impact

- $40-45M total liquidity depth across both pairs (Feb 2026 sizing at $1.00 GNK; ~$5.8M at $0.13 GNK unless the allocation is enlarged)
- <1% slippage on $40K trades (95th percentile trade size, Feb 2026 estimate)
- $550K-$1.1M annual LP fee revenue (3-6% APR on deployed capital; scales with rebased TVL)
- 100% liquidity retention (vs. 15-25% for mercenary capital)
- Cost efficiency: $0.50 per $1 TVL (20x cheaper than traditional LM)

#### Implementation Complexity

- No smart contract development required (uses existing Uniswap v3 infrastructure)
- Governance proposal drafting: 1-2 weeks
- Paired asset acquisition: 2-8 weeks (depends on source)
- Deployment execution: 1-2 days
- Monitoring dashboard: 1-2 weeks (Dune Analytics)

#### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Impermanent loss on GNK price decline | Medium | Medium | Concentrated ranges limit exposure; 80/20 Balancer pool as diversification option |
| Paired asset shortage (USDC/ETH) | Medium-High | Medium | Phased deployment, OTC negotiation, partial start |
| Governance rejection | Low | High | Clear communication: POL retains 100% vs. 15-25% for LM; $0.50/$ vs $10/$ |
| Smart contract exploit (Uniswap v3) | Very Low | High | Uniswap v3 audited, $100B+ TVL track record |

#### Success Metrics

| KPI | Target | Timeline |
|---|---|---|
| TVL deployed | $40-45M | Month 3 post-vote |
| Daily trading volume | $500K-$1M | Month 6 |
| LP fee revenue (annualized) | $550K-$1.1M | Month 6 |
| Slippage for $40K trade | <1% | Immediate post-deployment |
| Rebalancing frequency | <4x/year | Year 1 |

---

### Recommendation 3: Enhanced Revenue Allocation (Buyback + Real Yield)

**Priority:** HIGH | **Timeline:** Q3 2026 | **Complexity:** MEDIUM

#### Current State

Gonka's current inference revenue allocation is 70% hosts / 20% AI Training Fund / 10% unallocated. The 10% unallocated creates no value. The AI Training Fund accumulates indefinitely with no surplus mechanism. No buyback or staking yield exists.

#### Proposed Enhancement

**Restructure revenue to 70/20/5/5 with surplus distribution.**

```
Inference Revenue: 100%
  |-- 70% -> Hosts (UNCHANGED)
  |-- 20% -> AI Training Fund (UNCHANGED)
  |       |-- [Surplus above 6-month runway] -> veGNK holders (bonus real yield)
  |-- 5%  -> GNK Buyback-and-Burn (NEW: continuous TWAP, burn all purchased GNK)
  |-- 5%  -> veGNK Staker Yield Pool (NEW: weekly claim in GNK or USDC)

Base Fee: 100% BURNED (UNCHANGED -- EIP-1559 mechanism)
```

**Buyback Mechanism Parameters:**

| Parameter | Value | Rationale |
|---|---|---|
| Allocation | 5% of inference revenue | Meaningful at scale, conservative at launch |
| Execution | Continuous TWAP, 15-minute intervals, 96 buys/day | Minimizes front-running and slippage |
| Max slippage per order | 0.5% | Prevents adversarial MEV extraction |
| Minimum order size | $10 | Avoids dust transactions |
| Destination | Burn address (0x0...dead) | Permanent supply reduction |
| Dip-buying acceleration | 3x normal rate when GNK >20% below 30-day TWAP | Opportunistic accumulation |
| Governance pause | 33.4% quorum + >50% majority; auto-resumes after 30 days | Emergency override |

**AI Training Fund Surplus Design (MakerDAO Surplus Buffer model):**

| Parameter | Value |
|---|---|
| Runway target | 6 months of average monthly expenses |
| Surplus calculation | `Fund_Balance - (Monthly_Expenses x 6)` |
| Distribution eligibility | veGNK holders only (proportional to veGNK balance) |
| Distribution frequency | Weekly |
| Governance adjustable | Runway target (3-12 months) via standard vote |

**Revenue Impact at Scale:**

| Annual Revenue | Host Share (70%) | AI Fund (20%) | Buyback-Burn (5%) | Yield Pool (5%) |
|---|---|---|---|---|
| $5M | $3.5M | $1.0M | $250K | $250K |
| $25M | $17.5M | $5.0M | $1.25M | $1.25M |
| $100M | $70M | $20M | $5M | $5M |
| $500M | $350M | $100M | $25M | $25M |

**Competitive Advantage (updated July 2026):** Buyback-and-burn is no longer a marketing differentiator. Akash activated Burn-Mint Equilibrium via Mainnet 17 on March 23, 2026 -- all on-chain compute spend triggers a market buy-and-burn of AKT. io.net's Incentive Dynamic Engine went live June 11, 2026 (announced alongside an $8M enterprise deal, ~$650K/month), marketed as committing at least 50% of surplus revenue to IO buyback-and-burn and targeting >=12M IO removed in year one -- but independent analysis of io.net's own explorer indicates the burn is currently emission-funded rather than revenue-funded, with demand-driven emissions still switched off. Render has long used burn-mint equilibrium; Bittensor remains purely emission-based. What remains genuinely rare is *routing real revenue to lockers*: none of these networks pay protocol revenue to token lockers, and the largest marketed "revenue" burn is not yet revenue-backed. Gonka's 5% veGNK yield pool funded by actual inference revenue -- not the 5% burn -- is the moat, and messaging should lead with it.

#### Expected Impact

- At $25M annual revenue: 1.25M GNK burned/year (0.125% supply reduction) + $1.25M staker yield
- Combined with base fee burns: potential net deflationary by Year 3-5
- Reflexive value loop: more revenue -> more burns -> higher price -> more revenue
- veGNK staker APR: 5-15% real yield (competitive with GMX, Curve, Aave)

#### Implementation Complexity

- Smart contract: Buyback engine (TWAP contract), yield distribution contract, surplus calculation
- Estimated development: 8-12 weeks
- Audit required: Yes (handles protocol funds)
- External dependency: DEX liquidity (Uniswap v3 GNK pair must exist -- ties to Recommendation 2)

#### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Regulatory classification as security | Low (further reduced by 2026 SEC posture) | High | 2026 SEC "Project Crypto" (Jan 28 staff taxonomy statement, Mar 17 token safe-harbor direction) largely classifies governance/utility tokens sold for use as "digital tools," not securities. The SEC's July 2026 "Regulation Crypto" rulemaking (Innovation Exemption up to $75M/12mo, 12-36 month safe harbor, exit-from-securities mechanism) would further de-risk direct veGNK yield, but is still at OIRA with an operative rule quarters away, and its early-stage eligibility criteria may exclude Gonka. CLARITY Act: no floor vote scheduled as of July 17-18 after ethics-provision talks collapsed; passage odds ~43% with Aug 7 the last session day -- maintain conservative positioning until rules or statute are final. Note also the GENIUS Act stablecoin implementing rules (six-agency finalization deadline July 18, 2026), which bear on USDC yield treatment |
| Buyback front-running | Low | Low | Continuous TWAP with 15-min intervals makes front-running unprofitable |
| AI Training Fund underfunded | Low | Medium | 6-month runway threshold ensures operational reserves before any distribution |
| Revenue too low for meaningful buyback | Medium (early) | Low | Mechanism scales automatically; even small burns compound over time |

#### Success Metrics

| KPI | Target | Timeline |
|---|---|---|
| Buyback active | Continuous execution | Month 1 post-launch |
| Annual GNK burned (buyback) | >0.1% of supply | Year 1 |
| veGNK staker APR | 5-15% | Year 1 (depends on revenue) |
| Net deflationary status | Burns > emissions | Year 3-5 |

---

### Recommendation 4: Developer Onboarding Acceleration

**Priority:** HIGH | **Timeline:** Immediate | **Complexity:** LOW

#### Current State

Gonka has ~2,200 active developers (Feb 2026 estimate; not verifiable against July 2026 live sources). Fee transition analysis reveals that 15-25% annual developer growth is required to maintain host profitability as emissions decay. The OpenAI-compatible API reduces migration friction to near-zero (change 2 lines of code), but no structured onboarding program exists.

#### Proposed Enhancement

**Launch a 3-phase developer acquisition program targeting 25,000 active developers within 36 months.**

**Phase 1: Foundation (Months 1-6) -- Budget: 1.85M GNK**

| Initiative | Budget | Expected Outcome | Cost/Developer |
|---|---|---|---|
| Free tier (100 inferences/day) | 500K GNK | 5,000 signups, 500 active | $50-100 |
| "OpenAI to Gonka in 5 Minutes" migration guide | 50K GNK | 1,000 migrations | $25-50 |
| Hackathon sponsorship (3 events) | 300K GNK | 300 active builders | $500 |
| $50 compute credits per new developer | 1M GNK | 2,000 claimants | $50 |

**Phase 2: Growth (Months 7-18) -- Budget: 1.7M GNK**

| Initiative | Budget | Expected Outcome | Cost/Developer |
|---|---|---|---|
| Developer grants (10 x $25K) | 500K GNK | 50 high-value builders | $5,000 |
| University program (20 institutions) | 200K GNK | 2,000 student developers | $50 |
| LangChain/LlamaIndex official integration | 300K GNK | 5,000 framework users | $30 |
| Enterprise pilot program (20 companies) | 500K GNK | 20 enterprise accounts | $12,500 |
| Referral program ("bring a friend") | 200K GNK | 2,000 referred developers | $50 |

**Phase 3: Scale (Months 19-36) -- Budget: 5M GNK**

| Initiative | Budget | Expected Outcome |
|---|---|---|
| Ecosystem fund for 100+ projects | 5M GNK | 10,000+ organic developers |
| Self-service growth (network effects) | Minimal | Accelerating organic adoption |

**Cumulative Targets:**

| Milestone | Active Developers | Growth Rate |
|---|---|---|
| Month 6 | 6,000 | 173% (from 2,200 base) |
| Month 18 | 15,000 | 150% |
| Month 36 | 25,000 | 67% |

**Total Budget:** 8.55M GNK (~7.1% of Community Pool)
**Blended Acquisition Cost:** $150-500 per active developer (in line with 2026 benchmarks)
**Marketing Message:** "Same API. 70% Less Cost. Censorship-Resistant."

#### Expected Impact

- 25% annual developer growth sustains moderate fee transition scenario
- $50 free credits generate 12x ROI if developers convert to paid usage
- LangChain/LlamaIndex integration unlocks 100K+ existing framework users as potential Gonka users
- Enterprise pilots at $12,500/customer generate $100K+ lifetime value

#### Implementation Complexity

- Free tier: Configuration change, minimal development
- Migration guide: Documentation effort, 1-2 weeks
- Compute credits: Smart contract or manual distribution, 2-4 weeks
- Enterprise program: Business development, ongoing

#### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Free tier abuse (bots, farming) | Medium | Low | Rate limiting, progressive verification |
| Low conversion from free to paid | Medium | Medium | Generous free tier proves value before paywall |
| Enterprise sales cycle too long | High | Low | Focus on self-service growth first; enterprise is supplementary |

#### Success Metrics

| KPI | Target | Timeline |
|---|---|---|
| Monthly active developers | 6,000 | Month 6 |
| Free-to-paid conversion | >5% | Month 6 |
| Monthly inference volume growth | >10% MoM | Ongoing |
| Developer NPS (satisfaction) | >50 | Month 12 |

---

### Recommendation 5: Oracle-Based USD Pricing

**Priority:** HIGH | **Timeline:** Q2-Q3 2026 | **Complexity:** MEDIUM

#### Current State

Gonka prices inference in GNK terms via EIP-1559 dynamic pricing. This creates a dual volatility problem: GPU rental prices move independently of GNK, which fluctuates with market sentiment. (The Feb 2026 assumption of 30-50% annual GPU deflation no longer holds -- H100 rental deflation stalled and partially reversed in 2026 amid the AI memory supercycle, with centralized clouds raising prices. Volatility now cuts both ways, which strengthens rather than weakens the case for USD-denominated pricing.) When GNK appreciates, Gonka becomes uncompetitive in USD terms. When GNK depreciates -- as through mid-2026, with GNK at ~$0.13 -- hosts earn less in USD terms.

#### Proposed Enhancement

**Implement oracle-based USD pricing with GNK settlement.**

**Architecture:**

```
Developer Request -> Gonka Pricing Engine:
  1. Pull GNK/USD from Pyth Network (400ms latency)
  2. Look up base price in USD (governance-set, competitive with market)
  3. Apply EIP-1559 multiplier (utilization-based adjustment)
  4. Convert USD price to GNK using real-time oracle rate
  5. Developer pays GNK amount, receives inference
```

**Oracle Stack (Hybrid):**

| Layer | Source | Latency | Use Case |
|---|---|---|---|
| GNK/USD Price Feed | Pyth (primary) + Chainlink (fallback) | 400ms / 1hr heartbeat | Per-inference pricing conversion |
| GPU Market Rate Feed | Custom off-chain aggregator -> Pyth publisher | Hourly | Base price calibration |
| Floor Defense Price Feed | Chainlink (primary) + Pyth (confirmation) | 1hr + deviation-triggered | Trigger evaluation |
| Competitive Benchmark | UMA Optimistic Oracle | Weekly | Governance pricing decisions |

**Target Pricing (H100-equivalent, USD/hr, July 2026 market):**

| Position | Target $/hr | Rationale |
|---|---|---|
| Aggressive growth | $1.50-2.00 | Undercuts the July 2026 market median ($2.29-3.12); maximizes developer acquisition |
| Balanced (recommended) | $2.00-2.50 | At/just below market median with host profitability |
| Premium decentralized | $2.50-3.00 | Emphasize reliability and API quality |

**Competitive Positioning (July 2026 H100 market):**

```
Hyperscaler on-demand ($7-8/hr, Azure/AWS) <- Enterprise, compliance-heavy
Market median ($2.29-3.12/hr)              <- Specialized clouds, mainstream supply
[GONKA TARGET] ($2.00-2.50)                <- Cost-optimized, API-compatible, censorship-resistant
Budget decentralized ($1.40-1.99/hr)       <- Spot/best-effort (floor: Thunder Compute ~$1.40)
```

Note: the Feb 2026 draft targeted the same $2.00-2.50 band against a then-deflating market. With deflation stalled and the latest cohort median at ~$3.15/hr (AIMultiple, July 2026) -- mild firming, not just stabilization -- this band is now at-to-below market, and the aggressive tier may be needed to preserve a clear cost advantage.

#### Expected Impact

- Eliminates dual volatility problem entirely
- Developers see stable USD pricing regardless of GNK price movements
- Hosts earn competitive USD-equivalent revenue regardless of GNK volatility
- EIP-1559 now adjusts the USD-denominated base (not GNK-denominated), making convergence faster and more meaningful

#### Implementation Complexity

- Pyth integration: 2-4 weeks (SDK available)
- Chainlink feed creation: 4-8 weeks (requires partnership or self-funded feed)
- Pricing engine modification: 4-6 weeks
- GPU market rate aggregator: 2-4 weeks (off-chain service)
- Total estimated: 3-5 months

#### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Oracle manipulation | Very Low | High | Dual-oracle (Pyth + Chainlink) with deviation checks |
| Oracle downtime | Low | Medium | Chainlink 1hr heartbeat as fallback; cache last known price |
| GNK/USD feed doesn't exist yet | High | Medium | Self-fund Pyth publisher or negotiate Chainlink partnership |

#### Success Metrics

| KPI | Target | Timeline |
|---|---|---|
| Oracle integration live | Pyth + Chainlink | Month 4 |
| Price deviation from USD target | <5% at all times | Ongoing |
| Developer price complaints | Zero "too expensive" reports from GNK appreciation | Ongoing |

---

### Recommendation 6: veGNK Governance (Phase 1)

**Priority:** MEDIUM-HIGH | **Timeline:** Q3-Q4 2026 | **Complexity:** HIGH

#### Current State

Gonka uses 1-token-1-vote governance. The 200M founder allocation (20% of supply) could dominate governance. Current system is vulnerable to flash loan governance attacks (buy tokens, vote, sell). No mechanism aligns governance power with long-term commitment.

#### Proposed Enhancement

**Deploy veGNK: vote-escrowed GNK with linear time-weighted voting power.**

**Phase 1 Parameters (Q3-Q4 2026):**

| Parameter | Value | Rationale |
|---|---|---|
| Minimum lock | 1 month (30 days) | Filters transient holders; lower barrier than Curve's 1 week |
| Maximum lock | 2 years (730 days) | Aligns with AI infrastructure planning cycles; extend to 4 years in Phase 2 if adoption strong |
| Voting power formula | `veGNK = GNK_locked x (lock_time_remaining / 730 days)` | Linear decay, proven in 90% of ve protocols |
| Early exit | Not permitted | Maximum commitment, prevents gaming |
| Transferability | Non-transferable | Prevents vote buying on secondary markets |
| Collateral separation | veGNK does NOT count as host collateral | Clean separation; locked GNK cannot be slashed |
| Max boost (Phase 2) | 2.5x on AI Training Fund yield | Standard across ve protocols (Curve, Balancer) |

**veGNK Voting Power Example:**

| GNK Locked | Lock Duration | veGNK Received | Voting Power |
|---|---|---|---|
| 1,000 GNK | 2 years (max) | 1,000 veGNK | Full |
| 1,000 GNK | 1 year | 500 veGNK | 50% |
| 1,000 GNK | 6 months | 250 veGNK | 25% |
| 1,000 GNK | 1 month (min) | ~42 veGNK | 4.2% |

**Founder Allocation Impact:**

| Scenario | Founder veGNK | % of Total veGNK (if 40% lock rate) | Assessment |
|---|---|---|---|
| Founders don't lock | 0 | 0% | Community controls governance |
| Founders lock 1 year | 100M veGNK | 33% of ~300M total | Significant but not dominant |
| Founders lock 2 years (max) | 200M veGNK | 67% of ~300M total | Problematic -- needs monitoring |

**Mitigation:** Encourage broad GNK distribution before veGNK launch. Implement delegation so community can aggregate voting power. Monitor governance concentration; consider voluntary founder lock caps.

> **July 2026 -- delegation concentration is now a demonstrated risk, not a theoretical one.** The July 15, 2026 network update issued explicit guidance "Do not delegate to guardian nodes" after concentrated guardian delegations caused Kimi K2.6 to lose validation majority (epochs 328-329). Guardians are now positioned as fallback-only, and the protocol team is pushing delegation distribution across independent hosts as a systemic-risk mitigation. Any veGNK delegation design (here and in Rec #10) must inherit this constraint: cap or disincentivize delegation to guardian/genesis entities and monitor delegate concentration from day one.

**Governance Changes:**

| Parameter | Current | With veGNK |
|---|---|---|
| Quorum | 33.4% of total GNK | 33.4% of total veGNK |
| Majority | >50% of votes | >50% of veGNK votes |
| Veto | >33.4% of votes | >33.4% of veGNK votes |
| Flash loan vulnerability | HIGH (buy, vote, sell) | ZERO (can't borrow locked tokens) |

#### Expected Impact

- 35-50% of circulating GNK locked as veGNK (benchmark: 40% average across ve protocols)
- Flash loan governance attacks become impossible
- Long-term holders gain proportionally more voting power
- Real yield distribution (Rec #3) to veGNK holders creates lock-up flywheel

#### Implementation Complexity

- Smart contract development: 8-12 weeks (veGNK locking contract, voting integration)
- Security audit: 4-6 weeks (critical -- handles locked user funds)
- Governance transition: 2-4 weeks (migrate from token-weighted to veGNK-weighted)
- Total: 4-6 months

#### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Low adoption (<20% lock rate) | Medium | Medium | Strong real yield incentive from Rec #3; minimum 1-month lock is low barrier |
| Governance concentration by founders | Medium | High | Monitor lock distribution; implement delegation; voluntary caps |
| Smart contract bug in veGNK | Low | Very High | Formal verification, multiple audits, time-locked upgrade path |
| User confusion | Medium | Low | Clear documentation, phased rollout, community education |

#### Success Metrics

| KPI | Target | Timeline |
|---|---|---|
| veGNK deployed | Contract live on mainnet | Q4 2026 |
| Lock rate | >25% within 6 months | Q2 2027 |
| Average lock duration | >8 months | Q2 2027 |
| Governance participation | >15% of veGNK voting on proposals | Q2 2027 |
| Flash loan attacks | Zero | Ongoing |

---

### Recommendation 7: GNK Floor Price Defense

**Priority:** MEDIUM | **Timeline:** Q3 2026 | **Complexity:** MEDIUM

#### Current State

Bitfury purchased $12M GNK at $0.60 (20M GNK) as the first tranche of a $50M total investment commitment announced December 1, 2025 (framed publicly as the opening of a ~$1B plan to decentralize AI compute). The $0.60 purchase price created a psychological Schelling point -- which has since decisively failed: GNK fell through $0.60, through both proposed trigger levels ($0.45, $0.30), to an all-time low of $0.1258 on July 17, 2026. No programmatic floor defense mechanism exists, and the sustained bear market this recommendation treated as a tail scenario is now the live base case. All absolute trigger levels below must be reset against current market conditions, and the remaining ~$38M of Bitfury's commitment should be factored into treasury and defense planning.

#### Proposed Enhancement

**Deploy a treasury-managed, rules-based TWAP buyback mechanism with tiered triggers.**

**Trigger Architecture** (absolute levels are Feb 2026 values, already breached; reset relative to prevailing price at deployment -- the TWAP-relative triggers remain valid as designed):

| Tier | Trigger Condition | Daily Buyback Rate | Max Duration |
|---|---|---|---|
| Tier 1 | GNK < 75% of 30-day TWAP | 0.5% of defense treasury/day | 30 days |
| Tier 2 | Absolute floor (was $0.45; reset at deployment) OR < 60% of 30-day TWAP | 1.0% of defense treasury/day | 60 days |
| Tier 3 | Crisis floor (was $0.30; reset at deployment) | 2.0% of defense treasury/day | 90 days |
| Emergency | Governance vote | Up to 5% of total treasury | As voted |

**Treasury Allocation:**

| Source | Annual Amount | Purpose |
|---|---|---|
| Community Pool conversion | Up to 6M GNK/year (5%) | Convert to USDC for buyback treasury |
| Inference revenue share | 5-10% of net revenue | Ongoing floor defense funding |
| Target treasury balance | 2-5M USDC equivalent | 6-12 months of Tier 1 defense capacity |

**Execution Parameters:**

| Parameter | Value |
|---|---|
| Execution method | 24-hour TWAP, hourly sub-orders |
| Execution venue | GNK/USDC pool (Uniswap v3) |
| Slippage limit | 1% per sub-order |
| Price ceiling | Do not buy above trigger price (prevents buying into recovery) |
| Purchased GNK | Burn (governance can override to lock) |
| Transparency | All triggers and transactions on-chain, public dashboard |

**Floor Defense is a Speed Bump, Not a Wall:**

- Mild correction (-20%): Defense holds, treasury spends $50-100K, price recovers
- Moderate bear (-40%): Defense slows decline, treasury spends $300-500K
- Severe bear (-60%+, 6+ months): Treasury depleted, defense fails -- fundamentals must improve. **This is the live scenario as of July 2026** (GNK ~95% off its January 2026 high; total crypto market cap down ~43% year-over-year); treasury-depletion estimates must be recalibrated against it before deployment
- Stop conditions: Treasury < 20% of initial allocation, or buyback spending > 3 months of revenue

#### Expected Impact

- Replaces the failed $0.60 Schelling point with programmatic, transparent backing at recalibrated levels
- Slows price declines during market stress, providing time for fundamentals to recover
- On-chain transparency builds market confidence
- Purchased GNK is burned, creating permanent supply reduction during downturns

#### Implementation Complexity

- Smart contract: TWAP buyback engine, trigger evaluation, treasury vault -- 6-8 weeks
- Oracle dependency: Chainlink GNK/USD feed required (ties to Rec #5)
- Audit: Required (handles treasury funds)
- Total: 3-4 months

#### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Treasury depletion in prolonged bear | Medium | High | Stop conditions, governance override, revenue replenishment |
| Trigger manipulation (oracle attack) | Very Low | High | Dual-oracle validation, 30-day TWAP smoothing |
| Community opposition to selling GNK for USDC | Medium | Medium | Clear ROI analysis: $0.50 floor defense cost vs. $10 for re-acquiring liquidity |

#### Success Metrics

| KPI | Target | Timeline |
|---|---|---|
| Floor defense deployed | Contract live | Q3 2026 |
| Treasury funded | >$2M USDC | Q3 2026 |
| GNK price above recalibrated Tier 2 floor | 100% of time post-deployment | Ongoing |
| Defense activations per year | <4 | Year 1 |

---

### Recommendation 8: EIP-1559 Parameter Optimization

**Priority:** MEDIUM | **Timeline:** Q3 2026 | **Complexity:** LOW

#### Current State

Gonka's EIP-1559 implementation uses +-2% per-block adjustment with a 40-60% stability zone. Academic research (Ethereum Foundation) finds optimal adjustment rates between 6-11%, indicating Gonka's +-2% is conservative. At +-2%, convergence to equilibrium takes ~40 blocks; at +-4%, only ~20 blocks.

#### Proposed Enhancement

**Test and deploy +-4% adjustment rate on mainnet after 6-month baseline data collection.**

**Parameter Comparison:**

| Parameter Set | Convergence Speed | Volatility | Developer UX | Recommendation |
|---|---|---|---|---|
| +-2% (current) | 40 blocks | Low | Excellent | Keep as default for first 6 months |
| +-4% (proposed) | 20 blocks (50% faster) | Moderate | Good | Deploy after testnet validation |
| +-6% | 14 blocks | Moderate-High | Fair | Reserve for high-volume periods only |
| Asymmetric +4%/-2% | Fast up, slow down | Moderate | Good | Consider if demand is bursty |

**Implementation Roadmap:**

| Phase | Timeline | Action |
|---|---|---|
| Baseline | Month 0-6 | Collect convergence data at +-2% |
| Testnet | Month 6-9 | A/B test +-4% vs +-2% on testnet with simulated load |
| Governance proposal | Month 9 | Present data, propose +-4% upgrade |
| Mainnet deployment | Month 10+ | Deploy if governance approves |
| Adaptive (future) | Year 2+ | +-2% baseline, +-4-6% during extreme utilization |

#### Expected Impact

- 50% faster fee market convergence during demand spikes
- Better responsiveness to GPU market price moves in either direction (EIP-1559 adjusts faster to competitive pressure)
- Acceptable volatility increase (within Ethereum Foundation's stable range)

#### Implementation Complexity

- Configuration change: Single parameter update in consensus code
- Testnet validation: 4-8 weeks of testing
- No smart contract changes required

#### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Higher fee volatility annoys developers | Low | Low | Still well within Ethereum's 6-11% optimal range |
| Overshoot during demand spikes | Low | Low | 4% is conservative end of optimal range |

#### Success Metrics

| KPI | Target | Timeline |
|---|---|---|
| Convergence time | <25 blocks (from 40) | Post-deployment |
| Fee stability (coefficient of variation) | <15% | Ongoing |
| Developer churn from pricing | Zero attributable | Ongoing |

---

### Recommendation 9: GPU Pricing Competitive Tracking

**Priority:** MEDIUM | **Timeline:** Immediate | **Complexity:** LOW

#### Current State

No systematic tracking of competitor GPU pricing exists -- and 2026 has shown why it matters: after collapsing 64-81% over 2023-2025, H100 rental deflation stalled and partially reversed. As of July 2026 the H100 market median is $2.29-3.12/hr (range ~$1.40 budget to ~$7-8 hyperscaler on-demand), with the most recent cohort data (AIMultiple GPU index, July 2026) putting the median at ~$3.15/hr -- at or slightly above the top of the band, i.e., mild firming rather than pure stabilization. Drivers: the AI memory supercycle (decelerating from Q2's ~60% QoQ, but TrendForce raised its Q3/Q4 DRAM forecasts on July 8-9, so the 13-18% floor is now the conservative end) and surging inference demand. B200 -- which shipped at the start of 2025, not Q3 2026 as the original draft assumed -- rents for $2.69-16.11/hr (median ~$6.25); H200 cohort median is ~$4.11/hr ($2.30 FluidStack to $13.78 Azure). Blackwell accounts for >70% of NVIDIA high-end shipments (led by GB300/B300). Vera Rubin is slightly delayed (KeyBanc, mid-July 2026: thermal heat-lid issues and SK Hynix HBM4 qualification; Rubin's share of 2026 shipments cut from ~29% to ~22%, and the four-die Rubin Ultra reportedly cancelled/scaled back), though standard Rubin mass shipments to eight cloud partners remain on track for this summer -- less 2026 Rubin supply supports continued firmness in H100/H200/B200 rental prices. Without competitive tracking, Gonka risks being mispriced in either direction without realizing it.

#### Proposed Enhancement

**Deploy an off-chain pricing aggregator that tracks 10+ GPU providers and publishes weekly competitive reports.**

**Tracked Providers:**

| Category | Providers | Data Points |
|---|---|---|
| Hyperscalers | AWS, Azure, GCP | On-demand, reserved, spot pricing per GPU |
| Specialized | CoreWeave, Lambda Labs | On-demand, commitment pricing |
| Decentralized | Akash, Vast.ai, RunPod, io.net | Spot, on-demand pricing |
| API providers | OpenAI, DeepSeek, Anthropic | Per-token pricing for comparable models |

**Output:**

| Deliverable | Frequency | Audience |
|---|---|---|
| Competitive pricing dashboard | Real-time (hourly updates) | Internal team, governance |
| Weekly competitive report | Weekly | Governance, community |
| GPU Price Index | Daily | Oracle feed (future, Rec #5) |
| EIP-1559 base price recommendation | Monthly | Governance vote |

**Phase 2 (Month 6+):** Feed GPU pricing data to Pyth Network as custom publisher for on-chain integration with oracle-based pricing (Rec #5).

#### Expected Impact

- Early warning when Gonka becomes uncompetitive
- Data-driven EIP-1559 base price calibration
- Foundation for automated oracle-based pricing (Rec #5)

#### Implementation Complexity

- Off-chain service: 2-3 weeks development (API scraping, aggregation)
- Dashboard: 1-2 weeks (web interface)
- Operational cost: Minimal (API calls, hosting)

#### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Provider API changes | Medium | Low | Monitor and update scrapers; multiple redundant sources |
| Data accuracy | Low | Medium | Cross-validate across providers; flag outliers |

#### Success Metrics

| KPI | Target | Timeline |
|---|---|---|
| Dashboard live | Tracking 10+ providers | Month 1 |
| Weekly reports published | Consistent cadence | Ongoing |
| Pricing action taken from data | At least 1 governance proposal | Quarter 1 |

---

### Recommendation 10: veGNK Advanced Features (Phase 2-3)

**Priority:** LOW-MEDIUM | **Timeline:** 2027 | **Complexity:** HIGH

#### Current State

veGNK Phase 1 (Rec #6) provides basic locking and voting. Advanced features (boost mechanics, delegation, quadratic voting for specific decisions) are not included in Phase 1 to reduce launch risk.

#### Proposed Enhancement

**Phase 2 (Q1-Q2 2027) -- Boost + Delegation:**

| Feature | Specification |
|---|---|
| Yield boost | 1x-2.5x multiplier on AI Training Fund yield based on veGNK/staked GNK ratio |
| Delegation | veGNK holders can delegate voting power to trusted representatives |
| Delegation trigger | Implement only if governance participation < 10% of veGNK |
| Max lock extension | Consider extending max lock from 2 years to 4 years based on Phase 1 adoption data |

**Phase 3 (Q3-Q4 2027) -- Advanced Governance:**

| Feature | Specification |
|---|---|
| Host-gated quadratic voting | `votes = sqrt(GNK_held)` for Community Pool allocation decisions only |
| Sybil resistance | GPU host identity (verified by Sprint Consensus) as identity layer |
| Scope limitation | Quadratic voting only for host-specific governance (not protocol-wide) |
| Standard voting | veGNK linear voting remains default for all non-host decisions |

**Quadratic Voting Limitation:** Quadratic voting is only viable with Sybil resistance. Gonka's GPU host identity provides natural Sybil resistance (creating fake hosts requires buying real GPUs). Quadratic voting is therefore limited to host-gated decisions where GPU ownership serves as identity.

#### Expected Impact

- Boost mechanics drive veGNK lock rate from 25% to 40-50%
- Delegation increases effective governance participation
- Quadratic voting reduces whale dominance in Community Pool decisions
- 4-year max lock (if adopted) increases average lock duration and supply reduction

#### Implementation Complexity

- Boost contract: 4-6 weeks
- Delegation: 2-4 weeks
- Quadratic voting with host identity: 8-12 weeks (complex Sybil resistance integration)
- Multiple audits required
- Total: 6-9 months for full Phase 2-3

#### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Boost gaming | Medium | Low | veGNK/staked ratio prevents easy manipulation |
| Delegation centralization | Medium-High (demonstrated: July 2026 guardian-delegation incident, epochs 328-329) | Medium | Monitor delegate concentration; cap maximum delegated power; exclude or cap guardian/genesis entities as delegates per the July 15, 2026 network guidance |
| Quadratic voting Sybil attack | Low (host-gated) | Medium | GPU hardware requirement makes Sybil expensive |
| Complexity deters users | Medium | Low | Excellent documentation, phased rollout, simple UI |

#### Success Metrics

| KPI | Target | Timeline |
|---|---|---|
| veGNK lock rate with boost | >40% | 6 months post Phase 2 |
| Delegation adoption | >20% of veGNK delegated | 6 months post Phase 2 |
| Governance participation | >25% of veGNK voting | 6 months post Phase 2 |

---

## 5. Implementation Roadmap

### Phase A: Quick Wins (0-3 Months)

**Investment:** Low | **Impact:** Demand-side growth foundation and monitoring

| Action | Recommendation | Week | Deliverable |
|---|---|---|---|
| Deploy fee transition dashboard | Rec #1 | 1-4 | Live dashboard with all monitoring metrics |
| Launch developer free tier | Rec #4 | 1-2 | 100 free inferences/day for new signups |
| Publish "OpenAI to Gonka" migration guide | Rec #4 | 2-4 | Documentation + live API playground |
| Deploy GPU pricing tracker | Rec #9 | 2-5 | Dashboard tracking 10+ providers |
| Distribute $50 compute credits | Rec #4 | 4-8 | Credit distribution to 2,000 developers |
| Draft GIP-001 (POL governance proposal) | Rec #2 | 4-8 | Proposal ready for community vote |
| Submit contingency framework for governance approval | Rec #1 | 4-8 | Pre-approved trigger thresholds |
| Sponsor first hackathon | Rec #4 | 8-12 | 100+ developer participants |

**Phase A Expected Outcomes:**
- 3,500-4,000 active developers (from 2,200)
- Fee transition monitoring operational
- POL governance vote in progress
- GPU competitive positioning understood

### Phase B: Core Enhancements (3-9 Months)

**Investment:** Medium | **Impact:** Sustainable economic model

| Action | Recommendation | Month | Deliverable |
|---|---|---|---|
| Execute POL deployment (post-governance vote) | Rec #2 | 3-4 | $40-45M liquidity deployed |
| Integrate Pyth + Chainlink oracle stack | Rec #5 | 3-5 | GNK/USD price feeds live |
| Deploy oracle-based USD pricing engine | Rec #5 | 5-7 | USD-denominated inference pricing |
| Deploy buyback-and-burn smart contract | Rec #3 | 5-7 | Continuous TWAP buyback active |
| Deploy veGNK Phase 1 contract | Rec #6 | 6-9 | Locking + voting live on mainnet |
| Deploy yield distribution contract | Rec #3 | 7-9 | veGNK stakers earning real yield |
| Deploy floor price defense contract | Rec #7 | 7-9 | Tiered TWAP defense active |
| Testnet +-4% EIP-1559 | Rec #8 | 6-9 | A/B test results |
| Launch LangChain/LlamaIndex integration | Rec #4 | 6-9 | Official SDK support |
| Launch university program (20 institutions) | Rec #4 | 6-9 | 2,000 student developers |

**Phase B Expected Outcomes:**
- 8,000-10,000 active developers
- POL generating $550K-$1.1M annual fee revenue
- Buyback engine actively burning GNK
- veGNK live with >15% initial lock rate
- Floor defense operational with $2M+ treasury
- Oracle-based pricing eliminates dual volatility

### Phase C: Advanced Features (9-18 Months)

**Investment:** High | **Impact:** Long-term alignment and decentralization

| Action | Recommendation | Month | Deliverable |
|---|---|---|---|
| Deploy +-4% EIP-1559 on mainnet | Rec #8 | 9-10 | Faster fee convergence |
| Deploy veGNK Phase 2 (boost + delegation) | Rec #10 | 12-15 | 2.5x yield boost, delegation |
| Launch enterprise pilot program | Rec #4 | 12-18 | 20 enterprise accounts |
| Deploy host-gated quadratic voting | Rec #10 | 15-18 | QV for Community Pool decisions |
| Custom Pyth GPU pricing publisher | Rec #9 | 12-15 | On-chain GPU pricing |
| Evaluate max lock extension to 4 years | Rec #10 | 15-18 | Governance proposal if data supports |

**Phase C Expected Outcomes:**
- 15,000-20,000 active developers
- veGNK lock rate at 35-50%
- Governance fully decentralized (flash loan proof, time-weighted)
- Enterprise revenue stream established
- Full oracle stack operational

---

## 6. Risk Matrix

| # | Recommendation | Risk | Probability | Impact | Mitigation |
|---|---|---|---|---|---|
| 1 | Fee Monitoring | Monitoring fails to predict transition risk | Low | High | Multiple data sources, conservative thresholds |
| 1 | Fee Monitoring | Tail emission philosophical opposition | Medium | Medium | Time-limited activation, declining rate, community education |
| 2 | POL | Impermanent loss in bear market | Medium | Medium | Concentrated ranges, diversified pairs, fee revenue offsets IL |
| 2 | POL | Paired asset shortage (USDC/ETH) | Medium-High | Medium | Phased deployment, OTC negotiation, partial start |
| 2 | POL | Governance rejects POL allocation | Low | High | ROI analysis: 100% retention vs 15-25%, $0.50 vs $10 per $1 |
| 3 | Revenue | Regulatory classification as security | Low (reduced by 2026 SEC "Project Crypto" posture and pending July 2026 safe-harbor rulemaking) | High | Position yield as governance/utility participation; track the SEC's July 2026 proposed rules (still at OIRA; operative rule quarters away) and the CLARITY Act (no vote scheduled as of July 17-18; passage odds ~43%) for final certainty |
| 3 | Revenue | Revenue too low for meaningful impact | Medium (early) | Low | Mechanism scales automatically; compound over time |
| 4 | Developers | Free tier abuse | Medium | Low | Rate limiting, progressive verification |
| 4 | Developers | Growth targets missed | Medium | High | Multiple channels, adjust budgets, extend timeline |
| 5 | Oracle | Oracle manipulation | Very Low | High | Dual-oracle validation, deviation checks, TWAP smoothing |
| 5 | Oracle | GNK/USD feed creation delays | High | Medium | Self-fund Pyth publisher; use off-chain interim |
| 6 | veGNK | Low adoption (<20% lock rate) | Medium | Medium | Real yield incentive, minimum 1-month barrier |
| 6 | veGNK | Governance concentration by founders | Medium | High | Monitor, delegation, voluntary caps |
| 6 | veGNK | Smart contract vulnerability | Low | Very High | Formal verification, multiple audits, time-locked upgrades |
| 7 | Floor Defense | Treasury depletion in prolonged bear | Medium | High | Stop conditions, governance override, revenue replenishment |
| 7 | Floor Defense | Market interprets floor defense as weakness | Low | Medium | Transparent on-chain triggers signal stability, not crisis |
| 8 | EIP-1559 | Higher volatility annoys developers | Low | Low | +-4% is conservative end of optimal 6-11% range |
| 9 | GPU Tracking | Competitor data becomes unavailable | Medium | Low | Multiple redundant sources; manual fallback |
| 10 | veGNK Adv. | Complexity deters adoption | Medium | Low | Phased rollout, excellent documentation, simple UI |

---

## 7. Dependencies and Sequencing

### Dependency Graph

```
[Rec #1: Fee Monitoring]  -----> No dependencies (IMMEDIATE)
[Rec #4: Developer Growth] ----> No dependencies (IMMEDIATE)
[Rec #9: GPU Tracking]    -----> No dependencies (IMMEDIATE)

[Rec #2: POL]             -----> Governance vote, paired assets
                                   |
[Rec #5: Oracle Pricing]  -----> Pyth/Chainlink integration
     |                              |
     v                              v
[Rec #3: Revenue/Buyback]  -----> Requires DEX liquidity (Rec #2)
     |                         -----> Requires oracle (Rec #5, partial)
     |                              |
     v                              v
[Rec #7: Floor Defense]    -----> Requires oracle (Rec #5)
     |                         -----> Requires treasury USDC (Rec #2 process)
     |
     v
[Rec #6: veGNK Phase 1]   -----> Independent but synergistic with Rec #3
     |
     v
[Rec #8: EIP-1559]        -----> 6 months baseline data
     |
     v
[Rec #10: veGNK Phase 2-3] ----> Requires veGNK Phase 1 (Rec #6) live
```

### Critical Path

The critical path runs through oracle integration:

1. **Month 0:** Start Rec #1, #4, #9 (no dependencies)
2. **Month 1-2:** Begin Pyth/Chainlink integration (Rec #5) and POL governance (Rec #2)
3. **Month 3-4:** Deploy POL (Rec #2), completing liquidity prerequisite
4. **Month 4-5:** Oracle live (Rec #5), enabling USD pricing
5. **Month 5-7:** Deploy buyback (Rec #3) and floor defense (Rec #7) -- both need oracle + liquidity
6. **Month 6-9:** Deploy veGNK (Rec #6) -- independent but benefits from Rec #3 yield
7. **Month 9+:** Advanced features (Rec #8, #10) build on Phase B foundation

### Parallelizable Items

| Track | Items | Can Run Simultaneously |
|---|---|---|
| Monitoring Track | Rec #1, #9 | Both start immediately, independent |
| Growth Track | Rec #4 (all phases) | Runs continuously alongside everything |
| Infrastructure Track | Rec #2, #5 | POL and oracle integration in parallel |
| Smart Contract Track | Rec #3, #6, #7 | Sequential (share audit resources) |
| Parameter Track | Rec #8 | Independent, runs after 6-month baseline |

---

## 8. Open Questions for Governance

The following decisions require community governance votes. Recommended voting parameters and discussion timelines are provided.

| # | Decision | Recommended Vote | Quorum | Discussion Period | Impact |
|---|---|---|---|---|---|
| 1 | GIP-001: Allocate 22M GNK to POL | FOR: Deploy as specified. AGAINST: Maintain status quo. | 33.4% | 2 weeks discussion + 7 days voting | Largest single Community Pool allocation |
| 2 | Revenue restructure from 70/20/10 to 70/20/5/5 | FOR: Implement enhanced allocation. AGAINST: Keep 10% unallocated. | 33.4% | 2 weeks discussion + 7 days voting | Activates buyback + yield mechanisms |
| 3 | Contingency trigger thresholds | FOR: Approve triggers A, B, C as specified. AGAINST: No pre-approved contingencies. | 33.4% | 1 week discussion + 7 days voting | Pre-authorizes emergency responses |
| 4 | Floor defense treasury allocation | FOR: Allocate up to 6M GNK/year + 5-10% revenue. AGAINST: No floor defense. | 33.4% | 2 weeks discussion + 7 days voting | Commits treasury to price stability |
| 5 | veGNK deployment approval | FOR: Deploy veGNK with specified parameters. AGAINST: Keep 1-token-1-vote. | 33.4% | 3 weeks discussion + 7 days voting | Fundamental governance change |
| 6 | EIP-1559 +-4% upgrade | FOR: Increase to +-4%. AGAINST: Keep +-2%. | 33.4% | 1 week discussion + 7 days voting | Parameter change after testnet data |
| 7 | Tail emission activation (contingency only) | FOR: Activate 10,000 GNK/day. AGAINST: No tail emissions. | 50% (elevated) | 4 weeks discussion + 14 days voting | Supply cap modification -- requires elevated quorum |

**Suggested Governance Timeline:**

| Month | Governance Actions |
|---|---|
| Month 1-2 | GIP-001 (POL), contingency triggers |
| Month 3-4 | Revenue restructure, floor defense |
| Month 5-6 | veGNK deployment |
| Month 9-10 | EIP-1559 upgrade (after testnet data) |
| As needed | Tail emission (contingency only) |

---

## 9. Appendix: Key Data Points

Quick reference for decision-makers -- the most important numbers from all research.

### Token Supply

| Item | Value |
|---|---|
| Total supply | 1,000,000,000 GNK |
| Mining allocation | 680,000,000 GNK (68%) |
| Community Pool | 120,000,000 GNK (12%) |
| Founder allocation | 200,000,000 GNK (20%) |
| Initial epoch reward | 323,000 GNK/day |
| First halving | ~Year 4 (152,440 GNK/day) |
| Second halving | ~Year 8 (71,929 GNK/day) |
| 90% emitted by | ~Year 10 |

### GNK Market (July 17-18, 2026)

| Item | Value |
|---|---|
| GNK price | ~$0.13 (CoinMarketCap: $0.1307, July 18; aggregators diverge -- Crypto.com $0.1334, Bitget $0.2755, Coinpaprika $0.44, CryptoRank $0.2756 with a conflicting ATL of $0.1462 on Jul 16 -- treat CMC as canonical given thin liquidity) |
| Market cap | ~$13.85M |
| Circulating supply | ~105.9M of 1B max |
| All-time high | $2.61 (January 16, 2026) |
| All-time low | $0.1258 (July 17, 2026) |
| Drawdown from ATH | ~95% |
| Venues | OTC on HEX Exchange; SafeTrade (GNK/USDT); wrapped GNK. No major CEX listing (planned MEXC/Gate listings did not materialize) |

Caution: the fake "Gonka AI" token on Solana (~$0.00005, still live on Phantom/OKX as of July 2026) is unofficial and should not be cited.

### Network Parameters

| Item | Value |
|---|---|
| Participants | ~113 independent participants running ~582 MLNodes (joingonka.ai, April 2026 snapshot; the "448 hosts (Feb 2026)" figure matches no live source and should not be used in income models) |
| GPUs | ~1,178 active (joingonka.ai live counter, July 18, 2026), consistent with tracker.gonka.vip's ~1,214 -- use ~1,200 as the active-mining denominator. April 2026 snapshot was ~4,648; CoinMarketCap's "~5,000 H100" is stale marketing text; announced Feb 2026 peak was ~14,000; Feb 2026 modeling baseline was 6,000 |
| Live data sources | gonka.gg (free public API), gonkascan.com, gonkahub.com, tracker.gonka.vip |
| Developers | ~2,200 (Feb 2026 estimate, unverified in July 2026) |
| EIP-1559 stability zone | 40-60% utilization |
| EIP-1559 adjustment | +-2% per block (current) |
| Governance quorum | 33.4% |
| Host collateral | 0.0625 GNK per nonce |

**Protocol changes since February 2026** (not yet modeled in this document): chain releases v0.2.11 (Mar 19), v0.2.12 (Apr 27), and v0.2.13 (May 20, 2026) shipped the devshard escrow system (MaxEscrowsPerEpoch = 500,000; MaxNonce raised from a hardcoded 20,000 to 1,000,000; broker allowlist), reduced GenesisGuardianMultiplier to 0.33334 (genesis guardian voting power cut from ~34% to ~25%), and added a guardian-controlled emergency switch for devshard inference. Devshard runtime v2 (Jun 15) and v3.0.0 (Jul 9, 2026) introduced a new broker/gateway inference path. Security hotfix v0.2.13-post7 (Jul 6, 2026) -- the latest chain release -- patched a PoC-v2 weight-validation vulnerability after host gonka1w7s4pharl5qs2lupxkuw2c0gzcls8chehwafg3 was detected exploiting it, the network's first publicly disclosed live exploit attempt. The v0.2.14 chain upgrade (PR open for review since Jul 8, 2026) adds PoC duplicate-artifact protection and deprecates the classic API -- disabling billing on /v1/chat/completions -- so all paid inference flows through the devshard/broker path; fee-infrastructure assumptions in Recs #3, #5, and #8 should be re-checked against it once merged. Gonka has also begun regular GiP governance meetings. The July 15, 2026 network update added explicit guidance against delegating to guardian nodes after concentrated guardian delegations cost Kimi K2.6 its validation majority (epochs 328-329) -- guardians are now fallback-only, with delegation distribution across independent hosts pushed as a systemic-risk mitigation. The governance recommendations here (Recs #6, #10) should be re-checked against these live parameters before drafting proposals.

### GPU Market (July 2026)

| Item | Value |
|---|---|
| H100 market median | $2.29-3.12/hr; latest cohort median ~$3.15/hr (AIMultiple, Jul 2026) -- mild firming |
| H100 hyperscaler on-demand (Azure/AWS) | ~$7-8/hr |
| H100 budget decentralized/specialized | $1.40-3.50/hr (floor: Thunder Compute ~$1.40) |
| H100 price decline, 2023-2025 | 64-81% (deflation stalled/partially reversed in 2026) |
| H200 cohort median | ~$4.11/hr ($2.30 FluidStack to $13.78 Azure) |
| B200 (shipped start of 2025) | $2.69-16.11/hr, median ~$6.25 (floor $3.20 Runcrate; spot $2.74 Spheron); expected ~$2.50-3.00 at majors by Q4 2026 (Feb 2026 estimate) |
| NVIDIA high-end mix, 2026 | Blackwell >70% of shipments, led by GB300/B300; Vera Rubin slightly delayed (thermal heat-lid, HBM4 qualification; 2026 share cut ~29% -> ~22%, ~1.7-1.8M units; Rubin Ultra reportedly cancelled/scaled back), standard Rubin mass shipments still on track for summer 2026 |
| Price drivers | AI memory supercycle, decelerating but revised upward (TrendForce Jul 8-9: PC DRAM Q3 +15-20% QoQ, server DRAM +13-18%; ADATA reportedly sees DRAM +20-30%, NAND +35-40%), plus surging inference demand and reduced 2026 Rubin supply |
| GPU market CAGR | 29.4% to $33.9B by 2032 (Feb 2026 estimate, unverified) |

### Fee Transition Crossover Points (modeled scenarios, Feb 2026)

GNK prices below are scenario assumptions, not forecasts. At the actual ~$0.13 GNK (July 2026), crossover falls beyond even the conservative case.

| Scenario | Assumed GNK Price | Crossover Year |
|---|---|---|
| Conservative (10% dev growth) | $1.00 | Year 4 |
| Conservative | $5.00 | Year 8-9 |
| Moderate (25% dev growth) | $1.00 | Year 1 |
| Moderate | $5.00 | Year 3 |
| Aggressive (50% dev growth) | Any | Year 1-2 |

### POL Parameters (Feb 2026 sizing at $1.00 GNK -- rebase to live price; see Rec #2)

| Item | Value |
|---|---|
| Recommended allocation | 22M GNK (18.3% of Community Pool; ~$2.9M at $0.13 GNK) |
| GNK/USDC split | 60% (13.2M GNK) |
| GNK/ETH split | 40% (8.8M GNK) |
| Fee tier | 0.3% (both pairs) |
| Target liquidity depth | $40-45M (at $1.00 GNK) |
| Expected LP fee revenue | $550K-$1.1M/year (at $1.00 GNK sizing) |
| Rebalancing cost | ~$900/year |

### Revenue Allocation

| Item | Value |
|---|---|
| Hosts | 70% of inference revenue (unchanged) |
| AI Training Fund | 20% of inference revenue (unchanged) |
| Buyback-and-burn | 5% of inference revenue (new) |
| veGNK yield pool | 5% of inference revenue (new) |
| Base fee | 100% burned via EIP-1559 (unchanged) |
| Surplus distribution | AI Fund balance > 6-month runway -> veGNK holders |

### veGNK Parameters

| Item | Value |
|---|---|
| Lock range | 1 month to 2 years |
| Voting power | Linear: `GNK x (remaining / max)` |
| Max boost (Phase 2) | 2.5x on yield |
| Early exit | Not permitted |
| Transferability | Non-transferable |
| Collateral separation | veGNK separate from host collateral |
| Expected lock rate | 35-50% at steady state |

### Floor Defense Parameters

| Item | Value |
|---|---|
| Primary trigger | GNK < 75% of 30-day TWAP |
| Absolute trigger | Was $0.45 (Feb 2026) -- breached; reset at deployment |
| Crisis trigger | Was $0.30 (Feb 2026) -- breached; reset at deployment |
| Bitfury Schelling point | $0.60 purchase price -- failed (GNK ATL $0.1258, Jul 17, 2026); Bitfury total commitment is $50M (Dec 1, 2025), of which the $12M purchase was the first tranche |
| Treasury target | 2-5M USDC |
| Annual allocation | Up to 6M GNK + 5-10% revenue |

### Competitive Moats (updated July 2026)

| Moat | Gonka | Competitors |
|---|---|---|
| Yield distribution to lockers | 5% revenue + surplus to veGNK stakers | Still rare: no major AI compute network pays revenue to lockers |
| Buyback/burn | 5% continuous TWAP burn (proposed, revenue-funded) | No longer unique in marketing: Akash BME live Mar 2026; io.net IDE live Jun 2026 (burn currently emission-funded, not revenue-funded); Render burn-mint; Bittensor emissions only |
| OpenAI-compatible API | Full compatibility (2-line migration) | Partial or none |
| Dynamic pricing (EIP-1559) | Automatic utilization-based adjustment | Static or manual pricing |
| Censorship resistance | Decentralized, permissionless | Varies (some centralized) |
| Productive compute | ~100% of GPU cycles for AI tasks | Bitcoin: 0%, Bittensor: ~40% |

---

*This document is the capstone deliverable of Phase 1: Deep Macro-Tokenomics Research, updated July 18, 2026 to reflect verified market, competitive, regulatory, and protocol changes since the February 2026 draft. It is intended as a decision-ready strategy document for Gonka Network leadership. All recommendations have specific parameters, quantified impacts, and implementation timelines. For detailed research backing each recommendation, refer to the five Wave 1 research documents and three updated synthesis documents in the project archive (note: those companion documents predate this update and retain February-April 2026 assumptions).*

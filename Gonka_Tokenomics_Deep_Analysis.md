# GONKA NETWORK
## Deep Tokenomics Analysis & Research Report

**Analysis Date:** January 2026 (Enhanced February 2026; market data and protocol status refreshed as of 2026-07-18)
**Document Version:** 3.5 (2026-07-18)
**Sources:** Official Whitepaper (whitepaper.pdf), Tokenomics Document (tokenomics.pdf), GitHub Repository, CryptoRank, CoinMarketCap, live network explorers (gonka.gg, gonkascan.com, gonkahub.com, tracker.gonka.vip), External Research, Wave 1 Deep Macro-Tokenomics Research (5 parallel investigations, February 2026), July 2026 verification passes

---

## Executive Summary

Gonka Network represents a novel approach to decentralized AI compute infrastructure, positioning itself as the "Bitcoin of AI" with a key differentiator: **~98% of computational resources go to productive AI work** rather than consensus overhead. This analysis examines the tokenomics from three critical perspectives — developers, miners/hosts, and investors — with detailed incentive mechanics, economic cycle analysis, and stress-test scenarios.

**Key Findings:**
- Gonka's economic model creates a dual-income stream for hosts (mining rewards + work fees)
- The system maintains cost competitiveness when GNK trades below ~$10 vs centralized providers
- Host profitability threshold was modeled at ~$0.85 GNK on a 500-GPU network; with GNK at ~$0.13 and ~1,200 GPUs live (Jul 2026 live counters), per-GPU emissions are ~4x better than the earlier ~5,000-GPU assumption implied (break-even nearer ~$0.20 GNK), but hosts still earn below traditional rental rates
- Dynamic EIP-1559-inspired pricing creates natural supply/demand equilibrium
- Collateral system introduces 80/20 weight model with slashing penalties (20% malicious, 10% poor performance)
- 180-epoch grace period for new participants (no collateral required initially)
- Network scale (Jul 2026): the live counters converge on ~1,200 active GPUs — joingonka.ai shows 1,178 GPUs, tracker.gonka.vip ~1,214. Use ~1,200 as the active-mining denominator. CoinMarketCap's static "~5,000 H100 GPUs" project description is stale marketing text; joingonka.ai's April 2026 snapshot of ~4,648 GPUs across ~113 independent participants (~582 MLNodes) is also superseded; the widely cited ~14,000 H100-eq (announced Feb 2, 2026) was the announced peak. Nodes span ~20 countries; H100/H200/A100-class GPUs >80% of compute; ~40 supported GPU models (unofficial). The live model lineup (as of Jul 16, 2026) is **MiniMax M2.7** (sole PoC/base delegation model since Jun 25, 2026, Proposal 78), **GLM-5.2** (live Jun 26, 2026, Proposal 79; optional, weight factor 2.47), and **Kimi K2.6** (re-bootstrapping from epoch 331 after its second removal in three weeks — see Section 0.4). Qwen3-235B-A22B was retired from the network on Jun 25, 2026

**Market Status (as of 2026-07-18):**
- **GNK price:** ~$0.13 (CoinMarketCap), market cap ~$13.9M, circulating ~106M of 1B max; all-time high $2.61 (Jan 16, 2026), all-time low $0.1258 (Jul 17, 2026) — a ~95% drawdown
- **Liquidity:** Still not listed on major CEXs (CoinMarketCap: "not yet listed on major centralized exchanges"); 24h volume ~$33K per CMC (~$59K per Crypto.com; BitMart runs a GNK price page reporting ~$9.2K across "4 active markets," spot tradability unconfirmed); trades OTC on HEX Exchange and on SafeTrade (GNK/USDT). Wrapped-GNK routes should be treated with caution: a Solana token labeled "Gonka AI (GNK)" trades at ~$0.00005 (~2,500x below real GNK) and is almost certainly an unofficial impostor listing, while aggregator price feeds diverge wildly (CMC $0.13, CryptoRank $0.2756 — with a different ATL of $0.1462 on Jul 16, 2026 — Bitget $0.28, Coinpaprika $0.44); treat CMC as canonical given the thin liquidity. Do not cite Solana/PumpSwap listings
- **Macro backdrop:** Crypto is in a pronounced bear phase — total market cap ~$2.26T (down ~43% YoY from the Oct 2025 ~$4.27T high), BTC ~$64,000, sustained ETF outflows. The "severe bear" contingency scenario in this document is approximately the live base case
- **Counterpoint:** AI tokens were the least-bad crypto sector in Q1 2026 (smallest sector decline, ~-14%, while 38% of altcoins traded near all-time lows), with revenue-generating leaders TAO, FET, and RENDER posting outright gains; sector cap ~$20.9B by May 2026 with ~$3.4B daily volume. The relative-outperformance trend continued through Q2 2026 (NEAR +72% on a late-May surge, FET +23%, VVV +19%) — revenue-generating DePIN compute networks decoupled from pure-speculation tokens, direct support for Gonka's fee-revenue thesis

**v3.0 Enhancement Findings (February 2026 Deep Research; corrected July 2026):**
- **GPU price deflation stalled:** H100 pricing collapsed 64-81% from Q4 2024 to Q1 2026 ($8-10/hr to $1.50-2.99/hr), but deflation has since stalled: July 2026 H100 rental median is $2.29-3.12/hr, roughly flat to -4% year-over-year (on-demand average $3.89 Jul 2025 → $3.72 Jul 2026); the latest cohort data (AIMultiple GPU index, Jul 2026) puts the H100 median at ~$3.15/hr — mild firming, not renewed decline. The actual price *reversal* is on the hardware side: GPU server acquisition costs are up 30-50% from the AI memory supercycle (HBM sold out through 2026), and some hyperscaler list prices are rising. B200 shipped at the start of 2025 (not Q3 2026 as originally projected) and rents for $2.69-16.11/hr
- **Fee-to-emission crossover:** Conservative scenario projects Year 10-12, moderate scenario Year 3-4; host profitability at critical decay points requires GNK >= $0.85-$3.30 (Feb 2026 model, 500-GPU assumption)
- **Protocol-Owned Liquidity (POL):** 22M GNK recommended deployment via Uniswap v3 concentrated liquidity, generating $550K-1.1M annually in LP fees (Feb 2026 estimate; deployment ranges need recalibration at current prices)
- **Enhanced revenue allocation:** Proposed 20/70/5/5 model (AI Fund / hosts / buyback-burn / veGNK yield) replacing the current 20/80 split
- **veGNK governance:** Vote-escrowed locking (1 month - 2 years), linear time-weighting, 2.5x max boost; fully mitigates flash loan governance attacks
- **Real-yield first-mover window has closed for buyback/burn:** Akash activated Burn-Mint Equilibrium (Mar 23, 2026) and io.net's Incentive Dynamic Engine went live (Jun 11, 2026) — though the io.net burn is currently emission-funded rather than the marketed revenue buyback (see §5.5). Gonka's remaining differentiator is **yield distribution to lockers** (veGNK), which remains rare
- **Oracle-based USD pricing recommended** to solve dual volatility (GPU price swings + GNK price volatility)

**Technical Specifications (from Official Whitepaper):**
- Sprint consensus uses a **2.3 billion parameter Transformer model** (64 layers, 128 attention heads). Note: weight allocation fully switched to **PoC v2** with the mainnet v0.2.9 upgrade (see Section 0.1)
- Randomized task verification reduces redundancy to **1-10%** (vs 100% in competing networks)
- Emission decay rate: **-0.000475 per epoch** (halving every ~1,460 epochs / 4 years)
- Governance: **25% quorum** (cut from the original 33.4% in v0.2.13, May 2026), **>50% majority**, **33.4% veto threshold**

---

## 0. Token Distribution — Official Breakdown

### Total Supply: 1,000,000,000 GNK (1 Billion)

| Allocation | Amount | Percentage | Purpose |
|------------|--------|------------|---------|
| **Core Host Incentive** | 680,000,000 GNK | 68% | Bitcoin-style epoch rewards for compute contribution |
| **Community Pool** | 120,000,000 GNK | 12% | Early liquidity, governed by Hosts via voting |
| **Founders Allocation** | 200,000,000 GNK | 20% | Founding team recognition |

### Emission Schedule — Mathematical Specification

**Initial Epoch Reward:** 323,000 GNK per epoch

**Decay Formula:**
```
current_epoch_reward = initial_reward × exp(decay_rate × epochs_since_genesis)

Where:
- initial_reward = 323,000 GNK
- decay_rate = -0.000475 per epoch
- Halving occurs approximately every 1,460 epochs (~4 years)
```

**Emission Projections:**

| Epoch | Years Since Genesis | Epoch Reward (GNK) | Cumulative Supply |
|-------|--------------------|--------------------|-------------------|
| 0 | 0 | 323,000 | 0 |
| 1,460 | ~4 years | 161,500 (50% of initial) | ~400M |
| 2,920 | ~8 years | 80,750 (25% of initial) | ~550M |
| 4,380 | ~12 years | 40,375 (12.5% of initial) | ~620M |
| 5,840 | ~16 years | 20,188 (6.25% of initial) | ~655M |
| 8,760 | ~24 years | ~5,000 | ~675M |

**Note:** The 680M allocation is the maximum that can ever be minted through epoch rewards. The exponential decay ensures this cap is approached asymptotically.

**Nuance (per official GitHub tokenomics.md):** The per-epoch figure is a cap, not a guaranteed fixed emission — reward coins are capped-but-work-proportional via a subsidy mechanism, and rewards vest rather than unlocking immediately. Mainnet has been live since August/September 2025 with emissions running since genesis; ~106M GNK (~10.6% of max supply) is circulating as of July 2026.

---

## 0.1 Sprint Consensus Mechanism — Technical Deep Dive

> **July 2026 status:** The mainnet v0.2.9 upgrade fully switched weight allocation to **PoC v2**, phasing out the original PoC logic described below. Subsequent releases further changed PoC accounting: v0.2.13 fixed confirmation-PoC reward accounting and disabled confirmation PoC for the remainder of the upgrade epoch. The mechanism below is the original whitepaper specification and remains useful as design background, but no longer describes the live weight-allocation code path.

### Transformer-Based Proof-of-Work ("Sprint")

Sprint is Gonka's novel consensus mechanism that replaces wasteful hash computation with **useful AI-aligned computation**. All hosts participate in a ~10-minute competitive computation period.

**Sprint Transformer Model Specifications:**

| Parameter | Value | Purpose |
|-----------|-------|---------|
| **Total Parameters** | ~2.3 billion | Large enough to be GPU-intensive |
| **Layers** | 64 | Deep architecture mirrors LLM training |
| **Attention Heads** | 128 | Multi-head attention for parallelism |
| **Embedding Dimension** | 512 | Vector representation size |
| **Feed-Forward Hidden Dim** | 8,192 | FFN expansion factor |
| **Vocabulary Size** | 8,192 | Token space |
| **Sequence Length** | 4 | Short sequences for rapid iteration |

**Sprint Procedure (Pseudocode from Whitepaper):**

```python
def generate_proofs(node_public_key, latest_blockchain_state):
    """
    During Sprint, hosts iterate through nonces to find "Appropriate Vectors"
    close to a Target Vector. More vectors found = higher PoC weight.
    """
    timer.start()
    Sprint_seed = generate_Sprint_seed(latest_blockchain_state)
    transformer_model = initialize_transformer(Sprint_seed)
    node_seed = generate_node_seed(node_public_key)
    target_vector = generate_target_vector(Sprint_seed)
    valid_nonces = []

    for nonce in nonce_generator:
        input_seed = combine_seeds(nonce, node_seed, Sprint_seed)
        input_sequence = generate_input_sequence(input_seed)
        output_sequence = transformer_model.forward(input_sequence)
        output_vector = extract_last_vector(output_sequence)

        # Random permutation prevents continuity exploitation
        permutation = generate_random_permutation(input_seed)
        permuted_vector = permute_vector(output_vector, permutation)

        distance = compute_euclidean_distance(permuted_vector, target_vector)
        if distance < threshold:  # ~1 in 900 chance
            send_valid_nonce(nonce, node_public_key)
            valid_nonces.append(nonce)

        if timer.check() > Sprint_duration:  # ~10 minutes
            break

    return valid_nonces
```

**Key Design Elements:**

1. **Distance Threshold:** Calibrated so ~1 in 900 nonce attempts produces an "Appropriate Vector"
2. **Random Permutation:** Output vectors are randomly permuted before distance calculation to prevent hosts from exploiting neural network continuity
3. **Sprint Seed:** Generated from blockchain state, unpredictable and same for all hosts
4. **Node Seed:** Unique per host, derived from public key
5. **Voting Weight:** Directly proportional to valid nonces found during Sprint

**Why This Design Works:**
- Hardware optimized for LLM training/inference automatically excels at Sprint
- No pre-computation advantage (random seed generated at Sprint start)
- GPU utilization between Sprints is freed for actual AI inference work
- Voting weight correlates with real compute capacity

---

## 0.2 Collateral System — Detailed Mechanics

### Weight Calculation Formulas

**From the Official Tokenomics Document:**

```
Base Weight = Potential Weight × Base Weight Ratio
           = Potential Weight × 0.20  (20% unconditional)

Collateral-Eligible Weight = Potential Weight × (1 - Base Weight Ratio)
                           = Potential Weight × 0.80  (80% requires backing)

Final Effective Weight = Base Weight + Activated Collateral Weight
```

**Collateral Requirements:**

| Parameter | Default Value | Governance-Adjustable |
|-----------|---------------|----------------------|
| Base Weight Ratio | 20% | Yes |
| Collateral Per Weight Unit | 0.0625 GNK per nonce | Yes |
| Grace Period | 180 epochs (~6 months) | Yes |
| Unbonding Period | 1 epoch | Yes |
| Malicious Behavior Penalty | 20% of collateral | Yes |
| Poor Performance Penalty | 10% of collateral | Yes |
| Performance Threshold | 5% missed work | Yes |

**Example Calculation (H100 GPU):**

```
Assumptions:
- H100 produces ~1,600 nonces per epoch during Sprint
- Collateral Per Weight Unit = 0.0625 GNK

Required collateral for full 80% weight:
= 1,600 nonces × 0.0625 GNK/nonce
= 100 GNK

Result:
- Without collateral: 20% of potential weight activated
- With 50 GNK locked: 20% + 40% = 60% of potential weight
- With 100 GNK locked: 20% + 80% = 100% of potential weight
```

### Slashing Conditions

| Offense | Penalty | Detection Method |
|---------|---------|------------------|
| Malicious behavior (fake results, cheating) | 20% of locked collateral | Randomized verification + majority consensus |
| Poor performance (>5% work missed) | 10% of locked collateral | Workload tracking |
| Repeated offenses | Cumulative + reputation reset | Historical pattern analysis |

### Grace Period Mechanism

New hosts receive a **180-epoch grace period** during which:
- Full voting weight is granted without collateral
- Hosts can earn and accumulate GNK for future collateral
- Reputation building begins immediately
- After grace period: must lock collateral or drop to 20% base weight

---

## 0.3 Task Verification System — Efficiency Innovation

### The Verification Challenge

Traditional decentralized networks require **100% task redundancy** (every task verified by multiple nodes). Gonka achieves equivalent security with **1-10% redundancy** through:

### Majority Verification

```
Verification Rule:
- Task is trusted when Hosts representing >50% of total voting weight confirm the result
- Based on assumption that majority of PoC-weighted Hosts are honest
- Reduces verification from "every node" to "majority weight"
```

### Randomized Task Verification

```
Verification Frequency by Host Weight:
- 50% weight host: verifies ~1 in 20 tasks
- 10% weight host: verifies ~1 in 100 tasks
- Network average: ~1 in 10 tasks verified
- Unpredictable selection prevents gaming
```

**Pseudo-Random Selection Algorithm:**
```
Each transaction has unique ID
Host signs ID with private key → signature becomes seed
Seed determines if Host should validate that specific task
Signature can be shared and independently verified by other Hosts
```

### Reputation System Formula

**From the Whitepaper (Appendix D):**

```
Validation Frequency = 1 − (1−0.01) × MIN(DAYS_OF_REPUTATION, N) / N

Where:
- N = 30 (default, governance-adjustable)
- New hosts: 100% of tasks validated (frequency = 1.0)
- After N days without fraud: 1% of tasks validated (frequency = 0.01)
```

**Reputation-Based Reward Sharing:**

| Reputation Level | Validation Rate | Reward Distribution |
|------------------|-----------------|---------------------|
| New (0 days) | 100% | 50% kept, 50% to validators |
| Building (15 days) | ~50% | ~75% kept, ~25% to validators |
| Established (30+ days) | 1% | 99% kept, 1% to validators |

**Reputation Reset Triggers:**
- Caught producing false results → Reset to 0
- Extended inactivity (>30 days) → Reputation deleted
- Fraud detection → All cycle rewards forfeited

---

## 0.4 Governance Parameters — Official Specification

| Parameter | Value | Description | Effect |
|-----------|-------|-------------|--------|
| **Quorum** | 25% of PoC-weighted power (genesis default 33.4%; lowered in v0.2.13, May 2026) | Minimum participation for valid vote | Below quorum = proposal invalid |
| **Majority Threshold** | >50% Yes votes | Required for passage | Below majority = rejected |
| **Veto Threshold** | 33.4% of non-abstaining votes | NoWithVeto rejection level | Triggers forced rejection |

**Governance Scope:**
- Block finalization
- Model registrations (which LLMs to support)
- Unit pricing adjustments
- Protocol upgrades
- Community Pool allocations
- All collateral/slashing parameters

**All parameters defined in Genesis Code and modifiable via governance proposals.**

**July 2026 Protocol Update — Changes Since February 2026:**

Several on-chain parameter and protocol changes shipped after this document's original analysis:

| Release | Date | Key Changes |
|---------|------|-------------|
| v0.2.9 | Q1 2026 | Full switch of weight allocation to PoC v2 |
| v0.2.11 | Mar 19, 2026 | Experimental inference shards (subnets) with off-chain coordination; inference-message performance optimizations; BLS distributed-key-generation security fixes from audit findings |
| v0.2.12 | Apr 27, 2026 | **Major milestone:** multi-model Proof-of-Compute support; transaction fee infrastructure; versioned devshard runtimes; random MLNode preservation; governance-controlled model coefficients. Multi-model PoC and transaction fees are directly tokenomics-relevant (see note below) |
| v0.2.13 | May 20, 2026 | Devshard escrow system (MaxEscrowsPerEpoch = 500,000; MaxNonce raised from hardcoded 20,000 to 1,000,000; broker allowlist); governance quorum lowered to 25%; GenesisGuardianMultiplier reduced to 0.33334 (genesis guardian voting power cut from ~34% to ~25%); MiniMax M2.7 added as governance model; guardian-controlled emergency switch for devshard inference; confirmation-PoC reward accounting fix |
| Devshard runtime v2 | Jun 15, 2026 | First devshard-only upgrade shipped independently of chain software (v0.2.13-devshard-v2); new broker/gateway inference path |
| **v0.2.13-post7 (security hotfix)** | **Jul 6, 2026** | Patches a **PoC-v2 weight-validation vulnerability**. Per the official network-updates feed, host `gonka1w7s4pharl5qs2lupxkuw2c0gzcls8chehwafg3` was detected exploiting the flaw before the fix deployed — the network's **first publicly disclosed live exploit attempt** (see §6.3) |
| Devshard runtime v3.0.0 | Jul 9, 2026 (approved on-chain Jul 11) | Standalone versioned runtime; enables inference during validation phases (a real capacity gain); better RAM utilization; SQLite/Postgres backends. On Jul 16, 2026 the v1/v2 runtimes were removed entirely — all traffic must use /devshard/v3 |
| Proposals 78/79 (models) | Jun 25-26, 2026 | Proposal 78 removed **both Qwen3-235B-A22B and Kimi K2.6** (models lacking validation majority), making **MiniMax M2.7 the sole PoC model** and base delegation target; Proposal 79 restored Kimi K2.6 at weight_scale_factor **0.9** (re-bootstrapped at epoch 311, Jun 27) and introduced **GLM-5.2** as an optional model, weight factor 2.47, no participation penalty. Qwen3 was permanently retired |
| Proposals 87/88 (Kimi K2.6) | Jul 15-16, 2026 | Kimi K2.6 lost validation majority **again** in epochs 328-329 (concentrated guardian delegations plus provider failures); temporarily removed via expedited Proposal 87, then re-registered via Proposal 88 for re-bootstrap at epoch 331 — its **second** removal/re-bootstrap cycle in three weeks. Weight factor unchanged at 0.9 (set Jun 26 via Proposal 79) |

Note: the latest chain release is **v0.2.13-post7** (Jul 6, 2026 security hotfix) — the v0.2.14 chain upgrade exists only as an open PR (Jul 8, 2026), with no v0.2.14+ release as of July 18, 2026; devshard runtimes now version independently of the chain.

**Tokenomics implications of v0.2.12:** multi-model PoC means weight/reward allocation now spans multiple models with governance-controlled per-model coefficients (a new governance surface), and transaction fee infrastructure adds an on-chain fee lever not modeled in this document's original emission/fee analysis. Both merit dedicated analysis in a future revision.

**Live model lineup (as of Jul 16, 2026):** **MiniMax M2.7** is the sole PoC model and base delegation target (Proposal 78, Jun 25, 2026 — no longer merely the "governance model" it was introduced as in v0.2.13); **GLM-5.2** is live as an optional model with no participation penalty (Proposal 79, Jun 26, 2026; weight factor 2.47); **Kimi K2.6** — added ~May 2026 via DevShards and formerly the primary inference model — is mid-re-bootstrap from epoch 331 after its **second** validation failure in three weeks: first removed by Proposal 78 (Jun 25, lacking validation majority), restored at weight factor 0.9 by Proposal 79 (Jun 26) and re-bootstrapped at epoch 311 (Jun 27), then removed again after losing validation majority in epochs 328-329 (Proposals 87/88, Jul 15-16, 2026). **Qwen3-235B-A22B**, the single consolidated PoC model from v0.2.9 (Jan 2026) through June 2026, was retired on Jun 25, 2026 and is no longer served. Any Kimi-centric positioning (e.g., "cheapest K2.6 provider") should carry a strong reliability caveat — two validation failures in three weeks — until the re-bootstrap completes and holds. Any pricing example in this document referencing smaller Qwen/Llama models is illustrative only — those models are not served on the live network.

**Guardian delegation concentration (new governance risk, Jul 2026):** the July 15, 2026 network update issued explicit guidance — **"Do not delegate to guardian nodes"** — after concentrated guardian delegations contributed to Kimi K2.6 losing validation majority. Guardians are now positioned as fallback-only, and the protocol team is actively pushing delegation distribution across independent hosts as a systemic-risk mitigation. This shows the v0.2.13 GenesisGuardianMultiplier reduction did not fully resolve guardian power: delegation concentration, not just the multiplier parameter, is the live risk (see Section 6.3/6.4).

Gonka also launched regular GiP (governance improvement proposal) meetings, the first focused on network scalability. Ecosystem developments through July 2026: Gonka now markets **$80M+ raised from Coatue and Bitfury Capital** (up from the Bitfury $50M anchor of Dec 2025); the GAIB "GAIC" public enrollment window ran Jun 5 - Jul 5, 2026 and is now closed — GAIB reports the prior private phase delivered $600K+ with 200+ H200 GPUs in the first batch (GAIB handles H100/H200/B200 procurement and node ops, with a 10%-of-mined-GNK insurance pool); gonka.ai now names select hosts Gcore, Hyperfusion, and 6blocks plus community partners Web3.com Ventures, HardYaka, and Bitfury; third-party GPU-rental partners emerged (Spheron dedicated Gonka bare-metal, Gcore Gonka rental pages); a broker/gateway retail layer (GonkaBroker, GonkaGate, JoinGonka, OpenGNK, gonka.to) now fronts developer access with fixed-USD pricing; an independent explorer/analytics layer launched in 2026 — gonka.gg (real-time blocks, validators, GPU/ML nodes, inference map, free public API), gonkascan.com, gonkahub.com (dashboard with Telegram node alerts), and tracker.gonka.vip — providing continuously updated network-size and participant data; and Gonka plans Asia expansion (Japan, South Korea) by end of 2026.

**v3.0 Update -- veGNK Governance Enhancement:**

Analysis of 6+ ve-tokenomics protocols (Curve veCRV, Convex vlCVX, Velodrome veVELO, Balancer veBAL, PancakeSwap veCAKE, Frax veFXS) informs the following veGNK design:

**veGNK Core Parameters:**

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Lock range | 1 month - 2 years | Conservative start; shorter than Curve's 4 years to reduce friction |
| Voting power | Linear time-weighting | `veGNK = GNK_locked * (time_remaining / max_lock)` |
| Max boost | 2.5x on AI Training Fund yield | Industry standard (Curve, Balancer use 2.5x) |
| Early exit | Not permitted | 83% of ve protocols do not allow early exit |
| Transferability | Non-transferable | Prevents governance concentration via secondary markets |
| Expected lock rate | 35-50% of circulating supply | Based on benchmark average of 40% across 6 protocols |

**Governance Attack Defense:**

| Attack Vector | Current Risk | With veGNK | Mitigation Mechanism |
|--------------|-------------|-----------|---------------------|
| Flash loan governance attack | HIGH | ELIMINATED | Cannot borrow locked tokens; veGNK is non-transferable |
| Whale voting dominance | MEDIUM | REDUCED | Time-weighting reduces power of holders who don't lock long-term |
| Vote buying/bribery | MEDIUM | MANAGED | Bribe markets create transparency; veGNK holders are long-term aligned |
| Sybil attacks (many wallets) | LOW | LOW | PoC-weighted voting already resists Sybil via GPU verification |

**Quadratic Voting Assessment:**
Quadratic voting is NOT recommended for general governance due to severe Sybil vulnerability. However, it IS viable for host-gated Community Pool decisions where GPU-based identity (PoC weight) provides natural Sybil resistance.

**Governance Concentration Risk:**
The Founder allocation (200M GNK, 20% of supply) could control up to 67% of veGNK if locked for maximum duration while others lock shorter. Recommended monitoring: track veGNK distribution and consider voluntary lock caps or progressive time-weighting if concentration exceeds 50%.

**3-Phase veGNK Rollout (proposed Feb 2026; not implemented as of Jul 2026 — timeline needs revision):**
1. **Phase 1:** Basic lock + voting power (veGNK contract, governance integration)
2. **Phase 2 (+6 months):** Boost mechanics + delegation (2.5x yield boost, delegate voting)
3. **Phase 3 (+12 months):** Advanced features (expanded lock range, cross-chain voting, potential veNFT exploration)

---

## 0.5 Dynamic Pricing System — EIP-1559 Inspired

### Per-Model Pricing Mechanism

Each AI model has an **independent per-token price** adjusted every block:

```
Price Adjustment Rules:

IF utilization < 40%:
    price_change = -elasticity × (40% - utilization) / 40%
    new_price = old_price × (1 + price_change)
    # Prices DECREASE to encourage usage

IF utilization BETWEEN 40% AND 60%:
    new_price = old_price
    # STABILITY ZONE - no change

IF utilization > 60%:
    price_change = +elasticity × (utilization - 60%) / 40%
    new_price = old_price × (1 + price_change)
    # Prices INCREASE to moderate demand

CONSTRAINTS:
- Maximum change: ±2% per block
- Price floor: 1 nicoin per AI token (prevents zero-cost abuse)
```

### Grace Period for Early Adoption

**First 90 epochs:** Inference pricing is set to **zero**

- Enables experimentation without cost barriers
- Rapid prototyping and developer onboarding
- After grace period: dynamic pricing activates

**July 2026 status:** The 90-epoch (~90-day) free-inference grace period ended around November 20, 2025; paid, per-block dynamic pricing has been live on mainnet since then. (Not to be confused with the separate 180-epoch collateral exemption for new hosts — see Section 0.2.)

---

## 0.6 Decentralized AI Training Fund

### 20% Revenue Allocation

```
From all inference revenue:
- 80% → Hosts who execute tasks
- 20% → Decentralized AI Training Fund
```

**Fund Purpose:**
1. Finance training of new open-source LLMs
2. Grants for promising training procedure proposals
3. Community-voted allocation to maximize impact

**Governance Process for Training:**
1. Contributors propose code changes (pull requests)
2. Proposals undergo discussion and debate
3. Approved approaches become code updates
4. Formal training experiment proposals with parameters, dataset, funding
5. Governance voting (multiple iterations expected)
6. Execution and transparent results

**Commitment:** All models trained using Gonka resources remain **open-source**

**Revenue Allocation Adjustment:**
- Percentage modifiable via governance
- Only available after Year 5 (network must demonstrate training capabilities)
- Can increase/decrease based on impact on adoption

**v3.0 Update -- Enhanced Revenue Allocation Model:**

Research across 12 DeFi protocols (GMX, Aave, Hyperliquid, MakerDAO, Curve, Synthetix, etc.) reveals that the current 20/80 split leaves significant value on the table. The enhanced 20/70/5/5 model introduces structured value accrual:

```
CURRENT MODEL:                    PROPOSED ENHANCED MODEL:
┌─────────────────────┐           ┌─────────────────────┐
│ 20% → AI Training   │           │ 20% → AI Training   │
│        Fund          │           │        Fund          │
│                      │           │                      │
│ 80% → Hosts         │           │ 70% → Hosts         │
│                      │           │  5% → Buyback-Burn  │
│                      │           │  5% → veGNK Yield   │
└─────────────────────┘           └─────────────────────┘
```

**Enhanced Allocation Details:**

| Allocation | % | Mechanism | Frequency |
|-----------|---|-----------|-----------|
| AI Training Fund | 20% | Treasury accumulation for AI R&D | Continuous |
| Host task execution | 70% | Direct payment to executing hosts | Per-task |
| Buyback-and-burn | 5% | Continuous TWAP (15-min intervals, 0.5% max slippage) | Continuous |
| veGNK real yield | 5% | Distribution to veGNK lockers (+ AI Fund surplus) | Weekly |

**AI Training Fund Surplus Mechanism (MakerDAO Surplus Buffer Pattern):**

The AI Training Fund maintains a 6-month runway threshold. When the fund balance exceeds 6 months of operating expenses, the surplus is distributed to veGNK holders:

```
Priority 1: Fund accumulates to 6-month runway target
Priority 2: Surplus above target → distribute to veGNK holders
Priority 3: If fund is depleted → pause distributions, rebuild reserve
```

**Buyback-and-Burn Design:**
- Mechanism: Continuous TWAP orders (15-minute intervals)
- Max slippage: 0.5% per order
- Destination: Burn address (permanent supply reduction)
- Opportunistic dip-buying: 3x accelerated buyback when GNK is >20% below 30-day TWAP
- At $10M annual inference revenue: ~$500K annual buyback pressure

---

## 0.7 Distributed Training — DiLoCo Mechanism

### How Gonka Enables Decentralized LLM Training

**Traditional Distributed Training Problems:**
1. Untrusted hosts may submit fraudulent computations
2. Internet bandwidth limitations vs. datacenter networks
3. Each host storing entire model is impractical
4. Centralized coordinator is single point of failure

**Gonka's DiLoCo-Based Solution:**

```
DiLoCo Approach:
- Synchronize model parameters only every ~1,000 training steps
  (vs. every step in traditional distributed training)
- Bi-level optimization:
  - Inner loop: Local AdamW optimization
  - Outer loop: Federative Averaging with Nesterov momentum

On-Chain Management:
- Blockchain handles rendezvous, rank assignment, synchronization
- No centralized coordinator
- Trustless and resilient to host failure
```

### Proof-of-Learning Validation

```
State Preservation:
At random intervals, hosts preserve:
- Previous weights
- Current weights
- Optimizer states (momentum, adaptive learning rates)

Hash Commitment:
- Hosts commit hashes of preserved states to blockchain
- Timestamped, tamper-evident records
- Actual artifacts provided on-demand during validation

Validator Selection:
- Random validators from non-training hosts
- Verify hash matches on-chain commitment
- Confirm weight changes represent legitimate training
- Honeypot traps test validator diligence
```

### Model Sharding for Scale

```
Problem: 100B+ parameter models too large for single host

Solution: Sharding approaches (GShard, DiPaCo)
- Hosts store and train only portions of model
- Share updates for their assigned components
- Enables training frontier-scale MoE models (2026 norm: 400B-1T+ total
  parameters, e.g., DeepSeek V4 Flash at 284B through V4 Pro at 1.6T)

Practical DiLoCo Capacity:
- 8×H100 servers can train 30-50B parameter models
- Network-wide: Much larger models possible through sharding
```

---

## 1. The Three Ecosystem Roles — Deep Analysis

### 1.1 Developers (Demand Side)

**Definition:** Entities that consume AI computational services through Gonka's OpenAI-compatible API.

**Primary Functions:**
| Function | Description | Economic Impact |
|----------|-------------|-----------------|
| Submit inference requests | Chatbots, code completion, image generation | Creates demand for GNK |
| Deploy AI applications | Production workloads using open-source LLMs | Sustained network utilization |
| Pay in GNK tokens | All compute is priced in native currency | Direct token demand |
| Set price limits | Max cost per task prevents overpaying | Demand elasticity signal |

**Developer Personas:**
1. **Cost-Optimizers:** Startups seeking cheaper alternatives to OpenAI/Anthropic
2. **Privacy-Seekers:** Applications requiring data sovereignty and no logging
3. **Censorship-Resistant:** Content that centralized providers restrict
4. **Open-Source Advocates:** Developers preferring transparent, community-governed infrastructure

**Developer Economics:**
```
Developer Cost = (Prompt Tokens + Completion Tokens) × UnitsOfComputePerToken × UnitOfComputePrice

Where:
- UnitsOfComputePerToken = Model-specific constant (larger models = higher)
- UnitOfComputePrice = Dynamic epoch-by-epoch weighted median of host proposals
```

---

### 1.2 Hosts/Miners (Supply Side)

**Definition:** Hardware providers who contribute GPU computational resources to execute AI workloads and participate in network consensus.

**Primary Functions:**
| Function | Description | Economic Impact |
|----------|-------------|-----------------|
| Run GPU nodes | Execute inference/training tasks | Creates supply capacity |
| Participate in Sprint (PoC) | ~10-minute competitive computation for voting weight | Determines reward share |
| Validate other hosts | Verify task completion and results | Network integrity |
| Lock collateral | Back voting weight with GNK deposits | Skin-in-the-game security |

**Host Revenue Components:**
1. **Work Coins:** Fees from completed inference tasks (proportional to work performed)
2. **Reward Coins:** Newly minted subsidies (proportional to PoC weight)
3. **Top Miner Bonuses:** Additional rewards for high performers

**Host Weight Calculation (Official Formula):**
```
Base Weight = Potential Weight × 0.20  (unconditional)
Collateral-Eligible Weight = Potential Weight × 0.80  (requires GNK collateral)
Final Effective Weight = Base Weight + Activated Collateral Weight

Example (H100 producing 1,600 nonces/epoch):
- Collateral Per Weight Unit = 0.0625 GNK
- Full collateral required = 1,600 × 0.0625 = 100 GNK
- Without collateral: 20% weight
- With 100 GNK locked: 100% weight

Grace Period: First 180 epochs (~6 months) = no collateral required
Unbonding Period: 1 epoch (collateral remains slashable during withdrawal)
```

---

### 1.3 Token Investors (Capital Side)

**Definition:** Participants who purchase and hold GNK tokens without directly operating hardware.

**Primary Functions:**
| Function | Description | Economic Impact |
|----------|-------------|-----------------|
| Purchase GNK | Buy on exchanges or Community Pool | Price discovery |
| Provide liquidity | Enable host-to-fiat conversion | Market stability |
| Speculate on growth | Bet on AI compute demand increase | Capital formation |
| Participate in governance | Vote on network parameters (if holding) | Protocol direction |

**Investor Value Thesis:**
- **Scarcity:** 1 billion fixed supply with Bitcoin-style halving emissions
- **Utility:** Direct correlation between network usage and token demand
- **Efficiency:** ~98% productive compute vs. 0% (Bitcoin) or 40% (Bittensor)
- **Growth Exposure:** AI compute market projected $9B (2024) → $100B+ (2032)

---

## 2. Detailed Incentive Analysis by Role

### 2.1 Developer Incentives — Why Use Gonka?

#### Incentive #1: Cost Advantage Mechanics

**Why Gonka Can Be Cheaper:**

| Cost Factor | Centralized (AWS/OpenAI) | Gonka | Savings Mechanism |
|-------------|--------------------------|-------|-------------------|
| Corporate overhead | 15-30% margin | 0% | No shareholders, marketing, C-suite |
| Infrastructure profit | 20-40% markup | 0% | Hosts set competitive prices |
| Early-stage subsidy | None | Significant | Token emissions subsidize compute |
| Compute efficiency | ~70-80% | ~98% | Minimal consensus overhead |

**Price Comparison Analysis (illustrative, at GNK = $1.00, 50% utilization; actual GNK price is ~$0.13 as of Jul 2026, which makes Gonka correspondingly cheaper for developers):**

| Use Case | Gonka Cost/Month | OpenAI Cost/Month | Savings |
|----------|------------------|-------------------|---------|
| Personal chatbot (10M tokens) | $5 | $130 | 96% |
| Startup (100M tokens) | $50 | $1,300 | 96% |
| Mid-size app (1B tokens) | $500 | $13,000 | 96% |
| Enterprise (10B tokens) | $5,000 | $130,000 | 96% |

**Critical Price Thresholds:**

| Competitor | Break-Even GNK Price | Gonka Advantage Zone |
|------------|---------------------|----------------------|
| OpenAI GPT-4o | $20.00 | GNK < $20 |
| OpenAI GPT-3.5 | $4.00 | GNK < $4 |
| DeepSeek V4 Flash ($0.14/$0.28 per 1M) | $0.28 | GNK < $0.28 |
| Anthropic Claude | $30.00 | GNK < $30 |
| Self-hosted H100 | $3.00 | GNK < $3 |

*Benchmark note (Jul 2026): DeepSeek's API now serves only deepseek-v4-pro ($0.435/$0.87 per 1M) and deepseek-v4-flash ($0.14/$0.28); V2/V3/R1 endpoints are retired (V4 shipped Apr 24, 2026; R2 never shipped — reasoning is folded into V4's thinking mode). The V4 Flash benchmark halves the earlier V2-derived "GNK < $0.56" parity threshold used in prior revisions of this document.*

**v3.1 Update -- GPU Cloud Pricing Reality (July 2026):**

H100 pricing collapsed 64-81% from Q4 2024 ($8-10/hr) to Q1 2026 ($1.50-2.99/hr at decentralized providers), but the deflation has since **stalled** (rental medians roughly flat to -4% YoY as of July 2026), while hardware acquisition costs and some hyperscaler list prices have **reversed upward**:

| Provider Category | H100 $/hr (Jul 2026) | Note |
|-------------------|----------------------|------|
| Hyperscalers (on-demand, Azure/AWS) | ~$7-8 | Centralized clouds raising, not cutting, prices |
| Market median | $2.29-3.12 | Latest cohort (AIMultiple, Jul 2026) ~$3.15 — at/above the top of the band, i.e., mild firming |
| Budget decentralized / specialized | $1.99-3.50 | |
| Cheapest (Thunder Compute) | ~$1.40 | Full provider range $1.40-$8+ (IntuitionLabs tracks $1.49-6.98 across 15+ providers) |

*Adjacent cohorts (Jul 2026): H200 median ~$4.11/hr ($2.30 FluidStack to $13.78 Azure); B200 median $6.25/hr (floor $3.20 Runcrate, spot $2.74 Spheron).*

**Cause of the stall/hardware reversal:** the AI memory supercycle — HBM sold out through 2026, blended DRAM contract prices +~80% QoQ in Q1 2026 and ~+60% QoQ in Q2 2026, GPU server prices +30-50%, HBM absorbing ~23% of DRAM wafer capacity — plus surging inference demand. **The supercycle is decelerating, but the deceleration is being revised upward:** TrendForce (Jul 3, 2026) forecast Q3 2026 conventional DRAM contract prices up 13-18% QoQ (vs ~60% in Q2), HBM blended +8-13% (vs 53-58%), NAND +10-15% — then on ~Jul 8-9, 2026 **raised** its Q3 and Q4 forecasts (PC DRAM Q3 now +15-20% QoQ, up from 8-13%; server DRAM confirmed +13-18%, with US CSP long-term agreements capping increases), and module maker ADATA reportedly sees Q3 DRAM up 20-30% and NAND up 35-40%. "Decelerating" remains directionally right for contract prices, but the 13-18% floor is now the conservative end, not the consensus. Server DRAM remains in shortage through Q3 and GPU servers are still +30-50%, so host hardware acquisition costs stay elevated through 2026 — and GPU-hardware-cost relief in 2027 looks less likely than the early-July snapshot implied.

**Blackwell reality check (corrects v3.0):** B200 shipped at the start of 2025, not mid/Q3 2026. In 2026 Blackwell accounts for >70% of NVIDIA high-end shipments, led by GB300/B300 (Blackwell Ultra); B200 is already the mid-generation part. B200 rents for $2.69-16.11/hr (median ~$6.25), expected to stabilize ~$2.50-3.00 at major clouds only by Q4 2026. Gonka itself supports ~20 GPU types including H100, H200, and B200 (B200 recommended for optimal mining rewards), with B200 capacity onboarding via the GAIB partnership. The 2026 roadmap story is Vera Rubin — but the "accelerated" framing of early July is now too rosy: KeyBanc (mid-Jul 2026) reports the Rubin ramp slightly delayed by thermal heat-lid issues and SK Hynix HBM4 qualification, with initial July volume below projections and Rubin's share of NVIDIA's 2026 GPU shipments cut from ~29% to ~22% (~1.7-1.8M units); the Rubin Ultra four-die GPU was reportedly cancelled/scaled back due to packaging limits (Jul 1, 2026). Standard Rubin remains on track for mass shipments this summer to eight cloud partners (AWS, Azure, Google Cloud, Oracle, CoreWeave, Lambda, Nebius, Nscale), and the next-gen Kyber rack system remains pushed to 2028. Net effect: less 2026 Rubin supply than guided, which supports continued firmness in H100/H200/B200 rental prices. The v3.0 projections of H100 falling to $1.00-2.00 by Q3-Q4 2026 and $0.30-0.80 by 2028 assumed continuous 30-50% annual deflation and should be treated as invalidated.

**Implication:** With oracle-based USD pricing (recommended), Gonka's cost advantage is maintained regardless of GNK price volatility, as inference pricing dynamically adjusts via price feeds from Pyth (400ms latency) and Chainlink (1hr heartbeat) oracles.

**Why This Should Work:**
1. **No profit extraction:** Unlike AWS (30%+ margins), hosts compete on cost
2. **Emission subsidy:** Early developers get compute below actual cost
3. **Dynamic pricing:** Sub-40% utilization drives prices down automatically
4. **Open-source models:** No licensing fees for Llama, Qwen, etc.

---

#### Incentive #2: Censorship Resistance & Privacy

**Why This Matters:**

| Risk with Centralized | Gonka Solution | Technical Mechanism |
|-----------------------|----------------|---------------------|
| Account termination | No central authority | Decentralized task routing |
| Prompt logging | No unified logging | Tasks distributed across hosts |
| Content restrictions | No content policy | Protocol-level neutrality |
| Unilateral TOS changes | Governance voting | On-chain parameter changes |

**Target Developer Segments:**
- Adult content applications (restricted by OpenAI/Anthropic)
- Political content in restricted jurisdictions
- Financial analysis tools (liability concerns)
- Medical applications (HIPAA-like privacy needs)
- Competitive intelligence (trade secret protection)

**Why This Should Work:**
1. **Architectural neutrality:** Protocol doesn't evaluate content, only computes
2. **Distributed execution:** No single point for surveillance or shutdown
3. **Cryptographic payment:** GNK transactions don't require KYC
4. **Host sovereignty:** Each host chooses participation terms

---

#### Incentive #3: Transparent & Predictable Pricing

**EIP-1559-Inspired Dynamic Pricing (Official Specification):**

```
Price Adjustment Formula:

IF utilization < 40%:
    price_change = -elasticity × (40% - utilization) / 40%
    new_price = old_price × (1 + price_change)
    # Prices DECREASE to encourage usage

IF utilization BETWEEN 40% AND 60%:
    new_price = old_price
    # STABILITY ZONE - no change

IF utilization > 60%:
    price_change = +elasticity × (utilization - 60%) / 40%
    new_price = old_price × (1 + price_change)
    # Prices INCREASE to moderate demand

CONSTRAINTS:
- Maximum change: ±2% per block (prevents sudden spikes)
- Price floor: 1 nicoin per AI token (prevents zero-cost abuse)
- Per-model pricing: Each AI model has independent price
- Grace period: First 90 epochs = zero pricing for developer onboarding
```

**Why This Works for Developers:**

| Feature | Benefit | Mechanism |
|---------|---------|-----------|
| Max price limits | Never overpay | Tasks fail if price exceeds limit |
| Gradual changes | No sudden spikes | 2% max change per block |
| Per-model pricing | Cost optimization | Choose cheaper models when appropriate |
| Escrow with refunds | Pay only for actual use | Deposit max, refund unused |
| 90-epoch grace | Free experimentation | Zero pricing during onboarding |

**v3.0 Update -- EIP-1559 Parameter Sensitivity Analysis:**

Deep stress testing of the EIP-1559 adjustment mechanism reveals the current +-2% rate is conservative. Analysis of convergence speed and volatility across parameter ranges:

| Adjustment Rate | Convergence Speed | Price Volatility | Stability | Recommendation |
|----------------|-------------------|------------------|-----------|----------------|
| +-1% | Very slow (160+ blocks for 80% correction) | Minimal | Excellent | Too slow for market tracking |
| **+-2% (current)** | Slow (80 blocks / ~13 min for 80% correction) | Low | Excellent | Safe but sluggish |
| **+-4% (recommended)** | Moderate (40 blocks / ~7 min for 80% correction) | Moderate | Good | Best balance of speed and stability |
| +-6% | Fast (27 blocks / ~4.5 min) | High | Acceptable | Approaches instability threshold |
| +-8%+ | Very fast | Very high | Poor | Oscillation risk, not recommended |

**Key Finding:** At +-2%, an 80% GNK price spike requires ~80 blocks (~13 minutes) of consecutive -2% adjustments before the base fee corrects to maintain USD parity. At +-4%, this halves to ~40 blocks (~7 minutes). Academic research on Ethereum's EIP-1559 shows stability at rates up to 6-11%.

**Recommendation:** Increase adjustment rate to +-4% for testing on devnet/testnet. This provides faster market response while maintaining predictable pricing behavior. Governance can adjust this parameter based on real-world performance data.

---

#### Incentive #4: Access to Open-Source Model Training Fund

**20% of inference revenue funds decentralized AI training (Official Specification):**

```
Revenue Split:
- 80% → Hosts who execute inference tasks
- 20% → Decentralized AI Training Fund

Fund Usage:
1. Cover unit-of-compute costs during training
2. Grants for promising training procedures (via community voting)
3. R&D experiments approved through governance
```

| Benefit | Description |
|---------|-------------|
| Revenue sharing | Developers contributing training earn % of fund |
| Truly open-source | All models trained remain open-source (network guarantee) |
| Community governance | Training priorities set via PoC-weighted voting |
| Network effects | Better models → more developers → more training funds |
| Adjustable | Percentage modifiable via governance after Year 5 |

**Training Procedure Governance:**
1. Contributors propose code changes (pull requests)
2. Extensive presentation and debate on feasibility
3. Approved approaches become code updates
4. Formal training experiment proposal (parameters, dataset, funding)
5. Governance voting (multiple iterations expected)
6. Execution with full transparency

---

### 2.2 Host/Miner Incentives — Why Provide GPUs?

#### Incentive #1: Higher Revenue Potential vs. Traditional Rental

**Revenue Comparison (Per H100 GPU):**

*Assumptions: 90% uptime, 500-GPU network, 323,000 GNK/epoch emission*

> **July 2026 reality check:** This table is an illustrative early-network model. The live counters put the network at ~1,200 active GPUs (joingonka.ai 1,178; tracker.gonka.vip ~1,214) — not the ~5,000 in CoinMarketCap's stale project description or the ~14,000 announced Feb 2026 peak. At ~1,200 GPUs the mining denominator is ~2.4x the modeled 500, so per-GPU mining rewards are roughly 40% of the figures below (~250-270 GNK/day per H100-equivalent) — ~4x better than the 5,000-GPU assumption implied, putting host break-even nearer ~$0.20 GNK. With GNK at ~$0.13 hosts still earn below traditional rental rates from emissions alone, but the gap has narrowed materially; the economics depend on fee revenue growth and/or modest GNK price recovery.

| GNK Price | Daily Mining | Daily Work Fees | Daily Total | Monthly | vs. Traditional ($1,760/mo) |
|-----------|--------------|-----------------|-------------|---------|----------------------------|
| $0.50 | $29 | $5 | $34 | $1,020 | -42% (worse) |
| **$0.85** | **$49** | **$9** | **$58** | **$1,740** | **Break-even** |
| $1.00 | $58 | $10 | $68 | $2,040 | +16% (better) |
| $2.00 | $116 | $20 | $136 | $4,080 | +132% (better) |
| $5.00 | $290 | $50 | $340 | $10,200 | +480% (better) |
| $10.00 | $580 | $100 | $680 | $20,400 | +1060% (better) |

**Why Traditional Rental Revenue is Capped:**
1. Fixed USD pricing ($2.10-4.00/hr for H100)
2. You handle customer acquisition (marketing costs)
3. Utilization risk (you bear 100%)
4. No upside potential

**Why Gonka Revenue Can Be Higher:**
1. Token price appreciation potential (10x+)
2. Automatic task allocation (no marketing)
3. Shared utilization risk across network
4. Dual income: mining + work fees
5. Top miner bonuses for high performers

**Host Profitability Formula:**
```
Net Daily Profit = (Mining Rewards × GNK Price) + Work Fees - (Electricity + Depreciation + Opportunity Cost)

Where:
- Mining Rewards = (Your PoC Weight / Total Network PoC) × Daily Emission
- Work Fees = Your Task Revenue × (1 - 20% Training Fund)
- Opportunity Cost = Traditional rental revenue you're forgoing
```

**v3.0 Update -- Fee-to-Emission Transition Risk:**

As epoch rewards decay exponentially (halving every ~1,460 epochs / ~4 years), inference fee revenue must scale proportionally or hosts face a profitability crisis. Deep stress testing reveals:

**Host Profitability Thresholds at Critical Decay Points:**

| Decay Point | Epoch Reward (% of Initial) | Min GNK Price for Profitability | Required Fee Revenue to Compensate |
|-------------|----------------------------|--------------------------------|-----------------------------------|
| Year 0 (Launch) | 100% (323,000 GNK) | $0.85 | $0 (emissions sufficient) |
| Year 4 (First Halving) | ~47% (152,440 GNK) | $1.50 | $50M annual |
| Year 8 (Second Halving) | ~22% (71,929 GNK) | $2.50 | $142M annual |
| Year 12 (Third Halving) | ~10.5% (33,936 GNK) | $3.30 | $209M annual |

**Crossover Timeline by Scenario:**

| Scenario | Developer Growth | Year 4 Fee Revenue | Crossover Year | Risk Level |
|----------|-----------------|-------------------|----------------|------------|
| Conservative | 10%/yr | $96.9M | Year 10-12 | Medium-High |
| **Moderate (Target)** | **25%/yr** | **$1.24B** | **Year 3-4** | **Low** |
| Aggressive | 50%/yr | $26.3B | Year 2-3 | Very Low |

**Comparable Network Fee Transitions (Feb 2026 estimates; note Bittensor generated ~$43M Q1 2026 revenue from AI customers, and Akash crossed an ATH ~$5M compute spend in the first 90 days of 2026):**

| Network | Fee Revenue % (2026) | Crossover Timeline | Status |
|---------|---------------------|-------------------|--------|
| Bitcoin | 10-15% | Never (declining rewards) | At risk post-2040 |
| Filecoin | ~45% | Year 8-9 (2028-29) | On track |
| Akash | ~40% | Year 4-5 (2026-27) | On track |
| **Gonka** | **0% (Year 1)** | **Year 6-10 (scenario-dependent)** | **Monitor closely** |

**Contingency Triggers:** Activate contingency plans if Year 4 fee revenue falls below $50M (vs. $96.9M conservative baseline). Contingencies include: (a) governance-activated tail emissions (1-2% annual inflation cap), (b) enhanced developer subsidies from Community Pool, (c) host efficiency programs (GPU optimization grants).

---

#### Incentive #2: Bitcoin-Style Scarcity Economics

**Official Emission Formula (from Tokenomics PDF):**
```
current_epoch_reward = initial_reward × exp(decay_rate × epochs_since_genesis)

Where:
- initial_reward = 323,000 GNK
- decay_rate = -0.000475 per epoch
- Halving interval = ln(2) / 0.000475 ≈ 1,460 epochs (~4 years)
```

**Emission Schedule:**

| Epoch | Years | Epoch Reward | Cumulative | % of 680M Cap |
|-------|-------|--------------|------------|---------------|
| 0 | 0 | 323,000 GNK | 0 | 0% |
| 365 | ~1 | 275,000 GNK | ~118M | 17.4% |
| 1,460 | ~4 | 161,500 GNK | ~400M | 58.8% |
| 2,920 | ~8 | 80,750 GNK | ~550M | 80.9% |
| 4,380 | ~12 | 40,375 GNK | ~620M | 91.2% |
| 5,840 | ~16 | 20,188 GNK | ~655M | 96.3% |
| 8,760 | ~24 | ~5,000 GNK | ~675M | 99.3% |

**Why This Creates Value:**

1. **Early miner advantage:** Fewer GPUs competing → larger share
2. **Exponential decay:** Continuous reduction (not discrete halvings)
3. **Fixed cap:** 680M maximum from mining (68% of total supply)
4. **Scarcity feedback loop:**
```
More Hosts → fewer GNK per GPU → higher scarcity → potential price support
```

**Mathematical Relationship:**
```
If Network GPUs double: Individual mining reward halves
If Token Price doubles: Individual USD earnings stay same (or grow if demand increases)
If Both double: Supply increases, price increases → potential equilibrium
```

---

#### Incentive #3: Meaningful Work (Not Wasted Compute)

**Compute Efficiency Comparison (from Whitepaper Appendix A):**

| Network | Voting Weight Basis | Task Focus | Efficiency |
|---------|---------------------|------------|------------|
| **Bitcoin PoW** | Computational power (hash puzzles) | 100% security, 0% productive | 0% |
| **Ethereum PoS** | Amount of staked capital | Security + staking rewards | ~0% productive |
| **Bittensor** | Stake + subnet validation | 40% AI compute, 60% staking | ~40% |
| **Render** | Job-based allocation | GPU rendering | ~90% |
| **Gonka Sprint** | Transformer PoW + collateral | ~98% AI tasks, ~2% consensus | **~98%** |

**Why Gonka Achieves ~98% Efficiency:**
- Sprint uses time-bound transformer computation (~10 min)
- Between Sprints: 100% of GPU time goes to inference/training
- Randomized verification: 1-10% redundancy vs 100% in other networks
- No staking waste (collateral is economic commitment, not capital yield)

**Why ~98% Efficiency Matters to Hosts:**

1. **Environmental story:** Lower regulatory risk vs. Bitcoin mining
2. **Meaningful contribution:** AI advancement, not hash puzzles
3. **Energy efficiency:** Same electricity → more value created
4. **Public perception:** Defensible business model

---

#### Incentive #4: Early Liquidity Support (Community Pool)

**120 million GNK (12% of supply) reserved for liquidity:**

| Feature | Benefit to Hosts |
|---------|------------------|
| Pre-exchange liquidity | Convert GNK → USDT/ETH/BTC before listings |
| Reduced "wait to sell" risk | Don't hold illiquid tokens |
| Host governance | Hosts vote on pool operations |
| Price discovery | Market-based conversion rates |

**Recent Activity:**
- Bitfury announced a **$50M total investment commitment** to Gonka (Dec 1, 2025), publicly framed as the first strike in a ~$1B plan to decentralize AI compute; the community-pool-approved $12M GNK purchase at $0.60/GNK was the first tranche. As of Jul 2026 Gonka markets **$80M+ raised from Coatue and Bitfury Capital**
- Pool approved via on-chain voting by hosts
- **The $0.60 Schelling point did not hold:** GNK traded down to ~$0.13 by July 2026 through the broader bear market

**v3.0 Update -- Protocol-Owned Liquidity (POL) Enhancement:**

Deep research into POL models (Olympus DAO, Berachain, Tokemak, Balancer) demonstrates that protocol-owned liquidity is 10-20x more cost-efficient than traditional liquidity mining:

| Approach | Cost per $1 TVL | Liquidity Retention | Annual Revenue |
|----------|----------------|--------------------|----|
| Traditional Liquidity Mining | $10 per $1 retained | 10-25% after emissions end | $0 (emissions are cost) |
| **Protocol-Owned Liquidity** | **$0.50 per $1 TVL** | **100% (permanent)** | **$550K-1.1M in LP fees** |

**Recommended POL Deployment:**

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Total allocation | 22M GNK (~18.3% of Community Pool) | Conservative within 15-35% benchmark range |
| Pair split | 60% GNK/USDC + 40% GNK/ETH | Stability (USDC) + DeFi composability (ETH) |
| DEX | Uniswap v3 concentrated liquidity | 4-5x capital efficiency vs. v2 full-range |
| Fee tier | 0.3% | Standard for medium-volatility governance tokens |
| Range strategy | +-25-35% from current price | Balanced capital efficiency and rebalancing frequency |
| Target liquidity depth | $3-5M total | <1% slippage for $50K trades |

**Phased POL Rollout (proposed Feb 2026; not deployed as of Jul 2026 — ranges were sized at ~$1.00 GNK and need recalibration at ~$0.13):**
- Phase 1: 8M GNK in GNK/USDC 0.3% pool (+-25% range)
- Phase 2 (+1 quarter): 6M GNK in GNK/ETH 0.3% pool (+-30% range)
- Phase 3 (+2 quarters): Remaining 8M GNK after governance review of Phase 1-2 performance

---

### 2.3 Investor Incentives — Why Hold GNK?

#### Incentive #1: Exposure to AI Infrastructure Growth

**Market Size Projection:**

| Year | AI Compute Market | Decentralized Share (Est.) | Gonka Target Share |
|------|-------------------|---------------------------|-------------------|
| 2024 | $9B | 0.1% ($9M) | — |
| 2026 | $25B | 1% ($250M) | 10% ($25M) |
| 2028 | $50B | 3% ($1.5B) | 15% ($225M) |
| 2030 | $100B | 5-10% ($5-10B) | 20% ($1-2B) |

**Competitive Positioning (updated Jul 2026):**

| Project | Focus | Market Cap / Revenue (Jul 2026) | Productive Compute |
|---------|-------|--------------------------------|-------------------|
| Bittensor (TAO) | AI Marketplace | ~$1.9-2.2B mcap (~$192-199/TAO, ~71-75% below $757 ATH); ~$43M Q1 2026 revenue | ~40% |
| Render (RENDER) | GPU Rendering | ~$784M mcap ($1.51/RENDER, ~89% below $13.53 ATH) | ~90% |
| Akash (AKT) | General Cloud | ~$157M mcap (~$0.53/AKT); ATH ~$5M compute spend in first 90 days of 2026 | Variable |
| io.net | GPU Aggregation | Growing; $8M enterprise deal (~$650K/month) announced Jun 2026 | High |
| Aethir (ATH) | Enterprise GPU cloud | $127.8M FY2025 revenue; ~$147-166M ARR exiting 2025 (Aethir has also self-cited $126.0M ARR; no 2026 quarterly figures published); 150+ enterprise clients, 435K+ GPU containers in 93 countries | High |
| Gensyn ($AI) | AI compute / agents | TGE Apr 29, 2026 (Binance Alpha, Coinbase, KuCoin, Bitget); mainnet reported >5,000 H100-eq on day one; 70% of protocol revenue burned via Delphi app | High |
| **Gonka (GNK)** | **AI Inference** | **~$13.9M mcap ($0.13/GNK)** | **~98%** |

*Note: the DePIN token complex sold off hard in H1 2026 — earlier drafts of this table carried Dec 2025-era market caps 2-6x above the July 2026 figures now shown. New direct entrants since April 2026: Gensyn mainnet + $AI token (above) and BitTorrent's BTTInferGrid decentralized AI-inference network (launched Jun 17, 2026; bootstrapping through 2026).*

**v3.1 Update -- Competitive Landscape with Revenue Distribution Models:**

The v3.0 claim that "no competing AI compute network has implemented mature real yield distribution" is **no longer true**. Akash activated Burn-Mint Equilibrium (BME) via Mainnet 17 on March 23, 2026 (all on-chain compute spend triggers a market buy-and-burn of AKT, minting ACT stable credit for settlement). io.net's Incentive Dynamic Engine (IDE) went live June 11, 2026: emissions tied to real network earnings, ≥50% of surplus revenue marketed as buying back and burning IO, targeting ≥12M IO removed in year one. **Caveat:** independent analysis of io.net's own explorer indicates the burn is currently emission-funded rather than the marketed revenue buyback, with demand-driven emissions still switched off — which strengthens Gonka's "real revenue to lockers" differentiation.

| Network | Revenue Distribution | Real Yield to Holders | Buyback Mechanism | veToken Governance |
|---------|---------------------|----------------------|-------------------|-------------------|
| **Bittensor (TAO)** | Emission-based + ~$43M Q1 2026 AI customer revenue | None | None | None |
| **Render (RNDR)** | Burn-Mint Equilibrium | None (deflationary via burn) | Implicit (BME) | None |
| **Akash (AKT)** | BME (live Mar 23, 2026) | None (deflationary via burn; effective inflation cut to ~7.1%) | **Live (BME buy-and-burn)** | None |
| **io.net (IO)** | IDE (live Jun 11, 2026) | None (deflationary via burn) | Live, but currently **emission-funded** (marketed ≥50% surplus-revenue buy-and-burn not yet operating; demand-driven emissions switched off per Jul 2026 explorer analysis) | None |
| **Gonka (GNK)** (Proposed) | **20/70/5/5 split** | **5% to veGNK stakers + surplus** | **5% continuous TWAP burn (proposed)** | **veGNK (1mo-2yr lock)** |

**Gonka's Competitive Moat (revised):** Buyback-and-burn is now common in the category (Akash, io.net, Render). Gonka's remaining differentiator is **direct yield distribution to lockers** — 5% of inference revenue plus AI Training Fund surplus paid to veGNK holders — which no competing AI compute network currently offers. At $10M annual inference revenue, this generates ~$500K annual buyback pressure and ~$500K+ in staker yield.

**Why GNK May Appreciate:**
1. **Efficiency leadership:** Highest productive compute ratio
2. **Usage-based demand:** Every inference requires GNK purchase
3. **Supply constraints:** Halving reduces new supply
4. **Network effects:** More hosts → better service → more developers → more demand

---

#### Incentive #2: Defensible Token Economics

**GNK Token Utility:**
```
1. Payment: Developers MUST hold GNK to pay for compute
2. Governance: Voting weight proportional to PoC + collateral
3. Collateral: Hosts lock GNK to maximize earning weight
4. Staking: Locked tokens reduce circulating supply
```

**Why This Creates Demand:**
- Unlike "governance-only" tokens, GNK has forced utility
- Every inference = GNK demand
- Collateral requirements = GNK locked (reduced supply)
- No alternative payment method

---

## 3. The Complete Economic Cycle — Simple Explanation

### 3.1 Visual Economic Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    GONKA ECONOMIC CYCLE                         │
└─────────────────────────────────────────────────────────────────┘

    ┌──────────────┐
    │   STEP 1:    │
    │   MINING     │         Every epoch: 323,000 GNK minted
    │              │         (halving every ~4 years)
    └──────┬───────┘
           │
           ▼ GNK rewards distributed to hosts
    ┌──────────────┐
    │   STEP 2:    │         Rewards vest gradually (180 epochs default)
    │  CIRCULATION │         Hosts can: hold, sell on exchange, or
    │              │         convert via Community Pool
    └──────┬───────┘
           │
           ▼ GNK enters market / exchanges
    ┌──────────────┐
    │   STEP 3:    │         Developers buy GNK on exchanges
    │   DEMAND     │         Pay for inference tasks
    │              │         20% → AI Training Fund
    └──────┬───────┘         80% → Hosts who execute tasks
           │
           ▼ GNK returns to hosts
    ┌──────────────┐
    │   STEP 4:    │         Price rises → More hosts join → More supply
    │ EQUILIBRIUM  │         Price falls → Hosts leave → Less supply
    │              │         Dynamic pricing adjusts costs automatically
    └──────────────┘
```

### 3.2 Token Flow Detailed Breakdown

**Step 1: Token Generation (Mining)**

```
New GNK Created = Epoch Emission × (1 - Already Distributed %)

Distribution = Proportional to Proof of Compute (PoC) weight

PoC Weight = f(Sprint performance, Collateral deposited, Historical reliability)
```

**Sprint Mechanism (Proof of Compute) — Technical Specification:**

```
Sprint Model: 2.3 billion parameter Transformer
- 64 layers, 128 attention heads, 512 embedding dim
- Feed-forward hidden: 8,192 | Vocabulary: 8,192 | Sequence: 4

Procedure:
1. Sprint Seed generated from blockchain state (unpredictable, same for all)
2. All hosts start simultaneously (~10 minute window)
3. Hosts iterate nonces to find "Appropriate Vectors" near Target Vector
4. Distance threshold: ~1 in 900 chance per nonce
5. Valid nonces → voting weight → reward share
6. Between Sprints → GPUs perform actual AI inference
```

**Anti-Gaming Measures:**
- Random permutation of output vectors prevents continuity exploitation
- Node Seed (from public key) prevents result copying
- Sprint Seed prevents pre-computation

**Step 2: Token Entry into Circulation**

```
Host Receives: Mining Rewards (Reward Coins) + Work Fees (Work Coins)

Vesting System (from Official Tokenomics):
- Personalized scheduling: Track rewards per participant daily
- Efficient processing: Spread evenly across vesting period
- Automatic management: No intervention required
- Daily releases: Oldest entry released each day

Default Vesting Period: 180 epochs (~6 months)
Unlock Frequency: Once per epoch in equal amounts
Fractional amounts: Added to first day (no coins lost to rounding)
```

**Queryable Vesting Information:**
- Total amount to be vested
- Detailed breakdown (array of future unlocks)
- Total amount already released

**Liquidity Options:**
- **Hold:** Speculate on price appreciation
- **Sell on exchange:** Convert to USD/stablecoins — as of Jul 2026 via OTC (HEX Exchange) or SafeTrade (GNK/USDT); no major CEX listing yet and 24h volume is only ~$33K (CMC). Verify wrapped-GNK contracts before use: likely-impostor "Gonka AI" Solana listings trade ~2,500x below real GNK (see Market Status)
- **Community Pool:** 120M GNK for early liquidity (USDT/ETH/BTC conversion)
- **Lock as collateral:** Increase earning weight (up to 80% boost)

**Step 3: Token Demand (Developer Usage)**

```
Developer Payment Flow:

1. Developer deposits escrow (max potential cost based on completion token limit)
2. Inference task executes across host network
3. Actual cost calculated: Final Fee = Tokens × UnitsOfCompute × UnitPrice
4. Payment distributed: 80% to executing hosts, 20% to AI Training Fund
5. Remaining escrow refunded immediately to developer
```

**Step 4: Equilibrium & Price Discovery**

```
Supply/Demand Balancing:

IF demand > supply:
  → Utilization > 60%
  → Dynamic pricing increases (up to 2%/block)
  → Higher prices attract more hosts
  → Supply increases → Utilization normalizes

IF supply > demand:
  → Utilization < 40%
  → Dynamic pricing decreases (down to floor)
  → Lower prices attract more developers
  → Demand increases → Utilization normalizes

IF GNK price rises:
  → USD cost per inference increases
  → Some developers leave (price elastic)
  → Dynamic pricing reduces GNK-denominated cost
  → More hosts join (attracted by higher USD earnings)
  → Increased supply → prices moderate

IF GNK price falls:
  → USD cost per inference decreases
  → More developers join (cheaper compute)
  → Some hosts leave (unprofitable)
  → Remaining hosts get larger share
  → Equilibrium at new price level
```

---

## 4. Extreme Scenarios & System Balancing

> **Note (Jul 2026):** The scenarios below use an illustrative 500-GPU network at GNK = $1. The live network is ~1,200 active GPUs with GNK at ~$0.13. Scenario 4.2 (80% crash) approximately materialized: GNK fell ~95% from its $2.61 January 2026 ATH to $0.13 by July 2026, and the network first grew (~5,000 H100-eq Nov 2025 → ~12,000 Dec 2025 → ~14,000 announced Feb 2026) then contracted to ~1,200 live GPUs by July 2026 per the live counters — the host-exodus-then-stabilization pattern the "graceful contraction" logic below predicts, with per-GPU rewards for remaining hosts roughly an order of magnitude higher than at the announced peak.

### 4.1 Scenario: GNK Token Price 10x Increase

**Trigger:** Massive adoption, exchange listings, institutional buying

**Immediate Effects:**

| Stakeholder | Before (GNK=$1) | After (GNK=$10) | Impact |
|-------------|-----------------|-----------------|--------|
| Developer | $0.50/1M tokens | $5.00/1M tokens (if unchanged) | 10x cost increase |
| Host | $68/day | $680/day | 10x revenue increase |
| Network | 500 GPUs | Attracts new hosts | Supply expands |

**System Self-Correction:**

```
Phase 1: Price shock
- Developer costs spike in USD terms
- Some developers pause non-critical workloads
- Utilization drops below 40%

Phase 2: Dynamic pricing kicks in
- Per-token GNK cost decreases (up to 2%/block)
- New equilibrium: pay ~0.15 GNK instead of 0.50 GNK per 1M tokens
- USD cost stabilizes at ~$1.50 (3x increase, not 10x)

Phase 3: Supply expansion
- Higher USD earnings attract new hosts
- Network grows from 500 → 2000+ GPUs
- Competition increases → per-GPU rewards decrease
- New hosts bid lower prices → further cost reduction

Phase 4: New equilibrium
- Developers pay ~$1.50-2.00/1M tokens (competitive with alternatives)
- Hosts earn ~$200-300/day (still above traditional rental)
- Network has more capacity for growth
```

**Protection Mechanisms:**
- Developer price limits prevent overpaying
- Dynamic pricing has 2% max change per block (gradual)
- Increased supply automatically moderates prices
- Hosts can hedge by holding GNK reserves

---

### 4.2 Scenario: GNK Token Price 80% Crash

**Trigger:** Market correction, competitive pressure, regulatory concerns

**Immediate Effects:**

| Stakeholder | Before (GNK=$1) | After (GNK=$0.20) | Impact |
|-------------|-----------------|-------------------|--------|
| Developer | $0.50/1M tokens | $0.10/1M tokens | 80% cost reduction |
| Host | $68/day | $13.60/day | Below profitability |
| Network | 500 GPUs | Some hosts leave | Supply contracts |

**System Self-Correction:**

```
Phase 1: Host exodus
- Mining becomes unprofitable for high-cost operators
- ~60% of hosts may exit (leaving efficient operators)
- Network contracts to ~200 GPUs

Phase 2: Remaining host economics
- Fixed emission divided among fewer hosts
- Per-GPU rewards increase 2.5x
- Remaining hosts earn ~$34/day (survivable)

Phase 3: Developer influx
- 80% cost reduction attracts price-sensitive developers
- New use cases become economical
- Utilization increases → work fees increase

Phase 4: New equilibrium
- Smaller but profitable network
- Extremely competitive pricing attracts volume
- Token demand from developers supports price floor
- Gradual recovery as network proves reliability
```

**Key Insight:** The system contracts gracefully — hosts who leave increase rewards for remaining hosts, while cheap prices attract developers who create demand.

---

### 4.3 Scenario: Demand Exceeds Supply (Network Congestion)

**Trigger:** Viral application, sudden AI demand spike

**System Response:**

```
Utilization > 60% Triggers:

Block 1: Price +2%
Block 2: Price +2% (compounding)
Block 3: Price +2%
...
Block 50: Price ~+170% from baseline

Developer Response:
- Non-urgent tasks defer to off-peak
- Price-sensitive developers hit limits, tasks fail gracefully
- Premium developers continue (pay higher rates)

Host Response:
- Higher prices signal opportunity
- New hosts deploy GPUs
- Supply increases over days/weeks

Resolution:
- New capacity online → utilization drops
- Prices moderate → sustainable growth
- Network proved it can scale
```

**Developer Protections:**
- Max price limits prevent surprise costs
- Tasks fail rather than overpay (predictable)
- Per-model pricing allows switching to less-congested models
- Queue during congestion, execute when capacity available

---

### 4.4 Scenario: Zero Developer Demand (Empty Network)

**Trigger:** Competitive obsolescence, regulatory shutdown in key markets

**System Response:**

```
Utilization → 0% Effects:

Mining continues:
- Epoch emissions still distributed (323,000 GNK/epoch)
- Hosts receive mining rewards regardless of demand
- Work fees = $0 (no inference revenue)

Price floor activates:
- Dynamic pricing drops to floor (1 nicoin per AI token)
- Extremely cheap → attracts any marginal demand
- Even testing/development becomes nearly free

Host economics:
- Revenue = Mining only (no work fees)
- At $1 GNK, ~$58/day mining only
- Some hosts exit, but not all

Long-term:
- Cheap prices may attract niche use cases
- Privacy-focused developers, censorship-resistant applications
- Gradual recovery possible if product-market fit found
```

**Structural Safeguards:**
- Mining rewards continue regardless of demand (bootstrapping)
- Price floor prevents zero-cost abuse
- Community Pool provides exit liquidity even without exchanges
- Governance can adjust parameters if needed

---

### 4.5 Scenario: Gonka More Expensive Than Centralized Alternatives

**Trigger:** High GNK price + low network efficiency + aggressive competitor pricing

**When This Occurs:**

| Condition | GNK Price Required |
|-----------|-------------------|
| More expensive than OpenAI GPT-4o | GNK > $20 |
| More expensive than DeepSeek V4 Flash | GNK > $0.28 |
| More expensive than self-hosted H100 | GNK > $3 |

**Developer Segmentation Response:**

| Developer Type | Response | Why They Stay/Leave |
|----------------|----------|---------------------|
| Cost-only | Leave for centralized | No differentiation |
| Privacy-focused | Stay | No logging worth premium |
| Censorship-resistant | Stay | No alternative exists |
| Open-source advocates | Stay | Support ecosystem |
| Enterprise compliance | Leave | Need SLAs, support |

**System Correction:**
1. Cost-sensitive developers leave → utilization drops
2. Dynamic pricing reduces GNK-denominated costs
3. New equilibrium serves premium segments
4. If token price corrects, cost advantage returns

**Key Insight:** Gonka's defensible market is privacy/censorship-resistance. Pure cost competition is vulnerable to GNK price spikes.

---

### 4.6 Scenario: Malicious Host Attack

**Attack Vectors:**

| Attack | Description | Detection Method |
|--------|-------------|------------------|
| Fake results | Return garbage instead of inference | Randomized verification |
| Result copying | Copy another host's work | Cryptographic task binding |
| Downtime fraud | Claim availability without serving | Heartbeat + random tasks |
| Sybil attack | Create many fake host identities | PoC weight requires real compute |

**Penalty System (Official Parameters):**

| Setting | Default Value | Description |
|---------|---------------|-------------|
| Malicious Behavior Penalty | 20% | Penalty for cheating or providing false results |
| Poor Performance Penalty | 10% | Penalty for missing too much work |
| Performance Threshold | 5% missed | How much work can be missed before penalties apply |
| Unbonding Period | 1 epoch | Collateral remains slashable during withdrawal |

```
Caught cheating: 20% collateral slashed
Poor performance (>5% missed): 10% collateral slashed
Reputation reset: 100% verification rate until trust rebuilt
Accumulated rewards: FORFEITED for that cycle
```

**Why Cheating Doesn't Pay:**

```
Expected Value Calculation:

Honest Host:
- Revenue = R (certain)
- Cost = C (compute cost)
- Net = R - C

Cheating Host:
- Revenue if not caught = R + (saved compute cost)
- Probability of detection = P (randomized verification, 1-10%)
- Penalty if caught = 20% collateral + all cycle rewards
- Expected Value = (1-P)(R + saved) - P(Collateral × 20% + Rewards)

For P > 10-15%, cheating has negative expected value
```

**Reputation-Based Verification (Official Formula):**
```
Validation Frequency = 1 − (1−0.01) × MIN(DAYS_OF_REPUTATION, N) / N

Where N = 30 (default)
- Day 0: 100% of tasks validated
- Day 15: ~50% of tasks validated
- Day 30+: 1% of tasks validated
```

**Verification Economics:**
- High-reputation hosts: 1% verification rate (trusted)
- New hosts: 100% verification rate
- Random, unpredictable selection prevents gaming
- Verification cost shared across network based on weight

---

### 4.7 Scenario: Collateral System Stress Test

**Official Collateral Model Parameters:**

| Parameter | Default Value | Governance-Adjustable |
|-----------|---------------|----------------------|
| Base Weight Ratio | 20% | Yes |
| Collateral-Eligible Weight | 80% | Yes |
| Collateral Per Weight Unit | 0.0625 GNK per nonce | Yes |
| Grace Period | 180 epochs (~6 months) | Yes |
| Unbonding Period | 1 epoch | Yes |
| Malicious Behavior Penalty | 20% | Yes |
| Poor Performance Penalty | 10% | Yes |
| Performance Threshold | 5% missed | Yes |

```
Weight Calculation:
- Base Weight = Potential Weight × 0.20 (unconditional)
- Collateral-Eligible = Potential Weight × 0.80 (requires backing)
- Full Weight = Base + min(Collateral Deposited / Required, 80%)

Example (H100 with 1,600 nonces/epoch):
- Required for full weight: 1,600 × 0.0625 = 100 GNK
- Partial collateral (50 GNK): 20% + 40% = 60% weight
```

**Stress Scenario: Mass Collateral Withdrawal**

```
Trigger: GNK price crash, hosts fear further losses

Phase 1: Withdrawal requests
- Many hosts initiate collateral withdrawal
- Unbonding queue fills up
- Remaining collateral still slashable

Phase 2: Weight reduction
- Withdrawing hosts drop to 20% base weight
- Their share of rewards decreases 4x
- Committed hosts (collateral intact) gain larger share

Phase 3: New equilibrium
- Committed hosts earn more (less competition)
- Withdrawing hosts earn less (lower weight)
- Network smaller but more committed

Protection: Unbonding period prevents instant exit
Benefit: Remaining hosts have higher skin-in-the-game
```

---

## 5. Prediction Scenarios

### 5.1 Bull Case: Mass Adoption

**Assumptions:**
- AI inference market grows 10x to $100B+ by 2030
- Decentralized compute captures 5-10% ($5-10B)
- Gonka achieves 20% market share of decentralized AI
- Major exchange listings, institutional adoption

**Projections:**

| Metric | Year 1 | Year 3 | Year 5 |
|--------|--------|--------|--------|
| Network GPUs | 1,000 | 50,000 | 500,000 |
| Daily Inference Revenue | $10,000 | $1,000,000 | $10,000,000 |
| Active Developers | 5,000 | 100,000 | 1,000,000 |
| GNK Price (Est.) | $2-5 | $10-25 | $25-100 |
| Network Value (FDV) | $2-5B | $10-25B | $25-100B |
| Competitive Position | Niche | Contender | Leader |

**Impact by Role:**

| Role | Year 1 | Year 5 |
|------|--------|--------|
| Developer | 50-80% cost savings | Industry-standard API, full model selection |
| Host | $100-300/day per H100 | $500-2000/day per H100 |
| Investor | 2-5x from current | 25-100x from current |

**Catalysts Required:**
1. Exchange listings (Binance, Coinbase)
2. Enterprise adoption (Fortune 500)
3. Regulatory clarity (not classified as security)
4. Technical reliability proof (99.9% uptime)
5. Model quality parity with OpenAI

---

### 5.2 Base Case: Steady Growth

**Assumptions:**
- AI market grows 3x by 2030 (conservative)
- Decentralized compute remains niche (<1% of market)
- Gonka finds product-market fit with privacy-focused developers
- Mid-tier exchange listings, moderate liquidity

**Projections:**

| Metric | Year 1 | Year 3 | Year 5 |
|--------|--------|--------|--------|
| Network GPUs | 500 | 5,000 | 25,000 |
| Daily Inference Revenue | $1,000 | $50,000 | $200,000 |
| Active Developers | 500 | 10,000 | 50,000 |
| GNK Price (Est.) | $0.50-1 | $2-5 | $5-15 |
| Network Value (FDV) | $500M-1B | $2-5B | $5-15B |
| Competitive Position | Experimental | Niche | Established Niche |

**Impact by Role:**

| Role | Year 1 | Year 5 |
|------|--------|--------|
| Developer | Cost savings for specific use cases | Reliable alternative for privacy needs |
| Host | $30-70/day per H100 | $100-300/day per H100 |
| Investor | 0.5-1x from current | 5-15x from current |

**This Scenario If:**
- No major negative catalysts
- Steady organic growth
- Competition remains fragmented
- Regulatory environment neutral

---

### 5.3 Bear Case: Failure to Achieve Product-Market Fit

**Assumptions:**
- Centralized providers cut prices aggressively
- Regulatory crackdown on crypto/AI integration
- Technical challenges prevent scaling
- No meaningful exchange listings

**Projections:**

| Metric | Year 1 | Year 3 | Year 5 |
|--------|--------|--------|--------|
| Network GPUs | 200 | 500 | 100 (declining) |
| Daily Inference Revenue | $100 | $500 | $50 |
| Active Developers | 100 | 200 | 50 |
| GNK Price (Est.) | $0.10-0.30 | $0.05-0.15 | <$0.05 |
| Network Value (FDV) | $100-300M | $50-150M | <$50M |
| Competitive Position | Experimental | Struggling | Failed |

**Impact by Role:**

| Role | Year 1 | Year 5 |
|------|--------|--------|
| Developer | Limited reliability | Network too small for production |
| Host | $10-30/day (unprofitable) | Exit to other opportunities |
| Investor | -50-70% from current | -90%+ from current |

**This Scenario If:**
- OpenAI cuts prices 50%+
- SEC classifies GNK as security
- Major technical outage erodes trust
- Bittensor/Render capture all mindshare

---

### 5.4 Key Success Factors to Watch

| Factor | Positive Signal | Negative Signal | Status (Jul 2026) |
|--------|----------------|-----------------|-------------------|
| Developer adoption | Growing inference volume | Flat/declining usage | 2,200+ developers (Feb 2026 figure, unverified since); live lineup (Jul 16, 2026): MiniMax M2.7 (sole PoC), GLM-5.2, Kimi K2.6 (re-bootstrapping) — Qwen3-235B retired Jun 25, 2026 |
| Host growth | More GPUs joining | Hosts leaving | ~1,200 GPUs live (Jul 2026: joingonka.ai 1,178, tracker.gonka.vip ~1,214; down from the ~14,000 announced Feb 2026 and ~4,648 in Apr 2026); ~113 independent participants / ~582 MLNodes (Apr 2026 figures, unverified since); nodes in ~20 countries. Track live via gonka.gg, gonkascan.com, gonkahub.com, tracker.gonka.vip |
| Token liquidity | Exchange listings, volume | Illiquid, wide spreads | No major CEX listing; ~$33K daily volume (CMC) via OTC (HEX) and SafeTrade; impostor Solana "wrapped" listings circulating; GNK ~$0.13 |
| Technical reliability | Consistent uptime | Frequent outages | Mainnet live since Aug 2025; regular upgrades through v0.2.13-post7 + devshard v3; Kimi K2.6 failed validation twice in three weeks (removed Jun 25 via Prop 78, restored Jun 26, removed again Jul 15) — recurring model-availability incidents; PoC-v2 weight-validation exploit attempted live and hotfixed Jul 6 (v0.2.13-post7) |
| Competitive pricing | Cheaper than alternatives | More expensive | Very cheap at $0.13 GNK (developer-favorable, host-unfavorable) |
| Funding momentum | Continued investment | Investor exodus | $80M+ raised from Coatue and Bitfury Capital (Jul 2026 marketing); Bitfury $50M commitment (Dec 2025); GAIB GAIC public window closed Jul 5, 2026 |

**v3.0 Update -- Additional Key Success Factors:**

| Factor | Positive Signal | Negative Signal | Target Metric |
|--------|----------------|-----------------|---------------|
| **Fee-to-emission ratio** | Fee % of host revenue growing | Fee % stagnant or declining | >50% by Year 8 |
| **Developer growth rate** | >15% annual growth | <10% annual growth | 6K (6mo) -> 15K (18mo) -> 25K (36mo) |
| **veGNK lock rate** | >35% of circulating supply locked | <20% after 6 months | 35-50% target |
| **GPU fleet modernization** | B200/Blackwell adoption | Stuck on H100 only | Achieved: ~20 GPU types supported incl. B200 (recommended for optimal mining rewards); GAIB partnership onboarding B200 capacity |
| **POL liquidity depth** | <1% slippage for $50K trades | >3% slippage for $50K trades | $3-5M total depth |
| **Floor defense trigger count** | 0 (price above floor) | Frequent triggers | <2 per year |

**v3.1 Update -- Revised Prediction Adjustments:**

The prediction scenarios in Sections 5.1-5.3 should be interpreted with these adjustments:

- **GPU pricing impact (corrected):** The v3.0 assumption of continuous 30-50% annual H100 deflation did not hold. Rental deflation stalled in 2026 (Jul 2026 median $2.29-3.12/hr, roughly flat YoY); hardware acquisition costs reversed upward (+30-50%) due to the memory supercycle, whose price gains are decelerating but less than first reported (Q3 2026 DRAM +13-18% QoQ vs ~60% in Q2, with TrendForce's ~Jul 8-9 revision making 13-18% the conservative floor). Stable-to-firming rental rates support host USD revenue math, but the "cheap legacy H100" 2028 projection ($0.30-0.80/hr) is invalidated and hardware capex stays elevated through 2026.
- **Developer acquisition cost declining:** From $500-2,000 (2022) to $150-500 (2026). OpenAI-compatible API reduces Gonka's developer acquisition cost to the lower end.
- **Blackwell transition (corrected):** B200 shipped in early 2025 and is already supported on Gonka (recommended GPU for optimal mining rewards). Hosts on Blackwell gain 2x+ inference throughput; the next hardware wave, Vera Rubin, is mass-shipping this summer but with a slightly delayed ramp (thermal/HBM4 issues; 2026 shipment share cut ~29% → ~22%; Rubin Ultra reportedly cancelled/scaled back; Kyber rack delayed to 2028) — less 2026 Rubin supply supports firm H100/H200/B200 rental prices.
- **Oracle-based USD pricing:** If implemented, prediction scenarios based on fixed GNK-denominated pricing become obsolete; USD-benchmarked pricing automatically adjusts with market conditions.
- **Macro conditions:** With crypto in a bear market (total cap ~$2.2T, -43% YoY) and GNK at ~$0.13, Year 1 outcomes are tracking between the Base and Bear cases on price; the live ~1,200-GPU count sits just above the Bull case's Year 1 target (1,000 GPUs) but far below the ~14,000 announced peak.
- **Demand-side evidence (new):** Inference is roughly two-thirds of all AI compute in 2026 (Deloitte); token consumption is projected to grow ~24x to 120 quadrillion tokens/month between 2026-2030; agentic workloads consume 5-30x more tokens per task; token prices fell ~280x over two years while total enterprise AI spend rose ~320% — volume-driven growth, the core Gonka demand thesis. NVIDIA's Jensen Huang publicly endorsed decentralized AI training in 2026, and the Covenant-72B decentralized training run succeeded.

---

### 5.5 Comparative Analysis: Gonka vs. Competitors

| Dimension | Gonka | Bittensor | Render | Akash | io.net |
|-----------|-------|-----------|--------|-------|--------|
| **Focus** | AI Inference | AI Marketplace | GPU Rendering | General Cloud | GPU Aggregation |
| **Productive Compute** | ~98% | ~40% | ~90% | Variable | High |
| **Token Model** | Bitcoin-style halving | Subnet alpha tokens | Job-based | Bidding market | Usage-based |
| **Market Cap (Jul 2026)** | ~$13.9M | ~$1.9-2.2B | ~$784M | ~$157M | Growing |
| **Unique Value** | Highest efficiency | Subnet ecosystem | Creative industry | Broad compute | Multi-source |
| **API Compatibility** | OpenAI-compatible | Custom | Custom | Custom | Custom |
| **Collateral Required** | Yes (80% weight) | Staking | No | Deposit | Variable |
| **Real Yield** (v3.1) | **Proposed (5% + surplus)** | None | None (BME) | None (BME) | None (IDE burn) |
| **veToken Governance** (v3.1) | **Proposed (veGNK)** | None | None | None | None |
| **Buyback-Burn** (v3.1) | **Proposed (5% TWAP)** | None | Implicit (BME) | **Live (BME, Mar 2026)** | **Live (IDE, Jun 2026)** |
| **POL** (v3.1) | **Proposed (22M GNK)** | None | None | None | None |

**Omitted competitor — Aethir (ATH):** The highest-earning protocol in decentralized compute ($127.8M FY2025 revenue; ~$147-166M ARR exiting 2025, though Aethir itself has also cited a lower $126.0M ARR figure and analysts flag the inconsistency; no 2026 quarterly figures published as of Jul 2026; 150+ enterprise clients across AI training, Web3 infra, and cloud gaming). Aethir competes on enterprise GPU supply rather than token-incentivized inference, but any revenue comparison in this category is incomplete without it.

**New entrants and moves since April 2026:**
- **Gensyn ($AI):** mainnet live Apr 22, 2026; $AI TGE Apr 29 with Binance Alpha/Coinbase/KuCoin/Bitget listings (one of 2026's most volatile debuts); >5,000 H100-eq reported hashrate on day one; Delphi prediction-market app burns 70% of protocol revenue
- **BitTorrent BTTInferGrid:** decentralized AI-inference DePIN launched Jun 17, 2026 — a direct decentralized-inference entrant, bootstrapping through 2026 with enterprise/developer APIs planned
- **Solana convergence:** Bittensor launched canonical TAO on Solana on May 5, 2026 (announced at Solana Accelerate USA via Wormhole Labs' Sunrise gateway, enabling native trading on Jupiter/Meteora; coinciding with Grayscale opening its Bittensor Trust for private placement), while Akash is evaluating Solana as its migration target — Gonka's two largest decentralized competitors are converging on Solana liquidity/distribution
- **Gensyn market status (mid-Jul 2026):** $AI trades ~$0.023 (~$32M mcap, rank ~#579), roughly -78% from its $0.1035 ATH; gained an Upbit listing (KRW/BTC/USDT) and a canonical Uniswap V3 deployment on the Gensyn L2 supporting automated buybacks; mainnet/Delphi (Apr 22, 2026) remain live
- **Minor new entrant:** Tianrong Internet Products (OTC: TIPS) entered decentralized AI inference with its DEPINfer GPU-aggregation ecosystem and launched DEPIN Studios on Jul 6, 2026 — a small but new US-listed entrant in Gonka's segment

**Gonka's Defensible Advantages:**
1. **Efficiency leadership:** Only network with ~98% productive compute
2. **API familiarity:** OpenAI-compatible = easy developer migration
3. **Focused scope:** AI inference only (not trying to do everything)
4. **Economic alignment:** Hosts, developers, investors all benefit from growth
5. **(v3.1) Yield-to-lockers differentiation:** Buyback-burn is now common (Akash BME, io.net IDE), but no competing AI compute network distributes protocol revenue directly to token lockers — veGNK real yield remains the differentiator
6. **(v3.0) Comprehensive value accrual:** POL + buyback-burn + veGNK yield creates a multi-layered economic moat

**Gonka's Vulnerabilities:**
1. **Liquidity risk:** No major CEX listing (MEXC/Gate listings never materialized); thin OTC/SafeTrade liquidity, GNK down ~95% from ATH
2. **Smaller ecosystem:** ~1,200 GPUs live (Jul 2026) and far smaller market cap and mindshare than Bittensor
3. **Less brand recognition:** Newer entrant
4. **Price sensitivity:** Cost advantage depends on GNK price (mitigated by oracle-based USD pricing proposal); at $0.13, the pressure falls on hosts rather than developers
5. **(v3.1) GPU price volatility exposure:** GPU rental pricing swings in both directions (2024-Q1 2026 deflation, then 2026 memory-supercycle reflation) require continuous EIP-1559 adaptation
6. **(v3.0) Fee-to-emission transition dependency:** Long-term sustainability requires 15-25% annual developer growth

---

## 6. Risk Summary & Considerations

### 6.1 Market Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| GNK volatility | High | Medium | Hedging, price limits, oracle-based USD pricing |
| Adoption failure | Medium | High | Focus on niche markets, developer subsidies |
| Competition | High | Medium | Efficiency differentiation, real yield moat |
| **GPU price deflation** | **Very High** | **Medium** | **Oracle-based USD pricing, dynamic EIP-1559 adjustment** |

### 6.2 Regulatory Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Securities classification | Low-Medium (reduced in 2026) | High | Legal structure, jurisdictional strategy |
| Tax complexity | High | Low | Clear guidance, compliance tools |
| AI regulation | Medium | Medium | Content-neutral protocol design |

**July 2026 Regulatory Update:** The US posture shifted materially in 2026. The SEC's "Project Crypto" under Chair Atkins (A-C-T strategy; Jan 28, 2026 staff taxonomy statement; Mar 11, 2026 SEC-CFTC MOU; Mar 17, 2026 token-safe-harbor speech) now largely classifies governance/utility tokens as "digital tools" — not securities when sold for use rather than speculation. This materially lowers the risk differential previously assigned to direct veGNK yield distribution versus buyback-and-burn. Beyond the speech track, the SEC plans to propose rules in July 2026 effectively legalizing compliant token sales: a time-limited "Innovation Exemption" allowing raises up to $75M in any 12-month period, a 12-36 month safe harbor for token issuance/trading without full registration, and a mechanism for tokens to exit securities status once creators stop exerting managerial effort. Combined with the four-category taxonomy, this further de-risks veGNK yield distribution and could allow a compliant GNK sale — directly relevant to this document's fee-distribution and treasury recommendations. Statutory clarity remains unresolved: the CLARITY Act passed the House but is stalled in the Senate as of mid-July 2026 (Senate returned Jul 13; decisive Jul 17 hearing held; prediction-market odds of passage before the Aug 7 recess ~43%), likely slipping to 2027 if not passed before the recess.

### 6.3 Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Scalability limits | Low | High | Proven architecture, gradual growth |
| Protocol/consensus bugs | Low-Medium (raised Jul 2026) | High | CertiK audit completed; rapid hotfix response demonstrated (v0.2.13-post7) |
| Centralization | Medium | Medium | PoC prevents stake concentration, veGNK monitoring |

**July 2026 security incident (first live exploit attempt):** the **v0.2.13-post7** hotfix (Jul 6, 2026) patched a **PoC-v2 weight-validation vulnerability**; per the official network-updates feed, host `gonka1w7s4pharl5qs2lupxkuw2c0gzcls8chehwafg3` was detected exploiting the flaw before the fix deployed. This is the network's first publicly disclosed live exploit attempt. It was patched quickly, but it demonstrates that the PoC-weight path — the foundation of both consensus and reward allocation in this document's economic model — is an actively probed attack surface, which is why the protocol-bug probability above is raised from Low to Low-Medium.

### 6.4 Economic Transition Risks (v3.0 Addition)

| Risk | Probability | Impact | Mitigation | Early Warning |
|------|-------------|--------|------------|---------------|
| **Fee-to-emission crossover delay** | Medium | Critical | Contingency tail emissions, developer subsidies | Year 4 fee revenue < $50M |
| **Host exodus at halving points** | Medium | High | POL for exit liquidity, veGNK yield for retention | >15% host churn in 30 days |
| **Governance concentration (Founder allocation)** | Medium | High | veGNK lock distribution monitoring, voluntary caps | >50% veGNK controlled by single entity |
| **veGNK lock rate below threshold** | Low-Medium | Medium | Boost incentives, AI Fund surplus distribution | Lock rate < 25% after 6 months |
| **Floor price breach** | Low-Medium | High | Treasury TWAP buyback at 75% of 30d TWAP + $0.45 absolute floor | GNK approaches $0.45 |
| **POL impermanent loss** | Medium | Low | Concentrated range management, quarterly rebalancing | IL exceeds 10% of position value |

**Risk Interdependency Map:**

```
Fee Revenue Growth (Critical)
    ├── Developer Adoption Rate → Determines crossover timeline
    ├── GPU Price Deflation → Compressed margins if pricing doesn't adapt
    ├── Host Profitability → Determines network capacity and security
    │       ├── Mining Rewards (decaying) → Decreasing contribution
    │       └── Inference Fees (growing) → Must compensate for decay
    └── GNK Price → Affects host USD revenue and developer costs
            ├── Buyback Pressure → 5% of inference revenue
            ├── veGNK Locking → Reduces circulating supply
            └── POL → Provides liquidity depth and price stability
```

---

## 7. Enhancement Recommendations (v3.0 Addition)

Based on 5 parallel deep research investigations conducted in February 2026, the following enhancement recommendations are prioritized for Gonka's tokenomics optimization. **As of July 2026, none of these proposals have shipped and the Q2-Q4 2026 timelines below are stale — treat them as relative sequencing, not calendar dates. POL deployment ranges and floor-defense triggers were sized at ~$1.00 GNK and must be recalibrated at current (~$0.13) prices.**

### 7.1 Priority-Ordered Implementation Roadmap

| Priority | Enhancement | Timeline | Key Parameters | Expected Impact |
|----------|------------|----------|----------------|-----------------|
| **1** | **veGNK Phase 1** | Q2 2026 | 1mo-2yr lock, linear decay | 35-50% supply locked, governance resilience |
| **2** | **Enhanced Revenue Split** | Q2-Q3 2026 | 20/70/5/5 allocation | Real yield + deflationary pressure |
| **3** | **POL Deployment Phase 1** | Q2 2026 | 8M GNK in GNK/USDC | Permanent liquidity, LP fee revenue |
| **4** | **Oracle-Based USD Pricing** | Q3 2026 | Pyth + Chainlink + UMA stack | Eliminates dual volatility |
| **5** | **Buyback-and-Burn** | Q3 2026 | 5% continuous TWAP | Deflationary pressure, reflexive value |
| **6** | **veGNK Phase 2 (Boost)** | Q4 2026 | 2.5x max boost, delegation | Increased lock motivation |
| **7** | **POL Phase 2-3** | Q3-Q4 2026 | 14M GNK in GNK/ETH + expansion | Full liquidity deployment |
| **8** | **Floor Price Defense** | Q4 2026 | 75% of 30d TWAP trigger | Price stability in downturns |
| **9** | **Developer Subsidies** | Ongoing | $50-100 free compute credits | Growth acceleration |
| **10** | **EIP-1559 +-4% Testing** | Q3 2026 | Testnet parameter adjustment | Faster market tracking |

### 7.2 Enhancement Interdependencies

```
veGNK Phase 1 ←── Required for ──→ Real Yield Distribution
       │                                    │
       ▼                                    ▼
veGNK Phase 2 (Boost)              Buyback-and-Burn
       │                                    │
       └──── Both benefit from ────────────┘
                      │
                      ▼
              POL Deployment (provides liquidity for buyback execution)
                      │
                      ▼
           Oracle-Based USD Pricing (enables competitive pricing)
                      │
                      ▼
           Floor Price Defense (requires oracle feeds + treasury allocation)
```

### 7.3 Key Design Decisions Summary

| Decision | Selected Option | Alternatives Considered | Rationale |
|----------|----------------|------------------------|-----------|
| veGNK lock range | 1 month - 2 years | 1 week - 4 years (Curve) | Lower friction, align with AI planning cycles |
| Revenue split | 20/70/5/5 | 20/80/0/0 (current), 30/60/5/5 | Balanced host income, value accrual, R&D funding |
| Buyback mechanism | Continuous TWAP | Quarterly events (BNB), threshold-only (Maker) | Lower slippage (40-60% vs. periodic), transparent |
| Burn vs. distribute | Burn all buyback (5%) + distribute yield (5%) | Distribute all, burn all | Buyback-burn benefits all holders; yield rewards lockers |
| POL venue | Uniswap v3 concentrated | Balancer 80/20, Tokemak autopilot | Maximum capital efficiency (4-5x), direct control |
| Oracle stack | Pyth + Chainlink + UMA hybrid | Single oracle, no oracle | Pyth for speed (400ms), Chainlink for security (1hr), UMA for flexibility |
| Floor defense trigger | 75% of 30d TWAP + $0.45 absolute | Static floor, no floor | Relative trigger adapts to price level; absolute prevents catastrophic breach |

---

## 8. Economic Transition Analysis (v3.0 Addition)

### 8.1 Emission Decay vs. Fee Revenue: The Critical Balance

Gonka's long-term viability depends on inference fee revenue scaling as mining emissions decay. This analysis quantifies the transition dynamics:

**Emission Decay Timeline:**

```
Mining Reward (GNK/epoch)
323,000 ████████████████████████████████  Year 0
267,738 ██████████████████████████        Year 1
183,921 ██████████████████                Year 3
152,440 ███████████████                   Year 4 (First Halving)
 71,929 ███████                           Year 8 (Second Halving)
 33,936 ███                               Year 12 (Third Halving)
  7,582 █                                 Year 20
```

### 8.2 Three-Scenario Fee Revenue Model

**Revenue projections based on developer growth rate:**

| Year | Emission Revenue (at $1 GNK) | Conservative Fee Rev (10%/yr growth) | Moderate Fee Rev (25%/yr) | Aggressive Fee Rev (50%/yr) |
|------|------------------------------|--------------------------------------|--------------------------|----------------------------|
| 1 | $107.8M | $72.6M | $211.2M | $684.3M |
| 2 | $92.6M | $79.9M | $396.0M | $2,310.8M |
| 4 | $69.4M | $96.9M | $1,236.1M | $26,312.6M |
| 8 | $41.2M | $142.4M | $12,099.4M | Very High |
| 12 | $24.4M | $209.5M | Very High | Very High |

**Conservative Scenario Crossover Point: Year 10-12**
- This is the highest-risk scenario and should be used for contingency planning
- Requires sustained 10% annual developer growth with minimal churn
- Fee revenue exceeds emission revenue around Year 4 in absolute terms, but hosts depend on combined income

**Moderate Scenario Crossover Point: Year 3-4**
- Target trajectory for Gonka's success
- Comparable to Akash Network's demonstrated fee growth trajectory (~40-75% quarterly growth)
- Fee revenue dominates host income by Year 4

### 8.3 Host Economics Under Emission Decay

**Combined host income trajectory (per host, Feb 2026 model assuming 448 hosts at $1 GNK):**

> **Denominator caveat (Jul 2026):** the 448 "hosts" figure does not match any current live source and was likely a stale or differently-defined count. Current ecosystem data reports ~113 independent participants running ~582 MLNodes (joingonka.ai, April 2026). Per-participant income would be ~4x the figures below; per-MLNode income ~0.77x. The table is retained as the original model; rebuild against live participant counts before external use.

| Year | Monthly Emission Income | Monthly Fee Income (Conservative) | Total Monthly | vs. Traditional ($1,760/mo) |
|------|------------------------|----------------------------------|---------------|----------------------------|
| 1 | $20,074 | $9,456 | $29,530 | +1,578% |
| 4 | $12,913 | $12,615 | $25,528 | +1,350% |
| 8 | $7,667 | $18,545 | $26,212 | +1,389% |
| 12 | $4,545 | $27,268 | $31,813 | +1,707% |

**Key Insight:** Even in the conservative scenario, combined host income remains well above traditional GPU rental economics ($1,760/month). The transition from emission-dominant to fee-dominant income is smooth, not cliff-like, thanks to exponential decay (rather than discrete halvings).

### 8.4 Early Warning System

| Indicator | Green | Yellow | Red | Monitoring Frequency |
|-----------|-------|--------|-----|---------------------|
| Fee revenue growth rate | >15% annual | 10-15% annual | <10% annual | Monthly |
| Host churn rate | <5% per quarter | 5-10% per quarter | >10% per quarter | Weekly |
| Developer retention | >80% 6-month retention | 60-80% retention | <60% retention | Monthly |
| Fee/emission ratio | On or above conservative trajectory | 10-20% below trajectory | >20% below trajectory | Quarterly |
| Network utilization | 40-60% (stability zone) | 20-40% or 60-80% | <20% or >80% | Per-block |

**Contingency Activation:** If 2+ indicators enter Red status simultaneously, governance should evaluate contingency plans: tail emissions, enhanced developer subsidies, or host efficiency programs.

---

## 9. Competitive Landscape Update (v3.0 Addition)

### 9.1 GPU Cloud Market Positioning (July 2026)

```
Price ($/hr per H100)
$7-8 │ ─── Hyperscalers on-demand (AWS, Azure) ──── Enterprise segment
     │
$2.7-16 │ ─── B200 (median ~$6.25; ~$2.50-3.00 at majors expected Q4 2026)
     │
$2.3-3.1 │ ─── Market median H100 (deflation stalled in 2026; roughly flat YoY)
     │
$2.0-3.5 │ ─── Budget decentralized / specialized providers
     │
$1.5-2.5 │ ─── [GONKA TARGET ZONE] ──── API-compatible, censorship-resistant
     │
~$1.4 │ ─── Cheapest (Thunder Compute) ──── Best-effort
```

*Note: the v3.0 "$0.30-0.80 by 2028" commoditization band assumed continuous 30-50% annual deflation, which the 2026 memory supercycle invalidated. The Gonka target band remains competitive at current market medians.*

### 9.2 Developer Onboarding Competitive Analysis

| Platform | Time to First Inference | Migration Effort | Free Tier | API Compatibility |
|----------|------------------------|------------------|-----------|-------------------|
| OpenAI | 2 minutes | N/A (baseline) | $5 credits | Native |
| Anthropic | 3 minutes | 5-10 min refactor | $5 credits | Custom SDK |
| Together AI | 5 minutes | Base URL change | Free tier | OpenAI-compatible |
| **Gonka (Target)** | **5 minutes** | **2-line code change** | **$50-100 credits** | **OpenAI-compatible** |
| Akash | 30+ minutes | Full refactor | None | Custom |
| Bittensor | Hours | Full refactor | None | Custom |

**Gonka's Developer Advantage:** OpenAI-compatible API means literally changing `base_url` and `api_key` -- the lowest possible migration friction. Combined with generous free compute credits ($50-100), this creates a compelling trial-to-conversion funnel.

### 9.3 Developer Growth Targets

| Milestone | Timeline | Active Developers | Blended Acquisition Cost | Key Strategy |
|-----------|----------|-------------------|-------------------------|-------------|
| Baseline | Q1 2026 | 2,200 (last verified figure) | N/A | Organic growth |
| Near-term | 6 months | 6,000 | $150-300/dev | Free credits, hackathons |
| Medium-term | 18 months | 15,000 | $200-400/dev | Enterprise pilots, integrations |
| Long-term | 36 months | 25,000 | $300-500/dev | Ecosystem maturity, word-of-mouth |

### 9.4 Floor Price Defense Architecture

**Tiered Defense Mechanism:**

| Trigger Level | Condition | Action | Allocation |
|--------------|-----------|--------|------------|
| **Level 1 (Soft)** | GNK < 90% of 30-day TWAP | Increase regular buyback rate by 1.5x | Existing 5% buyback budget |
| **Level 2 (Medium)** | GNK < 75% of 30-day TWAP | Activate treasury TWAP buyback | Up to 2.5% Community Pool annually |
| **Level 3 (Hard)** | GNK < $0.45 (25% below Bitfury Schelling at $0.60) | Full defense activation | Up to 5% Community Pool + 5-10% inference revenue |
| **Emergency** | GNK < $0.30 (50% below Schelling) | Governance emergency vote | Additional measures TBD by governance |

**Floor Defense Sustainability:** Treasury depletion is possible in a severe bear market (6+ months at -60%+). The floor defense is a speed bump, not a wall. Revenue replenishment and governance recapitalization mechanisms ensure long-term viability.

**July 2026 recalibration required:** The "severe bear" tail scenario is now the live base case — GNK trades at ~$0.13, below both the $0.45 hard trigger and $0.30 emergency trigger, and the $0.60 Bitfury Schelling point did not hold. Note also that Bitfury's total commitment is $50M (announced Dec 1, 2025), of which the $12M purchase was the first tranche; the anchor analysis and all trigger levels, POL deployment ranges, and treasury-depletion estimates in this section were designed around $1.00 GNK and must be rebuilt against current conditions before implementation.

**Oracle Integration for Floor Defense:**

| Oracle | Role | Update Frequency | Use Case |
|--------|------|-----------------|----------|
| **Pyth Network** | Price feed (speed) | 400ms | Real-time TWAP calculation |
| **Chainlink** | Price feed (security) | 1-hour heartbeat | Floor trigger verification |
| **UMA (Optimistic Oracle)** | Benchmark pricing | Weekly | GPU market rate benchmarks |

---

## 10. Conclusion: Investment Thesis by Role

### For Developers:

**Use Gonka If:**
- Cost savings matter (GNK < $10)
- Privacy/censorship-resistance required
- Open-source model preference
- Willing to accept newer platform
- **(v3.0) Want lowest migration friction** (2-line code change from OpenAI)
- **(v3.0) Need GPU pricing that tracks market** (oracle-based USD pricing)

**Avoid Gonka If:**
- Enterprise SLA requirements
- Need specific proprietary models
- Risk-averse production environment

### For Hosts/Miners:

**Join Gonka If:**
- Believe in AI compute growth thesis
- Have efficient power costs
- Willing to hold GNK (or hedge)
- Early miner economics attractive
- **(v3.0) Want to earn real yield** through veGNK locking (5% allocation + AI Fund surplus)
- **(v3.0) Seeking long-term alignment** through veGNK governance participation

**Avoid Gonka If:**
- Need predictable USD revenue
- Can't afford collateral lockup
- Prefer passive rental income

### For Investors:

**Buy GNK If:**
- Long-term AI infrastructure believer
- Accept thin liquidity (no major CEX listing; OTC/SafeTrade only as of Jul 2026)
- See asymmetric upside from a ~$13.9M market cap after a ~95% drawdown, backed by ~1,200 GPUs of live compute (Jul 2026 live counters; down from the ~14,000 announced Feb 2026)
- Diversified crypto portfolio
- **(v3.0) Value real yield** over pure speculation (5% revenue to veGNK lockers, proposed)
- **(v3.0) Want deflationary exposure** (5% buyback-burn + EIP-1559 base fee burn, proposed)
- **(v3.1) Believe yield-to-lockers is the moat** — buyback/burn is now common (Akash, io.net), direct locker yield is not

**Avoid GNK If:**
- Need immediate liquidity
- Can't stomach 80%+ drawdowns (one has already occurred: $2.61 ATH to $0.13)
- Prefer proven networks

---

## Sources

### v3.0 Research Sources (February 2026 Deep Macro-Tokenomics Research)

**POL & Liquidity Management:**
- Olympus DAO Treasury Analytics (on-chain data, $6.3M+ LP fees)
- Berachain PoL Documentation (2026 architecture)
- Tokemak v2 Autopilot Documentation (DeFiLlama TVL)
- Balancer 80/20 Pool Analytics (BAL/WETH, AAVE/WETH)
- Uniswap v3 Whitepaper (concentrated liquidity efficiency)
- Gauntlet POL Research (mercenary liquidity quantification)

**Real Yield & Buyback Protocols:**
- GMX Stats (63% staked, $250M+ distributed)
- Hyperliquid TWAP Buyback Data (MEXC Analysis, 97% allocation)
- MakerDAO Smart Burn Engine (Surplus Buffer model)
- Aave V3 Aavenomics ($1M/week buyback program)
- Curve Finance veCRV Fee Distribution
- DWF Labs (2025) Buyback vs. Dividend Academic Research

**veToken Governance:**
- Curve veCRV Analytics (45% lock rate, 2.3yr avg duration)
- Velodrome ve(3,3) Model (52% lock rate)
- Balancer veBAL Documentation (80/20 BPT lock)
- PancakeSwap veCAKE (25% lock rate, early exit data)
- Frax veFXS (42% lock rate, multi-asset model)
- Beanstalk Flash Loan Attack Analysis ($182M exploit)

**Fee Transition & Economic Modeling:**
- Sedlmeir et al. (2024) "Bitcoin Security Budget" (SSRN)
- 1kx Network (2025) Token Economics Evaluation
- Filecoin Storage Fee Growth Data (DeFiLlama)
- Akash Network Lease Income Acceleration (Q1-Q4 2024)
- Bittensor Halving Impact Analysis (Crypto.com, January 2026)

**GPU Economics & Developer Growth:**
- Fluence NVIDIA H100 Deep Dive (Q1 2026 pricing)
- Grand View Research GPU Cloud Market ($3.34B to $33.91B projection)
- Lambda Labs, CoreWeave, RunPod, Vast.ai Pricing (Q1 2026)
- OpenAI API Growth Curve (2022-2025 developer metrics)
- Stripe Developer Onboarding Research

### Primary Sources (Official Documentation)

- [Gonka Whitepaper (PDF)](https://gonka.ai/whitepaper.pdf) — "Decentralized AI: Meaningful utilization of computational power for real-world application" by David Liberman
- [Gonka Tokenomics (PDF)](https://gonka.ai/tokenomics.pdf) — "Gonka: Designing a Compute-Native Decentralized Economy" (2025-07-31)
- [Gonka Official Website](https://gonka.ai/)
- [Gonka GitHub Repository - Tokenomics](https://github.com/gonka-ai/gonka/blob/main/docs/tokenomics.md)
- [Gonka FAQ](https://gonka.ai/FAQ/)

### Secondary Sources

- [CoinMarketCap - Gonka (GNK)](https://coinmarketcap.com/currencies/gonka/) — live price/market cap and ~5,000 H100-eq network description (Jul 2026)
- [gonka.gg](https://gonka.gg/) — third-party blockchain explorer (real-time blocks, validators, GPU/ML nodes, inference map, free public API)
- [gonkascan.com](https://gonkascan.com/), [gonkahub.com](https://gonkahub.com/), [tracker.gonka.vip](https://tracker.gonka.vip/) — live network dashboards / node trackers
- [joingonka.ai — What is Gonka](https://joingonka.ai/en/knowledge/what-is-gonka/) — participant/GPU/MLNode counts (Apr 2026)
- [Gonka GitHub Releases](https://github.com/gonka-ai/gonka/releases) — v0.2.9-v0.2.13-post7 protocol upgrades, devshard runtime, governance quorum change, model lineup
- [Gonka Network Updates](https://gonka.ai/docs/network-updates) — official feed: governance proposals, model add/remove cycles, v0.2.13-post7 security hotfix and exploit disclosure
- [Bitfury $50M Investment Announcement (Dec 1, 2025)](https://www.businesswire.com/news/home/20251201364475/en/)
- [Akash Q1 2026 Report (BME activation)](https://akash.network/blog/akash-network-q1-2026-report/)
- [io.net IDE Launch](https://io.net/blog/a-new-tokenomics-for-a-new-era-the-ide-is-now-live)
- [Aethir Q3 2025 Revenue Report](https://ecosystem.aethir.com/blog-posts/aethirs-record-breaking-q3)
- [CryptoRank - Gonka Funding & Tokenomics](https://cryptorank.io/ico/gonka)
- [Bittensor Analysis - Grayscale](https://research.grayscale.com/reports/bittensor-on-the-eve-of-the-first-halving)
- [Akash Network - AkashML Documentation](https://akash.network/blog/akashml-managed-ai-inference-on-the-decentralized-supercloud/)
- [io.net Platform Comparison](https://io.net/blog/article/io-net-vs-akash-vs-render-network-which-decentralized-platform-actually-delivers)

### Academic References (from Whitepaper)

- Douillard, Arthur, et al. "DiLoCo: Distributed low-communication training of language models."
- Jia, Hengrui, et al. "Proof-of-learning: Definitions and practice."
- McMahan, Brendan, et al. "Communication-efficient learning of deep networks from decentralized data."
- Lepikhin, Dmitry, et al. "GShard: Scaling giant models with conditional computation and automatic sharding."
- Douillard, Arthur, et al. "DiPaCo: Distributed path composition."
- Nakamoto, Satoshi. "A Peer-to-Peer Electronic Cash System." (Bitcoin whitepaper reference)

---

*Document Version: 3.5 | Analysis Date: January 2026 (Enhanced February 2026; refreshed 2026-07-18)*
*Updated with official specifications from whitepaper.pdf and tokenomics.pdf*
*v3.0: Enhanced with February 2026 deep macro-tokenomics research (5 parallel investigations covering POL, real yield, veGNK, fee transition stress test, GPU economics & developer growth)*
*v3.1 (2026-07-18): Verification pass — live GNK market data ($0.13, ~$13.9M mcap), network scale (~14,000 H100-eq), PoC v2 and v0.2.9-v0.2.13 protocol updates, corrected B200/GPU-pricing timeline, Akash BME and io.net IDE competitive updates, Aethir added, Bitfury $50M commitment, 2026 US regulatory shift, bear-market recalibration flags*
*v3.5 (2026-07-18): Third verification pass against the official network-updates feed — added v0.2.13-post7 security hotfix (Jul 6, 2026) and the first publicly disclosed live exploit attempt (PoC-v2 weight-validation flaw, host gonka1w7s4ph…); corrected Kimi K2.6 model history (removed alongside Qwen3 via Proposal 78 on Jun 25, restored at weight factor 0.9 via Proposal 79 on Jun 26, re-bootstrapped epoch 311, second removal Jul 15 — the earlier "0.78 → 0.9 via Proposal 88" claim was incorrect); noted v0.2.14 remains an open PR; added CryptoRank price/ATL divergence to the market caveat; protocol-bug risk raised to Low-Medium*
*v3.2 (2026-07-18): Second verification pass — corrected free-inference grace period (90 epochs, ended ~Nov 20, 2025), v0.2.11/v0.2.12 release contents (inference shards; multi-model PoC + transaction fees), DePIN market caps repriced to July 2026 (TAO ~$1.9-2.2B, RENDER ~$784M, AKT ~$157M), io.net IDE emission-funded-burn caveat, Gensyn $AI and BTTInferGrid entrants, TAO-on-Solana convergence, Vera Rubin in production (Kyber rack delayed to 2028), H100 rental "reversal" rescoped to hardware/hyperscalers, memory-supercycle trajectory through mid-2027, SEC July 2026 token-sale rulemaking, wrapped-GNK impostor-listing caution, GAIB/Spheron/Gcore/broker-layer ecosystem developments, five-month compute-figure data gap flagged*

> **Disclaimer:** This analysis is for educational purposes only and should not be construed as investment advice. Cryptocurrency investments carry high risk, including potential total loss of capital. Recipients of GNK coin rewards may incur tax obligations depending on their jurisdiction. The legal and regulatory environment surrounding cryptocurrencies is rapidly evolving. Always conduct your own research and consult qualified financial advisors before making investment decisions.

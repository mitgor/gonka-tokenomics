# GONKA NETWORK
## Tokenomics Explained
### A Comprehensive Guide to the Decentralized AI Economy

**July 18, 2026** | Updated with live network and market data

---

> **What is Gonka?**
>
> Gonka is a decentralized AI infrastructure network that optimizes computational power for AI model training and inference. Unlike traditional crypto networks that waste resources on network security, Gonka ensures nearly 100% of computational resources are used for meaningful AI tasks. This creates a cost-competitive alternative to centralized cloud providers like AWS, Azure, and OpenAI.

---

## Table of Contents

1. [The Three Key Roles in Gonka Network](#1-the-three-key-roles-in-gonka-network)
2. [Detailed Incentives for Each Role](#2-detailed-incentives-for-each-role)
3. [The Complete Economic Cycle](#3-the-complete-economic-cycle)
4. [Extreme Scenarios & System Balancing](#4-extreme-scenarios--system-balancing)
5. [Prediction Scenarios for Gonka Network](#5-prediction-scenarios-for-gonka-network)
6. [Proposed Tokenomics Enhancements](#6-proposed-tokenomics-enhancements)
7. [Economic Outlook](#7-economic-outlook)
8. [Risk Factors & Considerations](#8-risk-factors--considerations)

---

## 1. The Three Key Roles in Gonka Network

The Gonka ecosystem operates through the interaction of three primary participants, each with distinct responsibilities and incentives.

### 1.1 Developers (Demand Side)

Developers are the consumers of AI computational services. They build and deploy AI applications using the network's distributed computing power.

**What Developers Do:**
- Submit AI inference requests (chatbots, image generation, code completion)
- Deploy AI applications that utilize open-source LLM models
- Pay for computational services using GNK tokens
- Access the network through an OpenAI-compatible API

### 1.2 Hosts/Miners (Supply Side)

Hosts are hardware providers who contribute computational resources (GPUs) to the network. They are the backbone of the decentralized infrastructure.

**What Hosts Do:**
- Run GPU nodes that execute AI inference and training tasks
- Participate in Proof of Compute (PoC) to establish voting weight
- Validate other Hosts' work to ensure network integrity
- Earn GNK tokens through mining rewards and service fees

### 1.3 Token Investors (Capital Side)

Investors purchase and hold GNK tokens, providing liquidity and market price discovery for the ecosystem.

**What Investors Do:**
- Buy GNK tokens on exchanges or through the Community Pool mechanism
- Speculate on the future value of the network and AI compute demand
- Provide exit liquidity for Hosts who want to convert GNK to stablecoins

### Role Summary Table

| Role | Primary Action | Earns | Pays |
|------|---------------|-------|------|
| Developer | Uses AI compute | Lower costs, privacy | GNK for inference |
| Host/Miner | Provides GPUs | GNK tokens | Electricity, hardware |
| Investor | Holds tokens | Capital appreciation | Fiat/crypto |

---

## 2. Detailed Incentives for Each Role

### 2.1 Incentives for Developers

#### Incentive #1: Lower Costs Than Centralized Alternatives

**WHY IT WORKS:** Gonka can offer significantly lower prices because:
- **No corporate overhead:** Unlike AWS/Azure, there's no CEO salary, marketing budget, or shareholder profit margin
- **Subsidized compute:** Early-stage token emissions effectively subsidize compute costs for developers
- **100% productive compute:** Unlike Bitcoin (0% productive) or Bittensor (40% productive), nearly 100% of Gonka's compute goes to AI tasks
- **Grace period (ended):** The first ~90 epochs (~90 days) after launch had zero inference pricing to encourage adoption; it ended around November 20, 2025, and paid, per-block dynamic pricing has been live since. (A separate 180-epoch collateral exemption for new hosts is sometimes conflated with this — they are different mechanisms.)

#### Market Context: AI Inference Pricing Comparison

##### LLM API Pricing

| Provider | Model | Input (per 1M tokens) | Output (per 1M tokens) | Notes |
|----------|-------|----------------------|------------------------|-------|
| OpenAI | GPT-4o | $3.00 | $10.00 | Premium, closed-source |
| OpenAI | GPT-4.5 | $75.00 | $150.00 | Largest model |
| Anthropic | Claude 3.5 | $3.00 | $15.00 | Premium tier |
| DeepSeek | V4 Flash | $0.14 | $0.28 | Budget leader |
| DeepSeek | V4 Pro | $0.435 | $0.87 | Flagship, thinking mode built in |
| Google | Gemini 1.5 Flash | $0.037 | $0.15 | Lightweight |
| **Gonka (via brokers)** | MiniMax M2.7-class | ~$0.003* | ~$0.01* | Decentralized, subsidized |

*Non-DeepSeek LLM API rows are an early-2026 snapshot; verify current provider rates before relying on them (DeepSeek rows reflect the July 2026 V4 lineup — V3/R1/V2 endpoints were retired after V4's April 2026 release). Gonka's effective retail pricing (via gateways such as joingonka.ai, July 2026) is ~$0.003 per 1M tokens for frontier-class open models — roughly 830x below OpenAI — reflecting GNK trading ~95% below its January 2026 ATH while on-chain prices are GNK-denominated. Pricing varies with GNK token price and network utilization.*

##### GPU Cloud Hourly Rates Comparison (July 2026)

| Segment | H100 Price/Hour | B200 Price/Hour | Best For |
|---------|-----------------|-----------------|----------|
| Hyperscalers (AWS, Azure, GCP on-demand) | ~$7-8 | Up to ~$16 | Enterprise ecosystem |
| Specialized clouds (CoreWeave, Lambda) | $2.49-3.49 (early-2026 rates) | ~$6 | AI/ML focused |
| Budget/decentralized (Vast.ai, RunPod, Thunder Compute, Akash) | $1.40-3.50 | From ~$3.20 (spot ~$2.70) | Spot/budget |
| **Market median** | **$2.29-3.12** | **~$6.25** | — |
| **Gonka Network** | Variable* | Variable* | Censorship-resistant |

*Gonka pricing varies based on GNK token value and network demand. The ~90-day free-inference grace period ended in November 2025; paid dynamic pricing is live.*

**GPU Price Trend:** H100 pricing fell 64-81% from Q4 2024 ($8-10/hr) into early 2026, and the deflation has since stalled: on-demand H100 rental averages are roughly flat year-over-year (Jul 2025 $3.89 → Jul 2026 $3.72/hr, ~-4%), with the market median at $2.29-3.12/hr and a wide provider spread ($1.40 Thunder to $6.98 Azure). What is actually rising is GPU hardware acquisition cost (+30-50% from the AI memory supercycle — DRAM contract prices up ~80% QoQ in Q1 2026 and forecast +58-63% in Q2, HBM sold out through 2026) and some hyperscaler list prices — not the rental-market median. The NVIDIA B200 (Blackwell) is not upcoming — it shipped in early 2025, rents for ~$3.20-18.53/hr on-demand (median ~$6.25, spot from ~$2.70; the once-cited $2.69 RunPod rate is stale — RunPod now lists $5.89), and is supported on Gonka itself (B200 is the recommended GPU for optimal mining rewards). Gonka's dynamic EIP-1559 pricing adjusts automatically as hardware costs move.

---

### 2.2 Gonka LLM Token Cost Calculations & Predictions

> **Understanding Gonka Pricing Mechanics**
>
> Gonka uses dynamic per-model pricing inspired by Ethereum's EIP-1559. Prices adjust based on utilization:
> - Below 40% utilization: Prices decrease to attract usage
> - 40-60% utilization (optimal zone): Prices stable
> - Above 60% utilization: Prices increase (max 2% per block)
> - Price floor: 1 nicoin per AI token (prevents zero-cost scenarios)

#### Cost Calculation Model

The cost of LLM tokens in Gonka depends on three variables:
1. **GNK Token Market Price** (in USD)
2. **Network Utilization Rate** (affects dynamic pricing)
3. **Model Complexity** (different models have different base rates)

#### Scenario Analysis: LLM Token Costs at Different GNK Prices

*Assumptions: 50% network utilization (stable pricing zone), 7B parameter model*

| GNK Price | Cost per 1M Input Tokens | Cost per 1M Output Tokens | vs OpenAI GPT-4o | Competitive? |
|-----------|-------------------------|--------------------------|------------------|--------------|
| $0.10 | $0.02 | $0.05 | 99% cheaper | Extremely |
| **$0.13 (Jul 2026 market price)** | **$0.026** | **$0.065** | **99% cheaper** | **Extremely** |
| $0.50 | $0.10 | $0.25 | 97% cheaper | Very |
| $1.00 | $0.20 | $0.50 | 93% cheaper | Yes |
| $5.00 | $1.00 | $2.50 | 67% cheaper | Yes |
| $10.00 | $2.00 | $5.00 | 33% cheaper | Marginal |
| $20.00 | $4.00 | $10.00 | Same price | No advantage |
| $50.00 | $10.00 | $25.00 | More expensive | No |

**Key Insight:** Gonka remains cost-competitive with centralized providers when GNK trades below ~$10. Above this level, the decentralization and censorship-resistance benefits must justify the premium. At the July 2026 market price of ~$0.13 (down ~95% from the $2.61 all-time high of January 2026), Gonka sits deep in the "extremely competitive" zone for developers — the cost problem today is on the host side, not the developer side. A proposed oracle-based pricing enhancement (see Section 6) would eliminate this price sensitivity entirely.

#### Cost Prediction by Model Size

*At GNK = $1.00 (moderate scenario), 50% utilization. Illustrative parameter classes only — see live-lineup note below.*

| Model Type | Parameters | Est. Input Cost/1M | Est. Output Cost/1M | Comparable To |
|------------|------------|-------------------|--------------------|--------------|
| Small | 7B | $0.15 | $0.35 | GPT-3.5 Turbo |
| Medium | 32B | $0.40 | $0.90 | Claude Haiku |
| Large | 70B | $0.80 | $1.80 | GPT-4o mini |
| XL (MoE) | 235B+ | $2.50 | $5.50 | GPT-4o |

> **Live model lineup (as of July 16, 2026):** the network serves MiniMax M2.7 (sole PoC/base model and base delegation target since Proposal 78, June 25, 2026, which removed both Qwen3-235B-A22B — retired permanently — and Kimi K2.6 for lacking validation majority), GLM-5.2 (live since June 26, 2026 via Proposal 79, weight factor 2.47, optional with no participation penalty), and Kimi K2.6 (added ~May 2026 via DevShards; removed by Proposal 78 on June 25, restored by Proposal 79 on June 26 at weight factor 0.9 and re-bootstrapped at epoch 311 on June 27; then removed a second time via expedited Proposal 87 on July 15, 2026 after again losing validation majority in epochs 328-329, and re-registered via Proposal 88 on July 16 for a second re-bootstrap at epoch 331, weight factor unchanged at 0.9). Two validation failures in three weeks is a material stability caveat. Small dense models like Qwen 7B or Llama 70B/405B are not served; the size tiers above are illustrative cost scaling only.

#### Monthly Cost Projections for Typical Use Cases

*At GNK = $1.00, using the small-model tier (illustrative):*

| Use Case | Monthly Tokens | Gonka Cost | OpenAI Cost | Savings |
|----------|---------------|------------|-------------|---------|
| Personal chatbot | 10M | $5 | $130 | 96% |
| Small startup | 100M | $50 | $1,300 | 96% |
| Mid-size app | 1B | $500 | $13,000 | 96% |
| Enterprise | 10B | $5,000 | $130,000 | 96% |
| High-volume API | 100B | $50,000 | $1,300,000 | 96% |

#### Price Adjustment Scenarios

> **Scenario A: High Demand (>60% utilization)**
>
> If network utilization exceeds 60%:
> - Prices increase by up to 2% per block
> - Example: Base price $0.20 could rise to $0.30-0.40 during peak
> - Result: Some developers defer non-urgent tasks, utilization normalizes
> - Protection: Developers can set max price limits; tasks fail rather than overpay

> **Scenario B: Low Demand (<40% utilization)**
>
> If network utilization drops below 40%:
> - Prices decrease by up to 2% per block
> - Example: Base price $0.20 could fall to $0.10-0.15
> - Result: Lower prices attract more developers, utilization increases
> - Floor: Prices cannot go below 1 nicoin per AI token

> **Scenario C: GNK Price Volatility**
>
> If GNK price moves significantly:
> - GNK +100%: USD cost doubles, but dynamic pricing can reduce GNK-denominated costs
> - GNK -50%: USD cost halves, making Gonka extremely competitive
> - Protection: Developers can hedge by holding GNK reserves
> - Long-term: Market forces balance token price with utility value

#### Break-Even Analysis: Gonka vs Competitors

*At what GNK price does Gonka lose its cost advantage?*

| Competitor | Their Price/1M Output | Gonka Break-Even GNK Price | Current Advantage Zone |
|------------|----------------------|---------------------------|----------------------|
| OpenAI GPT-4o | $10.00 | $20.00 | GNK < $20 |
| OpenAI GPT-3.5 | $2.00 | $4.00 | GNK < $4 |
| DeepSeek V4 Flash | $0.28 | $0.56 | GNK < $0.56 |
| Self-hosted H100 | $1.50 equiv. | $3.00 | GNK < $3 |
| Anthropic Claude | $15.00 | $30.00 | GNK < $30 |

**Conclusion:** Gonka's cost advantage is strongest when GNK trades below ~$5.00. Above $10, only censorship-resistance and privacy justify the premium. Below $0.50 — including at the current ~$0.13 — Gonka undercuts even the cheapest alternatives.

---

#### Incentive #2: Censorship Resistance & Privacy

**WHY IT WORKS:** Centralized providers can:
- Shut down your account without warning
- Monitor and store all your prompts/responses
- Refuse service based on content policies
- Change pricing or terms unilaterally

Gonka's decentralized nature means no single entity controls access, making it ideal for applications requiring privacy or operating in jurisdictions with restrictive policies.

#### Incentive #3: Transparent & Predictable Pricing

**WHY IT WORKS:** Gonka uses EIP-1559-inspired dynamic pricing:
- Prices adjust based on network utilization (40-60% optimal zone)
- Maximum 2% price change per block prevents sudden spikes
- Developers set maximum cost limits per task
- Per-model pricing allows cost optimization based on needs

#### Incentive #4: Access to Open-Source Model Training

**WHY IT WORKS:** 20% of all inference revenue funds the Decentralized AI Training Fund:
- Developers who contribute to model training earn revenue shares
- All trained models remain open-source (unlike Meta's conditional licensing)
- Community-governed allocation ensures training serves actual needs

---

### 2.3 Incentives for Hosts/Miners

#### Incentive #1: Higher Revenue Potential vs. Traditional Renting

**WHY HOSTS CAN EARN MORE ON GONKA:**

##### Host Revenue Comparison Table

| Revenue Source | Traditional Rental | Gonka Network | Advantage |
|---------------|-------------------|---------------|-----------|
| Base hourly rate | $2.29-3.12/hr (H100 median, Jul 2026) | Variable (mining rewards) | Potential upside |
| Customer acquisition | Required (marketing) | Automatic (protocol) | No overhead |
| Utilization risk | You bear 100% | Shared across network | Lower risk |
| Price appreciation | None (fixed USD) | GNK may appreciate | Potential 10x+ |
| Dual income | No | Mining + Work fees | 2 revenue streams |
| Downtime penalty | Lost revenue | Minimal (vesting) | Protection |

##### Host Earnings Calculator (Per H100 GPU)

*Assumptions: 90% uptime, ~1,200 H100-equivalent GPUs actively mining (live counters, July 2026: joingonka.ai shows 1,178 GPUs active, tracker.gonka.vip ~1,214; the ~5,000 figure in CoinMarketCap's project description is stale marketing text, joingonka's ~4,648 dates to April 2026, and the ~14,000 from the Feb 2026 announcement was the announced peak), GNK emissions = 323,000/epoch. Per-GPU mining share: ~269 GNK/day.*

| GNK Price | Daily Mining Reward | Daily Work Fees* | Daily Total | Monthly Total | vs Traditional Rental |
|-----------|--------------------|-----------------|-------------|---------------|----------------------|
| **$0.13 (Jul 2026)** | **$35.00** | **$5.80** | **~$40.80** | **~$1,225** | **-25% (worse)** |
| $0.18 | $48.40 | $8.10 | $56.50 | $1,695 | ~Parity |
| $0.50 | $134.50 | $22.40 | $156.90 | $4,708 | +188% (better) |
| $1.00 | $269 | $44.80 | $313.80 | $9,415 | +476% (better) |
| $2.00 | $538 | $89.70 | $627.70 | $18,830 | +1,052% (better) |
| $5.00 | $1,345 | $224 | $1,569 | $47,076 | +2,780% (better) |

*Work fees assume 30% network utilization with inference demand. Traditional rental benchmark: ~$1,635/month ($2.52/hr H100 median, 90% uptime, Jul 2026)*

**Key Insight:** At the live network size of ~1,200 active H100-equivalents, hosts beat traditional rental when GNK exceeds ~$0.18 — roughly 4x more favorable than the ~$0.75 break-even implied by the stale ~5,000-GPU figure, and 12x better than the ~$2.20 implied by the announced 14,000-GPU peak. Even so, at the July 2026 price of ~$0.13, per-GPU host earnings sit ~25% below traditional rental rates; hosts are still mining at a modest loss versus renting out the same hardware, betting on GNK appreciation and future fee revenue. Note the flip side: the small denominator that improves per-GPU math is itself a symptom of host exit.

#### Incentive #2: Bitcoin-Style Scarcity Economics

**WHY IT WORKS:** Gonka uses a deflationary emission model similar to Bitcoin:
- Initial reward: 323,000 GNK per epoch (exponential decay, ~4-year halving cycle)
- Per-epoch rewards are capped but work-proportional: a subsidy mechanism scales payouts to actual compute contributed, and rewards vest gradually rather than paying out instantly
- Fixed 1 billion total supply creates scarcity; ~106M GNK (~10.6%) circulating as of July 2026
- As more GPUs join, fewer GNK per GPU creates potential price support

##### Emission Schedule & Halving Impact

| Year | Epoch Reward | Daily Emission | Cumulative Supply | % of Total |
|------|-------------|----------------|-------------------|------------|
| Year 1 | 323,000 GNK | 323,000 GNK | ~118M | 11.8% |
| Year 4 (1st halving) | 152,440 GNK | 152,440 GNK | ~350M | 35% |
| Year 8 (2nd halving) | 71,929 GNK | 71,929 GNK | ~555M | 55.5% |
| Year 12 (3rd halving) | 33,936 GNK | 33,936 GNK | ~682M | 68.2% |
| Year 20+ | <7,582 GNK | Minimal | ~680M | 68% |

#### Incentive #3: Meaningful Work (Not Wasted Compute)

**WHY IT WORKS:** Unlike Bitcoin mining where 100% of compute is 'wasted' on hash puzzles:
- Gonka's Proof of Compute (PoC v2 since the mainnet v0.2.9 upgrade) uses only brief periods for consensus
- Remaining time performs actual AI inference for paying customers
- Hosts contribute to AI advancement, not just network security
- Lower energy waste = better environmental optics = reduced regulatory risk

##### Compute Efficiency Comparison

| Network | Productive Compute | Security Overhead | Staking Waste | Net Efficiency |
|---------|-------------------|-------------------|---------------|----------------|
| Bitcoin | 0% | 100% | 0% | 0% |
| Ethereum PoS | 0% | ~5% | ~95% | 0% |
| Bittensor | ~40% | ~10% | ~50% | 40% |
| Render | ~90% | ~10% | 0% | 90% |
| **Gonka** | **~98%** | **~2%** | **0%** | **98%** |

#### Incentive #4: Early Liquidity Support

**WHY IT WORKS:** 120 million GNK is reserved for the Community Pool:
- Hosts can exchange mined GNK for USDT/ETH/BTC without relying on exchange liquidity
- As of July 2026, GNK is not listed on major CEXs (confirmed by CoinMarketCap); real liquidity remains thin — 24h volume ~$33K per CoinMarketCap (~$59K per Crypto.com), up from ~$9K earlier in 2026 — with trading limited to OTC on HEX Exchange and SafeTrade (GNK/USDT); BitMart runs a GNK price page reporting ~$9.2K volume across "4 active markets," but spot tradability there is unconfirmed. The Community Pool remains the most meaningful exit route
- Governed by Hosts themselves (decentralized decision-making)

> **Caution:** Do not treat "wrapped GNK" listings as a reliable exit route. A Solana token labeled "Gonka AI (GNK)" (mint AE36ntk1pza8rzKTsQ8QAmJHqL8adkBvzgzXvEM4mTFU) trades on Phantom/OKX Web3 at ~$0.00005 — roughly 2,500x below real GNK — and appears to be an unofficial or impostor listing. Aggregator price feeds also diverge wildly (CMC ~$0.13, Bitget ~$0.28, CryptoRank ~$0.28 — with a different ATL of $0.1462 vs CMC's $0.1258 — Coinpaprika ~$0.44; joingonka.ai displays ~$0.17), so treat CMC as canonical on thin liquidity and verify any venue before trading.

---

### 2.4 Incentives for Token Investors

#### Incentive #1: Exposure to AI Infrastructure Growth

**WHY IT WORKS:** The AI compute market is projected to grow from $9B (2024) to $100B+ (2032). GNK token value is tied to:
- Inference demand growth (more developers using the network)
- Network effect (more Hosts = better service = more developers)
- Scarcity mechanics (fixed supply with growing utility)

##### AI Crypto Market Comparison

| Project | Focus | Market Cap | Token Price | Productive Compute |
|---------|-------|------------|-------------|-------------------|
| Bittensor (TAO) | AI Model Marketplace | ~$1.9-2.2B (Jul 2026) | ~$192-199 | ~40% |
| Render (RENDER) | GPU Rendering | ~$784M (Jul 2026) | ~$1.51 | ~90% |
| Akash (AKT) | General Cloud | ~$157M (Jul 2026) | ~$0.53 | Variable |
| Fetch.ai (FET) | AI Agents | $1-2B (early-2026 est., unverified) | $1-2 | N/A |
| **Gonka (GNK)** | AI Inference | ~$13.9M (Jul 2026) | ~$0.13 (Jul 2026) | **~98%** |

*Note: GNK trades at ~$0.13 as of July 17-18, 2026 (~106M circulating of 1B max), after an all-time high of $2.61 on January 16, 2026 — a ~95% drawdown. Gonka is not alone: the DePIN token complex sold off hard in H1 2026 (RENDER is ~89% below its $13.53 ATH; TAO and AKT fell 2-6x from early-2026 levels). The valuation gap versus competitors implies large upside if adoption converges, but also reflects the market's current discount on early-stage, thinly traded tokens.*

---

## 3. The Complete Economic Cycle

Understanding how GNK flows through the Gonka ecosystem is essential for all participants.

### 3.1 Token Supply & Distribution

| Allocation | Amount (GNK) | Percentage | Purpose |
|------------|-------------|------------|---------|
| Core Host Incentive | 680,000,000 | 68% | Mining rewards via Proof of Compute |
| Community Pool | 120,000,000 | 12% | Early liquidity, governed by Hosts |
| Founders Allocation | 200,000,000 | 20% | Team compensation & development |

### 3.2 The Economic Flow Diagram

The Gonka economy operates as a circular flow of compute demand, token rewards, and market activity:

> **STEP 1: Token Generation (Mining)**
> - Every epoch, 323,000 GNK (initially) is minted and distributed
> - Distribution is proportional to each Host's Proof of Compute (PoC v2) weight
> - PoC weight is earned during brief competitive computation periods between inference work
> - Only Hosts with GPU hardware actively running can earn rewards

> **STEP 2: Token Entry into Circulation**
> - Newly minted GNK goes to Hosts who earned it
> - Rewards are subject to vesting (gradual daily release)
> - Hosts can convert GNK to USDT/ETH/BTC via Community Pool
> - Or sell via current trading venues (OTC on HEX Exchange, SafeTrade) — major CEX listings are still pending as of July 2026 and volumes are minimal; "wrapped GNK" listings on Solana appear unofficial (see caution in Section 2.3)

> **STEP 3: Token Demand (Developer Usage)**
> - Developers need GNK to pay for AI inference services
> - They buy GNK from exchanges or directly from the Community Pool
> - Payment goes to Hosts who execute and validate the tasks
> - 20% of inference revenue funds the AI Training Fund

> **STEP 4: Equilibrium & Price Discovery**
> - If demand exceeds supply, GNK price rises, more Hosts join, more supply
> - If supply exceeds demand, GNK price falls, some Hosts leave, less supply
> - Dynamic pricing adjusts inference costs based on network utilization
> - Long-term: emission halving reduces new supply, increasing scarcity

### 3.3 Proof of Compute (PoC v2)

Proof of Compute is Gonka's consensus mechanism that determines voting weight and reward distribution. The original "Sprint" PoC design was fully replaced by PoC v2 in the mainnet v0.2.9 upgrade (subsequent releases, e.g. v0.2.13, further refined confirmation-PoC reward accounting). The core structure remains:

1. All Hosts start simultaneously (random seed prevents pre-computation)
2. Each Host runs transformer-based computations for a brief competitive period
3. Valid computation results determine PoC weight
4. Weight determines: (a) share of mining rewards, (b) voting power, (c) task allocation
5. Between PoC periods, GPUs perform real AI inference work

---

## 4. Extreme Scenarios & System Balancing

Understanding how Gonka handles edge cases is crucial for risk assessment.

### 4.1 Scenario: GNK Token Price Increases Rapidly

> **What Happens:**
>
> If GNK appreciates significantly (e.g., 10x in 6 months):
> - Developer perspective: Inference becomes more expensive in fiat terms
> - Dynamic pricing kicks in: If utilization drops below 40%, per-token prices decrease
> - Result: Price per AI token drops to maintain competitive positioning
> - Developers pay fewer GNK for same compute, offsetting the price increase

**System Response:**
- More Hosts join (attracted by higher USD-equivalent earnings)
- Increased competition = more compute supply = lower per-token prices
- Network capacity grows, absorbing more demand at lower unit costs

#### Price Impact Model: GNK 10x Appreciation

| Metric | Before (GNK=$1) | After (GNK=$10) | Net Effect |
|--------|-----------------|-----------------|------------|
| GNK price per 1M tokens | 0.50 GNK | 0.15 GNK (adjusted) | -70% GNK needed |
| USD cost per 1M tokens | $0.50 | $1.50 | +200% USD cost |
| vs OpenAI GPT-4o ($10) | 95% cheaper | 85% cheaper | Still competitive |
| Host earnings (USD) | ~$75/day | ~$750/day | +900% earnings |
| New Host incentive | Low | Very High | Supply increases |

*Illustrative model at a hypothetical $1.00 baseline; GNK trades at ~$0.13 as of July 2026 and the live network is ~1,200 active GPUs.*

### 4.2 Scenario: GNK Token Price Crashes

> **Note (July 2026): this scenario has largely played out.** GNK fell ~95% from its $2.61 all-time high (January 16, 2026) to ~$0.13 (July 17, 2026), amid a broad crypto bear market (total crypto market cap ~$2.26T, down ~43% year-over-year; BTC ~$64,000). The dynamics below are no longer hypothetical.

> **What Happens:**
>
> If GNK drops significantly (e.g., 80% decline):
> - Host perspective: Fiat-equivalent earnings drop dramatically
> - Some Hosts become unprofitable and leave the network
> - Remaining Hosts get larger share of fixed emission rewards
> - Per-GPU earnings stabilize at new equilibrium

**System Response:**
- Developer perspective: Inference becomes cheaper in fiat, attracts more users
- Increased demand leads to more inference fees, supporting remaining Hosts
- Natural equilibrium: Hosts leave until remaining ones are profitable

#### Price Impact Model: GNK 80% Crash

| Metric | Before (GNK=$1) | After (GNK=$0.20) | Net Effect |
|--------|-----------------|-------------------|------------|
| USD cost per 1M tokens | $0.50 | $0.10 | -80% (very cheap) |
| vs DeepSeek V4 Flash ($0.28) | Comparable | 64% cheaper | Major advantage |
| Host earnings (USD) | ~$75/day | ~$15/day | -80% earnings |
| Host profitability | Better than rental | Loss vs rental | Some exit |
| Remaining host share | 1/5,000th | 1/2,000th (if 60% leave) | +150% per host |

This host-exit dynamic has also played out — more sharply than earlier revisions of this document acknowledged. Network compute grew through the early crash — from ~5,000 H100-equivalents in November 2025 through ~12,000 by late December to an announced ~14,000 in February 2026 — but live counters (joingonka.ai 1,178 GPUs, tracker.gonka.vip ~1,214, July 2026) show the active network down to roughly ~1,200 H100-equivalents by mid-July 2026, below even April's ~4,648. This is consistent with marginal operators exiting at current spot economics exactly as the model predicts, while remaining hosts capture a much larger emission share (~269 GNK/GPU/day).

### 4.3 Scenario: Inference Demand Exceeds Supply

> **What Happens:**
>
> If network utilization exceeds 60%:
> - Dynamic pricing increases per-token cost gradually (max 2% per block)
> - Developers pay more for same compute
> - Higher prices attract more Hosts to join
> - Increased capacity returns utilization to optimal zone

**Developer Protection:**
- Developers set maximum cost limits - tasks fail rather than overpay
- Per-model pricing allows switching to less-congested models
- Price changes capped at 2% per block prevents sudden spikes

### 4.4 Scenario: No Demand (Empty Network)

> **What Happens:**
>
> If developer demand disappears entirely:
> - Hosts still receive mining rewards (epoch emissions continue)
> - Zero inference fees = reduced total Host income
> - Utilization drops below 40%, prices fall to floor (1 nicoin per AI token)
> - Extremely low prices may attract new developers

**Structural Safeguards:**
- Price floor prevents zero-cost scenarios, maintaining economics
- Mining rewards continue regardless of demand (early network sustainability)
- Community Pool provides liquidity independent of thin exchange/OTC trading

### 4.5 Scenario: Gonka Inference More Expensive Than Market

> **What Happens:**
>
> If Gonka inference costs exceed centralized alternatives (e.g., OpenAI):
> - Developers leave for cheaper centralized options
> - Reduced demand triggers dynamic pricing reduction
> - Prices fall toward competitive levels
> - If emission-based subsidies aren't enough, network becomes uncompetitive

**When This Could Occur:**
- GNK token price is extremely high AND network is under-supplied
- Centralized providers drastically cut prices (competitive pressure)
- Technical issues reduce network efficiency

**Mitigation:** Developers seeking decentralization/privacy benefits may pay premium. Cost-only users will use centralized alternatives until Gonka prices become competitive again.

### 4.6 Scenario: Malicious Host Attack

> **What Happens:**
>
> If a Host tries to return fake/malicious results:
> - Randomized task verification catches cheaters probabilistically
> - Caught Hosts lose ALL accumulated rewards for that cycle
> - Reputation score resets to zero (100% verification rate)
> - Collateral can be slashed (20% for cheating, 10% for poor performance)

**Why Cheating Doesn't Pay:**
- Expected value of cheating is negative due to penalty severity
- High-reputation Hosts (honest over time) face lower verification overhead
- Majority verification ensures results can be trusted

---

## 5. Prediction Scenarios for Gonka Network

These scenarios explore potential futures based on different market conditions and adoption rates.

> **Reality checkpoint (July 2026):** On compute supply, Gonka now tracks only marginally above the bull case's Year-1 projection of 1,000 GPUs — live counters show ~1,200 H100-equivalents actively mining (joingonka.ai 1,178, tracker.gonka.vip ~1,214), down from ~4,648 across ~113 independent participants in April 2026 and far below the announced ~14,000 peak of Feb 2026. Nodes span ~20 countries with H100/H200/A100-class GPUs making up >80% of compute. On token price, it is tracking between the base and bear cases: GNK at ~$0.13 versus the base case's Year-1 range of $0.50-1, amid a broad crypto bear market. The scenarios below are kept as originally modeled for reference.

### 5.1 Bull Case: Mass Adoption Scenario

> **Assumptions:**
> - AI inference market grows 10x to $100B+ by 2030
> - Decentralized compute captures 5-10% of market ($5-10B)
> - Gonka achieves 20% market share of decentralized AI compute
> - GNK token reaches price discovery and broad exchange listings

**Projected Outcomes:**

| Metric | Year 1 | Year 3 | Year 5 |
|--------|--------|--------|--------|
| Network GPUs | 1,000 | 50,000 | 500,000 |
| Daily Inference Revenue | $10,000 | $1,000,000 | $10,000,000 |
| GNK Price (est.) | $2-5 | $10-25 | $25-100 |
| Network Value | $50-100M | $1-5B | $10-50B |
| Competitive Position | Niche | Contender | Leader |

**Impact by Role:**
- **Developers:** Access to cheap, censorship-resistant AI at scale
- **Hosts:** Early miners achieve 10-100x returns; later miners still profitable
- **Investors:** Potential for 25-100x appreciation from current mining cost

### 5.2 Base Case: Steady Growth Scenario

> **Assumptions:**
> - AI market grows 3x by 2030 (more conservative)
> - Decentralized compute remains niche (<1% of market)
> - Gonka finds product-market fit with privacy-focused developers
> - GNK lists on mid-tier exchanges, moderate liquidity

**Projected Outcomes:**

| Metric | Year 1 | Year 3 | Year 5 |
|--------|--------|--------|--------|
| Network GPUs | 500 | 5,000 | 25,000 |
| Daily Inference Revenue | $1,000 | $50,000 | $200,000 |
| GNK Price (est.) | $0.50-1 | $2-5 | $5-15 |
| Network Value | $10-25M | $100-250M | $500M-1.5B |
| Competitive Position | Experimental | Niche | Established Niche |

**Impact by Role:**
- **Developers:** Viable alternative for specific use cases (privacy, censorship)
- **Hosts:** Profitable for efficient operators; marginal for high-cost setups
- **Investors:** 5-15x returns possible; tied to actual network growth

### 5.3 Bear Case: Failure to Achieve Product-Market Fit

> **Assumptions:**
> - Centralized providers remain dominant and cut prices aggressively
> - Regulatory crackdown on crypto/AI integration
> - Technical challenges prevent scaling
> - GNK fails to achieve meaningful exchange listings

**Projected Outcomes:**

| Metric | Year 1 | Year 3 | Year 5 |
|--------|--------|--------|--------|
| Network GPUs | 200 | 500 | 100 (declining) |
| Daily Inference Revenue | $100 | $500 | $50 |
| GNK Price (est.) | $0.10-0.30 | $0.05-0.15 | <$0.05 |
| Network Value | $2-5M | $1-3M | <$1M |
| Competitive Position | Experimental | Struggling | Failed |

**Impact by Role:**
- **Developers:** Network too small/unreliable for production use
- **Hosts:** Mining becomes unprofitable; exit to other opportunities
- **Investors:** 90%+ losses; token becomes illiquid

### 5.4 Key Success Factors to Watch

| Factor | Positive Signal | Negative Signal |
|--------|----------------|-----------------|
| Developer Adoption | Growing inference volume | Flat or declining usage |
| Host Growth | More GPUs joining network | Hosts leaving for alternatives |
| Token Liquidity | Exchange listings, trading volume | Illiquid, wide spreads |
| Technical Reliability | Consistent uptime, low latency | Frequent outages, slow inference |
| Competitive Pricing | Cheaper than alternatives | More expensive than centralized |
| Community Governance | Active proposals, voting | Apathy, centralized decisions |

### 5.5 Comparison to Competitors

| Network | Focus | Compute Efficiency | Est. Market Cap | Unique Value |
|---------|-------|-------------------|-----------------|--------------|
| **Gonka (GNK)** | AI Inference | ~98% | ~$13.9M (Jul 2026) | Highest efficiency |
| Bittensor (TAO) | AI Marketplace | ~40% | ~$1.9-2.2B (Jul 2026) | Subnet ecosystem; ~$43M Q1 2026 revenue |
| Render (RENDER) | GPU Rendering | ~90% | ~$784M (Jul 2026) | Creative industry |
| Akash (AKT) | General Cloud | Variable | ~$157M (Jul 2026) | Broad compute; BME burn since Mar 2026 |
| io.net | GPU Aggregation | High | Growing | Multi-source |

**Gonka's Unique Value Proposition:**
- Only network with ~98% productive compute (vs 0% Bitcoin, 40% Bittensor)
- Transformer-based Proof-of-Work optimized for AI hardware
- Built-in training fund for open-source model development
- OpenAI-compatible API for easy developer adoption

---

## 6. Proposed Tokenomics Enhancements

Based on extensive research into DeFi best practices, AI compute market dynamics, and comparable network economics, the following enhancements are proposed to strengthen Gonka's long-term economic model. These recommendations are organized by priority and explained in plain language.

### CRITICAL Priority

#### 6.1 Fee-to-Emission Transition Planning

**What it is:** As Gonka matures, mining rewards gradually decrease (like Bitcoin's halving). The network must ensure that usage fees from AI inference grow large enough to replace these declining rewards as the primary income source for GPU hosts.

**Why it matters:** Think of it like a business that receives a large startup grant (mining rewards) that decreases each year. The business needs to grow its actual customer revenue (inference fees) fast enough to replace that grant before it runs out.

**The timeline:**

| Milestone | When | Mining Rewards | What Must Happen |
|-----------|------|---------------|-----------------|
| Launch | Year 0 | 323,000 GNK/day | Build developer base |
| First Halving | Year 4 | 152,440 GNK/day (~47% of launch) | Fee revenue should provide 50%+ of host income |
| Second Halving | Year 8 | 71,929 GNK/day (~22% of launch) | Fee revenue must dominate (~80%+ of host income) |
| Third Halving | Year 12 | 33,936 GNK/day (~10% of launch) | Fees provide 90%+ of income |
| Maturity | Year 20 | <7,582 GNK/day (~2% of launch) | Fully fee-supported network |

**The good news:** Under moderate growth assumptions (25% annual developer growth), fee revenue exceeds mining rewards as early as Year 3-4. Even under conservative assumptions (10% growth), fees dominate by Year 6-8. The network's design creates a natural and manageable transition.

**Built-in safety net:** If growth is slower than expected, the network has contingency options including governance-activated tail emissions (a small ongoing mining reward to keep hosts incentivized) and enhanced developer onboarding programs funded by the Community Pool.

**Early warning indicators:** The community can monitor key metrics including the "fee ratio" (percentage of host income from fees vs. mining) and developer growth rate. If fee revenue growth falls below 10% annually by Year 4, contingency measures should be activated.

---

### HIGH Priority

#### 6.2 Protocol-Owned Liquidity (POL)

**What it is:** Instead of paying other people to provide trading liquidity for the GNK token (which is expensive and temporary), the network uses a portion of its Community Pool to create its own permanent liquidity positions on decentralized exchanges.

**An analogy:** Think of it like a business that buys its own building instead of renting office space. Renting (traditional liquidity mining) means you pay monthly and the landlord can raise rent or evict you. Buying (POL) means you own the asset, it generates value over time, and nobody can take it away.

**How it works in practice:**
- Allocate 20-25 million GNK (16-21% of Community Pool) to create permanent trading liquidity
- Deploy across two pairs: 60% in GNK/USDC (for stable exits) and 40% in GNK/ETH (for DeFi integration)
- Use concentrated liquidity on Uniswap v3 for maximum capital efficiency (4-5x more effective than traditional methods)
- The liquidity positions earn trading fees continuously, generating revenue for the protocol

**Why this is better than the alternative:**

| Approach | Cost per $1 of Liquidity Retained | Liquidity Retained After Incentives End |
|----------|-----------------------------------|-----------------------------------------|
| Traditional liquidity mining | $10 per $1 retained | 10-25% (the rest leaves when rewards stop) |
| Protocol-Owned Liquidity | $0.50 per $1 of TVL | 100% (the protocol owns it permanently) |

**Projected benefits:** $550K-$1.1M in annual LP fee revenue (3-6% APR), with 100% of the liquidity retained permanently. This revenue can be reinvested in Years 1-2 and distributed or used for buybacks in Years 3+.

**Real-world validation:** Olympus DAO pioneered this approach and earned $6.3M+ in LP fees from its treasury positions. Leading DeFi protocols allocate 15-35% of their treasuries to POL.

---

#### 6.3 Real Yield Distribution

**What it is:** Token holders who lock their GNK for the long term earn a share of the network's actual revenue from AI inference fees, not just inflationary rewards. This is "real yield" because it comes from real business activity.

**An analogy:** This is like owning stock in a company that pays dividends from its profits, rather than one that only promises your shares will go up in value. The yield is backed by real revenue from real customers using the network.

**The proposed revenue allocation model:**

| Share | Recipient | Purpose |
|-------|-----------|---------|
| 70% | GPU Hosts | Payment for running AI inference tasks |
| 20% | AI Training Fund | Funds open-source AI model development |
| 5% | Buyback & Burn | Network buys GNK and permanently removes it from supply |
| 5% | veGNK Staker Yield | Distributed to long-term token holders |

Additionally, when the AI Training Fund accumulates more than 6 months of operating expenses (following the MakerDAO "Surplus Buffer" model), the excess is distributed to long-term stakers as bonus yield.

**Why this is significant:** The competitive gap here has narrowed. Akash activated its Burn-Mint Equilibrium on March 23, 2026, burning AKT from real usage (cutting effective inflation to ~7.1%) and crossed an all-time-high ~$5M in compute spend in Q1 2026; Bittensor generated ~$43M in Q1 2026 revenue from AI customers. No competitor yet distributes revenue directly to stakers as yield, so Gonka could still be first on that specific mechanism — but the "no competitor has any real-revenue value accrual" framing no longer holds, and the window for a differentiated first move is closing.

**Projected yield:** At $10M annual inference revenue, this generates approximately $500K in annual staker yield plus an additional $500K in buyback pressure. As the network grows, so does the yield.

---

#### 6.4 Developer Onboarding Acceleration

**What it is:** A structured program to rapidly grow the number of developers using Gonka for AI inference, leveraging the network's OpenAI-compatible API as a near-zero-friction migration path.

**Why developers are key:** Developer adoption is the single most important factor determining Gonka's long-term success. More developers means more inference requests, which means more fee revenue for hosts, which makes the network more sustainable. The fee transition analysis shows that 15-25% annual developer growth is needed to ensure host profitability as mining rewards decline.

**Gonka's secret weapon -- OpenAI API compatibility:**

Switching from OpenAI to Gonka requires changing just two lines of code. This eliminates the typical weeks-long migration effort that prevents developers from trying new platforms.

**Growth targets:**

| Milestone | Timeline | Active Developers | Key Strategy |
|-----------|----------|-------------------|--------------|
| Foundation | Months 1-6 | 6,000 (from ~2,200, Feb 2026 baseline) | Free compute credits, migration guides |
| Growth | Months 7-18 | 15,000 | University programs, framework partnerships |
| Scale | Months 19-36 | 25,000+ | Self-sustaining organic growth |

**Developer acquisition cost benchmark:** $150-500 per active developer, down from $500-2,000 in 2022 as tooling and API compatibility have improved across the crypto infrastructure space.

**Marketing message:** "Same API. 70% Less Cost. Censorship-Resistant."

---

### MEDIUM Priority

#### 6.5 veGNK Governance (Vote-Escrowed GNK)

**What it is:** A governance enhancement where token holders can lock their GNK tokens for a chosen period (1 month to 2 years) to receive increased voting power and higher rewards. The longer you lock, the more influence and yield you earn.

**An analogy:** Think of it like a loyalty program with real commitment. A customer who signs a 2-year contract gets better rates and more perks than someone who signs month-to-month. The difference is that with veGNK, the commitment is enforced by a smart contract -- once you lock, you cannot unlock early.

**How it works:**
- Lock 1,000 GNK for 2 years (maximum) = 1,000 veGNK voting power
- Lock 1,000 GNK for 1 year = 500 veGNK voting power
- Lock 1,000 GNK for 1 month (minimum) = ~42 veGNK voting power
- Voting power decays linearly as your lock period approaches its end
- veGNK holders receive up to 2.5x boost on yield rewards

**Why it benefits everyone:**
- **Reduces sell pressure:** Locked tokens cannot be sold, creating price stability
- **Aligns incentives:** Only committed holders influence governance decisions
- **Prevents attacks:** Locked tokens cannot be borrowed for flash loan governance attacks (a real threat that cost Beanstalk $182M)
- **Creates real yield recipients:** Only long-term committed holders earn the 5% real yield distribution

**Rollout plan (revised; not yet launched as of July 2026):**
- Phase 1 (H2 2026): Basic lock + voting power
- Phase 2 (H1 2027): Boost mechanics + delegation
- Phase 3 (2027+): Advanced features based on community feedback

**Industry validation:** The ve-tokenomics model is battle-tested across 15+ major protocols. Curve Finance (the pioneer) has 45% of its token supply locked, with an average lock duration of 2.3 years. Successful implementations typically achieve 35-50% lock rates.

---

#### 6.6 Revenue-Based Token Buybacks

**What it is:** The network uses 5% of all inference fee revenue to continuously buy GNK tokens on the open market and permanently destroy ("burn") them. This reduces the total token supply over time, making each remaining token more valuable.

**An analogy:** This works like a company's stock buyback program. When Apple or Google buy back their own shares, each remaining share represents a larger piece of the company. Similarly, when GNK is bought back and burned, each remaining GNK token represents a larger share of the Gonka network.

**How it works in practice:**
- Buybacks execute continuously via TWAP (Time-Weighted Average Price) orders, spread across 15-minute intervals
- This gradual approach minimizes market impact and achieves 40-60% lower slippage compared to large quarterly events
- Maximum 0.5% of pool liquidity per individual order to avoid market disruption
- All bought GNK is sent to a burn address (permanently removed from circulation)

**Opportunistic acceleration:** When GNK drops more than 20% below its 30-day average price, buyback intensity triples (3x acceleration). This provides natural price support during market downturns.

**Academic support:** Research confirms that buyback-and-burn creates 2-3x more long-term value for token holders compared to direct dividend distribution, because burned tokens benefit all holders proportionally while reducing future dilution.

---

#### 6.7 Floor Price Defense

**What it is:** A transparent, rules-based system that automatically activates GNK buybacks from the treasury when the token price drops below predetermined thresholds. This provides a safety net during severe market downturns.

**An analogy:** Think of it like a central bank's foreign exchange reserves. When a country's currency drops too far, the central bank uses reserves to buy its own currency and stabilize the price. Gonka's floor defense works the same way, but it is fully automated, transparent, and governed by smart contracts rather than opaque human decisions.

**How the triggers work:**

| Condition | Action | Daily Allocation |
|-----------|--------|------------------|
| GNK drops 25% below 30-day average | Tier 1: Moderate buyback begins | 0.5% of defense fund per day |
| GNK drops below $0.45 (absolute floor) | Tier 2: Increased buyback | 1.0% of defense fund per day |
| GNK drops below $0.30 (crisis level) | Tier 3: Maximum defense | 2.0% of defense fund per day |

**Funding:** Up to 5% of Community Pool annually, plus 5-10% of inference revenue, with a target treasury of 2-5M USDC equivalent.

**Why $0.45?** Bitfury's $12M purchase at $0.60/GNK established a natural price anchor. The $0.45 threshold (25% below that level) represents a significant decline warranting programmatic support.

**These triggers need recalibration.** As of July 2026, GNK trades at ~$0.13 — already far below both the $0.45 floor and the $0.30 crisis level — during a market-wide bear phase (total crypto market cap ~$2.26T, down ~43% from the October 2025 all-time high; sustained BTC ETF outflows). The "prolonged severe bear market" that this section originally treated as a tail scenario is approximately the live base case. Had the mechanism been deployed as specified, it would have been in maximum-defense mode for months with real treasury-depletion risk. Any implementation should re-anchor thresholds to current market levels rather than the Bitfury purchase price.

**Important caveat:** Floor defense is a speed bump, not an impenetrable wall. In a prolonged severe bear market, treasury resources can be depleted. The mechanism buys time for fundamentals to reassert; it does not guarantee a permanent price floor.

---

### LOW Priority

#### 6.8 EIP-1559 Fee Parameter Optimization

**What it is:** A fine-tuning of Gonka's dynamic pricing mechanism. The current system adjusts prices by up to 2% per block. Research suggests that increasing this to 4% would allow prices to respond faster to changing market conditions while maintaining stability.

**Why it matters:** When GPU market prices move sharply in either direction (H100 rental rates fell 64-81% from Q4 2024 into early 2026, then flattened through mid-2026) or when GNK's price changes significantly, the current 2% adjustment rate may take too long to bring Gonka's prices back to competitive levels. A 4% rate would converge roughly twice as fast.

**Risk assessment:** Academic research on Ethereum's EIP-1559 shows that adjustment rates up to 6-11% remain stable, so a move from 2% to 4% is well within the safe range.

---

#### 6.9 Quadratic Voting for Community Decisions

**What it is:** An alternative voting system where the cost of additional votes increases exponentially. One vote costs 1 token, but two votes cost 4 tokens, and three votes cost 9 tokens. This prevents wealthy participants from dominating governance decisions.

**Limited application:** Quadratic voting is vulnerable to "Sybil attacks" (one person creating many wallets to get cheaper votes). However, Gonka has a natural defense: GPU-based identity verification. Hosts who operate physical hardware have verifiable on-chain identities. Therefore, quadratic voting is recommended only for host-gated Community Pool decisions, where participants are verified GPU operators.

---

### ONGOING

#### 6.10 GPU Price Monitoring and Competitive Positioning

**What it is:** A continuous program to track GPU cloud market pricing and ensure Gonka remains competitively positioned as hardware costs decline.

**Why this is ongoing:** GPU rental pricing deflated 30-50% annually through 2025 (the H100 fell from $8-10/hr in Q4 2024), then stabilized in 2026: on-demand H100 averages are roughly flat year-over-year (~-4%, Jul 2025 $3.89 → Jul 2026 $3.72/hr). Meanwhile hardware acquisition costs are rising sharply — the AI memory supercycle is intensifying, with Q1 2026 DRAM contract prices up ~80% QoQ, Q2 2026 at +58-63% (NAND +70-75%), GPU-based server prices up 30-50%, and the price peak now expected Q3-Q4 2026 with no relief before mid-2027 (HBM takes ~23% of DRAM wafer capacity). Q3 2026 contract prices are still rising, and the "deceleration" is being revised upward: on July 8-9, 2026 TrendForce raised its Q3/Q4 forecasts (PC DRAM +15-20% QoQ, up from 8-13%; server DRAM +13-18%, with US CSP long-term agreements capping increases), and module maker ADATA reportedly sees Q3 DRAM up 20-30% and NAND up 35-40% — so the 13-18% figure is now the conservative end, not the consensus, and 2027 hardware-cost relief looks less likely. Some hyperscaler list prices have also risen. Pricing can swing in either direction, which is exactly why continuous monitoring matters.

**GPU Price Trajectory (updated July 2026):**

| Year | H100 $/hr | B200 $/hr | Key Event |
|------|-----------|-----------|-----------|
| 2024 | ~$6.00 (mid) | N/A | H100 supply expansion |
| 2025 | ~$3.50 (mid) | Ships early 2025 | Blackwell launch; decentralized marketplace growth |
| 2026 (Jul, actual) | $2.29-3.12 median (range ~$1.40-8) | $3.20-18.53 on-demand (median ~$6.25, spot ~$2.70) | Deflation stalls; memory supercycle; Blackwell >70% of NVIDIA high-end shipments (GB300/B300-led) |
| Late 2026-2027 (est.) | Uncertain — memory price peak expected Q3-Q4 2026, no relief before mid-2027 | ~$2.50-3.00 possible at major clouds by Q4 2026 | Vera Rubin ramp slightly delayed (thermal heat-lid issues, HBM4 qualification); 2026 shipment share cut ~29% → ~22% (~1.7-1.8M units); Rubin Ultra reportedly cancelled/scaled back; standard Rubin mass shipments this summer to eight cloud partners |

*Earlier versions of this document projected H100 at $1.00-1.50/hr by 2027-2028 driven by a "mid-2026 B200 launch"; both the launch timing and the continuous-deflation assumption were wrong and those projections are withdrawn.*

**Recommended solution: Oracle-based USD pricing.** Instead of pricing inference in GNK tokens (which creates a dual volatility problem -- GPU prices declining while GNK price fluctuates), the network can use price oracles (Chainlink, Pyth) to set inference prices in USD terms while accepting GNK payment at the real-time exchange rate. This automatically keeps Gonka competitive regardless of GNK price movements or GPU market changes.

---

## 7. Economic Outlook

### 7.1 Network Growth Trajectory

Gonka's growth depends on expanding both the supply side (GPU hosts) and the demand side (developers using AI inference). The following projections are based on our macro-tokenomics research:

**Developer Growth Projections:**

| Scenario | Annual Growth | Year 1 | Year 3 | Year 5 | Year 10 |
|----------|-------------|--------|--------|--------|---------|
| Conservative | 10% | 2,420 | 2,900 | 3,500 | 5,700 |
| Moderate (Target) | 25% | 2,750 | 4,300 | 6,700 | 20,500 |
| Aggressive | 50% | 3,300 | 7,425 | 16,700 | 130,000+ |

The moderate scenario is the target trajectory, comparable to successful Web3 infrastructure platforms. For context, OpenAI's developer base has grown approximately 100% annually since 2022.

**Host Growth Expectations:**
- Current (July 2026, live counters): ~1,200 H100-equivalent GPUs actively mining — joingonka.ai shows 1,178 GPUs active, consistent with tracker.gonka.vip's ~1,214. Earlier, larger figures are historical: ~4,648 GPUs from ~113 independent participants running ~582 MLNodes (joingonka.ai, April 2026), the announced ~14,000 peak of Feb 2, 2026 (up from ~5,000 in Nov 2025 and ~12,000 by late Dec 2025), and CoinMarketCap's static "~5,000 H100 GPUs" project description (unchanged marketing text). A previously cited "448+ active hosts" figure does not match any current source and was likely a stale or differently-defined count. Nodes span ~20 countries with H100/H200/A100-class GPUs making up >80% of compute; the live model lineup (July 16, 2026) is MiniMax M2.7 (sole PoC/base model), GLM-5.2, and Kimi K2.6 (second re-bootstrap from epoch 331; also removed/restored June 25-27 via Proposals 78-79). Third-party explorers (gonka.gg with a free public API, gonkascan.com, gonkahub.com, tracker.gonka.vip) publish real-time participant/GPU/inference data and should be treated as the primary live sources
- As inference revenue grows and GNK price stabilizes, more hosts join
- Self-balancing: If too few hosts, per-host earnings rise, attracting new entrants
- If too many hosts, per-host earnings fall, causing marginal operators to exit

### 7.2 Revenue Model Evolution

The most important economic transition for Gonka is the shift from mining-dominated to fee-dominated revenue. Here is how this plays out under moderate growth assumptions:

**Revenue Composition Over Time:**

| Year | Mining Rewards (% of Host Income) | Inference Fees (% of Host Income) | Status |
|------|-----------------------------------|-----------------------------------|--------|
| Year 1 | ~60% | ~40% | Mining dominant |
| Year 3 | ~35% | ~65% | Fees growing rapidly |
| Year 5 | ~20% | ~80% | Fees dominant |
| Year 8 | ~10% | ~90% | Fees nearly fully replace mining |
| Year 12 | ~5% | ~95% | Mature fee-based economy |

**Annual Fee Revenue Projections (Moderate Growth):**

| Year | Est. Annual Fee Revenue | Host Share (70%) | AI Training Fund (20%) | Buyback + Yield (10%) |
|------|------------------------|------------------|----------------------|----------------------|
| Year 1 | $211M | $148M | $42M | $21M |
| Year 4 | $1.2B+ | $865M+ | $247M+ | $124M+ |
| Year 8 | $12B+ | $8.5B+ | $2.4B+ | $1.2B+ |

*Note: These are model projections under the moderate (target) scenario at $0.08 average fee per inference. Actual fee revenue to date (paid pricing only went live in November 2025 after the ~90-day grace period ended) is far below the Year-1 model figure; treat these as aspirational targets, not forecasts.*

### 7.3 Competitive Position in Decentralized AI Compute

The decentralized AI compute market is rapidly expanding, with Gonka positioned to capture a meaningful share:

**Competitive Landscape (July 2026):**

| Network | Revenue Model | Real Yield to Token Holders | Productive Compute | Key Advantage | Key Weakness |
|---------|--------------|---------------------------|-------------------|---------------|-------------|
| **Gonka** | Inference fees + mining | Proposed (5% + surplus) | 98% | Highest efficiency, OpenAI API | No major CEX listing, early stage, ~95% price drawdown |
| Akash | 4% take rate + BME burn (Mar 2026) | Indirect (burn from real usage) | Variable | General-purpose compute; ATH ~$5M Q1 2026 compute spend | Lower reliability |
| Render | Burn-Mint Equilibrium | Indirect (deflationary via burn) | ~90% | Creative industry focus | Niche market |
| Bittensor | Emissions + ~$43M Q1 2026 AI-customer revenue | No direct distribution | ~40% | Subnet ecosystem | Post-halving stress |
| io.net | GPU aggregation | No | High | Multi-source aggregation | Centralized elements |

**Gonka's competitive advantages:**
1. **Highest productive compute ratio** (98%) -- nearly all GPU work serves real AI tasks
2. **OpenAI-compatible API** -- near-zero migration effort for the largest developer ecosystem
3. **Real yield distribution** (proposed) -- would be the first decentralized AI network to distribute revenue directly to token holders, though Akash's usage-driven burn (live since March 2026) has narrowed this differentiation
4. **EIP-1559 dynamic pricing** -- automatic price adjustment that tracks market conditions

### 7.4 Key Milestones to Watch

These are the critical markers that indicate whether Gonka is on track:

| Milestone | Status / Target (Jul 2026) | Why It Matters |
|-----------|---------------------------|---------------|
| **B200 GPU integration** | **Done** — B200 supported and recommended for optimal mining rewards; capacity onboarding via GAIB partnership | Next-gen hardware, 2x performance |
| **Compute scale (10,000+ H100-eq)** | **Not met** — announced peak ~14,000 (Feb 2026); live counters show ~1,200 active (Jul 2026) | Supply-side critical mass |
| **Developer count reaches 6,000** | Target (unverified as of Jul 2026) | Validates demand-side growth strategy |
| **Major exchange listings** | Pending — earlier MEXC/Gate expectations did not materialize; OTC and SafeTrade only | Provides liquidity, price discovery |
| **veGNK launch** | Not yet launched; revised target H2 2026 | Governance strengthening, supply lock-up |
| **POL deployment** | Proposed | Permanent, sustainable trading liquidity |
| **First real yield distribution** | After veGNK launch | Key differentiator (window narrowing) |
| **Fee ratio exceeds 50%** | Year 3-4 | Proves sustainable economics |
| **Developer count reaches 15,000** | Month 18 | Growth trajectory confirmed |
| **Developer count reaches 25,000** | Month 36 | Scale achieved, organic growth |
| **Fee dominance (>80%)** | Year 5-8 | Network is self-sustaining |

---

## 8. Risk Factors & Considerations

### 8.1 Market Risks

- **Volatility:** GNK token price may fluctuate significantly, affecting Host profitability
- **Adoption:** Network value depends on achieving critical mass of Hosts and Developers
- **Competition:** Centralized providers or other decentralized networks may offer better value

### 8.2 Regulatory Risks

- **Securities Classification:** GNK may be classified as a security in some jurisdictions
- **Tax Treatment:** Mining rewards may have complex tax implications
- **Compliance:** AI regulations may impact network operations

### 8.3 Technical Risks

- **Scalability:** Network must handle growing demand without degradation
- **Security:** Smart contract bugs or protocol vulnerabilities could cause losses
- **Decentralization:** If few large Hosts dominate, censorship resistance weakens (this is no longer hypothetical — see Section 8.7)

### 8.4 Fee Transition Risk

**What it is:** The risk that inference fee revenue does not grow fast enough to replace declining mining rewards, causing hosts to become unprofitable and exit the network.

**Why it matters:** This is the single most critical economic risk for Gonka. By Year 8, mining rewards will be approximately 22% of their initial value. If fee revenue has not scaled to provide the majority of host income, the network could face a profitability crisis and lose compute capacity.

**Severity by scenario:**

| Scenario | Fee Growth | Year 8 Host Profitability | Risk Level |
|----------|-----------|--------------------------|-----------|
| Conservative (10% growth) | Slow but steady | Profitable if GNK > $3.30 | Medium-High |
| Moderate (25% growth) | Strong | Profitable at any reasonable GNK price | Low |
| Aggressive (50% growth) | Dominant | Fees fully replace mining by Year 2-3 | Very Low |

**Mitigation:** Aggressive developer onboarding, contingency tail emissions, and continuous monitoring of the fee ratio. The contingency plan recommends activating if Year 4 fee revenue falls below $50M (vs. the $96.9M conservative baseline).

### 8.5 GPU Price Deflation Risk

**What it is:** The risk that rapid GPU hardware price declines make competing centralized and decentralized providers significantly cheaper than Gonka, eroding the network's cost advantage.

**Why it matters:** H100 rental pricing fell 64-81% from Q4 2024 into early 2026, and as of July 2026 the deflation has stalled — rental rates are roughly flat year-over-year while hardware acquisition costs rise 30-50% on the memory supercycle (now expected to persist through mid-2027, with TrendForce raising Q3/Q4 DRAM forecasts in July 2026). This currently improves Gonka's relative cost position — but rental deflation could resume once memory supply normalizes and Vera Rubin-generation hardware scales. That scaling is itself slipping: the Rubin ramp is slightly delayed (thermal and HBM4-qualification issues; 2026 shipment share cut to ~22% of NVIDIA's GPU volume), which supports continued firmness in H100/H200/B200 rental prices near term. If Gonka's EIP-1559 pricing does not adjust quickly enough when deflation resumes, the network could temporarily become more expensive than alternatives.

**Mitigation:** The proposed oracle-based USD pricing eliminates this risk by automatically tracking competitive market rates. The current EIP-1559 mechanism also provides self-correction, though at a potentially slower pace. Additionally, Gonka's value proposition extends beyond price alone -- censorship resistance, privacy, and OpenAI compatibility provide non-price differentiation.

### 8.6 Governance Centralization Risk

**What it is:** The risk that the 200M GNK founder allocation (20% of total supply) could dominate governance decisions if the veGNK system is implemented without safeguards.

**Why it matters:** If founders lock their full allocation for the maximum duration while other holders lock for shorter periods, the founders could control up to 67% of effective voting power. This would undermine the decentralized governance that gives Gonka its credibility.

**Mitigation strategies:**
- Voluntary lock caps or monitoring to track concentration
- veGNK implementation keeps locked tokens separate from host collateral (preventing hosts from combining mining power with governance power)
- Transparent on-chain monitoring of voting power distribution
- Gradual governance decentralization as the community grows
- Delegation features (Phase 2-3) allow smaller holders to pool voting power

### 8.7 Delegation Concentration Risk (New — July 2026)

**What it is:** The risk that compute delegations concentrate on a few nodes (especially genesis guardian nodes), so that a localized failure cascades into a network-level outage.

**Why it matters:** This risk has materialized twice in three weeks. Proposal 78 (June 25, 2026) removed Kimi K2.6 (alongside the retired Qwen3-235B) after it lost validation majority; Proposal 79 (June 26) restored it at weight factor 0.9 and it re-bootstrapped at epoch 311. Then concentrated guardian delegations plus provider failures caused Kimi K2.6 to lose validation majority again in epochs 328-329, forcing a second removal via expedited Proposal 87 (July 15) and re-registration via Proposal 88 (July 16) for re-bootstrap at epoch 331. The July 15 network update issued explicit guidance — "Do not delegate to guardian nodes" — repositioning guardians as fallback-only, with the protocol team pushing delegation distribution across independent hosts as a systemic-risk mitigation. Guardian power is therefore not a resolved, parameterized issue (the v0.2.13 GenesisGuardianMultiplier reduction notwithstanding); it is an active operational concentration risk.

**Implications:** Model availability on Gonka can be interrupted by delegation topology, not just hardware supply — a reliability caveat that applies to any positioning built on a single "primary" model. Watch delegation distribution across independent hosts as a key decentralization metric alongside GPU count.

---

> **Important Disclaimer**
>
> This document is for educational purposes only and should not be construed as investment advice. All figures, projections, and scenarios are theoretical. Cryptocurrency investments carry high risk, including potential total loss of capital. Always conduct your own research and consult qualified financial advisors before making investment decisions.

---

## Key Takeaways

1. **Gonka creates value** by directing ~98% of compute to productive AI work
2. **Three stakeholders** (Developers, Hosts, Investors) have aligned incentives
3. **Gonka is cost-competitive** when GNK trades below ~$10 — at the July 2026 price of ~$0.13 it is among the cheapest inference options available
4. **Hosts beat traditional rental only above ~$0.18 GNK** at the live ~1,200-GPU network size; at ~$0.13, hosts earn ~25% below rental rates and are betting on appreciation and fee growth — and the favorable per-GPU math is itself a product of host exit
5. **Dynamic pricing** automatically balances supply and demand
6. **Ten proposed enhancements** strengthen long-term sustainability: from protocol-owned liquidity and real yield to governance improvements and floor price defense
7. **The fee transition is manageable** under moderate growth assumptions, with fees exceeding mining rewards by Year 3-4
8. **Developer growth is the critical success factor** -- the proposed onboarding strategy targets 25,000 active developers within 36 months
9. **Success depends** on achieving critical mass in a competitive market

---

*Document Version: 3.5 | Last Updated: July 18, 2026*

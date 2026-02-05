# GONKA NETWORK
## Tokenomics Explained
### A Comprehensive Guide to the Decentralized AI Economy

**February 2026** | Updated with latest macro-tokenomics research

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
- **Grace period:** First 90 epochs have zero inference pricing to encourage adoption

#### Market Context: AI Inference Pricing Comparison (February 2026)

##### LLM API Pricing

| Provider | Model | Input (per 1M tokens) | Output (per 1M tokens) | Notes |
|----------|-------|----------------------|------------------------|-------|
| OpenAI | GPT-4o | $3.00 | $10.00 | Premium, closed-source |
| OpenAI | GPT-4.5 | $75.00 | $150.00 | Largest model |
| Anthropic | Claude 3.5 | $3.00 | $15.00 | Premium tier |
| DeepSeek | V3 | $0.14 | $0.28 | Budget leader |
| DeepSeek | R1 (Reasoner) | $0.55 | $2.19 | Reasoning model |
| Google | Gemini 1.5 Flash | $0.037 | $0.15 | Lightweight |
| **Gonka (Est.)** | Open-source LLMs | $0.05-0.20* | $0.10-0.50* | Decentralized, subsidized |

*Gonka pricing is estimated based on network economics and will vary with GNK token price and network utilization.*

##### GPU Cloud Hourly Rates Comparison (February 2026)

| Provider | Type | H100 Price/Hour | H200 Price/Hour | B200 Price/Hour (Est.) | Best For |
|----------|------|-----------------|-----------------|------------------------|----------|
| AWS | Hyperscaler | $3.90-12.29 | $5.00-6.50 | $6.00-10.00 (Q3 2026) | Enterprise ecosystem |
| Azure | Hyperscaler | $4.00-11.20 | $5.50-7.00 | $6.00-10.00 (Q3 2026) | Microsoft integration |
| GCP | Hyperscaler | $3.69-12.29 | $5.00-6.50 | $6.00-10.00 (Q3 2026) | TensorFlow/GKE |
| CoreWeave | Specialized | $2.49-3.49 | $3.00-4.00 | Not yet available | AI/ML focused |
| Lambda Labs | Specialized | $2.49-2.99 | $2.99-3.99 | Not yet available | Developer-friendly |
| Vast.ai | Decentralized | $1.50-2.99 | $2.00-3.50 | Not yet available | Spot/budget |
| RunPod | Decentralized | $2.39-3.29 | $2.20-3.50 | Not yet available | Community cloud |
| Akash Network | Decentralized | $1.80-2.80 | N/A | N/A | Best-effort |
| **Gonka Network** | Decentralized | Variable* | Variable* | Variable* | Censorship-resistant |

*Gonka pricing varies based on GNK token value and network demand. During grace period (first 90 epochs), inference is free.*

**GPU Price Trend:** H100 pricing has declined 64-81% over the past 24 months, from $8-10/hr (Q4 2024) to $1.50-2.99/hr (Q1 2026). The upcoming NVIDIA B200 (Blackwell architecture, 2x inference performance) is expected to further compress H100 pricing toward $0.50-1.00/hr by 2028. Gonka's dynamic EIP-1559 pricing adjusts automatically to stay competitive as hardware costs decline.

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
| $0.50 | $0.10 | $0.25 | 97% cheaper | Very |
| $1.00 | $0.20 | $0.50 | 93% cheaper | Yes |
| $5.00 | $1.00 | $2.50 | 67% cheaper | Yes |
| $10.00 | $2.00 | $5.00 | 33% cheaper | Marginal |
| $20.00 | $4.00 | $10.00 | Same price | No advantage |
| $50.00 | $10.00 | $25.00 | More expensive | No |

**Key Insight:** Gonka remains cost-competitive with centralized providers when GNK trades below ~$10. Above this level, the decentralization and censorship-resistance benefits must justify the premium. A proposed oracle-based pricing enhancement (see Section 6) would eliminate this price sensitivity entirely.

#### Cost Prediction by Model Size

*At GNK = $1.00 (moderate scenario), 50% utilization:*

| Model Type | Parameters | Est. Input Cost/1M | Est. Output Cost/1M | Comparable To |
|------------|------------|-------------------|--------------------|--------------|
| Small (Qwen 7B) | 7B | $0.15 | $0.35 | GPT-3.5 Turbo |
| Medium (Qwen 32B) | 32B | $0.40 | $0.90 | Claude Haiku |
| Large (Llama 70B) | 70B | $0.80 | $1.80 | GPT-4o mini |
| XL (Llama 405B) | 405B | $2.50 | $5.50 | GPT-4o |

#### Monthly Cost Projections for Typical Use Cases

*At GNK = $1.00, using a 7B model:*

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
| DeepSeek V2 | $0.28 | $0.56 | GNK < $0.56 |
| Self-hosted H100 | $1.50 equiv. | $3.00 | GNK < $3 |
| Anthropic Claude | $15.00 | $30.00 | GNK < $30 |

**Conclusion:** Gonka's cost advantage is strongest when GNK trades in the $0.50-$5.00 range. Above $10, only censorship-resistance and privacy justify the premium. Below $0.50, Gonka undercuts even the cheapest alternatives.

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
| Base hourly rate | $1.50-2.99/hr | Variable (mining rewards) | Potential upside |
| Customer acquisition | Required (marketing) | Automatic (protocol) | No overhead |
| Utilization risk | You bear 100% | Shared across network | Lower risk |
| Price appreciation | None (fixed USD) | GNK may appreciate | Potential 10x+ |
| Dual income | No | Mining + Work fees | 2 revenue streams |
| Downtime penalty | Lost revenue | Minimal (vesting) | Protection |

##### Host Earnings Calculator (Per H100 GPU)

*Assumptions: 90% uptime, network has 500 H100-equivalent GPUs, GNK emissions = 323,000/epoch*

| GNK Price | Daily Mining Reward | Daily Work Fees* | Daily Total | Monthly Total | vs Traditional Rental |
|-----------|--------------------|-----------------| -----------|---------------|----------------------|
| $0.50 | $29 | $5 | $34 | $1,020 | -42% (worse) |
| $1.00 | $58 | $10 | $68 | $2,040 | +16% (better) |
| $2.00 | $116 | $20 | $136 | $4,080 | +132% (better) |
| $5.00 | $290 | $50 | $340 | $10,200 | +480% (better) |
| $10.00 | $580 | $100 | $680 | $20,400 | +1060% (better) |

*Work fees assume 30% network utilization with inference demand. Traditional rental benchmark: $1,760/month ($2.44/hr avg, 90% uptime)*

**Key Insight:** Hosts become profitable vs traditional rental when GNK exceeds ~$0.85. Early miners with lower competition earn proportionally more.

#### Incentive #2: Bitcoin-Style Scarcity Economics

**WHY IT WORKS:** Gonka uses a deflationary emission model similar to Bitcoin:
- Initial reward: 323,000 GNK per epoch distributed to all Hosts
- Halving every ~4 years (1,460 epochs), reducing new supply over time
- Fixed 1 billion total supply creates scarcity
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
- Gonka's 'Sprint' (Proof of Compute) uses only brief periods for consensus
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
- Hosts can exchange mined GNK for USDT/ETH/BTC before exchange listings
- Reduces the 'can't sell until listed' risk of early mining
- Governed by Hosts themselves (decentralized decision-making)

---

### 2.4 Incentives for Token Investors

#### Incentive #1: Exposure to AI Infrastructure Growth

**WHY IT WORKS:** The AI compute market is projected to grow from $9B (2024) to $100B+ (2032). GNK token value is tied to:
- Inference demand growth (more developers using the network)
- Network effect (more Hosts = better service = more developers)
- Scarcity mechanics (fixed supply with growing utility)

##### AI Crypto Market Comparison (February 2026)

| Project | Focus | Market Cap | Token Price | Productive Compute |
|---------|-------|------------|-------------|-------------------|
| Bittensor (TAO) | AI Model Marketplace | $5-7B est. | $250-400 | ~40% |
| Render (RNDR) | GPU Rendering | $3-5B est. | $5-8 | ~90% |
| Akash (AKT) | General Cloud | $500M-1B | $2-5 | Variable |
| Fetch.ai (FET) | AI Agents | $1-2B | $1-2 | N/A |
| **Gonka (GNK)** | AI Inference | Pre-listing | ~$1 mining cost | **~98%** |

*Note: Current mining cost of GNK is approximately $1, suggesting potential upside if network achieves adoption comparable to competitors.*

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
> - Distribution is proportional to each Host's Proof of Compute (PoC) weight
> - PoC weight is earned during 'Sprint' - a 10-minute competitive computation period
> - Only Hosts with GPU hardware actively running can earn rewards

> **STEP 2: Token Entry into Circulation**
> - Newly minted GNK goes to Hosts who earned it
> - Rewards are subject to vesting (gradual daily release)
> - Hosts can convert GNK to USDT/ETH/BTC via Community Pool
> - Or Hosts can sell on exchanges once listed

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

### 3.3 The Sprint Mechanism (Proof of Compute)

Sprint is Gonka's consensus mechanism that determines voting weight and reward distribution:

1. All Hosts start simultaneously (random seed prevents pre-computation)
2. Each Host runs transformer-based computations for ~10 minutes
3. The number of valid 'nonces' found determines PoC weight
4. Weight determines: (a) share of mining rewards, (b) voting power, (c) task allocation
5. Between Sprints, GPUs perform real AI inference work

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
| Host earnings (USD) | $68/day | $680/day | +900% earnings |
| New Host incentive | Low | Very High | Supply increases |

### 4.2 Scenario: GNK Token Price Crashes

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
| vs DeepSeek ($0.28) | Comparable | 64% cheaper | Major advantage |
| Host earnings (USD) | $68/day | $13.60/day | -80% earnings |
| Host profitability | Profitable | Marginal/Loss | Some exit |
| Remaining host share | 1/500th | 1/200th (if 60% leave) | +150% per host |

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
- Community Pool provides liquidity even without exchange trading

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
| **Gonka (GNK)** | AI Inference | ~98% | Pre-listing | Highest efficiency |
| Bittensor (TAO) | AI Marketplace | ~40% | $5-7B | Subnet ecosystem |
| Render (RNDR) | GPU Rendering | ~90% | $3-5B | Creative industry |
| Akash (AKT) | General Cloud | Variable | $500M-1B | Broad compute |
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

**Why this is significant:** Among decentralized AI compute networks -- including Akash, Render, and Bittensor -- none have implemented genuine real yield distribution. Gonka would be the first, creating a significant competitive advantage in attracting long-term capital.

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
| Foundation | Months 1-6 | 6,000 (from 2,200) | Free compute credits, migration guides |
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

**Rollout plan:**
- Phase 1 (Q2 2026): Basic lock + voting power
- Phase 2 (Q4 2026): Boost mechanics + delegation
- Phase 3 (2027): Advanced features based on community feedback

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

**Important caveat:** Floor defense is a speed bump, not an impenetrable wall. In a prolonged severe bear market (6+ months of -60% decline), treasury resources could be depleted. The mechanism buys time for fundamentals to reassert, not guarantee a permanent price floor.

---

### LOW Priority

#### 6.8 EIP-1559 Fee Parameter Optimization

**What it is:** A fine-tuning of Gonka's dynamic pricing mechanism. The current system adjusts prices by up to 2% per block. Research suggests that increasing this to 4% would allow prices to respond faster to changing market conditions while maintaining stability.

**Why it matters:** When GPU market prices drop suddenly (as they have done, falling 64-81% over the past 24 months) or when GNK's price changes significantly, the current 2% adjustment rate may take too long to bring Gonka's prices back to competitive levels. A 4% rate would converge roughly twice as fast.

**Risk assessment:** Academic research on Ethereum's EIP-1559 shows that adjustment rates up to 6-11% remain stable, so a move from 2% to 4% is well within the safe range.

---

#### 6.9 Quadratic Voting for Community Decisions

**What it is:** An alternative voting system where the cost of additional votes increases exponentially. One vote costs 1 token, but two votes cost 4 tokens, and three votes cost 9 tokens. This prevents wealthy participants from dominating governance decisions.

**Limited application:** Quadratic voting is vulnerable to "Sybil attacks" (one person creating many wallets to get cheaper votes). However, Gonka has a natural defense: GPU-based identity verification. Hosts who operate physical hardware have verifiable on-chain identities. Therefore, quadratic voting is recommended only for host-gated Community Pool decisions, where participants are verified GPU operators.

---

### ONGOING

#### 6.10 GPU Price Monitoring and Competitive Positioning

**What it is:** A continuous program to track GPU cloud market pricing and ensure Gonka remains competitively positioned as hardware costs decline.

**Why this is ongoing:** GPU pricing deflates 30-50% annually. The H100, which cost $8-10/hr in Q4 2024, now costs $1.50-2.99/hr. By 2028, it may cost $0.50-1.00/hr. Gonka's pricing must track these changes or risk becoming uncompetitive.

**GPU Price Deflation Trajectory:**

| Year | H100 $/hr (Mid) | H200 $/hr (Mid) | B200 $/hr (Mid) | Key Event |
|------|-----------------|-----------------|-----------------|-----------|
| 2024 | $6.00 | N/A | N/A | H100 supply expansion |
| 2025 | $3.50 | $4.50 | N/A | Decentralized marketplace growth |
| 2026 (current) | $2.50 | $3.50 | $6.00-10.00 (launch) | B200 arrives |
| 2027 | $1.50 | $2.50 | $3.00-5.00 | Blackwell matures |
| 2028 | $1.00 | $1.50 | $2.00-4.00 | Blackwell Ultra / Rubin announced |

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
- Current: 448 hosts with ~6,000 H100-equivalent GPUs
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

*Note: These are model projections under the moderate (target) scenario at $0.08 average fee per inference. Actual outcomes will depend on real-world adoption.*

### 7.3 Competitive Position in Decentralized AI Compute

The decentralized AI compute market is rapidly expanding, with Gonka positioned to capture a meaningful share:

**Competitive Landscape (February 2026):**

| Network | Revenue Model | Real Yield to Token Holders | Productive Compute | Key Advantage | Key Weakness |
|---------|--------------|---------------------------|-------------------|---------------|-------------|
| **Gonka** | Inference fees + mining | Yes (proposed 5% + surplus) | 98% | Highest efficiency, OpenAI API | Pre-listing, early stage |
| Akash | 4% take rate | No (inflationary only) | Variable | General-purpose compute | Lower reliability |
| Render | Burn-Mint Equilibrium | No (deflationary via burn) | ~90% | Creative industry focus | Niche market |
| Bittensor | Pure emissions | No (purely inflationary) | ~40% | Subnet ecosystem | Post-halving stress |
| io.net | GPU aggregation | No | High | Multi-source aggregation | Centralized elements |

**Gonka's competitive advantages:**
1. **Highest productive compute ratio** (98%) -- nearly all GPU work serves real AI tasks
2. **OpenAI-compatible API** -- near-zero migration effort for the largest developer ecosystem
3. **Real yield distribution** (proposed) -- first decentralized AI network to share actual revenue with token holders
4. **EIP-1559 dynamic pricing** -- automatic price adjustment that tracks market conditions

### 7.4 Key Milestones to Watch

These are the critical markers that indicate whether Gonka is on track:

| Milestone | Target Timeline | Why It Matters |
|-----------|----------------|---------------|
| **Developer count reaches 6,000** | Month 6 | Validates demand-side growth strategy |
| **Fee ratio exceeds 50%** | Year 3-4 | Proves sustainable economics |
| **Exchange listings** | Year 1-2 | Provides liquidity, price discovery |
| **veGNK launch** | Q2 2026 | Governance strengthening, supply lock-up |
| **POL deployment** | Year 1 | Permanent, sustainable trading liquidity |
| **First real yield distribution** | After veGNK launch | Differentiator vs all competitors |
| **Developer count reaches 15,000** | Month 18 | Growth trajectory confirmed |
| **Fee dominance (>80%)** | Year 5-8 | Network is self-sustaining |
| **Developer count reaches 25,000** | Month 36 | Scale achieved, organic growth |
| **B200 GPU integration** | Q3-Q4 2026 | Next-gen hardware, 2x performance |

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
- **Decentralization:** If few large Hosts dominate, censorship resistance weakens

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

**Why it matters:** H100 pricing has already fallen 64-81% in 24 months, and the B200 launch in 2026 will trigger another wave of depreciation. If Gonka's EIP-1559 pricing does not adjust quickly enough, the network could temporarily become more expensive than alternatives.

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

---

> **Important Disclaimer**
>
> This document is for educational purposes only and should not be construed as investment advice. All figures, projections, and scenarios are theoretical. Cryptocurrency investments carry high risk, including potential total loss of capital. Always conduct your own research and consult qualified financial advisors before making investment decisions.

---

## Key Takeaways

1. **Gonka creates value** by directing ~98% of compute to productive AI work
2. **Three stakeholders** (Developers, Hosts, Investors) have aligned incentives
3. **Gonka is cost-competitive** when GNK trades below ~$10 (vs major providers)
4. **Hosts can earn more** than traditional rental when GNK exceeds ~$0.85
5. **Dynamic pricing** automatically balances supply and demand
6. **Ten proposed enhancements** strengthen long-term sustainability: from protocol-owned liquidity and real yield to governance improvements and floor price defense
7. **The fee transition is manageable** under moderate growth assumptions, with fees exceeding mining rewards by Year 3-4
8. **Developer growth is the critical success factor** -- the proposed onboarding strategy targets 25,000 active developers within 36 months
9. **Success depends** on achieving critical mass in a competitive market

---

*Document Version: 3.0 | Last Updated: February 2026*

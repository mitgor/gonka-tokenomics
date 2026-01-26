# Architecture

**Analysis Date:** 2026-01-26

## Pattern Overview

**Overall:** Three-stakeholder economic system with decentralized token incentives and dynamic market equilibrium

**Key Characteristics:**
- Three distinct participant roles with aligned incentives: Developers (demand), Hosts/Miners (supply), Investors (capital)
- Token-based reward distribution proportional to computational contribution (Proof of Compute)
- Dynamic pricing mechanism (EIP-1559 inspired) that adjusts AI inference costs based on network utilization
- Deflationary emission schedule with ~4-year halving cycles creating scarcity mechanics
- Circular economic flow where developer demand funds host rewards through inference fees and mining emissions

## Layers

**Compute Layer (Supply):**
- Purpose: Provides computational resources for AI inference tasks
- Participants: GPU Hosts/Miners running Proof of Compute (PoC)
- Contribution mechanism: Sprint consensus (10-minute competitive computation period)
- Reward structure: Mining rewards (epoch-based emissions) + work fees (from developer inference payments)
- Dependency: Driven by developer demand; sustainable when GNK price supports profitability

**Demand Layer (Consumer):**
- Purpose: Consumes AI inference services using open-source LLM models
- Participants: Developers building/deploying AI applications
- Payment mechanism: GNK token payments at dynamic per-model rates
- Pricing: EIP-1559 inspired with 40-60% optimal utilization zone
- Access method: OpenAI-compatible API for easy developer adoption
- Value proposition: Cost advantage when GNK < $10, censorship-resistance, privacy, transparent pricing

**Token/Capital Layer (Incentive):**
- Purpose: Creates supply-demand balance through token economics and investor participation
- Allocation: 1 billion total GNK supply distributed across mining rewards, community pool, and founders
- Distribution mechanism: 323,000 GNK per epoch (initially) to hosts proportional to PoC weight
- Community Pool: 120 million GNK for early-stage host liquidity (USDT/ETH/BTC conversion)
- Founders: 200 million GNK for team compensation and protocol development
- Scarcity: Fixed supply with halving events driving long-term value appreciation

**Governance & Validation Layer:**
- Purpose: Ensures network integrity and system stability
- Validation mechanism: Randomized task verification catching cheating hosts probabilistically
- Consensus: Proof of Compute (PoC) weight determines voting power and reward distribution
- Penalties: Slashing rules (20% for cheating, 10% for poor performance)
- Training fund: 20% of inference revenue directed to Decentralized AI Training Fund

## Data Flow

**Inference Request Flow:**

1. Developer submits inference request through OpenAI-compatible API with GNK tokens
2. Request router allocates task to available Host based on model demand and PoC weight
3. Host executes AI inference on GPU, returning result to developer
4. Task verification occurs (randomized subset re-verification)
5. Payment flows to Host (Work Fee) + Training Fund (20% of revenue)
6. Developer receives inference result

**Token Distribution Flow:**

1. Each epoch (regular interval), 323,000 GNK is newly minted
2. Distribution allocated proportionally to Hosts based on Sprint PoC weight
3. Rewards subject to vesting schedule (gradual daily release)
4. Hosts can: sell on exchanges (once listed), convert via Community Pool (USDT/ETH/BTC), or hold for appreciation
5. Hosts receive additional GNK from inference work fees (portion of developer payments)

**Economic Equilibrium Flow:**

1. Developer demand increases → Network utilization rises above 60%
2. Dynamic pricing increases per-token cost (max 2% per block)
3. Higher prices attract new Hosts to join network
4. Increased GPU supply reduces per-token prices back toward 40-60% optimal zone
5. If supply exceeds demand → prices fall toward floor (1 nicoin per AI token)
6. Lower prices attract developers → demand increases → equilibrium restored

**State Management:**
- Host reputation scores (track verification rate and uptime) determine task allocation priority
- Host collateral/slashing state (tracks penalty accumulation)
- Per-model dynamic pricing state (maintains utilization-based price curves)
- Network utilization tracking (determines when to trigger price adjustments)
- Emission schedule state (tracks halving progress)

## Key Abstractions

**Proof of Compute (PoC/Sprint):**
- Purpose: Consensus mechanism determining host voting weight and reward distribution
- Mechanics: 10-minute transformer-based computation period where hosts compete to find valid nonces
- Weight calculation: Number of valid nonces found = PoC weight for that epoch
- Application: Higher weight = larger share of mining rewards + task allocation priority
- Example files: (Not yet implemented - in design phase)
- Pattern: Consensus-weighted reward distribution

**Dynamic Pricing Engine:**
- Purpose: Automatic supply-demand balancing without manual intervention
- Parameters: Network utilization rate (target 40-60%), per-model base rates, GNK token price
- Logic: Below 40% utilization → decrease prices; above 60% → increase prices (max 2%/block)
- Price floor: 1 nicoin per AI token prevents zero-cost scenarios
- Adjustment mechanism: Gradual price changes prevent sudden developer shocks
- Example files: (Not yet implemented)
- Pattern: Feedback control system with rate limits

**Vesting Schedule:**
- Purpose: Smooth host token availability and reduce sell pressure
- Mechanics: Mining rewards released gradually over time after earning
- Benefit: Encourages long-term host participation; reduces pump-and-dump volatility
- Example files: (Not yet implemented)
- Pattern: Time-locked incentive

**Community Pool:**
- Purpose: Early liquidity provision for hosts before exchange listings
- Governance: Decentralized voting by hosts on conversions and pool rules
- Mechanism: 120 million GNK converted to USDT/ETH/BTC at community-determined rates
- Benefit: Reduces host risk during early network phase; maintains decentralized control
- Example files: (Not yet implemented)
- Pattern: Community-governed treasury

## Entry Points

**For Developers:**
- Location: OpenAI-compatible API endpoint
- Triggers: Submit inference request with GNK token payment
- Responsibilities: Route requests to hosts, execute inference, collect payments, distribute to training fund

**For Hosts:**
- Location: Host software running Sprint consensus mechanism
- Triggers: Join network by running GPU node; participate in each epoch's PoC competition
- Responsibilities: Execute Sprint (10-min PoC), perform inference work, validate peer results, maintain uptime

**For Investors:**
- Location: Community Pool interface + future exchange listings
- Triggers: Purchase GNK tokens for speculation/investment
- Responsibilities: Participate in governance voting once listed; hold/trade for price appreciation

## Error Handling

**Strategy:** Probabilistic verification with deterministic penalties

**Patterns:**
- Cheating detection: Randomized subset verification catches dishonest results
- Response: Caught hosts lose ALL accumulated rewards for cycle + 20% collateral slash
- Poor performance: 10% collateral slash; reputation score reset
- Network resilience: Majority verification ensures trustworthiness; no single host can corrupt results
- Developer protection: Max price limits prevent overpayment; tasks fail rather than exceed cost ceiling

## Cross-Cutting Concerns

**Pricing:** Dynamic EIP-1559 inspired model based on utilization; transparent per-model costs; price floors and ceilings prevent extreme volatility

**Incentive Alignment:** Mining rewards + work fees create dual income streams for hosts; cost advantages create developer incentives; token scarcity creates investor incentives

**Decentralization:** No single authority controls pricing, task allocation, or token distribution; hosts vote via PoC weight; community governs early liquidity pool

**Environmental Impact:** 98% productive compute vs 0% Bitcoin/Ethereum waste; minimal consensus overhead; appeal vs regulatory pressure on proof-of-work mining

---

*Architecture analysis: 2026-01-26*

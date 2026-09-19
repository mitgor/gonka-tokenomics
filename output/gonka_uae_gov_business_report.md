# Gonka for the UAE: Government-Grade AI Inference and the Business Around It

**Report for the ADI Foundation / Sirius International Holding discussion** · September 19, 2026 · Draft

*Companion to the Gonka × ADI one-pager and the two fleet blurbs. All network figures are from a chain snapshot at epoch 397 (September 18, 2026) and public explorers; market rates are September 2026. The estimate model is `uae_fleet_model.py`; every assumption in it is editable.*

---

## 1. Executive summary

- **What Gonka is today.** A live Cosmos-based proof-of-compute network where ~98% of GPU time does real AI inference. It is small: 494 physical GPUs across 21 hosts, ~22B tokens served per day on three open models (MiniMax M2.7, DeepSeek V4 Flash, GLM-5.3-Flash), GNK at $0.15 with $16M market cap and ~$65K of daily trading. Fee revenue is effectively zero because on-chain pricing is 0.001 GNK per million tokens with dynamic pricing switched off. Backers: Coatue, Bitfury ($12M at $0.60 plus a $50M commitment), Gcore, Hyperfusion, 6Block. NVIDIA-only today.
- **What the UAE fleet does to it.** 20,000 H200 would carry 99% of network weight. Emission is fixed (~273K GNK/day), so the fleet's GNK income is ~80–90M GNK/yr whether it deploys 2,000 or 20,000 GPUs. At spot that is $12–13M/yr; at $1.50 it is $133M; rental parity for the full H200 tranche needs GNK at ~$3.70. The protocol also forces the fleet to buy ~3,260 GNK per H200 as collateral, which for 20,000 GPUs exceeds the entire unlocked float. While income is mining only, the rational structure is a **2,000–3,000 H200 Gonka tranche** (captures ~90% of emission, parity at ~$0.45) with the remaining capacity run as sovereign inference behind Gonka's API and ADI's settlement rail. Once inference demand fills the fleet, the whole fleet should sell tokens through Gonka, and the picture changes as the scenarios below show.
- **The numbers at a glance (demand-filled scenarios).** Assuming demand matches the capacity on offer and Gonka's on-chain pricing is switched to market rates, the fleet's gross revenue is:

| Fleet | Medium: rented at market | Medium: via Gonka | Optimistic: rented at market | Optimistic: via Gonka |
|---|---|---|---|---|
| 20,000 H200 | $45/GPU/day · **$326M/yr** | $80/GPU/day · **$585M/yr** | $67/GPU/day · **$491M/yr** | $232/GPU/day · **$1,694M/yr** |
| 10,000 MI300X | $31/GPU/day · **$111M/yr** | $62/GPU/day · **$228M/yr** | $46/GPU/day · **$168M/yr** | $181/GPU/day · **$659M/yr** |
| **GPU fleet (30,000)** | **$437M/yr** | **$813M/yr (1.9x)** | **$659M/yr** | **$2,353M/yr (3.6x)** |
| 1,000 Cerebras CS-3 (softest estimate; "market" = direct inference sales) | $2,050/unit/day · $749M/yr | $2,110/unit/day · $770M/yr | $5,970/unit/day · $2,180M/yr | $6,110/unit/day · $2,231M/yr |
| Total incl. CS-3 | $1,187M/yr | $1,583M/yr (1.3x) | $2,839M/yr | $4,584M/yr (1.6x) |

  Medium: GNK $0.60, 55% of capacity sold at $1.00 per million output tokens (input billed on a 3:1 mix folded in; the GonkaBroker/DeepInfra price level), rental at the $3.10/hr H200 index and 60% utilisation. Optimistic: GNK $1.50, 80% sold at $2.00/M (MiniMax M2.7, GLM-5.x, DeepSeek V4 Pro list level), rental 13% above index at 80% utilisation. Gross before power (~$31M/yr fleet-wide on either path). The Gonka uplift is a token-resale effect: fees are 93–95% of Gonka-path revenue, and GNK mining adds $53M/yr (medium) to $134M/yr (optimistic) fleet-wide. Without demand, the mining-only case in section 3 applies: ~$12–13M/yr at spot, ~$133M/yr at $1.50, rental parity for the full H200 tranche only at GNK ~$3.70. Full assumptions in section 3.3; model in `uae_fleet_model.py`.
- **Why it fits government.** The UAE has set the most aggressive public-sector AI targets anywhere: 50% of federal services on agentic AI within two years, Abu Dhabi "AI-native government" by 2027 with 100% sovereign cloud, a new Federal Authority for AI and Data. Every one of those programs is an inference bill. Gonka gives the government three things a hyperscaler contract does not: verifiable compute (every inference is proof-checked by other hosts), a permissioned in-country zone with data residency, and a settlement path in a central-bank-approved dirham stablecoin instead of a foreign cloud invoice.
- **The business.** Three revenue lines: (1) mining income on the Gonka tranche, (2) token-resale margin on inference, which is 3–15x per GPU-hour over raw rental when demand is filled, (3) the token position itself. Around them sit the ADI-native opportunities: DDSC-settled AI billing, "AI on ADI" for developers worldwide, Arabic-model hosting via governance, verifiable-inference records for regulated workflows, and export to Africa and Asia along corridors ADI is already building.
- **Preconditions.** Governance changes on Gonka (USD-oracle or re-enabled dynamic pricing, AMD and Cerebras support, a fee-capture mechanism), a hold-and-collateralise policy for rewards, a CEX listing, and a four-operator structure to respect the 30% per-participant cap.

## 2. Gonka as it actually is (September 2026)

| Item | Value | Note |
|---|---|---|
| Hosts / GPUs | 21 participants, 84 ML nodes, 494 GPUs | H100 SXM 268, H200 128, A100 32, B300 10, B200 4, others |
| Consensus weight | 282,125 units | H100 SXM ≈ 427, H200 ≈ 970, B200 ≈ 1,600 per GPU |
| Emission | 323,000 × e^(−0.000475 × epoch) GNK per ~23.5h epoch → ~267K at epoch 397 | 100% to hosts by weight; halves every ~1,460 epochs; 180-epoch linear vesting |
| Collateral | 20% of weight free; 4.2 GNK per weight unit for the rest; 30% cap per participant | Slashing: 20% invalid work, 10% downtime |
| Demand | ~22B tokens/day, ~2.1M requests, ~5% output tokens | Fees since genesis: 495 GNK. On-chain price 0.001 GNK/M; dynamic pricing disabled |
| Token | $0.15; 105.9M self-reported circulating (83.9M on-chain, 57.8M unlocked); max 1B | Uniswap V3 liquidity $0.7M; SafeTrade only CEX; Tangem live, Ledger in progress |
| Hardware | B300, B200, RTX PRO 6000, H200, H100, A100 80GB; ≥320 GB VRAM per node | No AMD or Cerebras support anywhere in docs, code or proposals |
| Trajectory | 439 hosts at epoch 100 (Nov 2025) → 21 at epoch 397 | Hosts left as GNK fell 94% from its January high; per-GPU rewards for survivors rose ~5x |

Two implications. First, the network is a working protocol with a tokenomics problem, not a technology problem: rewards are real, fees are not, and liquidity is thin. Second, any fleet the UAE brings is not "joining" the network in a meaningful sense; it becomes the network. That is why this report treats the deal as a design problem rather than a hosting decision.

## 3. Fleet economics

### 3.1 Mechanics that drive the numbers

- **Weight, not GPU count, sets income.** An H200 carries ~2.3x an H100's weight on the live network. For MI300X and CS-3 there is no weight until Gonka supports them; the model uses forward estimates of 1.8x and 40x H100 (ranges 1.2–2.4x and 25–60x). MI300X has more memory and bandwidth than H200 but a 10–30% ROCm kernel gap; a CS-3 draws 23 kW and Cerebras claims ~1.5x tokens per watt versus Blackwell, but has never published aggregate throughput per system.
- **Emission is fixed.** The fleet's share of emission is its weight over total weight. At 2,000 H200 the share is 87%; at 20,000 it is 99%. Everything beyond ~3,000 H200 adds dilution, not income.
- **Collateral is mandatory.** 4.2 GNK per weight unit for 80% of the weight, i.e. ~3,260 GNK per H200, ~2,580 per MI300X, ~57,000 per CS-3 at the estimated weights.
- **Fees require a pricing fix.** With the on-chain price at 0.001 GNK per million tokens, a fully loaded fleet would give away ~$1B/yr of inference. Enabling dynamic pricing (parameters exist: 40–60% utilisation band, elasticity 0.05) or the USD-oracle pricing proposed in Gonka's own tokenomics research is a governance vote the fleet would control.

### 3.2 Per-unit and fleet estimates

| Tranche on Gonka | GNK/unit/day | $/unit/day at $0.15 | at $0.60 | at $1.50 | Parity GNK price | Collateral (GNK) |
|---|---|---|---|---|---|---|
| H200, 500 pilot | 311 | $47 | $187 | $467 | $0.14 | 1.6M |
| H200, 2,000 | 107 | $16 | $64 | $161 | $0.42 | 6.5M |
| H200, 5,000 | 46 | $7 | $28 | $69 | $0.96 | 16.3M |
| H200, 20,000 | 12 | $1.80 | $7 | $18 | $3.68 | 65.2M |
| MI300X (full fleet) | 4.3 | $0.64 | $2.55 | $6.40 | ~$8 | 25.8M |
| CS-3 (full fleet) | 95 | $14 | $57 | $142 | ~$8 | 57.4M |

Rental benchmarks: H200 $44.64/day ($3.10/hr, 60% billed), MI300X $30.53/day ($2.12/hr). Fleet rental value ~$440M/yr if fully sold; realised GAIB Gonka income ~$17 per H200 per day.

**Fleet income by scenario (any tranche ≥2,000 H200):** ~$12–13M/yr at spot, ~$53M at $0.60, ~$133M at $1.50, ~$326M at $3.68. Inference fees on top, at $0.40/M blended: ~$3M/yr on Gonka's current demand, ~$22M on an estimated 150B tokens/day of UAE government and enterprise demand, ~$146M on a 25% share of global open-model traffic. Full-fleet power: 54 MW IT, ~$31M/yr at $0.05/kWh.

### 3.3 Demand-filled scenarios: market rental versus Gonka

The mining-only figures above assume today's demand. If inference demand matches the capacity on offer, the fleet earns from tokens, not from emission, and the comparison that matters is GPU-hours sold at market versus tokens sold through Gonka. The executive-summary table uses these assumptions:

| Assumption | Medium | Optimistic | Basis |
|---|---|---|---|
| GNK price | $0.60 | $1.50 | Bitfury entry (Nov 2025); DePIN-peer re-rating |
| Share of capacity sold | 55% | 80% | Neocloud breakeven 56–70%; CoreWeave contracted fleets run higher |
| Price per 1M output tokens (input billed, 3:1 mix folded in) | $1.00 | $2.00 | GonkaBroker/DeepInfra level (~$0.25 per total token); MiniMax M2.7, GLM-5.x, DeepSeek V4 Pro list level |
| Output throughput per unit | H200 1,800 tok/s; MI300X 1,400; CS-3 48,000 | same | InferenceX single-node H200 on 1T-class MoE 990–1,580 tok/s; lighter MoEs higher; CS-3 unverified |
| Market rental | $3.10/hr H200, $2.12/hr MI300X at 60% | +13% at 80% | Silicon Data neocloud index, Sept 2026 |
| Cerebras "market" | direct inference sales at scenario price | same | No CS-3 rental market exists |
| Uptime | 90% | 90% | Professional operator |

Results: the 30,000-GPU fleet grosses $437M/yr at market versus $813M/yr via Gonka in the medium case (1.9x) and $659M/yr versus $2,353M/yr in the optimistic case (3.6x). Per unit, H200 moves from $45 to $80/day (medium) and $67 to $232/day (optimistic); MI300X from $31 to $62 and $46 to $181. Cerebras adds $749M–2,180M/yr on either path and is the softest line because Cerebras has never published aggregate throughput per system. Two conditions make these numbers real: a governance vote that replaces the 0.001 GNK/M on-chain price with dynamic or USD-oracle pricing, and demand routed to the fleet (section 4 and 5). Fees and rental scale linearly with tranche size; only the mining pool is fixed.

### 3.4 Price impact of the influx

The fleet moves the price it is paid in, so the estimate has to be reflexive. Four channels, largest first.

1. **Collateral buying (upward, one-off, deal-driven).** 20,000 H200 need 65M GNK, more than the 57.8M unlocked float and 78% of all on-chain supply. Even 5,000 H200 need 28% of the float. None of this is executable on a $0.7M DEX pool; it must come from the Community Pool (120M GNK, host-governed) or originator supply at a negotiated price. That transaction, like Bitfury's $0.60 purchase, becomes the market's reference price. In practice the collateral purchase *is* the strategic investment.
2. **Emission dilution (neutral for the fleet, terminal for incumbents).** Survivors' per-GPU rewards fall 87–99%; the remaining 21 hosts mostly leave. Decentralisation optics are managed through the 30% per-participant cap (four independent operators, e.g. Khazna, Core42, EHC and a Sirius entity) and by inviting existing hosts (GAIB, Gcore, Hyperfusion, 6Block) to co-locate in the UAE zone.
3. **Reward sell pressure (downward, continuous, policy-controlled).** ~245K GNK/day to the fleet, vesting over 180 epochs. Sold, that is ~$37K/day into ~$65K/day of volume and the price goes to zero. Held and recycled as collateral, it is zero sell pressure and makes the fleet the majority holder within a year. A written hold policy and a CEX listing are preconditions.
4. **Re-rating (upward, uncertain).** GNK's FDV is $150M against ~$3B of committed hardware. DePIN peers price at $0.8–3B; Render alone was ~$784M in July. A re-rating to $0.60–1.50 is consistent with peers and makes a 2,000–5,000 H200 tranche pay at or above rental parity. Parity for all 20,000 needs $3.70 (FDV $3.7B), which is not a base case and should not be pitched as one.

### 3.5 Sizing rule

While income is mining only, deploy the smallest tranche that captures ~90% of emission (2,000–3,000 H200), fund its ~8M GNK collateral through a negotiated purchase, hold rewards, and add tranches only when price and liquidity milestones are met: 5,000 H200 at GNK ≥$1 with a CEX listing, 10,000 at ≥$2, the remainder as soon as sold inference, not emission, is the main income line (the demand-filled case in 3.3, where the whole fleet belongs on Gonka). AMD follows a ROCm port (3–6 months of engineering, fundable from the Community Pool as a bounty like Devshard v5's $91K); Cerebras follows a proof-of-compute port (9–18 months, needs Cerebras engineering because PoC assumes CUDA and a GPU memory model) and is better used for sovereign low-latency inference in the meantime.

## 4. Why Gonka does best at UAE government level

### 4.1 The demand is mandated, not hypothetical

- **Federal:** 50% of federal government services and operations on agentic AI within two years (May 2026 directive, overseen by Sheikh Mansour); four federal AI agents already live (procurement, tax audit, customer happiness, technical support); a Federal Authority for AI and Data created June 2026 under Omar Al Olama; every ministry has a Chief AI Officer.
- **Abu Dhabi:** AED 13B Digital Strategy 2025–27, "world's first fully AI-native government by 2027", 100% sovereign cloud adoption, 200+ AI solutions, 100+ use cases across 40+ entities already. The DGE sovereign environment is sized for 11M+ daily digital interactions. TAMM handled 55.5M transactions in H1 2026, 98% digital, with an AI assistant resolving 97% of queries without a human and AED 723M of annual savings attributed.
- **Dubai:** two-year private-sector shift to agentic AI, 295,000 companies, 100 AI assistants, 27 government entities on an AI infrastructure platform.
- **Sector agencies:** ADNOC with 115+ AI agents and 3,000 models in daily use; AD Ports' "intelligence headquarters" with thousands of digital workers; the Abu Dhabi Judicial Department's AI judicial platform; M42's Med42 clinical model on Malaffi.

At a few thousand tokens per agentic interaction, government demand alone plausibly reaches 50–200B tokens/day by 2027. That is small next to a 20,000-H200 fleet (2.8T tokens/day of capacity) but large next to Gonka's current 22B, and it is the demand that matters politically.

### 4.2 What Gonka offers that a hyperscaler contract does not

| Government requirement | Hyperscaler / sovereign-cloud answer | Gonka + ADI answer |
|---|---|---|
| Data residency (PDPL full compliance Jan 2027; health and CBUAE-regulated data must stay in-country) | Core42/Azure or OCI dedicated region; contractual | Permissioned host zone in UAE datacentres; requests routed only to whitelisted UAE nodes; enforced by protocol, auditable on ADI Chain |
| Auditability of AI outputs | Vendor logs | Every inference is proof-of-compute verified by other hosts; the model, input hash, host and verifier can be anchored as an ADI "trusted record" without publishing the prompt |
| Vendor independence | Single US vendor stack | Open-weight models (DeepSeek, GLM, MiniMax; Falcon/Jais/K2 addable by vote), open protocol, multiple operators |
| Payment rail | Foreign-currency cloud invoices | DDSC on ADI Chain; CBUAE rules prohibit utility tokens as mainland payment, so GNK stays the settlement asset between hosts and DDSC the customer-facing one |
| Cost | $3–13/H200-hr at hyperscaler list | Marginal cost of owned GPUs; open-model token prices 10–100x below closed frontier APIs |
| Sovereign control of the stack | Sovereign-cloud "controls layer" on a foreign platform | Government-affiliated operators hold the weight, vote the parameters, and run the sequencer (ADI Chain supports on-premise sequencers) |

### 4.3 Regulatory path

- **GNK on ADI Chain.** ADI Chain is an EVM-compatible Ethereum L2 (ZKsync stack). Gonka already runs an Ethereum bridge with WGNK as an ERC-20, so a bridged GNK on ADI is a contract deployment plus Chainlink CCIP (ADI's partner since March 2026), not new protocol work. Under ADGM's 2025 rules a firm can add an "Accepted Virtual Asset" by notification and self-assessment against FSRA criteria (liquidity on regulated venues, transparency, governance, custody compatibility). GNK fails the liquidity criterion today; a CEX listing and the ADI-side liquidity pool are what make it pass.
- **Payments.** CBUAE's Payment Token Services Regulation bars non-payment tokens as a means of payment on the mainland. That is why the design bills customers in DDSC and settles hosts in GNK behind the scenes. Nothing in the design asks a ministry to hold crypto.
- **Mining and hosting.** Legal under commercial and datacentre licences (precedents: MARA–Zero Two 250 MW in Masdar City, Phoenix Group's 550 MW pivoting to AI/HPC).
- **Chips.** Since July 10, 2026 the UAE is in BIS Country Group A:5 with licence-free NVIDIA and AMD sales to G42, Core42, MGX and hyperscalers. The undeployed H200s are not export-constrained; the constraint everyone reports is grid power and transformers, which favours a fleet owner that already has energised capacity.

### 4.4 Arabic and sovereign models

Gonka adds models by governance proposal with a per-model weight factor. The UAE operators, holding the weight, can put Falcon-H1 Arabic (TII), Jais 2 (Inception/MBZUAI/Cerebras) and K2 Think or K2 Horizon (MBZUAI) on the network and make them proof-of-compute models. That turns Gonka into the distribution layer for UAE-built models to developers worldwide, which none of the sovereign-cloud arrangements does.

## 5. Business opportunities

| Opportunity | Buyer | Mechanism | Indicative size |
|---|---|---|---|
| **Sovereign inference-as-a-service** | Federal entities, DGE, Dubai Digital, ADNOC, AD Ports, DoH/M42, ADJD | Permissioned UAE zone; DDSC billing; verified records | 50–200B tokens/day by 2027 → $7–30M/yr at open-model rates, $50–190M/yr if frontier-priced |
| **IHC portfolio demand** | 1,400+ IHC subsidiaries (FAB, Alpha Dhabi, EHC, Esyasoft, Emirates Driving, ADREC) | Group-wide AI credit line settled in DDSC | IHC deploys ~$2B/month with an "if there's no AI, there's no investment" mandate; capturing 1% of group AI spend is a nine-figure line |
| **Telco and enterprise resale** | e& (already selling "Sovereign AI Compute" with Core42), du, banks (FAB, ENBD, ADCB) | White-label Gonka endpoint under the telco's sovereign-AI brand | e& and du are both building sovereign AI offers; a partner with owned H200 capacity undercuts Core42 |
| **"AI on ADI" for developers worldwide** | OpenClaw, MCP-native agent builders, x402 payers | Gonka's OpenAI-compatible API, MCP server, DDSC/x402 settlement on ADI | Global open-model traffic ~4T tokens/day; each 1% share ≈ $6M/yr at $0.40/M, 10x that at frontier pricing |
| **Token resale margin** | All of the above | Sell tokens, not GPU-hours: $10–48 gross per H200-hour vs $3.10 rental | 3–15x per-hour uplift when demand is filled; the fleet's real P&L lever |
| **Export corridors** | AfCFTA JV, Ghana $1B AI hub, Condor Galaxy India (G42), M-Pesa markets (ADI) | Gonka nodes in partner countries settle in DDSC/GNK; UAE zone as the hub | UAE has pledged $1B for African AI infrastructure; Gonka is a ready-made multi-country compute fabric |
| **Cerebras sovereign tier** | Government and financial real-time agents | 1,000 CS-3 serving Arabic and frontier open models at 1,000–3,000 tok/s per user | Cerebras' own inference prices ($0.35–0.75/M gpt-oss, $6/$12 405B); at 35% fill a CS-3 grosses ~$650/day → ~$240M/yr across 1,000 units |
| **Verifiable-AI records** | Energy provenance (Good Energy pattern), trade documents, claims, registries | Inference proofs anchored on ADI Chain | Extends ADI's existing 113M-record use case to AI decisions; pricing per record |
| **Tokenisation adjacency** | ADGM funds (Mubadala Capital precedent), BNY/Finstreet custody | GNK as an ADGM-accepted asset; tokenised GPU revenue (GAIB pattern) | Kearney: ~$500B of GCC assets on-chain by 2030 |

## 6. Deal structure

1. **Operators.** Four independent Gonka participants, each under the 30% cap, e.g. Khazna, Core42, EHC (IHC's modular-datacentre JV with Supermicro) and a Sirius vehicle. Existing hosts invited to co-locate.
2. **Tranche 1.** 2,000–3,000 H200 in energised Abu Dhabi capacity (3–4 MW). Collateral ~8M GNK acquired by negotiated purchase from the Community Pool or originator supply; the purchase sets the reference price and is the investment leg. Rewards held and recycled into collateral; no market sales.
3. **Pricing and fees.** Governance proposals, voted with the fleet's weight: enable dynamic pricing or USD-oracle pricing; direct a share of fees to a buyback or to a UAE-zone treasury; add Falcon/Jais/K2 as PoC models.
4. **Rails.** Bridged GNK on ADI Chain via Chainlink CCIP; DDSC↔GNK pool with a licensed ADGM market maker (Finstreet); ADGM Accepted-Virtual-Asset notification once liquidity criteria are met; Ledger and Tangem already cover custody.
5. **Sovereign inference layer.** The remaining ~17,000 H200 and the AMD/Cerebras fleets serve UAE demand through the same API and settlement, off-protocol until supported, so revenue starts before the ports land.
6. **Engineering.** ROCm port bounty (MI300X), Cerebras PoC design study with Cerebras (a G42/MBZUAI relationship already exists), permissioned-routing feature for the UAE zone, x402/DDSC payment adapter.
7. **Milestone ladder.** 5,000 H200 at GNK ≥$1 with CEX listing; 10,000 at ≥$2; further only when fees exceed emission for the tranche.

## 7. Risks and mitigations

| Risk | Why it matters | Mitigation |
|---|---|---|
| Takeover optics | The fleet would hold 87–99% of weight | Four-operator cap structure; publish a maximum-share policy; keep incumbents |
| Token liquidity | $65K/day volume cannot absorb any selling | Hold policy; CEX listing as a milestone; OTC collateral purchase |
| Pricing switched off | Fees are nil today; a big fleet gives away inference | Governance vote on pricing before tranche 1 goes live |
| Network stability | Model churn (Kimi removed twice), 46% weight drop over seven epochs, host count 21 | Professional operators; bounties for Devshard and chain upgrades; SLA with Hyperfusion/6Block |
| AMD and Cerebras estimates | Weights are our forward estimates, not measured | Benchmark in a 64-GPU / 4-CS-3 lab before committing weight assumptions |
| Cerebras fit | 44 GB on-chip SRAM; large models span multiple systems; PoC assumes GPU memory model | Treat CS-3 as inference tier first; PoC port only with Cerebras engineering |
| Regulatory | PTSR bars utility tokens as payment; CMA replaced SCA in January 2026; G42's chip authorisation reportedly runs on a nine-month clock | DDSC-only customer billing; ADGM entity; keep the fleet under UAE-government-affiliated operators |
| Demand shortfall | Fleet capacity is 100x today's Gonka demand | Size the Gonka tranche to emission, not capacity; sovereign layer carries the rest |
| GNK price does not re-rate | Tranche pays 0.4x rental at spot | Tranche 1 is sized to break even at $0.42; collateral bought below that |

## 8. Twelve-month plan

| Quarter | Milestones |
|---|---|
| Q4 2026 | Term sheet; 64-GPU benchmark node in Abu Dhabi; collateral purchase agreed; pricing and model proposals drafted; ADI-Chain GNK contract and DDSC pool designed |
| Q1 2027 | Tranche 1 (2,000 H200) live under four operators; dynamic/oracle pricing enabled; first DDSC-billed government workload (TAMM or a federal agent); Falcon-H1 Arabic proposal |
| Q2 2027 | Sovereign layer serving ≥50B tokens/day; MI300X ROCm port complete and benchmarked; CEX listing; ADGM AVA notification; "AI on ADI" developer endpoint public |
| Q3 2027 | Tranche 2 decision against the milestone ladder; Cerebras PoC design study; first export-corridor node (AfCFTA pilot) |

## 9. Assumptions and sources

- Protocol parameters, weights, emission, demand and fees: `node2.gonka.ai` chain API (epoch 397), tracker.gonka.vip, gonka.gg, gonkahub.com, gonkadocs.com proposals #78–#105, gonka.ai docs and tokenomics paper.
- Prices: CoinMarketCap, CoinGecko, Uniswap V3 (September 19, 2026).
- Rental and hardware: Silicon Data indices, getdeploying.com, provider pricing pages, InferenceX (SemiAnalysis) throughput runs, Cerebras filings and pricing, September 2026.
- UAE programs and regulation: The National, Khaleej Times, Gulf News, DGE, Microsoft, ADGM, CBUAE, Bloomberg, DCD, May–September 2026.
- Demand-filled scenarios (section 3.3): medium GNK $0.60 / 55% sold / $1.00 per 1M output tokens / rental at index and 60%; optimistic GNK $1.50 / 80% / $2.00 / rental +13% at 80%.
- Model assumptions (editable in `uae_fleet_model.py`): H200 weight 970; MI300X 1.8x H100; CS-3 40x H100; H200 realised rent $3.10/hr at 60% utilisation; blended token price $0.40/M; 90% uptime; PUE 1.3; $0.05/kWh; four operators.
- Known conflicts: GNK all-time high ($2.61 on CoinMarketCap vs $0.32 on CryptoRank); circulating supply (105.9M self-reported vs 83.9M on-chain); Cerebras unit cost ($1.5–3M, no list price).

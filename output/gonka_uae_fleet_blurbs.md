# Gonka × UAE fleet: two blurbs

*September 19, 2026 · Estimates from `uae_fleet_model.py` on live chain data (epoch 397) and September 2026 market rates. Numbers are estimates, not commitments.*

---

## Blurb 1 — What 20,000 H200 + 10,000 MI300X + 1,000 Cerebras CS-3 are worth on Gonka

**The short version.** Gonka pays hosts a fixed ~273,000 GNK per day, split by proof-of-compute weight. Today that pool is shared by 494 GPUs, so one H200 earns ~800–900 GNK (~$120–140) a day, about 3x what it rents for. A UAE fleet changes the denominator: 20,000 H200 would hold 99% of network weight, and each GPU's share drops to ~12 GNK ($1.80) a day. The fleet's total GNK income is nearly fixed at ~80–90M GNK a year regardless of how many GPUs it deploys, so the only variables that matter are **how many GPUs you put on-protocol** and **what GNK is worth**. Adding the AMD and Cerebras tranches (once Gonka supports them) raises capacity but not income, and cuts the per-unit share further.

**Estimate per accelerator per day (mining share only, 90% uptime).**

| Tranche on Gonka | GNK/unit/day | At $0.15 (spot) | At $0.60 | At $1.50 | Parity GNK price | vs rental at spot |
|---|---|---|---|---|---|---|
| **H200**, 500 pilot | 311 | $47 | $187 | $467 | $0.14 | ~1.0x |
| **H200**, 2,000 | 107 | $16 | $64 | $161 | $0.42 | 0.36x |
| **H200**, 5,000 | 46 | $7 | $28 | $69 | $0.96 | 0.16x |
| **H200**, all 20,000 | 12 | $1.80 | $7 | $18 | $3.68 | 0.04x |
| **MI300X**, 10,000 in full fleet* | 4.3 | $0.64 | $2.55 | $6.40 | ~$8 | 0.02x |
| **Cerebras CS-3**, 1,000 in full fleet* | 95 | $14 | $57 | $142 | ~$8 | no rental market |

\*Forward estimates, not yet supported on Gonka: MI300X at 1.8x H100 weight after a ROCm port (range 1.2–2.4x); CS-3 at 40x H100 weight after a proof-of-compute port (range 25–60x). Traditional rental benchmark: H200 $44.64/day ($3.10/hr at 60% billed utilisation), MI300X $30.53/day ($2.12/hr). GAIB's private Gonka phase realised ~$17 per H200 per day.

**Fleet-level annual picture.** Rental value of the GPU tranches is ~$440M/yr (H200 $326M, MI300X $111M) *if* a buyer exists; the fleet is currently undeployed and earning zero. On Gonka the fleet's mining income is ~$12–13M/yr at spot, ~$53M at $0.60, ~$133M at $1.50, ~$326M at parity ($3.68), for **any tranche of 2,000 H200 or more**. Inference fees add little today: Gonka bills 0.001 GNK per million tokens and has collected 495 GNK in fees since genesis, and current demand (22B tokens/day) would fill 0.8% of the H200 tranche. If UAE government and enterprise demand of ~150B tokens/day were routed through the fleet at market rates ($0.40/M blended) that is ~$22M/yr; a 25% share of global open-model traffic (~1T tokens/day) would be ~$146M/yr. Power for the full fleet is ~54 MW IT (70 MW at PUE 1.3), ~$31M/yr at Abu Dhabi tariffs.

**Medium and optimistic scenarios (demand fills the fleet).** Assumes inference demand matches the capacity on offer, the full fleet is on Gonka with on-chain pricing switched from 0.001 GNK/M to dynamic or USD-oracle pricing, and tokens are sold at market rates through Gonka's API. Medium: GNK $0.60, 55% of capacity sold at $1.00 per million output tokens (input billed on a 3:1 mix folded in; roughly the GonkaBroker/DeepInfra price level), rental at the $3.10/hr H200 index and 60% utilisation. Optimistic: GNK $1.50, 80% sold at $2.00/M (MiniMax M2.7, GLM-5.x, DeepSeek V4 Pro list level), rental 13% above index at 80% utilisation. Gross revenue before power (~$31M/yr fleet-wide on either path).

| Fleet | Medium: rented at market | Medium: via Gonka | Optimistic: rented at market | Optimistic: via Gonka |
|---|---|---|---|---|
| 20,000 H200 | $45/GPU/day · **$326M/yr** | $80/GPU/day · **$585M/yr** | $67/GPU/day · **$491M/yr** | $232/GPU/day · **$1,694M/yr** |
| 10,000 MI300X | $31/GPU/day · **$111M/yr** | $62/GPU/day · **$228M/yr** | $46/GPU/day · **$168M/yr** | $181/GPU/day · **$659M/yr** |
| **GPU fleet (30,000)** | **$437M/yr** | **$813M/yr (1.9x)** | **$659M/yr** | **$2,353M/yr (3.6x)** |
| 1,000 Cerebras CS-3 (softest estimate; no rental market, "market" = direct inference sales) | $2,050/unit/day · $749M/yr | $2,110/unit/day · $770M/yr | $5,970/unit/day · $2,180M/yr | $6,110/unit/day · $2,231M/yr |
| Total incl. CS-3 | $1,187M/yr | $1,583M/yr (1.3x) | $2,839M/yr | $4,584M/yr (1.6x) |

Two things the table shows. Once demand exists, the Gonka path is a token-resale business: fees are 93–95% of Gonka-path revenue and GNK mining is $53M/yr (medium) to $134M/yr (optimistic) fleet-wide, so the token is the settlement asset and upside kicker, not the income. And the multiple over rental comes from selling tokens instead of GPU-hours (1.8–3.5x for H200, 2.0–3.9x for MI300X); Cerebras earns about the same either way because its "market" is already token sales. Per-unit figures scale linearly with tranche size for fees and rental; only the mining pool is fixed.

**Price impact of the influx (this is the crux).** Four forces, in order of size:

1. **Collateral demand.** Unlocking full weight requires 4.2 GNK per weight unit, i.e. ~3,260 GNK per H200. A 5,000-GPU tranche needs 16M GNK (28% of the unlocked float); 20,000 needs 65M GNK, more than the entire unlocked float (57.8M) and 78% of everything on-chain. This cannot be bought on a market with $0.7M of DEX liquidity; it has to be a negotiated purchase from the Community Pool or originator supply, which is the strategic-investment leg and re-anchors the reference price the way Bitfury's $0.60 print did.
2. **Dilution.** Incumbent hosts' per-GPU rewards fall 87–99% and most of the 21 remaining hosts exit; the network becomes the fleet. The 30% per-participant cap means the fleet must run as at least four operators to collect more than 30% of emission.
3. **Sell pressure.** The fleet would receive ~245,000 GNK/day, vesting over 180 epochs. Sold at spot that is ~$37K/day into ~$65K/day of total volume: the price collapses. Held, it makes the fleet the majority holder within ~12 months. A hold-and-collateralise policy plus a CEX listing is a precondition, not an option.
4. **Re-rating.** GNK's fully diluted value is $150M; the fleet's replacement value is ~$3B. A sovereign 31,000-accelerator commitment is the largest single DePIN compute deployment on record and would re-rate the token, but rental parity for the full 20,000 H200 needs GNK at ~$3.70 (FDV $3.7B, above every DePIN peer). Parity for a 2,000–5,000 tranche needs $0.42–0.96, inside the range of comparable networks.

**Recommendation embedded in the numbers.** The 2,000–3,000 H200 limit applies while income is mining only: that tranche captures ~90% of emission (collateral ~8M GNK, parity at ~$0.45). Once demand materialises as in the medium and optimistic scenarios, route the whole fleet's inference through Gonka's API, settle in DDSC, and add mining tranches against GNK price and liquidity milestones. Bring MI300X on after a ROCm port (est. 3–6 months) and Cerebras after a proof-of-compute port (est. 9–18 months); the Cerebras tranche is worth more serving sovereign low-latency inference at Cerebras-class prices ($0.35–0.75/M) than mining.

---

## Blurb 2 — Why doing it with Gonka beats plain GPU hosting (the multiples)

The fleet is undeployed, so the honest baseline is zero. Against traditional hosting, Gonka adds three multipliers that renting cannot:

- **Guaranteed base income, no customer needed.** A 500-H200 pilot earns ~$47/GPU/day at today's price, on par with the best neocloud rental rate and ~2.8x what GAIB realised, with no sales cycle, no utilisation risk, and no H200 rental market in the UAE yet (hyperscalers there do not even list H200).
- **Token optionality on ~90M GNK a year.** Any tranche of 2,000+ H200 collects ~9% of GNK's max supply per year. Relative to the tranche's rental value that is 0.4x at spot, **1.6x at $0.60, 4x at $1.50, 10x at $3.70**. The collateral the protocol forces you to buy (~3,260 GNK per H200) is the same asset, bought before the re-rating your own deployment triggers.
- **Resale margin on inference.** Selling tokens instead of GPU-hours yields $10–48 gross per H200-hour on current open-model prices versus $3.10 rental, a 3–15x per-hour uplift when demand is filled. Gonka supplies the OpenAI-compatible API, verification and settlement rails; the UAE supplies the demand (federal target of 50% of government services on agentic AI within two years, TAMM's 55M transactions per half-year, ADNOC's 115 agents) and the export corridors to Africa and Asia.

- **With demand, the multiple is 2–4x on the GPU fleet.** If inference demand fills the capacity, the 30,000-GPU fleet grosses ~$437M/yr rented at market versus ~$813M/yr via Gonka in the medium case (GNK $0.60, 55% sold at $1.00/M output), and ~$659M/yr versus ~$2.35B/yr in the optimistic case (GNK $1.50, 80% sold at $2.00/M): 1.9x and 3.6x. Cerebras adds ~$0.75–2.2B/yr on either path, with Gonka contributing mining and distribution on top. Power is ~$31M/yr either way.

Adjacent opportunities: DDSC-settled AI billing on ADI Chain, hosting Falcon/Jais/K2 Arabic models via Gonka governance, verifiable inference records for regulated workflows, and a Cerebras-class sovereign low-latency tier no other decentralized network offers.

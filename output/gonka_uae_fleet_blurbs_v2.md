# Gonka × UAE fleet: two blurbs (v2, founder-calibrated)

*September 19, 2026 · v2 recalibrated to Gonka founder feedback (David Liberman, Sept 19); v1 retained as `gonka_uae_fleet_blurbs.md`. Estimates from `uae_fleet_model_v2.py` on live chain data (epoch 397) and September 2026 market rates. Numbers are estimates, not commitments.*

---

## Blurb 1 — What 10,000 MI300X, 1,000 Cerebras CS-3 and 20,000 H200 are worth on Gonka

**The short version.** Gonka pays hosts a fixed ~273,000 GNK a day, split by proof-of-compute weight. On today's network of 494 GPUs that pool pays an MI300X ~$69 a day (1.6x its $1.80/hr on-demand rate; it has dipped to 0.9x), an H200 ~$140 a day (1.3x its $4.50/hr on-demand rate; dipped to 0.7x) and a B300 ~$396 a day (2.1x of $7.85/hr; never below 1.2x). Long-term GPU contracts, the only way a 30,000-unit fleet is actually rented, pay 0.4–0.5x on-demand, so **Gonka today pays 2.6–5x what a contract pays**. A UAE fleet changes the denominator: its GNK income is nearly fixed at ~80–90M GNK a year whatever it deploys, so the deployment itself must move the GNK price to the level where per-GPU yield settles back near market. The founders' own estimate is that 10,000 MI300X alone take GNK to ~$2, with the same per-GPU earnings at larger scale; the model reproduces that ($2.01 at 1.2x on-demand). Doing the same with 20,000 H200 would need GNK near $8–10, which is why the pitch leads with MI300X and B300, treats Cerebras as a sovereign tier, and uses the H200s to sell inference rather than to mine.

**Mining share per accelerator per day (90% uptime).** "Equilibrium GNK" is the price at which the tranche's mining yield settles at 1.2x on-demand.

| Tranche on Gonka | GNK/unit/day | At $0.15 (spot) | At $2.00 (post-ramp) | At $4.50 (20% MoM growth) | Equilibrium GNK | Collateral (GNK) |
|---|---|---|---|---|---|---|
| **MI300X**, 1,000 | 154 | $23 | $308 | $693 | $0.30 | 1.6M |
| **MI300X**, 5,000 | 44 | $6.60 | $88 | $198 | $1.06 | 8.0M |
| **MI300X**, all 10,000 | 23 | $3.50 | $46 | $104 | $2.01 (founder: ~$2) | 16.0M |
| **H200**, 2,000 | 107 | $16 | $214 | $482 | $1.09 | 6.5M |
| **H200**, all 20,000 | 12 | $1.80 | $24 | $54 | $9.63 | 65.2M |
| Full fleet, per H200 / MI300X / CS-3 | 5.7 / 2.8 / 101 | $0.86 / $0.42 / $15 | $11 / $5.60 / $202 | $26 / $13 / $455 | ~$10 | 145M |
| **B300** (reference, not in fleet) | 2,638 today | $396 today (2.1x on-demand) | | | | 9,150 per unit |

Forward estimates, not yet supported on Gonka: MI300X at the founder-implied weight of 476 (1.1x H100, 0.49x H200; the founders quote a yield, so an internal benchmark likely exists); CS-3 at 40x H100 (range 25–60x, Cerebras publishes no aggregate throughput). Market baselines: on-demand H200 $4.50/hr, MI300X $1.80/hr, B300 $7.85/hr; contracts 0.4–0.5x of that. GAIB's private Gonka phase realised ~$17 per H200 per day.

**Medium and optimistic scenarios (demand fills the fleet).** Assumes inference demand matches the capacity on offer, the full fleet is on Gonka with on-chain pricing switched from 0.001 GNK/M to dynamic or USD-oracle pricing, and tokens are sold at market rates through Gonka's API. Medium: GNK $2.00 (the founders' post-ramp equilibrium), 55% of capacity sold at $1.00 per million output tokens (input billed on a 3:1 mix folded in; the GonkaBroker/DeepInfra price level), rental at the $3.10/hr H200 and $1.80/hr MI300X index at 60% utilisation (the contract-rate level). Optimistic: GNK $4.50 (20% month-on-month organic growth for six months after the ramp), 80% sold at $2.00/M (MiniMax M2.7, GLM-5.x, DeepSeek V4 Pro list level), rental 13% above index at 80% utilisation. Gross before power (~$31M/yr fleet-wide on either path).

| Fleet | Medium: rented at market | Medium: via Gonka | Optimistic: rented at market | Optimistic: via Gonka |
|---|---|---|---|---|
| 10,000 MI300X | $26/GPU/day · **$95M/yr** | $53/GPU/day · **$192M/yr** | $39/GPU/day · **$143M/yr** | $150/GPU/day · **$546M/yr** |
| 20,000 H200 | $45/GPU/day · **$326M/yr** | $88/GPU/day · **$646M/yr** | $67/GPU/day · **$491M/yr** | $250/GPU/day · **$1,824M/yr** |
| **GPU fleet (30,000)** | **$421M/yr** | **$838M/yr (2.0x)** | **$634M/yr** | **$2,370M/yr (3.7x)** |
| 1,000 Cerebras CS-3 (softest estimate; "market" = direct inference sales) | $2,050/unit/day · $749M/yr | $2,260/unit/day · $823M/yr | $5,970/unit/day · $2,180M/yr | $6,430/unit/day · $2,346M/yr |
| Total incl. CS-3 | $1,170M/yr | $1,661M/yr (1.4x) | $2,813M/yr | $4,715M/yr (1.7x) |

Once demand exists, the Gonka path is a token-resale business: fees are ~88–90% of Gonka-path revenue and GNK mining is $178M/yr (medium) to $401M/yr (optimistic) fleet-wide. The multiple over rental comes from selling tokens instead of GPU-hours (2.0x for H200 and MI300X in the medium case, 3.7–3.8x in the optimistic case); Cerebras earns about the same either way because its market is already token sales. Fees and rental scale linearly with tranche size; only the mining pool is fixed.

**Price impact of the influx.** Three cases, in the order the founders and the model agree on:

1. **Downside: spot, no re-rating ($0.15).** A 10,000-MI300X tranche earns $3.50 per GPU per day, 0.16x a contract rate; 20,000 H200 earn $1.80. This is the state if the collateral is bought without moving the market and rewards are sold into ~$65K/day of volume. It is a transient the deal structure must avoid, not a base case.
2. **Base: the deployment re-prices GNK to equilibrium (~$2 for 10,000 MI300X).** Unlocking full weight requires 4.2 GNK per weight unit: 16M GNK for 10,000 MI300X (28% of the unlocked float), 65M for 20,000 H200 (more than the float). None of it is executable on a $0.7M DEX pool, so it is a negotiated purchase from the Community Pool or originator supply that sets the reference price the way Bitfury's $0.60 print did. At ~$2, per-GPU earnings are the same yield as today on a larger base: 10,000 MI300X × ~$46/day ≈ $170M/yr of mining income, plus whatever inference the fleet sells. Rewards (~245K GNK/day, vesting over 180 epochs) must be held and recycled as collateral; the 30% per-participant cap means at least four operators; incumbent hosts' per-GPU rewards fall 87–99%, so keep them by co-locating.
3. **Upside: organic growth after the ramp.** The founders' scenario is six months of fleet-driven ramp, then six months of organic growth: 10% month-on-month adds 1.5x (GNK ~$3), 20% adds 2.3x (~$4.50), 50% adds 7x (~$14). These are their haircut figures (straight compounding would give 1.8x, 3.0x and 11x). The fleet's collateral and held rewards ride that path; that, not the mining yield, is the investment case.

**Recommendation embedded in the numbers.** Lead with MI300X: it has no rental market to speak of (no listings on Akash, io.net or Vast; contracts at $0.72–0.90/hr), earns 1.6x on-demand on Gonka today, and a 10,000-unit ramp lands GNK at a credible ~$2. Add B300 for any new capacity (2.1x on-demand, never below 1.2x, the highest weight per GPU on the network). Bring the H200s in as inference capacity sold through Gonka's API and settled in DDSC, adding H200 mining tranches only as the network grows past them (2,000 H200 reach equilibrium at ~$1.09; 20,000 need ~$9.60). Cerebras follows a proof-of-compute port (9–18 months) and serves the sovereign low-latency tier in the meantime.

---

## Blurb 2 — Why doing it with Gonka beats plain GPU hosting (the multiples)

The fleet is undeployed, so the honest baseline is zero, and the realistic alternative for 30,000 units is a long-term contract at 0.4–0.5x on-demand. Against that, Gonka adds four multipliers:

- **Base income above contract rates, no customer needed.** On today's network Gonka pays an MI300X 1.6x on-demand (3–4x a contract), an H200 1.3x (2.6–3.2x a contract) and a B300 2.1x (4–5x a contract), with dips to 0.9x, 0.7x and 1.2x respectively. A 1,000-MI300X pilot earns ~$23/GPU/day at spot, above a contract rate, with no sales cycle and no utilisation risk.
- **A price path the deployment itself creates.** 10,000 MI300X take GNK to ~$2 (same per-GPU yield on a bigger base, ~$170M/yr of mining); organic growth after the ramp adds 1.5x at 10% month-on-month (~$3), 2.3x at 20% (~$4.50), 7x at 50% (~$14), per the founders' haircut figures. The 16M GNK of collateral the protocol forces you to buy, plus ~90M GNK a year of held rewards, are the same asset bought before that path.
- **With demand, 2–4x on the GPU fleet.** If inference demand fills the capacity, the 30,000-GPU fleet grosses ~$421M/yr rented at market versus ~$838M/yr via Gonka in the medium case (GNK $2, 55% sold at $1.00/M output), and ~$634M/yr versus ~$2.37B/yr in the optimistic case (GNK $4.50, 80% sold at $2.00/M): 2.0x and 3.7x. Cerebras adds ~$0.75–2.2B/yr on either path. Power is ~$31M/yr either way.
- **Resale margin on inference.** Selling tokens instead of GPU-hours yields $10–48 gross per H200-hour on current open-model prices versus $3–4.50 rental. Gonka supplies the OpenAI-compatible API, verification and settlement rails; the UAE supplies the demand (federal target of 50% of government services on agentic AI within two years, TAMM's 55M transactions per half-year, ADNOC's 115 agents) and the export corridors to Africa and Asia.

Adjacent opportunities: DDSC-settled AI billing on ADI Chain, hosting Falcon/Jais/K2 Arabic models via Gonka governance, verifiable inference records for regulated workflows, and a Cerebras-class sovereign low-latency tier no other decentralized network offers.

"""UAE fleet on Gonka: opportunity estimate with reflexive GNK price.

Fleet: 20,000 H200 (Gonka-supported today), 10,000 AMD MI300X and 1,000 Cerebras CS-3
(not yet supported; modelled as forward H100-equivalent PoC weight + throughput).

Per accelerator: (1) share of the fixed daily GNK emission, (2) inference fees.
Emission share is diluted by the fleet itself, so GNK price is a scenario input, not spot.
Sources: chain snapshot epoch 397 (2026-09-18), tracker.gonka.vip, gonka.gg, Silicon Data,
InferenceX, getdeploying (all 2026-09). Run: python3 uae_fleet_model.py
"""
import math

# ---- protocol (live params, epoch 397) ----
E0, DECAY, EPOCH = 323_000, 0.000475, 397     # GNK/epoch at genesis, decay per epoch, current epoch
EPOCHS_PER_DAY = 24 / 23.5
EXISTING_WEIGHT = 282_125                      # total consensus weight before the fleet joins
W_H100 = 427                                   # live median weight of one H100 SXM
COLLATERAL_GNK_PER_WEIGHT, BASE_WEIGHT = 4.2, 0.20   # 20% weight free; 4.2 GNK/weight unit for the rest
PARTICIPANT_CAP, N_PARTICIPANTS = 0.30, 4      # 30% cap per participant; fleet split across 4 operators
VESTING_EPOCHS = 180
GNK_SPOT, ONCHAIN_CIRC, DAILY_VOLUME_USD = 0.15, 83.9e6, 65_000
UPTIME = 0.90

# ---- accelerators ----
# weight: PoC weight per unit. H200 = live median (2.27x H100). MI300X = forward estimate 1.8x H100
#   (192 GB HBM3 / 5.3 TB/s vs H200 141 GB / 4.8 TB/s, minus ROCm 10-30% kernel gap; range 1.2-2.4x).
#   CS-3 = forward estimate 40x H100 (23 kW vs 0.7 kW power ratio x Cerebras' claimed ~1.5x tokens/W
#   vs Blackwell; range 25-60x; aggregate tok/s per CS-3 is not disclosed by Cerebras).
# tps: sustained output tok/s on Gonka's lineup (M2.7 230B-A10B, V4 Flash 284B-A13B, GLM-5.3-Flash);
#   InferenceX single-node H200 runs 990-1,580 on 1T-class MoE; lighter MoEs ~1.5-2x that.
# kw: node-level power per accelerator (H200 node 10.2 kW/8). rent: realised $/hr for a large fleet
#   (Silicon Data neocloud index Sept 2026: H200 $3.10, MI300X $2.12; CS-3 has no rental market).
# capex: replacement value (H200 HGX $370k/8; MI300X ~$18k; CS-3 $1.5-3M, no list price).
FLEET = {
    "H200":   dict(n=20_000, weight=970,      tps=1_800,  kw=1.00, rent=3.10, capex=46_000,    live=True),
    "MI300X": dict(n=10_000, weight=1.8*W_H100, tps=1_400, kw=1.10, rent=2.12, capex=18_000,    live=False),
    "CS-3":   dict(n=1_000,  weight=40*W_H100,  tps=48_000, kw=23.0, rent=None, capex=2_000_000, live=False),
}
PUE, KWH_USD = 1.30, 0.05                      # Gulf air-cooled; Abu Dhabi industrial $0.041-0.054/kWh
RENT_UTIL = 0.60                               # billed utilisation of a GPU cloud (breakeven 56-70%)

# ---- inference demand the fleet can actually sell (tokens/day) ----
# Gonka today: 22B tokens/day at 0.001 GNK per 1M tokens (fees ~nil). Fleet capacity is ~100x that,
# so fees are demand-bound. Demand scenarios = tokens/day routed to the fleet at market prices.
USD_PER_M_TOKENS = 0.40                        # blended realised $/M (M2.7/V4 Flash $0.30/1.20 list;
                                               #   GLM-5.x $0.5-4.4; 3:1 input-heavy mix; broker margin out)
DEMAND = {                                     # tokens/day
    "Gonka today":            22e9,
    "UAE gov+enterprise":    150e9,            # TAMM/DGE 11M daily interactions, federal agentic-AI,
                                               #   ADNOC/banks/telcos: ~50-200B tokens/day by 2027 (est.)
    "Global open-model 25%": 1_000e9,          # OpenRouter ~4T tokens/day (May 2026); 25% share
}

# ---- GNK price scenarios (reflexive) ----
SCENARIOS = {
    "A. Spot (no re-rating)":          0.15,
    "B. Bitfury entry (Nov 2025)":     0.60,
    "C. DePIN-peer re-rating":         1.50,
    "D. Rental parity (solved)":       None,
}


def emission_per_day(epoch=EPOCH):
    return E0 * math.exp(-DECAY * epoch) * EPOCHS_PER_DAY


def tranches(include_future):
    return {k: a for k, a in FLEET.items() if a["live"] or include_future}


def fleet_weight(include_future):
    return sum(a["n"] * a["weight"] for a in tranches(include_future).values())


def fleet_share(include_future):
    """Share of emission the fleet captures, after the per-participant cap."""
    raw = fleet_weight(include_future) / (EXISTING_WEIGHT + fleet_weight(include_future))
    return min(raw, PARTICIPANT_CAP * N_PARTICIPANTS)


def capacity_tokens_per_day(include_future):
    return sum(a["n"] * a["tps"] * 86_400 * UPTIME for a in tranches(include_future).values())


def per_unit(name, gnk_price, include_future, demand_tokens):
    a = FLEET[name]
    fw = fleet_weight(include_future)
    gnk_day = emission_per_day() * fleet_share(include_future) * (a["weight"] / fw) * UPTIME
    fill = min(demand_tokens / capacity_tokens_per_day(include_future), 1.0)
    fee_usd = a["tps"] * 86_400 * UPTIME * fill / 1e6 * USD_PER_M_TOKENS
    power_usd = a["kw"] * PUE * 24 * KWH_USD
    rent_usd = a["rent"] * 24 * RENT_UTIL if a["rent"] else None
    return dict(gnk_day=gnk_day, mining=gnk_day * gnk_price, fees=fee_usd, power=power_usd,
                gross=gnk_day * gnk_price + fee_usd, rent=rent_usd, fill=fill)


def collateral_gnk(include_future):
    return fleet_weight(include_future) * (1 - BASE_WEIGHT) * COLLATERAL_GNK_PER_WEIGHT


def parity_price(include_future, demand_tokens):
    """GNK price at which mining + fees == traditional rental across the GPU tranches."""
    names = [n for n, a in tranches(include_future).items() if a["rent"]]
    r = {n: per_unit(n, 0, include_future, demand_tokens) for n in names}
    rent = sum(FLEET[n]["n"] * r[n]["rent"] for n in names)
    fees = sum(FLEET[n]["n"] * r[n]["fees"] for n in names)
    gnk = sum(FLEET[n]["n"] * r[n]["gnk_day"] for n in names)
    return max(rent - fees, 0) / gnk


def report():
    em = emission_per_day()
    print(f"Emission: {em:,.0f} GNK/day (epoch {EPOCH}); at spot ${em*GNK_SPOT:,.0f}/day vs "
          f"${DAILY_VOLUME_USD:,} daily traded volume")
    for phase, fut in (("PHASE 1: 20,000 H200 only", False), ("PHASE 2: full fleet (AMD + Cerebras supported)", True)):
        fw, share = fleet_weight(fut), fleet_share(fut)
        cap = capacity_tokens_per_day(fut)
        print(f"\n=== {phase} ===")
        print(f"fleet weight {fw:,.0f} vs existing {EXISTING_WEIGHT:,} -> raw share "
              f"{fw/(EXISTING_WEIGHT+fw):.1%}, after {N_PARTICIPANTS}x{PARTICIPANT_CAP:.0%} cap {share:.1%}; "
              f"incumbents' per-GPU reward falls {1-EXISTING_WEIGHT/(EXISTING_WEIGHT+fw):.1%}")
        col = collateral_gnk(fut)
        print(f"collateral for full weight: {col/1e6:,.1f}M GNK = {col/ONCHAIN_CIRC:.0%} of on-chain circulation "
              f"(${col*GNK_SPOT/1e6:,.0f}M at spot, ${col*1.5/1e6:,.0f}M at $1.50)")
        print(f"capacity {cap/1e12:,.2f}T tokens/day")
        for dname, dtok in DEMAND.items():
            print(f"\n  demand: {dname} ({dtok/1e9:,.0f}B tokens/day, fill {min(dtok/cap,1):.1%})")
            SCENARIOS["D. Rental parity (solved)"] = parity_price(fut, dtok)
            for sc, p in SCENARIOS.items():
                tot = 0
                line = []
                for name in tranches(fut):
                    r = per_unit(name, p, fut, dtok)
                    yr = r["gross"] * FLEET[name]["n"] * 365
                    tot += yr
                    mult = f"{r['gross']/r['rent']:.2f}x rent" if r["rent"] else "no rental mkt"
                    line.append(f"    {name:6s} {r['gnk_day']:7.1f} GNK/d  ${r['mining']:8.2f} mining + "
                                f"${r['fees']:8.2f} fees = ${r['gross']:8.2f}/d  (power ${r['power']:5.2f}, "
                                f"{mult})  fleet ${yr/1e6:,.0f}M/yr")
                print(f"   {sc} GNK ${p:.2f}: fleet gross ${tot/1e6:,.0f}M/yr")
                print("\n".join(line))
    # self-check: fleet GNK/day sums to emission x share x uptime
    tot = sum(per_unit(n, 1, True, 0)["gnk_day"] * FLEET[n]["n"] for n in FLEET)
    assert abs(tot - em * fleet_share(True) * UPTIME) < 1e-6 * tot


if __name__ == "__main__":
    report()


def ladder(sizes=(250, 500, 1_000, 2_000, 5_000, 10_000, 20_000)):
    """H200 tranche size -> GNK/GPU/day, USD/day at spot, GNK price for rental parity, collateral."""
    a = FLEET["H200"]
    print("\n=== TRANCHE LADDER (H200 only, no fee income, 90% uptime) ===")
    print(f"{'H200s':>7} {'share':>6} {'GNK/GPU/d':>10} {'$/GPU/d@spot':>13} {'x rent':>7} {'parity GNK':>11} "
          f"{'collateral GNK':>15} {'% unlocked float':>17}")
    for n in sizes:
        w = n * a["weight"]
        share = min(w / (EXISTING_WEIGHT + w), PARTICIPANT_CAP * N_PARTICIPANTS)
        gnk = emission_per_day() * share / n * UPTIME
        rent = a["rent"] * 24 * RENT_UTIL
        col = w * (1 - BASE_WEIGHT) * COLLATERAL_GNK_PER_WEIGHT
        print(f"{n:>7,} {share:>6.0%} {gnk:>10.0f} {gnk*GNK_SPOT:>13.2f} {gnk*GNK_SPOT/rent:>7.2f} "
              f"{rent/gnk:>11.2f} {col/1e6:>13.1f}M {col/57.8e6:>17.0%}")


if __name__ == "__main__":
    ladder()
    f = FLEET
    print(f"\nFleet replacement value: H200 ${f['H200']['n']*f['H200']['capex']/1e9:.2f}B, MI300X "
          f"${f['MI300X']['n']*f['MI300X']['capex']/1e9:.2f}B, CS-3 ${f['CS-3']['n']*f['CS-3']['capex']/1e9:.1f}B "
          f"(CS-3 unit cost unverified, $1.5-3M)")
    mw = sum(a['n']*a['kw'] for a in f.values())/1000
    print(f"IT load: {mw:,.0f} MW ({mw*PUE:,.0f} MW at PUE {PUE}); power cost "
          f"${mw*1000*PUE*24*365*KWH_USD/1e6:,.0f}M/yr at ${KWH_USD}/kWh")
    print(f"Collateral per H200 for full weight: {f['H200']['weight']*(1-BASE_WEIGHT)*COLLATERAL_GNK_PER_WEIGHT:,.0f} GNK")
    print(f"Traditional rental per H200: ${f['H200']['rent']*24*RENT_UTIL:.2f}/day; per MI300X ${f['MI300X']['rent']*24*RENT_UTIL:.2f}/day")
    print(f"GAIB private phase realised: ${600_000/200/180:.1f}/H200/day (600K / 200 GPUs / ~180 days)")


# ---- demand-filled revenue scenarios: fleet rented at market vs monetised via Gonka ----
# Assumes demand matches available inference capacity (fill = share of capacity sold), full fleet
# on Gonka with pricing enabled. usd_per_m_out = $ per 1M OUTPUT tokens with input billing folded in
# on a 3:1 input:output mix (medium ~ GonkaBroker/DeepInfra level, ~$0.25 per total token;
# optimistic ~ MiniMax M2.7 / GLM-5.x / DeepSeek V4 Pro list level).
REV_SCENARIOS = {
    "Medium":     dict(gnk=0.60, fill=0.55, usd_per_m_out=1.00, rent_util=0.60, rent_mult=1.00),
    "Optimistic": dict(gnk=1.50, fill=0.80, usd_per_m_out=2.00, rent_util=0.80, rent_mult=1.13),
}


def revenue_scenarios():
    print("\n=== DEMAND-FILLED SCENARIOS: market rental vs via Gonka (full fleet, $/unit/day and $M/yr) ===")
    for sc, p in REV_SCENARIOS.items():
        print(f"\n-- {sc}: GNK ${p['gnk']:.2f}, {p['fill']:.0%} of capacity sold at ${p['usd_per_m_out']:.2f}/M output, "
              f"rental at {p['rent_mult']:.2f}x index and {p['rent_util']:.0%} utilisation")
        tm = tg = 0
        for name, a in FLEET.items():
            tok_day = a["tps"] * 86_400 * UPTIME * p["fill"]
            fees = tok_day / 1e6 * p["usd_per_m_out"]
            gnk_day = per_unit(name, 1, True, 0)["gnk_day"]
            mining = gnk_day * p["gnk"]
            gonka = fees + mining
            market = a["rent"] * p["rent_mult"] * 24 * p["rent_util"] if a["rent"] else fees  # CS-3: direct sales
            tm += market * a["n"] * 365; tg += gonka * a["n"] * 365
            print(f"   {name:6s} market ${market:8.2f}/d = ${market*a['n']*365/1e6:7.0f}M/yr | "
                  f"gonka ${gonka:8.2f}/d (fees ${fees:.2f} + mining {gnk_day:.1f} GNK=${mining:.2f}) = "
                  f"${gonka*a['n']*365/1e6:7.0f}M/yr | {gonka/market:.2f}x")
        print(f"   TOTAL  market ${tm/1e6:,.0f}M/yr | via Gonka ${tg/1e6:,.0f}M/yr | {tg/tm:.2f}x")


if __name__ == "__main__":
    revenue_scenarios()

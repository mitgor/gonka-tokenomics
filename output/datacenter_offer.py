"""Datacenter offer harness: what a datacenter's GPU capacity earns if it joins Gonka.

Simulates one or more datacenters joining the live network (cumulatively, in the order given),
and prints an offer sheet per datacenter: GNK and USD per GPU per day, per year, network share,
collateral to unlock full weight, the GNK price at which mining yield matches on-demand rental,
and the comparison with long-term contract rates. Reuses the protocol constants and founder
calibration in uae_fleet_model_v2.py.

Usage:
  python3 datacenter_offer.py --dc "Khazna:H200=2000,B300=64" --dc "EHC:MI300X=1000"
  python3 datacenter_offer.py --dc "Moro:H200=500" --gnk 0.15 --gnk 2.0 --uptime 0.92
  python3 datacenter_offer.py --dc "Site:MW=5,type=H200"        # size a tranche from power capacity
  python3 datacenter_offer.py --selftest
"""
import argparse
import sys

import uae_fleet_model_v2 as m

# weight = live median PoC weight (H100/H200/B200/A100), founder-implied (B300, MI300X),
# forward estimate (CS-3). od = on-demand $/hr Sept 2026. kw = node-level power per unit.
GPUS = {
    "H100":   dict(weight=427,   od=3.38, kw=0.90),
    "H200":   dict(weight=970,   od=4.50, kw=1.00),
    "B200":   dict(weight=1_598, od=6.97, kw=1.40),
    "B300":   dict(weight=2_724, od=7.85, kw=1.60),
    "A100":   dict(weight=203,   od=1.50, kw=0.50),
    "MI300X": dict(weight=476,   od=1.80, kw=1.10),   # not yet supported on Gonka
    "CS-3":   dict(weight=17_080, od=None, kw=23.0),  # not yet supported; no rental market
}
CONTRACT = 0.45          # long-term contracts pay ~0.4-0.5x on-demand (founder)
PUE = 1.30


def parse_dc(spec):
    """'Name:H200=2000,B300=64' or 'Name:MW=5,type=H200' -> (name, {gpu: n})."""
    name, _, body = spec.partition(":")
    kv = dict(p.split("=") for p in body.split(",") if p)
    if "MW" in kv:
        t = kv.get("type", "H200")
        n = int(float(kv["MW"]) * 1000 / (GPUS[t]["kw"] * PUE))
        return name, {t: n}
    return name, {k: int(v) for k, v in kv.items()}


def weight_of(fleet):
    return sum(n * GPUS[g]["weight"] for g, n in fleet.items())


def offer(name, fleet, network_weight, gnk_prices, uptime):
    """Offer sheet for one datacenter, given the network weight it joins (excluding itself)."""
    em = m.emission_per_day()
    w = weight_of(fleet)
    share = min(w / (network_weight + w), m.PARTICIPANT_CAP * m.N_PARTICIPANTS)
    gnk_day = em * share * uptime
    collateral = w * (1 - m.BASE_WEIGHT) * m.COLLATERAL_GNK_PER_WEIGHT
    od_day = sum(n * GPUS[g]["od"] * 24 for g, n in fleet.items() if GPUS[g]["od"])
    parity = od_day / gnk_day if od_day else float("nan")
    mw = sum(n * GPUS[g]["kw"] for g, n in fleet.items()) * PUE / 1000
    print(f"\n=== OFFER: {name} — {', '.join(f'{n:,} {g}' for g, n in fleet.items())} ===")
    print(f"network share {share:.1%}  |  {gnk_day:,.0f} GNK/day = {gnk_day*365/1e6:,.1f}M GNK/yr  |  "
          f"collateral for full weight {collateral/1e6:,.2f}M GNK  |  {mw:.1f} MW at PUE {PUE}")
    print(f"GNK price for mining = on-demand rental: ${parity:,.2f}   (contracts pay ~{CONTRACT:.0%} of on-demand)")
    print(f"{'GPU':7s} {'weight':>7} {'GNK/GPU/d':>10} " + " ".join(f"{'$/d @'+format(p,'.2f'):>12}" for p in gnk_prices)
          + f" {'on-demand $/d':>14} {'contract $/d':>13}")
    for g, n in fleet.items():
        gw = GPUS[g]["weight"]
        gd = em * share * uptime * gw / w
        od = GPUS[g]["od"]
        row = f"{g:7s} {gw:>7,} {gd:>10.1f} " + " ".join(f"{gd*p:>12,.2f}" for p in gnk_prices)
        row += f" {od*24:>14,.2f} {od*24*CONTRACT:>13,.2f}" if od else f" {'n/a':>14} {'n/a':>13}"
        print(row)
    yr = [gnk_day * 365 * p for p in gnk_prices]
    print("fleet USD/yr: " + "  ".join(f"@${p:.2f} ${v/1e6:,.1f}M" for p, v in zip(gnk_prices, yr))
          + (f"  |  on-demand ${od_day*365/1e6:,.1f}M, contract ${od_day*CONTRACT*365/1e6:,.1f}M" if od_day else ""))
    return w


def selftest():
    em = m.emission_per_day()
    one_h200 = em * (970 / (m.EXISTING_WEIGHT + 970)) * 970 / 970 * m.GNK_SPOT
    assert abs(one_h200 - 4.50 * 24 * 1.3) / (4.50 * 24 * 1.3) < 0.05, one_h200   # founder: 1.3x on-demand
    assert parse_dc("X:MW=1,type=H200")[1]["H200"] == int(1000 / (1.0 * PUE))
    print("selftest ok: one H200 on today's network earns "
          f"${one_h200:.0f}/day (founder: ${4.5*24*1.3:.0f})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dc", action="append", default=[], help='"Name:H200=2000,B300=64" or "Name:MW=5,type=H200"')
    ap.add_argument("--gnk", action="append", type=float, help="GNK price scenario(s); default spot, $2, $4.50")
    ap.add_argument("--uptime", type=float, default=m.UPTIME)
    ap.add_argument("--network-weight", type=float, default=m.EXISTING_WEIGHT, help="live weight before joins")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest(); sys.exit()
    if not a.dc:
        ap.print_help(); sys.exit(1)
    prices = a.gnk or [m.GNK_SPOT, 2.0, 4.5]
    print(f"Live network weight {a.network_weight:,.0f}; emission {m.emission_per_day():,.0f} GNK/day; "
          f"datacenters join in the order given, each offer reflects everyone before it.")
    nw = a.network_weight
    for spec in a.dc:
        name, fleet = parse_dc(spec)
        nw += offer(name, fleet, nw, prices, a.uptime)
    if len(a.dc) > 1:
        print(f"\nAfter all joins: network weight {nw:,.0f} "
              f"({nw/a.network_weight:.0f}x today). Re-run with each DC alone to see its standalone offer.")

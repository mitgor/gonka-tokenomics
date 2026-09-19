# Founder calibration note (Gonka founders, September 19, 2026)

Points relayed by David Liberman, paraphrased from the original (Russian) messages. Used to
recalibrate `uae_fleet_model_v2.py`, `gonka_uae_fleet_blurbs_v2.md` and `datacenter_offer.py`.

## Current-network yields (494 GPUs, epoch ~397)
| GPU | Yield vs on-demand | On-demand $/hr | Low point seen | Implied PoC weight |
|---|---|---|---|---|
| MI300X | 1.6x | $1.80 | 0.9x | 476 (1.1x H100, 0.49x H200) |
| H200 | 1.3x | $4.50 | 0.7x | 967 (matches live median 970) |
| B300 | 2.1x | $7.85 | 1.2x | 2,724 (2.8x H200; live median 1,611 on n=10) |

- GPU owners on long-term contracts receive under 0.4–0.5x of on-demand rates.
- Advice: lead with MI300X, B300 and maybe Cerebras; not with H200.

## Price path
- Connecting 10,000 MI300X alone takes GNK to ~$2, giving the same per-GPU earnings at larger
  scale rather than more (model reproduces $2.01 at 1.2x on-demand yield).
- If the network keeps growing after that: 10% month-on-month adds 1.5x (~$3), 20% adds 2.3x
  (~$4.50), 50% adds 7x (~$14). Assumes six months of gradual fleet-driven growth, then six
  months of organic growth. These are haircut figures (straight compounding: 1.8x, 3.0x, 11.4x).

## Open questions sent back
1. Is the MI300X yield measured on an internal build or projected from benchmarks?
2. What haircut sits behind the growth multipliers?

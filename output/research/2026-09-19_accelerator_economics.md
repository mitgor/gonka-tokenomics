# Accelerator economics fact sheet (agent, 2026-09-19) — key items
## H200 rental
- On-demand median $4.40 (getdeploying/aimultiple 2026-09-18); Silicon Data neocloud index $3.10 (up 14% May-Jul 2026); cheapest in-stock $3.00; DeepInfra $2.69; CoreWeave spot $2.62; Nebius spot $2.45; Gcore $3.13; Akash $4.45; Vast $3.45.
- Reserved: GCP $4.66 (36mo), Azure $6.86, AWS capacity block ~$5, Together $3.99-4.99, Cirrascale n/a. InferenceX hyperscaler-volume cost basis $1.22-1.41/hr.
- H200 vs H100: ~1.4x decode (bandwidth), 1.37-1.42x MLPerf 70B; +79-115% on Llama 3.3 70B FP4 (InferenceX). H100 median $3.38; B200 $6.97.
- New price $30-40k/GPU; HGX 8x $300-420k (~$370k typical); resale H200 NVL executed $32.3k (102% of launch basis); H100 SXM $14.6k (43%).
- Power 700W TDP; node ~10.2kW.
- "H200 not yet available in UAE hyperscaler DCs" (Spheron Jul 2026). No reporting of stranded H200 in Gulf. Operational GPU est: Abu Dhabi 15-20k, Dubai 5-8k.
## MI300X
- Median $2.90 (-4% 90d); Silicon Data $2.12; reserved DO $1.91, Cyfuture $1.61, Azure $3.45; spot $1.11-1.85; TensorWave from $1.71. SemiAnalysis: MI300X must rent at $1.9-2.4 to match H200 perf/$ at $2.50; H200 beats MI300X on DeepSeek V3; ROCm 90-95% CUDA throughput. NOT listed on Akash/io.net/Vast. MSRP ~$15k, market ~$18k; eBay $20-25k. 750W TBP (585-701W measured). MI355X = 92-104% of B300 (MLPerf 6.0). vLLM recipes for DeepSeek V4 Flash + Kimi K3 on MI300X exist.
## Cerebras CS-3
- No list price: CG-1 64 CS-2 >$100M (~$1.56M/node incl infra, 2023); Wikipedia "up to $3M/node"; 23 kW (25kW alt), 15U. No per-hour rental published. Inference API: gpt-oss-120b $0.35/$0.75 @3,000 tok/s/user; Llama 405B $6/$12 @969; K2.6 981 tok/s/user; reserved blended $0.25-0.60 (unverified). Claims vs DGX B200: 21x faster per user Llama 70B, 32% lower cost, 32% lower power. Aggregate tok/s per CS-3 never disclosed. CS-4 (Aug 2026): 2x speed, 10x throughput/W, ships Q3 2026. OpenAI 750MW deal; Condor Galaxy India 64 CS-3 (G42, May 2026); MBZUAI 62% + G42 24% of 2025 revenue. IPO May 2026 CBRS $185 → ~$66B. Cloud GM 20-30%.
## Hosting economics
- Breakeven util ~56-70%; neocloud GM 55-65% pre-depreciation; CoreWeave Q2 2026 GAAP GM 65.9%, adj op margin 5%.
- All-in capex ~$50k/GPU greenfield (server $30k, network $4k, storage $2.5k, facility $14k). Payback 100xH100: 20mo @ $3.50, 30mo @ $2.50, 45mo @ $1.80; H200 at $3.49 → ~20+mo real.
- Colo $140-260/kW-mo; PUE Gulf air 1.4-1.6, Khazna liquid 1.20-1.25.
- Abu Dhabi ADDC industrial AED 0.150/kWh = $0.041; commercial $0.054; Dubai $0.063-0.103; regional est $0.05-0.07. Gulf risk premium 15-25% on GPU pricing.
- Enterprise GPU util avg ~5% (Speediyo, paywalled). Deloitte: own above 70% util.
## Token economics
- Open model prices ($/M in/out): DeepSeek V4 Pro $1.32/$3.96 Together, $1.30/$2.60 DeepInfra; V4.1 Flash $0.30/$1.20 official, $0.09/$0.18 DeepInfra; Kimi K3 $3/$15; GLM-5.3 $1.40/$4.40; GLM-5.3-Flash $0.15/$0.50; GLM-5.2 $0.49-0.75/$1.56-2.40; Qwen3.5-397B $0.45/$3; Llama 4 Maverick $0.27/$0.85; MiniMax M2.7 $0.30/$1.20; gpt-oss-120b $0.15/$0.60; Llama 3.3 70B $0.59-1.04.
- H200 tok/s/GPU: DeepSeek V4 Pro 5,139 @100 tok/s/user (multi-node disagg, InferenceX 2026-09-16); R1 single-node 739-1,582; V3 wide-EP 2,200; K2.6 INT4 991 @32; Llama 3.3 70B FP4 3,310 @38; V4 Flash ~250/GPU (rough, 4x H200).
- Gross token revenue per H200-hr at 100% util: V4 Pro $48-73; R1 $7-15; K2.6 $10.7; Llama 70B $9-12 vs rental $3-4.40. DeepInfra rents H200 $2.69 and sells V4 Pro at $2.60/M → ~39x markup over InferenceX cost.
- OpenRouter total ~28T tokens/week (May 2026, from repo). io.net 4B daily tokens.
## Export
- BIS A:5 (2026-07-10): license-free NVIDIA/AMD to G42, Core42, MGX, US hyperscalers in UAE. Nov 2025: 35k GB300 each G42/HUMAIN. Microsoft license ~60.4k A100-eq incl GB300; had shipped 21.5k A100-eq mix of A100/H100/H200. Stargate UAE phase 1 ~100k GB300, 200MW, Q3 2026 target.

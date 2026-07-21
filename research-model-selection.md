# Top 5 Open-Source Models for Gonka.ai — Usage Demand Analysis

**Date:** 2026-07-18 (originally 2026-02-13; re-baselined for the July 2026 model landscape)
**Purpose:** Identify which open-source AI models would generate the highest usage demand on Gonka.ai's GPU compute network, based on GitHub activity, X.com presence, HuggingFace downloads, and real-world inference demand on competing decentralized networks.

**Context (July 2026):** Gonka is no longer a single-model network. It serves Qwen3 235B, Kimi K2.6, and MiniMax M2.7 at ~100M tokens/day combined, with GLM-5.2 listed as "coming soon" on the Gonka blog — reseller Gonka24 already publishes a GLM-5.2 rate card at $0.095/$0.30 per 1M (its struck-through "$0.95/$3.00 list" is Gonka24's own marketing anchor, not any real provider's rate — Z.ai's official API is $1.40/$4.40 per 1M; OpenRouter serves it from ~$0.41–$1.00 in / ~$4.00 out). That fourth family partially answers the "no frontier-class option" model-breadth criticism. This doc ranks what to serve (and keep serving) next.

---

## Ranking Criteria

- **GitHub activity** — Stars, forks, contributors, release cadence
- **X.com buzz** — Community discussion volume, viral potential, developer mindshare
- **Inference demand** — Actual usage on decentralized compute networks (Akash, Render) and on Gonka itself
- **GPU intensity** — How much compute each request consumes (higher = more revenue per request)
- **Ecosystem fit** — How well the model maps to distributed GPU infrastructure

---

## #1. Kimi K2.6 / K2.7-Code — with K3 weights imminent

**Category:** Agentic / Coding LLM (MoE)
**License:** Modified MIT

### Why #1

Agentic models are the hottest category in mid-2026, and Moonshot's K-series leads it. Kimi K2.6 (April 20, 2026: 1T MoE, 32B active, ~256K context, multimodal) now powers Kimi's paid chat and is already served on Gonka. Kimi K2.7-Code (June 12, 2026) is the current best open coding-agent model: +21.8% on Kimi Code Bench v2 over K2.6 with ~30% fewer reasoning tokens. Kimi K3 (launched July 16, 2026: 2.8T-param MoE with 896 experts, 1M-token context, always-on thinking mode, native multimodal, $3/$15 per 1M API) debuted #3 on the Artificial Analysis Intelligence Index (57.11 — level with Opus 4.8 and GPT-5.5, behind Claude Fable 5 and GPT-5.6 Sol) and took #1 in Frontend Code Arena (1,679) ahead of Claude Fable 5 (1,631) and GPT-5.6 Sol (1,618) — the first open model to top a frontier arena leaderboard. With full open weights committed for July 27, 2026 on Hugging Face (API/app only until then), expected under Moonshot's Modified MIT license — hosting-eligible for Gonka, unlike MiniMax's Community License — it would be the largest open-weight model to date (a title MiniMax's rumored 2.7T "M3 Pro" could contest as early as Q3 2026 — see #3).

Note: K2.5 (Jan 2026) is now three generations behind. Moonshot discontinued the older kimi-k2 series API models on May 25, 2026, and following the K3 launch its platform docs state K2.5 is closed to newly registered users, with API traffic redirected to K2.6 and full platform sunset scheduled August 31, 2026. Any K2.5-anchored plan has ~6 weeks of first-party shelf life; third-party hosts (OpenRouter $0.375/$2.025, DeepInfra $0.45/$2.25) still serve it, with lifecycle risk.

### Signals

| Signal | Data |
|--------|------|
| Momentum | K2.6 → K2.7-Code → K3 shipped within three months; K3 dominated AI news July 16–17 |
| Third-party hosting | Together, Fireworks, DeepInfra all headline K2.6/K2.7 |
| Pricing anchor | K2.7-Code official API: $0.95 input / $0.19 cache-hit / $4.00 output per 1M tokens; K3: $3/$15 per 1M ($0.30/M cached input = 90% discount), built-in web search billed $0.015/call |
| Gonka demand | K2.6 already live on the network (a K2.6 validation fix shipped in the v0.2.13 cycle) |

### Hardware Requirements

- **K2.6 / K2.7-Code:** 1T total params, 32B active — multi-node H100/H200-class deployments; K2.7-Code needs ~577GB VRAM at INT4
- **K3:** 2.8T total / ~50B active ("2.8T-A50B"; 16 of 896 experts active per token), ships in MXFP4 quantization; Moonshot recommends at least 64 accelerators for serving — feasible only for Gonka's largest hosts once weights land

### Gonka.ai Fit

The natural tiering story: K2.6 as the workhorse agent tier (already served), K2.7-Code as the coding-agent tier, K3 as the frontier tier once weights land. Serving the newest open frontier model days after release is the single strongest demand magnet available to a decentralized network.

### Links

- https://huggingface.co/moonshotai/Kimi-K2.7-Code
- https://platform.kimi.ai/docs/models
- https://simonwillison.net/2026/Jul/16/kimi-k3/

---

## #2. GLM-5.2 (Zhipu / Z.ai) — All-Round LLM

**Category:** General Purpose / Coding LLM (MoE)
**License:** MIT

### Why #2

GLM-5.2 (announced June 13, 2026; weights out June 16) is the strongest all-round open-weight model as of July 2026: ~744B-param MoE (~40B active; LLM Stats lists 753B — sources disagree), 1M-token context (5x GLM-5.1's 200K; 131K output), MIT license, selectable High/Max reasoning modes. Artificial Analysis Intelligence Index v4.1 puts it at ~51, ahead of MiniMax M3 (44), DeepSeek V4 Pro (44), and Kimi K2.6 (44). Independent testing has it beating GPT-5.5 on coding at roughly 1/6 the cost (SWE-bench Pro 62.1 vs GPT-5.5's 58.6). API pricing: $1.40/$4.40 per 1M ($0.26 cached) direct from Z.ai, or $1.00/$4.00 via OpenRouter. Caveat: Zhipu shipped GLM-5.2 with no official benchmarks; secondary-blog figures like Terminal-Bench 81.0 / DeepSWE 46.2 are unverified — do not quote externally. It is already on Gonka's "coming soon" list — this pick is being validated in real time.

### Signals

| Signal | Data |
|--------|------|
| Benchmarks | SWE-bench Pro 62.1 (independent; vs GPT-5.5's 58.6); Intelligence Index v4.1 ~51 — top downloadable open-weight model (K3's 57.11 stays API-only until Jul 27) |
| License | MIT — cleanest possible for commercial hosting |
| Gonka status | "Coming soon" per Gonka blog; Gonka24 rate card live at $0.095/$0.30 per 1M — a ~93% undercut vs Z.ai's $1.40/$4.40 official rate (ignore Gonka24's own "$0.95/$3.00 list" anchor) |
| Mindshare | Chinese open models (Kimi, DeepSeek, Qwen, GLM, MiniMax) now dominate open-weight leaderboards |

### Hardware Requirements

- **GLM-5.2:** ~744B total / ~40B active — multi-GPU enterprise deployment; quantized variants reduce footprint

### Gonka.ai Fit

The "default strong open model" slot that Llama used to own has shifted to Qwen/DeepSeek/GLM. GLM-5.2's MIT license and 1M-token context make it the premium general-purpose tier Gonka has lacked — and with it now "coming soon" on the network (Gonka24 rate card already live), the priority shifts from "add it" to "launch it well and price the undercut."

### Links

- https://www.eigent.ai/blog/glm-5-2
- https://datanorth.ai/news/zhipu-ai-releases-glm-5-2
- https://kie.ai/blog/glm-5-2-benchmark-deep-dive

---

## #3. MiniMax M3 (with M2.5 / M2.7 legacy tiers) — Efficient Agent LLM

**Category:** Agentic / SWE LLM (MoE, multimodal)
**License:** MiniMax Community License (open weights on Hugging Face: MiniMaxAI/MiniMax-M3 — NOT MIT/Apache; see caveat below)

### Why #3

MiniMax M3 (released June 1, 2026; open weights on Hugging Face by ~June 7) is now the MiniMax flagship: 428B total / 23B active MoE with MiniMax Sparse Attention (MSA), 1M-token context, native multimodality (image + video input; can operate a desktop), thinking + non-thinking modes. Vendor-reported: 80.5% SWE-bench Verified and 59.0% SWE-Bench Pro (above GPT-5.5 and Gemini 3.1 Pro on that suite). First-party pricing is $0.30/$1.20 per 1M for inputs up to 512K tokens, rising to $0.60/$2.40 above 512K — and the pricing page labels these rates a permanent 50% discount off struck-through list prices. Cost-model any 1M-context agent workload at the $0.60/$2.40 tier, not the headline rate.

**License caveat:** M3 ships under the "MiniMax Community License," not MIT/Apache. Per the LICENSE file on Hugging Face, commercial use requires prominent "Built with MiniMax M3" attribution (website/UI/docs), and there is no notification-free commercial tier: organizations below $20M/year revenue must send a one-time commercial-use notification email to api@minimax.io, while those at or above $20M/year need separate prior written authorization from MiniMax. For a commercial decentralized hosting network that is a materially different posture than MIT (GLM-5.2, DeepSeek V4), Apache 2.0 (Qwen 3.5/3.6, Inkling, Mistral 3), or Modified-MIT (Kimi) — get legal review before committing GPU capacity.

The legacy tiers remain relevant, though M2.5 (Feb 12, 2026) no longer leads open-weight SWE-bench Verified: its 80.2% has been edged by M3's 80.5% and DeepSeek V4 Pro's 80.6% (all vendor-reported). M2.5 still holds 51.3% Multi-SWE-bench (#1) and 76.3% BrowseComp — a 230B MoE with only 10B active parameters. M2.7 (released March 18, 2026; open-sourced ~April 12; 205K context) scores 56.22% SWE-Pro and 57.0% Terminal Bench 2 with "self-evolving agent" training, and is already served on Gonka (route support added in devshard v3, July 9, 2026).

**Roadmap watch (single-sourced):** The Information reported in mid-July 2026 that MiniMax is preparing "M3 Pro," a 2.7-trillion-parameter model — ~6x M3's total size, rivaling Kimi K3's 2.8T — with a planned open-source release as early as Q3 2026. Active-parameter count and license terms are unannounced. If real, it breaks the "MiniMax = small-active-params margin engine" framing below and contests K3's largest-open-model claim; whether it ships under the Community License or something else is decisive for Gonka hosting.

### Signals

| Signal | Data |
|--------|------|
| Flagship | M3: 428B/23B MoE, 1M context, native multimodal, 80.5% SWE-bench Verified / 59.0% SWE-Bench Pro (vendor-reported) |
| Benchmarks | M2.5: 80.2% SWE-bench Verified (former open-weight leader), 51.3% Multi-SWE-bench (#1) |
| License risk | MiniMax Community License: attribution required; notification email below $20M/yr revenue, written authorization at/above $20M/yr |
| Economics | 10–23B active params — the most serve-efficient frontier-class agent models available |
| Gonka demand | M2.7 already live on the network; M3 is the natural upgrade path |
| Roadmap | "M3 Pro" (2.7T params, possible Q3 2026 open-source release) reported by The Information, mid-July 2026 — single-sourced, license unannounced |

### Hardware Requirements

- **M2.5 / M2.7:** 230B total / 10B active — single-node enterprise GPU deployments feasible
- **M3:** 428B total / 23B active — larger footprint than M2.x but still far below 1T-param K-series

### Gonka.ai Fit

The small-active-params design is the best economics fit for a distributed GPU network: many more nodes can serve MiniMax than K-series or GLM, at near-frontier agent quality. Where Kimi is the demand magnet, MiniMax is the margin engine — and M3's multimodal input adds a capability no other model in Gonka's lineup has.

### Links

- https://www.minimax.io/blog/minimax-m3
- https://huggingface.co/MiniMaxAI/MiniMax-M3
- https://huggingface.co/blog/mlabonne/minimax-m25
- https://www.marktechpost.com/2026/04/12/minimax-just-open-sourced-minimax-m2-7-a-self-evolving-agent-model-that-scores-56-22-on-swe-pro-and-57-0-on-terminal-bench-2/

---

## #4. FLUX.2 (dev / schnell) — Image Generation

**Category:** Text-to-Image
**License:** Open weights (dev: non-commercial research; schnell: Apache 2.0)

### Why #4

Image generation is the single biggest consumer of GPU inference hours in open-source AI. FLUX.2 (Black Forest Labs, Nov 2025) is the successor to Stable Diffusion, built by the same core researchers, and remains a leading open image family for photorealism. As of mid-2026 it no longer clearly leads, however: roundups place it in a tight cluster with Qwen-Image/Qwen Image Max, HunyuanImage 3.0, HiDream, and Stable Diffusion 3.5, and the Artificial Analysis Text-to-Image Arena's open-weights leader is NVIDIA's Cosmos3-Super-Text2Image (~1,216 Elo as of mid-July 2026, ahead of the next open models HiDream-O1-Image-Dev at 1,185 and Ideogram 4.0 Quality at 1,166; arena Elos drift weekly, so treat exact figures as snapshots; 65B params, permissive OpenMDW-1.1 license, serves via vLLM-omni/SGLang). FLUX.2 still wins this slot on community/tooling momentum (ComfyUI), not raw arena rank — re-evaluate the pick against Cosmos3 before committing GPU capacity; its license is cleaner than FLUX.2 dev's non-commercial terms.

### Signals (Feb 2026 estimates, not re-verified)

| Signal | Data |
|--------|------|
| GitHub/Community | ComfyUI (primary interface) doubled in popularity; developer count grew 10x YoY |
| X.com | Constant stream of FLUX.2 generations shared; creative community extremely active |
| Usage volume | Stable Diffusion ecosystem generated 12.59B images through 2024; FLUX.2 absorbing this demand |
| GPU demand | 32B parameter model — needs serious GPU, especially at 4MP output resolution |

### Hardware Requirements

- **FLUX.2 schnell:** ~12GB VRAM (quantized), fast generation
- **FLUX.2 dev (FP8):** ~16GB VRAM
- **FLUX.2 dev (BF16):** ~24GB+ VRAM
- **GGUF quantized variants:** Scale from 8GB to 24GB depending on quality

### Gonka.ai Fit

Each image generation request burns seconds of GPU time. FLUX.2 dev is free to download but needs real GPU muscle — exactly what a compute network sells. The creative AI community is enormous and accustomed to paying for cloud GPU access; ComfyUI integration makes this trivially accessible. Image/video remains the gap on LLM-centric decentralized networks — including Gonka's current all-LLM lineup.

### Links

- https://huggingface.co/black-forest-labs/FLUX.2-dev
- https://comfyanonymous.github.io/ComfyUI_examples/flux2/
- https://pxz.ai/blog/flux-vs-stable-diffusion:-technical-&-real-world-comparison-2026

---

## #5. Wan 2.7 (fallback: Wan 2.2) — Video Generation

**Category:** Text-to-Video / Image-to-Video
**License:** Apache 2.0

### Why #5

Video generation is extremely GPU-intensive (minutes of GPU time per clip vs seconds for images) and the fastest-growing consumer AI category. The earlier "video frontier went closed" framing has flipped: after an API-first window (Wan 2.5-Preview, Wan 2.6), **Wan 2.7 weights are open under Apache 2.0** — now confirmed on both Hugging Face and ModelScope, with inference code at Wan-Video/Wan2.7 on GitHub (all live by April 22, 2026, alongside the April 6 API launch, ~$0.10/sec of 720p at the time). Wan 2.7 is a ~27B total / 14B active MoE that generates up to 1080p video up to 15 seconds with native audio output, adds a chain-of-thought "thinking mode" planning step, and ships four heads under one architecture: text-to-video, image-to-video, reference-to-video (with voice cloning), and instruction-based video editing. Together AI already serves a Wan 2.7 API — the earlier "verify the artifacts before committing capacity" caveat is closed. Wan 2.7 supersedes Wan 2.2 as the serve target; Wan 2.2 remains the budget-tier fallback.

### Signals

| Signal | Data |
|--------|------|
| GitHub | Wan2GP ("for the GPU poor") remains an active community project with many forks/wrappers |
| X.com | Video generation demos go viral constantly |
| Open weights | Wan 2.2 and Wan 2.7 both Apache 2.0 (Wan 2.7 on Hugging Face + ModelScope, code at Wan-Video/Wan2.7); Wan 2.5/2.6 remain API-only |
| Third-party hosting | Together AI serves a Wan 2.7 API — commercial demand validated |
| Competition | HunyuanVideo 1.5 (Tencent, 8.3B params) and LTX-2 are the main open alternatives |

### Hardware Requirements

- **Wan 2.7:** ~27B total / 14B active MoE; consumer FP8 deployment feasible at reduced settings, 80GB-class GPUs for full-quality 1080p/15s with audio
- **Wan 2.2 T2V-1.3B:** ~8GB VRAM (consumer GPU accessible; Feb 2026 figure, not re-verified)
- **Wan 2.2 T2V-14B:** Multi-GPU or high-end enterprise GPU; ~4 minutes for a 5-second 480p video on RTX 4090 unoptimized (Feb 2026 figure, not re-verified)

### Gonka.ai Fit

Video is the GPU-hungriest workload in consumer AI — the highest revenue ceiling per request. With Wan 2.7 weights open, Gonka can host the actual video frontier, not a generation-old fallback: full-quality 1080p with native audio is exactly the hardware tier a compute network sells, while consumers cap out at reduced FP8 settings. The audio and video-editing heads materially widen the serve case beyond plain t2v. Position it as "frontier open video, hosted" — and keep Wan 2.2 as the budget tier.

### Links

- https://github.com/deepbeepmeep/Wan2GP
- https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
- https://wavespeed.ai/landing/models/best-open-source-video-models-2026

---

## Honorable Mentions

| Model | Category | Why Considered | Why Not Top 5 |
|-------|----------|----------------|---------------|
| DeepSeek V4 (Pro 1.6T/49B, Flash 284B/13B) | Reasoning/General LLM | Preview released Apr 24, 2026; official V4 launching mid-July 2026 with China's first time-of-day API pricing — regular rates V4-Pro ¥3.00/¥6.00 per 1M (≈$0.42/$0.84, ¥0.025 cache-hit), V4-Flash ¥1.00/¥2.00, DOUBLING during Beijing peak hours (9:00–12:00, 14:00–18:00); legacy deepseek-chat/deepseek-reasoner endpoints retire after July 24, 2026 (forced migration); 1M-token context; MIT license, open weights; V4 Pro (Think Max) scores 80.6% SWE-bench Verified — the highest open-weight result, tied with Gemini 3.1 Pro (~55% on SWE-bench Pro); large efficiency gains (V4-Pro: ~27% of V3.2's single-token FLOPs, 10% of its KV cache at 1M context) | Strong, but overlaps GLM/Kimi slots; peak-hour pricing means any 24/7 agent cost model using the flat rate understates Beijing-business-hours cost by up to 2x — and "no rush-hour pricing" is a new positioning lever for Gonka. No R2 exists as of July 2026 — reasoning is folded into V4. Note: R1 and its distills (Jan 2025) are 18 months old and no longer competitive — earlier versions of this doc ranked them #1 |
| Qwen3.5 / 3.6 (397B-A17B down to 0.8B, Apache 2.0) | Efficient MoE family | Already served on Gonka; broadest size range in open source; Qwen3-Coder-480B at 69.6% SWE-bench Verified | Already live — keep serving; the efficient-tier pick is now dense Qwen3.6-27B (Apr 22, 2026 — reportedly beats the 397B Qwen3.5 flagship on agentic coding and fits a single 24GB GPU), ahead of Qwen3.6-35B-A3B. Note the family split: Qwen3.5/3.6 are Apache 2.0 open weights, but Qwen3.7 Max (May 20, 2026: 1M context, reasoning-native, DashScope-API-only at $2.50/$7.50 per 1M with 90% cache discount) is the first closed Qwen flagship — the shift began with Qwen3.6-Max-Preview (Apr 20). Smaller open-weight Qwen 3.7 variants are expected on the 3.6 cadence (Jun–Jul 2026), i.e. potentially imminent — a watch item alongside K3 weights and the Mistral early-access model, relevant to whether Gonka re-tiers its Qwen lineup |
| Thinking Machines Inkling (975B/41B) | General LLM (multimodal MoE) | Released Jul 15, 2026, Apache 2.0, 1M context, 45T-token pretrain, controllable thinking effort; leading US open-weights model per Artificial Analysis; Inkling-Small (12B active) preview | Too new to have proven inference demand; strong candidate for a future Apache-2.0 Western tier — watch closely |
| NVIDIA Nemotron 3 Ultra (550B/55B) | General LLM (hybrid Mamba-Attention MoE) | Weights on HF June 4, 2026; 1M context; OpenMDW-1.1 permissive license (weights + training data + recipes, commercial use allowed); Intelligence Index v4.1 = 48 | Behind the Chinese open frontier; superseded as US leader by Inkling |
| Mistral Large 3 (675B/41B) / Medium 3.5 / Ministral 3-14B | General LLM | Entire line Apache 2.0 — most permissive frontier-class Western licensing; Mistral confirms a much larger "fat but sparse" MoE family in early access July 2026 (params/benchmarks/license undisclosed) targeting the frontier gap | Behind Chinese open models on agent/coding benchmarks; the early-access model is a watch item alongside K3 weights |
| Llama 4 (Scout/Maverick) | General LLM | Last open Llama models (Apr 2025); still widely deployed | Meta effectively exited frontier open weights: Muse Spark (Apr 8, 2026) is closed, Behemoth never shipped, no Llama 5 exists (confirmed by Wikipedia, VentureBeat, deeplearning.ai). Source-hygiene warning: multiple SEO sites publish detailed fake "Llama 5 released" articles — treat any Llama 5 claim in web roundups as fabricated. No longer competitive |
| Whisper Large V3 Turbo | Speech-to-Text | Gold standard STT, 99+ languages, 809M params | Lightweight model — low GPU demand per request |
| Kokoro TTS (82M) | Text-to-Speech | Excellent quality, Apache 2.0, 210x real-time on RTX 4090 | Tiny model, runs on CPU — doesn't drive GPU demand |
| HunyuanVideo 1.5 / LTX-2 | Video Generation | Open-weight alternatives to Wan | Wan family has more community momentum; complementary offerings |

---

## Strategic Summary

### Demand Profile by Category

| Model | Category | GPU Intensity | User Volume | Revenue/Request |
|-------|----------|--------------|-------------|-----------------|
| Kimi K2.6/K2.7 (+K3) | Agent LLM | Very High | Very High | High |
| GLM-5.2 | All-round LLM | High | High | Medium-High |
| MiniMax M3 (M2.5/M2.7 legacy) | Agent LLM (efficient, multimodal) | Low-Medium | High | Medium (best margin) |
| FLUX.2 | Image Gen | High | Very High | High |
| Wan 2.7 (fallback 2.2) | Video Gen | Very High | Growing | Very High |

### Recommended Rollout Strategy

**Wave 1 (already live — deepen):**
- Kimi K2.6 and MiniMax M2.7 are already served; add K2.7-Code as the coding-agent tier and keep Qwen current (3.5/3.6, with dense 3.6-27B as the efficient tier)

**Wave 2 (close the LLM gap):**
- GLM-5.2 — strongest all-round open model, MIT license, premium general-purpose tier; already "coming soon" on Gonka — execute the launch
- MiniMax M3 — upgrade the M2.7 route to the new flagship (428B/23B, multimodal, open weights since June), pending legal review of the MiniMax Community License (attribution + notification email below $20M/yr, written authorization at/above); watch the single-sourced "M3 Pro" 2.7T Q3-2026 report before locking capacity plans
- Kimi K3 — the moment open weights land (committed for July 27, 2026, expected Modified MIT), be among the first networks to serve it (plan for MXFP4, ~64+ accelerators per Moonshot)

**Wave 3 (open the media front):**
- FLUX.2 dev — massive creative community, high GPU hours per user (re-check vs OpenMDW-licensed Cosmos3)
- Wan 2.7 — highest compute per request; Apache-2.0 artifacts confirmed on Hugging Face and ModelScope (Together AI already serves it); keep Wan 2.2 as the budget tier

### Key Insight

**FLUX.2 and Wan** generate the most GPU hours per user (image/video workloads are compute-hungry). **Kimi, GLM, and MiniMax** bring the highest volume of users (agentic coding is the dominant LLM workload of 2026), with MiniMax's small-active-params architecture (10B in M2.x, 23B in M3) delivering the best serve economics for a distributed network. A balanced portfolio across both categories maximizes network utilization — and serving K3 weights within days of release is the highest-leverage demand event available in 2026.

### Competitive Context

Chinese open-weight labs (Moonshot, Zhipu, MiniMax, DeepSeek, Alibaba/Qwen) still lead the open leaderboards, and Meta has exited frontier open weights — but "Meta exited = the US exited" is no longer accurate. Two significant US open-weight releases landed mid-2026: NVIDIA Nemotron 3 Ultra (June 4: 550B/55B hybrid Mamba-Attention MoE, 1M context) and Thinking Machines' Inkling (July 15: 975B/41B multimodal MoE, Apache 2.0, 1M context), now the leading US open-weights model per Artificial Analysis. Both are candidate serve targets — Apache-2.0 Inkling especially, versus Modified-MIT Chinese models.

On the decentralized-compute side, AkashML has moved fast: as of July 2026 it publishes a full public model catalog with transparent per-model pricing (including Kimi K2.6 and DeepSeek V3.2), offers $100 free credits to new accounts, claims ~65 datacenters with sub-200ms global latency, grew from ~5B tokens/day (May 2026) to 10B+ tokens/day (early July), counts Venice and ElizaOS as named production users, and shipped "Akash Agents," a crypto-abstracted agent-deployment layer. A decentralized competitor now serves the same Kimi generation as Gonka's flagship — model breadth and rotation speed, not exclusivity, are the moat. Its early-2026 most-requested models (Llama 3.3-70B, DeepSeek V3, Qwen3-30B-A3B) have all since been superseded, underscoring how fast serving lineups must rotate. Strong image and video generation offerings remain notably absent from decentralized networks — a gap Gonka can exploit with FLUX.2 and Wan.

---

## Sources

- [Kimi K2.7-Code — Hugging Face](https://huggingface.co/moonshotai/Kimi-K2.7-Code)
- [Kimi K3 — Simon Willison](https://simonwillison.net/2026/Jul/16/kimi-k3/)
- [Moonshot AI releases Kimi K3 — CNBC](https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html)
- [Kimi platform model lifecycle — Moonshot docs](https://platform.kimi.ai/docs/models)
- [Kimi K2.6 pricing and deployment — DeepInfra](https://deepinfra.com/blog/kimi-k2-6-pricing-guide-deployment-tradeoffs)
- [GLM-5.2 release — DataNorth](https://datanorth.ai/news/zhipu-ai-releases-glm-5-2)
- [GLM-5.2 benchmark deep dive — kie.ai](https://kie.ai/blog/glm-5-2-benchmark-deep-dive)
- [Kimi K3 achieves #3 on the Intelligence Index — Artificial Analysis](https://artificialanalysis.ai/articles/kimi-k3-achieves-3-in-the-artificial-analysis-intelligence-index-comparable-to-opus-4-8-and-gpt-5-5)
- [MiniMax M3 — MiniMax blog](https://www.minimax.io/blog/minimax-m3)
- [MiniMax-M3 — Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M3)
- [MiniMax M2.5 — Hugging Face blog](https://huggingface.co/blog/mlabonne/minimax-m25)
- [MiniMax M2.7 open-sourced — MarkTechPost](https://www.marktechpost.com/2026/04/12/minimax-just-open-sourced-minimax-m2-7-a-self-evolving-agent-model-that-scores-56-22-on-swe-pro-and-57-0-on-terminal-bench-2/)
- [MiniMax M3 Community License — Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/LICENSE)
- [MiniMax plans 2.7T-parameter "M3 Pro" — The Information](https://www.theinformation.com/briefings/exclusive-chinas-minimax-plans-launch-2-7-trillion-parameter-model)
- [DeepSeek V4 preview release — DeepSeek API news](https://api-docs.deepseek.com/news/news260424/)
- [DeepSeek V4 mid-July launch with peak-time API pricing — TechNode](https://technode.com/2026/06/30/deepseek-to-launch-v4-in-mid-july-with-new-peak-time-api-pricing/)
- [Qwen3.6 — GitHub](https://github.com/QwenLM/Qwen3.6)
- [Mistral 3 — Mistral AI](https://mistral.ai/news/mistral-3/)
- [Introducing Inkling — Thinking Machines Lab](https://thinkingmachines.ai/news/introducing-inkling/)
- [Inkling: the new leading US open-weights model — Artificial Analysis](https://artificialanalysis.ai/articles/thinking-machines-has-released-inkling-the-new-leading-u-s-open-weights-model)
- [Llama (language model) — Wikipedia](https://en.wikipedia.org/wiki/Llama_(language_model))
- [Best open-source video models 2026 — WaveSpeed](https://wavespeed.ai/landing/models/best-open-source-video-models-2026)
- [Wan 2.7 thinking mode — Tellers](https://tellers.ai/blog/wan_2_7_thinking_mode_ai_video_generation_2026-04-15)
- [Wan2GP — GitHub](https://github.com/deepbeepmeep/Wan2GP)
- [HunyuanVideo 1.5 — GitHub](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5)
- [FLUX vs Stable Diffusion 2026 — PXZ](https://pxz.ai/blog/flux-vs-stable-diffusion:-technical-&-real-world-comparison-2026)
- [DeepSeek V4 Pro — Hokai model hub](https://hokai.io/hub/models/deepseek-v4-pro)
- [Open-weight models that matter, June 2026 — OpenRouter](https://openrouter.ai/blog/insights/the-open-weight-models-that-matter-june-2026/)
- [MiniMax M3 pricing — MiniMax](https://minimax-ai.chat/models/minimax-m3/)
- [MiniMax M3 license and benchmark caveats — TechTimes](https://www.techtimes.com/articles/317532/20260601/minimax-m3-open-weight-coding-model-frontier-claims-unverified-benchmarks.htm)
- [Kimi K3 2.8T-A50B — Latent Space](https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest)
- [Kimi K3 open weights July 27 — kimi-k2.org](https://kimi-k2.org/blog/31-kimi-k3-open-weights-july-27)
- [Qwen 3.7 Max launch guide — Codersera](https://codersera.com/blog/qwen-3-7-max-launch-guide-2026/)
- [Kimi K2.6 — Artificial Analysis](https://artificialanalysis.ai/models/kimi-k2-6)
- [GLM-5.2 — LLM Stats](https://llm-stats.com/models/glm-5.2)
- [Nemotron 3 Ultra release — MarkTechPost](https://www.marktechpost.com/2026/06/04/nvidia-ai-releases-nemotron-3-ultra-an-open-550b-mixture-of-experts-hybrid-mamba-transformer-for-long-running-agents/)
- [Cosmos3-Super-Text2Image — Hugging Face](https://huggingface.co/nvidia/Cosmos3-Super-Text2Image)
- [Text-to-Image Arena leaderboard — Artificial Analysis](https://artificialanalysis.ai/image/leaderboard/text-to-image)
- [Wan 2.7 open-source guide — wan27.org](https://wan27.org/blog/wan-2-7-open-source-guide)
- [Wan 2.7 Hugging Face guide — wan27.org](https://wan27.org/blog/wan-2-7-huggingface-guide)
- [Wan 2.7 — Together AI](https://www.together.ai/models/wan-27)
- [GLM-5.2 pricing — Z.ai docs](https://docs.z.ai/guides/overview/pricing)
- [GLM-5.2 — OpenRouter](https://openrouter.ai/z-ai/glm-5.2)
- [AkashML model catalog](https://akashml.com/models)
- [Gonka blog](https://blog.gonkahub.com/)
- [Gonka24 rate cards](https://gonka24.com/)
- [Gonka endpoints — PricePerToken](https://pricepertoken.com/endpoints/gonka)
- [Gonka releases — GitHub](https://github.com/gonka-ai/gonka/releases)
- [Best Open Source TTS 2026 — BentoML](https://www.bentoml.com/blog/exploring-the-world-of-open-source-text-to-speech-models)
- [LLM release timeline — llm-stats](https://llm-stats.com/llm-updates)

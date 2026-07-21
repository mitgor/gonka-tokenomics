# Strategy: Kimi K-Series Integration + Agent Inference for Gonka.ai

**Date:** 2026-07-18 (originally drafted 2026-02-13 around Kimi K2.5; re-baselined to the July 2026 model landscape)
**Status:** Research & Strategy
**Depends on:** Gonka.ai platform infrastructure (separate from this tokenomics repo)

---

## Part 1: Kimi K-Series Integration Strategy

### Where the K-Series Stands (July 2026)

This strategy was originally built around Kimi K2.5 (released January 27, 2026). K2.5 has since been superseded twice, and Moonshot's own lineup has moved fast:

| Model | Released | Key specs | Status |
|-------|----------|-----------|--------|
| Kimi K2.5 | Jan 27, 2026 | 1T MoE, 262K context, multimodal, Modified MIT | Being sunset: closed to newly registered users since the K3 launch (Jul 16), API traffic redirected to K2.6, full platform sunset Aug 31, 2026. Older kimi-k2 series API models were already discontinued May 25, 2026. Third-party hosts (OpenRouter $0.375/$2.025, DeepInfra $0.45/$2.25) still serve it, with lifecycle risk |
| Kimi K2.6 | Apr 20, 2026 | 1T MoE, 32B active, ~256K context, multimodal; official API $0.95/$4.00 per 1M in/out ($0.16/M cache-hit input) | Moonshot's current workhorse; powers Kimi's paid chat. **On Gonka: mid-re-bootstrap after its second removal in three weeks** — first removed Jun 25 (Proposal 78, lacked validation majority, alongside Qwen3-235B), restored Jun 26 (Proposal 79, weight_scale_factor 0.9) and re-bootstrapped at epoch 311 (Jun 27); then lost validation majority again in epochs 328–329 (concentrated guardian delegations + provider failures), removed via expedited Proposal 87 (Jul 15), re-registered via Proposal 88 (Jul 16) for re-bootstrap at epoch 331, weight factor unchanged at 0.9 |
| Kimi K2.7-Code | Jun 2026 | Coding/agentic post-train on K2.6 base; 1T MoE, 32B active, 256K context, Modified MIT; +21.8% on Kimi Code Bench v2 vs K2.6, ~30% fewer reasoning tokens; API $0.95 in / $0.19 cache-hit / $4.00 out per 1M | Current open-weight coding-agent flagship |
| Kimi K3 | Jul 16, 2026 | 2.8T MoE (896 experts, 16 active/token), Kimi Delta Attention, native vision, up to 1M context, always-on thinking mode; API $3/$15 per 1M ($0.30/M cached input — 90% discount; built-in web search billed $0.015/call); Artificial Analysis Intelligence Index 57.11 — level with Opus 4.8 and GPT-5.5, behind Claude Fable 5 and GPT-5.6 Sol; #1 in Frontend Code Arena (1,679, debut Jul 16) — the first open model to top a frontier arena leaderboard | Announced; API/app only — weights committed for Jul 27, 2026 on Hugging Face, expected under Moonshot's Modified MIT license; largest open-weight model to date |

**Note on the earlier K2.5 pitch:** the original draft claimed a "131K context window" and a Feb-2026 "Quality Index of 46.77" top ranking. K2.5's context is actually 262,144 tokens, and its benchmark standing is no longer leading — the open-weight SWE-bench Verified leaders as of July 2026 are DeepSeek V4 Pro (80.6%, Think Max mode — tied with Gemini 3.1 Pro) and MiniMax M3 (80.5%, vendor-reported), edging MiniMax M2.5's 80.2%; the closed frontier reference is GPT-5.3 Codex at 85%. K2.7-Code remains the top pick for coding agents (its benchmarks are Moonshot-internal only).

### Why the K-Series Still Matters for Gonka.ai

1. **Native agentic capabilities** — The K2.x line is architecturally agentic (swarm-like decomposition into parallel sub-tasks by dynamically instantiated domain agents), and K2.6/K2.7-Code are explicitly agent-swarm and long-horizon-coding focused. This is not bolted-on tool use.

2. **Multimodal** — K2.6 is multimodal; K3 adds native vision with 1M-token context.

3. **OpenAI-compatible API** — Drop-in replacement for existing OpenAI API consumers. Chat completions with full tool calling. Any app using OpenAI's API can switch to a Gonka-hosted K-series model with a base URL change.

4. **Open weights, permissive license** — K2.7-Code ships under a Modified MIT license today; K3 open weights are expected ~July 27, 2026. That makes the K-series self-hostable in a way frontier closed models are not.

**Recommendation:** treat **K2.6 as the workhorse tier** — with the caveat that on Gonka it has now failed validation majority twice in three weeks (removed Jun 25 and Jul 15), so any "cheapest K2.6 provider" or reliability messaging must wait until it is stably re-validated — **K2.7-Code as the coding/agent flagship** (available now), and **K3 as the frontier tier** once weights land. MiniMax M2.7, not K2.6, is Gonka's base model (sole PoC model since Jun 25, 2026). Do not build new GTM material around K2.5: Moonshot has closed it to new users and sunsets it Aug 31, 2026.

### Hardware Requirements

The table below was derived in February 2026 for K2.5. K2.6/K2.7-Code share the same 1T-MoE base, so the figures are a reasonable starting point for those models, but they should be re-derived per model before deployment. **K3 sizing (Jul 2026 specifics):** 2.8T total / ~50B active parameters ("2.8T-A50B"; 16 of 896 experts active ≈ 1.8%), shipped in MXFP4 quantization, with Moonshot recommending at least 64 accelerators for serving. Reference point: the 1T K2.7-Code needs ~577GB VRAM at INT4. A full sizing exercise still needs to happen once weights land (~Jul 27).

| Configuration | Hardware | Performance | Use Case |
|---------------|----------|-------------|----------|
| Full precision (1T-class) | 8x H200 GPUs (141GB each) | Production-grade throughput | Premium tier |
| Production minimum | 4x H200 GPUs | Good throughput | Standard tier |
| Enterprise alternative | 2x H100 80GB or 4x A100 80GB | Adequate for moderate load | Cost-optimized |
| Budget/quantized (1.8-bit) | 1x 24GB GPU + 256GB RAM | ~10 tokens/s | Development/testing only |
| Extreme budget (UD-TQ1_0) | 1x 24GB GPU + 240GB storage | ~1-2 tokens/s | Not viable for production |

**Storage (K2.5 baseline, Feb 2026):** 630GB full model, 240GB for 1.8-bit quantized. Expect similar for K2.6/K2.7-Code; K3 ships in MXFP4, so expect roughly 1.5-2TB-class storage (exact figure TBD at weights release).

**Recommended for Gonka.ai:** 4x H200 per serving instance with vLLM for 1T-class models, scaling horizontally for demand.

### Deployment Architecture

```
                    ┌─────────────────────────────────┐
                    │         Gonka.ai Gateway         │
                    │   (Load Balancer + Auth + Rate   │
                    │    Limiting + Usage Metering)    │
                    └──────────────┬──────────────────┘
                                   │
                    ┌──────────────┴──────────────────┐
                    │        vLLM Serving Layer        │
                    │   moonshotai/Kimi-K2.7-Code      │
                    │   -tp 8                          │
                    │   --tool-call-parser kimi_k2     │
                    │   --reasoning-parser kimi_k2     │
                    └──────────────┬──────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                     │
        ┌─────┴─────┐      ┌─────┴─────┐        ┌─────┴─────┐
        │  GPU Node  │      │  GPU Node  │        │  GPU Node  │
        │  4x H200   │      │  4x H200   │        │  4x H200   │
        │ Instance 1 │      │ Instance 2 │        │ Instance N │
        └────────────┘      └────────────┘        └────────────┘
```

### vLLM Deployment Command

The command below is the Feb-2026 K2.5 recipe, updated to target K2.7-Code with its 256K context. Verify flags against the current vLLM recipe for the exact model before deploying (the `kimi_k2` parsers are in vLLM/sglang mainline; the Feb-2026 "requires v0.15.0+/nightly" caveat no longer applies).

```bash
vllm serve moonshotai/Kimi-K2.7-Code \
  -tp 8 \
  --tool-call-parser kimi_k2 \
  --reasoning-parser kimi_k2 \
  --trust-remote-code \
  --max-model-len 262144 \
  --gpu-memory-utilization 0.92
```

### API Interface

K-series models expose a fully OpenAI-compatible API when served via vLLM:

```
POST /v1/chat/completions
```

Supports:
- Standard chat completions (messages array)
- Tool/function calling (tools parameter)
- Vision/multimodal inputs (image_url in content, on multimodal variants)
- Streaming (stream: true)
- Thinking/reasoning mode (via system prompt or model config)

**This means:** Any application currently using OpenAI, Anthropic, or other LLM APIs can point to Gonka.ai's endpoint with zero code changes beyond updating the base URL and API key.

### Quantized Variants for Tiered Offering

Quant tiers below are the Feb-2026 K2.5 GGUF derivation; sizes should transfer approximately to K2.6/K2.7-Code (same 1T base) but need re-verification per model. K3 tiers TBD after weights release.

| Variant | Size | VRAM Needed | Speed | Quality |
|---------|------|-------------|-------|---------|
| Full (INT4 native) | 630GB | 4x H200 | Fast | Best |
| GGUF Q4_K_XL | ~350GB | 2x H200 + RAM | Good | Near-full |
| GGUF Q2_K_XL | ~200GB | 1x H200 + RAM | Moderate | Good |
| GGUF UD-TQ1_0 (1.8-bit) | 240GB | 1x 24GB + 256GB RAM | Slow (~10 tok/s) | Acceptable |

**Tiered pricing strategy (reframed for July 2026):**
- **Frontier:** K3, once weights land (~Jul 27, 2026) — highest quality, premium pricing
- **Premium:** K2.7-Code full precision — production coding/agent workloads
- **Standard:** K2.6 (re-bootstrapping on Gonka as of Jul 2026) or Q4-quantized K2.7-Code — development and moderate production
- **Budget:** Q2/1.8-bit quants — experimentation and low-throughput use

### Integration Milestones

Gonka completed Phase 1 for K2.6, but K2.6 is currently in its second removal/re-bootstrap cycle (removed Jun 25 and again Jul 15; re-registered Jul 16 for epoch 331); Phase 1 counts as complete only once it holds validation majority again. Remaining milestones apply to K2.7-Code and K3:

**Phase 1: Basic Inference** *(done for K2.6; re-stabilization pending)*
- Deploy on vLLM with OpenAI-compatible API
- Gonka.ai gateway (auth, rate limiting, usage metering)
- `/v1/chat/completions` with text chat and tool calling

**Phase 2: K2.7-Code Tier**
- Deploy K2.7-Code as the coding-agent flagship
- Multimodal inputs on K2.6 (vision, image preprocessing pipeline)

**Phase 3: Agentic**
- Enable native swarm execution mode
- Multi-step tool call chains, agent session persistence
- Agentic API endpoints

**Phase 4: K3 + Scale**
- Size and deploy K3 when open weights land (2.8T-A50B, MXFP4, Moonshot recommends ≥64 accelerators)
- Horizontal scaling with load balancing, auto-scaling on queue depth
- Geographic distribution for latency optimization

### Competitive Positioning

The original "first decentralized network to serve K2.5" positioning is dead: **AkashML now serves Kimi K2.6** (1T MoE, 256K context) at $0.95/M input and $4.00/M output — matching Moonshot's official K2.6 API price. AkashML is no longer a poorly-documented also-ran: as of July 2026 it publishes a full public model catalog with per-model pricing (including K2.6 and DeepSeek V3.2), offers $100 free credits, claims ~65 datacenters with sub-200ms global latency, grew from ~5B tokens/day (May 2026) to 10B+ tokens/day (early July), counts Venice and ElizaOS as production users, and has shipped **"Akash Agents"** — a crypto-abstracted agent-deployment layer. The predicted encroachment on agent features has begun. Credible July-2026 differentiation levers:

- **K2.7-Code and (soon) K3** — being early on the *current* generation, not K2.5
- **Price** — undercutting the $0.95/$4.00 K2.6 rate that both Moonshot and AkashML charge. One caution on the "prices only fall" assumption: frontier open-weight pricing is now rising (K3's $3/$15 is ~3x K2.6's $0.95/$4.00), and DeepSeek's official V4 (mid-July 2026) introduces China's first time-of-day API pricing — rates double during Beijing peak hours (9:00–12:00, 14:00–18:00). Flat, predictable pricing is itself now a positioning lever for Gonka against 24/7 agent workloads
- **Agent extensions** (Part 2, Option C) — session persistence, memory API, model tiering. Akash Agents means this is no longer uncontested; Gonka must ship, not just plan
- **Multi-model breadth** — narrowed but not gone as of July 2026: Qwen3-235B was retired from the network Jun 25, 2026 (Proposal 78), MiniMax M2.7 is the sole PoC/base model, **GLM-5.2-FP8 is live** (added via Proposal 79, Jun 26, weight factor 2.47), and K2.6 is re-bootstrapping. The "~100M tokens/day across ~5 inference models" figure is a pre-retirement (spring 2026) estimate, not re-verified

Target audiences remain valid: developers who can't run 4-8x H200 locally, Asian-market developers familiar with MoonshotAI, agent builders, and multimodal application builders.

---

## Part 2: Agent Inference Research — Can Gonka Run Model + Agent?

### The Opportunity

2026 is defined by the shift from "model inference" (stateless request/response) to "agent inference" (stateful, continuous, multi-step execution). This represents a fundamental infrastructure upgrade:

| Dimension | Model Inference | Agent Inference |
|-----------|----------------|-----------------|
| Request pattern | Single request → single response | Multi-step chains, tool calls, loops |
| State | Stateless | Stateful (conversation, memory, context) |
| Duration | Seconds | Minutes to hours (always-on agents) |
| GPU utilization | Burst | Sustained |
| Token volume | Thousands per request | Millions per session |
| Revenue model | Per-token or per-request | Per-session or subscription |

**Key stats (per the OpenRouter/a16z "State of AI" 100-trillion-token study, published ~Dec 2025 covering usage through late 2025):** open-weight models reached ~33% of total OpenRouter token volume; Chinese open models peaked near ~30% of usage in some weeks (up from a 1.2% base); and **agentic inference is the study's fastest-growing usage behavior**. 67% of enterprises consume >1B tokens/month (Deloitte 2026). (Unverified figures dropped from earlier drafts: ">half of all output tokens are agentic," "~61% Chinese open-source share," "~28T tokens/week," and "China processes ~140T tokens/day" are not supported by the cited study; the "inference at 55% of AI infra spend, headed to 70-80%" framing also remains an early-2026 estimate, not re-verified.)

### OpenClaw: Case Study for Agent + Inference

**What it is:** OpenClaw (formerly Clawdbot/Moltbot) was the breakout AI agent repository of early 2026 — 145,000+ GitHub stars as of February 2026. It's a self-hosted, open-source autonomous AI agent that connects to messaging platforms (WhatsApp, Telegram, Slack, Discord, iMessage, etc.) and executes tasks via LLMs.

**Architecture:**

```
┌──────────────────────────────────────────────────┐
│                   OpenClaw                        │
│                                                   │
│  ┌────────────┐  ┌──────────────┐  ┌───────────┐│
│  │  Channels   │  │ Agent Runner │  │   Tools   ││
│  │ (Telegram,  │→ │ (Lane Queue, │→ │ (Shell,   ││
│  │  Slack,     │  │  Model       │  │  Browser, ││
│  │  Discord)   │  │  Resolver)   │  │  Files)   ││
│  └────────────┘  └──────┬───────┘  └───────────┘│
│                          │                        │
│                   ┌──────┴───────┐                │
│                   │ LLM Backend  │                │
│                   │ (Cloud API   │                │
│                   │  OR Ollama/  │                │
│                   │  Local GPU)  │                │
│                   └──────────────┘                │
└──────────────────────────────────────────────────┘
```

**Key architectural features:**
- **Lane Queue system** — Serial execution by default to prevent race conditions
- **Semantic Snapshots** — Parses accessibility trees instead of screenshots (reduces token cost)
- **Model Resolver** — Auto-failover between providers; model tiering (cheap for classification, strong for reasoning)
- **Plugin system** — Channels, tools, providers, memory are all pluggable
- **Local-first** — All data stored as Markdown/YAML on-device, Git-backupable

**How OpenClaw uses inference:**
- Message arrives via channel → Agent Runner classifies intent (cheap model)
- Complex tasks → Stronger model for multi-step planning
- Tool execution → Shell/browser/file operations on local machine
- Results → Formatted and sent back through channel
- Memory → Long-term context stored as Markdown files

**OpenClaw + Ollama integration is already documented and works.** Users can point OpenClaw at any OpenAI-compatible endpoint — including a Gonka.ai-hosted model.

### How Gonka.ai Could Serve Agent Inference

#### Option A: Model-Only Backend (Simpler)

Gonka.ai serves only the LLM inference. Agents (OpenClaw, CrewAI, LangGraph, etc.) run on the user's machine or server and call Gonka.ai as their model backend.

```
User's Machine                    Gonka.ai
┌──────────────┐                 ┌──────────────────┐
│  OpenClaw    │ ── HTTP API ──→ │  Kimi K2.7-Code  │
│  (agent)     │ ←── response ── │  (vLLM)          │
│              │                 │                   │
│  CrewAI      │ ── HTTP API ──→ │  MiniMax M2.7    │
│  (agent)     │ ←── response ── │  (vLLM)          │
└──────────────┘                 └──────────────────┘
```

**Pros:** Simplest to build. OpenAI-compatible API is all you need. Every agent framework already supports this.
**Cons:** Users must run agent infrastructure themselves. No recurring "always-on" revenue.

#### Option B: Full Agent Hosting (Ambitious)

Gonka.ai runs both the agent runtime AND the model inference. Users deploy their agents to Gonka.ai.

```
Gonka.ai Platform
┌─────────────────────────────────────────────────────┐
│                                                      │
│  ┌──────────────────┐    ┌────────────────────────┐ │
│  │  Agent Runtime    │    │  Model Inference       │ │
│  │  ┌────────────┐  │    │  ┌──────────────────┐  │ │
│  │  │ OpenClaw   │──│────│─→│  Kimi K2.7-Code  │  │ │
│  │  │ Instance 1 │  │    │  │  (local network) │  │ │
│  │  └────────────┘  │    │  └──────────────────┘  │ │
│  │  ┌────────────┐  │    │  ┌──────────────────┐  │ │
│  │  │ CrewAI     │──│────│─→│  MiniMax M2.7    │  │ │
│  │  │ Instance 2 │  │    │  │  (local network) │  │ │
│  │  └────────────┘  │    │  └──────────────────┘  │ │
│  └──────────────────┘    └────────────────────────┘ │
│                                                      │
│  ┌──────────────────────────────────────────────┐   │
│  │  Shared Services                              │   │
│  │  (Memory store, tool sandbox, monitoring)     │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

**Pros:** Much higher revenue per user (agent + inference). Enables always-on agents (24/7 GPU usage). Massive stickiness — users won't easily migrate running agents.
**Cons:** Significantly more complex. Security concerns (running user code). Container orchestration overhead.

#### Option C: Hybrid — Agent-Aware Inference (Recommended)

Gonka.ai primarily serves inference but adds agent-specific features that make it the preferred backend for agent frameworks:

```
Gonka.ai
┌───────────────────────────────────────────────────┐
│  Standard Inference (OpenAI-compatible)            │
│  + Agent Extensions:                               │
│    • Session persistence (conversation state)      │
│    • Memory API (long-term context storage)        │
│    • Tool result caching                           │
│    • Model tiering (auto-route cheap vs strong)    │
│    • Webhook callbacks for async tool execution    │
│    • Usage dashboards per agent session            │
└───────────────────────────────────────────────────┘
```

**Pros:** Builds on Option A (simple base) but adds value that generic inference providers don't offer. Differentiates from Akash/Render/io.net. Creates stickiness without running user code.
**Cons:** Requires designing agent-aware API extensions beyond OpenAI spec.

### Agent Framework Compatibility Matrix

| Framework | GitHub Stars | Local Inference Support | OpenAI-Compatible | Gonka.ai Fit |
|-----------|-------------|------------------------|-------------------|-------------|
| OpenClaw | 145,000+ (Feb 2026) | Yes (Ollama) | Yes | Excellent — point at Gonka endpoint |
| LangGraph | Large ecosystem | Yes (any LLM) | Yes | Excellent — standard LangChain integration |
| CrewAI | Major framework | Yes (Ollama, local) | Yes | Excellent — multi-agent, high token usage |
| AutoGen | Microsoft-backed | Yes (local models) | Yes | Good — async agent conversations |
| Haystack | Growing | Yes | Yes | Good — RAG + agent pipelines |

**Key insight:** All major agent frameworks support OpenAI-compatible endpoints. Any model Gonka.ai serves via vLLM's OpenAI-compatible API is automatically compatible with every framework above.

### Economics of Agent Inference for Gonka.ai

| Metric | Model-Only Inference | Agent-Aware Inference |
|--------|---------------------|-----------------------|
| Avg session duration | Seconds | Minutes to hours |
| Tokens per session | 1K-10K | 100K-1M+ |
| GPU utilization pattern | Bursty | Sustained |
| Revenue per user/month | $5-50 | $50-500+ |
| Churn risk | High (commodity) | Low (workflow lock-in) |
| Competitive moat | Low | Medium-High |

**The always-on agent opportunity:** Companies are seeing monthly AI bills of tens of millions. Decentralized networks offer 50-60% cost savings (early-2026 estimate). If Gonka.ai captures even a fraction of the agent inference market, the GPU utilization and revenue per node would be dramatically higher than serving stateless chat completions.

**Serving-economics note (July 2026):** for agent workloads on a distributed GPU network, MiniMax models are dramatically cheaper to serve than 1T-param K-series models thanks to small active-parameter counts: M2.5 is 230B MoE / 10B active (80.2% SWE-bench Verified — no longer the open-weight leader; see Part 1), and open-weight M2.7 (released Mar 18, 2026, open-sourced ~Apr 12) is not just live on Gonka — since June 25, 2026 (Proposal 78) it is the network's **sole PoC model and base delegation target**. **MiniMax M3 (June 1, 2026; open weights ~Jun 7) now supersedes M2.x as the MiniMax flagship:** 428B total / 23B active MoE with MiniMax Sparse Attention, 1M-token context, native multimodality (image + video input), thinking + non-thinking modes, 80.5% SWE-bench Verified and 59.0% SWE-Bench Pro (both vendor-reported). Official first-party pricing: $0.30/$1.20 per 1M for inputs up to 512K tokens, **$0.60/$2.40 above 512K** — use the higher tier when modeling 1M-context agent workloads — and MiniMax labels displayed rates as a permanent 50% discount off struck-through list prices.

**M-series roadmap watch (mid-July 2026):** The Information reports MiniMax is preparing **"M3 Pro," a 2.7-trillion-parameter model** — ~6x M3's total size and rivaling Kimi K3's 2.8T — with a planned open-source release as early as Q3 2026. This is single-sourced (two people familiar); active-parameter count and license terms are unannounced. If real, it undercuts both the "MiniMax = small-active-params margin engine" framing above and K3's "largest open-weight model" positioning — but until active params and license are known, it changes no serving decision.

**M3 license caveat (flag before committing GPU capacity):** M3 ships under the **MiniMax Community License**, not MIT/Apache. Per the LICENSE file on Hugging Face: commercial use requires prominent "Built with MiniMax M3" attribution (website/UI/docs); organizations below $20M/year revenue must send a one-time commercial-use notification email to api@minimax.io; at or above $20M/year, separate prior written authorization from MiniMax is required. There is **no notification-free commercial tier at all**. For a commercial decentralized hosting network this is materially more restrictive than the MIT (GLM-5.2, DeepSeek V4), Apache 2.0 (Qwen 3.5/3.6, Inkling, Mistral 3), or Modified-MIT (Kimi) alternatives. The agent-inference tiering should route by cost: MiniMax (M2.7 today, M3 as upgrade target *pending license review*) for high-volume agent loops, K2.7-Code for hard coding tasks, K3 for frontier reasoning — with DeepSeek V4 Pro (MIT, 80.6% Verified) as the license-clean alternative to M3.

### Recommended Strategy

1. **Launch with Option A** (model-only, OpenAI-compatible) — covers 100% of agent frameworks immediately *(effectively done: MiniMax M2.7 is live as the sole PoC/base model; GLM-5.2 is live since late June; K2.6 is re-bootstrapping; Qwen was retired Jun 25, 2026)*
2. **Add agent-aware extensions** (Option C) as differentiation — session persistence, memory API, model tiering
3. **Evaluate Option B** (full agent hosting) based on demand signals — only if users actively request it
4. **Flagship models:** K2.7-Code today for coding agents, K3 when weights land (~Jul 27, 2026); MiniMax as the cost-efficient agent workhorse and Gonka base model (M2.7 is the sole PoC model now, M3 the upgrade target pending Community License review; DeepSeek V4 Pro is the MIT fallback). Retire all K2.5-flagship messaging (Moonshot sunsets K2.5 Aug 31, 2026), and hold Kimi-reliability claims until K2.6's re-bootstrap stabilizes — it has failed validation majority twice in three weeks.

---

## Part 3: Competitive Landscape

### What Competitors Offer (July 2026)

| Network | Models Served | Agent Support | Differentiator |
|---------|---------------|---------------|----------------|
| Akash / AkashML | Public catalog incl. Llama, DeepSeek V3.2, Qwen, **Kimi K2.6** ($0.95/$4.00 per 1M) | **Akash Agents** (crypto-abstracted agent deployment) | Kubernetes-native; ~65 datacenters, 10B+ tokens/day (Jul 2026), Venice + ElizaOS in production |
| Render | GPU rental (not model-specific) | None | Raw GPU access |
| io.net | Various | None | GPU aggregation |
| DecentralGPT | Open models | Verifiable compute | Proof-based inference |
| **Gonka.ai** | **Three governance-approved active models: MiniMax M2.7 (sole PoC/base model since Jun 25, 2026), GLM-5.2-FP8 (weight factor 2.47, live since Proposal 79, Jun 26), Kimi K2.6 (re-bootstrapping since Jul 16). Qwen3-235B retired Jun 25 (Proposal 78)** | **Agent-aware inference (planned)** | **Agent extensions + price** |

### Gonka.ai's Differentiation Levers

The original "first-to-market with K2.5" moat no longer exists (AkashML serves K2.6; Moonshot discontinued older kimi-k2 API models in May 2026). Current levers:

1. **Current-generation Kimi** — Be early on K2.7-Code serving and K3 weights (Jul 27, 2026, expected Modified MIT), not a superseded model — while being honest that Gonka's K2.6 deployment has gone through two removal/re-registration cycles (Jun 25–27 and Jul 15–16) and needs to prove stability first
2. **Agent-aware inference** — Session persistence, memory, tiering. Akash has shipped "Akash Agents" (agent deployment), so this lever is now contested; Gonka's differentiation must come from inference-side extensions (session state, memory API, cost-routing) rather than being first
3. **Multi-model, cost-routed coverage** — currently three active models: MiniMax M2.7 (base), GLM-5.2-FP8 (live), and re-bootstrapping K2.6; extend breadth by adding K2.7-Code, and evaluate as serve targets:
   - **MiniMax M3** (428B/23B-active, 1M context, multimodal) — see serving-economics note, the rumored 2.7T "M3 Pro" (Q3 2026, license unannounced), and **MiniMax Community License caveat** in Part 2
   - **GLM-5.2** (already live on Gonka since Proposal 79; announced Jun 13, 2026, weights Jun 16; 744B MoE per eigent.ai — LLM Stats lists 753B, discrepancy unresolved; 1M context, 131K output, MIT license; API $1.40/$4.40 per 1M direct from Z.ai ($0.26 cached) or $1.00/$4.00 via OpenRouter; strongest all-round open-weight model per Artificial Analysis Intelligence Index v4.1 ~51; independent SWE-bench Pro 62.1 vs GPT-5.5's 58.6 — GLM-5.2 shipped no official benchmarks, so treat secondary-blog figures as unverified)
   - **DeepSeek V4** (Apr 24, 2026 was the *Preview*; official release announced Jun 30 for mid-July 2026. V4-Pro 1.6T/49B-active, MIT, 1M context, **80.6% SWE-bench Verified in Think Max mode — the open-weight leader, tied with Gemini 3.1 Pro**, ~55% SWE-bench Pro; V4-Flash 284B/13B. **Pricing is now time-of-day**: China's first peak-hour API pricing doubles rates during Beijing business hours (9:00–12:00, 14:00–18:00) — V4-Pro ≈$0.42/$0.84 per 1M off-peak, ≈$0.84/$1.68 peak (¥3.00/¥6.00 regular, ¥0.025 cache-hit); V4-Flash ¥1.00/¥2.00 regular. Legacy deepseek-chat/deepseek-reasoner endpoints retire after Jul 24, 2026 — forced migration. Any 24/7 agent cost model using the old flat $0.435/$0.87 rate understates peak-hour cost by up to 2x; conversely, Gonka's flat pricing is a "no rush-hour surcharge" positioning lever)
   - **US open-weight resurgence:** Thinking Machines' **Inkling** (Jul 15, 2026; 975B/41B-active multimodal MoE, Apache 2.0, 1M context, controllable thinking effort — now the leading US open-weights model per Artificial Analysis) and **NVIDIA Nemotron 3 Ultra** (Jun 4, 2026; 550B/55B-active hybrid Mamba-Attention MoE, 1M context). Chinese labs still lead open weights overall, but "US labs have exited open weights" is no longer true — Apache-2.0 Inkling is an especially clean fit for a decentralized network
   - **Qwen watch item:** Alibaba's flagship **Qwen3.7 Max** (May 20, 2026) is closed — DashScope-API-only, 1M context, reasoning-native, $2.50/$7.50 per 1M with 90% cache discount, the first closed Qwen flagship — but smaller **open-weight Qwen 3.7 variants are expected Jun–Jul 2026** on the 3.6 cadence, i.e. potentially imminent. Relevant if Gonka wants to re-add a Qwen tier after the Jun 25 retirement; track alongside K3 weights (Jul 27) and the Mistral early-access model
4. **Price** — Undercut the $0.95/$4.00 K2.6 rate set by Moonshot and AkashML
5. **GNK token economics** — Staking, fee discounts, host incentives from tokenomics research

---

## Sources

Original (Feb 2026):

- [Kimi K2.5 Deployment Guide — GitHub](https://github.com/MoonshotAI/Kimi-K2.5/blob/master/docs/deploy_guidance.md)
- [Kimi K2.5 vLLM Recipe](https://docs.vllm.ai/projects/recipes/en/latest/moonshotai/Kimi-K2.5.html)
- [Kimi K2.5 Run Locally — Unsloth](https://unsloth.ai/docs/models/kimi-k2.5)
- [Kimi K2.5 Hardware Requirements — APXML](https://apxml.com/posts/gpu-system-requirements-kimi-llm)
- [OpenClaw — GitHub](https://github.com/openclaw/openclaw)
- [OpenClaw Architecture — Vertu](https://vertu.com/ai-tools/openclaw-clawdbot-architecture-engineering-reliable-and-controllable-ai-agents/)
- [OpenClaw + Ollama Tutorial — DataCamp](https://www.datacamp.com/tutorial/openclaw-ollama-tutorial)
- [AI Infrastructure Shifts 2026 — Unified AI Hub](https://www.unifiedaihub.com/blog/ai-infrastructure-shifts-in-2026-from-training-to-continuous-inference)
- [AI Inference Defines 2026 — VAST Data](https://www.vastdata.com/blog/2026-the-year-of-ai-inference)
- [Deloitte AI Infrastructure Report](https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/ai-infrastructure-compute-strategy.html)
- [Top AI Agent Frameworks 2026 — Lindy](https://www.lindy.ai/blog/best-ai-agent-frameworks)
- [AkashML Managed AI Inference](https://akash.network/blog/akashml-managed-ai-inference-on-the-decentralized-supercloud/)

July 2026 re-baseline:

- [Moonshot AI releases Kimi K3 — CNBC](https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html)
- [Kimi K3 — Simon Willison](https://simonwillison.net/2026/Jul/16/kimi-k3/)
- [Kimi K2.7-Code — Hugging Face](https://huggingface.co/moonshotai/Kimi-K2.7-Code)
- [Kimi K2.7-Code release — MarkTechPost](https://www.marktechpost.com/2026/06/12/moonshot-ai-releases-kimi-k2-7-code-a-coding-model-reporting-21-8-on-kimi-code-bench-v2-over-k2-6/)
- [Kimi K2.6 — Hugging Face](https://huggingface.co/moonshotai/Kimi-K2.6)
- [Kimi K2.6 pricing guide — DeepInfra](https://deepinfra.com/blog/kimi-k2-6-pricing-guide-deployment-tradeoffs)
- [Moonshot platform model lifecycle](https://platform.kimi.ai/docs/models)
- [AkashML Kimi K2.6](https://akashml.com/models/kimi-k2.6)
- [Gonka endpoints — PricePerToken](https://pricepertoken.com/endpoints/gonka)
- [MiniMax M2.5 — Hugging Face blog](https://huggingface.co/blog/mlabonne/minimax-m25)
- [MiniMax M2.7 open-sourced — MarkTechPost](https://www.marktechpost.com/2026/04/12/minimax-just-open-sourced-minimax-m2-7-a-self-evolving-agent-model-that-scores-56-22-on-swe-pro-and-57-0-on-terminal-bench-2/)
- [Kimi K3 #3 on Intelligence Index — Artificial Analysis](https://artificialanalysis.ai/articles/kimi-k3-achieves-3-in-the-artificial-analysis-intelligence-index-comparable-to-opus-4-8-and-gpt-5-5)
- [MiniMax M3 announcement](https://www.minimax.io/blog/minimax-m3)
- [MiniMax-M3 — Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M3)
- [GLM-5.2 release — DataNorth](https://datanorth.ai/news/zhipu-ai-releases-glm-5-2)
- [DeepSeek V4 — API docs news](https://api-docs.deepseek.com/news/news260424/)
- [Introducing Inkling — Thinking Machines Lab](https://thinkingmachines.ai/news/introducing-inkling/)
- [Inkling: leading US open-weights model — Artificial Analysis](https://artificialanalysis.ai/articles/thinking-machines-has-released-inkling-the-new-leading-u-s-open-weights-model)
- [Open-weight coding leaderboard — BenchLM](https://benchlm.ai/coding)
- [DeepSeek V4 Pro — Hokai model hub](https://hokai.io/hub/models/deepseek-v4-pro)
- [Open-weight models that matter, June 2026 — OpenRouter](https://openrouter.ai/blog/insights/the-open-weight-models-that-matter-june-2026/)
- [MiniMax M3 official pricing](https://minimax-ai.chat/models/minimax-m3/)
- [MiniMax M3 license and benchmark caveats — TechTimes](https://www.techtimes.com/articles/317532/20260601/minimax-m3-open-weight-coding-model-frontier-claims-unverified-benchmarks.htm)
- [Kimi K3: 2.8T-A50B — Latent Space](https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest)
- [Kimi K3 MXFP4 overview — Hugging Face blog](https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei)
- [K3 signals the end of super-cheap Chinese AI — The Decoder](https://the-decoder.com/kimis-open-model-k3-nears-gpt-5-6-sol-and-fable-5-while-signaling-the-end-of-super-cheap-chinese-ai/)
- [GLM-5.2 — eigent.ai](https://www.eigent.ai/blog/glm-5-2) / [LLM Stats](https://llm-stats.com/models/glm-5.2)
- [AkashML models catalog](https://akashml.com/models)
- [OpenRouter State of AI](https://openrouter.ai/state-of-ai) / [a16z State of AI](https://a16z.com/state-of-ai/)
- [Gonka network updates (Proposals 78, 79, 87, 88)](https://gonka.ai/docs/network-updates/)
- [DeepSeek V4 mid-July launch, peak-time API pricing — TechNode](https://technode.com/2026/06/30/deepseek-to-launch-v4-in-mid-july-with-new-peak-time-api-pricing/)
- [Kimi K3 open weights July 27](https://kimi-k2.org/blog/31-kimi-k3-open-weights-july-27)
- [Moonshot API pricing — BenchLM](https://benchlm.ai/moonshot/api-pricing)
- [Qwen 3.7 Max launch guide — Codersera](https://codersera.com/blog/qwen-3-7-max-launch-guide-2026/)
- [Qwen open weights vs closed frontier — InsiderLLM](https://insiderllm.com/guides/qwen-open-weights-vs-closed-frontier-2026/)
- [MiniMax "M3 Pro" 2.7T report — The Information](https://www.theinformation.com/briefings/exclusive-chinas-minimax-plans-launch-2-7-trillion-parameter-model)
- [MiniMax M3 Community License — Hugging Face](https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/LICENSE)

**Source-hygiene note:** several SEO sites (e.g. ragyfied.com, shiporskip.io) publish detailed but fabricated "Meta released Llama 5" articles. No Llama 5 exists: Meta's April 2026 release was the closed-weight Muse Spark, and Llama 4 Scout/Maverick (Apr 2025) remain its last open models. Treat web roundups accordingly when refreshing this doc.

# Gonka Competitive Feature Matrix: Agent-Relevant Inference Provider Comparison

**Version:** 2.2
**Date:** 2026-07-18
**Audience:** Gonka leadership and GTM strategy team
**Scope:** Comparison of Gonka vs OpenRouter vs OpenAI vs Anthropic vs Together AI across 8 agent-relevant dimensions

---

## Executive Summary

OpenClaw developers building AI agents need inference providers that go beyond simple chat completions. Agentic workflows consume 5-30x the tokens of chatbot usage (Gartner, March 2026), resend full context via heartbeats every 30 minutes, and increasingly require server-side state management, automatic model routing, and persistent memory. When evaluated against these agent-specific requirements, no single provider dominates across all dimensions.

The competitive picture has shifted materially since the v1.0 (April 2026) edition of this matrix. Gonka's two headline differentiators have both been eroded: OpenAI's Responses + Conversations API now provides server-side stateful conversations on its primary API surface, and cost-based model routing has been commoditized by client-side routers (ClawRouter and peers) that ship with or alongside OpenClaw. Prompt caching is now effectively universal across the compared landscape. Meanwhile Gonka's position has improved in two ways: pricing is live and is currently the cheapest listed rate for its served models, and the network serves two model families (Kimi K2.6 and MiniMax M2.7) at ~100M tokens/day -- with GLM-5.2 approved as a third via Proposal 79 (June 26, 2026) though its rollout is incomplete -- up from the single-model K2.5 plan. Two caveats temper this: Proposal 78 (June 25, 2026) removed both Qwen3-235B (permanently; MiniMax M2.7 became sole PoC model and base delegation target) and Kimi K2.6 for lacking validation majority; Kimi was restored the next day by Proposal 79 at weight_scale_factor 0.9 and re-bootstrapped at epoch 311 (June 27), then failed validation and was removed again by Proposal 87 (July 15) and re-bootstrapped a second time -- two validation failures in three weeks on the network's flagship model family.

The overall score -- Gonka 2/8, OpenRouter 1/8, OpenAI 4/8, Anthropic 1/8, Together AI 0/8 -- reveals a landscape where Gonka's remaining structural advantages are session persistence (shared with OpenAI) and raw price (currently subsidy-assisted). Closing the infrastructure and ecosystem gaps identified in the companion provider landscape document (gonka_provider_landscape_map.md) remains the priority.

---

## Methodology

Each of the 8 dimensions below is evaluated from the perspective of an OpenClaw agent developer building production agent systems. Scoring follows a strict framework:

- **WIN:** The provider has a clear, measurable advantage for OpenClaw agent use cases on this dimension. The advantage must be structural (not just marketing), and must matter for agents specifically (not general LLM usage).
- **TIE:** The provider delivers comparable functionality. Minor differences exist but do not meaningfully affect agent development outcomes.
- **LOSE:** The provider has a clear disadvantage that creates friction, cost, or capability gaps for OpenClaw agent developers.

Scoring is framed from the agent developer's perspective: "As an OpenClaw developer building a production agent, which provider serves me best on this dimension?" Each verdict includes one-line evidence. The framework deliberately avoids weighting dimensions -- leadership should weight based on their strategic priorities.

All data points are sourced from provider documentation, pricing pages, third-party price trackers, and the research corpus in `.planning/research/`. Prices verified as of July 2026 unless otherwise noted. Where a figure is an earlier internal estimate that could not be re-verified, it is marked as such. Note that this matrix's compared set excludes DeepSeek (April 24 was the V4 *Preview*; the official V4 release, announced June 30 for mid-July 2026, introduces China's first time-of-day API pricing -- rates double during Beijing peak hours (9:00-12:00, 14:00-18:00): V4-Pro roughly $0.42/$0.84 per 1M off-peak, $0.84/$1.68 peak; V4-Flash CNY 1.00/2.00 regular; the legacy deepseek-chat and deepseek-reasoner endpoints retire after July 24, 2026 -- so any 24/7 agent cost model using a flat DeepSeek rate understates peak-hour cost up to 2x, and "no rush-hour pricing" is a new positioning lever for Gonka) and Google Gemini (3.5 Flash $1.50/$9.00 standard -- the $0.75/$4.50 rate widely quoted is the Batch/Flex non-interactive tier, not a cut to the standard rate; cached input $0.15, 1M context; 3.1 Pro $2/$12 up to 200K context, $4/$18 above; 3.1 Flash-Lite $0.25/$1.50); DeepSeek undercuts most compared providers, while Gemini 3.5 Flash at standard rates now sits mid-pack (July 2026 coverage frames it at ~3x the cost of the model it replaced) and should be added in a future revision. Groq is a further omission worth flagging: it serves open-weight models (Llama, Qwen, DeepSeek distills, Gemma) at $0.05-$0.90 per 1M input (e.g. Llama 3.1 8B Instant $0.05/M input, Llama 3.3 70B $0.59/$0.79) on LPU hardware at 500+ tokens/sec with a free tier -- a direct price-and-speed competitor for latency-sensitive agent tool-call chains.

---

## Feature Matrix

| Dimension | Gonka | OpenRouter | OpenAI | Anthropic | Together AI |
|-----------|-------|------------|--------|-----------|-------------|
| **Agent Sessions** | **WIN:** Server-side session persistence via /v1/sessions API; state survives across requests without client re-sending context | **LOSE:** Stateless passthrough; all session management is client-side | **WIN:** Responses + Conversations API (previous_response_id, server-side conversation objects) provides native server-side state on the primary API surface | **LOSE:** No session management; stateless chat completions only | **LOSE:** No session management; stateless API |
| **Model Tiering / Auto-Routing** | **TIE:** 3-tier auto-routing via X-Gonka-Tier header; native at the infrastructure layer, but client-side routers now replicate this for every provider | **TIE:** Manual model selection from 400+ catalog; no native tier routing, but ClawRouter-class client routers fill the gap | **TIE:** Manual model selection; no auto-routing, but commodity client routers apply | **TIE:** Manual model selection; same client-router mitigation applies | **TIE:** Manual model selection; same client-router mitigation applies |
| **Tool Calling** | **TIE:** Kimi K2.6 / MiniMax M2.7 native tool calling, OpenAI-compatible format; 200-300 sequential calls stable in internal K2.5-era tests (needs re-run on current lineup) | **TIE:** Passes through each provider's tool calling implementation; quality varies by underlying model | **WIN:** Best-in-class function calling with structured outputs and guaranteed JSON schema compliance | **TIE:** Strong tool use with structured output features; reliable but less mature than OpenAI's | **TIE:** Supported for compatible models via OpenAI-compatible API; quality depends on model |
| **Streaming** | **TIE:** vLLM SSE streaming via OpenAI-compatible endpoint | **TIE:** SSE streaming passthrough from upstream providers | **TIE:** Native SSE streaming with full event types | **TIE:** Native SSE streaming | **TIE:** SSE streaming via OpenAI-compatible API |
| **Memory / Context Management** | **TIE:** /v1/memory API with TF-IDF search provides persistent key-value memory; functional but lower recall than vector-based approaches | **TIE:** Passes through underlying providers' prompt caching automatically (cached input at 10-20% of standard rates on many models) | **WIN:** Native prompt caching, automatic, cached input billed at 10% of the input rate (90% discount) | **WIN:** Prompt caching with 90% discount on cached reads (25% write premium); Batch API stacks a further 50% off | **TIE:** Prompt caching now enabled by default with 5-10x cached-input discounts on select models (e.g. K2.6 $1.20 -> $0.20 cached) |
| **Pricing Model** | **WIN:** Live blended per-token rate recalculated every block from network utilization -- recently ~$0.0003 per 1M tokens via brokers; cheapest listed provider for Kimi K2.6 and MiniMax M2.7 on price trackers. Caveat: rate is near-zero partly because the network is underutilized and subsidized | **TIE:** Per-token passthrough at provider list price; 5.5% payment-processing fee on card credit purchases (5.0% crypto), no per-token markup | **TIE:** Transparent per-token pricing: GPT-5.4 $2.50/$15 (mini $0.75/$4.50, nano $0.20/$1.25), GPT-5.6 (GA Jul 9, 2026) Sol $5/$30, Terra $2.50/$15, Luna $1/$6; 90% caching discount | **TIE:** Opus 4.8 $5/$25, Sonnet 5 $3/$15 ($2/$10 intro through Aug 31, 2026), Haiku 4.5 $1/$5; flagship Fable 5 at $10/$50 remains premium, but Opus-class pricing fell 3x vs the 2025 lineup | **TIE:** Own GPU clusters, no middleman markup; K2.6 $1.20/$4.50 ($0.20 cached), K2.7-Code $0.95/$4.00 ($0.19 cached); no longer the K2-family price leader |
| **Uptime / Reliability** | **LOSE:** No published SLA; ~100M tokens/day is real traffic but the network is unproven at enterprise scale, with inherent variability from heterogeneous decentralized nodes; Kimi K2.6 failed validation and was removed/re-bootstrapped twice in three weeks (Proposals 78 and 87) | **TIE:** Established track record with multi-year operation; free tier throttled under load; no formal SLA but generally reliable | **WIN:** 99.9%+ SLA with global infrastructure; multi-region redundancy; the reliability benchmark | **TIE:** Enterprise SLA and solid infrastructure record, but Fable 5 / Mythos 5 were offline ~3 weeks (Jun 12 - Jul 1, 2026) under a US export-control order -- a material flagship outage for agent developers | **TIE:** Own infrastructure with reliable track record; no formal SLA published |
| **Model Breadth** | **LOSE:** 2 model families (Kimi K2.6, MiniMax M2.7; Qwen3-235B retired Jun 25, 2026), with GLM-5.2 approved via Proposal 79 but rollout incomplete; improved from the single-model K2.5 plan but still the smallest open catalog compared | **WIN:** 400+ models from 70+ providers; broadest selection available; single API key accesses every model | **TIE:** GPT-5.4/5.5/5.6 lineup across mini/nano tiers; limited but well-differentiated selection | **LOSE:** 4 current models (Fable 5, Opus 4.8, Sonnet 5, Haiku 4.5); smallest catalog among compared providers | **TIE:** 200+ open models including K2.6, K2.7-Code, GLM-5.2, MiniMax M3/M2.7, Llama 3.3, and fine-tuning options |

### Summary Scores

| Provider | Wins | Ties | Losses | Score |
|----------|------|------|--------|-------|
| **Gonka** | 2 | 4 | 2 | **2/8** |
| **OpenRouter** | 1 | 6 | 1 | **1/8** |
| **OpenAI** | 4 | 4 | 0 | **4/8** |
| **Anthropic** | 1 | 5 | 2 | **1/8** |
| **Together AI** | 0 | 7 | 1 | **0/8** |

---

## Dimension Deep Dives

### 1. Agent Sessions

**What OpenClaw agents need:** When an OpenClaw agent processes a multi-step task -- classifying a request, planning an approach, executing subtasks, synthesizing results -- it makes multiple LLM calls that share conversational context. Without server-side session persistence, each call must re-send the full conversation history, inflating token costs. OpenClaw heartbeats compound this: every 30 minutes, the agent resends its full context to check for new tasks, costing approximately 9,600 tokens per heartbeat regardless of whether anything changed (internal estimate: OpenClaw pricing guides, .planning/research/STACK.md). Over 24 hours, heartbeats alone generate 48 full context re-sends.

**How each provider delivers:**

**Gonka** offers a dedicated /v1/sessions API (built in v1.2) where agents create a session via X-Gonka-Session-ID header, and the server maintains conversation state across requests. Subsequent calls within the same session do not need to re-send prior messages -- the server appends them automatically. This is a genuine architectural advantage for agent workloads, directly reducing the token overhead of heartbeats and multi-step tasks. However, the current implementation stores sessions in-memory (v1.2 tech debt), meaning sessions are lost on server restart -- a production reliability concern that partially undermines the feature's value proposition.

**OpenRouter** is a stateless passthrough proxy. It receives a request, routes it to the upstream provider, and returns the response. No conversation state is maintained between requests. Agents using OpenRouter must manage their own session state client-side. Note, however, that OpenRouter passes through upstream providers' prompt caching (see dimension 5), so the *cost* of re-sent context is substantially mitigated even though the architecture remains stateless.

**OpenAI** now offers server-side state natively on its primary API surface. The Responses API with the Conversations API (previous_response_id chaining and server-side conversation objects) replaced the Assistants API, which is deprecated and shuts down August 26, 2026. Unlike the old Assistants threads -- a separate, beta API surface -- server-side stateful conversations are the default path for new OpenAI integrations. This upgrades OpenAI from TIE to WIN on this dimension and materially weakens Gonka's "only provider with sessions" claim: any external material asserting that must be retired.

**Anthropic** offers no session management. Each request is stateless. Anthropic's prompt caching (dimension 5) partially compensates by reducing the cost of re-sent context, but the tokens are still transmitted and processed -- caching reduces cost, not bandwidth.

**Together AI** offers no session management. Each request is fully stateless, though default-on prompt caching (new since April 2026) reduces the cost of repeated context.

**Verdict rationale:** Gonka and OpenAI both offer server-side session persistence natively. Gonka's advantage is now shared rather than unique; its remaining edge is combining sessions with the /v1/memory API on an OpenAI-compatible chat surface, plus price. Messaging should shift from "only provider with sessions" to "sessions plus memory at decentralized prices."

---

### 2. Model Tiering / Auto-Routing

**What OpenClaw agents need:** A well-designed agent does not use the same model for every subtask. Classification is a simple task that can be handled by a cheap, fast model; complex reasoning requires a strong, expensive model. Tiered routing is now standard enterprise practice: the AICC (AI Cost Council) analysis of 2.4B enterprise API calls ("Enterprise Token Costs Drop 67% Year-Over-Year as Multi-Model AI Adoption Hits Record High") shows blended enterprise cost falling from $18.40/M to $6.07/M tokens between Q1 2025 and Q1 2026 (67% YoY), with a tiered-routing median of $2.31/M, attributed to model routing/tiering plus price cuts.

**How each provider delivers:**

**Gonka** implements 3-tier auto-routing through the X-Gonka-Tier header and automatic content pattern matching (built in v1.2, infrastructure/agent/tiering.py). The implementation was built against K2.5 quantization tiers (lite/mid/full); with the network now serving multiple model families (K2.6, M2.7), the tier-to-model mapping needs re-verification and this section's implementation details should be re-derived against the current lineup. The pattern -- header-based tier selection plus content-aware auto-routing at the infrastructure layer -- remains sound.

**The competitive context has changed decisively since April 2026:** cost-based model routing is now a solved, commoditized layer in the OpenClaw ecosystem. ClawRouter ships with/alongside OpenClaw as a governance surface (bundled routing, dynamic model discovery, quotas, budget reporting), and multiple third-party routers exist: BlockRunAI's ClawRouter (41-55+ models, sub-millisecond local tier classification into SIMPLE/MEDIUM/COMPLEX/REASONING, claiming up to 92% savings), iblai/claw-router (70%+ savings claims), ClawRoute, and others. A developer no longer maintains custom routing middleware -- they install a router, and that router works with every provider in this comparison.

**OpenRouter, OpenAI, Anthropic, and Together AI** all still require manual model selection natively, but the client-router layer neutralizes this as a differentiator: an OpenClaw developer gets tiering across any of them for free.

**Verdict rationale:** Downgraded from a Gonka WIN (v1.0) to an all-around TIE. Gonka remains the only compared provider with *infrastructure-level* tiering, but since commodity client routers deliver the same outcome for every provider, the feature no longer changes an agent developer's provider choice. Gonka's defensible differentiation now rests on sessions/memory and price, not routing.

---

### 3. Tool Calling

**What OpenClaw agents need:** Tool calling (function calling) is the mechanism by which agents interact with external systems -- reading files, running searches, executing code, calling APIs. For agent workloads, tool calling reliability is arguably the single most important model capability: does the model reliably select the right tool, format parameters correctly, and handle multi-step tool chains without hallucinating function names or arguments?

**How each provider delivers:**

**Gonka** serves the Kimi K2.6 and MiniMax M2.7 families, both of which support native tool calling in OpenAI-compatible function calling format and are explicitly agent/coding-focused models. Internal v1.2 integration tests (infrastructure/tests/test_openclaw.py) demonstrated 200-300 stable sequential tool calls -- but those tests ran against K2.5 and should be re-run against the current model lineup before the figure is cited externally. Tool calling quality remains model-dependent (the models' quality, not Gonka's infrastructure).

**OpenRouter** passes through whatever tool calling the underlying model provider supports. The variability is the issue: an agent using OpenRouter with automatic model selection cannot guarantee consistent tool calling quality across models. OpenRouter documents which models support function calling, which helps, but the quality guarantee is only as strong as the chosen model.

**OpenAI** delivers best-in-class function calling with structured outputs (guaranteed JSON schema compliance). The GPT-5.x lineup reliably selects tools, formats parameters, and handles complex multi-tool workflows. This remains the benchmark against which other tool calling implementations are measured.

**Anthropic** offers strong tool use that has matured through 2025-2026. Claude models (Fable 5, Opus 4.8, Sonnet 5) handle multi-tool workflows well. Tool use quality is close to OpenAI's but slightly less mature in edge cases. The TIE verdict reflects that for most agent workflows, Anthropic's tool calling is reliable and productive.

**Together AI** supports tool calling for compatible models (K2.6, K2.7-Code, Llama 3.3, etc.) via OpenAI-compatible API. Quality depends on the model chosen.

**Verdict rationale:** OpenAI wins because structured outputs with guaranteed schema compliance is a measurable, concrete advantage for agent workloads. Gonka, Anthropic, and Together AI all offer functional tool calling that serves most agent use cases, earning TIEs. OpenRouter's passthrough model creates variability that prevents a WIN but does not constitute a clear loss.

---

### 4. Streaming

**What OpenClaw agents need:** Server-Sent Events (SSE) streaming allows agents to begin processing partial responses before the full generation completes, reducing perceived latency and enabling progressive processing. All major inference providers support SSE streaming, and OpenClaw expects it via the standard OpenAI streaming format.

**How each provider delivers:**

All five compared providers support SSE streaming via the OpenAI-compatible `stream: true` parameter. Gonka implements streaming through vLLM's native SSE support. OpenRouter passes through streaming from upstream providers. OpenAI, Anthropic, and Together AI all provide native streaming implementations. Practical differences (time to first token, tool-call streaming edge cases) are minor for the standard agent use case.

**Verdict rationale:** Streaming is table stakes. All providers deliver it. Universal TIE.

---

### 5. Memory / Context Management

**What OpenClaw agents need:** Long-running agents accumulate knowledge over time -- user preferences, project context, prior decisions, learned patterns. Two mechanisms address this: prompt caching (reducing the cost of re-sending known context) and persistent memory APIs (storing and retrieving knowledge across sessions). OpenClaw agents are particularly affected because heartbeats resend approximately 9,600 tokens every 30 minutes (internal estimate) -- 460,800 tokens of repeated context per day.

**The landscape change since v1.0 of this matrix is that prompt caching is now effectively universal:** OpenAI (90% off cached input), Anthropic (90% off), Google Gemini (implicit + explicit caching), Together AI (default-on, 5-10x discounts), DeepInfra (K2.6 cached at $0.15), Fireworks, DeepSeek (cache-hit $0.0028/M), Moonshot's own API (K2.7 cache-hit $0.19; K3 cached input $0.30 vs $3.00 uncached), and OpenRouter (automatic passthrough). Any Gonka savings claim computed against uncached baselines is invalid and must be recomputed against cached rates.

**How each provider delivers:**

**Gonka** offers a /v1/memory API (built in v1.2) providing persistent key-value memory storage. The current search implementation uses TF-IDF (v1.2 tech debt -- noted in PROJECT.md), which provides functional keyword-based retrieval but lower recall than vector embedding approaches. This is a capability no other compared provider offers in the same form, but the quality gap vs vector search limits its practical advantage. Combined with session persistence (dimension 1), agents can maintain both short-term (session) and long-term (memory) context.

**OpenRouter** passes through underlying providers' prompt caching automatically, with cached input billed at 10-20% of standard rates for many models. The v1.0 claim that "caching is not exposed through the routing layer" is no longer true. OpenRouter still offers no persistent memory API, but on the economics of repeated context it now tracks the underlying providers. Upgraded from LOSE to TIE.

**OpenAI** provides native, automatic prompt caching with cached input billed at 10% of the input rate -- a 90% discount (e.g. GPT-5.4 cached input $0.25/M vs $2.50/M). OpenAI now also offers explicit cache writes billed at 1.25x uncached input, with extended ~24h cache retention -- meaning both OpenAI and Anthropic now carry write premiums on explicit caching, which the "Gonka sessions have no cache-write premium" pitch should reflect. For OpenClaw heartbeats resending the same system prompt, the repeated portion costs one-tenth of standard on cache hits.

**Anthropic** offers 90% discount on cached reads with a 25% write premium on the first cache write. Over 48 daily heartbeats the effective savings on the cached-context portion approach 89%. The Batch API adds a further 50% off all tokens, stackable with caching, for latency-tolerant workloads. OpenAI and Anthropic caching economics are now essentially at parity.

**Together AI** now runs prompt caching enabled by default (the disable flags are deprecated) with 5-10x cached-input discounts on select models: K2.6 $1.20 -> $0.20 cached, K2.7-Code $0.95 -> $0.19, DeepSeek V4 Pro $1.74 -> $0.20. The v1.0 LOSE verdict ("no memory or caching features") is obsolete; upgraded to TIE.

**Verdict rationale:** OpenAI and Anthropic win with the deepest, most automatic caching (both 90%). OpenRouter and Together AI now deliver meaningful caching and move to TIE. Gonka's memory API remains a unique capability, but TF-IDF search quality and the universality of competitor caching hold it at TIE.

---

### 6. Pricing Model

**What OpenClaw agents need:** Agentic workflows consume 5-30x the tokens of chatbot usage (Gartner, March 2026), and inference now accounts for roughly 85% of enterprise AI budgets. Heartbeats add a recurring fixed cost (~9,600 input tokens every 30 minutes, internal estimate). For agent developers, the pricing model matters as much as the per-token rate: hidden costs, transparency, and predictability all affect total cost of operating agent infrastructure.

**How each provider delivers:**

**Gonka** pricing is now live and published, replacing the "TBD" status of the v1.0 matrix. The network charges a single blended per-token rate recalculated every block from network utilization -- recently around $0.0003 per 1M tokens via brokers. Access is resold by third-party brokers (GonkaGate, JoinGonka, OpenGNK, GonkaBroker, Gonka24), each adding its own fee, and four of the five now show public pricing. Gonka24 publishes model-specific retail rates: MiniMax M2.7 $0.018/$0.072, Kimi K2.6 $0.055/$0.32, GLM-5.2 $0.095/$0.30 per 1M. Note the spread: the $0.018/$0.072 figure quoted in earlier GTM drafts as Gonka24's general rate is only the M2.7 "from" price -- K2.6 workloads cost roughly 4x the old flat $0.045 blended assumption (K2.6 blended ~$0.19 at 1:1), so any Gonka24-based monthly projections built on the flat rate understate K2.6 cost ~4x. JoinGonka now publishes itemized rates for Kimi K2.6 -- $0.003 per 1M input and $0.009 per 1M output (the "~$0.003 blended" figure in earlier drafts was only the input side). The OpenGNK (proxy.gonka.gg) near-passthrough figure of ~$0.00016434 per 1M quoted in earlier drafts could not be re-verified as of July 18: current gateway comparisons describe proxy.gonka.gg as ~133% more expensive than other Gonka gateways, with live prices reflecting a "temporary pricing adjustment" from the network -- treat any OpenGNK figure as MEDIUM confidence and volatile, and re-verify before publishing the broker-fee table. GonkaBroker also lists rates. All retail tiers remain far below any centralized provider. Gonka is listed as the cheapest provider for Kimi K2.6 and MiniMax M2.7 on price trackers; for reference, the cheapest centralized baselines are OpenRouter K2.6 at $0.66/$3.41, then DeepInfra K2.6 at $0.75/$3.50 and Fireworks K2.6 at $0.95/$4.00 (Moonshot's own first-party K2.6 rate is $0.95/$4.00, cache-hit input ~$0.16), and MiniMax M2.7 at $0.30/$1.20 official ($0.24/$0.96 via OpenRouter, ~12 providers serving it). Two caveats for GTM use: (1) the rate is near-zero largely because the network is underutilized and partly subsidized -- it will rise with utilization and should not be quoted as a durable price point; (2) effective developer cost varies enormously by broker and by model -- from JoinGonka's $0.003/$0.009 to Gonka24's 100x+ retail markup -- and only GonkaGate's fee schedule remains unitemized. Even so, the current rate is orders of magnitude below every compared provider, earning a WIN with the sustainability caveat clearly disclosed.

**OpenRouter** passes tokens through at provider list price with no per-token markup. The 5.5% figure widely cited (including in v1.0 of this document) is a payment-processing fee on credit-card credit purchases ($0.80 minimum); crypto payments carry a 5.0% flat fee, and BYOK fees are request-based as of July 2026: the first 1M BYOK requests per month are free (Enterprise: 5M), after which OpenRouter charges 5% of what the same call would have cost on its platform. OpenRouter's K2-family listings (K2.6 at $0.66/$3.41, K2.5 at $0.375/$2.025) actually undercut every direct host including DeepInfra, and cached-input passthrough further reduces effective agent costs. (Lifecycle note: following the K3 launch on July 16, Moonshot has closed K2.5 to newly registered users and scheduled full platform sunset for August 31, 2026, redirecting K2.5 API traffic to K2.6 -- third-party K2.5 rates remain purchasable for now but any K2.5-anchored comparison has weeks of shelf life.) The "OpenRouter is more expensive per token" framing from v1.0 is wrong; the TIE reflects competitive passthrough pricing with a modest funding-fee layer.

**OpenAI** offers transparent per-token pricing: GPT-5.4 at $2.50/$15 per 1M (mini $0.75/$4.50, nano $0.20/$1.25), GPT-5.5 in the $5/M-input class, and GPT-5.6, GA since July 9, 2026, at Sol $5/$30, Terra $2.50/$15, Luna $1/$6 per 1M in/out with 1M-token context on all three tiers (Terra $1.25/$7.50 in Batch or Flex). Cached input at 10% of the input rate (explicit cache writes at 1.25x) and a Batch API at ~50% off substantially reduce effective agent costs. GPT-4o -- the v1.0 benchmark at $2.50/$10 -- was retired from ChatGPT on April 3, 2026 and lingers in the API as legacy only; it should no longer anchor comparisons.

**Anthropic** pricing has fallen sharply since the v1.0 comparison: Claude Opus 4.8 at $5/$25 per 1M (down 3x from Opus 4's $15/$75), Claude Sonnet 5 at $3/$15 (introductory $2/$10 through Aug 31, 2026), Claude Haiku 4.5 at $1/$5. The new flagship Claude Fable 5 at $10/$50 remains premium, but the workhorse Opus/Sonnet tiers are now broadly competitive with OpenAI. Combined with 90% caching and a 50%-off Batch API, the v1.0 LOSE verdict ("highest cost per token") no longer holds; every "Opus $45 blended / 30x more expensive" calculation built on the old rates is wrong by roughly 3x. Upgraded to TIE.

**Together AI** operates its own GPU clusters with no middleman markup. Its Kimi lineup is now K2.6 at $1.20/$4.50 ($0.20 cached) and K2.7-Code at $0.95/$4.00 ($0.19 cached); K2.5 no longer appears on its serverless pricing page, so the v1.0 benchmark of "$0.50/$2.50, lowest verified K2.5 price" no longer exists. Llama 4 Maverick ($0.27/$0.85), previously cited as the open-model price floor, has also been delisted; the open-model floor is now set by DeepSeek V4 Flash ($0.14/$0.28) and small Qwen models on other hosts. Together's pricing is transparent and fair but no longer the cheapest in any compared category. Downgraded from WIN to TIE.

**Verdict rationale:** Gonka wins on current listed price by a wide margin, with the subsidy/utilization caveat stated plainly. Everyone else lands at TIE: OpenRouter (passthrough plus funding fee), OpenAI and Anthropic (premium but transparent, deep caching and batch discounts), Together (fair but no longer cheapest).

---

### 7. Uptime / Reliability

**What OpenClaw agents need:** Agent reliability requirements are fundamentally different from chatbot requirements. An agent mid-workflow -- having already read files, planned an approach, and completed 3 of 5 subtasks -- loses all progress if the inference provider is unavailable for the 4th call. OpenClaw agents running on heartbeats need near-continuous availability. For production agent deployments, uptime SLAs and historical reliability track records determine whether the provider can be trusted with mission-critical workflows.

**How each provider delivers:**

**Gonka** now carries real production traffic -- roughly 100M tokens/day across its served models -- which is an improvement over the pre-launch status in v1.0. But it still has no published SLA, no public status page, and no published historical uptime data. Decentralized infrastructure introduces inherent variability: heterogeneous GPU hardware, public internet routing between nodes, and variable node availability. Model-serving stability is also now a documented concern: Kimi K2.6 failed validation majority and was removed twice in three weeks -- Proposal 78 (June 25, restored by Proposal 79 June 26, re-bootstrapped epoch 311 June 27) and again Proposal 87 (July 15, followed by a second re-bootstrap). The LOSE verdict stands: an agent developer evaluating Gonka for production use still has essentially zero reliability data to base a decision on, and the absence of evidence is itself evidence of risk.

**OpenRouter** has operated for multiple years with a generally reliable track record but no formal SLA. As a routing layer, its reliability depends on both its own infrastructure and upstream providers -- a double dependency, mitigated by automatic fallback routing to alternative providers for the same model. TIE: operational maturity without formal guarantees.

**OpenAI** sets the industry standard: 99.9%+ SLA backed by global, multi-region infrastructure with automatic failover and a public status page with historical data. WIN.

**Anthropic** delivers enterprise SLAs and historically strong infrastructure reliability, but suffered a roughly three-week flagship outage in mid-2026: Claude Fable 5 and Mythos 5 were taken offline on June 12, 2026 by a US Commerce Department export-control order and only restored July 1, 2026 -- across Claude.ai, the Claude Platform, Claude Code, and Cowork. The cause was regulatory, not infrastructure, but from an agent developer's perspective a multi-week flagship outage is an outage. Downgraded from WIN (v2.1) to TIE. (Post-restoration pricing note: Fable 5 was included in up to 50% of weekly subscription usage limits only through July 7, 2026; since then subscription access is metered via usage credits at the same $10/$50 per 1M API rate, so API-metered pricing is the only basis for Fable 5 agent cost modeling.)

**Together AI** operates its own GPU clusters with a generally reliable track record and no formal published SLA. TIE.

**Verdict rationale:** OpenAI wins with a formal SLA and a clean track record. Anthropic, OpenRouter, and Together AI earn TIEs -- Anthropic's June 2026 export-control outage removes its unqualified WIN and, incidentally, is a concrete data point for Gonka's multi-provider/decentralization argument (no single regulator can switch off a decentralized network's flagship). Gonka still loses: real traffic is a start, but publishable uptime data, a status page, and an SLA are prerequisites for production trust.

---

### 8. Model Breadth

**What OpenClaw agents need:** Different agent tasks benefit from different models, and model breadth provides fallback resilience. For OpenClaw agents specifically, breadth enables the multi-model tiering pattern that agent developers consistently cite as a cost priority.

**How each provider delivers:**

**Gonka** now serves two model families -- Kimi K2.6 (superseding the originally planned K2.5; a K2.6 validation fix shipped in the v0.2.13 cycle) and MiniMax M2.7 (route support added in devshard v3, released July 9, 2026; sole PoC model and base delegation target since Proposal 78 retired Qwen3-235B on June 25, 2026; note the Kimi validation churn covered in dimension 7) -- at ~100M tokens/day combined, with GLM-5.2 (Z.ai, released June 13, 2026; 1M context, open weights, leads open agent benchmarks) approved via Proposal 79 (June 26, introduced at weight_scale_factor 2.47). GLM-5.2's serving status is genuinely ambiguous as of July 19: Gonka's own network-updates page describes it as proposed with current status unclear, GonkaBroker lists it as "coming soon" with no price, while Gonka24 already sells a GLM-5.2 rate card at $0.095/$0.30 per 1M -- the defensible position is "approved via Proposal 79; live via some brokers, rollout incomplete." (Gonka24's advertised "$0.95/$3.00 standard price" comparison is its own marketing figure, not any real provider's list rate -- Z.ai's official GLM-5.2 API is $1.40/$4.40 per 1M ($0.26 cached input), Together AI serves it at the identical $1.40/$4.40 ($0.26 cached), and OpenRouter serves it from ~$0.41-$1.00 input / ~$4.00 output; anchor comparisons on those.) This retires the v1.0 "single model, no fallback" weakness in its sharpest form, and the model choices are well-matched to agent workloads (MiniMax's 10B-active MoE architecture is particularly serve-efficient for a distributed GPU network). Context: the broader open-model landscape has also moved -- Kimi K2.7-Code (June 2026) and Kimi K3 (launched via app/API July 16, 2026 at $3/$15, $0.30 cached; open weights still committed for July 27 on Hugging Face, expected under Moonshot's Modified MIT license -- Gonka-hostable, unlike MiniMax M3's restricted Community License; #1 on Frontend Code Arena, and now independently scored at Artificial Analysis Intelligence Index 57.11 -- level with Opus 4.8 and GPT-5.5, behind Claude Fable 5 and GPT-5.6 Sol -- a more defensible anchor than the arena Elo alone) are the current Moonshot flagships; MiniMax M3 (June 1, 2026; 428B total / 23B active MoE, 1M context, native multimodality) supersedes M2.5/M2.7 as MiniMax's flagship while keeping the small-active-params serving economics -- MiniMax now publishes first-party M3 pricing of $0.30/$1.20 per 1M up to 512K input tokens, rising to $0.60/$2.40 above 512K (displayed rates labeled a permanent 50% discount off list), so 1M-context agent cost modeling should use the $0.60/$2.40 tier; Together AI also serves M3 and M2.7 at $0.30/$1.20 ($0.06 cached). The US open-weight field has also revived: Thinking Machines' Inkling (July 15, 2026; 975B/41B active, Apache 2.0, 1M context) and NVIDIA Nemotron 3 Ultra (June 2026) are both candidate serve targets for a decentralized network -- Apache-2.0 Inkling especially. Gonka's catalog is real but still the smallest compared, currently one flagship generation behind on both its served families; the in-progress GLM-5.2 addition partially answers the "no frontier-class option" criticism, though a permissively-licensed Western option is still absent. LOSE, though narrower than in v1.0.

**OpenRouter** offers 400+ active models from 70+ providers (OpenRouter's own figure as of mid-July 2026; the "500+" in v1.0 was an overstatement). A single API key provides access to every model with consistent formatting. Model breadth remains OpenRouter's primary competitive advantage and the reason it is built into OpenClaw as a default provider. WIN. OpenRouter's breadth remains particularly threatening to Gonka because it provides the same Kimi-family access via upstream providers, plus hundreds of alternatives.

**OpenAI** offers the GPT-5.4/5.5/5.6 lineup across mini/nano tiers plus embeddings and media models. Small numerically, but each model serves a distinct purpose and quality tier, providing genuine tiering capability. TIE.

**Anthropic** offers 4 current models (Fable 5, Opus 4.8, Sonnet 5, Haiku 4.5, plus legacy versions). The smallest catalog among compared providers, though well-differentiated across capability tiers. LOSE.

**Together AI** offers 200+ open models including K2.6, K2.7-Code, GLM-5.2/5.1 ($1.40/$4.40, $0.26 cached), MiniMax M3/M2.7 ($0.30/$1.20, $0.06 cached), Llama 3.3, and fine-tuning options. TIE.

**Verdict rationale:** OpenRouter wins decisively. Together AI and OpenAI earn TIEs. Anthropic and Gonka lose -- Anthropic for a small but high-quality lineup, Gonka for the still-narrow (though much improved) multi-family catalog.

---

## Key Takeaways

1. **Gonka's two v1.0 differentiators have been halved.** Server-side sessions are now shared with OpenAI's Responses + Conversations API (the primary OpenAI surface; the old Assistants API dies August 26, 2026), and automatic model tiering has been commoditized by ClawRouter-class client routers that work with every provider. The defensible remainder is the sessions + memory combination on an OpenAI-compatible surface -- and price.

2. **Gonka's biggest competitive liabilities remain trust gaps, not feature gaps.** Model breadth (2-3 families vs 400+ models) and reliability (no SLA, no status page vs 99.9%+) require infrastructure and time. The ~100M tokens/day of real traffic is an asset that is currently invisible: publishing uptime stats and a transparent status page converts it into trust. Note also that the "only decentralized provider with agent features" claim used elsewhere in the GTM corpus is no longer tenable: Akash Agents now deploys OpenClaw (and Hermes) agents "in a few clicks" -- a direct play for the same OpenClaw-builder personas -- and AkashML serves Kimi K2.6 with a full public catalog and per-model pricing at 10B+ tokens/day as of early July 2026 (up from ~5B in May), roughly 100x Gonka's ~100M tokens/day, with Venice, ElizaOS, Morpheus, and Gensyn as named customers. Chutes (Bittensor Subnet 64) is larger still, self-reporting 160B tokens/day -- and on June 29, 2026 Kraken listed seven Bittensor subnet alpha tokens including Chutes AI (SN64) and Targon Compute (SN4), giving Chutes major-exchange token liquidity (leading subnet alphas carry tens-of-millions-to-$100M+ market caps) on top of its throughput story.

3. **OpenRouter remains Gonka's primary competitive threat because it occupies the "default OpenClaw provider" position.** OpenRouter is built in, requires zero configuration, passes through provider caching, and its funding fee (5.5% card / 5.0% crypto, not a per-token markup) is smaller friction than v1.0 assumed. It also already exposes decentralized inference: Chutes (Bittensor Subnet 64) is a visible OpenRouter provider serving 9 models (as of July 18, 2026: Z.ai GLM, Qwen, MoonshotAI Kimi, Google Gemma, and MiniMax models; DeepSeek not confirmed in the current listing), so "the only decentralized provider a developer can actually use" is no longer part of Gonka's story -- any OpenRouter user can route to decentralized inference with zero config today. Gonka must either become a built-in OpenClaw provider or demonstrate advantages compelling enough to justify manual setup -- realistically, price plus sessions.

4. **Prompt caching is now universal, not an OpenAI/Anthropic specialty, and it substantially narrows the sessions cost story.** OpenAI (90% reads, 1.25x explicit writes, ~24h retention), Anthropic (90% reads, 25% write premium), Together (default-on 5-10x), OpenRouter (passthrough), and Moonshot's own API (K3 cached at $0.30 vs $3.00) all discount repeated context. Both major closed providers now carry write premiums on explicit caching, so the "no cache-write premium" session pitch applies to OpenAI as well as Anthropic. Every "sessions save 60-84% vs uncached competitors" figure in the GTM corpus was computed against baselines that no longer exist and must be recomputed against cached rates. The session pitch should emphasize the architectural benefit (simpler agent code, no context re-transmission at all) alongside a re-derived, smaller cost delta.

5. **Gonka can now compete on price -- carefully.** The live blended rate (~$0.0003/M via brokers, cheapest listed for K2.6 and M2.7) replaces the v1.0 "pricing TBD" gap and beats every compared provider by orders of magnitude. But the rate is a function of underutilization and subsidy, and brokers add fees that now span orders of magnitude -- JoinGonka's itemized $0.003/$0.009 per 1M for K2.6 to Gonka24's per-model retail card (M2.7 $0.018/$0.072, K2.6 $0.055/$0.32, GLM-5.2 $0.095/$0.30) -- so the recommended broker-fee comparison table can now be built from public data (only GonkaGate remains unitemized; OpenGNK's earlier ~$0.00016/M "near-passthrough" figure is unverified and now contradicted by gateway comparisons, so re-verify it before publication), and any material quoting "$0.018/$0.072" as Gonka's or Gonka24's general rate must switch to the per-model card. External materials should present the network rate with its mechanism (per-block, utilization-based) rather than a fixed price promise, and cost comparisons should be re-based on current competitor prices: OpenRouter K2.6 $0.66/$3.41 (the cheapest centralized K2.6), Together K2.6 $1.20/$4.50, Fireworks K2.6 $0.95/$4.00, Moonshot first-party K2.6 $0.95/$4.00, MiniMax M2.7 $0.30/$1.20 official (Together matches), DeepSeek V4 with time-of-day pricing (~$0.42/$0.84 off-peak, 2x during Beijing peak hours), Gemini 3.5 Flash $1.50/$9 standard ($0.75/$4.50 Batch/Flex tier only), Anthropic Opus 4.8 $5/$25, Groq Llama 3.3 70B $0.59/$0.79.

---

## Source Citations

| Source | Used For | Confidence |
|--------|----------|------------|
| .planning/research/STACK.md | OpenClaw provider architecture, heartbeat token estimates, community cost reports | HIGH (internal; heartbeat figure is a Feb-Apr 2026 estimate, not re-verified) |
| .planning/research/FEATURES.md | Feature landscape, decision criteria, gap analysis | HIGH |
| .planning/research/ARCHITECTURE.md | GTM framework, competitive analysis structure, persona definitions | HIGH |
| .planning/research/PITFALLS.md | Anti-patterns, trust barriers, recovery strategies | HIGH |
| infrastructure/agent/sessions.py, tiering.py, memory.py | Gonka session, tiering, and memory implementation details | HIGH (verified against codebase; tiering built pre-multi-model, needs re-verification) |
| infrastructure/tests/test_openclaw.py | Gonka OpenClaw integration test results (K2.5-era; re-run pending) | MEDIUM |
| pricepertoken.com/endpoints/gonka; gonkabroker.com; gonka24.com; proxy.gonka.gg | Gonka live blended rate, Gonka24 per-model retail rates, OpenGNK passthrough rate, served models, ~100M tokens/day | HIGH (accessed July 2026) |
| blog.gonkahub.com | GLM-5.2 "coming soon" to the Gonka network | HIGH (accessed July 2026) |
| github.com/gonka-ai/gonka/releases | K2.6 validation fix (v0.2.13), MiniMax M2.7 route support (devshard v3, Jul 9, 2026) | HIGH (accessed July 2026) |
| OpenRouter pricing and FAQ (openrouter.ai) | Funding fees (5.5% card / 5.0% crypto), caching passthrough, catalog size, request-based BYOK terms (1M free/mo, Enterprise 5M), K2.6 $0.66/$3.41 listing | HIGH (accessed July 2026) |
| gonka.ai/docs/network-updates | Proposal 78 (Jun 25, 2026): Qwen3-235B retired; MiniMax M2.7 sole PoC model and base delegation target | HIGH (accessed July 2026) |
| docs.z.ai pricing; openrouter.ai/z-ai/glm-5.2 | GLM-5.2 official list rate $1.40/$4.40 ($0.26 cached); OpenRouter GLM-5.2 range | HIGH (accessed July 2026) |
| llm-stats.com/ai-trends; stackspend.app | Anthropic Fable 5 / Mythos 5 export-control outage (Jun 12 - Jul 1, 2026) | HIGH (accessed July 2026) |
| blog.kraken.com; cryptobriefing.com | Kraken listing of Bittensor subnet alpha tokens incl. Chutes SN64 (Jun 29, 2026) | HIGH (accessed July 2026) |
| Together AI pricing and docs (together.ai) | K2.6/K2.7-Code pricing, default-on caching, K2.5 and Maverick delisting | HIGH (accessed July 2026) |
| OpenAI pricing, deprecations (developers.openai.com) | GPT-5.4/5.5 pricing, GPT-5.6 GA tiers (Jul 9, 2026), 90% cached-input discount, 1.25x explicit cache writes, GPT-4o retirement, Assistants API sunset (Aug 26, 2026), Responses/Conversations API | HIGH (accessed July 2026) |
| Anthropic pricing (platform.claude.com) | Opus 4.8 $5/$25, Sonnet 5 $3/$15 (intro $2/$10), Haiku 4.5 $1/$5, Fable 5 $10/$50, 90% cache read / 25% write, Batch 50% | HIGH (accessed July 2026) |
| DeepSeek API pricing (api-docs.deepseek.com); Google Gemini pricing (ai.google.dev) | Excluded-competitor price floor context | HIGH (accessed July 2026) |
| Artificial Analysis, pricepertoken.com, openrouter.ai, fireworks.ai, platform.minimax.io | Multi-provider Kimi-family and MiniMax M2.7 pricing comparison; MiniMax M3, Inkling, Nemotron 3 Ultra landscape | MEDIUM-HIGH (accessed July 2026) |
| github.com/openclaw/clawrouter; github.com/BlockRunAI/ClawRouter; github.com/iblai/claw-router | Client-side router commoditization of model tiering | HIGH (accessed July 2026) |
| Messari State of Akash Q1 2026; akashml.com | Akash Agents OpenClaw deployment, AkashML Kimi K2.6 serving, 10B+ tokens/day throughput | HIGH (accessed July 2026) |
| groq.com/pricing | Groq open-model pricing and LPU throughput | HIGH (accessed July 2026) |
| tao.app/subnets/64; tao.media; openrouter.ai | Chutes (Bittensor SN64) throughput self-reports and OpenRouter provider listing | MEDIUM (self-reported token volume; accessed July 2026) |
| Gartner (March 2026, via industry coverage) | Agentic workflows at 5-30x chatbot token consumption | MEDIUM |
| AICC (AI Cost Council), "Enterprise Token Costs Drop 67% Year-Over-Year as Multi-Model AI Adoption Hits Record High" | $18.40 -> $6.07/M blended enterprise cost decline, $2.31/M tiered-routing median (Q1 2025 -> Q1 2026, 2.4B API calls) | HIGH (accessed July 2026) |

---

*Document: gonka_competitive_feature_matrix.md | Version 2.2 | 2026-07-18 (supersedes v2.1 and v1.0, 2026-04-01)*
*Companion document: gonka_provider_landscape_map.md (provider segmentation and gap analysis)*

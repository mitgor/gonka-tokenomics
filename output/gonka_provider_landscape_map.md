# Gonka Provider Landscape Map and Gap Analysis

**Version:** 1.0
**Date:** 2026-04-01
**Audience:** Gonka leadership and GTM strategy team
**Scope:** Inference provider landscape segmentation, competitive positioning, and prioritized gap analysis for OpenClaw GTM

---

## Executive Summary

The AI inference provider landscape relevant to OpenClaw agent developers contains four distinct segments: centralized API providers (OpenAI, Anthropic, Google, DeepSeek, Mistral), multi-provider routers (OpenRouter, LiteLLM, Portkey), dedicated inference platforms (Together AI, Groq, DeepInfra, Fireworks AI, SiliconFlow), and decentralized GPU networks (Gonka, Akash/AkashML, io.net, Render, SaladCloud).

Gonka occupies a unique position as the only decentralized provider with agent-native API extensions (sessions, memory, tiering, webhooks). No other provider combines decentralized infrastructure with agent-aware features. AkashML is the closest decentralized competitor, having launched an OpenAI-compatible managed inference API in November 2025 with 65 datacenters, but AkashML lacks any agent-specific extensions.

However, Gonka's competitive advantages are currently gated by five critical gaps that must be closed before any GTM push: Gonka is not a built-in OpenClaw provider, has no public documentation site, offers no self-serve API key signup, has no published pricing page, and stores sessions in-memory (v1.2 tech debt). These are not feature gaps -- they are table-stakes infrastructure gaps that prevent developers from evaluating Gonka at all. The feature matrix (gonka_competitive_feature_matrix.md) shows Gonka wins on sessions and tiering, but those wins are invisible to developers who cannot discover, evaluate, or sign up for the service.

Six additional gaps can be deferred past initial GTM launch, including single-model limitation, JSON key storage, TF-IDF search quality, GPU load balancing, developer dashboard, and SLA guarantees.

---

## Landscape Segmentation Framework

The inference provider landscape is mapped onto a 2x2 grid using two structural axes that determine how providers compete:

**X-axis: Single Provider vs Multi-Provider Router.** Single providers serve their own models on their own (or contracted) infrastructure. Multi-provider routers aggregate access to multiple upstream providers through a unified API. This distinction matters because routers compete on breadth and convenience while single providers compete on cost, performance, and unique capabilities.

**Y-axis: Centralized vs Decentralized Infrastructure.** Centralized providers operate their own data centers or lease cloud capacity (AWS, GCP, Azure). Decentralized providers distribute compute across independent GPU hosts incentivized by token economics. This distinction affects pricing structure (margin-driven vs market-driven), reliability characteristics (guaranteed SLA vs variable node quality), and regulatory positioning (single jurisdiction vs distributed).

**Third dimension overlay: Agent-Awareness.** Beyond the 2x2 grid, providers are classified by their level of agent-specific functionality:
- **None:** Standard stateless inference API with no agent features
- **Partial:** Some agent-relevant features (e.g., Assistants API, prompt caching) but not designed around agent workflows
- **Native:** Purpose-built agent features (sessions, memory, tiering, webhooks) integrated into the core API

```
                    Single Provider              Multi-Provider Router
Centralized    | OpenAI [Partial],              | OpenRouter [None],
               | Anthropic [Partial],           | LiteLLM [None],
               | Google [None],                 | Portkey [Partial]
               | DeepSeek [None],               |
               | Mistral [None]                 |
---------------+--------------------------------+---------------------------
Decentralized  | GONKA [Native],                | (empty -- opportunity?)
               | Akash/AkashML [None],          |
               | SaladCloud [None],             |
               | io.net [None],                 |
               | Render [None]                  |
```

The empty quadrant (Decentralized Multi-Provider Router) represents an unoccupied market position. No provider currently aggregates multiple decentralized inference networks through a single API. This could be a future opportunity for Gonka if it expands beyond K2.5 to route across multiple decentralized providers, but this is out of scope for current positioning.

---

## Segment 1: Centralized API Providers

Centralized API providers operate their own infrastructure (or lease dedicated cloud capacity) to serve proprietary and/or open-source models. They compete on model quality, reliability, and developer ecosystem integration. All five providers below are built-in to OpenClaw, meaning developers can use them with zero custom configuration.

### OpenAI

**Key strength:** Proprietary models (GPT-5.4, GPT-4o) with best-in-class tool calling and structured outputs. Brand trust built over 3+ years of API operation. Native prompt caching (50% discount on cached input tokens) directly addresses OpenClaw heartbeat costs.

**OpenClaw integration:** Built-in. Set `OPENAI_API_KEY` environment variable and models are available immediately. Zero configuration required.

**Agent-relevant features:** Assistants API provides thread-based state management (partial agent-awareness). Function calling with guaranteed JSON schema compliance. Prompt caching reduces heartbeat costs. No dedicated session or memory API on the chat completions endpoint.

**Threat level to Gonka: MEDIUM.** OpenAI is not a direct competitor in the traditional sense -- it serves proprietary models that Gonka does not offer. However, OpenAI's prompt caching partially substitutes for Gonka's session persistence, weakening that differentiator. OpenAI's reliability and tool calling quality set the bar that Gonka must meet. Developers using OpenAI are unlikely to switch to Gonka entirely but may add Gonka for cost-optimized K2.5 inference on specific tasks.

### Anthropic

**Key strength:** Claude Opus 4 and Sonnet 4 for strong reasoning and tool use. Aggressive prompt caching economics (90% discount on cached tokens, 25% write premium) make Anthropic the most cost-effective provider for repeated-context workloads despite premium per-token rates.

**OpenClaw integration:** Built-in. Set `ANTHROPIC_API_KEY` environment variable.

**Agent-relevant features:** Strong tool use (beta structured outputs). Prompt caching is the most aggressive in the market for repeat-context patterns. No session management, no memory API.

**Threat level to Gonka: LOW.** Anthropic's premium pricing ($15/$75 per 1M tokens for Opus 4) positions it at the opposite end of the cost spectrum from Gonka. Developers choosing Anthropic prioritize model quality over cost. Gonka's competition with Anthropic is limited to the specific case where developers want to replace Claude with K2.5 for cost savings on tasks where K2.5's quality is sufficient.

### Google

**Key strength:** Gemini 3.x models with generous free tier and strong multimodal capabilities. Google Cloud integration for enterprise customers.

**OpenClaw integration:** Built-in. Set `GOOGLE_API_KEY` environment variable.

**Agent-relevant features:** Function calling. No dedicated agent features.

**Threat level to Gonka: LOW.** Google competes on ecosystem (GCP integration) and free tier generosity, neither of which overlaps with Gonka's positioning.

### DeepSeek

**Key strength:** Ultra-competitive pricing ($0.55/$2.19 per 1M tokens for V3.2) with strong model performance. Chinese origin may be a concern for some enterprise users but a non-issue for individual developers focused on cost.

**OpenClaw integration:** Built-in. Set `DEEPSEEK_API_KEY` environment variable.

**Agent-relevant features:** Tool calling support. No dedicated agent features.

**Threat level to Gonka: MEDIUM.** DeepSeek competes directly on the cost dimension that Gonka targets. If Gonka's per-token pricing cannot beat DeepSeek's rates, the cost advantage narrative weakens. DeepSeek's V3.2 is a viable alternative to K2.5 for many agent tasks.

### Mistral

**Key strength:** European hosting options for data residency requirements. Open-weight model options. Strong performance on coding and reasoning tasks.

**OpenClaw integration:** Built-in. Set `MISTRAL_API_KEY` environment variable.

**Agent-relevant features:** Function calling. No dedicated agent features.

**Threat level to Gonka: LOW.** Mistral occupies a niche (European hosting, open-weight) that does not directly compete with Gonka's positioning.

**Segment summary:** All five centralized providers are built-in to OpenClaw, creating zero-friction developer access. Gonka's challenge is not to displace these providers but to earn a slot alongside them -- first as a custom provider, then as a built-in option. The centralized segment's primary advantage over Gonka is ecosystem integration (already in OpenClaw), not features.

---

## Segment 2: Multi-Provider Routers

Multi-provider routers aggregate access to multiple upstream inference providers through a unified API. They compete on model breadth, convenience, and developer experience. OpenRouter is the primary competitive threat to Gonka among all providers across all segments.

### OpenRouter (PRIMARY COMPETITOR)

**Key strength:** 500+ models from all major providers accessible through a single API key. Built-in to OpenClaw with zero configuration. Acts as a discovery layer -- developers can try any model without creating accounts with individual providers.

**OpenClaw integration:** Built-in. Set `OPENROUTER_API_KEY` environment variable. Models are browsable and selectable within OpenClaw's interface. OpenRouter is the de facto default multi-model provider for OpenClaw developers who want model flexibility.

**Why OpenRouter is the real competitive threat:** OpenRouter and Gonka compete for the same developer at the same decision point: "I'm building an OpenClaw agent and need an inference provider." OpenRouter's advantages are formidable:

1. **Zero-config integration.** OpenRouter is built into OpenClaw. Gonka requires manual JSON provider configuration. This integration gap alone determines the default choice for developers who do not actively seek alternatives.

2. **Model breadth as moat.** OpenRouter provides access to 500+ models including the same K2.5 that Gonka serves (via upstream providers like Together AI and DeepInfra). A developer using OpenRouter already has K2.5 access plus every other model. Switching to Gonka means losing 499 models to gain sessions and tiering.

3. **Established ecosystem.** OpenRouter has multi-year operational history, developer trust, and community adoption within OpenClaw. Gonka is unknown.

4. **Pricing transparency.** OpenRouter publishes per-model pricing for all 500+ models. The 5.5% credit markup is documented. A developer can estimate costs before writing any code. Gonka has no published pricing.

**OpenRouter's weaknesses (where Gonka can compete):**

1. **Stateless passthrough.** OpenRouter maintains no server-side state between requests. No sessions, no memory, no context management. For agent workloads with frequent heartbeats, this means full context re-transmission on every call with no cost mitigation (OpenRouter does not offer prompt caching -- that is the upstream provider's feature).

2. **No automatic tiering.** OpenRouter lets developers choose models but does not auto-route based on task complexity. The developer must build all routing logic client-side.

3. **5.5% hidden markup.** OpenRouter's credit purchase system adds a 5.5% cost layer that is not immediately visible in per-model pricing comparisons.

4. **No unique infrastructure.** OpenRouter routes to other providers' infrastructure. It does not control reliability, latency, or availability. When upstream providers degrade, OpenRouter's service degrades.

**Competitive dynamics:** Gonka's viable path against OpenRouter is not to replace it entirely but to demonstrate that for agent-heavy workloads, the combination of sessions + tiering + potential cost savings (once pricing is set) justifies the manual configuration overhead. The secondary path is to become a built-in OpenClaw provider, eliminating the configuration gap entirely.

**Threat level to Gonka: HIGH.** OpenRouter occupies the exact market position Gonka wants: the default inference provider for OpenClaw developers. Displacing a built-in default requires compelling, demonstrable advantages.

### LiteLLM

**Key strength:** Open-source Python proxy that provides a unified OpenAI-compatible interface across 100+ LLM providers. Self-hosted, so developers maintain full control. Supports load balancing, fallbacks, and spend tracking.

**OpenClaw integration:** Community integration available. Not built-in but widely used by developers who want self-hosted routing.

**Agent-relevant features:** Load balancing across providers, automatic fallback on failures, budget limits. No agent-specific features (sessions, memory).

**Threat level to Gonka: LOW.** LiteLLM is self-hosted middleware, not an inference provider. It could route to Gonka, making it complementary rather than competitive. Developers using LiteLLM are typically more sophisticated and may evaluate Gonka on its merits.

### Portkey

**Key strength:** AI gateway with guardrails, observability, caching, and automatic retries. Enterprise-focused with compliance features.

**OpenClaw integration:** Not integrated.

**Agent-relevant features:** Request caching, automatic retries with fallbacks, prompt guardrails. Partial agent-awareness through caching and reliability features but no dedicated session or memory management.

**Threat level to Gonka: LOW.** Portkey is an enterprise infrastructure layer. It targets larger organizations needing governance and observability, not individual OpenClaw developers.

**Segment summary:** OpenRouter is the critical competitor in this segment. Its built-in OpenClaw integration and 500+ model catalog create the highest competitive barrier Gonka faces. LiteLLM and Portkey are complementary (could route to Gonka) rather than directly competitive.

---

## Segment 3: Dedicated Inference

Dedicated inference providers operate their own GPU infrastructure (purchased or leased) to serve models with optimized price-performance. They compete on per-token cost, latency, and model availability.

### Together AI

**Key strength:** Operates its own H100/H200/B200 GPU clusters with no middleman cloud margin. Verified cheapest K2.5 inference at $0.50/$2.50 per 1M tokens (source: together.ai/pricing). 200+ open models including Llama 4, K2.5, and fine-tuning support. Batch inference for cost-optimized non-realtime workloads.

**OpenClaw integration:** Not built-in. Custom provider configuration required (similar friction to Gonka).

**Agent-relevant features:** None beyond standard OpenAI-compatible API. No sessions, memory, tiering, or caching features.

**Threat level to Gonka: MEDIUM.** Together AI is the pricing benchmark for K2.5 inference. If Gonka cannot match or beat $0.50/$2.50 per 1M tokens, the decentralized cost advantage narrative collapses. Together AI's lack of agent features is Gonka's opening, but Together AI's pricing + model breadth (200+) vs Gonka's single model creates a compelling alternative for cost-focused developers.

**NVIDIA Blackwell GPU impact:** Together AI is among the first providers deploying Blackwell B200 GPUs, which deliver up to 10x cost-per-token reduction compared to H100 (source: NVIDIA GTC 2026 presentation, blogs.nvidia.com). This means Together AI's already-low prices are likely to decrease further in 2026, narrowing any cost advantage from Gonka's decentralized compute structure.

### Groq

**Key strength:** Custom LPU (Language Processing Unit) hardware, now backed by NVIDIA's $20B technology licensing deal (December 2025). Ultra-low latency: 0.13s time-to-first-token on compatible models. Groq 3 LPU unveiled at GTC 2026 with 150 TB/s memory bandwidth. Sets the latency benchmark for the industry.

**OpenClaw integration:** Not built-in. Custom provider configuration required.

**Agent-relevant features:** None beyond standard API. Speed-optimized but no agent-specific extensions.

**Threat level to Gonka: LOW.** Groq competes on latency, which is not Gonka's positioning. Groq does not serve K2.5 currently. For agent developers who prioritize speed (e.g., real-time conversational agents), Groq is compelling but serves a different use case than Gonka's agent-infrastructure positioning.

### DeepInfra

**Key strength:** Cost-efficient managed inference. K2.5 at $0.45/$2.25 per 1M tokens -- the lowest verified K2.5 price among all providers (source: Artificial Analysis). Serverless endpoints with auto-scaling.

**OpenClaw integration:** Not built-in. Custom provider configuration.

**Threat level to Gonka: MEDIUM.** DeepInfra's K2.5 pricing at $0.45/$2.25 undercuts even Together AI. For pure K2.5 inference cost, DeepInfra may be the cheapest option, making Gonka's cost advantage even harder to establish.

### Fireworks AI

**Key strength:** Low latency focus with optimized structured output generation. Strong function calling performance. Competitive pricing.

**OpenClaw integration:** Not built-in. Custom provider configuration.

**Agent-relevant features:** Optimized structured output (relevant for tool calling). No dedicated agent features.

**Threat level to Gonka: LOW.** Fireworks competes on latency and structured output quality, not on agent infrastructure.

### SiliconFlow

**Key strength:** Benchmarked as best overall value across price-performance metrics (source: siliconflow.com analysis). Managed infrastructure.

**OpenClaw integration:** Not built-in. Custom provider configuration.

**Threat level to Gonka: LOW.** Niche provider without OpenClaw presence.

**Segment summary:** Together AI and DeepInfra set the cost benchmarks that Gonka must meet or beat. Blackwell GPU deployment by these providers will push per-token costs down further in 2026. Gonka's differentiation against this segment must be agent-specific features, not price alone.

---

## Segment 4: Decentralized GPU Networks

Decentralized GPU networks distribute inference compute across independent GPU operators, typically incentivized by token economics. They compete on cost (no central margin), censorship resistance, and geographic distribution. This is Gonka's home segment.

### Gonka (Current Position)

**Key strength:** The only decentralized provider with agent-native API extensions. Server-side sessions (/v1/sessions), persistent memory (/v1/memory with TF-IDF search), automatic model tiering (X-Gonka-Tier header), webhook notifications, and multi-model routing -- all built on an OpenAI-compatible API. Sprint Consensus uses 98% of GPU compute for productive inference (2% for consensus), compared to traditional PoW chains that waste 100% on hashing. Kimi K2.5 as flagship model with 76.8% SWE-Bench, native Agent Swarm capability, and 131K context window.

**OpenClaw integration:** NOT built-in. Requires manual JSON provider configuration:
```json
{
  "models": {
    "providers": {
      "gonka": {
        "baseUrl": "https://api.gonka.ai/v1",
        "apiKey": "${GONKA_API_KEY}",
        "api": "openai-completions",
        "models": [{ "id": "kimi-k2.5", "contextWindow": 131072 }]
      }
    }
  }
}
```
This configuration requirement is the single highest-friction barrier to adoption, as detailed in the gap analysis below.

**Agent-relevant features:** Native -- purpose-built for agent workloads. Sessions persist across requests (no context re-send). Tiering auto-routes to cost-optimal model variant. Memory API provides long-term key-value storage. Webhooks enable fire-and-forget async patterns. These features exist nowhere else in the decentralized segment.

**Unique position:** Gonka sits at the intersection of two attributes that no other provider combines: decentralized infrastructure AND agent-native features. Centralized providers offer some agent features (OpenAI Assistants, prompt caching) but not decentralization. Decentralized providers offer compute but not agent features. Gonka is the only provider in the matrix below that has both.

### Akash / AkashML (Closest Decentralized Competitor)

**Key strength:** The most mature decentralized compute platform. Kubernetes-as-a-Service with reverse auction pricing. 65 datacenters globally. In November 2025, launched AkashML -- a managed AI inference service with an OpenAI-compatible API. This was a significant shift: Akash moved from raw GPU rental to managed inference, directly competing with Gonka's positioning.

**OpenClaw integration:** Not built-in. Custom provider configuration required. AkashML's OpenAI-compatible API means the same configuration pattern works as for Gonka.

**Agent-relevant features:** None. AkashML provides standard OpenAI-compatible inference endpoints but no sessions, memory, tiering, or webhooks. Raw Akash compute is even further from agent-awareness -- developers deploy their own inference stack.

**Competitive dynamics with Gonka:** AkashML is Gonka's closest decentralized competitor because both offer:
- OpenAI-compatible inference API
- Decentralized infrastructure with token incentives
- Lower cost than centralized providers (Akash via reverse auction, Gonka via mining subsidies)

However, AkashML's model catalog, current pricing, and uptime statistics are not well-documented publicly (research confidence: LOW). What is clear is that AkashML lacks any agent-specific features -- no sessions, no memory, no tiering. This gap is Gonka's primary differentiator within the decentralized segment.

**Threat level to Gonka: MEDIUM.** AkashML is the competitor most likely to copy Gonka's agent features. If AkashML adds sessions and memory to its managed inference API, Gonka's decentralized differentiator weakens significantly. The window for Gonka to establish itself as the agent-native decentralized provider is time-sensitive.

### io.net

**Key strength:** Scale -- self-reported 300K+ GPUs across 55+ countries. Largest decentralized GPU inventory. Token incentive model attracts hardware operators.

**OpenClaw integration:** Not integrated. io.net provides raw GPU compute, not managed inference endpoints.

**Agent-relevant features:** None. io.net is infrastructure (raw compute), not an inference API.

**Threat level to Gonka: LOW.** io.net does not compete at the inference API layer. It could theoretically become a compute substrate that Gonka routes to, making it potentially complementary rather than competitive.

### Render

**Key strength:** GPU rendering focus with some inference capabilities. Established in the creative/rendering market.

**OpenClaw integration:** Not integrated. Not agent-focused.

**Agent-relevant features:** None.

**Threat level to Gonka: LOW.** Render is focused on rendering workloads, not agent inference. Minimal competitive overlap.

### SaladCloud

**Key strength:** Consumer GPU aggregation for cost-efficient compute. Notably, SaladCloud has published OpenClaw-specific integration guides -- the only decentralized provider besides Gonka to explicitly target the OpenClaw developer audience.

**OpenClaw integration:** Not built-in, but has published guides for OpenClaw integration (source: .planning/research/STACK.md).

**Agent-relevant features:** None. Cost optimization only.

**Threat level to Gonka: LOW-MEDIUM.** SaladCloud's explicit OpenClaw targeting is noteworthy. While it lacks agent features, its OpenClaw guides indicate awareness of the same target market. If SaladCloud adds managed inference with agent features, it becomes a competitor.

**Segment summary:** Gonka's decentralized segment position is unique and defensible in the near term. No other decentralized provider offers agent-native extensions. AkashML is the closest competitor with its OpenAI-compatible managed inference API but lacks agent features. SaladCloud's OpenClaw-specific guides indicate that the OpenClaw developer market is attracting attention from other decentralized providers. The window for Gonka to establish category leadership is time-sensitive.

---

## Competitive Positioning Summary

**Where Gonka wins:**
- Agent-native features (sessions, memory, tiering, webhooks) that no other provider -- centralized or decentralized -- matches in combination
- Only decentralized provider with OpenAI-compatible API AND agent extensions
- Sprint Consensus 98% productive compute creates genuine economic efficiency vs PoW chains
- K2.5 as flagship agent model (76.8% SWE-Bench, native Agent Swarm) is a credible model choice for agent workloads

**Where Gonka loses:**
- Not built-in to OpenClaw (vs OpenRouter, OpenAI, Anthropic, Google, DeepSeek, Mistral -- all zero-config)
- Single model (K2.5 in 3 quants) vs OpenRouter's 500+ and Together AI's 200+
- No reliability track record or SLA (vs OpenAI's 99.9%+ SLA)
- No published pricing (vs every competitor having transparent, published rates)
- Missing table-stakes developer infrastructure: no docs site, no self-serve signup, no pricing page

**What determines the outcome:**
Gonka does not need to compete on model breadth or match OpenAI's reliability track record at launch. Gonka needs to demonstrate that for the specific use case of OpenClaw agent developers who run multi-step agent workflows with heartbeats and tool calling, the combination of server-side sessions + automatic tiering + decentralized cost structure delivers measurably better outcomes than OpenRouter or direct provider access. This requires:
1. Closing the table-stakes gaps (docs, signup, pricing) so developers can evaluate the proposition
2. Publishing verifiable pricing that demonstrates cost savings on realistic agent workloads
3. Establishing minimum reliability credibility (published uptime stats, transparent status page)
4. Becoming a built-in OpenClaw provider to eliminate configuration friction

As shown in the feature matrix (gonka_competitive_feature_matrix.md), Gonka's WIN dimensions (sessions, tiering) are genuinely unique. But unique features matter only if developers can discover, evaluate, and adopt them -- which is currently gated by the infrastructure gaps below.

---

## Gap Analysis: Must Close Before GTM Push

These five gaps must be resolved before any external marketing, developer outreach, or partnership conversations. They represent table-stakes infrastructure that every competitor already has. Without these, developers literally cannot evaluate Gonka.

| Gap | Why Critical | v1.2 Tech Debt? | Competitive Impact | Priority |
|-----|-------------|-----------------|-------------------|----------|
| **Not a built-in OpenClaw provider** | Every Gonka user must manually configure JSON provider settings. OpenRouter, OpenAI, Anthropic, Google, DeepSeek, and Mistral are all zero-config. This is the single highest-friction barrier -- developers who do not actively seek Gonka will never encounter it. | No | CRITICAL: Gonka is invisible to the ~95% of OpenClaw developers who use default providers | P0 |
| **No public documentation site** | Developers cannot evaluate Gonka without documentation. No quickstart guide, no API reference, no migration guide, no troubleshooting section. The v1.2 codebase has inline documentation but no developer-facing documentation site. Every compared provider has docs.provider.com as a minimum. | No | CRITICAL: Developers make provider decisions based on documentation quality; no docs = no evaluation | P0 |
| **No self-serve API key signup** | Current key provisioning is manual (admin API, direct configuration). No self-service signup flow, no GitHub OAuth, no email registration. OpenAI: sign up in 30 seconds. OpenRouter: sign up in 30 seconds. Gonka: contact someone? The conversion funnel cannot exist without self-serve signup. | No | CRITICAL: Every unconverted developer who cannot self-serve is a permanently lost prospect | P0 |
| **No public pricing page** | Gonka's per-token pricing is TBD. No pricing page, no cost calculator, no comparison table. Developers cannot estimate costs, compare against competitors, or budget for Gonka usage. The "50-70% cheaper" claim from Gonka marketing is unverifiable without published rates. Together AI prices K2.5 at $0.50/$2.50 per 1M tokens; DeepInfra at $0.45/$2.25. Gonka must publish comparable pricing data. | No | CRITICAL: Cannot execute any pricing-based messaging; cost advantage claims are empty without numbers | P0 |
| **In-memory sessions** | Sessions are stored in application memory and lost on server restart. This is Gonka's primary differentiator (WIN in feature matrix) but the implementation has a production reliability flaw: any restart, deploy, or crash destroys all active sessions. For agent developers who adopt sessions as a core workflow pattern, data loss on restart is unacceptable and would damage trust irreparably at first occurrence. | YES (v1.2 tech debt) | HIGH: Undermines the feature that most differentiates Gonka from all competitors; first session loss event destroys developer trust | P1 |

**"Closed" definition for each gap:**

1. **Built-in OpenClaw provider:** PR merged to openclaw/openclaw repo adding Gonka to the built-in provider list. Developers set `GONKA_API_KEY` environment variable and Gonka appears in model selection without JSON configuration. Interim milestone: published OpenClaw custom provider guide in Gonka docs with copy-paste YAML snippet.

2. **Public documentation site:** docs.gonka.ai live with: quickstart guide (< 5 min to first API call), API reference (all endpoints documented), OpenClaw integration guide, migration guide from OpenRouter, pricing page (when available), status page. Minimum viable: 10 pages covering the developer journey from discovery to first successful inference.

3. **Self-serve API key signup:** Web form at api.gonka.ai with email + GitHub OAuth. Developer receives API key immediately after signup. No manual approval step. Free tier activated automatically with rate limits. Stretch goal: API key creation via CLI (`gonka auth login`).

4. **Public pricing page:** gonka.ai/pricing with per-token rates for K2.5 (all quantization tiers), comparison table against OpenRouter/Together AI/DeepInfra, cost calculator for OpenClaw agent workloads (input: messages/day, heartbeat interval; output: estimated monthly cost), and free tier limits.

5. **Persistent sessions:** Sessions stored in Redis or equivalent distributed cache. Sessions survive server restarts. TTL-based expiration with configurable retention. Session state replicated across nodes for high availability.

---

## Gap Analysis: Can Defer

These six gaps are real competitive disadvantages but do not block initial GTM efforts targeting early adopter developers. They should be addressed according to the timeline below.

| Gap | Why Deferrable | v1.2 Tech Debt? | When to Address | Priority |
|-----|---------------|-----------------|-----------------|----------|
| **Single model (K2.5 only, 3 quants)** | Position as "the best K2.5 agent experience" rather than "every model." Early adopters choosing Gonka specifically want K2.5 agent features, not model breadth. Add 1-2 additional models (Llama 4, DeepSeek V3) when scaling to Active/Heavy user tiers. | No | Before Active/Heavy user tier launch (3-6 months post-GTM) | P2 |
| **JSON key storage** | Current API keys stored in JSON file. Security concern at scale (no hashing, no rotation, no scoping) but acceptable for early adopter phase with < 100 keys. Enterprise users will require proper key management. | YES (v1.2 tech debt) | Before enterprise outreach or > 100 active API keys | P2 |
| **TF-IDF search (not vector embeddings)** | Memory API works but recall quality is lower than vector-based approaches. For early adopters, keyword-based memory retrieval is functional. Quality gap becomes apparent when developers compare memory recall against OpenAI's native prompt caching or build sophisticated memory-dependent agent workflows. | YES (v1.2 tech debt) | Before marketing memory feature as a primary differentiator; implement vector embeddings | P3 |
| **No GPU load balancing** | Single-node inference routing. OK for early traffic (< 10 concurrent users per node). Performance degradation begins at higher concurrency as requests queue on a single vLLM instance. | YES (v1.2 tech debt) | Before > 10 concurrent users per inference node | P2 |
| **No developer dashboard** | Admin API exists for usage stats, key management, model health, and session management. No web-based developer dashboard. CLI/API-first is acceptable for early developer adopters who are comfortable with curl and command-line tools. Dashboard becomes important when non-technical team members need spend visibility. | No | Before Active tier users need self-serve spend visibility (3-6 months post-GTM) | P3 |
| **No SLA guarantee** | No formal uptime commitment. Early adopters tolerate best-effort reliability if the features are compelling and the price is right. Enterprise and startup users require SLA terms with credits for downtime. Alternative: publish transparent uptime statistics (actual measured uptime, p95 latency) instead of promising SLA terms. | No | Before enterprise/startup outreach; publish uptime stats as interim measure | P3 |

---

## Recommendations for Phases 16-20

This landscape analysis and gap identification should directly inform the downstream phases of the v1.3 GTM research milestone.

**Phase 16 (Developer Personas & Journey Mapping):** The primary pain point for each persona should be validated against OpenRouter as the default alternative, not OpenAI or Anthropic. When mapping the developer journey, the key friction point is not "which model do I choose?" but "why should I configure a custom provider (Gonka) when the built-in option (OpenRouter) already works?" Persona pain points should center on what OpenRouter fails to deliver (sessions, tiering, cost optimization for agent workloads) rather than what OpenAI or Anthropic lack.

**Phase 17 (Positioning & Messaging):** Lead with agent-native features, not decentralization or cost. The feature matrix shows Gonka wins on sessions and tiering -- two dimensions that directly address the most expensive patterns in OpenClaw agent workloads. Messaging should be: "Your agents remember context without paying for it twice. Your agents use the right model for each task automatically. And it costs less because the infrastructure has no central margin." Decentralization is the mechanism, not the headline benefit. Cost is a supporting point, contingent on published pricing.

**Phase 19 (Partnership & Ecosystem Strategy):** Getting Gonka added as a built-in OpenClaw provider is the single highest-impact GTM action identified in this analysis. The must-close gap analysis shows that built-in status eliminates the configuration friction that is the #1 barrier to developer adoption. The partnership strategy should define a concrete path from current state (custom JSON config) to built-in provider (environment variable only), including the technical requirements for an OpenClaw PR, the community engagement needed, and the timeline.

**Phase 20 (Product-Led Growth & v1.4 Backlog):** The must-close gaps define the minimum viable GTM checklist. The v1.4 engineering backlog should be ordered exactly as the must-close gaps: (1) public docs site, (2) self-serve API key signup, (3) pricing page with cost calculator, (4) persistent sessions (Redis migration), (5) OpenClaw built-in provider PR. Items 1-4 are engineering prerequisites; item 5 is a community/partnership action that can proceed in parallel. The can-defer gaps should be ranked in the v1.4 backlog but explicitly excluded from the GTM launch checklist.

---

## Source Citations

| Source | Used For | Confidence |
|--------|----------|------------|
| .planning/research/STACK.md | OpenClaw provider architecture, competitive pricing, community channels | HIGH |
| .planning/research/FEATURES.md | Feature landscape, decision criteria, competitive gaps | HIGH |
| .planning/research/ARCHITECTURE.md | GTM framework, competitive segments, partnership tiers, anti-patterns | HIGH |
| .planning/research/PITFALLS.md | Trust barriers, recovery strategies, crypto-jargon avoidance | HIGH |
| .planning/PROJECT.md | v1.2 tech debt list, infrastructure capabilities, key decisions | HIGH |
| gonka_competitive_feature_matrix.md | Feature comparison verdicts, session/tiering WIN analysis | HIGH |
| Akash 2025 Year in Review (akash.network/blog) | AkashML launch Nov 2025, 65 datacenters, managed inference | MEDIUM |
| NVIDIA GTC 2026 / Blackwell inference blog (blogs.nvidia.com) | 10x cost-per-token reduction for Blackwell-equipped providers | MEDIUM |
| NVIDIA Groq acquisition / Groq 3 LPU | $20B licensing deal Dec 2025, 150 TB/s bandwidth, 0.13s TTFT | MEDIUM |
| io.net vs Akash vs Render comparison (io.net/blog) | Decentralized GPU network capabilities and limitations | MEDIUM |
| DePIN Compute Wars 2026 (cryptollia.com) | Decentralized provider landscape overview | MEDIUM |
| SaladCloud OpenClaw guides | SaladCloud's OpenClaw-specific documentation | MEDIUM |
| OpenRouter pricing and integration docs | 5.5% credit markup, built-in OpenClaw status | MEDIUM |
| Together AI pricing page | K2.5 at $0.50/$2.50, Llama 4 Maverick at $0.27/$0.85 | MEDIUM |
| Artificial Analysis (artificialanalysis.ai) | Multi-provider K2.5 pricing comparison, DeepInfra at $0.45/$2.25 | MEDIUM |
| OpenClaw custom provider configuration (haimaker.ai) | Custom provider JSON config walkthrough | MEDIUM |

---

*Document: gonka_provider_landscape_map.md | Version 1.0 | 2026-04-01*
*Companion document: gonka_competitive_feature_matrix.md (feature comparison matrix with Win/Lose/Tie scoring)*

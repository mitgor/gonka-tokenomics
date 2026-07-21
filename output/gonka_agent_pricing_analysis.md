# Gonka Agent Workload Pricing Analysis

**Version:** 2.0
**Date:** 2026-07-18 (supersedes v1.0, 2026-04-01)
**Classification:** Internal -- for leadership decision-making
**Requirement:** COMP-02

---

## 1. Executive Summary

OpenClaw agent workloads cost 3-10x more than equivalent chatbot interactions due to three compounding factors: heartbeat context resending (full system prompt + workspace context resent every 30 minutes = 48 calls/day minimum), multi-step tool call chains (3-10 tool calls per user message), and always-on operation (agents run 24/7, not on-demand). **The dominant cost driver is heartbeats, not message volume.** A single agent with 30-minute heartbeats consumes 461K tokens/day on heartbeats alone -- nearly equal to 50 user messages worth of tokens.

This analysis models three realistic OpenClaw agent workload tiers (Casual, Active, Heavy) across the current provider landscape: OpenRouter, DeepInfra, Together AI, DeepSeek, OpenAI, Anthropic, and Gonka.

**What changed since v1.0 (April 2026):**

- **Gonka pricing is now live and published -- but the network rate and the broker retail rate are very different numbers.** The v1.0 hypothetical Scenarios A/B/C ($0.25-$0.45 per 1M input) are obsolete. Gonka's network charges a single blended per-token rate recalculated every block from network utilization -- recently ~$0.0003 per 1M tokens on trackers, effectively near-zero because the network is underutilized and partly subsidized. That is NOT what developers pay: access is resold by third-party brokers (GonkaGate, JoinGonka, OpenGNK, GonkaBroker, Gonka24), and published broker retail now spans from JoinGonka's itemized $0.003 input / $0.009 output per 1M for Kimi K2.6, to Gonka24's model-specific rate card (MiniMax M2.7 $0.018/$0.072; Kimi K2.6 $0.055/$0.32; GLM-5.2 $0.095/$0.30 per 1M), to GonkaBroker's $0.30-$0.35 per 1M flat ($0.30 MiniMax M2 family, $0.35 Kimi K2 family, input=output, fixed at top-up). Note Gonka24's headline $0.018/$0.072 is the M2.7 "from" price only, not a network-wide rate. OpenGNK's earlier ~$0.00016 near-passthrough figure could not be re-verified in July and current gateway comparisons describe proxy.gonka.gg as ~133% more expensive than other Gonka gateways under a "temporary pricing adjustment" -- do not treat it as the floor. Gonka is still listed as the cheapest provider for Kimi K2.6 and MiniMax M2.7 on price trackers -- at broker rates, not at $0.0003.
- **Gonka's model lineup churned hard in late June/July 2026.** Proposal 78 (Jun 25, 2026) removed BOTH Qwen3 235B (retired for good) and Kimi K2.6 (lost validation majority), making MiniMax M2.7 the sole PoC/base model. Proposal 79 (Jun 26) restored Kimi K2.6 at weight_scale_factor 0.9 (re-bootstrapped at epoch 311 on Jun 27) and approved GLM-5.2 (Z.ai; 1M context, open weights; weight factor 2.47, optional with no participation penalty) -- though GLM-5.2's serving status remains ambiguous as of mid-July: Gonka24 sells a rate card for it while GonkaBroker lists it "Coming soon" and Gonka's own updates page calls its status unclear. Kimi K2.6 then lost validation majority AGAIN in epochs 328-329 (concentrated guardian delegations plus provider failures), was removed via expedited Proposal 87 (Jul 15) and re-registered via Proposal 88 (Jul 16) for its second re-bootstrap, at epoch 331, keeping the 0.9 weight factor set in June. The live lineup as of Jul 18, 2026: **MiniMax M2.7 (sole PoC/base), GLM-5.2 (approved; rollout incomplete), and Kimi K2.6 (second re-bootstrap)**. Two K2.6 validation failures in three weeks: any "cheapest K2.6 provider" claim needs a reliability caveat until K2.6 stabilizes. Network volume ~100M tokens/day combined (tracker estimate, not re-verified in July).
- **Prompt caching is now effectively universal.** OpenAI (90% cached-input discount), Anthropic (90%), Google, Together AI (default-on, 5-10x), DeepInfra, DeepSeek (cache-hit ~98% off), Moonshot's own API, and OpenRouter (passthrough) all discount cached input. The v1.0 narrative -- "heartbeat resending is unoptimized everywhere except Gonka sessions" -- no longer holds. Session persistence remains an architectural advantage, but its dollar delta versus cached competitors is much smaller than the 60-84% savings v1.0 claimed.
- **The model landscape moved.** Kimi K2.5 has been superseded by K2.6 (Apr 20, 2026), K2.7-Code (Jun 12, 2026), and Kimi K3 (launched via app/API Jul 16, 2026; open weights due ~Jul 27, expected under Moonshot's Modified MIT license). K2.5 is now formally on the way out: Moonshot's platform docs close it to newly registered users, redirect K2.5 API traffic to K2.6, and schedule full platform sunset for August 31, 2026 -- Moonshot's first-party K2.5 rate is no longer a purchasable price, and third-party K2.5 hosting carries acute lifecycle risk. DeepSeek's Apr 24 "V4" was a Preview; the official V4 lands mid-July 2026 with China's first time-of-day API pricing -- rates DOUBLE during Beijing peak hours (9:00-12:00, 14:00-18:00) -- and legacy deepseek-chat/deepseek-reasoner endpoints retire after July 24, 2026 (see Section 4). MiniMax released M3 (Jun 1, 2026; downloadable weights on Hugging Face under the commercially restricted MiniMax Community License -- attribution required, prior authorization above $20M/yr revenue) as its new flagship above M2.7, keeping small-active-params serving economics (428B total / 23B active); mid-July reporting (The Information, single-sourced) says a 2.7T-parameter "M3 Pro" may open-source as early as Q3 2026. GPT-4o is retired; OpenAI's lineup is GPT-5.4/5.5/5.6, with GPT-5.6 GA since Jul 9, 2026 at published Sol/Terra/Luna tier pricing. Google added Gemini 3.5 Flash (May 19, 2026) at $1.50/$9.00 standard -- the $0.75/$4.50 rate widely reported as a "price cut" is the Batch/Flex tier (a standing 50%-off non-interactive tier), not the interactive rate; July coverage frames 3.5 Flash as ~3x the cost of the model it replaced. Anthropic's lineup is Opus 4.8, Sonnet 5, Haiku 4.5, and Claude Fable 5 -- with Opus-class pricing down 3x from the $15/$75 that v1.0 used, and a material reliability event: Fable 5 and Mythos 5 were offline June 12 - July 1, 2026 under a US Commerce Department export-control order.

**Key findings (July 2026):**

- At published broker retail rates, Gonka is roughly 3-50x cheaper than the cheapest centralized hosts of the same models -- not the "2-3 orders of magnitude" a raw network-rate reading suggests. Heavy tier (~2.94B tokens/month) costs ~$132/month via Gonka24 if the workload runs on MiniMax M2.7, ~$550/month on Kimi K2.6 at Gonka24's model-specific rate, or ~$880-$1,030 via GonkaBroker, versus ~$2,800-$3,800 on cached centralized K2.6 hosts. Any figure built on the earlier "$0.018/$0.072 flat across all Gonka models" assumption understates K2.6 cost ~4x. The underlying network rate is utilization-driven and partly subsidized; it will rise as the network fills, and leadership should not market it as a stable rate.
- K2.5 should no longer anchor any comparison: Moonshot has closed it to new users and scheduled platform sunset for Aug 31, 2026, so its former first-party rate ($0.60/$3.00) is not a current purchasable price. Third-party hosts still serve it (OpenRouter $0.375/$2.025, DeepInfra $0.45/$2.25) with ~6 weeks of shelf life and lifecycle risk. The current-generation anchor is K2.6: OpenRouter is cheapest at $0.66/$3.41 -- undercutting DeepInfra ($0.75/$3.50) on both input and output and Moonshot's first-party $0.95/$4.00 (cache-hit input ~$0.16/M). Any "cheapest centralized K2.6" anchor in Gonka savings math should use $0.66 input, not $0.75.
- With caching universal, the session-persistence savings pitch must be recomputed against cached baselines, including Moonshot's own cached-input pricing (Kimi K3: $0.30/M cached vs $3.00/M uncached). The advantage shrinks substantially but does not disappear: sessions have no TTL, no cache-write premium (both Anthropic and now OpenAI charge write premiums on explicit caching -- 25% and 1.25x respectively), and eliminate resending entirely rather than discounting it.

**Cross-reference:** See `output/gonka_competitive_feature_matrix.md` for the feature matrix comparing Gonka across agent-relevant dimensions including pricing model. (Note: the matrix's Memory/caching verdicts for Together AI and OpenRouter predate universal caching and need the same July 2026 re-run applied here.)

---

## 2. Methodology

### Why Per-Task Cost Matters More Than Per-Token Cost

Traditional inference pricing comparisons focus on $/1M tokens -- the headline rate on every provider's pricing page. This metric is misleading for agent workloads because it ignores the structural overhead that agents impose: context resending, multi-step tool chains, and always-on heartbeats.

A chatbot sends a message and receives a response. An OpenClaw agent sends a message, receives a response, executes 3-10 tool calls (each an additional LLM request), and then resends its entire context every 30 minutes regardless of whether the user sent anything. **The true cost of an agent workload is a function of architecture, not just token price.**

### How OpenClaw Agent Cost Is Calculated

Each inference call in an OpenClaw agent includes:

1. **System prompt + workspace context:** ~9,600 tokens per turn. This includes the agent's personality configuration, tool definitions, workspace state, and conversation history. Source: OpenClaw pricing guides and community analysis (aicost.org, clawback.tools). (Feb 2026 community estimate; not re-verified for current OpenClaw releases.)
2. **Heartbeat overhead:** OpenClaw agents send periodic "heartbeat" messages to maintain context and check for updates. Each heartbeat resends the full system prompt + context (~9,600 tokens). At 30-minute intervals, this is 48 heartbeats/day. At 5-minute intervals (for monitoring-heavy agents), this is 288 heartbeats/day.
3. **Tool call chains:** Each user message triggers an average of 3-10 tool calls. Each tool call is a separate LLM inference request averaging ~500 tokens input + ~200 tokens output (700 tokens total). Source: LangChain State of Agent Engineering report; OpenClaw community benchmarks.

### The Three Workload Tiers

This analysis models three tiers representing real OpenClaw deployment patterns observed in community reports and pricing guides:

- **Casual:** A solo developer running one agent on one channel. Budget model, minimal heartbeats.
- **Active:** A small team running multiple agents across channels. Mixed model routing.
- **Heavy:** A business running always-on agent infrastructure. Premium models, aggressive heartbeats, high message volume.

### Assumptions

- **Input:output token ratio:** 1:1 blended unless provider-specific data indicates otherwise. Agent workloads tend to be input-heavy (large context, small responses), so actual costs may skew lower for providers with cheaper input tokens. Where this materially affects the analysis, it is noted.
- **Heartbeat tokens:** Each heartbeat resends the full system prompt + workspace context (~9,600 tokens). Raw cost tables apply no caching; caching adjustments are applied separately in Sections 5-6.
- **Tool call tokens:** Average 500 tokens input + 200 tokens output per tool call (700 tokens total). This is conservative; complex tool chains (web scraping, database queries) can be significantly higher.
- **All prices as of July 2026** unless marked otherwise. Inference pricing is volatile; figures should be revalidated before use in external communications. Gonka's rate in particular is recalculated every block and should be treated as a snapshot, not a quote.

---

## 3. Workload Tier Definitions

### Casual Tier

**Profile:** A solo developer running a personal assistant agent on Telegram or Discord.

| Parameter | Value |
|-----------|-------|
| Agents | 1 |
| Channels per agent | 1 (e.g., Telegram) |
| User messages per day | 50 |
| Heartbeat interval | 30 minutes |
| Heartbeats per day | 48 |
| Tokens per turn (system prompt + context) | ~9,600 |
| Tool calls per user message | 3 (average) |
| Tokens per tool call | ~700 (500 input + 200 output) |
| Model tier | Single model (budget tier) |

**Daily token breakdown:**

| Component | Calculation | Daily Tokens |
|-----------|-------------|-------------|
| User messages | 50 messages x 9,600 tokens | 480,000 |
| Heartbeats | 48 heartbeats x 9,600 tokens | 460,800 |
| Tool calls | 150 calls x 700 tokens | 105,000 |
| **Daily total** | | **1,045,800** |

**Monthly total:** ~31.5M tokens (1,045,800 x 30 days)

**Observation:** Heartbeats account for 44% of daily token consumption despite generating zero user-facing value. At this tier, heartbeat cost nearly equals message cost.

### Active Tier

**Profile:** A small team (e.g., crypto project, small startup) running multiple community management and support agents.

| Parameter | Value |
|-----------|-------|
| Agents | 3 |
| Channels per agent | 2 (e.g., Telegram + Discord) |
| Total channel-agents | 6 |
| User messages per day (total) | 200 |
| Heartbeat interval | 30 minutes |
| Heartbeats per day | 48 x 6 = 288 |
| Tokens per turn | ~9,600 |
| Tool calls per user message | 5 (average) |
| Tokens per tool call | ~700 |
| Model routing | 70% budget, 30% strong model |

**Daily token breakdown:**

| Component | Calculation | Daily Tokens |
|-----------|-------------|-------------|
| User messages | 200 messages x 9,600 tokens | 1,920,000 |
| Heartbeats | 288 heartbeats x 9,600 tokens | 2,764,800 |
| Tool calls | 1,000 calls x 700 tokens | 700,000 |
| **Daily total** | | **5,384,800** |

**Monthly total:** ~161.5M tokens (5,384,800 x 30 days)

**Observation:** Heartbeats now dominate at 51% of daily token consumption. With 6 channel-agents each heartbeating independently, the overhead scales linearly with channel count. Multi-model routing (70/30 split) affects cost but not token volume -- this is reflected in the cost projections.

### Heavy Tier

**Profile:** A business or DAO running production-grade agent infrastructure for customer support, monitoring, trading, or community management.

| Parameter | Value |
|-----------|-------|
| Agents | 10 |
| Channels per agent | 3 (e.g., Telegram + Discord + Web) |
| Total channel-agents | 30 |
| User messages per day (total) | 1,000+ |
| Heartbeat interval | 5 minutes (aggressive monitoring) |
| Heartbeats per day | 288 x 30 = 8,640 |
| Tokens per turn | ~9,600 |
| Tool calls per user message | 8 (average; complex workflows) |
| Tokens per tool call | ~700 |
| Model routing | Mixed: budget for simple, premium for complex |

**Daily token breakdown:**

| Component | Calculation | Daily Tokens |
|-----------|-------------|-------------|
| User messages | 1,000 messages x 9,600 tokens | 9,600,000 |
| Heartbeats | 8,640 heartbeats x 9,600 tokens | 82,944,000 |
| Tool calls | 8,000 calls x 700 tokens | 5,600,000 |
| **Daily total** | | **98,144,000** |

**Monthly total:** ~2.94B tokens (98,144,000 x 30 days)

**Observation:** Heartbeats account for **84.5%** of all token consumption at this tier. The 5-minute heartbeat interval (6x more frequent than the 30-minute default) combined with 30 channel-agents creates massive overhead. This is the tier where server-side session persistence and aggressive caching matter most.

---

## 4. Per-Provider Pricing Data

All pricing data below was gathered from provider pricing pages, aggregator sites, and independent analyses. Every figure includes its source and confidence level.

### Kimi-Family Pricing Across Providers (July 2026)

Kimi K2.5 (released Jan 2026) is now three generations behind Moonshot's lineup (K2.6 -> K2.7-Code -> K3) and formally sunsetting: Moonshot discontinued older kimi-k2-series API models on May 25, 2026, closed K2.5 to newly registered users after the K3 launch (Jul 16), redirects K2.5 API traffic to K2.6, and has scheduled full platform sunset for August 31, 2026. Together AI no longer lists K2.5 on its serverless pricing page. K2.5 rows below are retained for continuity only; all worked examples and recommendations in this revision are based on K2.6.

| Provider | Model | Input/1M | Cached Input/1M | Output/1M | Blended/1M (1:1) | Source | Confidence |
|----------|-------|----------|-----------------|-----------|------------------|--------|------------|
| OpenRouter | Kimi K2.5 | $0.375 | passthrough (10-20% of input on supported upstreams) | $2.025 | $1.20 | openrouter.ai | HIGH |
| DeepInfra | Kimi K2.5 | $0.45 | -- | $2.25 | $1.35 | Artificial Analysis | HIGH |
| Moonshot (official) | Kimi K2.5 | $0.60 (closed to new users; sunset Aug 31, 2026) | $0.10 (cache hit) | $3.00 | $1.80 | benchlm.ai / platform.kimi.ai | HIGH (rate); model delisting |
| SiliconFlow | Kimi K2.5 | $0.23 | -- | $3.00 | $1.62 | Artificial Analysis | MEDIUM |
| OpenRouter | Kimi K2.6 | $0.66 | passthrough | $3.41 | $2.04 | openrouter.ai | HIGH |
| DeepInfra | Kimi K2.6 | $0.75 | $0.15 | $3.50 | $2.13 | deepinfra.com | HIGH |
| Moonshot (official) | Kimi K2.6 | $0.95 | ~$0.16 (cache hit) | $4.00 | $2.48 | benchlm.ai / platform.kimi.ai | HIGH |
| Fireworks | Kimi K2.6 | $0.95 | -- | $4.00 | $2.48 | fireworks.ai | HIGH |
| Together AI | Kimi K2.6 | $1.20 | $0.20 | $4.50 | $2.85 | together.ai/pricing | HIGH |
| Together AI | Kimi K2.7-Code | $0.95 | $0.19 | $4.00 | $2.48 | together.ai/pricing | HIGH |
| Moonshot (official) | Kimi K2.7-Code | $0.95 | $0.19 | $4.00 | $2.48 | platform.kimi.ai | HIGH |
| Moonshot (official) | Kimi K3 | $3.00 | $0.30 | $15.00 | $9.00 | platform.kimi.ai | HIGH |

Notes: On Artificial Analysis's 3:1 input:output blend, DeepInfra is the lowest-cost K2.5 option at ~$0.90 blended per 1M (from $0.45/$2.25); SiliconFlow's cheap input does not make it cheapest on either AA's mix or this document's 1:1 assumption. K2.5 is also served by CoreWeave, Novita, ModelRun ($0.40 input), Azure, and Amazon Bedrock (fastest, ~113-185 tok/s per AA) -- all with the Aug 31 sunset lifecycle risk noted above. Together AI also serves GLM-5.2 and GLM-5.1 at $1.40/$4.40 ($0.26 cached input, identical to Z.ai's official rate) and MiniMax M3 and M2.7 at $0.30/$1.20 ($0.06 cached) -- Together belongs in any GLM-5.2 or M2.7 centralized-host comparison set.

### Budget and Frontier Model Pricing (July 2026)

| Provider | Model | Input/1M | Cached Input/1M | Output/1M | Blended/1M (1:1) | Source | Confidence |
|----------|-------|----------|-----------------|-----------|------------------|--------|------------|
| DeepSeek | V4 Flash | ~$0.14 off-peak (~$0.28 Beijing peak) | $0.0028 (cache hit) | ~$0.28 off-peak (~$0.56 peak) | $0.21 off-peak | api-docs.deepseek.com / TechNode | HIGH |
| DeepSeek | V4 Pro | ~$0.42 off-peak (~$0.84 Beijing peak) | ~¥0.025 (cache hit) | ~$0.84 off-peak (~$1.68 peak) | $0.63 off-peak | api-docs.deepseek.com / TechNode | HIGH |
| MiniMax (official) | MiniMax M2.7 | $0.30 | $0.06 (write $0.375) | $1.20 | $0.75 | platform.minimax.io | HIGH |
| Groq | Llama 3.3 70B | $0.59 | -- | $0.79 | $0.69 | groq.com/pricing | HIGH |
| Groq | Llama 3.1 8B Instant | $0.05 | -- | $0.08 | $0.07 | groq.com/pricing | HIGH |
| Google | Gemini 3.1 Flash-Lite | $0.25 | -- | $1.50 | $0.88 | ai.google.dev | HIGH |
| Google | Gemini 3.5 Flash | $1.50 (Batch/Flex $0.75) | $0.15 | $9.00 (Batch/Flex $4.50) | $5.25 ($2.63 batch) | ai.google.dev | HIGH |
| Google | Gemini 3.1 Pro | $2.00 (<=200K ctx; $4.00 above) | -- | $12.00 (<=200K; $18.00 above) | $7.00 | ai.google.dev | HIGH |
| OpenAI | GPT-5.4 | $2.50 | $0.25 (90% off) | $15.00 | $8.75 | developers.openai.com | HIGH |
| OpenAI | GPT-5.4 mini | $0.75 | -- | $4.50 | $2.63 | developers.openai.com | HIGH |
| Anthropic | Claude Haiku 4.5 | $1.00 | 90% read discount | $5.00 | $3.00 | platform.claude.com | HIGH |
| Anthropic | Claude Sonnet 5 | $3.00 (intro $2.00 through Aug 31, 2026) | 90% read discount | $15.00 (intro $10.00) | $9.00 ($6.00 intro) | platform.claude.com | HIGH |
| Anthropic | Claude Opus 4.8 | $5.00 | 90% read discount | $25.00 | $15.00 | platform.claude.com | HIGH |
| Anthropic | Claude Fable 5 | $10.00 | 90% read discount | $50.00 | $30.00 | platform.claude.com | HIGH |

Notes: GPT-4o -- the OpenAI anchor in v1.0 -- was retired from ChatGPT on April 3, 2026, and chatgpt-4o-latest left the API in February 2026. GPT-5.5 (~$5/M input class) and GPT-5.6 sit above GPT-5.4 in the lineup; GPT-5.6 went GA July 9, 2026 with published tiers Sol $5/$30, Terra $2.50/$15, Luna $1/$6 per 1M in/out, 1M-token context on all three (Terra $1.25/$7.50 in Batch or Flex). Gemini 3.5 Flash's standard rate is $1.50/$9 (launched May 19, 2026; $0.15/M cached input, 1M context); the $0.75/$4.50 sometimes reported as a price cut is the Batch/Flex tier -- a standing 50%-off non-interactive tier -- so interactive agent workloads pay $1.50/$9, roughly 3x the model it replaced. Gemini 3.1 Pro's $2/$12 applies only up to 200K context ($4/$18 above); it is still labeled Preview and left Google's API free tier April 1, 2026. MiniMax M2.7 runs $0.24/$0.96 via OpenRouter and is served by ~12 providers (Together, Fireworks, GMI, Novita FP8, SambaNova, etc.); Fireworks also lists DeepSeek V4 Flash $0.14/$0.28, V4 Pro $1.74/$3.48, Qwen 3.6 Plus $0.50/$3.00, and MiniMax M2.7 $0.30/$1.20. Anthropic Opus-class pricing fell ~3x from the $15/$75 v1.0 used. OpenAI, Anthropic, and Google all offer Batch APIs at ~50% off all tokens, stackable with caching -- relevant to any non-latency-sensitive agent workload. Groq (previously absent from this analysis) serves open-weight models (Llama, Qwen, DeepSeek distills, Gemma) at $0.05-$0.90/1M input on LPU hardware at 500+ tokens/sec -- the fastest inference available as of mid-2026, with a free tier -- and is a direct competitor for latency-sensitive agent tool-call chains, though it does not host Kimi or MiniMax models. MiniMax's first-party M3 pricing is $0.30/$1.20 per 1M for inputs up to 512K tokens, rising to $0.60/$2.40 above 512K (displayed rates are a labeled permanent 50% discount from list); 1M-context agent workload modeling on M3 should use the $0.60/$2.40 tier.

### Gonka Pricing (LIVE)

Gonka's inference pricing is now published at two layers that must not be conflated:

1. **Network rate:** a single blended per-token rate recalculated every block from network utilization -- tracker snapshots show ~**$0.0003 per 1M tokens** (GonkaGate-quoted), effectively near-zero because the network is underutilized and partly subsidized by GNK emissions. This is a raw network snapshot, not a retail price.
2. **Broker retail rate:** what developers actually pay. Access is resold by third-party brokers (GonkaGate, JoinGonka, OpenGNK, GonkaBroker, Gonka24). Three now have publicly itemized pricing -- Gonka24, GonkaBroker, and JoinGonka -- and Gonka24's rates are **model-specific**, not flat: MiniMax M2.7 $0.018/$0.072 (the cheapest, "from" price), Kimi K2.6 $0.055/$0.32, GLM-5.2 $0.095/$0.30 per 1M. JoinGonka now publishes itemized rates of $0.003 input / $0.009 output per 1M for Kimi K2.6. GonkaBroker charges $0.30 (MiniMax M2 family) / $0.35 (Kimi K2 family) per 1M flat (input=output, fixed at top-up time); GonkaBroker lists GLM-5.2 as "Coming soon" with no price. OpenGNK (proxy.gonka.gg) was previously the near-network passthrough at ~$0.00016 per 1M, but that figure could not be re-verified in July -- current gateway comparisons describe proxy.gonka.gg as ~133% more expensive than other Gonka gateways under a "temporary pricing adjustment" from the network. Broker retail therefore spans from thousandths of a cent (JoinGonka) to ~$0.35 per 1M (GonkaBroker) -- and even the top of the range sits well below any centralized provider for the same models.

Price trackers list Gonka as the cheapest provider for Kimi K2.6 and MiniMax M2.7.

| Item | Value | Source | Confidence |
|------|-------|--------|------------|
| Network rate (blended, per 1M tokens) | ~$0.0003 (per-block, utilization-driven; not a retail price) | pricepertoken.com/endpoints/gonka | MEDIUM (snapshot; volatile by design) |
| Broker retail: OpenGNK | Earlier ~$0.00016/1M passthrough not re-verifiable (Jul 2026); gateway comparisons now rank proxy.gonka.gg ~133% above other Gonka gateways ("temporary pricing adjustment") | pricepertoken.com; proxy.gonka.gg | MEDIUM (volatile; re-verify before publication) |
| Broker retail: JoinGonka | $0.003 input / $0.009 output per 1M (Kimi K2.6, itemized) | joingonka.ai/en/gateway | HIGH |
| Broker retail: Gonka24 (per model) | M2.7 $0.018/$0.072; K2.6 $0.055/$0.32; GLM-5.2 $0.095/$0.30 per 1M | gonka24.com | HIGH |
| Broker retail: GonkaBroker | $0.30 (MiniMax M2) / $0.35 (Kimi K2) per 1M flat, fixed at top-up | gonkabroker.com | HIGH |
| Models served (as of Jul 16, 2026) | MiniMax M2.7 (sole PoC/base since Jun 25, Proposal 78 -- Qwen3 235B retired); GLM-5.2 (live Jun 26, Proposal 79, weight 2.47, optional); Kimi K2.6 (re-bootstrapping from epoch 331 per Proposals 87/88) | gonka.ai/docs/network-updates | HIGH |
| Network volume | ~100M tokens/day across served models (spring 2026 estimate, not re-verified) | price tracker / release notes | MEDIUM |
| Access path | Third-party brokers; only GonkaGate and JoinGonka fee schedules remain unitemized | broker sites | HIGH |

**Interpretation for leadership:** the v1.0 Scenario A/B/C question ("should Gonka price 30-50% below DeepInfra?") is moot -- even the highest broker retail rate ($0.35 flat) undercuts every scenario and every centralized K2.6/M2.7 host. The strategic questions are now: (1) how fast the network rate rises as utilization grows, (2) the near-zero-to-1,000x spread between network rate and broker retail -- the broker margin is where the user's bill actually forms, and OpenGNK's near-passthrough shows how thin that margin can go; and (3) whether the subsidy is sustainable (see Section 7 on token inflation risk). Cost comparisons in this document use broker retail rates, not the network rate, and use Gonka24's per-model rates rather than a single blended figure. **Availability caveat:** Kimi K2.6 on Gonka is mid-re-bootstrap (removed via expedited Proposal 87 on Jul 15 after losing validation majority in epochs 328-329; re-registered via Proposal 88 on Jul 16 with weight factor raised 0.78 -> 0.9). Gonka K2.6 pricing should not be quoted externally without that reliability disclosure until re-bootstrap completes.

---

## 5. Hidden Cost Analysis

Headline per-token rates tell an incomplete story. Each provider has structural costs and advantages that materially affect the true cost of running OpenClaw agents.

### OpenRouter

v1.0 described a "5.5% credit markup on all usage" and "no prompt caching." Both are wrong as of July 2026:

- **The 5.5% is a payment-processing fee on credit-card credit purchases** ($0.80 minimum per transaction; crypto payments are 5.0% flat). Per-token catalog rates are provider passthrough with no inference markup. BYOK fees are request-based as of July 2026: the first 1M BYOK requests/month are free on standard plans, then 5% of what the call would have cost on OpenRouter's platform (Enterprise: 5M free requests/month).
- **Prompt caching passes through automatically** from underlying providers, with cached input billed at roughly 10-20% of standard input rates on many models. OpenRouter heartbeat costs are NOT "fully unoptimized."
- **OpenRouter's K2.5 listing ($0.375/$2.025) is currently the cheapest K2.5 access in this analysis** -- it undercuts the direct providers it routes to.
- **Free tier degradation and rate limiting** remain real: free-tier requests queue behind paid users, and high-volume agent workloads can hit throttling, creating agent idle time that costs reliability rather than tokens.
- **Net hidden cost: ~5-5.5% at credit purchase (card/crypto), zero per-token markup, caching passthrough. Materially cheaper than v1.0 assumed.**

### OpenAI

**Prompt caching: automatic, cached input billed at 10% of the input rate (90% discount)** -- not the 50% v1.0 used. OpenAI automatically caches prompts longer than 1,024 tokens; OpenClaw's ~9,600-token system prompt qualifies.

- **Impact on heartbeats:** the cacheable system-prompt portion of every heartbeat after the first costs 10% of list input price. Combined with input-heavy heartbeat traffic, heartbeat costs drop roughly 60-70% (estimate; depends on cacheable share).
- **Explicit caching (new):** OpenAI now also offers explicit cache writes billed at 1.25x uncached input, with extended ~24h cache retention. Automatic cache reads keep the 90% discount.
- **Batch API:** ~50% off all tokens for non-interactive workloads, stackable with caching.
- **Premium base price:** GPT-5.4 at $2.50/$15.00 blended is still ~6-7x the cheapest K2.5 access. Caching narrows but does not close the gap.
- **Net adjustment: roughly -60-70% on heartbeat costs (estimate), premium base price remains.**

### Anthropic

**Prompt caching: 90% discount on cache reads, 25% write premium on first fill.** Unchanged mechanics from v1.0; the pricing around it changed dramatically.

- **Opus-class pricing fell 3x:** Opus 4.8 is $5/$25 versus the $15/$75 Opus 4 rate v1.0 used. Every "Opus is 30x more expensive" claim in v1.0-era GTM material is now wrong by roughly 3x.
- **Impact on heartbeats:** steady-state cached heartbeat cost is ~10% of list on the cached portion; net heartbeat reduction ~70% (same mechanics as v1.0).
- **Batch API:** additional 50% off, stackable with caching.
- **Rate limits** remain tighter than OpenAI's and can bottleneck Heavy tier concurrency.
- **Availability:** Claude Fable 5 and Mythos 5 were offline June 12 - July 1, 2026 under a US Commerce Department export-control order -- a ~3-week flagship outage across Claude.ai, the Claude Platform, Claude Code, and Cowork. Regulatory rather than infrastructural, but from an agent operator's perspective it is an outage, and it argues for multi-provider fallback in any Anthropic-anchored agent stack.
- **Subscription billing tightened for agents:** effective June 15, 2026, Anthropic split subscription usage into two pools, following an April 2026 restriction on third-party tools consuming flat-rate plans -- explicitly closing the "always-on agent on a flat subscription" arbitrage (reported effective subsidies of 12-175x). GitHub Copilot similarly moved to AI Credits June 1, 2026. Agent workloads are being pushed onto metered API pricing industry-wide, which is the pricing basis this analysis already uses.
- **Net adjustment: ~-70% on heartbeats; base price now 2.5-12x K2.5-class rates (Haiku 4.5 to Fable 5), no longer "6-30x."**

### Together AI

v1.0 scored Together "no caching -- heartbeats at full price." Wrong as of July 2026:

- **Prompt caching is enabled by default** (the disable flags are deprecated), with 5-10x cached-input discounts on select models: Kimi K2.6 $1.20 -> $0.20 cached, K2.7-Code $0.95 -> $0.19, DeepSeek V4 Pro $1.74 -> $0.20.
- **K2.5 is gone from the serverless pricing page.** Together's Kimi lineup is K2.6 and K2.7-Code. The "$0.50/$2.50 lowest verified K2.5 price" benchmark used throughout v1.0-era docs no longer exists.
- **No markup; no reported rate limit concerns.**
- **Net adjustment: cached heartbeats at roughly 1/5 to 1/6 of list input price on Kimi models (est. -60-70% heartbeat cost).**

### DeepSeek (new in v2.0)

Omitted from v1.0; it is the aggressive price floor of the centralized market and belongs in any Gonka cost comparison. Note the April 24 release was the V4 *Preview*; the official V4 (announced Jun 30) lands mid-July 2026 with China's first **time-of-day API pricing**.

- **V4 Flash: ~$0.14 input / ~$0.28 output regular (¥1.00/¥2.00), cache-hit input $0.0028** (98% off). Heartbeat-dominated workloads are nearly free on cache hits.
- **V4 Pro: ¥3.00/¥6.00 regular (~$0.42/$0.84), ¥0.025 cache hit -- and rates DOUBLE during Beijing peak hours (9:00-12:00 and 14:00-18:00 CST).** A 24/7 agent workload cannot dodge the peak windows: any flat-rate DeepSeek cost model understates cost by up to 2x during Beijing business hours. Conversely, "no rush-hour pricing" is a new positioning lever for Gonka.
- **Legacy deepseek-chat/deepseek-reasoner endpoints retire after July 24, 2026 -- forced migration** onto the V4 time-of-day schedule.
- **Net position: still the cheapest centralized option off-peak; peak-hour doubling and the forced migration make its 24/7 agent economics worse than the headline rate suggests.**

### Gonka

Gonka's structural advantages now sit on top of a near-zero network rate resold at published broker retail.

**Server-side session persistence eliminates context resending.** Gonka's session API maintains conversation state server-side; agents send only the delta since the last call. Architecturally this is "permanent prompt caching" without TTL expiration and without a cache-write premium.

- **Impact on heartbeats:** if sessions cut heartbeat token overhead by 80%, effective monthly tokens drop to ~12.6M (Casual), ~56.3M (Active), ~0.61B (Heavy). At Gonka24's M2.7 rate ($0.045/1M blended) this saves cents to tens of dollars per month -- the session advantage is presently mostly about latency, bandwidth, and future-proofing against rate normalization -- but at Gonka24's K2.6 rate (~$0.19/1M blended) the Heavy-tier session saving is ~$440/month, and at GonkaBroker's $0.30-0.35 flat rates it reaches ~$700/month.
- **Competitive context:** with caching universal -- including Moonshot's own API (K3 cached input $0.30/M vs $3.00/M) -- "sessions vs. no caching" is no longer the frame. The honest frame is "sessions vs. caching": no TTL, no write premium (Anthropic charges +25% and OpenAI 1.25x on explicit cache writes), no client-side resend, works identically across all served models.
- **Broker fees:** the user's bill forms at the broker layer, anywhere from near-passthrough to ~1,000x above the network rate. Three brokers (Gonka24, GonkaBroker, OpenGNK) now have publicly visible pricing; only GonkaGate and JoinGonka remain unitemized. A broker-fee comparison table can now be built from public data.
- **Session caveat (v1.2 tech debt, status unverified as of July 2026):** the v1.2 implementation used in-memory sessions lost on server restart. Confirm whether persistent storage shipped before marketing sessions as production-ready.
- **Net position: broker retail at ~$0.00016-$0.35/1M depending on broker and model -- 3-50x below cached centralized rates for the same models at the mainstream Gonka24/GonkaBroker rates (network rate itself unsustainable as a permanent assumption) -- plus a genuine session architecture advantage whose full dollar value materializes if/when rates normalize.**

### Hidden Cost Summary

| Provider | Markup | Prompt Caching | Session Persistence | Rate Limits | Net Effect on Agent Workloads |
|----------|--------|---------------|---------------------|-------------|-------------------------------|
| OpenRouter | 5-5.5% at credit purchase only | Passthrough (10-20% of input) | None | Moderate | Cheapest K2.5 access; caching passthrough |
| OpenAI | None | 90% off cached reads (auto); explicit writes 1.25x | None | Lenient | ~-60-70% on heartbeats (est.); premium base |
| Anthropic | None | 90% reads / +25% writes | None | Strict | ~-70% on heartbeats; Opus-class now 3x cheaper than v1.0 figures; Fable 5 offline Jun 12 - Jul 1 (export-control) |
| Together AI | None | Default-on, 5-10x on select models | None | Lenient | ~-60-70% on Kimi heartbeats (est.); K2.5 delisted |
| DeepInfra | None | K2.6 cached $0.15 | None | Lenient | Cheap K2.5 base; caching on K2.6 |
| DeepSeek | None | Cache-hit ~98% off | None | Lenient | Centralized price floor |
| Gonka | Broker retail: ~$0.00016 passthrough (OpenGNK) to $0.30-0.35 flat (GonkaBroker); Gonka24 per-model | N/A (sessions instead) | Yes (~80% token reduction) | TBD | Cheapest listed K2.6/M2.7 access + sessions |

---

## 6. Monthly Cost Projections

The following tables show monthly cost per provider for each workload tier. "Raw Monthly Cost" applies headline blended rates to total monthly tokens with no caching. "Cached-Adjusted Cost" applies an estimated caching discount of ~65% to the heartbeat portion of tokens for providers with 90%-class cached-input pricing (~90% for DeepSeek cache hits). **The adjusted column is an estimate** -- caching applies to input tokens only and actual cacheable share varies; treat these as directional, not quotable.

Heartbeat share of tokens: Casual 44%, Active 51%, Heavy 84.5%.

**Blended rate formula:** Monthly tokens x (input price + output price) / 2.

### Casual Tier (~31.5M tokens/month)

**Worked example (DeepInfra K2.5):** 31.5M x $1.35/1M = $42.53/month

| Provider | Model | Blended/1M | Raw Monthly | Cached-Adjusted (est.) |
|----------|-------|------------|-------------|------------------------|
| Gonka (broker retail) | MiniMax M2.7 / K2.6 / GLM-5.2 | $0.045 (M2.7) / ~$0.19 (K2.6) via Gonka24; $0.30-0.35 (GonkaBroker) | **~$1.42 (M2.7) - ~$5.90 (K2.6) - $11** | same (broker rates are all-in) |
| DeepSeek | V4 Flash | $0.21 | $6.62 | **~$4** |
| OpenRouter | K2.5 | $1.20 | $37.80 | ~$27 (upstream-dependent) |
| DeepInfra | K2.5 | $1.35 | $42.53 | $42.53 (no K2.5 caching) |
| OpenRouter | K2.6 | $2.04 | $64.26 | ~$46 (upstream-dependent) |
| DeepInfra | K2.6 | $2.13 | $66.94 | **~$48** |
| Together AI | K2.6 | $2.85 | $89.78 | **~$64** |
| OpenAI | GPT-5.4 | $8.75 | $275.63 | **~$197** |
| Anthropic | Sonnet 5 | $9.00 | $283.50 | **~$202** (~$135 at intro pricing) |
| Anthropic | Opus 4.8 | $15.00 | $472.50 | **~$337** |

**Casual Tier Takeaway:** Centralized K2.5/K2.6 access clusters at roughly $38-90/month; DeepSeek undercuts everything centralized at ~$4-7. Gonka's published broker retail lands at ~$1.42/month (Gonka24, M2.7) to ~$5.90 (Gonka24, K2.6) to ~$11/month (GonkaBroker) -- cheapest in the table, but on the same order as DeepSeek at the high end, not "approximately nothing." Frontier models cost 3-8x the Kimi-class hosts even with caching, not the 3-20x spread v1.0 reported (Opus-class prices fell 3x).

### Active Tier (~161.5M tokens/month)

**Worked example (DeepInfra K2.5):** 161.5M x $1.35/1M = $218.03/month

| Provider | Model | Blended/1M | Raw Monthly | Cached-Adjusted (est.) |
|----------|-------|------------|-------------|------------------------|
| Gonka (broker retail) | MiniMax M2.7 / K2.6 / GLM-5.2 | $0.045 (M2.7) / ~$0.19 (K2.6) via Gonka24; $0.30-0.35 (GonkaBroker) | **~$7 (M2.7) - ~$30 (K2.6) - $57** | same (broker rates are all-in) |
| DeepSeek | V4 Flash | $0.21 | $33.92 | **~$18** |
| OpenRouter | K2.5 | $1.20 | $193.80 | ~$131 (upstream-dependent) |
| DeepInfra | K2.5 | $1.35 | $218.03 | $218.03 |
| OpenRouter | K2.6 | $2.04 | $329.46 | ~$223 (upstream-dependent) |
| DeepInfra | K2.6 | $2.13 | $343.19 | **~$229** |
| Together AI | K2.6 | $2.85 | $460.28 | **~$308** |
| OpenAI | GPT-5.4 | $8.75 | $1,413.13 | **~$945** |
| Anthropic | Sonnet 5 | $9.00 | $1,453.50 | **~$972** |
| Anthropic | Opus 4.8 | $15.00 | $2,422.50 | **~$1,620** |

**Active Tier Takeaway:** With heartbeats at 51% of tokens, caching now does for every major provider a version of what v1.0 claimed only Gonka sessions could do. The v1.0 comparison ("DeepInfra $218 vs Gonka Scenario B $59") is obsolete in both directions: Gonka's broker retail runs ~$7-$57 depending on model and broker -- below even Scenario B -- and competitors' cached rates are 30-35% below their raw rates.

### Heavy Tier (~2.94B tokens/month)

**Worked example (DeepInfra K2.5):** 2,943M x $1.35/1M = $3,973.05/month

| Provider | Model | Blended/1M | Raw Monthly | Cached-Adjusted (est.) |
|----------|-------|------------|-------------|------------------------|
| Gonka (broker retail) | MiniMax M2.7 / K2.6 / GLM-5.2 | $0.045 (M2.7) / ~$0.19 (K2.6) via Gonka24; $0.30-0.35 (GonkaBroker) | **~$132 (M2.7) - ~$550 (K2.6) - $1,030** | same (broker rates are all-in) |
| DeepSeek | V4 Flash | $0.21 | $618.03 | **~$148** |
| OpenRouter | K2.5 | $1.20 | $3,531.60 | ~$2,000 (upstream-dependent) |
| DeepInfra | K2.5 | $1.35 | $3,973.05 | $3,973.05 |
| OpenRouter | K2.6 | $2.04 | $6,003.72 | ~$3,400 (upstream-dependent) |
| DeepInfra | K2.6 | $2.13 | $6,253.88 | **~$2,820** |
| Together AI | K2.6 | $2.85 | $8,387.55 | **~$3,783** |
| OpenAI | GPT-5.4 | $8.75 | $25,751.25 | **~$11,614** |
| Anthropic | Sonnet 5 | $9.00 | $26,487.00 | **~$11,946** |
| Anthropic | Opus 4.8 | $15.00 | $44,145.00 | **~$19,909** |

**Heavy Tier Takeaway:** With heartbeats at 84.5% of tokens, caching cuts every cached provider's bill roughly in half -- and Gonka broker retail serves the entire workload for ~$132 (Gonka24, only if the workload runs on MiniMax M2.7), ~$550 (Gonka24 on K2.6), or ~$880-$1,030 (GonkaBroker), versus ~$2,800-$3,800 on cached centralized K2.6. Three caveats keep this from being an unqualified marketing headline: (1) a Heavy-tier customer at 2.94B tokens/month would roughly double Gonka's entire current network volume (~100M tokens/day = ~3B/month), which would itself move the per-block price; (2) the near-zero underlying network rate is subsidy- and idle-capacity-driven, not a cost floor; (3) at the GonkaBroker end of the retail range, DeepSeek's cache-hit pricing (~$148) is actually cheaper. The honest Heavy-tier claim is "3-20x cheaper than centralized hosts of the same models today, with price discovery risk as utilization grows."

---

## 7. At-Scale Economics

What happens when an organization scales beyond the Heavy tier to 100+ agents?

### Linear Scaling (Centralized Providers)

**OpenRouter / Together AI / DeepInfra / DeepSeek:** cost scales linearly with agent count -- each token costs the same whether it is the first or the billionth. 100 Heavy-tier agents lands at roughly $200K-$400K/month on cached Kimi-class rates, or ~$15K/month on DeepSeek V4 Flash cache-hit-heavy workloads (estimates from Section 6 adjusted figures x100). Enterprise agreements may discount committed spend, but the linear structure holds.

**OpenAI / Anthropic:** enterprise committed-use agreements reportedly discount 20-40% above ~$100K annual spend (industry estimate, unverified). Even with a 40% discount and caching, 100 Heavy-tier agents on GPT-5.4 or Sonnet 5 exceeds $700K/month. Anthropic's rate limits are the binding constraint before pricing is: concurrent-request caps likely require enterprise negotiation before 100 always-on agents are viable. Nor is there a subscription escape hatch: Anthropic's June 15, 2026 billing restructure (two usage pools; April 2026 third-party-tool restriction) and Copilot's June 1 move to AI Credits closed the flat-rate-plan arbitrage for always-on agents -- at-scale agent workloads pay metered API rates.

### Decentralized Network Economics

**Gonka:** the per-block utilization pricing creates a fundamentally different scaling dynamic -- in both directions. Today's ~$0.0003/1M network rate exists because supply vastly exceeds demand; brokers retail it at ~$0.00016-$0.35/1M depending on broker and model. A 100-agent Heavy deployment (~294B tokens/month) would cost ~$13K/month at Gonka24's M2.7 rate (~$55K on K2.6) -- the M2.7 figure competitive with DeepSeek's ~$15K cache-hit floor -- but would be ~100x the network's entire current volume; the per-block price (and broker rate cards built on it) would reprice long before that demand landed. Conversely, as more GPU miners join, supply growth can hold prices down.

Caveats that still apply:

1. **Token inflation risk:** the near-zero rate is partly funded by GNK emissions subsidizing miners. If emissions decay (see v1.0 research) without matching fee revenue, either prices rise or supply exits.
2. **Price discovery risk:** no large agent deployment has yet tested what Gonka's rate does under sustained load. Leadership should not extrapolate today's rate to at-scale commitments.
3. **Centralized budget tiers keep getting cheaper -- but frontier open-weight pricing is now rising.** Blackwell-class hardware enables up to 10x cost-per-token reduction for centralized providers (NVIDIA, 2026), and DeepSeek has pushed budget prices to $0.14/M input. Token prices industry-wide fell ~280x over two years. But the trend has partially reversed above the budget tier: Gemini 3.5 Flash's $1.50/$9 standard rate is ~3x the model it replaced (the $0.75/$4.50 figure is batch-only), Kimi K3's $3/$15 is ~3x K2.6's official $0.95/$4.00, and industry coverage frames K3 as "signaling the end of super cheap Chinese AI" (The Decoder, Jul 2026). The floor is still falling at the workhorse tier Gonka serves; the frontier tier is drifting toward closed-model pricing.

Demand-side context (replacing the forecast-only Goldman/Deloitte citations): OpenRouter's Series B announcement (Businesswire, May 26, 2026) puts weekly volume at **25T tokens** -- up from ~5T six months prior, ~100T tokens/month (a ~28T/week mid-2026 figure circulates but is unofficial); agentic workloads now generate more than half of all output tokens, surpassing human usage; 67% of enterprises consume >1B tokens/month (Deloitte 2026); and Chinese open-source models capture ~61% of global OpenRouter token usage -- directly supportive of Gonka's Kimi/Qwen/MiniMax strategy.

**Scaling verdict:** Gonka's current advantage is real but reflexive -- it is cheap because it is empty. The durable at-scale advantages are session persistence (heartbeat elimination that compounds with agent count) and decentralized supply growth, not today's headline rate.

---

## 8. Where Gonka Wins and Where It Does Not

### Where Gonka Wins

**Price, today, by a wide margin.** At published broker retail of ~$0.00016-$0.35/1M, Gonka is the cheapest listed provider for Kimi K2.6 and MiniMax M2.7 on price trackers -- versus $0.66-$1.20/1M input on the cheapest centralized K2.6 hosts (OpenRouter $0.66/$3.41 is now the centralized floor) and MiniMax's official $0.30/$1.20 for M2.7. For cost-driven experimentation and hobbyist agent workloads, nothing centralized matches the Gonka broker rates. The caveats -- utilization-driven underlying rate, subsidy-backed, broker- and model-dependent (quote the per-model broker retail, never the ~$0.0003 network snapshot, and never Gonka24's M2.7 "from" price as a network-wide rate), and K2.6's mid-July re-bootstrap (below) -- belong in every external claim.

**Agent workloads with frequent heartbeats.** Session persistence eliminates heartbeat context resending rather than discounting it. Versus caching it has no TTL, no cache-write premium (Anthropic charges +25%, and OpenAI's explicit caching now bills writes at 1.25x uncached input), and no client-side full-context resend. Note the frame changed: with caching universal (OpenAI, Anthropic, Google, Together, DeepInfra, DeepSeek, Moonshot's own API, OpenRouter passthrough), the pitch is "better than caching," not "the cost no one else can touch." The dollar delta versus a well-cached competitor is far smaller than the 60-84% v1.0 claimed and should be recomputed against cached baselines before external use.

**Multi-model coverage of strong open-weight models -- with churn.** The v1.0 "single-model K2.5 network" weakness is gone, but the lineup moved again in late June/July: Qwen3 235B was retired June 25 (Proposal 78), MiniMax M2.7 is now the sole PoC/base model, GLM-5.2 (open agent-benchmark leader, 1M context) went live June 26 (Proposal 79, weight 2.47, optional), and Kimi K2.6 is re-bootstrapping from epoch 331 after Proposals 87/88. Three families, one of them mid-recovery. The open-weight SWE-bench Verified leader is now DeepSeek V4 Pro (Apr 24, 2026; 1.6T MoE, MIT license, 1M context) at 80.6% in Think Max mode, tied with Gemini 3.1 Pro and displacing MiniMax M2.5's 80.2%. Kimi K3's open weights (2.8T MoE, 1M context, due ~Jul 27, 2026) are the obvious next addition. MiniMax M3 (weights since ~Jun 7, 2026; 428B/23B active, 1M context, native multimodal, vendor-reported 59.0% SWE-Bench Pro; first-party pricing $0.30/$1.20 up to 512K input, $0.60/$2.40 above) is attractive on serving economics but ships under the commercially restricted MiniMax Community License (attribution; prior authorization above $20M/yr revenue) -- a material constraint for a decentralized hosting network that must be resolved before Gonka can serve it. Watch item: The Information reports (mid-Jul 2026, single-sourced) MiniMax is preparing "M3 Pro," a 2.7T-parameter model rivaling K3's 2.8T, with possible open-source release as early as Q3 2026; active-parameter count and license unannounced -- the license question is decisive for Gonka hosting.

**Privacy-sensitive workloads.** Decentralized inference means no single entity (including Gonka) stores conversation data centrally. For agents handling sensitive information, this remains a meaningful differentiator over centralized providers.

**Token-aligned users.** For crypto-native users who hold or earn GNK, paying for inference with tokens they mine or stake creates a closed economic loop. Niche, but real for the DePIN ecosystem.

### Where Gonka Does Not Win

**Users who need broad model choice.** Gonka's 3 model families (one mid-re-bootstrap) versus OpenRouter's 400+ catalog (OpenRouter's own docs: 400+ active models on 70+ providers; avoid the old "500+"/"losing 499 models" phrasing). A developer wanting GPT-5.6 or Claude Fable 5 for hard reasoning plus a cheap open model for simple tasks cannot do it on Gonka alone. This remains the largest gap, though far narrower than the v1.0 "one model vs. 500" framing.

**Latency-sensitive tool-call chains.** Groq serves open-weight models on LPU hardware at 500+ tokens/sec -- the fastest inference available as of mid-2026 -- at $0.05-$0.90/1M input with a free tier. For agent workloads where tool-call chain latency compounds (the core workload in this analysis), a decentralized network cannot match dedicated-silicon speed, and Groq competes on price too at the small-model end.

**Users who need enterprise SLAs.** No published SLA, no guaranteed uptime, no enterprise support tier -- unchanged from v1.0. OpenAI and Anthropic offer contractual uptime SLAs. Additionally, per-block price volatility is itself an SLA problem: an enterprise cannot budget against a rate that reprices every block. (Counterweight: SLAs do not cover regulatory action -- Anthropic's Fable 5 was offline June 12 - July 1, 2026 under a US export-control order, a 3-week flagship outage that modestly strengthens the multi-provider/decentralization argument. And Gonka's own K2.6 removal/re-registration in July shows decentralized governance produces model-level outages too.)

**Users who need price stability.** New since v1.0: the same mechanism that makes Gonka near-free today makes its price unpredictable tomorrow. Centralized providers publish fixed rate cards; Gonka publishes a formula. For CFO-approved production budgets, "cheap but floating" can lose to "10x more but fixed."

**Users already optimized for a provider's caching ecosystem.** Developers who structured prompts around OpenAI/Anthropic/Moonshot cache behavior face real switching costs to re-architect for sessions -- and with 90% cached-input discounts, their incentive to switch on cost alone is weaker than v1.0 assumed.

**Users who need zero-config OpenClaw integration.** OpenRouter is built into OpenClaw; Gonka requires manual provider configuration, plus choosing a broker. The broker layer adds a second decision (and a second fee) that centralized providers do not impose.

---

## 9. Recommendations for Leadership

The v1.0 recommendation set (pick Scenario B, publish a pricing page, add a free tier) is largely overtaken by events: pricing is live, published, and near-zero. The July 2026 recommendations:

### 1. Market the price honestly: "cheapest today," not "cheapest forever"

Gonka's tracker-verified position as the cheapest K2.6/M2.7 provider is a legitimate acquisition headline. But the rate is utilization-driven and partly emission-subsidized. External messaging should cite tracker listings ("cheapest listed provider for Kimi K2.6") rather than quoting $0.0003/1M as a stable rate, and should disclose the per-block repricing mechanism. Until K2.6's re-bootstrap (epoch 331, Proposals 87/88) completes and holds, "cheapest K2.6 provider" claims also need a reliability disclosure -- the model was removed from the network for a day in mid-July. Overclaiming a subsidy-driven price invites a painful correction when utilization rises.

### 2. Publish the broker-fee comparison -- the public data now exists

At near-zero network rates, the user's actual bill is dominated by broker fees. Three brokers (Gonka24, GonkaBroker, OpenGNK) now have publicly visible pricing -- from OpenGNK's ~$0.00016/1M near-passthrough to GonkaBroker's $0.35 flat -- so the recommended broker-fee comparison table can be built today from public data; only GonkaGate and JoinGonka remain unitemized. Publish it (or a first-party access path) before competitors or reviewers do it unfavorably. "Near-free network, opaque middlemen" is a bad story to let others write -- and it is now only half true.

### 3. Recompute and reposition the session story against cached baselines

The "heartbeats cost $0 on Gonka; everywhere else they're your biggest expense" message is no longer structurally true -- cached heartbeats cost ~10-30% of list nearly everywhere, including on Moonshot's own API. The defensible version: sessions beat caching (no TTL, no write premium, no resend, uniform across models), and they future-proof agent costs against Gonka's own rate normalization. Recompute all savings deltas against cached competitor rates before any external use; the v1.0-era 60-84% figures must not be cited.

### 4. Stabilize K2.6, then add Kimi K3 weights when they arrive (~Jul 27, 2026)

GLM-5.2 has landed (live June 26, Proposal 79) and Gonka's lineup -- MiniMax M2.7 (sole PoC/base), GLM-5.2, K2.6 (re-bootstrapping) -- covers the workhorse tier, minus the retired Qwen3 235B. The immediate priority is completing K2.6's re-bootstrap cleanly: the epoch 328-329 validation failure (concentrated guardian delegations plus provider failures) is a governance/operations lesson that will recur as models are added. Next: K3's open weights -- 2.8T MoE, 1M context, debuting #3 on Artificial Analysis behind Claude Fable 5 and GPT-5.6 -- would give Gonka a frontier-tier offering and a news hook. K2.7-Code is the nearer-term coding-agent addition; DeepSeek V4 Pro (open-weight SWE-bench Verified leader at 80.6%, MIT license) is worth evaluating too. MiniMax M3 requires resolving its Community License restrictions first. Any remaining K2.5- or Qwen-anchored GTM material should be retired.

### 5. Resolve and verify session persistence productionization

The v1.2 in-memory session caveat predates this revision; verify whether persistent session storage has shipped. The session advantage cannot be marketed until it survives a server restart.

---

## Appendix: Calculation Reference

### Token-to-Cost Formula

```
Monthly Cost = Monthly Tokens x (Input Price/1M + Output Price/1M) / 2
```

Assumes 1:1 input:output ratio. Actual agent workloads are typically 60-70% input / 30-40% output, which would reduce costs for providers with cheaper input tokens. The 1:1 assumption is conservative.

### Session Persistence Adjustment

```
Effective Monthly Tokens = Message Tokens + (Heartbeat Tokens x 0.20) + Tool Call Tokens
```

The 0.20 factor assumes 80% of heartbeat tokens are eliminated by sessions (only delta context sent instead of full resend). If the system prompt is 80%+ of heartbeat context, sessions could reduce heartbeat overhead by 85-90%.

### Prompt Caching Adjustment (90%-class providers: OpenAI, Anthropic, Moonshot, Together/DeepInfra Kimi models)

```
Adjusted Heartbeat Cost ~= Heartbeat Cost x (1 - Cacheable% x InputShare x 0.90)
```

Section 6 tables use a flat ~65% heartbeat-cost reduction as the working estimate (80% cacheable share, input-heavy heartbeat traffic, 90% cached-input discount). Anthropic adds a 25% cache-write premium on first fill, which amortizes within two heartbeats. DeepSeek cache hits (~98% off) use ~90%. These are estimates; actual savings depend on cacheable share and input:output mix.

---

## Sources

### Pricing Data (HIGH confidence unless noted; accessed July 2026)
- [Gonka network pricing](https://pricepertoken.com/endpoints/gonka) -- live blended per-block rate ~$0.0003/1M; model list; OpenGNK ~$0.00016/1M passthrough listing.
- [Gonka24 rate card](https://gonka24.com/) -- per-model discount rates: M2.7 $0.018/$0.072, K2.6 $0.055/$0.32, GLM-5.2 $0.095/$0.30.
- [GonkaBroker pricing](https://gonkabroker.com/gonka-api-pricing/) -- broker access and fee structure.
- [OpenGNK proxy](https://proxy.gonka.gg/) -- near-network-rate passthrough broker.
- [JoinGonka](https://joingonka.ai/en/knowledge/what-is-gonka/) -- advertised ~$0.003/1M for K2.6-class inference (marketing figure).
- [Gonka network updates](https://gonka.ai/docs/network-updates/) -- Proposal 78 (Qwen3 235B retired, M2.7 sole PoC, Jun 25), Proposal 79 (GLM-5.2 live, Jun 26), Proposals 87/88 (K2.6 removal and re-registration, Jul 15-16).
- [Groq pricing](https://groq.com/pricing) -- Llama 3.1 8B Instant $0.05/M input, Llama 3.3 70B $0.59/$0.79; LPU 500+ tok/s; free tier.
- [MiniMax M3 pricing](https://minimax-ai.chat/models/minimax-m3/) -- $0.30/$1.20 up to 512K input, $0.60/$2.40 above; permanent 50%-off framing.
- [OpenRouter](https://openrouter.ai/pricing), [K2.5 listing](https://openrouter.ai/moonshotai/kimi-k2.5) -- $0.375/$2.025; 5.5% card / 5.0% crypto credit-purchase fee; caching passthrough.
- [Together AI Pricing](https://www.together.ai/pricing) -- K2.6 $1.20/$0.20 cached/$4.50; K2.7-Code $0.95/$0.19/$4.00; default-on caching.
- [DeepInfra K2.6 guide](https://deepinfra.com/blog/kimi-k2-6-pricing-guide-deployment-tradeoffs) -- K2.6 $0.75/$3.50, cached $0.15.
- [Artificial Analysis: K2.5 Providers](https://artificialanalysis.ai/models/kimi-k2-5/providers) -- DeepInfra $0.45/$2.25; SiliconFlow, CoreWeave, Bedrock comparisons.
- [OpenAI Pricing](https://developers.openai.com/api/docs/pricing) -- GPT-5.4 $2.50/$15, cached input 10% of list; GPT-4o retirement.
- [Anthropic Pricing](https://platform.claude.com/docs/en/about-claude/pricing) -- Opus 4.8 $5/$25, Sonnet 5 $3/$15 (intro $2/$10), Haiku 4.5 $1/$5, Fable 5 $10/$50; caching and Batch API.
- [DeepSeek Pricing](https://api-docs.deepseek.com/quick_start/pricing/) -- V4 Flash $0.14/$0.28, cache-hit $0.0028.
- [Google Gemini Pricing](https://ai.google.dev/gemini-api/docs/pricing) -- Gemini 3.1 Pro $2/$12, 3.1 Flash-Lite $0.25/$1.50.
- [Moonshot platform pricing](https://platform.kimi.ai/docs/pricing/chat-k26) -- K2.7-Code and K3 rates; kimi-k2-series deprecation (May 25, 2026).

### Model Landscape (July 2026)
- [Kimi K3 announcement coverage](https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html) -- 2.8T MoE, 1M context, $3/$15, weights ~Jul 27.
- [Kimi K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code) -- coding model, 256K context, Modified MIT.
- [Gonka releases](https://github.com/gonka-ai/gonka/releases) -- K2.6 validation fix (v0.2.13), MiniMax M2.7 route support (devshard v3, Jul 9, 2026).

### Agent Workload Data (MEDIUM confidence; Feb 2026 community estimates, not re-verified)
- [OpenClaw Token Costs 2026](https://aicost.org/blog/openclaw-ai-token-costs-2026-pricing-breakdown-optimization) -- 9,600 tokens/turn system prompt overhead.
- [OpenClaw Pricing Guide](https://clawback.tools/openclaw-pricing) -- Heartbeat cost analysis, 30-min and 5-min intervals.
- LangChain State of Agent Engineering -- Tool call multiplier (3-10x) for agent vs chatbot workloads.

### Market Context (MEDIUM confidence)
- [NVIDIA Blackwell Inference Cost Blog](https://blogs.nvidia.com/blog/inference-open-source-models-blackwell-reduce-cost-per-token/) -- 10x cost reduction for providers using Blackwell GPUs.
- Deloitte 2026 TMT Predictions -- inference ~two-thirds of AI compute in 2026; token prices fell ~280x over two years while enterprise AI spend rose ~320%; 67% of enterprises consume >1B tokens/month.
- [OpenRouter State of AI (with a16z, May 2026)](https://openrouter.ai/state-of-ai) -- 100T-token study: ~4x YoY throughput growth to ~28T tokens/week; agentic workloads >50% of output tokens; Chinese open-source models ~61% of token usage.
- [The Decoder on Kimi K3 pricing](https://the-decoder.com/kimis-open-model-k3-nears-gpt-5-6-sol-and-fable-5-while-signaling-the-end-of-super-cheap-chinese-ai/) -- K3 $3/$15 as end of "super cheap Chinese AI" at the flagship tier.

### Internal References
- `.planning/research/STACK.md` -- OpenClaw architecture, provider ecosystem
- `.planning/research/FEATURES.md` -- Feature landscape, competitive dimensions
- `.planning/research/PITFALLS.md` -- GTM pitfalls, trust barriers
- `output/gonka_competitive_feature_matrix.md` -- Feature matrix (COMP-01 cross-reference; needs the same July 2026 caching re-run)

---

*Gonka's live rate is a per-block, utilization-driven snapshot, not a stable quote. Cached-adjusted competitor figures in Section 6 are estimates. Leadership should not cite specific dollar savings externally until session savings are recomputed against cached competitor baselines and broker fee schedules are verified.*

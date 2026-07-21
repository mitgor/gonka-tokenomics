# Gonka Message House

**Version:** 1.4
**Date:** 2026-07-18
**Classification:** Internal -- canonical messaging framework for all Gonka developer-facing communications
**Feeds into:** Phase 18 (Channel Strategy), Phase 19 (Partnership & Ecosystem)
**Requirement:** MSG-02

---

## 1. Executive Summary

This document is the single source of truth for how Gonka talks to developers. Every blog post, landing page, documentation snippet, conference talk, comparison table, and community reply should reference this framework before publishing. It contains: a core positioning statement that leads with developer outcomes; ranked value propositions grounded in competitive evidence; per-persona differentiation for three developer archetypes; a complete architecture-to-message mapping that translates every Gonka technical feature into a developer benefit; vocabulary guidelines that prevent crypto jargon from leaking into developer-facing content; and competitive differentiation statements tailored to the competitor each persona is most likely comparing Gonka against. All claims are sourced from Phase 15 (competitive analysis) and Phase 16 (developer personas) research, revalidated against live sources on 2026-07-18, with parenthetical citations throughout.

> **July 2026 revision notes (read before reusing any number):**
> 1. **Gonka pricing is now live and published -- distinguish network rate from broker retail.** The raw network rate, recalculated every block from utilization, has recently been ~$0.0003 per 1M tokens (GonkaGate quote, subsidized/underutilized). What developers actually pay is the broker retail rate, and Gonka24's schedule is now **per-model, not flat**: MiniMax M2.7 $0.018/$0.072 per 1M (the cheapest, "from" price), Kimi K2.6 $0.055/$0.32, GLM-5.2 $0.095/$0.30. GonkaBroker publishes $0.30 (MiniMax M2) and $0.35 (Kimi K2) per 1M, flat input=output. Never quote "$0.018/$0.072" as Gonka's or Gonka24's general rate -- it is the M2.7 floor only; K2.6 workloads cost roughly 4x more than that floor implies. Five known brokers: GonkaGate, JoinGonka, OpenGNK, GonkaBroker, Gonka24. External "cheapest listed provider" claims must quote broker retail (~$0.02-0.35/1M -- still far below Together/AkashML at $0.95-$4.50), never the near-zero network rate. Price trackers list Gonka as the cheapest provider for Kimi K2.6 and MiniMax M2.7. The hypothetical Scenario A/B/C framing ($0.25-$0.45 per 1M input) is obsolete; all "Scenario B" dollar figures below are April 2026 estimates retained for narrative shape and marked as such.
> 2. **Prompt caching is now universal** across the compared landscape (OpenAI and Anthropic at 90% off cached input, Together default-on, DeepInfra, Fireworks, Moonshot's own API, DeepSeek, and OpenRouter passthrough). Savings deltas computed against uncached April baselines overstate the session advantage; the honest claim is "sessions eliminate repeated context entirely, caching only discounts it to 10-20% of the input rate."
> 3. **The model landscape moved -- and Gonka's lineup moved with it.** Gonka now serves Kimi K2.6 and MiniMax M2.7 (verified live: pricepertoken.com, GonkaBroker menu; K2.6 validation fix shipped in v0.2.13, M2.7 route support in devshard v3). **Proposal 78 (June 25, 2026) removed BOTH Qwen3-235B and Kimi K2.6 for lacking validation majority; Qwen3-235B is retired for good, and MiniMax M2.7 is now the sole PoC model and base delegation target** -- any "three model families" or Qwen-inclusive lineup copy is stale. K2.6 was restored the next day (Proposal 79, Jun 26 -- which set its weight_scale_factor at 0.9 and introduced GLM-5.2 on-network at 2.47) and re-bootstrapped at epoch 311 on Jun 27, then hit a SECOND validation-failure removal in mid-July (Proposal 87, Jul 15) with another re-bootstrap. Two K2.6 validation failures in three weeks: never describe K2.6 as "continuously live," and note the "Proposal 88 raised the weight factor 0.78 → 0.9" history circulating in sibling docs conflicts with the official feed -- 0.9 was set Jun 26 via Proposal 79 (gonka.ai/docs/network-updates). **GLM-5.2 is imminent as a third family** -- the Gonka blog lists it as "coming soon" and Gonka24 already publishes a GLM-5.2 rate card ($0.095/$0.30 per 1M vs $0.95/$3.00 list). Any residual "K2.5 tiers only / two generations behind" copy is stale and must not ship. Upstream: Kimi K3 launched via app/API Jul 16, 2026 (2.8T MoE, 896 experts/16 active, 1M context, $3/$15 per 1M; open weights due ~Jul 27 -- largest open-weight release ever; took #1 in Frontend Code Arena ahead of Claude Fable 5 and GPT-5.6 Sol). With the K3 launch Moonshot closed Kimi K2.5 to newly registered users and scheduled full platform sunset for Aug 31, 2026, redirecting K2.5 API traffic to K2.6 -- do not quote Moonshot's first-party K2.5 rate ($0.60/$3.00) as a current purchasable price, and treat any K2.5-anchored comparison (third-party hosts like OpenRouter $0.375/$2.025 and DeepInfra $0.45/$2.25 still serve it) as having ~6 weeks of shelf life (platform.kimi.ai/docs/models). MiniMax M3 (Jun 1, 2026; 428B/23B active, 1M context, native multimodal, 59.0% SWE-Bench Pro vendor-reported) supersedes M2.5/M2.7 as MiniMax's flagship. The open-weight SWE-bench Verified leader is now DeepSeek V4 Pro at 80.6% (Think Max mode; released Apr 24, 2026; MIT license, 1M context), tied with Gemini 3.1 Pro and displacing MiniMax M2.5 (80.2%); GLM-5 sits at 77.8%. Messaging that calls K2.5 "the best open-source agent model" -- or M2.5 the open-weight leader -- must not ship externally.
> 4. **Two former WIN claims weakened.** OpenAI's Responses + Conversations API now provides server-side stateful conversations on its primary API surface (Assistants API shuts down Aug 26, 2026), and cost-based model routing is commoditized in the OpenClaw ecosystem (ClawRouter and third-party routers). Sessions/memory remain differentiated in degree, not in kind; tiering is no longer unique.

---

## 2. Core Positioning Statement

> **For OpenClaw developers who spend too much on inference because their agents resend full context on every heartbeat, Gonka is the agent-native inference provider that combines the lowest published per-token price on the market with server-side session persistence, unlike OpenRouter and Together AI whose prompt caching still bills repeated context at 10-20% of the input rate, because Gonka maintains conversation state server-side so your agent never pays for the same context twice.**

### Positioning Statement Breakdown

| Element | Content | Source |
|---------|---------|--------|
| **Target audience** | OpenClaw developers running always-on AI agents | (developer personas: all three personas use OpenClaw) |
| **Need** | Agents resend full context on every heartbeat, inflating costs by 44-85% pre-caching | (pricing analysis: Section 3, heartbeat overhead by tier -- Apr 2026 estimate; deltas shrink against cached rates) |
| **Category** | Agent-native inference provider | (provider landscape map: Gonka combines decentralized infrastructure with agent-native extensions; Akash Agents now partially overlaps -- see 7.3) |
| **Key benefit** | Lowest published per-token price (broker retail ~$0.02-0.35/1M vs $0.95+ elsewhere for the same models) plus session persistence that eliminates repeated-context billing entirely | (live pricing: pricepertoken.com/endpoints/gonka, gonkabroker.com, gonka24.com; competitive matrix: Agent Sessions -- WIN) |
| **Alternatives** | OpenRouter and Together AI | (competitive matrix: both lack server-side sessions on chat completions) |
| **Reason to believe** | Server-side conversation state eliminates repeated context transmission; caching elsewhere only discounts it | (competitive matrix: Agent Sessions; architecture mapping: X-Gonka-Session-ID) |

### Why This Positioning Works

1. **Leads with developer outcome** (cost reduction), not technology (decentralization) -- per CONTEXT.md locked decision and PITFALLS.md Pitfall 1
2. **Names a specific, quantified pain** (heartbeat overhead) that developers experience personally -- per pricing analysis Section 3
3. **Names the specific mechanism** (session persistence) rather than a vague "decentralized compute" claim -- per PITFALLS.md Anti-Pattern 2
4. **Names specific alternatives** the audience is already using, not generic "other providers" -- per ARCHITECTURE.md Anti-Pattern 3
5. **Survives the caching counter-argument** -- it concedes competitors cache and states the residual delta precisely, rather than pretending heartbeats are unoptimized everywhere

---

## 3. Value Propositions (Ranked)

Value propositions are ranked by differentiation strength, following the USP ranking from ARCHITECTURE.md Section "Unique Selling Propositions (Ranked)" but rewritten as developer-facing benefit statements. Ranking updated July 2026: pricing (VP1) now leads because Gonka's live rate is verifiably the lowest published; tiering demoted (routing is commoditized).

### VP1: The Lowest Published Per-Token Price -- and Your Agent Stops Paying for Context It Already Has

**Headline:** Near-zero per-token pricing, and Gonka remembers your agent's conversation server-side so heartbeats cost almost nothing.

**What this means for developers:** OpenClaw agents resend their full system prompt and workspace context (~9,600 tokens) on every heartbeat -- 48 times per day at default 30-minute intervals. That is 460,800 tokens per day that generate zero user-facing value (pricing analysis: Section 3, Casual tier). Two things make Gonka the cheapest way to run that workload: (1) per-model broker retail pricing of ~$0.018-0.35 per 1M tokens (Gonka24: M2.7 $0.018/$0.072, K2.6 $0.055/$0.32, GLM-5.2 $0.095/$0.30; GonkaBroker: $0.30-0.35 flat), listed by price trackers as the cheapest provider for the models it serves -- versus $0.95-$4.50 per 1M for the same Kimi/MiniMax models on Together or AkashML; and (2) server-side session persistence via `/v1/sessions` maintains conversation state across requests, so repeated context is never retransmitted or billed at all, where competitors' prompt caching still bills cached input at 10-20% of the standard rate.

**Supporting evidence:**
- Live pricing: pricepertoken.com lists Gonka as cheapest provider for Kimi K2.6 and MiniMax M2.7; broker retail is per-model -- Gonka24 M2.7 $0.018/$0.072, K2.6 $0.055/$0.32, GLM-5.2 $0.095/$0.30; GonkaBroker $0.30-0.35/1M flat. The ~$0.0003/1M figure is the raw network rate (subsidized, utilization-dependent) -- quote per-model broker retail externally, never the network rate or the M2.7 floor as a blanket rate
- Competitive matrix verdict: Agent Sessions -- **WIN** (server-side session persistence on the chat completions API; OpenAI now offers server-side state via Responses/Conversations, see Section 5)
- Apr 2026 modeled deltas ($218/mo -> $59/mo Active tier, $47/mo -> $13/mo Casual) were computed against uncached competitor rates and Scenario B pricing; both inputs are obsolete. Recompute against July 2026 cached rates and live Gonka pricing before using any dollar figure externally.

**Resonates most with:**
- **Weekend Builder** -- cost per task is their #1 decision driver; heartbeat waste is their primary pain point (developer personas: Weekend Builder, Decision Driver #1)
- **Startup CTO** -- multi-agent heartbeat overhead scales linearly with channel count; 6 channel-agents = 288 heartbeats/day (developer personas: Startup CTO, Pain Points)

**Proof point:** At the Active tier (6 channel-agents, 200 messages/day), heartbeats consume 51% of all tokens. Gonka's sessions reduce this to approximately 10%, saving 2.2M tokens per day (pricing analysis: Section 3, Active tier observation -- token mechanics remain valid; dollar translation must use live rates).

---

### VP2: The Right Model for Every Task -- Without Maintaining a Router

**Headline:** Classification on the cheap tier, complex reasoning on the strong one -- built into the API, not bolted on as middleware.

**What this means for developers:** OpenClaw agents perform diverse tasks within a single workflow: classifying inputs (cheap), planning approaches (moderate), executing complex reasoning (expensive). Gonka's `X-Gonka-Tier` header and content-aware auto-routing (ARCHITECTURE.md: mapping table) let agents select cost-performance tiers per request without application code changes.

**Honesty update (July 2026):** Cost-based routing is no longer unique. ClawRouter ships with/alongside OpenClaw as a governance surface, and multiple third-party routers exist (BlockRunAI's ClawRouter, iblai/claw-router, ClawRoute), claiming 70-92% savings; tiered routing is standard enterprise practice. The residual claim is convenience and placement: Gonka's tiering is server-side and zero-install, so it composes with sessions (a client-side router cannot route a request whose context lives on Gonka's servers). Do not use "no other provider offers automatic tiering" or "all four competitors scored LOSE" externally -- both are stale.

**Supporting evidence:**
- Server-side tiering requires no router install, no local classifier, no separate config (ARCHITECTURE.md: X-Gonka-Tier)
- Using multiple models "is the norm" per the LangChain State of Agent Engineering report (survey Nov 18-Dec 2, 2025, n=1,340), indicating demand for task-specific routing. Externally, cite the report's verbatim "multiple models is the norm" phrasing -- the previously quoted "76%" figure could not be verified in the published report (verified figures: 57% have agents in production, 89% have implemented observability, 32% cite quality as the top barrier); re-check against the report before using any percentage
- Agentic workloads now generate more than half of all output tokens on OpenRouter, surpassing human usage, and 67% of enterprises consume >1B tokens/month (OpenRouter/a16z State of AI, May 2026; Deloitte 2026) -- multi-task agent workflows are the dominant demand pattern

**Resonates most with:**
- **Startup CTO** -- one less component to operate; server-side tiering composes with sessions (developer personas: Startup CTO, Pain Point #2)
- **Weekend Builder** -- automatic optimization without installing or understanding a router (developer personas: Weekend Builder, Decision Driver #2)

**Proof point:** Gonka's 3-tier routing (lite/mid/full quantization) lets an agent use a heavily quantized model for classification at a fraction of full-model cost, then route complex reasoning to the full model -- via a single header or automatic content analysis, no middleware (ARCHITECTURE.md: architecture-to-message mapping, X-Gonka-Tier).

---

### VP3: One URL Change, Everything Else Just Works

**Headline:** Add Gonka to your OpenClaw agent in 90 seconds -- change the base URL, keep your code.

**What this means for developers:** Gonka's OpenAI-compatible API means switching from OpenRouter or Together AI requires editing one JSON block in `openclaw.json` -- setting `baseUrl`, `apiKey`, and `api: "openai-completions"`. No SDK changes, no new libraries, no code modifications. The same `/v1/chat/completions` endpoint, the same streaming format, the same function calling syntax. Every OpenClaw integration test passes against Gonka's API (ARCHITECTURE.md: architecture-to-message mapping, OpenAI-compatible API).

**Supporting evidence:**
- Competitive matrix verdict: Streaming -- **TIE**; Tool Calling -- **TIE** (competitive matrix: Gonka matches the standard that OpenClaw expects)
- Kimi K2-family models are stable across 200-300 sequential tool calls in testing (competitive matrix: Section 3, verified against v1.2 integration tests on K2.5)
- OpenClaw's `api: "openai-completions"` config pattern makes Gonka a drop-in custom provider (ARCHITECTURE.md: OpenClaw Configuration Pattern)

**Resonates most with:**
- **Weekend Builder** -- ease of integration is their #2 decision driver; any friction beyond copy-pasting a config snippet is a dealbreaker (developer personas: Weekend Builder, Decision Driver #2)
- **Startup CTO** -- needs to evaluate without committing engineering resources to a provider migration (developer personas: Startup CTO, Activation stage)
- **Privacy-First Builder** -- evaluates by testing prompts that other providers would block; drop-in compatibility means instant testing (developer personas: Privacy-First Builder, Activation stage)

**Proof point:** Three fields in `openclaw.json` is all it takes: `baseUrl: "https://api.gonka.ai/v1"`, `apiKey: "${GONKA_API_KEY}"`, `api: "openai-completions"`. Verified working with OpenClaw, CrewAI, and LangGraph integration test suites (ARCHITECTURE.md: Component 6, OpenClaw Configuration Pattern).

---

### VP4: No Content Filters, No Prompt Logs, No Permission Required

**Headline:** Your agent processes every prompt without filtering, refusal, or centralized logging.

**What this means for developers:** OpenAI and Anthropic enforce content policies that block legitimate use cases -- legal adversarial arguments, security exploit analyses, medical condition discussions, politically sensitive content. Agents processing these tasks hit refusals that break multi-step workflows. Gonka serves open-weight Kimi K2-family models with no built-in content filtering, on decentralized infrastructure with no central authority that can impose content policies or review prompts (competitive matrix: content filtering comparison).

**Supporting evidence:**
- Kimi K2-family models are open-weight with no content filtering (developer personas: Privacy-First Builder, Gonka Value Proposition)
- Decentralized infrastructure means no single entity aggregates all prompt logs (developer personas: Privacy-First Builder, Gonka Value Proposition)
- Privacy-First Builder persona exists specifically because content filtering on OpenAI/Anthropic blocks legitimate use cases (developer personas: Privacy-First Builder, Pain Point #1)

**Resonates most with:**
- **Privacy-First Builder** -- data privacy and censorship resistance is their #1 non-negotiable requirement (developer personas: Privacy-First Builder, Decision Driver #1)

**Proof point:** OpenAI content filtering: strict. Anthropic content filtering: strict. Gonka content filtering: none (open-weight model, decentralized infrastructure, no content policy team). Verified: prompts that trigger refusals on OpenAI/Anthropic complete without filtering on Gonka (developer personas: Privacy-First Builder, Activation stage).

> **Honesty note:** Current privacy guarantee is architectural (no central log aggregation), not cryptographic (TEE-based encrypted inference is not yet built). This distinction must be stated clearly in all privacy-related messaging. Overclaiming damages credibility irreparably in security communities. Note also that broker access (GonkaGate etc.) inserts a third party between the developer and the network -- privacy claims must account for the broker layer. (PITFALLS.md: Pitfall 1; developer personas: Privacy-First Builder, Objection #1)

---

### VP5: Inference Gets Cheaper as the Network Grows

**Headline:** More GPU hosts join, competition drives prices down -- the opposite of centralized provider pricing.

**What this means for developers:** Traditional inference providers increase margins as they scale. Gonka's decentralized network creates the opposite dynamic: as more GPU hosts join (attracted by GNK mining rewards), they compete for inference requests, driving per-token costs down. This is no longer theoretical -- the live blended rate, recalculated every block from utilization, is currently the lowest published price on the market (partly because the network is underutilized and rewards subsidize hosts; be explicit about this when quoting the rate, and do not promise it holds at high utilization). Sprint Consensus ensures 98% of GPU power serves actual inference requests (ARCHITECTURE.md: architecture-to-message mapping, Sprint Consensus).

**Supporting evidence:**
- Live blended per-token rate published and utilization-driven; broker retail schedules now public (pricepertoken.com/endpoints/gonka; gonkabroker.com; gonka24.com)
- 98% productive compute via Sprint Consensus (ARCHITECTURE.md: USP #3)
- Mining rewards subsidize GPU hosting costs, enabling below-market pricing (ARCHITECTURE.md: architecture-to-message mapping, GNK mining rewards)
- Sector context: AI/DePIN compute networks with real fee revenue decoupled from speculative tokens in the 2026 bear market (Bittensor $43M Q1 revenue; NVIDIA CEO endorsement of decentralized training). Do NOT say "AI tokens were the only profitable crypto sector in Q1 2026" -- the defensible claim is that AI-linked tokens posted the smallest sector decline (~-14%) in Q1 2026, with revenue-generating leaders (TAO, FET, RENDER) posting outright gains; sector cap ~$20.9B by May 2026. Investor-facing materials only
- Demand context: OpenRouter weekly volume "exploded to 25T tokens" per its May 26, 2026 Series B release (up from ~5T six months prior), running ~100T tokens/month across 8M+ users; Chinese open-source models capture ~61% of global OpenRouter token usage and the DeepSeek/Kimi/Qwen family tops the weekly token rankings (DeepSeek-V4-Flash alone settled 3.43T tokens in one May week) -- direct empirical support for the Kimi/MiniMax open-weight strategy. Cite 25T/week (Businesswire) as the hard number; the ~28T-29T/week mid-2026 figures are third-party trackers (Businesswire May 26, 2026; openrouter.ai/state-of-ai)

**Resonates most with:**
- **Startup CTO** -- watching inference costs grow linearly with agent count; a provider with structurally declining costs aligns with runway management (developer personas: Startup CTO, Decision Driver #2)
- **Weekend Builder** -- benefits from lower costs over time without negotiating enterprise discounts (developer personas: Weekend Builder, Decision Driver #1)

**Proof point:** Sprint Consensus dedicates 98% of GPU compute to serving inference requests, with only 2% spent on consensus, versus proof-of-work chains that spend 100% of compute on hash puzzles (ARCHITECTURE.md: architecture-to-message mapping, 98% productive compute).

---

## 4. Per-Persona Differentiation

### 4.1 Weekend Builder

**Persona-specific positioning statement:** Gonka is the cheapest way to run an always-on OpenClaw agent -- the lowest published per-token rate on the market, plus server-side sessions that eliminate the heartbeat tax.

**Top 3 messages ranked by cost (primary decision driver):**

1. **"Your heartbeats are half your bill. Gonka eliminates them."** At the Casual tier, heartbeats consume 44% of monthly tokens -- 460,800 tokens per day generating zero user-facing value. Gonka's sessions reduce this to ~92,000 tokens/day. (pricing analysis: Section 3, Casual tier; Section 5, Gonka hidden cost analysis)

2. **"The cheapest listed provider for the models it serves."** Price trackers list Gonka as the lowest-priced provider for Kimi K2.6 and MiniMax M2.7. Broker retail is per-model: Gonka24 charges $0.018/$0.072 per 1M for MiniMax M2.7, $0.055/$0.32 for Kimi K2.6, and $0.095/$0.30 for GLM-5.2; GonkaBroker runs $0.30-0.35 per 1M flat -- versus $0.95+ for the same models elsewhere. Caveats in all external use: quote the rate for the model the workload actually runs on (the $0.018/$0.072 floor is M2.7 only), and quote broker retail, not the ~$0.0003/1M utilization-floating, subsidy-assisted network rate. (pricepertoken.com/endpoints/gonka; gonka24.com; gonkabroker.com; supersedes the Apr 2026 "$13 vs $47" Scenario B comparison, which must not be quoted)

3. **"Add Gonka in 90 seconds. No wallet, no tokens, no SDK."** Three fields in openclaw.json. API key via GitHub OAuth. No credit card for the free tier. No blockchain interactions. (ARCHITECTURE.md: OpenClaw Configuration Pattern; PITFALLS.md: Pitfall 2)

**Lead with:** Cost savings (live tracker listings, not stale dollar projections), ease of setup (90 seconds, 3 fields), heartbeat waste elimination
**Never lead with:** Decentralization, GNK tokens, network economics, Sprint Consensus, mining rewards

**Elevator pitch (30 seconds):**
> "You know how your OpenClaw agent costs way more than it should? Half your token bill is heartbeats -- your agent resending context every 30 minutes. Gonka keeps that context server-side, so heartbeats cost almost nothing, and its per-token rate is currently the cheapest listed anywhere. Same agent, same code, one config change. It takes 90 seconds to set up."

---

### 4.2 Startup CTO

**Persona-specific positioning statement:** Gonka gives your team production-grade agent infrastructure with built-in session persistence, server-side model tiering, and webhook notifications -- fewer moving parts than the router-plus-cache-plus-middleware stack your engineers currently operate.

**Top 3 messages ranked by reliability (primary decision driver):**

1. **"Sessions, tiering, and webhooks -- built in, not bolted on."** Client-side routers (ClawRouter and friends) now solve model routing, but you still install, configure, and operate them, and they cannot manage server-side state. Gonka provides all three natively: `/v1/sessions` for state persistence, `X-Gonka-Tier` for server-side routing, and `/v1/webhooks` for event-driven agent architecture. (competitive matrix: Agent Sessions -- WIN; tiering claim softened per July 2026 revalidation; developer personas: Startup CTO, Pain Point #2)

2. **"Materially lower inference costs at scale."** Sessions cut the ~51% heartbeat token share to ~10%, and the per-token rate is the lowest currently listed. The Apr 2026 "$218 -> $59/month" Active-tier projection was built on obsolete Scenario B and uncached competitor pricing -- do not quote it; run the staging test instead. (pricing analysis: Section 3 token mechanics; live pricing per trackers)

3. **"Your staging test will prove it -- one agent, one day, real numbers."** Deploy one agent on staging with Gonka as provider. Measure p95 latency, daily token consumption, and heartbeat cost. Compare to your current provider with its caching enabled. The cost difference will be visible in 24 hours. (developer personas: Startup CTO, Activation stage)

**Lead with:** Agent-native features (sessions, tiering, webhooks), engineering time savings, staging-measurable cost reduction
**Never lead with:** Decentralization philosophy, token economics, blockchain architecture, "unstoppable network" language

**Elevator pitch (30 seconds):**
> "Your agents are spending 51% of their tokens on heartbeats, and your team operates a router and cache config to contain it. Gonka has session persistence, server-side model tiering, and webhooks built into the API -- no middleware to run -- and its per-token rate is currently the cheapest listed anywhere. Point one staging agent at it for a day and compare the numbers."

---

### 4.3 Privacy-First Builder

**Persona-specific positioning statement:** Gonka is an inference API where open-weight models run on decentralized infrastructure with no content policy, no centralized prompt logging, and no authority that can impose filtering after the fact.

**Top 3 messages ranked by privacy/censorship resistance (primary decision driver):**

1. **"No content filter. No refusals. Your prompt, your responsibility."** Gonka serves open-weight Kimi K2-family models with no built-in content filtering. Prompts that trigger refusals on OpenAI and Anthropic -- legal adversarial arguments, security analyses, medical discussions -- complete without interference on Gonka. (developer personas: Privacy-First Builder, Pain Point #1; competitive matrix: content filtering comparison)

2. **"Decentralized means no central prompt log."** There is no single Gonka entity that aggregates all prompts and responses. No content policy team reviews your agent's conversations. No terms-of-service update can retroactively restrict what your agent can process. The infrastructure code is open source at github.com/mitgor/gonka-ai-infrastructure -- you can audit it yourself. Note the caveat: if you access Gonka through a third-party broker, the broker sees your traffic -- direct network access is the stronger privacy posture. (developer personas: Privacy-First Builder, Gonka Value Proposition; PITFALLS.md: Pitfall 1)

3. **"Agent features that self-hosting cannot match."** Self-hosted vLLM gives you privacy but not session persistence, automatic tiering, memory API, or webhook notifications. Gonka gives you both: the privacy posture of decentralized open-weight inference AND the agent-native features of a managed platform. (developer personas: Privacy-First Builder, Gonka Value Proposition #2)

**Lead with:** No content filtering (specific examples of blocked use cases), open-source infrastructure (auditable), practical privacy guarantees (what is real today)
**Never lead with:** Decentralization as philosophy, Web3 ideology, blockchain, "trustless" or "permissionless" language, privacy claims beyond what is currently implemented

**Elevator pitch (30 seconds):**
> "You are running sensitive workloads on self-hosted vLLM because OpenAI and Anthropic block your prompts. Gonka serves open-weight Kimi models with no content filtering, on decentralized infrastructure with no central prompt logging. You get the privacy of self-hosting plus session persistence, automatic tiering, and webhooks that vLLM does not have. The infrastructure code is open source -- audit it yourself."

---

## 5. Architecture-to-Message Mapping

Every Gonka technical feature mapped to a developer benefit statement, proof point, and competitive context. Competitive context revalidated 2026-07-18.

| Technical Feature | What It Does (Internal) | Developer Benefit Statement | Proof Point | Competitive Context (July 2026) |
|---|---|---|---|---|
| **Decentralized GPU network** | Inference runs on distributed GPU hosts incentivized by GNK mining rewards, not centralized data centers | Your inference runs on a network with no single point of failure and no single authority controlling access or content | 98% of GPU compute serves inference requests via Sprint Consensus (ARCHITECTURE.md: USP #3) | OpenRouter: centralized routing proxy. Together AI: own GPU clusters (centralized). OpenAI/Anthropic: centralized with content policies. Akash: decentralized, and since Q1 2026 offers Akash Agents (one-click agent deployment) plus AkashML managed inference -- no longer "no agent features" (Messari State of Akash Q1 2026) |
| **GNK mining rewards** | GPU hosts earn GNK tokens for serving inference, subsidizing their compute costs and driving competition | Inference costs decrease as more GPU hosts join the network and compete for your requests | Live blended rate recalculated per block; currently the lowest listed price for served models (pricepertoken.com) | OpenRouter: passthrough token pricing plus a payment-processing fee on credit purchases (5.5% card / 5.0% crypto) -- no supply-side cost-reduction mechanism. Together AI: fixed pricing on own clusters |
| **98% productive compute** | Sprint Consensus uses 98% of GPU power for useful inference, 2% for consensus verification | Every GPU cycle serves your requests. No compute wasted on hash puzzles or proof-of-work busywork | 98% productive vs 0% productive on traditional PoW chains (ARCHITECTURE.md: architecture-to-message mapping) | No centralized competitor wastes compute on consensus, but no decentralized competitor matches 98% productivity (provider landscape map: decentralized segment) |
| **OpenAI-compatible API** | Drop-in replacement for OpenAI /v1/chat/completions endpoint with identical request/response format | Change one URL in your openclaw.json. Everything else -- streaming, tool calling, function format -- just works | Verified compatible with OpenClaw, CrewAI, and LangGraph integration test suites; K2-family stable across 200-300 sequential tool calls (competitive matrix: Section 3) | OpenRouter: also OpenAI-compatible. Together AI: also OpenAI-compatible. AkashML: also OpenAI-compatible (since Nov 2025). Raw Akash: manual vLLM setup |
| **X-Gonka-Session-ID** | Server-side conversation persistence via /v1/sessions API; state maintained across requests without client re-sending context | Your agent remembers context without paying for it twice. Heartbeats send only new data, not the full conversation history every 30 minutes | ~80% reduction in heartbeat token overhead; Casual tier drops from 31.5M to ~12.6M tokens/month (pricing analysis: Section 5 -- token mechanics; dollar figures stale) | OpenAI: Responses + Conversations API now provides server-side stateful conversations on its PRIMARY surface (Assistants API shuts down Aug 26, 2026) -- no longer a Gonka-only capability; Gonka's edge is sessions on the chat-completions-compatible surface OpenClaw uses. OpenRouter: stateless passthrough with caching passthrough. Anthropic/Together: no session management, 90%-off / default-on caching respectively |
| **X-Gonka-Tier header** | 3-tier auto-routing (lite/mid/full quantization); agents select cost-performance tier per request via header or automatic content analysis | Classification on the cheap tier, reasoning on the strong one -- server-side, with no router to install or operate | 3 quantization tiers with automatic content-aware routing (competitive matrix: Section 2) | Routing is commoditized client-side: ClawRouter ships with/alongside OpenClaw; BlockRunAI ClawRouter, iblai/claw-router, ClawRoute claim 70-92% savings. Gonka's residual advantage: server-side placement (composes with sessions), zero install. Do not claim uniqueness |
| **Memory API** | Persistent key-value memory store at /v1/memory with TF-IDF search for retrieval across sessions | Give your agent a permanent memory that persists across conversations and survives restarts | Functional keyword-based retrieval via TF-IDF; combined with sessions provides both short-term (session) and long-term (memory) context (competitive matrix: Section 5) | Prompt caching is now universal (OpenAI/Anthropic 90% off cached, Together default-on, DeepInfra, Fireworks, Moonshot API, OpenRouter passthrough) but caching discounts repeated context, it does not store persistent memory. Memory API remains differentiated vs OpenRouter/Together/Anthropic |
| **Webhook notifications** | Push notifications for async task completion, cost threshold alerts, and model updates via /v1/webhooks | Stop polling. Get notified when async tasks complete, costs exceed thresholds, or models update | Event-driven architecture eliminates polling loops (developer personas: Startup CTO, Gonka Value Proposition #3) | No compared provider offers inference-layer webhook notifications. Developers currently implement their own polling or callback mechanisms (ARCHITECTURE.md: architecture-to-message mapping) |
| **Multi-model routing** | Route requests to different vLLM backends based on model parameter in the request | One API key, one endpoint -- specify the model and Gonka routes to the right backend | Multi-model routing built in v1.2 infrastructure; network currently serves Kimi K2.6 and MiniMax M2.7 (Qwen3-235B retired Jun 25, 2026 per Proposal 78, which also removed K2.6 -- restored Jun 26 per Proposal 79, second removal/re-bootstrap mid-Jul; M2.7 is the sole PoC model), with GLM-5.2 imminent (introduced on-network Jun 26 via Proposal 79 at weight 2.47; Gonka blog "coming soon"; Gonka24 GLM-5.2 rate card live) (pricepertoken.com; GonkaBroker menu; gonka.ai/docs/network-updates) | OpenRouter: multi-model routing is their core product (400+ models from 60+ providers), WIN on breadth. Together AI: 200+ models. Gonka LOSE on breadth, though a third family (GLM-5.2, leader on open agent benchmarks) narrows the "no frontier-class option" criticism (competitive matrix: Section 8) |
| **Open-weight model serving (Kimi K2.6, MiniMax M2.7)** | 1T-parameter MoE Kimi K2.6 with native tool calling and 256K context, plus MiniMax M2.7 (sole PoC model since Jun 25, 2026) | Strong open-weight agent models -- purpose-built for tool calling and multi-step reasoning at a fraction of frontier model cost | Stable across 200-300 sequential tool calls; 256K context window (K2-family tool-call stability verified against v1.2 tests on K2.5; K2.6 live per pricepertoken.com) | **Model currency:** Gonka serves current-generation K2.6; upstream, Moonshot shipped K2.7-Code (Jun 2026) and K3 (launched Jul 16, 2026: 2.8T MoE, 1M context, open weights ~Jul 27; #1 Frontend Code Arena). MiniMax's flagship is now M3 (Jun 1, 2026: 428B/23B active, 1M context, multimodal) -- M2.7 is one generation behind it. Open-weight SWE-bench Verified leader is DeepSeek V4 Pro at 80.6% (Think Max; tied with Gemini 3.1 Pro), ahead of MiniMax M2.5 (80.2%) and GLM-5 (77.8%). AkashML serves K2.6 at $0.95/$4.00 -- Gonka undercuts it via brokers. Frontier comparisons are now vs GPT-5.x ($2.50-$5/M input) and Claude Opus 4.8 ($5/$25) / Sonnet 5 ($3/$15) -- not GPT-4o (retired Apr 2026) or Opus 4 ($15/$75, obsolete). Roadmap: GLM-5.2 imminent (third family; leads open agent benchmarks); K3 as frontier tier once weights land; evaluate MiniMax M3 |
| **vLLM serving** | Industry-standard inference serving framework with continuous batching, PagedAttention, and optimized throughput | Production-grade inference infrastructure, not a weekend project. The same serving stack that Together AI and DeepInfra use | vLLM is the industry standard for open-model serving; continuous batching optimizes GPU utilization; PagedAttention reduces memory waste (ARCHITECTURE.md: architecture-to-message mapping) | Together AI and DeepInfra also use optimized serving. Gonka matches on serving quality but differentiates on infrastructure model (decentralized) and agent features (provider landscape map: dedicated inference segment) |

---

## 6. Vocabulary Guidelines

### 6.1 Never-Say List

These terms must never appear in developer-facing content (landing pages, documentation, blog posts, API reference, error messages, community replies, social media). They trigger the "is this a crypto thing?" reaction that causes immediate tab-close among Web2 developers (PITFALLS.md: Pitfall 7).

| Internal Term | Why It Alienates | Developer-Facing Alternative |
|---|---|---|
| **Staking** | Implies financial risk, lock-up periods, and crypto speculation. Developers associate staking with DeFi protocols and rug pulls. | "Provider requirements" or "compute commitment" (for host-facing docs); omit entirely in developer-facing content |
| **Epochs** | Meaningless to Web2 developers. Signals blockchain infrastructure that they do not want to understand. | "Cycles" or "intervals" if timing context is needed; prefer specific durations ("every 4 years") |
| **Validators** | Implies a blockchain consensus mechanism requiring technical understanding of distributed systems. | "Network nodes" or "compute providers" or simply "GPU hosts" |
| **Gas** | Immediately signals Ethereum-style transaction fees. Developers will assume they need ETH or tokens to use the API. | "API usage" or "compute cost" -- never suggest per-transaction blockchain fees |
| **Slashing** | Implies punitive loss of staked tokens. Sounds adversarial and risk-laden. | "Quality enforcement" or "performance standards" |
| **Governance proposals** | Signals DAO-style voting mechanisms that developers do not want to participate in to use an inference API. | "Feature requests" or "community feedback" |
| **DePIN** | Crypto-insider acronym (Decentralized Physical Infrastructure Networks). Meaningless and alienating to target audience. | "Distributed compute network" or "decentralized infrastructure" (but only in technical context, never as a headline) |
| **Web3** | Loaded term associated with crypto hype, NFTs, and speculative token projects. Triggers skepticism in mainstream developers. | Do not use. Describe specific capabilities instead: "open infrastructure," "community-operated compute" |
| **Tokenomics** | Insider term for token economic design. Signals crypto project, not API provider. | "Network economics" or "pricing model" -- developers want to know what things cost, not how your token works |
| **Consensus mechanism** | Technical blockchain term that implies developers need to understand distributed consensus to use the API. | "How the network verifies quality" -- only in an optional technical deep-dive, never in onboarding or marketing |
| **Mining** | Signals cryptocurrency mining with its associations of energy waste, GPU hoarding, and environmental harm. | "Hosting" or "serving inference" -- GPU hosts serve inference requests, they do not "mine" tokens |
| **On-chain** | Signals blockchain transactions. Developers will assume they need a wallet and will encounter transaction fees. | "Verified" or "recorded" if provenance matters; omit entirely when describing developer-facing features |
| **Wallet** | Single most alienating word for Web2 developers. If this word appears before "API key" on any page, you have lost the developer. | "Account" -- developers have accounts, not wallets. Wallet should only appear in GPU host documentation and agent-payments (x402) documentation, never in the human-developer onboarding path |
| **Token** (as cryptocurrency) | Ambiguous and loaded. In developer context, "token" means LLM tokens. Using it for GNK currency creates confusion and crypto association. | "Credits" for API usage currency. "GNK" when specifically discussing the network token in investor/host-facing materials only |
| **Smart contract** | Signals Ethereum/Solidity development. Developers will think they need to deploy contracts to use inference. | Omit from developer-facing content. If needed in technical architecture docs: "automated agreement" or "network rule" |
| **Decentralized** (as headline) | Not inherently bad, but leading with it signals a crypto project rather than an API provider. Use as supporting context, not headline. | Use in supporting position: "...powered by decentralized infrastructure" not "Decentralized AI inference platform" (PITFALLS.md: Pitfall 1) |

> **Scope note (July 2026):** The "no wallet, no tokens" rule applies to the three human developer personas. It does NOT preclude a separate, clearly segmented agent-payments track: x402 agent payments went mainstream in 2026. The x402 Foundation (Linux Foundation) reached operational launch July 14, 2026 with 40 member organizations across three tiers -- the full premier roster is Adyen, AWS, American Express, Circle, Cloudflare, Coinbase, Fiserv, Google, Mastercard, Monad Foundation, MoonPay, Ripple, Shopify, Solana Foundation, Stellar Development Foundation, Stripe, and Visa (drop Anthropic/Vercel from member lists; they do not appear on the premier roster; the inclusion of PSPs Adyen and Fiserv underlines the payments-industry weight). Volume is real, not test traffic: in the 30 days ending ~July 15, 2026 the protocol processed ~75M transactions moving ~$24M (~$800K/day, avg ~$0.32/tx) between ~94K buyers and ~22K sellers, predominantly sub-dollar USDC payments; Chainalysis reports 95% of payment value is now in transactions above $1 (up from 49% in early 2025). AWS CloudFront/WAF x402 support is GA and Cloudflare's Monetization Gateway opened applications July 1. Position x402 within the three-layer 2026 agentic-payments stack when talking to enterprise buyers: x402 for machine-to-machine execution/micropayments, AP2 for authorization (signed Intent/Cart/Payment mandates as W3C Verifiable Credentials; 60+ partners; in production with Gemini Spark since Google I/O, May 19, 2026 -- Google has since donated AP2 to the FIDO Alliance, so say "AP2, now under the FIDO Alliance," not "Google's AP2"), and ACP for agent checkout (an open standard co-created by Stripe, OpenAI, and Meta; live as Instant Checkout for US ChatGPT Free/Plus/Pro users buying from US Etsy sellers, with 1M+ Shopify merchants announced and Salesforce support announced) -- x402 is the correct layer for agent-procured inference, but enterprise buyers will ask about AP2/ACP. Caveat the layer split: AP2 v0.2 adds "Human Not Present" payments (agents executing payments autonomously), so the clean "x402=execution, AP2=authorization" separation is a simplification, not a hard boundary. BlockRunAI's ClawRouter already sells OpenClaw inference via USDC micropayments over x402 with wallet-signature auth, and ClawRouter clones are proliferating. Gonka, already a crypto network, has a natural x402 story for the agent-as-customer segment; keep it on separate pages, never in the human onboarding path.

### 6.2 Approved Vocabulary

Every crypto/blockchain concept that might appear in developer-facing content, mapped to its approved alternative.

| Concept | Approved Term | Usage Example |
|---|---|---|
| The Gonka network | "Gonka" or "the Gonka network" | "Deploy on Gonka" -- not "Deploy on the Gonka decentralized network" |
| GNK token (in dev context) | "Compute credits" or "API credits" | "Earn credits toward inference costs" -- not "Earn GNK tokens" |
| GNK token (in host context) | "GNK rewards" | "GPU hosts earn GNK rewards for serving inference" (host docs only) |
| GPU hosts earning rewards | "GPU providers" or "compute providers" | "Thousands of GPU providers compete to serve your requests" |
| Sprint Consensus | "Quality verification" | "Every response is quality-verified before delivery" (simple) |
| Mining/proof-of-work | "Serving inference" | "GPU providers serve inference requests and earn rewards" |
| Node operators | "GPU hosts" or "compute providers" | "Our network of GPU hosts provides redundant infrastructure" |
| Token emission schedule | "Network growth incentives" | "Incentives attract more GPU providers, driving costs down" |
| Proof of useful work | "Productive compute" | "98% of GPU power serves your requests" |
| Decentralized infrastructure | "Distributed infrastructure" or "redundant infrastructure" | "Gonka runs on distributed infrastructure across thousands of GPU hosts" |
| Permissionless | "Open access" or "no restrictions" | "Open access inference with no content filtering" |
| Trustless | "Independently verifiable" | "Infrastructure code is open source and independently verifiable" |
| Block rewards | "Host earnings" | "GPU hosts earn competitive rewards for providing compute" |
| Network fees | "Usage-based pricing" | "Pay only for what you use -- standard per-token pricing" |
| DAO / governance | "Community input" or "feedback" | "Share feedback to shape the product roadmap" |
| Mainnet / testnet | "Production" / "staging" | "Gonka's production network" -- not "Gonka mainnet" |
| Gas fees | (never reference) | Omit. There are no per-transaction blockchain fees for developers |
| Wallet connection | "API key" | "Get your API key in 60 seconds via GitHub OAuth" |
| On-chain verification | "Automated quality checks" | "Every inference response passes automated quality checks" |

### 6.3 Context Rules

Crypto terminology is acceptable in specific, clearly delineated contexts where the audience expects it:

**Acceptable contexts:**

1. **"How It Works Under the Hood" documentation section.** A clearly labeled optional deep-dive for technically curious developers. Gate this behind a click ("Want to understand the network architecture?") so developers never encounter it during onboarding or standard API usage. Acceptable terms: consensus mechanism, Sprint Consensus, mining rewards, GNK token, proof of useful work.

2. **Investor-facing materials.** Pitch decks, token economics documents, and materials for crypto-native investors expect and require blockchain terminology. Use full crypto vocabulary. These materials must never be linked from developer-facing pages.

3. **GPU host documentation.** Documentation for GPU providers who join the network to earn GNK rewards. These users are crypto-aware (they are running nodes for token incentives) and expect terms like staking, rewards, slashing penalties, and epochs. Host docs should be a separate documentation section from developer API docs.

4. **Agent-payments (x402) documentation.** A future agent-as-customer track (wallet-signature auth, USDC micropayments over x402) may use wallet/crypto vocabulary because its audience -- agent builders integrating payment rails -- expects it. Must live under its own section, never linked from the human quickstart.

5. **Conference talks at crypto/Web3 events.** When presenting at Token2049, ETHDenver, or similar events, use the audience's vocabulary. But even here, lead with the developer use case first, then explain the infrastructure.

6. **Internal communications.** Team Slack, internal docs, planning documents -- use whatever terminology is efficient for internal understanding.

**Never acceptable:**

- Landing page (docs.gonka.ai homepage)
- API reference documentation
- Quickstart guide
- Pricing page
- Error messages returned by the API
- Social media posts targeting developers (Twitter/X, Reddit, Hacker News)
- Blog posts about developer features
- OpenClaw integration documentation
- Community replies in OpenClaw Discord or GitHub

---

## 7. Competitive Differentiation Statements

Per-persona competitive positioning against the single competitor each persona is most likely comparing Gonka to (ARCHITECTURE.md: Anti-Pattern 3, focus on 2-3 per persona, not all competitors).

### 7.1 Weekend Builder: Gonka vs OpenRouter

**The competitor context:** OpenRouter is the default inference provider in OpenClaw -- zero configuration required. It is the path of least resistance. The Weekend Builder has never changed their provider and sees no reason to unless the cost savings are dramatic and the switch is trivially easy. Note: OpenRouter passes through provider prompt caching automatically (cached input at 10-20% of standard rates for many models), and its 5.5% figure is a payment-processing fee on card-funded credit purchases (5.0% crypto), not a per-token markup -- do not describe OpenRouter heartbeats as "fully unoptimized." (competitive matrix: Key Takeaway #3, revised; developer personas: Weekend Builder, Objection #2)

**Differentiation statement:**

> Unlike OpenRouter, which still bills your agent's repeated context at cached-input rates (10-20% of the input price) plus a payment-processing fee when you top up by card, Gonka maintains your agent's conversation server-side so heartbeats retransmit nothing at all -- and its live per-token rate is currently the cheapest listed on the market. One config change. (pricing analysis: Section 3 token mechanics; live pricing per pricepertoken.com)

**Supporting claims:**

| Dimension | OpenRouter | Gonka | Verdict |
|---|---|---|---|
| Agent Sessions | Stateless passthrough; caching passthrough only, session management client-side | Server-side session persistence via /v1/sessions API | Gonka **WIN** (competitive matrix) |
| Pricing | Provider list-price passthrough + payment-processing fee on credit purchases (5.5% card / 5.0% crypto) | Per-model broker retail $0.018-0.35/1M (Gonka24: M2.7 $0.018/$0.072, K2.6 $0.055/$0.32; GonkaBroker flat $0.30-0.35; network rate utilization-dependent, partly subsidized) | Gonka advantage at current utilization (live trackers) |
| Model Breadth | 400+ models from 60+ providers | 2 model families (Kimi K2.6, MiniMax M2.7), GLM-5.2 imminent | OpenRouter **WIN** (competitive matrix) |
| Setup | Built-in to OpenClaw, zero config | Custom provider, 3 fields in openclaw.json | OpenRouter advantage (developer personas) |

**Honest concession:** OpenRouter offers hundreds of models and zero-config OpenClaw integration, and its caching passthrough already blunts the worst of heartbeat cost. Gonka's two-family catalog (three once GLM-5.2 lands) and manual configuration are real disadvantages. The cost savings must be compelling enough to justify the switch. (competitive matrix: Model Breadth -- Gonka LOSE)

---

### 7.2 Startup CTO: Gonka vs Together AI

**The competitor context:** Together AI is the performance pick for teams running open Kimi models at scale: own GPU clusters, default-on prompt caching, and current pricing of K2.6 at $1.20 input / $0.20 cached / $4.50 output per 1M and K2.7-Code at $0.95 / $0.19 cached / $4.00. Together no longer lists K2.5 on its serverless pricing page -- the Apr 2026 "$0.50/$2.50 lowest verified K2.5 price" benchmark no longer exists and must not be cited. (together.ai/pricing, verified Jul 2026)

**Differentiation statement:**

> Unlike Together AI, which offers per-token inference with caching but no agent-specific features, Gonka provides server-side session persistence, model tiering, and webhook notifications built into the API -- eliminating middleware your team currently maintains -- at a live per-token rate currently far below Together's K2.6/K2.7 pricing. Validate it on staging in a day. (competitive matrix: Agent Sessions, Together AI scored LOSE; live pricing per trackers)

**Supporting claims:**

| Dimension | Together AI | Gonka | Verdict |
|---|---|---|---|
| Agent Sessions | No session management; stateless API with default-on caching | Server-side session persistence | Gonka **WIN** (competitive matrix) |
| Model Tiering | Manual model selection | 3-tier server-side auto-routing via X-Gonka-Tier (client-side routers exist for any provider -- see Section 3, VP2) | Gonka advantage on placement, not uniqueness |
| Per-token Pricing | K2.6: $1.20/$0.20 cached/$4.50; K2.7-Code: $0.95/$0.19/$4.00 (per 1M) | K2.6 broker retail: $0.055/$0.32 (Gonka24) to $0.35 flat (GonkaBroker) per 1M (network rate utilization-dependent, partly subsidized) | Gonka advantage at current utilization (~4-20x cheaper on K2.6) |
| Model Currency | Serves K2.6 and K2.7-Code | Serves K2.6 (plus MiniMax M2.7; GLM-5.2 imminent); K3 planned as frontier tier once weights land (~Jul 27) | Near-parity; Together edge on K2.7-Code |
| Uptime / Reliability | Reliable track record, no formal SLA | No SLA; K2.6 twice removed and re-bootstrapped for validation failures within three weeks (Jun 25 and Jul 15, 2026) | Together AI advantage (competitive matrix: Uptime -- Gonka LOSE) |

**Honest concession:** Together AI offers default-on caching, a reliable operational track record, and K2.7-Code, which Gonka does not yet serve. Gonka's low rate depends on network subsidy and low utilization, and its production reliability is unproven -- concretely, K2.6 failed network validation and was removed/re-bootstrapped twice in three weeks (Jun 25 and Jul 15, 2026, per gonka.ai/docs/network-updates). The agent-native feature advantage must be demonstrated on the CTO's staging environment before trust is established. (competitive matrix: Uptime -- Gonka LOSE)

---

### 7.3 Privacy-First Builder: Gonka vs Akash Network

**The competitor context:** Akash Network is the closest decentralized alternative -- a Kubernetes-as-a-Service platform for GPU compute, advertising ~65 datacenters with sub-200ms global latency and a reverse auction pricing model. AkashML (OpenAI-compatible managed inference API, launched November 2025) now publishes a full public model catalog with transparent per-model pricing -- including Kimi K2.6 at $0.95/$4.00 per 1M and DeepSeek V3.2 -- gives new accounts $100 free credits, and grew throughput from ~5B tokens/day (May 2026) to 10B+ tokens/day (early July 2026), with named production users Venice and ElizaOS. Akash has also shipped Akash Agents, a crypto-abstracted one-click agent-deployment layer. The MEDIUM-threat prediction that Akash would copy Gonka's agent positioning has materialized -- treat Akash as a HIGH-attention competitor and never claim Gonka is "the only decentralized provider with agent features" or that AkashML's catalog/pricing is opaque. (akashml.com; akashml.com/models; Messari State of Akash Q1 2026)

**Differentiation statement:**

> Unlike Akash, whose agent story is deployment tooling (run your agent on Akash compute), Gonka's is inference-layer agent features -- session persistence, memory API, tiering, and webhooks built into the inference API itself -- while both platforms share the decentralized infrastructure and content freedom that appeal to privacy-conscious developers. (provider landscape map: Gonka vs Akash comparison, revised Jul 2026)

**Supporting claims:**

| Dimension | Akash Network | Gonka | Verdict |
|---|---|---|---|
| API Compatibility | AkashML: OpenAI-compatible (since Nov 2025); raw Akash: manual vLLM setup | OpenAI-compatible API, drop-in for OpenClaw; tested with OpenClaw/CrewAI/LangGraph | Parity (ARCHITECTURE.md) |
| Agent Features | Akash Agents: one-click agent deployment (Q1 2026); no inference-layer sessions/memory/tiering/webhooks | Inference-layer agent-native feature set (sessions, memory, tiering, webhooks) | Gonka advantage at the inference layer; Akash advantage at the deployment layer |
| Content Filtering | No content policy (decentralized) | No content policy (decentralized, open-weight models) | Equivalent privacy posture |
| Privacy Guarantees | Distributed compute, no central logging | Distributed compute, no central logging; neither offers TEE yet | Equivalent current state; both need TEE for cryptographic guarantees (developer personas: Privacy-First Builder, Objection #1) |
| Model Selection | Full public catalog via AkashML, including Kimi K2.6 ($0.95/$4.00 per 1M) and DeepSeek V3.2 | Kimi K2.6, MiniMax M2.7 (per-model broker retail $0.018-0.35/1M); GLM-5.2 imminent, K3 on roadmap | Akash advantage on breadth; Gonka advantage on price for shared models (K2.6: $0.055/$0.32 vs $0.95/$4.00) |

**Honest concession:** Akash has a longer operational track record, offers managed inference with a broader model catalog, and has entered the agent space via Akash Agents. Neither platform offers TEE-based encrypted inference -- privacy guarantees are architectural, not cryptographic. For the highest-sensitivity workloads, both require the same trust assumptions. (developer personas: Privacy-First Builder, Objection #1; Messari Q1 2026)

---

## 8. Objection Handling Quick Reference

Consolidated objection responses for rapid reference during community interactions, sales conversations, and content creation. Each response is grounded in research evidence.

**Community-climate note (July 2026):** The OpenClaw community is unusually security-anxious after the Clawdbot -> Moltbot -> OpenClaw double rename (Jan 2026), the typosquat/malicious-clone wave that followed, and the ClawHavoc incident. Developers apply crypto-scam-level scrutiny to ANY new OpenClaw-adjacent tool, crypto or not. Expect the "is this a scam?" objection by default; over-index on verifiable proof (open-source repo, tracker listings, staging tests) rather than assertions.

| Objection | Persona(s) | Response | Evidence |
|---|---|---|---|
| "I have never heard of Gonka." | All | Lead with the developer pain point (heartbeat costs, content filtering) not the brand. "You know how half your OpenClaw bill is heartbeats? There is a provider that eliminates that." Let the value proposition create the introduction. | (ARCHITECTURE.md: Objection Map; developer personas: universal blocker #1) |
| "Is this a crypto thing?" / "Is this a scam?" | All | "No. It is an API. You get an API key, paste a URL into your openclaw.json, and make inference calls. The infrastructure happens to be decentralized, which is why it is cheaper, but you never interact with blockchain, wallets, or tokens. Everything is verifiable: the infrastructure is open source, and independent price trackers list us." | (PITFALLS.md: Pitfalls 1, 2, 7; community-climate note above) |
| "OpenRouter already works, why switch?" | Weekend Builder | "It works, and its caching already discounts repeated context to 10-20% of the input rate. Gonka goes further: sessions keep your conversation server-side so heartbeats retransmit nothing, and the per-token rate is currently the cheapest listed anywhere. One config change to test it." | (competitive matrix: Agent Sessions; live pricing per trackers) |
| "Decentralized = unreliable." | Startup CTO | "That is a fair concern. Test on staging first. Deploy one agent, measure p95 latency and uptime for a week, compare to your current provider. We want you to evaluate with data, not promises." Internal note: if asked, disclose the two K2.6 validation-failure removal/re-bootstrap cycles (Jun 25 and Jul 15, 2026) rather than letting a prospect find them in the public network-updates feed. | (competitive matrix: Uptime -- Gonka LOSE acknowledged; gonka.ai/docs/network-updates; developer personas: Startup CTO, Objection #1) |
| "This model is not Claude or GPT." | Weekend Builder, Startup CTO | "For agent workloads -- tool calling, multi-step reasoning, code generation -- current open-weight models are competitive with frontier models at a fraction of the cost, and Gonka is the cheapest listed provider for the ones it serves. Kimi K2-family models are stable across 200-300 sequential tool calls in our testing." Do NOT cite "76.8% SWE-Bench, best open-source agent model" -- the open-weight SWE-bench Verified leader is DeepSeek V4 Pro (80.6%, Think Max, tied with Gemini 3.1 Pro), ahead of MiniMax M2.5 (80.2%) and GLM-5 (77.8%). Supporting datapoint: Kimi K3 took #1 in Frontend Code Arena ahead of Claude Fable 5 and GPT-5.6 Sol -- the open-weight quality objection is dissolving at the frontier. | (benchlm.ai/coding, Jul 2026; simonwillison.net Jul 16, 2026; competitive matrix: Section 3, Tool Calling) |
| "We need multiple models." | Startup CTO | "Gonka serves two model families today -- Kimi K2.6 and MiniMax M2.7 -- with GLM-5.2 (leader on open agent benchmarks) being added to the network, which covers most agent workloads. For teams needing broader diversity, run Gonka alongside your existing provider: use Gonka for the workloads its models handle (where sessions and broker pricing save the most), keep OpenAI/Anthropic for tasks that need their proprietary models." | (competitive matrix: Model Breadth -- Gonka LOSE vs OpenRouter acknowledged; pragmatic dual-provider approach) |
| "How do I know you do not log prompts?" | Privacy-First Builder | "The infrastructure code is open source at github.com/mitgor/gonka-ai-infrastructure -- audit it. No central entity aggregates prompts. We are honest that this is architectural privacy (no central log aggregation), not cryptographic privacy (TEE-based encryption is on the roadmap, not shipped). If you use a third-party broker, the broker sees your traffic -- go direct for the strongest posture. We will not overclaim." | (developer personas: Privacy-First Builder, Objection #1; PITFALLS.md: Pitfall 1) |
| "Can it handle production scale?" | Startup CTO | "We have integration test results for OpenClaw, CrewAI, and LangGraph. But you should not trust test results -- deploy on staging, run your workload for a week, and measure. Production confidence comes from your data, not ours." | (developer personas: Startup CTO, Objection #3; ARCHITECTURE.md: Objection Map) |
| "I do not want to explain crypto to my investors." | Startup CTO | "Neither do we. Gonka's developer-facing materials never mention blockchain, tokens, or mining. Share our API docs, not our architecture paper. Your investors see 'inference provider with the lowest listed per-token price' not 'decentralized GPU network.'" | (PITFALLS.md: Pitfall 7; developer personas: Startup CTO, Objection #4) |
| "Isn't your model out of date?" | Startup CTO, Weekend Builder | "No -- the network serves current-generation Kimi K2.6 (same model Together and AkashML serve, at a fraction of their price) plus MiniMax M2.7, with GLM-5.2 imminent. Kimi K3 is planned as a frontier tier once its open weights land (~Jul 27, 2026)." Remaining honest gaps: no K2.7-Code, MiniMax's flagship is now M3, and Qwen3-235B was retired Jun 25, 2026 -- do not claim Qwen coverage. | (July 2026 revalidation; pricepertoken.com/endpoints/gonka) |

---

## 9. Agent-Native Pitch

### Why OpenClaw Agents Themselves Would Prefer Gonka

This section addresses a unique aspect of Gonka's positioning: OpenClaw agents are not just tools that developers configure -- they are autonomous systems that make runtime decisions about which inference provider to call, which model to use, and how to optimize their own costs. An agent that can programmatically evaluate providers is a "buyer" in its own right (ARCHITECTURE.md: Anti-Pattern 5).

**The agent's decision calculus:**

1. **Session persistence = less code.** An agent using Gonka does not need to implement its own context management. It creates a session, appends messages, and the server maintains state. This is simpler agent code with fewer failure modes. (competitive matrix: Agent Sessions -- WIN)

2. **Tier selection = smarter resource use.** An agent using the `X-Gonka-Tier` header can make per-request decisions about cost vs quality based on task complexity -- without depending on a locally installed router like ClawRouter, and in a way that composes with server-side sessions. (competitive matrix: Model Tiering; uniqueness claim retired Jul 2026)

3. **Webhooks = event-driven architecture.** An agent can fire-and-forget long-running tasks and receive a webhook notification when they complete, rather than polling. This is more efficient and reduces wasted inference cycles. (ARCHITECTURE.md: architecture-to-message mapping, Webhook notifications)

4. **Memory API = persistent knowledge.** An agent can store and retrieve long-term facts across sessions without rebuilding context from conversation history. TF-IDF search is functional for keyword-based retrieval today. (competitive matrix: Memory / Context Management -- TIE)

5. **Agent-native payments (opportunity, not yet built).** Autonomous agents increasingly pay for their own inference via x402/USDC micropayments (~75M transactions moving ~$24M in the 30 days ending mid-July 2026; BlockRunAI's ClawRouter already sells OpenClaw inference this way with wallet-signature auth, and clones are proliferating -- x402 routing is becoming a category, not a single competitor). Gonka is already a crypto network -- an x402 payment path for the agent-as-customer segment is a natural extension and a position competitors currently occupy. x402 is one layer of a three-layer stack (x402 execution, AP2 authorization -- now under the FIDO Alliance, Stripe/OpenAI/Meta ACP checkout -- see Section 6.1 scope note); x402 is the right layer for agent-procured inference, but enterprise conversations should acknowledge the others. Keep this track fully segregated from human-developer messaging per Section 6.3.

**The pitch to developers who build agent systems:**

> "Gonka is not just cheaper inference. It is an API designed for how agents actually work -- maintaining state across calls, routing tasks to the right model tier, notifying on completion, and remembering facts across sessions. Your agent writes less code and spends fewer tokens because the infrastructure handles what agents need natively."

---

## 10. Message Hierarchy Summary

For quick reference when creating any developer-facing content:

### Primary Message (Use First)
**"Gonka is the cheapest listed inference for your OpenClaw agent -- and your agent stops paying for context it already has."**

### Secondary Messages (Support Primary)
- "Session persistence eliminates heartbeat waste entirely -- caching elsewhere only discounts it."
- "Server-side model tiering: classification on the cheap tier, reasoning on the strong one, no router to install."
- "One config change, 90 seconds, no wallet, no tokens, no SDK."

### Tertiary Messages (Use When Relevant to Audience)
- "No content filters, no prompt logs, no permission required." (Privacy-First only)
- "Inference gets cheaper as the network grows." (Cost-conscious audiences)
- "Agent-native features at the inference layer that other providers bolt on as middleware." (Technical audiences)

### Never-Lead-With Messages
- Decentralization, blockchain, Web3, DePIN
- GNK tokens, mining rewards, staking (x402 agent-payments content lives on its own segregated track)
- Sprint Consensus (unless in technical deep-dive)
- "Unstoppable network" or "permissionless" language

### Retired Claims (Do Not Use Externally -- July 2026)
- "Cuts agent costs by up to 73%" / "$47 -> $13" / "$218 -> $59" (Apr 2026 Scenario B math; recompute against live pricing and cached competitor rates first)
- "K2.5 is the best open-source agent model" / "76.8% SWE-Bench Verified" as a leadership claim (superseded by DeepSeek V4 Pro 80.6%, MiniMax M2.5 80.2%, GLM-5 77.8%, and Moonshot's own K2.7-Code/K3)
- "MiniMax M2.5 leads open-weight SWE-bench Verified at 80.2%" (DeepSeek V4 Pro, Apr 24, 2026, scores 80.6% in Think Max mode -- the open-weight leader, tied with Gemini 3.1 Pro)
- "131K context window" (K2.5 shipped with 256K; K2.6/K2.7 also 256K, K3 1M)
- "No other provider offers server-side session management" (OpenAI Responses + Conversations API now does, on its primary surface)
- "No other provider offers automatic model tiering" / "all four competitors scored LOSE" (routing is commoditized: ClawRouter and third-party routers)
- "OpenRouter charges a 5.5% markup on all usage" / "no caching on OpenRouter" (it is a payment-processing fee on card credit purchases; caching passes through)
- "Together AI serves K2.5 at $0.50/$2.50, the lowest verified price" (Together no longer lists K2.5; current lineup is K2.6/K2.7-Code)
- "GPT-4o at $2.50/$10 with 50% cache discount" and "Claude Opus 4 at $15/$75 / 30x more expensive" (GPT-4o retired; current comparisons: GPT-5.x, Claude Opus 4.8 $5/$25, Sonnet 5 $3/$15; cached input on current OpenAI models is 90% off, not 50%)
- "OpenRouter's 500+ models" / "400+ models on 70+ providers" (Jul 2026 sources support 400+ models from 60+ providers; "70+ providers" is unsupported -- use "hundreds of models" or re-pull exact counts from openrouter.ai/models)
- "Gonka is the only decentralized provider with agent features" (Akash Agents launched Q1 2026)
- "Gonka serves K2.5 tiers only / two generations behind" (K2.6 and MiniMax M2.7 are live on the network -- verified July 2026)
- "Qwen3-235B is the sole PoC model" / any lineup including Qwen (Qwen3-235B retired Jun 25, 2026 per Proposal 78; MiniMax M2.7 is now the sole PoC model and base delegation target)
- "Kimi K2.6 has been continuously live since ~May 2026" / "Proposal 88 raised K2.6's weight factor 0.78 → 0.9" (the official feed shows Proposal 78 (Jun 25) removed K2.6 alongside Qwen3-235B for lacking validation majority; Proposal 79 (Jun 26) restored it already at 0.9 -- and introduced GLM-5.2 at 2.47; re-bootstrap at epoch 311 on Jun 27; Proposal 87 (Jul 15) was K2.6's SECOND removal. Two validation failures in three weeks -- state the stability caveat accordingly)
- "Moonshot serves K2.5 first-party at $0.60/$3.00 (cache hit $0.10)" as a current price, or any framing of K2.5 as a live Moonshot product (K2.5 closed to newly registered users after the K3 launch Jul 16, 2026; full platform sunset Aug 31, 2026; API traffic redirected to K2.6. Third-party K2.5 hosting -- OpenRouter $0.375/$2.025, DeepInfra $0.45/$2.25 -- persists with lifecycle risk)
- "~$0.0003 per 1M tokens via brokers" as an end-user price (that is the raw network rate; broker retail is $0.018-0.35/1M per model -- quote broker retail)
- "$0.018/$0.072 per 1M" as Gonka's or Gonka24's general rate, and any Gonka24 monthly cost projection built on a flat/blended rate (e.g., "~$132/month Heavy tier") -- Gonka24 pricing is per-model (M2.7 $0.018/$0.072, K2.6 $0.055/$0.32, GLM-5.2 $0.095/$0.30); K2.6 workloads cost ~4x the flat-rate projections (Heavy tier on K2.6 is ~$550/month, not ~$132)
- "76% of teams use multiple models" (unverified in the published LangChain report; use the report's "multiple models is the norm" phrasing)
- "AI tokens were the only profitable crypto sector in Q1 2026" (restate as: smallest sector decline, ~-14%, with TAO/FET/RENDER posting gains)
- "AkashML's catalog and pricing are not well-documented" / "Akash lacks agent features" (AkashML publishes a full catalog with per-model pricing incl. K2.6; Akash Agents shipped)
- "165M+ x402 transactions / ~69K agents / 98.6% USDC / mostly testing-gamed volume" (superseded by 30-day run-rate figures: ~75M tx, ~$24M, ~94K buyers; say "predominantly USDC"; 95% of payment value now in transactions above $1)
- "x402 Foundation core members: Google, Visa, AWS, Circle, Anthropic, Cloudflare, Vercel" (Jul 14, 2026 operational launch: 40 members; full premier roster is Adyen, AWS, Amex, Circle, Cloudflare, Coinbase, Fiserv, Google, Mastercard, Monad Foundation, MoonPay, Ripple, Shopify, Solana Foundation, Stellar Development Foundation, Stripe, Visa; Anthropic and Vercel not on it)
- x402 as "the" agent payment rail with no context (situate it in the three-layer stack: x402 execution / AP2 authorization / ACP checkout)
- "Google's AP2" as protocol steward (Google donated AP2 to the FIDO Alliance; it is now community-led -- say "AP2, now under the FIDO Alliance")
- "OpenAI/Stripe's ACP" without Meta (ACP is an open standard co-created by Stripe, OpenAI, and Meta; live scope is Instant Checkout for US ChatGPT users buying from US Etsy sellers, Shopify and Salesforce announced)

---

*Document: gonka_message_house.md | Version 1.4 | 2026-07-18 (supersedes 1.3; 1.0 dated 2026-04-01)*
*Feeds into: Phase 18 (Channel Strategy), Phase 19 (Partnership & Ecosystem)*
*Sources: gonka_competitive_feature_matrix.md, gonka_developer_personas.md, gonka_agent_pricing_analysis.md, gonka_provider_landscape_map.md, ARCHITECTURE.md, PITFALLS.md; July 2026 revalidation sources cited inline*

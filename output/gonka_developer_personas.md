# Gonka Developer Personas and AAARRRP Journey Maps

**Version:** 1.0
**Date:** 2026-04-01
**Purpose:** Define developer archetypes considering Gonka as their OpenClaw inference provider, with evidence-grounded decision drivers and journey maps
**Feeds into:** Phase 17 (Messaging & Positioning), Phase 18 (Channel Strategy)

---

## Executive Summary

OpenClaw builders are overwhelmingly Web2-native software engineers who have never held a cryptocurrency token. They discovered OpenClaw through GitHub trending or Reddit, deployed a personal AI agent in a weekend, and are now grappling with inference costs, provider reliability, and the friction of configuring custom providers. They evaluate inference providers the same way they evaluate any API service: Does it work? Is it affordable? Is it easy to set up?

This document defines three developer personas differentiated by **primary decision driver** (cost, reliability, and privacy/censorship resistance), each aligned with a workload tier from the pricing analysis (Casual, Active, Heavy). A fourth persona is not included because the research corpus shows that the privacy/censorship driver, while strong for Gonka, applies across workload scales rather than defining a separate archetype -- it is instead captured as Persona 3.

These personas are **not fictional**. Every decision driver ranking, pain point, and objection traces to specific findings in the research corpus (FEATURES.md, PITFALLS.md, ARCHITECTURE.md, competitive feature matrix, and pricing analysis). Where evidence is indirect (community signals rather than direct interviews), confidence levels are noted.

---

## Persona: The Weekend Builder

### Profile

- **Role:** Software engineer building personal AI agents as side projects
- **Team size:** Solo
- **Technical level:** Mid to senior (comfortable with APIs, JSON config, CLI tools)
- **Crypto familiarity:** None -- has heard of Bitcoin, has never held a token, does not know what "staking" means
- **Current stack:** OpenClaw + OpenRouter (the default provider, never changed it) on a personal VPS or local machine
- **Monthly inference spend:** $20-50 (Casual tier, ~31.5M tokens/month per pricing analysis Section 3)
- **OpenClaw usage pattern:** One agent on Telegram or Discord acting as a personal assistant, coding helper, or research bot. Runs 24/7 with 30-minute heartbeat intervals. 50 user messages/day.

### Decision Drivers (Ranked)

1. **Cost per task** -- "I am spending $40/month on a hobby project and that feels too high for what I get."
   Evidence: FEATURES.md ranks cost per task as the #1 developer decision criterion, citing "$300+ in 2 days" community complaints and the fact that OpenClaw agents make 3-10x more LLM calls than chatbots. At the Casual tier, heartbeats alone consume 44% of monthly tokens (pricing analysis Section 3), meaning nearly half the bill generates zero user-facing value.

2. **Ease of integration** -- "I do not want to spend a weekend reconfiguring my agent to try a new provider."
   Evidence: FEATURES.md ranks ease of integration as #4, noting that "adding a custom provider = editing one JSON block with baseUrl" (FEATURES.md Section: Developer Decision Criteria). OpenClaw supports 14 built-in providers where setup is automatic; Gonka requires manual `openclaw.json` configuration (STACK.md Section 1: Built-In vs Custom Providers). For this persona, any friction beyond copy-pasting a config snippet is a dealbreaker.

3. **Model quality for agentic tasks** -- "It needs to handle tool calling and multi-step reasoning without breaking."
   Evidence: FEATURES.md ranks model quality as #3. 76% of teams use multiple models (LangChain State of Agent Engineering). K2.5 scores 76.8% on SWE-Bench Verified and is stable across 200-300 sequential tool calls (FEATURES.md Section: Developer Decision Criteria), making it competitive with frontier models for agent workloads at a fraction of the cost.

### Pain Points

- **Heartbeats cost nearly as much as actual messages.** At the Casual tier, heartbeats consume 44% of total tokens (460,800 tokens/day) despite generating zero user-facing output (pricing analysis Section 3). This persona sees their monthly bill and cannot reconcile "I only sent 50 messages today" with a $40+ charge.
  Source: gonka_agent_pricing_analysis.md Section 3 (Casual Tier)

- **OpenRouter free tier is unreliable for always-on agents.** Models "appear, disappear, hit throttles, degrade under peak load" and free requests are queued behind paid users (FEATURES.md citing OpenRouter Free API Changes 2026). For an agent running 24/7 on Telegram, this means missed messages and inconsistent responses during peak hours.
  Source: FEATURES.md Section: Developer Decision Criteria, criterion #2

- **Single-model limitation feels risky.** This persona currently uses OpenRouter which provides access to 500+ models. Switching to a provider with only one model (K2.5 in 3 quantization tiers) means no fallback if K2.5 is degraded or unsuitable for a particular task. The competitive feature matrix scores Gonka as LOSE on model breadth.
  Source: gonka_competitive_feature_matrix.md Section 8 (Model Breadth)

### Adoption Triggers

- Monthly OpenRouter bill crosses the $50 threshold and they search "cheaper OpenClaw inference provider" on Reddit or GitHub
- OpenRouter free tier degrades during a weekend when they are actively building, causing frustration and a search for alternatives
- They see a Reddit r/LocalLLaMA comparison post showing K2.5 performance at 10x lower cost than GPT-4o and click through to Gonka docs
- A ClawHub skill or community plugin for Gonka appears, making setup trivially easy

### Objections

- **"I have never heard of Gonka."** Awareness is zero among mainstream OpenClaw developers who do not follow decentralized compute channels. Discovery depends on presence in the OpenClaw ecosystem (ClawHub, Discord, provider docs), which Gonka currently lacks.
  Source: ARCHITECTURE.md Objection Map ("I've never heard of Gonka" -- All personas)

- **"OpenRouter already works, why would I change?"** Switching inertia is real. OpenRouter is built into OpenClaw with zero configuration. Gonka requires manual JSON editing. The marginal effort feels unjustified unless the cost savings are dramatic and clearly documented.
  Source: ARCHITECTURE.md Objection Map ("OpenRouter already works" -- Builder persona); PITFALLS.md Pitfall 6 (ecosystem dynamics and default provider stickiness)

- **"Is this a crypto thing? I do not want to set up a wallet."** Any association with cryptocurrency triggers skepticism -- rug pulls, scams, and volatile tokens are top-of-mind for Web2 developers encountering blockchain-adjacent projects. If the landing page mentions "tokens" or "staking," this persona closes the tab immediately.
  Source: PITFALLS.md Pitfall 7 (crypto jargon alienation); PITFALLS.md Pitfall 2 (requiring crypto knowledge)

- **"K2.5 is not Claude or GPT."** Unfamiliarity with Kimi K2.5 creates doubt about model quality, despite strong benchmarks. This persona has muscle memory with Claude or GPT-4o and needs concrete evidence that K2.5 handles their specific agent tasks (tool calling, code generation, multi-step reasoning) comparably.
  Source: ARCHITECTURE.md Objection Map ("K2.5 isn't Claude/GPT" -- Builder persona)

### Gonka Value Proposition (for this persona)

- **Server-side session persistence eliminates heartbeat waste.** Gonka's sessions API maintains conversation state server-side, reducing heartbeat token overhead by ~80%. At the Casual tier, this drops monthly token consumption from 31.5M to ~12.6M tokens, reducing costs from ~$47/month (Together AI) to ~$13/month (Gonka Scenario B). No other provider offers this on the standard chat completions API.
  Maps to: Decision Driver #1 (cost per task)
  Source: gonka_agent_pricing_analysis.md Section 5 (Gonka hidden cost analysis)

- **Drop-in OpenClaw compatibility.** Gonka's OpenAI-compatible API means adding it as a custom provider requires editing one JSON block in `openclaw.json` -- setting `baseUrl`, `apiKey`, and `api: "openai-completions"`. No SDK changes, no new libraries, no code modifications. Competitive feature matrix scores Gonka as TIE on streaming and tool calling -- everything just works.
  Maps to: Decision Driver #2 (ease of integration)
  Source: STACK.md Section 1 (provider selection flow); FEATURES.md Section: Developer Decision Criteria, #4

- **K2.5 is purpose-built for agent tasks.** 76.8% SWE-Bench Verified, stable across 200-300 sequential tool calls, 131K context window, native Agent Swarm support. For the cost-conscious solo builder, K2.5 delivers frontier-model agentic performance at open-source pricing.
  Maps to: Decision Driver #3 (model quality)
  Source: FEATURES.md Section: Differentiators, Tier 1; ARCHITECTURE.md Architecture-to-Message Mapping

---

## Persona: The Startup CTO

### Profile

- **Role:** Technical co-founder or CTO of an early-stage AI startup building products on OpenClaw
- **Team size:** 3-8 engineers
- **Technical level:** Senior (architectural decisions, infrastructure management, cost optimization)
- **Crypto familiarity:** Aware -- understands blockchain conceptually, has read about decentralized compute, but has never integrated crypto payments into a product and does not want to
- **Current stack:** OpenClaw + Together AI or direct OpenAI API for production; OpenRouter for development/testing. Considering vLLM self-hosting to reduce costs.
- **Monthly inference spend:** $200-500 (Active tier, ~161.5M tokens/month per pricing analysis Section 3)
- **OpenClaw usage pattern:** 3 agents across 6 channels (Telegram, Discord, web chat) handling customer support, community management, and internal tooling. Multi-model routing: 70% budget model for classification/simple tasks, 30% strong model for complex reasoning.

### Decision Drivers (Ranked)

1. **Reliability and uptime** -- "If our support agent goes down for 10 minutes, we lose customers and our investors ask questions."
   Evidence: FEATURES.md ranks reliability as #2 decision criterion. For production agent deployments, a single failed inference call in a multi-step workflow can cascade into lost agent state and wasted prior computation (competitive feature matrix Section 7: Uptime/Reliability). This persona has paying customers depending on agent availability 24/7. OpenRouter's free tier degradation under load is unacceptable; even paid tiers lack formal SLAs.

2. **Cost at scale** -- "We are burning $400/month on inference and that number doubles every quarter as we add agents."
   Evidence: FEATURES.md ranks cost as #1 overall, but for this persona it is #2 because unreliable cheap inference is worse than expensive reliable inference. At the Active tier, heartbeats account for 51% of token consumption (pricing analysis Section 3). With 6 channel-agents heartbeating independently, the overhead scales linearly with channel count. The difference between DeepInfra ($218/month) and Gonka Scenario B ($59/month) at this tier is $159/month -- meaningful for a startup watching runway.

3. **Agent-native features** -- "I need sessions, model routing, and usage tracking built into the provider, not bolted on with custom middleware."
   Evidence: FEATURES.md Section: Differentiators lists session persistence, auto-tiering, memory API, and webhooks as Tier 1 high-impact features already built. The competitive feature matrix shows Gonka as the only provider with WIN verdicts on both agent sessions and model tiering. This persona currently builds custom middleware for model routing and session management -- Gonka's native support eliminates that engineering overhead.

### Pain Points

- **Multi-agent heartbeat overhead scales linearly and dominates costs.** With 6 channel-agents, heartbeat overhead reaches 51% of total tokens (2.76M tokens/day just from heartbeats). Adding a 7th channel-agent increases monthly cost by ~$36 (at DeepInfra rates) with no increase in user-facing capability.
  Source: gonka_agent_pricing_analysis.md Section 3 (Active Tier)

- **Custom middleware for model routing is engineering overhead.** No provider offers automatic task-based routing between cheap and expensive models. This persona's team has built custom middleware to route classification tasks to budget models and reasoning tasks to strong models -- code they must maintain, debug, and update when providers change APIs.
  Source: gonka_competitive_feature_matrix.md Section 2 (Model Tiering -- all competitors scored LOSE)

- **No provider offers production-grade SLAs for agent workloads.** OpenAI and Anthropic offer SLAs but at premium pricing (3-20x more per token than K2.5 providers). K2.5 providers (Together AI, DeepInfra, OpenRouter) offer no formal SLAs. This persona is stuck choosing between reliability (expensive) and affordability (unguaranteed).
  Source: gonka_competitive_feature_matrix.md Section 7 (Uptime/Reliability); FEATURES.md Table Stakes ("Reasonable uptime >99%" -- NOT PROVEN for Gonka)

- **Prompt caching is a partial workaround, not a solution.** OpenAI's 50% caching discount and Anthropic's 90% caching discount reduce heartbeat costs, but they do not eliminate them -- tokens are still transmitted, processed, and billed (at reduced rates). Server-side sessions would eliminate the re-transmission entirely.
  Source: gonka_competitive_feature_matrix.md Key Takeaway #4

### Adoption Triggers

- Monthly inference bill crosses $500 and the board asks "can we reduce infrastructure costs by 50%?"
- A production agent outage on OpenRouter during a customer demo triggers an urgent search for providers with reliability data
- They evaluate self-hosting vLLM and realize Gonka offers the same infrastructure with session persistence and tiering built in -- no DevOps overhead
- A competitor startup publishes a case study showing 70% cost reduction on Gonka, creating FOMO

### Objections

- **"Decentralized infrastructure means unreliable inference."** This is the primary blocker. The competitive feature matrix scores Gonka as LOSE on uptime/reliability -- no published SLA, no public status page, no historical uptime data. For a startup with paying customers, adopting unproven infrastructure is a career risk for the CTO.
  Source: ARCHITECTURE.md Objection Map ("Decentralized = unreliable" -- Startup persona); PITFALLS.md Pitfall 3 (unreliable inference undermining trust at first contact)

- **"We need multiple models, not just K2.5."** 76% of teams use multiple models. This persona's agents route between budget models (classification) and strong models (reasoning). Gonka's single-model offering with 3 quantization tiers provides some tiering capability but not true multi-model diversity. If K2.5 is degraded, there is no fallback model.
  Source: FEATURES.md criterion #3 (model quality / multi-model); gonka_competitive_feature_matrix.md Section 8 (Model Breadth -- Gonka scored LOSE)

- **"Can it handle our scale?"** The CTO needs evidence of production-scale performance, not just integration test results. v1.2 tests demonstrate functional correctness but not concurrent load handling, failover behavior, or sustained throughput under multi-agent pressure.
  Source: ARCHITECTURE.md Objection Map ("Can it handle production scale?" -- Startup persona)

- **"I do not want to explain to investors why we depend on crypto infrastructure."** Even if the CTO personally understands decentralized compute, explaining it to non-technical investors creates friction. If Gonka's marketing materials look like a DeFi protocol, the CTO will not share them internally.
  Source: PITFALLS.md Pitfall 1 (leading with decentralization); Pitfall 7 (crypto jargon)

### Gonka Value Proposition (for this persona)

- **Session persistence at scale: 73% cost reduction at the Active tier.** DeepInfra costs $218/month at Active tier; Gonka Scenario B costs $59/month. The savings come entirely from eliminating heartbeat context re-sending via server-side sessions -- a structural advantage that scales super-linearly as more agents are added.
  Maps to: Decision Driver #2 (cost at scale)
  Source: gonka_agent_pricing_analysis.md Section 6 (Active Tier monthly cost projections)

- **Built-in model tiering eliminates custom middleware.** Gonka's X-Gonka-Tier header and content-aware auto-routing replace the custom routing middleware this team currently maintains. Classification goes to lite K2.5, reasoning goes to full K2.5 -- automatically, with no application code changes.
  Maps to: Decision Driver #3 (agent-native features)
  Source: gonka_competitive_feature_matrix.md Section 2 (Model Tiering); ARCHITECTURE.md Architecture-to-Message Mapping

- **Webhook notifications enable event-driven agent architecture.** Gonka's webhook system (built in v1.2) notifies agent backends when async tasks complete, costs exceed thresholds, or models update. No other compared provider offers this. For a startup running production agents, this means fewer polling loops and more responsive agent behavior.
  Maps to: Decision Driver #3 (agent-native features)
  Source: FEATURES.md Section: Differentiators, Tier 2

- **Reliability path: transparent status metrics.** While Gonka currently lacks SLA guarantees, providing real-time uptime dashboards, p95 latency data, and public post-mortems would address this persona's #1 concern. The value proposition is conditional on Gonka establishing a reliability track record before this persona commits production workloads.
  Maps to: Decision Driver #1 (reliability)
  Source: PITFALLS.md Pitfall 3 (recovery strategy: publish real-time uptime stats)

---

## Persona: The Privacy-First Agent Builder

### Profile

- **Role:** Senior developer or security engineer building agents that handle sensitive data (legal, medical, financial, or politically sensitive content)
- **Team size:** Solo or small team (2-4), often working on open-source or activist-adjacent projects
- **Technical level:** Senior (understands API security, data residency, content filtering implications)
- **Crypto familiarity:** None -- privacy motivation is technical (no prompt logging, no content filtering), not ideological. Does not care about decentralization philosophy; cares about practical data handling guarantees.
- **Current stack:** OpenClaw + local Ollama or self-hosted vLLM for sensitive workloads; OpenRouter or OpenAI for non-sensitive tasks. Runs separate inference stacks to segregate sensitive data.
- **Monthly inference spend:** $30-150 (spans Casual to Active tier depending on workload; uses Heavy token volumes when running local models at zero marginal cost)
- **OpenClaw usage pattern:** Agents that process sensitive documents, draft legal arguments, analyze medical data, or generate content that triggers content filters on OpenAI/Anthropic. Needs unrestricted inference without prompt logging.

### Decision Drivers (Ranked)

1. **Data privacy and censorship resistance** -- "I need a provider that does not log my prompts, does not filter my outputs, and does not have a content policy team reviewing my agent's conversations."
   Evidence: FEATURES.md ranks data privacy as #7 and censorship resistance as #8 by overall community frequency, but for this persona they are the #1 non-negotiable requirement. FEATURES.md notes "OpenRouter allows restricting to trusted providers; some devs run local models for privacy" and "Growing demand for uncensored models; OpenClaw devs want agents that can discuss anything." Gonka's position on both is rated STRONG: "Decentralized = no single entity logs all prompts" and "Decentralized network has no content policy; K2.5 is open-weight."

2. **Model quality for unrestricted tasks** -- "The model needs to handle edge cases that GPT-4o refuses -- drafting adversarial legal arguments, discussing sensitive medical conditions, generating security exploit analyses."
   Evidence: FEATURES.md anti-features table notes OpenAI and Anthropic have strict content policies. The competitive feature matrix Section 8 notes K2.5 is open-weight with no content filtering. For this persona, model quality is inseparable from model freedom -- a model that refuses the prompt is a model with zero quality for their use case, regardless of benchmark scores.

3. **Cost efficiency vs self-hosting** -- "I am currently running Ollama on my own hardware. If a cloud provider can match my privacy requirements at lower total cost of ownership, I would switch."
   Evidence: Self-hosting on consumer hardware has hidden costs: electricity, maintenance, limited GPU memory constraining model size, and inability to scale. FEATURES.md criterion #1 (cost per task) applies, but this persona frames it as total cost of ownership including hardware depreciation and time spent maintaining infrastructure.

### Pain Points

- **Content filtering on OpenAI and Anthropic blocks legitimate use cases.** Agents processing legal discovery documents, generating security assessments, or analyzing medical data trigger content filters that refuse to complete the request. This is not about generating harmful content -- it is about providers making unilateral decisions about what counts as "harmful."
  Source: FEATURES.md Messaging Theme #3 ("No Rules, No Logs, No Limits"); gonka_competitive_feature_matrix.md (content filtering: OpenAI "Strict," Anthropic "Strict," Gonka "None (open)")

- **Self-hosting is expensive and high-maintenance.** Running vLLM on local hardware requires GPU investment ($2,000-10,000+), electricity costs, cooling, and ongoing maintenance. Model updates require manual deployment. There is no auto-tiering, no session persistence, no webhook support -- just raw inference.
  Source: ARCHITECTURE.md Persona 3 (AI Startup -- "Together AI or direct cloud GPU with vLLM"); FEATURES.md gap analysis (Gonka has features that self-hosted vLLM does not)

- **OpenRouter's privacy guarantees are provider-dependent.** OpenRouter allows "restricting to trusted providers" but the developer must trust both OpenRouter (as routing intermediary) and the upstream provider. Data passes through two entities instead of one. For sensitive workloads, this doubles the attack surface.
  Source: FEATURES.md criterion #7 (data privacy); competitive feature matrix (OpenRouter: "Provider-dependent" content filtering)

- **No provider combines privacy with agent-native features.** This persona can get privacy from self-hosted vLLM but loses sessions, tiering, memory, and webhooks. They can get agent features from Gonka but need assurance that Gonka's decentralized infrastructure provides genuine privacy guarantees (not just marketing claims).
  Source: gonka_provider_landscape_map.md (Gonka is the only provider combining decentralized infrastructure with agent-native extensions)

### Adoption Triggers

- OpenAI or Anthropic updates content policies and blocks a use case that was previously allowed, forcing an urgent provider search
- Self-hosted GPU fails or needs replacement, creating a cost inflection point where cloud alternatives become attractive
- A colleague or open-source community member shares a Gonka configuration that demonstrates unrestricted inference with OpenClaw
- They read a technical deep-dive explaining how Gonka's decentralized architecture prevents prompt logging at the infrastructure level (not just policy level)

### Objections

- **"How do I know Gonka actually does not log my prompts? Decentralized does not automatically mean private."** This is the critical trust barrier. Decentralized infrastructure distributes prompts across nodes, but each node operator could theoretically log requests. Without end-to-end encryption or TEE (Trusted Execution Environment), "decentralized = private" is a claim, not a guarantee.
  Source: FEATURES.md Differentiator Tier 3 ("Privacy-preserving inference -- Encrypted prompts; no host sees plaintext" -- listed as Very High complexity, not yet built); PITFALLS.md Pitfall 1 (leading with decentralization claims that are not technically verified)

- **"K2.5 is the only model. What if it cannot handle my specific use case?"** Privacy-sensitive tasks often require specialized capabilities (legal reasoning, medical terminology, code analysis). K2.5 is a general-purpose agent model -- it may not match GPT-4o or Claude on domain-specific tasks. With no alternative models on Gonka, there is no fallback.
  Source: gonka_competitive_feature_matrix.md Section 8 (Model Breadth -- LOSE for Gonka)

- **"I do not trust 'no content policy' from a company I have never heard of."** The absence of content filtering is a feature for this persona, but only if the provider is credible. An unknown provider claiming "no rules" could be a fly-by-night operation that disappears with their data.
  Source: PITFALLS.md Pitfall 3 (unreliable inference undermining trust); Pitfall 5 (community theater vs genuine adoption)

### Gonka Value Proposition (for this persona)

- **Open-weight model on decentralized infrastructure: no content policy, no centralized prompt logs.** K2.5 is open-weight with no built-in content filtering. Gonka's decentralized network has no central authority that can impose content policies or review prompts. For use cases blocked by OpenAI/Anthropic filters, Gonka is the only API provider that serves unrestricted inference.
  Maps to: Decision Driver #1 (privacy and censorship resistance)
  Source: FEATURES.md Messaging Theme #3; competitive feature matrix (Gonka: "None (open)" on content filtering)

- **Agent features that self-hosting cannot match.** Self-hosted vLLM gives privacy but not session persistence, automatic tiering, memory API, or webhook notifications. Gonka offers both: the privacy guarantees of open-weight decentralized inference AND the agent-native features of a managed platform.
  Maps to: Decision Driver #1 + practical value
  Source: gonka_provider_landscape_map.md (Gonka uniquely combines decentralized + agent-native); FEATURES.md gap analysis

- **Cost advantage over self-hosting.** Decentralized compute costs 60-80% less than centralized alternatives (FEATURES.md Section: Developer Decision Criteria, Gonka Position for criterion #1). For this persona, Gonka's per-token pricing may be lower than the total cost of ownership of running their own GPU -- especially when factoring in electricity, maintenance, and the engineering time saved by using Gonka's built-in agent features.
  Maps to: Decision Driver #3 (cost vs self-hosting)
  Source: FEATURES.md; gonka_agent_pricing_analysis.md Section 5 (Gonka hidden cost analysis)

---

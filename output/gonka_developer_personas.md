# Gonka Developer Personas and AAARRRP Journey Maps

**Version:** 1.3
**Date:** 2026-07-18 (refreshed against July 2026 market data; dollar figures marked as April 2026 model estimates where not re-verified)
**Purpose:** Define developer archetypes considering Gonka as their OpenClaw inference provider, with evidence-grounded decision drivers and journey maps
**Feeds into:** Phase 17 (Messaging & Positioning), Phase 18 (Channel Strategy)

---

## Executive Summary

OpenClaw builders are overwhelmingly Web2-native software engineers who have never held a cryptocurrency token. They discovered OpenClaw through GitHub trending or Reddit (the repo hit 247K stars and 47.7K forks by March 2, 2026 -- the fastest-growing repository in GitHub history -- and has spawned a fork ecosystem including security-hardened sandboxed forks, Chinese DeepSeek/WeChat adaptations, and commercial services from Tencent and Z.ai), deployed a personal AI agent in a weekend, and are now grappling with inference costs, provider reliability, and the friction of configuring custom providers. They evaluate inference providers the same way they evaluate any API service: Does it work? Is it affordable? Is it easy to set up?

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
   Evidence: FEATURES.md ranks ease of integration as #4, noting that "adding a custom provider = editing one JSON block with baseUrl" (FEATURES.md Section: Developer Decision Criteria). OpenClaw ships built-in providers where setup is automatic (18+ as of v2026.7.1, the current stable release as of July 18, 2026; v2026.7.2 -- which adds remote coding sessions, cloud workers, and guided Control UI setup -- exists only as pre-release betas, so anchor counts on v2026.7.1 until 7.2 GA lands), with onboarding defaulting to openrouter/auto; Gonka requires manual `openclaw.json` configuration (STACK.md Section 1: Built-In vs Custom Providers). Note: OpenClaw is now stewarded by the OpenClaw Foundation (formally launched July 8, 2026 as a 501(c)(3) with published leadership and 30+ donor/partner orgs); OpenAI is one of five published major donors (alongside Offline Holdings, University of Michigan, Microsoft, and NVIDIA) and employs the project's creator, who leads the "Claw Labs" team inside OpenAI -- so the "built-in provider PR" path still runs through a conflicted gatekeeper, a neutrality concern analysts have raised against the foundation's "Switzerland of AI" positioning. The Foundation now has a first full-time team of ten, is chaired by Dave Morin, counts Red Hat as a contributing partner on enterprise open source and supply-chain security, and is convening standards councils on agent identity, agent profiles, evals, and enterprise deployment -- a vendor-neutral engagement venue for Gonka that does not run through the conflicted built-in-provider PR path (see partnership playbook). For this persona, any friction beyond copy-pasting a config snippet is a dealbreaker.

3. **Model quality for agentic tasks** -- "It needs to handle tool calling and multi-step reasoning without breaking."
   Evidence: FEATURES.md ranks model quality as #3. Most production agent teams use multiple models -- tiered multi-model routing is standard enterprise practice in 2026. (Earlier drafts cited a ~45% LangChain/LangGraph vs ~20% CrewAI production-share split; that split could not be attributed to a named survey and is retired. Verifiable July 2026 datapoints: LangGraph overtook CrewAI in GitHub stars in early 2026, leads monthly search volume ~27.1K vs ~14.8K, and has crossed ~38M monthly PyPI downloads; CrewAI is at ~45K+ GitHub stars (July 2026 measurements range 45.4K-46.3K) with a claimed 450M monthly workflows; and Princeton's HAL benchmark shows framework choice can move identical-model agent scores by up to 30 percentage points.) Gonka's flagship Kimi K2.6 (1T MoE, 32B active, 256K context, multimodal, agent-swarm focused) is competitive with frontier models for agent workloads at a fraction of the cost; its predecessor K2.5 scored 76.8% on SWE-Bench Verified and was stable across 200-300 sequential tool calls (FEATURES.md).

### Pain Points

- **Heartbeats cost nearly as much as actual messages.** At the Casual tier, heartbeats consume 44% of total tokens (460,800 tokens/day) despite generating zero user-facing output (pricing analysis Section 3). This persona sees their monthly bill and cannot reconcile "I only sent 50 messages today" with a $40+ charge.
  Source: gonka_agent_pricing_analysis.md Section 3 (Casual Tier)

- **OpenRouter free tier is unreliable for always-on agents.** Models "appear, disappear, hit throttles, degrade under peak load" and free requests are queued behind paid users (FEATURES.md citing OpenRouter Free API Changes 2026). For an agent running 24/7 on Telegram, this means missed messages and inconsistent responses during peak hours.
  Source: FEATURES.md Section: Developer Decision Criteria, criterion #2

- **Narrow model catalog still feels risky.** This persona currently uses OpenRouter, which provides access to 400+ active models across 70+ providers (OpenRouter's official figure as of mid-July 2026). Gonka now serves multiple model families -- Qwen, Kimi K2.6, and MiniMax M2.7, roughly five inference models at ~100M tokens/day combined -- so the old "single model, no fallback" objection has softened, but the breadth gap vs OpenRouter remains large. The competitive feature matrix scores Gonka as LOSE on model breadth.
  Source: gonka_competitive_feature_matrix.md Section 8 (Model Breadth); pricepertoken.com/endpoints/gonka (July 2026)

### Adoption Triggers

- Monthly OpenRouter bill crosses the $50 threshold and they search "cheaper OpenClaw inference provider" on Reddit or GitHub
- OpenRouter free tier degrades during a weekend when they are actively building, causing frustration and a search for alternatives
- They see a Reddit r/LocalLLaMA comparison post showing Kimi K2.6 performance at a fraction of GPT-5.4's cost ($2.50/$15 per 1M tokens) and click through to Gonka docs
- A ClawHub skill or community plugin for Gonka appears, making setup trivially easy (caveat: after the early-2026 ClawHavoc supply-chain incident -- Koi Security's Feb 1 audit found 341 malicious of 2,857 skills, OpenClaw's Feb 7 VirusTotal partnership removed ~2,419 suspicious skills and added automatic scanning of every published skill, Koi's continued scanning raised confirmed-malicious findings to 824 as ClawHub passed 10,700 skills (~Feb 16), and Antiy CERT researchers then pushed the count to 1,184+ malicious skill packages by Feb 19 (one analysis puts flagged-malicious-or-suspicious at ~7.6% of the registry; Unit 42's analysis covering Feb-May 2026 found five still-unblocked malicious skills, including a Base64 curl-pipe-bash dropper padded with 22 MB of filler specifically to exceed content-analysis size limits) -- ClawHub screening has scanning added but is being actively evaded, and users are suspicious of skills touching API keys or payments -- a listed skill must be signed and provenance-verified to be a trust asset rather than a liability)

### Objections

- **"I have never heard of Gonka."** Awareness is zero among mainstream OpenClaw developers who do not follow decentralized compute channels. Discovery depends on presence in the OpenClaw ecosystem (ClawHub, Discord, provider docs), which Gonka currently lacks.
  Source: ARCHITECTURE.md Objection Map ("I've never heard of Gonka" -- All personas)

- **"OpenRouter already works, why would I change?"** Switching inertia is real. OpenRouter is built into OpenClaw with zero configuration. Gonka requires manual JSON editing. The marginal effort feels unjustified unless the cost savings are dramatic and clearly documented.
  Source: ARCHITECTURE.md Objection Map ("OpenRouter already works" -- Builder persona); PITFALLS.md Pitfall 6 (ecosystem dynamics and default provider stickiness)

- **"Is this a crypto thing? I do not want to set up a wallet."** Any association with cryptocurrency triggers skepticism -- rug pulls, scams, and volatile tokens are top-of-mind for Web2 developers encountering blockchain-adjacent projects. If the landing page mentions "tokens" or "staking," this persona closes the tab immediately.
  Source: PITFALLS.md Pitfall 7 (crypto jargon alienation); PITFALLS.md Pitfall 2 (requiring crypto knowledge)

- **"Kimi is not Claude or GPT."** Unfamiliarity with the Kimi family creates doubt about model quality, despite strong benchmarks. This persona has muscle memory with Claude or GPT-5.x and needs concrete evidence that K2.6 handles their specific agent tasks (tool calling, code generation, multi-step reasoning) comparably. (This objection is dissolving: Kimi K3 launched via app/API July 16, 2026 -- 2.8T-param MoE, 1M-token context, $3/$15 per M tokens -- and became the first open model to top a frontier arena leaderboard, debuting #1 on Frontend Code Arena ahead of Claude Fable 5 and GPT-5.6 Sol, with full open weights scheduled by July 27. On overall intelligence indices K3 ranks third-to-fourth -- Artificial Analysis ~57 vs Fable 5 ~60 and GPT-5.6 Sol ~59 -- so it is frontend-frontier, not across-the-board frontier.)
  Source: ARCHITECTURE.md Objection Map ("K2.5 isn't Claude/GPT" -- Builder persona); July 2026 Kimi K3 coverage

### Gonka Value Proposition (for this persona)

- **Server-side session persistence eliminates heartbeat waste.** Gonka's sessions API maintains conversation state server-side, reducing heartbeat token overhead by ~80%. At the Casual tier, this drops monthly token consumption from 31.5M to ~12.6M tokens -- modeled in April 2026 as ~$47/month (Together AI) vs ~$13/month (Gonka Scenario B). These dollar figures are April 2026 estimates computed at K2.5-era rates and need recomputation against current K2.6/K3 pricing and cached-input baselines (Moonshot now offers 90% cached-input discounts) before external use. No other provider offers server-side sessions on the standard chat completions API.
  Maps to: Decision Driver #1 (cost per task)
  Source: gonka_agent_pricing_analysis.md Section 5 (Gonka hidden cost analysis)

- **Drop-in OpenClaw compatibility.** Gonka's OpenAI-compatible API means adding it as a custom provider requires editing one JSON block in `openclaw.json` -- setting `baseUrl`, `apiKey`, and `api: "openai-completions"`. No SDK changes, no new libraries, no code modifications. Competitive feature matrix scores Gonka as TIE on streaming and tool calling -- everything just works.
  Maps to: Decision Driver #2 (ease of integration)
  Source: STACK.md Section 1 (provider selection flow); FEATURES.md Section: Developer Decision Criteria, #4

- **Kimi K2.6 is purpose-built for agent tasks.** 1T MoE with 32B active parameters, 256K context window, multimodal, agent-swarm and long-horizon-coding focused (note: the K2.5 predecessor also had a 256K context -- earlier drafts citing 131K understated it by 2x). For the cost-conscious solo builder, K2.6 delivers frontier-adjacent agentic performance at open-source pricing.
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
   Evidence: FEATURES.md ranks cost as #1 overall, but for this persona it is #2 because unreliable cheap inference is worse than expensive reliable inference. At the Active tier, heartbeats account for 51% of token consumption (pricing analysis Section 3). With 6 channel-agents heartbeating independently, the overhead scales linearly with channel count. The April 2026 model put DeepInfra at $218/month vs Gonka Scenario B at $59/month at this tier -- a $159/month gap, meaningful for a startup watching runway (estimates pending recomputation at current K2.6/K3 rates). The macro trend strengthens the thesis: agentic workflows consume 5-30x the tokens of chatbots (Gartner, March 2026), inference is now ~85% of enterprise AI budgets, Goldman Sachs projects token consumption multiplying 24x between 2026 and 2030 on agent adoption, and the FinOps Foundation's 2026 State of FinOps report found 73% of enterprises reported AI costs exceeding original projections despite per-token prices falling 67% YoY -- consumption growth outran every budget model.

3. **Agent-native features** -- "I need sessions, model routing, and usage tracking built into the provider, not bolted on with custom middleware."
   Evidence: FEATURES.md Section: Differentiators lists session persistence, auto-tiering, memory API, and webhooks as Tier 1 high-impact features already built. Important July 2026 revision: cost-based model routing is now a commoditized layer in the OpenClaw ecosystem (ClawRouter ships alongside OpenClaw; third-party routers like BlockRunAI's ClawRouter and iblai/claw-router claim 70-92% savings), so routing is no longer a Gonka-unique WIN. The defensible differentiator is server-side sessions and memory -- state management that client-side routers cannot replicate. Delivery mechanism matters too: MCP (Model Context Protocol) is the dominant agent-tool integration standard as of July 2026 -- stewarded by the Linux Foundation's Agentic AI Foundation since December 2025, 97M+ monthly SDK downloads, 9,652 servers in the official registry (May 24, 2026), first-party support in ChatGPT, Gemini, Copilot, VS Code, and Cursor, and 41% of software organizations running MCP servers in production (Stacklok 2026; more bullish contested figures circulate). Note the protocol is evolving: the MCP 2026-07-28 release candidate (final spec ships July 28, 2026) makes remote MCP servers stateless and load-balancer-friendly (no sticky sessions, routing on an Mcp-Method header, cacheable tools/list) and adds an Extensions framework, a Tasks primitive (servers can answer tools/call with a task handle driven via tasks/get, tasks/update, tasks/cancel -- standardized server-directed async execution), MCP Apps, authorization hardening, and a formal deprecation policy, with Tier-1 SDKs expected to ship support within about ten weeks. Two implications: sessions/memory must be exposed compatibly with the stateless transport, and the Tasks primitive gives every MCP-capable stack a standardized async pattern -- narrowing Gonka's webhook differentiator. This persona expects sessions, memory, and tiering to be exposed as MCP tools, not just REST endpoints.

### Pain Points

- **Multi-agent heartbeat overhead scales linearly and dominates costs.** With 6 channel-agents, heartbeat overhead reaches 51% of total tokens (2.76M tokens/day just from heartbeats). Adding a 7th channel-agent increases monthly cost by ~$36 (at DeepInfra rates) with no increase in user-facing capability.
  Source: gonka_agent_pricing_analysis.md Section 3 (Active Tier)

- **Model routing is solved client-side, but state management is not.** As of mid-2026 this persona no longer maintains custom routing middleware -- they install a router (ClawRouter and similar tools classify tasks into tiers locally and route automatically; tiered routing is standard enterprise practice -- per the AICC (AI Cost Council) analysis of 2.4B enterprise API calls, blended enterprise cost fell from $18.40/M to $6.07/M tokens between Q1 2025 and Q1 2026 (a 67% drop attributed to routing/tiering plus price cuts), and organizations running a tiered model architecture achieved a Q1 2026 median blended cost of $2.31/M vs $18.40/M for frontier-only routing). What routers do not solve: session state and memory still live client-side and get re-transmitted on every heartbeat. That is the remaining overhead Gonka's server-side sessions address.
  Source: gonka_competitive_feature_matrix.md Section 2 (needs revision -- the April 2026 "all competitors scored LOSE on tiering" verdict is obsolete); github.com/openclaw/clawrouter; github.com/BlockRunAI/ClawRouter

- **No provider offers production-grade SLAs for agent workloads.** OpenAI and Anthropic offer SLAs but at premium pricing (multiples per token of Kimi-class providers). Kimi providers (Together AI, DeepInfra, Fireworks, OpenRouter) offer no formal SLAs. This persona is stuck choosing between reliability (expensive) and affordability (unguaranteed).
  Source: gonka_competitive_feature_matrix.md Section 7 (Uptime/Reliability); FEATURES.md Table Stakes ("Reasonable uptime >99%" -- NOT PROVEN for Gonka)

- **Prompt caching is a partial workaround, not a solution.** OpenAI and Anthropic both bill cached input at ~10% of the input rate (a 90% discount -- earlier drafts citing 50% for OpenAI are obsolete), and Moonshot's own API now offers 90% cached-input discounts too (Kimi K3: $0.30/M cached vs $3.00/M uncached). Caching reduces heartbeat costs materially but does not eliminate them -- tokens are still transmitted, processed, and billed at reduced rates. Server-side sessions eliminate the re-transmission entirely, but the savings differential must now be argued against 90%-cached baselines, not uncached ones.
  Source: gonka_competitive_feature_matrix.md Key Takeaway #4

### Adoption Triggers

- Monthly inference bill crosses $500 and the board asks "can we reduce infrastructure costs by 50%?" (the agent-cost-blowout pattern is now widely reported -- e.g. Uber's December 2025 Claude Code rollout going from 32% to 84% of a 5,000-engineer org between February and March 2026, averaging $150-$250/month per engineer with a $500-$2,000/month power-user tail, ~70% of committed code AI-generated, and the full 2026 AI budget exhausted in about four months)
- A production agent outage on OpenRouter during a customer demo triggers an urgent search for providers with reliability data
- They evaluate self-hosting vLLM and realize Gonka offers the same infrastructure with session persistence and tiering built in -- no DevOps overhead
- A competitor startup publishes a case study showing 70% cost reduction on Gonka, creating FOMO

### Objections

- **"Decentralized infrastructure means unreliable inference."** This is the primary blocker. The competitive feature matrix scores Gonka as LOSE on uptime/reliability -- no published SLA, no public status page, no historical uptime data. For a startup with paying customers, adopting unproven infrastructure is a career risk for the CTO.
  Source: ARCHITECTURE.md Objection Map ("Decentralized = unreliable" -- Startup persona); PITFALLS.md Pitfall 3 (unreliable inference undermining trust at first contact)

- **"We need model breadth and fallback depth."** Most production teams use multiple models (tiered routing is standard practice in 2026). Gonka now serves multiple families -- Qwen, Kimi K2.6, MiniMax M2.7 -- which answers the old "single model, no fallback" version of this objection, but roughly five models is still thin next to OpenRouter's hundreds, and the CTO will ask how quickly Gonka adds new flagship models (e.g. Kimi K3 once open weights land ~July 27, 2026).
  Source: FEATURES.md criterion #3 (model quality / multi-model); gonka_competitive_feature_matrix.md Section 8 (Model Breadth -- Gonka scored LOSE; margin has narrowed since April)

- **"Can it handle our scale?"** The CTO needs evidence of production-scale performance, not just integration test results. v1.2 tests demonstrate functional correctness but not concurrent load handling, failover behavior, or sustained throughput under multi-agent pressure.
  Source: ARCHITECTURE.md Objection Map ("Can it handle production scale?" -- Startup persona)

- **"I do not want to explain to investors why we depend on crypto infrastructure."** Even if the CTO personally understands decentralized compute, explaining it to non-technical investors creates friction. If Gonka's marketing materials look like a DeFi protocol, the CTO will not share them internally.
  Source: PITFALLS.md Pitfall 1 (leading with decentralization); Pitfall 7 (crypto jargon)

### Gonka Value Proposition (for this persona)

- **Session persistence at scale: ~73% modeled cost reduction at the Active tier.** The April 2026 model put DeepInfra at $218/month at the Active tier vs $59/month for Gonka Scenario B (estimates -- recompute at current K2.6/K3 rates and against cached-input baselines before quoting externally). The savings come from eliminating heartbeat context re-sending via server-side sessions -- a structural advantage that scales as more agents are added.
  Maps to: Decision Driver #2 (cost at scale)
  Source: gonka_agent_pricing_analysis.md Section 6 (Active Tier monthly cost projections)

- **Built-in model tiering, now table stakes rather than a moat.** Gonka's X-Gonka-Tier header and content-aware auto-routing route classification to lighter models and reasoning to K2.6 automatically, with no application code changes. Since client-side routers (ClawRouter et al.) now provide comparable routing for any provider, this is a convenience parity feature -- the pitch should lead with sessions/memory and treat tiering as included, not differentiating.
  Maps to: Decision Driver #3 (agent-native features)
  Source: gonka_competitive_feature_matrix.md Section 2 (Model Tiering -- verdict obsolete as of July 2026); ARCHITECTURE.md Architecture-to-Message Mapping

- **Webhook notifications enable event-driven agent architecture.** Gonka's webhook system (built in v1.2) notifies agent backends when async tasks complete, costs exceed thresholds, or models update. This lead is narrowing: OpenAI's background mode and the MCP 2026-07-28 Tasks primitive (standardized async task handles for every MCP-capable stack) both close part of the gap, so the pitch is "inference-layer webhooks today, plus MCP Tasks support on the roadmap" rather than a unique capability. For a startup running production agents, this still means fewer polling loops and more responsive agent behavior.
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
   Evidence: FEATURES.md ranks data privacy as #7 and censorship resistance as #8 by overall community frequency, but for this persona they are the #1 non-negotiable requirement. FEATURES.md notes "OpenRouter allows restricting to trusted providers; some devs run local models for privacy" and "Growing demand for uncensored models; OpenClaw devs want agents that can discuss anything." Gonka's position on both is rated STRONG: "Decentralized = no single entity logs all prompts" and "Decentralized network has no content policy; the served models (Kimi K2.6, Qwen, MiniMax M2.7) are open-weight."

2. **Model quality for unrestricted tasks** -- "The model needs to handle edge cases that GPT-5.x refuses -- drafting adversarial legal arguments, discussing sensitive medical conditions, generating security exploit analyses."
   Evidence: FEATURES.md anti-features table notes OpenAI and Anthropic have strict content policies. The Kimi models Gonka serves are open-weight with no built-in content filtering. For this persona, model quality is inseparable from model freedom -- a model that refuses the prompt is a model with zero quality for their use case, regardless of benchmark scores.

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

- **"What if none of Gonka's models can handle my specific use case?"** Privacy-sensitive tasks often require specialized capabilities (legal reasoning, medical terminology, code analysis). Gonka's catalog (Qwen, Kimi K2.6, MiniMax M2.7) gives some fallback options, but these are general-purpose agent models -- they may not match GPT-5.x or Claude on domain-specific tasks, and the catalog is still a fraction of OpenRouter's.
  Source: gonka_competitive_feature_matrix.md Section 8 (Model Breadth -- LOSE for Gonka)

- **"I do not trust 'no content policy' from a company I have never heard of."** The absence of content filtering is a feature for this persona, but only if the provider is credible. An unknown provider claiming "no rules" could be a fly-by-night operation that disappears with their data.
  Source: PITFALLS.md Pitfall 3 (unreliable inference undermining trust); Pitfall 5 (community theater vs genuine adoption)

### Gonka Value Proposition (for this persona)

- **Open-weight models on decentralized infrastructure: no content policy, no centralized prompt logs.** Kimi K2.6, Qwen, and MiniMax M2.7 are open-weight with no built-in content filtering. Gonka's decentralized network has no central authority that can impose content policies or review prompts. For use cases blocked by OpenAI/Anthropic filters, Gonka serves unrestricted inference through a standard API.
  Maps to: Decision Driver #1 (privacy and censorship resistance)
  Source: FEATURES.md Messaging Theme #3; competitive feature matrix (Gonka: "None (open)" on content filtering)

- **Agent features that self-hosting cannot match.** Self-hosted vLLM gives privacy but not session persistence, automatic tiering, memory API, or webhook notifications. Gonka offers both: the privacy guarantees of open-weight decentralized inference AND the agent-native features of a managed platform.
  Maps to: Decision Driver #1 + practical value
  Source: gonka_provider_landscape_map.md (Gonka uniquely combines decentralized + agent-native); FEATURES.md gap analysis

- **Cost advantage over self-hosting.** Decentralized compute costs 60-80% less than centralized alternatives (FEATURES.md Section: Developer Decision Criteria, Gonka Position for criterion #1). For this persona, Gonka's per-token pricing may be lower than the total cost of ownership of running their own GPU -- especially when factoring in electricity, maintenance, and the engineering time saved by using Gonka's built-in agent features.
  Maps to: Decision Driver #3 (cost vs self-hosting)
  Source: FEATURES.md; gonka_agent_pricing_analysis.md Section 5 (Gonka hidden cost analysis)

---

## AAARRRP Journey Maps

The AAARRRP framework (Phil Leggetter, 2016) extends the AARRR pirate metrics with two stages critical for developer-focused products: **Awareness** at the front (how developers discover the product before any signup) and **Product** at the back (how developer feedback shapes the roadmap). The 7 stages are: Awareness, Acquisition, Activation, Retention, Revenue, Referral, Product.

Each persona below has a complete journey map with OpenClaw-specific touchpoints, persona-specific objections sourced from the research corpus, and measurable key metrics per stage.

---

### Journey Map: The Weekend Builder

| Stage | Touchpoint | Action | Objection | Content/Asset Needed | Key Metric |
|-------|-----------|--------|-----------|---------------------|------------|
| **Awareness** | Reddit r/LocalLLaMA or r/OpenClaw thread comparing Kimi inference providers by cost | Reads a comparison post showing per-task costs across providers; sees Gonka listed with session-based savings; clicks link to docs.gonka.ai | "Never heard of Gonka -- is this some crypto scam or a real API provider?" (ARCHITECTURE.md Objection Map; PITFALLS.md Pitfall 7) | Comparison blog post: "OpenClaw Inference Costs: Gonka vs OpenRouter vs Together AI" with a calculator showing heartbeat savings. Landing page must look like Vercel, not a DeFi protocol (PITFALLS.md Pitfall 1). | Unique visitors to docs.gonka.ai from Reddit referral links |
| **Acquisition** | docs.gonka.ai quickstart page | Clicks "Get API Key," authenticates via GitHub OAuth, receives API key in under 60 seconds. No credit card, no wallet, no token purchase. | "Do I need to create a wallet or buy tokens to use this?" (PITFALLS.md Pitfall 2 -- 95% funnel drop at wallet step) | Self-serve signup flow with GitHub OAuth. Prominent "No wallet required. No tokens needed. Just an API key." messaging on signup page. | API keys created per week; time from landing to key creation (target: under 2 minutes) |
| **Activation** | Terminal / code editor with openclaw.json open | Copies the Gonka provider config snippet from docs (3 fields: `baseUrl`, `apiKey`, `api: "openai-completions"`), pastes into `openclaw.json`, adds `gonka/kimi-k2.6` to agent model allowlist, runs existing agent. First response arrives from K2.6 through Gonka network. Aha moment: "It just works, and it is faster than I expected." | "What if my agent breaks after switching providers? I do not want to debug config issues on a Saturday." (PITFALLS.md Pitfall 6 -- ecosystem dynamics, provider config friction) | Pre-built openclaw.json snippet on docs page with copy button. "Add Gonka to OpenClaw in 90 seconds" tutorial. Troubleshooting guide for the two-step provider gotcha (provider definition + model allowlisting per STACK.md). | First API call within 24 hours of key creation; time from key creation to first successful inference (target: under 5 minutes) |
| **Retention** | Usage dashboard at dashboard.gonka.ai or API usage endpoint | Checks daily spend after one week of usage. Sees session persistence reduced heartbeat costs by 70-80% vs OpenRouter. Compares: "$40/month on OpenRouter vs $13/month on Gonka for the same agent" (April 2026 modeled figures -- refresh against current rates). Keeps using Gonka as primary provider. | "Is this cost savings real and sustainable, or is it a temporary promo that will end?" (PITFALLS.md Pitfall 4 -- race to bottom, unsustainable pricing) | Cost comparison calculator: "Your OpenClaw bill: OpenRouter vs Gonka" showing heartbeat savings breakdown. Usage API endpoint returning spend-to-date with session token savings highlighted. | API calls in week 2+ after signup; week-over-week retention rate; percentage of users who make calls in 3 consecutive weeks |
| **Revenue** | Pricing page at docs.gonka.ai/pricing | Exceeds free trial credit ($5-10 per FEATURES.md Anti-Features: "Offer a generous trial credit"). Sees clear pricing: per-token rates with session savings calculator. Enters credit card. Continues using Gonka. | "What if I set up billing and my agent runs away with costs? OpenClaw agents can spike unpredictably." (FEATURES.md: "$300+ in 2 days" community complaints) | Spending caps and usage alerts (configurable via API). Pricing page with "no surprise bills" guarantee and per-day spending limit feature -- the buyer pain is industry-wide: 73% of enterprises reported AI costs exceeding projections despite 67% YoY per-token price declines (FinOps Foundation, 2026). Pricing comparison table: Gonka vs OpenRouter vs Together AI at Casual tier. | Free-to-paid conversion rate; median time from first call to first payment; monthly revenue per user at Casual tier |
| **Referral** | Twitter/X or Reddit | Tweets "just cut my OpenClaw bill by ~2/3 by switching to Gonka -- sessions eliminate heartbeat waste" with a screenshot of their cost comparison (illustrative; per pricing analysis v2.0, external claims should be tracker-verified "cheapest listed provider for K2.6/M2.7" statements with the utilization/subsidy caveat, not the April 2026 $40-to-$13 figures). Posts in r/OpenClaw or r/LocalLLaMA with their experience and config snippet. | "I do not want to recommend something that might go down and make me look bad." (PITFALLS.md Pitfall 3 -- reliability reputation) | Shareable cost savings badge/screenshot template. Referral credit program: $5 credit for each referred developer who makes 100+ API calls. Pre-written tweet/post templates with accurate claims. | Organic Gonka mentions on Reddit/Twitter per week; referral signup rate; viral coefficient (referrals per active user) |
| **Product** | GitHub issues on gonka-ai-infrastructure repo or feedback form at docs.gonka.ai/feedback | Submits a feature request: "Add DeepSeek R1 as a budget fallback model" or reports a bug: "Sessions drop after 4 hours of inactivity." Receives a response within 48 hours. | "Will anyone actually read my feedback? Open-source projects often ignore issues." (PITFALLS.md Pitfall 5 -- community theater vs genuine engagement) | Public GitHub repo with issue templates for bug reports and feature requests. Monthly "what we shipped from community feedback" blog post. Visible issue response time SLA (48 hours). | Feature requests submitted per month; bug reports per month; median response time on GitHub issues; percentage of issues with team response within 48 hours |

---

### Journey Map: The Startup CTO

| Stage | Touchpoint | Action | Objection | Content/Asset Needed | Key Metric |
|-------|-----------|--------|-----------|---------------------|------------|
| **Awareness** | Hacker News "Show HN" post or a technical blog post comparing agent infrastructure costs at scale | Reads a deep-dive analysis on agent inference costs, including the heartbeat overhead problem and session persistence as a solution. Sees Gonka cited as the only provider with server-side sessions. Bookmarks docs.gonka.ai for team evaluation. | "Interesting technology, but decentralized infrastructure is a red flag for production workloads. Akash and Render both struggled with reliability." (PITFALLS.md Pitfall 3; competitive feature matrix Section 7 -- Gonka LOSE on uptime) | Technical white paper: "The Hidden Cost of Agent Heartbeats: Why Session Persistence Saves 73% at Scale." Includes uptime data and p95 latency benchmarks (once available). Must read like a Cloudflare blog post, not a crypto whitepaper. | Hacker News upvotes and comment quality; docs.gonka.ai traffic from HN; enterprise inquiry form submissions |
| **Acquisition** | docs.gonka.ai/enterprise or team onboarding flow | Creates team account, generates multiple API keys for dev/staging/prod environments. Reviews architecture docs explaining how decentralized inference achieves reliability through redundant nodes and health-checked routing. | "I need to justify this to my co-founder and investors. If your docs mention blockchain or tokens, I cannot share this internally." (PITFALLS.md Pitfall 7 -- crypto jargon; Pitfall 1 -- decentralization-first messaging) | Team account management: multiple API keys with scoped permissions (per-environment, per-budget). Architecture overview page explaining reliability without blockchain jargon: "redundant infrastructure across multiple regions" not "decentralized validator network." | Team accounts created per month; number of API keys per team account; architecture doc page views |
| **Activation** | Staging environment with 1 agent connected to Gonka | Deploys one agent on staging with Gonka as provider. Runs integration tests (agent session creation, heartbeat cost measurement, tool calling verification). Measures p95 latency and compares to current provider. Aha moment: "Our staging agent costs $2/day on Gonka vs $7/day on DeepInfra, and latency is comparable." (Illustrative figures from the April 2026 pricing model.) | "We tested one agent on staging. How do I know it will hold up with 6 channel-agents in production?" (ARCHITECTURE.md Objection Map: "Can it handle production scale?") | Staging-to-production migration guide. Load testing results showing concurrent agent performance. OpenClaw integration test suite results (from v1.2 test infrastructure). API endpoint for real-time latency and uptime metrics. | First API call by team accounts within 7 days; staging-to-production conversion rate; p95 latency delta vs current provider |
| **Retention** | Production dashboard showing multi-agent costs and reliability metrics | Monitors 6 channel-agents running on Gonka. Reviews weekly cost reports showing session persistence savings. Tracks uptime against internal SLA requirements. Gradual migration: moves 2 agents to Gonka first, then 4, then all 6 as confidence builds. | "We had one timeout last Tuesday at 3am. Is that a pattern or a fluke? I need incident reports." (PITFALLS.md Pitfall 3 -- first impressions are permanent for infrastructure trust) | Real-time status page (status.gonka.ai) with per-model availability, regional latency, and historical uptime graphs. Incident report template and post-mortem publication process. Weekly email report: cost savings, uptime percentage, p95 latency trends. | Monthly active agents per team; week-over-week agent count growth; uptime as measured by client-side monitoring; support ticket volume per team |
| **Revenue** | Enterprise pricing discussion or self-serve paid tier | Commits to paid plan after 2-4 weeks of staging + gradual production rollout. Negotiates volume pricing for 161M+ tokens/month. Explores GNK API credit discount (optional, not required -- USD billing default). | "We need a formal SLA with credits for downtime. Our customers have SLAs with us, and we need to pass that guarantee upstream." (competitive feature matrix Section 7 -- no Gonka SLA currently) | Enterprise pricing tier with committed-use discounts. SLA framework: 99.5% uptime target with credit mechanism (even PITFALLS.md notes this is a differentiator -- "even Venice.ai doesn't do this"). Invoice and receipt system for accounting/procurement. | Enterprise plan conversion rate; average contract value; committed monthly token volume; SLA credit payouts (lower is better) |
| **Referral** | Tech blog or conference talk | Writes a company engineering blog post: "How We Cut Agent Infrastructure Costs by 73% with Session Persistence" detailing their migration from DeepInfra to Gonka. Presents at an AI engineering meetup or conference. | "If Gonka has an outage after I publicly recommend them, it reflects poorly on our engineering judgment." (PITFALLS.md Pitfall 3 -- reliability reputation) | Case study co-creation program: Gonka helps draft the blog post with accurate data. Speaking opportunity support: presentation templates, benchmark data, demo environment. Co-branded content with "Built with Gonka" badge for production deployments. | Engineering blog posts mentioning Gonka per quarter; conference talks featuring Gonka; inbound leads from case study referrals |
| **Product** | Dedicated Slack channel or private GitHub discussions with Gonka engineering team | Requests roadmap features: additional model support (DeepSeek R1 as fallback), Redis-backed session persistence (addressing v1.2 in-memory tech debt), and multi-region routing. Participates in quarterly product advisory calls. | "We are investing engineering time integrating with Gonka. If the roadmap does not align with our needs, we need to know now." (PITFALLS.md Pitfall 4 -- competing on price alone without feature evolution) | Product advisory program for high-volume customers. Public roadmap with timeline visibility. Private beta access for new features. Quarterly advisory board call with engineering team. | Feature requests from enterprise customers per quarter; percentage of enterprise-requested features shipped within 6 months; advisory board participation rate |

---

### Journey Map: The Privacy-First Agent Builder

| Stage | Touchpoint | Action | Objection | Content/Asset Needed | Key Metric |
|-------|-----------|--------|-----------|---------------------|------------|
| **Awareness** | GitHub gonka-ai-infrastructure repository README or a technical article on privacy-preserving inference architectures | Discovers Gonka while researching alternatives to self-hosted vLLM for sensitive workloads. Reads about open-weight Kimi/Qwen/MiniMax models served on decentralized infrastructure with no content policies. Checks if "no prompt logging" is an architectural guarantee or just a marketing claim. | "Every cloud provider says they do not log data, then gets subpoenaed and it turns out they do. How is Gonka different architecturally?" (PITFALLS.md Pitfall 1 -- decentralization claims must be backed by technical reality; FEATURES.md Tier 3 differentiator: encrypted inference is "Very High complexity, not yet built") | Technical deep-dive: "How Decentralized Inference Protects Prompt Privacy -- Architecture, Not Promises." Must honestly address current limitations (no TEE yet) while explaining structural advantages (no central log aggregation, open-weight model, independent node operators). | GitHub repo stars from privacy/security communities; docs.gonka.ai traffic from privacy-focused forums (Lobsters, security-focused subreddits); time spent on privacy architecture page |
| **Acquisition** | docs.gonka.ai signup with focus on data handling documentation | Reviews data handling policy and privacy architecture docs before signing up. Looks for: no-log policy, data residency information, node operator agreements, open-source infrastructure code (verifiable claims). Creates API key only after satisfying privacy requirements. | "I need to verify these privacy claims independently. Is the infrastructure code open source so I can audit it?" (PITFALLS.md Pitfall 3 -- trust at first contact; FEATURES.md criterion #7: "some devs run local models for privacy" -- high bar for trust) | Open-source infrastructure code (already at github.com/mitgor/gonka-ai-infrastructure). Published data handling policy: what is logged, what is not, for how long, under what jurisdictions. No-log verification guide: how to audit node behavior independently. | Signups that viewed privacy docs first (percentage); time spent on data handling policy page before signup; API keys created by users from privacy-focused referral sources |
| **Activation** | Terminal with openclaw.json -- configuring Gonka for a sensitive workload | Configures Gonka as the provider for a sensitive agent workload. Tests with prompts that would be blocked by OpenAI/Anthropic content filters (legal adversarial arguments, security exploit analysis, medical condition discussions). Aha moment: "It processed my prompt without filtering or refusing. And the agent session persists server-side so I am not re-sending sensitive context on every heartbeat." | "What if a Gonka node operator is logging my prompts? Decentralized does not mean encrypted." (FEATURES.md Tier 3: "Privacy-preserving inference -- Encrypted prompts; no host sees plaintext" is listed as Very High complexity, NOT YET BUILT) | Honest capabilities page: "What Gonka guarantees today vs what is on the roadmap." Today: no central log aggregation, no content filtering, open-weight model. Roadmap: TEE-based encrypted inference. Comparison: "Gonka privacy vs self-hosted vLLM privacy vs OpenAI privacy." | First API call with a prompt that would be filtered on OpenAI/Anthropic; session creation for sensitive workloads; percentage of activation calls that complete without content filtering |
| **Retention** | Ongoing usage with monitoring of Gonka's privacy posture | Uses Gonka for all sensitive inference workloads. Monitors Gonka's open-source repo for privacy-relevant changes. Periodically audits node behavior using the verification guide. Keeps self-hosted vLLM as backup for highest-sensitivity tasks until TEE is available. | "Gonka updated their terms of service. Did anything change about data handling? I need to re-audit." (FEATURES.md criterion #7 -- ongoing trust, not one-time verification) | Changelog for privacy-relevant changes (tagged separately from feature releases). Automated privacy audit tool: script that checks node behavior and reports anomalies. Community-maintained privacy watchdog (open-source). | Retention rate for privacy-focused users; percentage of users who maintain Gonka as primary vs backup provider; privacy audit script downloads/runs per month |
| **Revenue** | Paid tier with privacy-specific features | Converts to paid plan. Values session persistence for reducing how often sensitive context traverses the network. Willing to pay a premium for privacy-preserving features (TEE, encrypted inference) when available. | "I would pay more for guaranteed encrypted inference. Is that on the roadmap with a timeline?" (FEATURES.md Tier 3 differentiator -- "Very High complexity") | Privacy-tier pricing: standard pricing with optional TEE-backed inference at a premium when available. Roadmap commitment on encrypted inference with quarterly updates. Early access program for privacy beta features. | Revenue from privacy-focused users; willingness-to-pay survey for TEE features; privacy tier conversion rate (when available) |
| **Referral** | Privacy-focused communities: Lobsters, security subreddits, open-source mailing lists | Writes a detailed technical review: "Running Sensitive AI Workloads on Gonka: A Privacy Audit" on their personal blog or in an open-source community. Shares openclaw.json config for privacy-optimized Gonka setup. | "I can only recommend this if I can honestly say the privacy guarantees hold up to scrutiny. Overclaiming will damage my reputation in the security community." (PITFALLS.md Pitfall 1 -- claims must match reality) | Privacy audit results template (community-contributed). "Gonka Privacy Review" companion doc for referrers to share alongside their recommendation. Honest limitations page that referrers can point to: "here is what Gonka guarantees today and what is still in progress." | Privacy-focused blog posts reviewing Gonka; mentions in security/privacy community channels; referral signups from privacy-focused sources; sentiment analysis of privacy community discussions |
| **Product** | GitHub security advisories and privacy feature requests on gonka-ai-infrastructure repo | Files feature requests for TEE-based encrypted inference, per-request encryption options, and zero-knowledge proof of no-logging. Reports potential privacy vulnerabilities through responsible disclosure. Contributes to open-source privacy tooling. | "If I report a privacy vulnerability, will it be fixed quickly or buried? I have seen open-source projects ignore security issues for months." (PITFALLS.md Pitfall 5 -- community theater) | Responsible disclosure policy with 72-hour acknowledgment SLA. Security advisory publication process. Bug bounty program for privacy/security issues. Public privacy roadmap with community voting on priorities. | Privacy-related feature requests per quarter; responsible disclosure reports and resolution times; privacy-focused open-source contributions from community; TEE feature demand signal (upvotes, comments) |

---

## Cross-Persona Insights

### Common Objections Across All Personas (Universal Blockers)

Three objections appear across all three personas and represent the universal barriers to Gonka adoption:

1. **"I have never heard of Gonka."** Zero awareness among mainstream OpenClaw developers. Gonka is not a built-in OpenClaw provider, has no ClawHub presence, and is absent from provider comparison discussions in the OpenClaw community. Until awareness is established, all other journey stages are moot.
   Source: ARCHITECTURE.md Objection Map; gonka_provider_landscape_map.md (5 critical gaps)

2. **"Is this a crypto thing?"** The association between decentralized infrastructure and cryptocurrency triggers immediate skepticism. Web2 developers associate "crypto" with scams, volatility, and unnecessary complexity. Gonka's landing page, docs, and messaging must look and feel like a cloud platform (Vercel, Supabase) not a DeFi protocol.
   Source: PITFALLS.md Pitfalls 1, 2, and 7

3. **"Can I trust the reliability?"** Decentralized infrastructure has a reputation problem. Akash saw active providers drop below 100; Render's daily active users declined below 100 (PITFALLS.md Pitfall 3). Every persona needs evidence -- uptime stats, latency data, public status page -- before committing production workloads.
   Source: PITFALLS.md Pitfall 3; competitive feature matrix Section 7

### Scope Note: The Agent-as-Customer Segment (July 2026)

The "No wallet required. No tokens needed. Just an API key." framing remains correct for all three human personas above. But since April 2026, agent-native payment rails have gone mainstream: the x402 Foundation went operationally live under the Linux Foundation on July 14, 2026 with 40 member organizations across three tiers -- including Visa, Mastercard, American Express, Stripe, Ripple, Google, AWS, Shopify, Cloudflare, and Coinbase -- and in the 30 days ending ~July 15, 2026 the protocol processed ~75M transactions moving ~$24M (~$800K/day) between ~94,000 buyers and ~22,000 sellers, settling predominantly in USDC. Chainalysis reports x402 agentic payments crossed 100M cumulative transactions on Base within three quarters (June 2026), with $1+ transactions growing from 49% to 95% of payment value while 10c-$1 transactions collapsed from 46% to 4%. The April-era "volume is still small / arguably organic" caveat no longer holds. In Gonka's own target ecosystem, BlockRunAI's ClawRouter already authenticates OpenClaw agents with wallet signatures and pays for inference via USDC micropayments over x402 -- occupying the "agent-native payments for OpenClaw" position. Gonka, already a crypto network, has a natural x402 story for a fourth, non-human buyer: the autonomous agent paying for its own inference. Note that x402 is one layer of a three-layer 2026 agentic-payments stack: x402 handles machine-to-machine execution/micropayments; AP2 (now under the FIDO Alliance -- Google donated the Agent Payments Protocol, making it community-led) handles authorization via signed Intent/Cart/Payment mandates (60+ partners; shipped in production with Gemini Spark, May 2026; AP2 v0.2's "Human Not Present" payments let agents execute autonomously, blurring the clean execution/authorization split with x402); and ACP -- now an open standard co-created by Stripe, OpenAI, and Meta -- handles agent checkout (Instant Checkout live for US ChatGPT users buying from US Etsy sellers, 1M+ Shopify merchants announced, Salesforce support announced). For agent-procured inference x402 is the correct layer, but enterprise buyers will ask about AP2/ACP. This segment is out of scope for these personas but should be evaluated separately; it does not change the API-key-first messaging for human developers.
   Source: x402 Foundation announcements; Chainalysis x402 adoption data; github.com/BlockRunAI/ClawRouter; Google AP2 / OpenAI-Stripe ACP launch coverage

### Stage Where Each Persona Is Most Likely to Drop Off

| Persona | Highest Drop-off Stage | Why | Mitigation Priority |
|---------|----------------------|-----|-------------------|
| Weekend Builder | **Awareness to Acquisition** | Has never heard of Gonka; even if they see a mention, crypto association causes tab-close before reaching signup. Conversion from awareness to signup depends entirely on first-impression messaging. | P0: Landing page that looks like a cloud platform. Comparison content on Reddit/r/LocalLLaMA. |
| Startup CTO | **Activation to Retention** | Successfully tests on staging but stalls at production migration. The gap between "works on staging" and "trusted for production" requires uptime data, SLA frameworks, and incident response processes that Gonka does not yet have. | P0: Public status page. P1: SLA framework with credit mechanism. |
| Privacy-First Builder | **Acquisition to Activation** | Reviews privacy docs during signup and discovers that encrypted inference (TEE) is not yet built. The gap between "no central logging" (current) and "no host can see prompts" (required for highest-sensitivity workloads) stalls adoption. | P0: Honest capabilities page distinguishing current vs roadmap privacy features. |

### Content Assets That Serve Multiple Personas Simultaneously

| Asset | Personas Served | Why Multi-Persona |
|-------|----------------|-------------------|
| **"OpenClaw Inference Cost Comparison: Gonka vs OpenRouter vs Together AI"** blog post with heartbeat savings calculator | Weekend Builder (primary), Startup CTO (secondary) | Both cost-driven personas need to see the session persistence savings quantified. The Weekend Builder shares it on Reddit; the CTO shares it with their co-founder. |
| **openclaw.json config snippet with copy button** on docs.gonka.ai | All three personas | Every persona goes through the same activation step: pasting a provider config into openclaw.json. The snippet must be copy-paste ready with all three fields (baseUrl, apiKey, api type) and the model allowlist entry. |
| **Public status page (status.gonka.ai)** with real-time uptime, p95 latency, and historical data | Startup CTO (primary), Weekend Builder (secondary), Privacy-First (tertiary) | The CTO needs it for production evaluation. The Weekend Builder checks it to verify the provider is real. The Privacy-First builder monitors it as part of ongoing trust verification. |
| **"How Gonka Works: Architecture Without the Jargon"** technical explainer | All three personas | Addresses the universal "is this a crypto thing?" objection by explaining decentralized inference using cloud infrastructure language (redundant nodes, health-checked routing, geographic distribution) without blockchain terminology. |
| **Data handling and privacy policy page** | Privacy-First (primary), Startup CTO (secondary) | The Privacy-First builder needs it as a prerequisite for signup. The CTO needs it for compliance review before enterprise adoption. |
| **Official Gonka MCP server** exposing sessions, memory, tiering, and usage/cost queries as MCP tools | Startup CTO (primary), Weekend Builder (secondary) | MCP is the standard agent-tool delivery mechanism in 2026 (already planned in the partnership playbook); build it against the 2026-07-28 spec (final July 28, 2026), whose stateless remote-server transport shapes how Gonka's stateful sessions/memory should be exposed, and target the new Tasks primitive for async work (webhook notifications become the complement, not the sole async channel). A registry-listed Gonka MCP server makes agent-native features discoverable inside ChatGPT, Copilot, Cursor, and every MCP-capable agent framework -- distribution the REST API alone does not get. |

### Priority Ranking of AAARRRP Stages by Impact

Based on where each persona drops off and where Gonka's current gaps are largest, the stages should be prioritized for investment:

| Priority | Stage | Rationale |
|----------|-------|-----------|
| **P0** | **Awareness** | All three personas have zero awareness of Gonka. No journey progresses past Stage 1 without investment here. Content on Reddit, Hacker News, and GitHub. Landing page that passes the "is this crypto?" test. |
| **P0** | **Acquisition** | Self-serve API key signup does not exist (gonka_provider_landscape_map.md: critical gap). Without it, Awareness investment is wasted -- interested developers cannot sign up. |
| **P1** | **Activation** | The openclaw.json config snippet and quickstart guide are essential. The two-step provider gotcha (provider definition + model allowlisting) will trip developers without clear documentation (STACK.md). Time-to-first-inference target: under 5 minutes. |
| **P1** | **Retention** | Status page, cost comparison tools, and usage dashboards convert trial users into sustained users. The Startup CTO will not move to production without uptime evidence. |
| **P2** | **Revenue** | Pricing page, spending caps, and billing infrastructure. Less urgent than Awareness/Acquisition because developers cannot pay if they cannot sign up. But must be ready before the free trial credit runs out. |
| **P3** | **Referral** | Referral programs and case study support. This stage activates organically once Retention is strong -- happy developers share naturally. Structured referral programs amplify but do not create this behavior. |
| **P3** | **Product** | Feedback channels (GitHub issues, advisory programs). Important for long-term retention and roadmap alignment, but not a growth bottleneck in the early stages. |

### Journey Divergence Summary

The three journey maps reveal fundamentally different adoption patterns that cannot be served by a single marketing funnel:

- **The Weekend Builder** follows a **self-service, content-driven path.** They discover Gonka through organic community content (Reddit, GitHub), sign up without talking to anyone, and evaluate entirely through personal experimentation. Their journey is optimized by reducing friction at every step: copy-paste configs, instant API keys, obvious cost savings.

- **The Startup CTO** follows a **trust-building, evidence-driven path.** They discover Gonka through technical credibility signals (Hacker News, engineering blogs), evaluate through structured staging tests, and adopt through gradual production migration. Their journey is optimized by providing reliability evidence: uptime data, SLA frameworks, incident response processes, and peer case studies.

- **The Privacy-First Builder** follows an **audit-driven, verification-first path.** They discover Gonka through privacy architecture discussions, evaluate by auditing the open-source codebase and data handling policies, and adopt only after satisfying themselves that privacy claims are technically grounded. Their journey is optimized by radical transparency: open-source infrastructure, honest capabilities documentation, and verifiable privacy guarantees.

These divergent paths mean that Phase 17 (Messaging) must produce persona-specific messaging -- not a single value proposition -- and Phase 18 (Channels) must allocate resources to different channels for each persona rather than concentrating on one "primary" channel.

---

*Document: gonka_developer_personas.md | Version 1.3 | 2026-07-18*
*Companion documents: gonka_competitive_feature_matrix.md, gonka_agent_pricing_analysis.md, gonka_provider_landscape_map.md*

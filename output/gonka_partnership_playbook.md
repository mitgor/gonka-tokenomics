# Gonka Partnership & Ecosystem Strategy Playbook

**Version:** 1.3
**Date:** 2026-07-18 (updated from 2026-04-01 original)
**Classification:** Internal -- strategic playbook for Gonka's OpenClaw ecosystem integration
**Status:** Strategy Document
**Dependencies:** Phase 15 competitive analysis (gonka_competitive_feature_matrix.md), Phase 17 messaging (gonka_message_house.md), Phase 18 channel strategy (gonka_channel_strategy.md), provider landscape gap analysis (gonka_provider_landscape_map.md)
**Requirement:** GTM-02

---

## Executive Summary

Gonka's path to developer adoption runs through the OpenClaw ecosystem. This playbook defines a four-tier integration roadmap -- from custom provider listing to built-in provider status and co-development partnership -- with specific prerequisites, effort estimates, timelines, and success criteria at each tier. It also provides a ClawHub skill submission plan, a community-first strategy for getting Gonka merged as a built-in OpenClaw provider, and a comprehensive technical requirements checklist tracking what Gonka must deliver before each tier can be unlocked.

All partner-facing language in this playbook follows Phase 17 positioning: lead with heartbeat cost reduction (73% savings via server-side session persistence), not decentralization or network economics. Partner conversations should reference the message house (gonka_message_house.md) for approved vocabulary and positioning guidance.

### What Changed Since the April Original (July 2026 Update)

Five ecosystem shifts materially affect this playbook:

1. **Model refresh.** Kimi K2.5 has been superseded twice: Kimi K2.6 (April 2026 -- 1T MoE, 32B active, ~256K context, multimodal) and Kimi K2.7-Code (June 2026 -- coding/agent model, Modified MIT, official API $0.95 input / $4.00 output per 1M). Moonshot launched Kimi K3 via app/API on July 16, 2026 (2.8T MoE, 896 experts / 16 active, 1M context, native multimodal, $3/$15 per 1M, $0.30 cached input; full open weights still scheduled by July 27, 2026 -- the largest open-weight release ever). K3 debuted #1 in Frontend Code Arena ahead of Claude Fable 5 and GPT-5.6 Sol -- the first open model at the closed-frontier tier. All model references in this playbook now target K2.6 as the workhorse tier with K2.7-Code and K3 as follow-ons; a K2.5-only catalog is a generation behind and undermines the "agent-native" pitch.
2. **ClawHub trust crisis.** The ClawHavoc supply-chain campaign triggered a registry purge and hardened screening. The sourced sequence: Koi Security's Feb 1, 2026 audit found 341 malicious skills out of 2,857 scanned (335 in the ClawHavoc/AMOS campaign); OpenClaw partnered with VirusTotal on Feb 7, 2026, removing ~2,419 suspicious skills and adding automatic scanning of every published skill; Koi's continued scanning raised confirmed-malicious findings to 824 (~Feb 16, as ClawHub passed 10,700 skills); by Feb 19, Antiy CERT researchers had uncovered at least 1,184 malicious skill packages, with one analysis putting flagged-malicious-or-suspicious at ~7.6% of the registry, and Unit 42 (Palo Alto) has since published its own AI supply-chain threat analysis of the marketplace. The skill submission plan (Section 3) now budgets for security review and provenance expectations.
3. **OpenClaw governance change.** The OpenClaw Foundation formally launched as a 501(c)(3) on July 8, 2026 -- chaired by Dave Morin with Peter Steinberger, with published leadership, paid maintainers, an MIT-license commitment, and "Switzerland of AI" neutrality positioning. Five published major donors: Offline Holdings, University of Michigan (reported largest), OpenAI, Microsoft, and NVIDIA -- the donor page designates no "lead sponsor" -- plus 311 individuals/orgs via GitHub Sponsors; partners include Microsoft, Tencent, Atlassian, Vercel, Cloudflare, GitHub, Blacksmith and Convex -- 30+ orgs total. Scale as of mid-July 2026 (foundation-published): 4.5 million new claws (users/agents) per week, "fastest growing GitHub repository in history," and ~30,000 ClawCon registrations across 34 events in 16 countries in five months; 18+ built-in providers (April-2026 count -- re-check against v2026.7.2 release notes). The built-in provider path (Tier 3) now runs through a foundation where OpenAI is a major donor, employs the project's creator (Steinberger runs Claw Labs inside OpenAI), and supports inference -- a rival inference vendor with structural influence; rivals now also ship their own OpenClaw distributions (NVIDIA NemoClaw, Microsoft Scout, Tencent maintaining security/stability/ClawHub). The foundation is now operational: a first full-time team of ten, Red Hat as a contributing partner on enterprise open source and supply-chain security, and standards councils convening on agent identity, agent profiles, evals, and enterprise deployment. Those councils are a vendor-neutral engagement venue for Gonka that does not run through the conflicted built-in-provider PR path (see Section 4).
4. **MCP went mainstream -- and the spec is about to move.** 97M+ monthly SDK downloads, 9,652 servers in the official MCP Registry as of May 24, 2026 (10,000+ active public servers per Anthropic; third-party registries index 16,000-20,000), first-party support in ChatGPT, Gemini, Copilot, VS Code and Cursor. MCP itself is now neutrally governed -- donated to the Agentic AI Foundation under the Linux Foundation in December 2025 with multi-vendor governance (Anthropic, OpenAI, Block) -- which strengthens the MCP Registry as the hedge against OpenClaw Foundation gatekeeping. The MCP 2026-07-28 release candidate (final spec ships July 28, 2026) is more than the stateless-transport headline: remote servers become stateless/load-balancer-friendly (no sticky sessions or shared session store; routing on an `Mcp-Method` header; cacheable `tools/list`), plus an Extensions framework, a Tasks primitive (a server can answer `tools/call` with a task handle, driven via `tasks/get`/`tasks/update`/`tasks/cancel` -- standardized server-directed async execution), MCP Apps, authorization hardening, and a formal deprecation policy, with Tier-1 SDK support expected within ten weeks. The Tasks primitive gives every MCP-capable agent stack a standardized async pattern, which narrows Gonka's inference-layer-webhook differentiator across the board, not just against OpenAI's background mode. The Gonka MCP server is now a primary distribution channel, not a Tier 2 add-on -- build it against the 2026-07-28 spec, map stateful sessions/memory onto the stateless transport, and target Tasks for async work.
5. **Agent-native payments (x402).** The Linux Foundation declared the x402 Foundation operationally live on July 14, 2026 with 40 member organizations across three tiers -- including Visa, Mastercard, American Express, Stripe, Ripple, Google, AWS, Shopify, Cloudflare and Coinbase. Real volume followed: ~75M transactions moving ~$24M (~$800K/day) in the 30 days ending mid-July 2026. x402 has also shipped at the edge -- AWS added x402 support to CloudFront and AWS WAF (GA, late June 2026) and Cloudflare opened a Monetization Gateway waitlist. BlockRunAI's ClawRouter already occupies the "agent-native payments for OpenClaw" position. x402 is one layer of a three-layer 2026 agentic-payments stack alongside AP2 (authorization mandates; Google donated the Agent Payments Protocol to the FIDO Alliance, so it is now community-led) and OpenAI/Stripe's ACP (agent checkout) -- see the partner framing section's x402 note for the agent-as-customer segment.

**Ecosystem context:** Gonka now markets "$80M+ raised from Coatue and Bitfury Capital" (as of July 2026; the earlier anchors were Bitfury's $12M strategic round, Nov 2025, and $50M commitment, Dec 2025). A supply-side partner ecosystem has formed around the network as of July 2026: gonka.ai names Gcore, Hyperfusion, and 6blocks as select hosts, with Web3.com Ventures, HardYaka, and Bitfury as community partners, and lists CertiK as auditor; the GAIB × Gonka "GAIC" public enrollment window ran June 5 - July 5, 2026 and is now closed -- GAIB reports the prior private phase delivered $600K+ with 200+ H200 GPUs in the first batch (GAIB handles GPU procurement and node ops for H100/H200/B200 hardware, with a 10%-of-mined-GNK insurance pool); Spheron and Gcore now run dedicated Gonka GPU-rental pages; and a broker/gateway retail layer (GonkaBroker, GonkaGate, JoinGonka, OpenGNK, gonka.to) fronts developer access with fixed-USD pricing. Gonka plans Asia expansion (Japan, South Korea) by end of 2026. On the software side, Devshard v3.0.0 (July 9, 2026) enables inference during validation phases -- a capacity gain relevant to partner reliability conversations. The v0.2.14 chain upgrade PR (open for review since July 8, 2026) adds PoC duplicate-artifact protection and deprecates the classic API -- disabling billing on `/v1/chat/completions` -- pushing all paid inference through the devshard/broker path; the OpenAI-compatible integration story in this playbook must be validated against that path before external use. AI tokens were the only profitable crypto sector in Q1 2026 (~$21.7B sector cap), with revenue-generating compute networks decoupling from speculative tokens -- supporting Gonka's fee-revenue thesis in infrastructure-partner conversations (not developer-facing ones).

---

## Four-Tier Integration Roadmap

The four tiers represent progressively deeper integration with the OpenClaw ecosystem. Each tier unlocks more developer reach, reduces adoption friction, and builds the relationship capital needed for the next tier. Tiers are sequential -- each depends on the prior tier being complete and validated.

```
Timeline (months from start)
|-----|----------|----------|----------|----------|----------|----------|
0     1          2          3          4          5          6         12+

[==== Tier 1: Listed Provider ====]
      Start immediately, 2-3 weeks
                 Validate: 10+ devs
                 [======= Tier 2: Community Plugin =======]
                           2-3 weeks engineering + 1 week testing
                                     Validate: 50+ npm installs
                 [---- Community relationship building (ongoing) ----]
                                               [== Tier 3: Built-In Provider ==]
                                               PR prep + review: 2-6 weeks
                                                                 [Tier 4: Preferred]
                                                                  Ongoing relationship
```

### Tier 1 -- Listed Provider (Immediate, v1.3 deliverable)

**Description:** Gonka documented as a custom provider in the OpenClaw ecosystem. Developers can configure Gonka by copying a JSON snippet into their `openclaw.json` file. No changes to OpenClaw's codebase required.

**Prerequisites:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| OpenAI-compatible `/v1/chat/completions` API | DONE (re-verify) | Shipped in v1.2; maps to OpenClaw's `api: "openai-completions"`. Caveat: the v0.2.14 chain upgrade PR (Jul 2026) disables billing on the classic `/v1/chat/completions` path, routing paid inference through devshard/broker -- confirm the public endpoint fronts that path |
| Publicly accessible endpoint | NEEDED | `https://api.gonka.ai/v1` must be live and reachable |
| API documentation site (docs.gonka.ai) | NEEDED | Quickstart guide, API reference, OpenClaw integration guide -- minimum 10 pages |
| Self-service API key signup | NEEDED | Web form with email + GitHub OAuth; no manual approval; free tier activated automatically |
| Published pricing page | NEEDED | Per-token rates for K2.6 tiers (and K3 once weights land), comparison table, cost calculator for OpenClaw agent workloads |

**Deliverables:**

1. **`openclaw.json` configuration template** -- copy-paste ready, published on docs.gonka.ai:
   ```json
   {
     "models": {
       "providers": {
         "gonka": {
           "baseUrl": "https://api.gonka.ai/v1",
           "apiKey": "${GONKA_API_KEY}",
           "api": "openai-completions",
           "models": [
             {
               "id": "kimi-k2.6",
               "name": "Kimi K2.6",
               "contextWindow": 262144,
               "maxTokens": 8192,
               "cost": { "input": 0.50, "output": 1.50 }
             }
           ]
         }
       }
     }
   }
   ```
   Note: Both `baseUrl` and model allowlisting in `agents.defaults.models` are required -- missing either causes silent failure (a known OpenClaw gotcha). The integration guide must document both steps. Cost values shown are illustrative placeholders pending Gonka's published pricing (April-2026 estimates, not verified July-2026 rates); add `kimi-k3` to the catalog once open weights land (~July 27, 2026) and Gonka serves it.

2. **Integration guide on docs.gonka.ai** -- "Add Gonka to OpenClaw in 90 Seconds" covering: signup, API key setup, JSON config, model allowlisting, verification, and session/tiering feature intro.

3. **Community presence** -- Posts in OpenClaw Discord `#models` channel sharing the config template when developers ask about cost-effective providers or agent-native features. Organic responses only, not promotional spam.

**Effort estimate:** 1-2 weeks engineering (documentation site + API key signup flow) + 1 week content creation.

**Timeline:** Can begin immediately upon v1.3 milestone completion. All prerequisites are P0 must-close items from the provider landscape gap analysis.

**Success criteria:**
- At least 10 developers successfully configure Gonka as a custom provider
- Config template appears organically in OpenClaw community discussions
- First-call-within-24h rate exceeds 60% of signups
- docs.gonka.ai integration guide ranks in top 10 for "OpenClaw custom provider" search

**Risk:** Low -- no external approvals needed. All deliverables are within Gonka's control.

---

### Tier 2 -- Community Plugin (Near-term, v1.4 candidate)

**Description:** An npm package (`openclaw-plugin-gonka`) that auto-configures Gonka as a provider and exposes Gonka's agent-native extensions (sessions, memory, tiering) as MCP tools. Reduces developer setup from manual JSON editing to a single `npm install` + API key.

**Prerequisites:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| All Tier 1 items complete | NEEDED | Validated with 10+ active users |
| MCP server implementation | NEEDED | ~500 LOC TypeScript per ARCHITECTURE.md. Note: MCP is now the de facto agent interoperability standard (97M+ monthly SDK downloads, 9,652 servers in the official MCP Registry as of May 2026, first-party support in ChatGPT, Gemini, Copilot, VS Code, Cursor). Build against the 2026-07-28 spec (final ships July 28, 2026): remote servers become stateless/load-balancer-friendly, which affects how Gonka's stateful sessions/memory map to MCP tools, and the new Tasks primitive (`tools/call` returning a task handle driven via `tasks/get`/`tasks/update`/`tasks/cancel`) is the standardized target for Gonka's async work. This is a primary distribution channel, not an afterthought -- prioritize accordingly |
| Gonka-specific MCP tools | NEEDED | Tools for session management, memory API, model tiering |
| OpenClaw plugin API compatibility | NEEDED | Must match OpenClaw's jiti-based plugin loading pattern |
| npm publishing account | NEEDED | Publish to npmjs.com as `openclaw-plugin-gonka` |

**Deliverables:**

1. **npm package** (`openclaw-plugin-gonka`) -- auto-registers Gonka as a provider, configures the current model catalog (K2.6 workhorse; K2.7-Code and K3 as Gonka serves them) with correct context window and cost metadata, exposes MCP tools for:
   - `gonka_session_create` / `gonka_session_resume` -- manage server-side sessions
   - `gonka_memory_store` / `gonka_memory_recall` -- persistent agent memory
   - `gonka_tier_set` -- set model tier (lite/mid/full) for cost optimization
2. **ClawHub skill listing** (SKILL.md) -- teaches OpenClaw agents how to use Gonka-specific features (see Section 3: ClawHub Submission Plan)
3. **Official MCP Registry listing** -- publish the Gonka MCP server to the MCP Registry for discoverability across every major agent host (ChatGPT, Gemini, Copilot, VS Code, Cursor), independent of OpenClaw
4. **Plugin documentation** -- installation guide, configuration options, MCP tool reference, migration guide from manual JSON config
5. **One-liner setup:** `npm install openclaw-plugin-gonka` + set `GONKA_API_KEY` environment variable

**Effort estimate:** 2-3 weeks engineering (MCP server + npm packaging + tests) + 1 week testing with real OpenClaw agents.

**Timeline:** Begin after Tier 1 achieves 10+ active users (validation signal that the market wants Gonka). Target start: 4-6 weeks after Tier 1 launch.

**Success criteria:**
- 50+ npm installs in first month
- Plugin appears in ClawHub marketplace search results
- Setup time reduced from ~5 minutes (manual JSON) to ~90 seconds (npm install + API key)
- At least 5 developers use MCP tools (sessions, memory, or tiering) within first month

**Risk:** Medium -- must match OpenClaw's plugin API, which evolves with new releases. Plugin may require updates when OpenClaw changes its plugin loading mechanism. Pin to specific OpenClaw versions and test against nightly builds.

---

### Tier 3 -- Built-In Provider (Medium-term goal)

**Description:** Gonka added to OpenClaw's built-in providers (18+ as of v2026.7.1 -- OpenAI, Anthropic, Gemini, Azure, Bedrock, Groq, Together, Fireworks, OpenRouter and others; onboarding defaults to openrouter/auto; re-verify the count against v2026.7.2, the current release as of July 2026, before external use). Developers configure Gonka by setting a single `GONKA_API_KEY` environment variable -- no `baseUrl`, no model config, no JSON editing. Gonka appears in `openclaw models list` output alongside OpenAI, Anthropic, and OpenRouter.

**Prerequisites:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| All Tier 2 items complete | NEEDED | Community plugin validated with 50+ installs |
| Reliability track record | NEEDED | Public uptime stats page showing 99%+ availability over 30+ days |
| Community adoption signals | NEEDED | npm install count, GitHub stars, Discord mentions, active developer count |
| OpenClaw maintainer relationship | NEEDED | Established through community engagement (see Section 4: PR Strategy) |
| Clean PR contribution history | NEEDED | 3-5 merged non-Gonka PRs to openclaw/openclaw (bug fixes, docs, tests) |
| Comprehensive test suite | NEEDED | Provider tests matching OpenClaw's jest-based test patterns |
| Rate limit documentation | NEEDED | Published RPM/TPM limits per tier |

**Deliverables:**

1. **PR to openclaw/openclaw** -- adds Gonka provider module matching existing provider implementation patterns (TypeScript, same file structure, same config schema as OpenRouter/Together AI/Groq modules)
2. **Provider test suite** -- comprehensive jest tests matching OpenClaw's assertion style and test patterns
3. **Documentation page** -- added to OpenClaw docs alongside other providers, covering: setup, available models, capability flags (`reasoning`, `toolUse`, `vision`), pricing, and Gonka-specific extensions
4. **Model catalog** -- accurate pricing, context windows, and capability metadata for the current Kimi lineup (K2.6, K2.7-Code, K3 as served)
5. **Extension headers** -- `X-Gonka-Session-ID` and `X-Gonka-Tier` handled as optional provider extensions that enhance but do not break standard OpenClaw flow

**Effort estimate:** 1-2 weeks engineering (PR preparation, tests, docs) + unknown review time (depends on maintainer responsiveness and feedback cycles).

**Timeline:** Target 3-6 months after Tier 2; depends on community traction, maintainer relationship quality, and OpenClaw team's priorities for adding new providers.

**Success criteria:**
- PR merged into openclaw/openclaw main branch
- Gonka appears in `openclaw models list` output
- Developers can configure Gonka with only `GONKA_API_KEY` environment variable
- Gonka provider page live in official OpenClaw documentation

**Risk:** High -- requires OpenClaw maintainer approval. This is not guaranteed. Per the CONTEXT.md decision: "community approach, not cold PR -- build relationship first." The community relationship plan (Section 4) is a prerequisite, not an optional nice-to-have. A cold PR from an unknown contributor will likely be ignored or rejected. Added risk (July 2026): the OpenClaw Foundation formally launched July 8, 2026; OpenAI is one of five published major donors and employs the project's creator (Steinberger runs the "Claw Labs" team inside OpenAI) -- a structurally conflicted gatekeeper for a rival inference network, even under the foundation's published "Switzerland of AI" neutrality positioning. Governance and leadership are now published; review them before investing PR effort, and treat the MCP Registry (Tier 2) -- itself neutrally governed under the Linux Foundation's Agentic AI Foundation -- as the hedge if built-in status stalls.

---

### Tier 4 -- Preferred Partner (Long-term aspiration)

**Description:** Co-development relationship with the OpenClaw team. Joint feature development, Gonka-specific optimizations in OpenClaw, marketing collaboration, and representation in OpenClaw's official communications.

**Prerequisites:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| All Tier 3 items complete | NEEDED | Built-in provider status achieved and stable |
| Significant OpenClaw user base | NEEDED | 1,000+ API-active developers using Gonka via OpenClaw |
| Sustained community contribution | NEEDED | Multiple merged PRs, active community presence, skill contributions |
| Demonstrated ecosystem value | NEEDED | Evidence that Gonka drives OpenClaw adoption or improves the ecosystem |
| Joint feature interest | NEEDED | OpenClaw team expresses interest in collaborating on agent-native features |

**Deliverables:**

1. **Joint roadmap** -- co-developed features that benefit both OpenClaw and Gonka (e.g., native session support in OpenClaw's provider abstraction, optimized agent templates using Gonka's tiering)
2. **Co-branded developer content** -- joint blog posts, conference talks, and tutorials showcasing Gonka + OpenClaw agent workflows
3. **Gonka-optimized agent templates** -- default agent configurations in OpenClaw that leverage Gonka's session persistence and auto-tiering for cost-optimized workflows
4. **Feature collaboration** -- Gonka engineers contribute to OpenClaw's agent infrastructure, OpenClaw team helps optimize Gonka's provider integration

**Effort estimate:** Ongoing relationship investment -- not a fixed engineering sprint but a continuous presence in the OpenClaw ecosystem through code contributions, community engagement, and technical leadership.

**Timeline:** 6-12 months after built-in provider status. This is a relationship outcome, not an engineering deliverable -- it cannot be forced or scheduled.

**Success criteria:**
- Joint announcement or co-authored feature (e.g., OpenClaw blog post featuring Gonka)
- Gonka mentioned in official OpenClaw communications (release notes, docs, social media)
- OpenClaw team proactively consults Gonka on agent-related provider features
- Gonka-specific agent templates included in OpenClaw defaults or examples

**Risk:** Very high -- depends entirely on relationship quality, Gonka's demonstrated user traction, and OpenClaw team's strategic priorities. This tier is aspirational and should not be planned as a guaranteed outcome. Focus engineering energy on Tiers 1-3; Tier 4 emerges from sustained excellence at Tier 3.

---

## Technical Partnership Requirements Checklist

A comprehensive checklist of everything Gonka must deliver to unlock each partnership tier. Items are grouped by category, with current status, blocking tier, effort estimate, and responsible team.

### API & Infrastructure

| # | Requirement | Status | Blocks Tier | Effort | Owner |
|---|-------------|--------|-------------|--------|-------|
| 1 | OpenAI-compatible `/v1/chat/completions` API | DONE (re-verify vs v0.2.14 classic-API deprecation) | 1 | -- | Engineering |
| 2 | Tool calling with `--enable-auto-tool-choice` configured | DONE | 1 | -- | Engineering |
| 3 | SSE streaming via OpenAI-compatible endpoint | DONE | 1 | -- | Engineering |
| 4 | Rate limiting with 429 responses (triggers OpenClaw key rotation) | DONE | 1 | -- | Engineering |
| 5 | Usage metering per API key | DONE | 1 | -- | Engineering |
| 6 | Publicly accessible production endpoint | NEEDED | 1 | 1-2 weeks | Engineering |
| 7 | API documentation site (docs.gonka.ai) | NEEDED | 1 | 2-3 weeks | Engineering |
| 8 | Self-service API key signup (email + GitHub OAuth) | NEEDED | 1 | 1-2 weeks | Engineering |
| 9 | Public pricing page with cost calculator | NEEDED | 1 | 1 week | Engineering + Leadership |
| 10 | Rate limit documentation (RPM/TPM per tier) | NEEDED | 2 | 2 days | Engineering |
| 11 | Public uptime/status page | NEEDED | 3 | 1 week | Engineering |
| 12 | Persistent sessions (Redis migration from in-memory) | NEEDED | 3 | 1-2 weeks | Engineering |

### SDK & Tooling

| # | Requirement | Status | Blocks Tier | Effort | Owner |
|---|-------------|--------|-------------|--------|-------|
| 13 | `openclaw.json` configuration template | NEEDED | 1 | 1 day | Engineering |
| 14 | OpenClaw integration guide ("Add Gonka in 90 Seconds") | NEEDED | 1 | 2-3 days | Content |
| 15 | npm provider plugin (`openclaw-plugin-gonka`) | NEEDED | 2 | 2-3 weeks | Engineering |
| 16 | MCP server for agent extensions (sessions, memory, tiering) | NEEDED | 2 | 2-3 weeks | Engineering |
| 17 | Quickstart repository (GitHub template) | NEEDED | 2 | 1 week | Engineering |
| 18 | Gonka provider module for openclaw/openclaw PR | NEEDED | 3 | 1-2 weeks | Engineering |

### Community & Content

| # | Requirement | Status | Blocks Tier | Effort | Owner |
|---|-------------|--------|-------------|--------|-------|
| 19 | OpenClaw Discord presence (#help, #models, #users-helping-users) | NEEDED | 1 | Ongoing | Community |
| 20 | Integration guide on dev.to or Medium | NEEDED | 2 | 3-5 days | Content |
| 21 | Video tutorial ("OpenClaw + Gonka in 5 Minutes") | NEEDED | 2 | 1 week | Content |
| 22 | ClawHub skill submission (SKILL.md) | NEEDED | 2 | 1 week + 1-3 weeks security screening | Engineering + Content |
| 23 | Non-Gonka PR contributions to openclaw/openclaw | NEEDED | 3 | 2-4 weeks (3-5 merged PRs) | Engineering |
| 24 | GitHub Discussion RFC for built-in provider | NEEDED | 3 | 2 days | Engineering + Community |

### Reliability & Trust

| # | Requirement | Status | Blocks Tier | Effort | Owner |
|---|-------------|--------|-------------|--------|-------|
| 25 | Uptime monitoring and public status page | NEEDED | 3 | 1 week | Engineering |
| 26 | Published benchmark results (latency p50/p95, throughput) | NEEDED | 3 | 1 week | Engineering |
| 27 | SLA terms document | NEEDED | 4 | 1 week | Leadership |
| 28 | Security audit or security practices statement | NEEDED | 4 | 2-4 weeks | Engineering + Leadership |

### Business

| # | Requirement | Status | Blocks Tier | Effort | Owner |
|---|-------------|--------|-------------|--------|-------|
| 29 | Public pricing page with per-token rates | NEEDED | 1 | 1 week | Leadership |
| 30 | Terms of service | NEEDED | 1 | 1 week | Leadership |
| 31 | Privacy policy | NEEDED | 1 | 1 week | Leadership |
| 32 | Support channels (GitHub issues + Discord) | NEEDED | 1 | 1 day | Community |
| 33 | Cost comparison calculator (Gonka vs OpenRouter vs Together AI) | NEEDED | 2 | 3-5 days | Engineering |

**Summary:** 5 items DONE, 28 items NEEDED. The 5 completed items are all API-level capabilities shipped in v1.2. The 28 NEEDED items span documentation, tooling, community presence, reliability infrastructure, and business requirements.

### Partner Conversation Framing

When engaging with OpenClaw maintainers, community members, or potential partners, lead with developer outcomes, not infrastructure:

**Lead with:** "Gonka cuts agent inference costs by up to 73% because server-side session persistence eliminates the heartbeat context re-send that accounts for 44-85% of agent token consumption" (gonka_message_house.md: Core Positioning Statement).

**Support with:** "Drop-in OpenAI-compatible API -- 90-second setup, three fields in openclaw.json, no SDK changes" (gonka_message_house.md: VP3).

**Never lead with:** Decentralization, GNK tokens, mining rewards, DePIN, Web3, staking, epochs, validators, or any term on the 16-item never-say list (gonka_message_house.md: Section 6.1).

**Exception -- the agent-as-customer segment (x402, July 2026 update):** The "API keys only, never crypto" rule holds for human Web2 developer personas, but agent-native payment rails went mainstream between April and July 2026. The x402 Foundation went operationally live under the Linux Foundation on July 14, 2026 with 40 member organizations across three tiers -- the traditional-payments entrants (Visa, Mastercard, American Express, Stripe, Ripple) alongside Google, AWS, Shopify, Cloudflare and Coinbase. Volume is no longer a caveat: ~75M transactions moving ~$24M (~$800K/day, ~29 tx/sec) between ~94,000 buyers and ~22,000 sellers over the 30 days ending mid-July 2026, mostly sub-dollar payments settling predominantly in USDC. Distribution is commoditizing too: AWS shipped x402 support in CloudFront and AWS WAF (GA), and Cloudflare's Monetization Gateway waitlist lets any customer charge for APIs or MCP tools via x402 -- meaning an x402-gated Gonka inference endpoint becomes deployable behind commodity edge infra. BlockRunAI's ClawRouter already occupies the "agent-native payments for OpenClaw" position, authenticating agents with wallet signatures and paying for inference via USDC micropayments over x402. Situate the story correctly: x402 is the machine-to-machine execution/micropayment layer of a three-layer 2026 stack, alongside AP2 (authorization via signed Intent/Cart/Payment mandates as W3C Verifiable Credentials; 60+ partners; in production with Gemini Spark since May 2026; Google has since donated the Agent Payments Protocol to the FIDO Alliance, making it community-led rather than Google-stewarded) and OpenAI/Stripe's ACP (agent checkout, live in ChatGPT). One caveat to the clean layer separation: AP2 v0.2 introduces "Human Not Present" payments -- agents executing payments autonomously -- which moves AP2 into x402's machine-to-machine territory, so present "x402=execution, AP2=authorization" as a simplification, not a hard boundary. For agent-procured inference x402 is the right layer, but enterprise buyers will ask how Gonka relates to AP2 and ACP -- partner-facing material should answer that. Gonka -- already a crypto network -- has a natural x402 story for autonomous-agent buyers and should scope an x402 payment endpoint as a distinct workstream with its own (crypto-permissive) messaging, kept strictly separate from the developer-facing message house.

**For partner-facing technical discussions:** Frame Gonka as "the agent-native inference provider" -- a description that is accurate, memorable, and crypto-free. The decentralized infrastructure is the "how," not the "what." Developers and partners care about what Gonka does for their agents, not how the network achieves consensus.

---

## ClawHub Submission Plan

ClawHub is OpenClaw's skills marketplace -- markdown-based agent capability definitions (SKILL.md files) injected into system prompts based on context. Publishing Gonka content on ClawHub puts Gonka in front of developers who are actively configuring their agents.

**Security context (updated July 2026) -- this changes the plan.** The sourced ClawHavoc sequence: Koi Security's Feb 1, 2026 audit found 341 malicious skills out of 2,857 scanned (335 in the ClawHavoc/AMOS campaign, malware targeting crypto wallets); OpenClaw responded by partnering with VirusTotal on Feb 7, 2026, removing ~2,419 suspicious skills and adding automatic scanning of every published skill; as ClawHub grew past 10,700 skills, Koi's continued scanning more than doubled confirmed-malicious findings to 824 (~Feb 16); by Feb 19, Antiy CERT had uncovered at least 1,184 malicious skill packages -- one analysis puts flagged-malicious-or-suspicious at ~7.6% of the registry -- and Unit 42 (Palo Alto) has since published its own AI supply-chain threat analysis of the marketplace. This came alongside a one-click RCE (CVE-2026-25253, patched v2026.1.29) and 30,000+ internet-exposed OpenClaw instances. Consequences for Gonka:

- ClawHub now runs hardened screening (the VirusTotal automatic scanning above); budget for a security review stage, provenance/signing expectations, and slower approval than the original 7-day plan assumed
- The community is acutely suspicious of skills that touch API keys or payments -- and the ClawHavoc malware stole cryptocurrency, so a crypto-adjacent provider is a credibility landmine. Lead with security posture: publish the skill from a verified Gonka org account, sign releases, keep the skill's scope minimal (headers and config only, no key handling beyond the standard env-var pattern), and state this explicitly in the listing
- Developer distrust of third-party skills means organic install counts will be slower than pre-ClawHavoc benchmarks; weight the MCP Registry listing (Tier 2) as the complementary distribution channel

### What to Submit

**1. Gonka Provider Skill (Primary Submission)**

A SKILL.md file that teaches OpenClaw agents how to use Gonka-specific features. When an agent loads this skill, it learns about Gonka's session persistence, model tiering, and memory API -- enabling it to use these features automatically without developer intervention.

Draft SKILL.md outline:

```markdown
---
name: gonka-agent-extensions
description: Use Gonka's agent-native inference features -- server-side sessions,
  automatic model tiering, and persistent memory
version: 1.0.0
author: Gonka Network
tags: [inference, sessions, memory, tiering, cost-optimization]
---

# Gonka Agent Extensions

You are connected to a Gonka inference provider. Gonka offers agent-native
features that reduce your inference costs and improve your capabilities.

## Session Persistence

When making requests to Gonka, include the `X-Gonka-Session-ID` header to
maintain conversation state server-side. This eliminates the need to resend
full context on every request, reducing token consumption by up to 80%.

### How to Use Sessions

- On first request: Set `X-Gonka-Session-ID: <unique-id>` header
- On subsequent requests: Use the same session ID to resume context
- Sessions persist across requests -- your conversation history is maintained
  server-side without retransmitting tokens

## Model Tiering

Use the `X-Gonka-Tier` header to select cost-performance tiers per request:

- `X-Gonka-Tier: lite` -- fast classification, simple tasks (lowest cost)
- `X-Gonka-Tier: mid` -- balanced reasoning tasks
- `X-Gonka-Tier: full` -- complex reasoning, code generation (highest quality)

### When to Use Each Tier

- Classification and routing decisions: use `lite`
- Summarization and standard responses: use `mid`
- Code generation, complex reasoning, multi-step planning: use `full`

## Memory API

Store and retrieve persistent key-value data via the Gonka Memory API:

- Store: `POST /v1/memory` with key-value pairs
- Recall: `GET /v1/memory?query=<search-term>` (TF-IDF keyword search)
- Memory persists across sessions and agent restarts

## Example Usage Pattern

For a cost-optimized agent workflow:
1. Set session ID on first request (eliminate heartbeat costs)
2. Use `lite` tier for input classification
3. Use `full` tier for complex reasoning steps
4. Store important results in memory for future recall
```

**2. Gonka Configuration Template Skill**

A companion skill providing the exact `openclaw.json` configuration for adding Gonka as a custom provider:

```json
{
  "models": {
    "providers": {
      "gonka": {
        "baseUrl": "https://api.gonka.ai/v1",
        "apiKey": "${GONKA_API_KEY}",
        "api": "openai-completions",
        "models": [
          {
            "id": "kimi-k2.6",
            "name": "Kimi K2.6",
            "contextWindow": 262144,
            "maxTokens": 8192,
            "cost": { "input": 0.50, "output": 1.50 }
          }
        ]
      }
    }
  }
}
```

**3. Gonka Quickstart Skill**

A step-by-step skill that walks an agent through setting up Gonka as a provider. Covers: where to get an API key, how to configure `openclaw.json`, how to verify the connection, and how to enable agent-native features.

### Submission Process

| Step | Action | Timeline |
|------|--------|----------|
| 1 | Create GitHub repository `gonka-openclaw-skill` following ClawHub naming conventions | Day 1 |
| 2 | Write SKILL.md following OpenClaw's skill format (markdown with YAML frontmatter, structured sections for agent consumption) | Day 2-3 |
| 3 | Test skill locally with an OpenClaw agent to verify system prompt injection works correctly -- agent should demonstrate awareness of Gonka features | Day 4-5 |
| 4 | Submit to ClawHub via the post-ClawHavoc contribution process from a verified Gonka org account, with signed releases and provenance metadata | Day 6-7 |
| 5 | Clear ClawHub security screening -- respond promptly to reviewer questions; expect extra scrutiny for a crypto-adjacent provider | Week 2-4 (registry-dependent) |
| 6 | Promote in OpenClaw Discord `#skills` channel and GitHub Discussions -- brief post explaining what the skill does, how it helps agents optimize costs, and the security posture (signed, minimal scope, no key handling) | After approval |

### Timeline

2-5 weeks from Tier 1 completion: ~1 week authoring and testing, plus post-ClawHavoc security screening (variable, assume 1-3 weeks). The SKILL.md can be drafted during Tier 1 work and submitted as soon as the public endpoint and API key signup are live.

### Success Metrics

- Skill appears in ClawHub search results for "inference," "cost optimization," "sessions," "agent memory"
- 25+ installs in first month after approval (pre-ClawHavoc benchmark; expect slower organic uptake given current skill distrust)
- Skill referenced in OpenClaw community discussions (Discord, GitHub Discussions)
- Agents using the skill demonstrate correct usage of session headers and tiering

### Maintenance Plan

- Update skill when Gonka adds new features (new models, new MCP tools, new API capabilities)
- Update when OpenClaw changes skill format or injection mechanism
- Monitor ClawHub for user issues or questions about the skill
- Version the skill alongside Gonka API versions

---

## Built-In Provider PR Strategy

Getting Gonka merged as a built-in OpenClaw provider is the single highest-impact GTM action identified in the provider landscape analysis (gonka_provider_landscape_map.md: Phase 19 recommendations). Built-in status eliminates the JSON configuration friction that is the #1 barrier to developer adoption -- developers would set a single environment variable instead of editing a config file.

**Core principle: Community approach, not cold PR -- build relationship first.** A PR from an unknown contributor proposing a new provider will likely be ignored, deprioritized, or rejected. OpenClaw's maintainers receive thousands of PRs. Earning credibility through sustained community contribution is the prerequisite.

**Governance caveat (July 2026):** provider decisions now route through the OpenClaw Foundation (formally launched July 8, 2026 as a 501(c)(3), chaired by Dave Morin with Peter Steinberger). The five published major donors are Offline Holdings, University of Michigan (reported largest), OpenAI, Microsoft, and NVIDIA -- no designated "lead sponsor" -- with 30+ partner orgs including Microsoft, Tencent, Atlassian, Vercel, Cloudflare, GitHub, Blacksmith and Convex. OpenAI's position -- major donor, employer of the project's creator (Steinberger runs Claw Labs inside OpenAI), inference supporter, and shipper of Codex Security hardening -- makes the foundation a potentially conflicted gatekeeper for a rival inference provider; NVIDIA (NemoClaw) and Microsoft (Scout) now ship their own OpenClaw distributions, so several major donors are themselves competing distributors. This raises the value of the Tier 2 assets (community plugin + MCP Registry listing) as the fallback distribution path. Counterweight: the foundation's new standards councils (agent identity, agent profiles, evals, enterprise deployment; first full-time team of ten, Red Hat contributing on enterprise open source and supply-chain security) are a vendor-neutral engagement channel that bypasses the provider-PR gate -- the agent-identity council in particular intersects Gonka's wallet-authenticated x402 payment story.

### Community Relationship Building (Pre-PR Phase)

**Month 1-2: Establish Presence**

- Join the official OpenClaw Discord ("Friends of the Crustacean," discord.com/invite/clawd -- ~175K members as of July 2026, having crossed 100K within six weeks of its January 2026 founding) and become a helpful presence in `#help`, `#models`, and `#users-helping-users` channels; the channel directory lives at docs.openclaw.ai
- Answer provider configuration questions -- especially around custom provider setup, model configuration, and common gotchas (like the missing model allowlisting silent failure)
- Share Gonka config snippets when organically relevant: when developers ask about cost-effective providers, agent-native features, or session management. Not promotional -- only when the question matches Gonka's strengths
- Follow OpenClaw GitHub repositories: watch issues, read PR discussions, understand the project's code review culture
- Goal: Be recognized as a helpful community member, not a vendor

**Month 2-3: Contribute Non-Gonka PRs**

- Contribute to openclaw/openclaw with bug fixes, documentation improvements, test coverage, or developer experience enhancements
- Target 3-5 merged PRs before proposing the Gonka provider. Examples:
  - Fix a documentation typo or clarify confusing provider setup instructions
  - Add test coverage for an edge case in the provider loading mechanism
  - Improve error messages for common configuration mistakes
  - Write a "troubleshooting custom providers" guide for the docs
- Each PR builds contributor credibility and demonstrates familiarity with the codebase
- Goal: Establish a track record as a quality contributor

**Month 3-4: Engage on Provider Architecture**

- Participate in GitHub Discussions about provider architecture, agent infrastructure, and the future of built-in provider support
- Understand maintainer priorities: What are their pain points? What providers are they considering adding? What criteria matter most?
- Share insights from the Gonka community plugin experience -- what developers want, what patterns work, what gaps exist
- Seek a seat or observer role in the OpenClaw Foundation's standards councils (agent identity, agent profiles, evals, enterprise deployment) -- a vendor-neutral venue independent of the provider-PR gate; agent identity is the natural fit given Gonka's wallet-authenticated x402 work
- Goal: Become a trusted voice in provider-related technical discussions

**Throughout: Track Community Adoption Signals**

- Users mentioning Gonka in OpenClaw Discord
- Gonka config snippets shared in community channels
- GitHub issues filed about Gonka integration
- npm install counts for the community plugin
- Third-party blog posts or tutorials mentioning Gonka + OpenClaw
- These metrics will support the eventual PR proposal

### PR Preparation (Technical)

**Study existing implementations:**
- Examine how OpenRouter, Together AI, and Groq providers are structured in the openclaw/openclaw source
- Note: file structure, TypeScript patterns, config schema, test patterns, documentation format
- Ensure the Gonka module follows the same conventions exactly -- do not introduce novel patterns

**Implement the Gonka provider module:**
- TypeScript module matching OpenClaw's provider implementation pattern
- Config schema: `GONKA_API_KEY` environment variable, automatic model catalog, capability flags
- Model catalog with accurate data:
  - `kimi-k2.6`: contextWindow 262144, maxTokens 8192, pricing (input/output per 1M tokens), capability flags (`reasoning: true`, `toolUse: true`, `vision: true`)
  - `kimi-k2.7-code` and `kimi-k3` as Gonka serves them; include quantization tiers if exposed as separate model IDs
- Handle Gonka-specific headers (`X-Gonka-Session-ID`, `X-Gonka-Tier`) as optional provider extensions that enhance but do not break standard OpenClaw flow
- Ensure standard chat completions, tool calling, and streaming work without any Gonka-specific headers

**Write comprehensive tests:**
- Jest tests matching OpenClaw's test patterns (same assertion style, same file naming)
- Test: provider initialization, model listing, chat completion, streaming, tool calling, error handling
- Test: Gonka-specific headers are passed through when set, omitted gracefully when not set

**Write documentation:**
- Documentation page matching existing provider docs format
- Setup instructions: "Set `GONKA_API_KEY` environment variable, Gonka models are available immediately"
- Feature highlights: session persistence, model tiering, memory API (as optional advanced features)
- Pricing and model capabilities table

### PR Submission Strategy

**Step 1: Open a GitHub Discussion BEFORE the PR**

Title: "RFC: Add Gonka as Built-In Provider"

Content:
- Why Gonka is different from existing providers (not just another OpenAI wrapper -- agent-native extensions that reduce inference costs by up to 73% through server-side sessions)
- Community adoption metrics: npm plugin installs, active developer count, Discord mentions, community feedback
- Link to existing community plugin and ClawHub skill
- Technical readiness: OpenAI-compatible API, comprehensive tests, stable uptime stats
- Ask for feedback on the proposal before submitting code

**Step 2: Wait for maintainer feedback**

- Do not submit the PR until at least one maintainer responds positively to the Discussion
- Address any concerns or questions raised
- Incorporate feedback into the implementation

**Step 3: Submit PR with complete context**

PR description template:
- **What:** Add Gonka as a built-in provider
- **Why:** Gonka offers agent-native extensions (sessions, memory, tiering) that no other built-in provider has; [X] developers already use Gonka via community plugin; built-in status reduces setup from npm install + JSON config to a single env var
- **How:** Provider module matching existing patterns (link to code), tests (link), docs (link)
- **Adoption data:** npm downloads, API-active developer count, community plugin installs, Discord mentions
- **Maintenance commitment:** Gonka team commits to maintaining the provider module, updating model catalog, and responding to issues

**Step 4: Iterate on review feedback**

- Respond to code review within 24 hours
- Make requested changes promptly
- Do not argue with stylistic preferences -- match the project's conventions

### Handling Rejection

| Rejection Reason | Response | Timeline |
|-----------------|----------|----------|
| Insufficient adoption | Set concrete metric targets (e.g., 500+ npm installs, 100+ API-active developers); revisit in 3 months with updated data | 3 months |
| Technical concerns | Address every piece of feedback; resubmit with improvements; offer to pair with a maintainer on the implementation | 2-4 weeks |
| Too many providers | Propose "community-maintained" provider with lighter integration -- provider config in a contrib/ directory with community ownership | 1-2 weeks |
| No response | Follow up once after 2 weeks; engage in other Discussions to stay visible; try again with updated metrics in 2 months | 2 months |
| Philosophical disagreement | Accept and continue with community plugin approach; community plugin gives 90% of built-in benefits with no approval needed | Ongoing |

### Realistic Timeline

| Phase | Duration | Cumulative |
|-------|----------|------------|
| Community presence and initial contributions | 1-2 months | 1-2 months |
| Non-Gonka PR contributions (3-5 merged) | 1-2 months | 2-4 months |
| RFC Discussion and feedback cycle | 2-4 weeks | 3-5 months |
| PR preparation | 1-2 weeks | 3-5 months |
| PR review and iteration | 2-4 weeks | 4-6 months |
| **Total** | **3-6 months** from starting community engagement |

**Important caveat:** This is NOT a guaranteed outcome. It depends on Gonka's community traction, OpenClaw team's priorities, and the quality of the relationship built during the pre-PR phase. The community plugin (Tier 2) provides 90% of the developer experience benefit and is fully within Gonka's control. Built-in status (Tier 3) is a goal worth pursuing, but the strategy should not depend on it.

---

## Execution Priority Matrix

All partnership and ecosystem activities ordered by priority, with dependencies and target dates.

| Priority | Activity | Tier | Effort | Dependencies | Target Date |
|----------|----------|------|--------|--------------|-------------|
| P0 | Deploy public endpoint (`api.gonka.ai/v1`) | 1 | 1-2 weeks | v1.3 completion | Month 1 |
| P0 | Launch API documentation site (docs.gonka.ai) | 1 | 2-3 weeks | None | Month 1 |
| P0 | Implement self-service API key signup | 1 | 1-2 weeks | Docs site | Month 1 |
| P0 | Publish pricing page with cost calculator | 1 | 1 week | Pricing decision (Leadership) | Month 1 |
| P0 | Publish `openclaw.json` config template | 1 | 1 day | Public endpoint | Month 1 |
| P0 | Join OpenClaw Discord; begin community presence | 1 | Ongoing | None | Immediately |
| P1 | Write and publish OpenClaw integration guide | 1 | 2-3 days | Docs site, config template | Month 1-2 |
| P1 | Submit Gonka Provider Skill to ClawHub | 2 | 2-5 weeks (incl. security screening) | Public endpoint, API key signup | Month 2-3 |
| P1 | Build npm plugin (`openclaw-plugin-gonka`) | 2 | 2-3 weeks | Tier 1 validation (10+ users) | Month 2-3 |
| P1 | Build MCP server for agent extensions | 2 | 2-3 weeks | npm plugin | Month 2-3 |
| P1 | Create quickstart GitHub template repo | 2 | 1 week | Config template, integration guide | Month 2-3 |
| P1 | Publish integration guide on dev.to / Medium | 2 | 3-5 days | Working integration | Month 2-3 |
| P1 | Migrate sessions from in-memory to Redis | 3 | 1-2 weeks | None (v1.2 tech debt) | Month 2-3 |
| P2 | Record video tutorial ("OpenClaw + Gonka in 5 min") | 2 | 1 week | Working integration | Month 3-4 |
| P2 | Contribute 3-5 non-Gonka PRs to openclaw/openclaw | 3 | 2-4 weeks | Community presence | Month 2-4 |
| P2 | Launch public uptime/status page | 3 | 1 week | Public endpoint | Month 3-4 |
| P2 | Publish benchmark results (latency, throughput) | 3 | 1 week | Production traffic data | Month 3-4 |
| P2 | Build cost comparison calculator tool | 2 | 3-5 days | Published pricing | Month 3-4 |
| P3 | Open RFC Discussion for built-in provider | 3 | 2 days | 3-5 merged PRs, adoption metrics | Month 4-5 |
| P3 | Prepare and submit built-in provider PR | 3 | 1-2 weeks | Positive RFC feedback | Month 5-6 |
| P3 | Publish SLA terms document | 4 | 1 week | Uptime track record | Month 6+ |
| P3 | Pursue co-development opportunities | 4 | Ongoing | Built-in provider status | Month 9-12+ |

---

## Next Steps

The three most important immediate actions to start executing this playbook:

1. **Close P0 infrastructure gaps (Month 1).** Deploy the public API endpoint, launch docs.gonka.ai with the OpenClaw integration guide, implement self-service API key signup, and publish the pricing page. These are table-stakes prerequisites -- nothing else in this playbook can proceed without them. See the provider landscape gap analysis (gonka_provider_landscape_map.md: Must Close Before GTM Push) for the "closed" definition of each gap.

2. **Establish OpenClaw Discord presence (Immediately).** Join the OpenClaw Discord and begin participating in `#help`, `#models`, and `#users-helping-users` channels. This is zero-cost, zero-dependency, and can start today. The goal is to become a recognized, helpful community member before any Gonka promotion begins. Every month of community presence before the built-in provider PR increases the probability of acceptance.

3. **Publish the `openclaw.json` config template (Week 1 of Tier 1).** The configuration template is the single most reusable asset in this playbook. It appears in the integration guide, the ClawHub skill, the community plugin, the quickstart repo, and every piece of content about Gonka + OpenClaw. Create it once, publish it on docs.gonka.ai, and reference it everywhere.

---

*Document: gonka_partnership_playbook.md | Version 1.3 | 2026-07-18*
*Companion documents: gonka_message_house.md (positioning), gonka_channel_strategy.md (channels), gonka_competitive_feature_matrix.md (competitive analysis), gonka_provider_landscape_map.md (gap analysis)*

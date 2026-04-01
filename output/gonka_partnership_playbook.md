# Gonka Partnership & Ecosystem Strategy Playbook

**Version:** 1.0
**Date:** 2026-04-01
**Classification:** Internal -- strategic playbook for Gonka's OpenClaw ecosystem integration
**Status:** Strategy Document
**Dependencies:** Phase 15 competitive analysis (gonka_competitive_feature_matrix.md), Phase 17 messaging (gonka_message_house.md), Phase 18 channel strategy (gonka_channel_strategy.md), provider landscape gap analysis (gonka_provider_landscape_map.md)
**Requirement:** GTM-02

---

## Executive Summary

Gonka's path to developer adoption runs through the OpenClaw ecosystem. This playbook defines a four-tier integration roadmap -- from custom provider listing to built-in provider status and co-development partnership -- with specific prerequisites, effort estimates, timelines, and success criteria at each tier. It also provides a ClawHub skill submission plan, a community-first strategy for getting Gonka merged as a built-in OpenClaw provider, and a comprehensive technical requirements checklist tracking what Gonka must deliver before each tier can be unlocked.

All partner-facing language in this playbook follows Phase 17 positioning: lead with heartbeat cost reduction (73% savings via server-side session persistence), not decentralization or network economics. Partner conversations should reference the message house (gonka_message_house.md) for approved vocabulary and positioning guidance.

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
| OpenAI-compatible `/v1/chat/completions` API | DONE | Shipped in v1.2; maps to OpenClaw's `api: "openai-completions"` |
| Publicly accessible endpoint | NEEDED | `https://api.gonka.ai/v1` must be live and reachable |
| API documentation site (docs.gonka.ai) | NEEDED | Quickstart guide, API reference, OpenClaw integration guide -- minimum 10 pages |
| Self-service API key signup | NEEDED | Web form with email + GitHub OAuth; no manual approval; free tier activated automatically |
| Published pricing page | NEEDED | Per-token rates for K2.5 tiers, comparison table, cost calculator for OpenClaw agent workloads |

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
               "id": "kimi-k2.5",
               "name": "Kimi K2.5",
               "contextWindow": 131072,
               "maxTokens": 8192,
               "cost": { "input": 0.50, "output": 1.50 }
             }
           ]
         }
       }
     }
   }
   ```
   Note: Both `baseUrl` and model allowlisting in `agents.defaults.models` are required -- missing either causes silent failure (a known OpenClaw gotcha). The integration guide must document both steps.

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
| MCP server implementation | NEEDED | ~500 LOC TypeScript per ARCHITECTURE.md |
| Gonka-specific MCP tools | NEEDED | Tools for session management, memory API, model tiering |
| OpenClaw plugin API compatibility | NEEDED | Must match OpenClaw's jiti-based plugin loading pattern |
| npm publishing account | NEEDED | Publish to npmjs.com as `openclaw-plugin-gonka` |

**Deliverables:**

1. **npm package** (`openclaw-plugin-gonka`) -- auto-registers Gonka as a provider, configures K2.5 model with correct context window and cost metadata, exposes MCP tools for:
   - `gonka_session_create` / `gonka_session_resume` -- manage server-side sessions
   - `gonka_memory_store` / `gonka_memory_recall` -- persistent agent memory
   - `gonka_tier_set` -- set model tier (lite/mid/full) for cost optimization
2. **ClawHub skill listing** (SKILL.md) -- teaches OpenClaw agents how to use Gonka-specific features (see Section 3: ClawHub Submission Plan)
3. **Plugin documentation** -- installation guide, configuration options, MCP tool reference, migration guide from manual JSON config
4. **One-liner setup:** `npm install openclaw-plugin-gonka` + set `GONKA_API_KEY` environment variable

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

**Description:** Gonka added to OpenClaw's ~20 built-in providers. Developers configure Gonka by setting a single `GONKA_API_KEY` environment variable -- no `baseUrl`, no model config, no JSON editing. Gonka appears in `openclaw models list` output alongside OpenAI, Anthropic, and OpenRouter.

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
4. **Model catalog** -- accurate pricing, context windows, and capability metadata for K2.5 (all quantization tiers)
5. **Extension headers** -- `X-Gonka-Session-ID` and `X-Gonka-Tier` handled as optional provider extensions that enhance but do not break standard OpenClaw flow

**Effort estimate:** 1-2 weeks engineering (PR preparation, tests, docs) + unknown review time (depends on maintainer responsiveness and feedback cycles).

**Timeline:** Target 3-6 months after Tier 2; depends on community traction, maintainer relationship quality, and OpenClaw team's priorities for adding new providers.

**Success criteria:**
- PR merged into openclaw/openclaw main branch
- Gonka appears in `openclaw models list` output
- Developers can configure Gonka with only `GONKA_API_KEY` environment variable
- Gonka provider page live in official OpenClaw documentation

**Risk:** High -- requires OpenClaw maintainer approval. This is not guaranteed. Per the CONTEXT.md decision: "community approach, not cold PR -- build relationship first." The community relationship plan (Section 4) is a prerequisite, not an optional nice-to-have. A cold PR from an unknown contributor will likely be ignored or rejected.

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
| 1 | OpenAI-compatible `/v1/chat/completions` API | DONE | 1 | -- | Engineering |
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
| 22 | ClawHub skill submission (SKILL.md) | NEEDED | 2 | 1 week | Engineering + Content |
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

**For partner-facing technical discussions:** Frame Gonka as "the agent-native inference provider" -- a description that is accurate, memorable, and crypto-free. The decentralized infrastructure is the "how," not the "what." Developers and partners care about what Gonka does for their agents, not how the network achieves consensus.

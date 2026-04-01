# Roadmap: Gonka Tokenomics

## Milestones

- ✅ **v1.0 Tokenomics Research** - Phase 1 (shipped 2026-02-05)
- ✅ **v1.1 Economic Modeling** - Phases 1-9 (shipped 2026-02-07)
- ✅ **v1.2 Kimi K2.5 Integration** - Phases 10-14 (shipped 2026-02-13)
- 🚧 **v1.3 OpenClaw Go-To-Market Research** - Phases 15-20 (in progress)

## Phases

<details>
<summary>✅ v1.0 Tokenomics Research (Phase 1) - SHIPPED 2026-02-05</summary>

Phase 1: 8 plans across 3 waves. See MILESTONES.md for details.

</details>

<details>
<summary>✅ v1.1 Economic Modeling (Phases 1-9) - SHIPPED 2026-02-07</summary>

Phases 1-9: 21 plans total. See MILESTONES.md for details.

</details>

<details>
<summary>✅ v1.2 Kimi K2.5 Integration & Agent Inference (Phases 10-14) - SHIPPED 2026-02-13</summary>

- [x] Phase 10: K2.5 Model Serving (1/1 plans) -- completed 2026-02-13
- [x] Phase 11: API Gateway (1/1 plans) -- completed 2026-02-13
- [x] Phase 12: Agent Inference Extensions (1/1 plans) -- completed 2026-02-13
- [x] Phase 13: Multi-Model & Admin (1/1 plans) -- completed 2026-02-13
- [x] Phase 14: Integration Testing (1/1 plans) -- completed 2026-02-13

5 phases, 5 plans, 27 requirements. See milestones/v1.2-ROADMAP.md for details.

</details>

### 🚧 v1.3 OpenClaw Go-To-Market Research (In Progress)

**Milestone Goal:** Research how to position Gonka as the inference provider of choice for OpenClaw developers, producing six interlocking GTM strategy documents that culminate in a prioritized v1.4 engineering backlog.

- [ ] **Phase 15: Competitive Analysis & Market Mapping** - Map the inference provider landscape and identify where Gonka wins
- [ ] **Phase 16: Developer Personas & Journey Mapping** - Define who OpenClaw builders are and how they make provider decisions
- [ ] **Phase 17: Positioning & Messaging** - Synthesize competitive gaps and persona insights into a message house
- [ ] **Phase 18: Channel Strategy** - Determine where and how to reach OpenClaw developers
- [ ] **Phase 19: Partnership & Ecosystem Strategy** - Define OpenClaw integration tiers and ClawHub entry plan
- [ ] **Phase 20: Product-Led Growth & v1.4 Backlog** - Synthesize all research into an actionable growth model and engineering priorities

## Phase Details

### Phase 15: Competitive Analysis & Market Mapping
**Goal**: Leadership has a complete picture of the inference provider landscape for OpenClaw agents -- who competes, on what dimensions, and where Gonka's structural advantages create winnable positions
**Depends on**: Nothing (first phase of v1.3)
**Requirements**: COMP-01, COMP-02, COMP-03
**Success Criteria** (what must be TRUE):
  1. A feature matrix exists comparing Gonka vs OpenRouter vs OpenAI vs Anthropic vs Together AI across agent-relevant dimensions (sessions, tiering, tool calling, streaming, memory, pricing model)
  2. Per-task and monthly cost projections exist for realistic OpenClaw agent workloads across all compared providers, showing where Gonka is cheaper and where it is not
  3. A provider landscape map categorizes all inference providers targeting OpenClaw developers into segments (centralized API, multi-provider router, dedicated inference, decentralized GPU) with positioning notes
  4. Gonka's competitive gaps are explicitly identified -- what must be closed before GTM push vs what can be deferred
**Plans**: TBD

Plans:
- [ ] 15-01: TBD
- [ ] 15-02: TBD

### Phase 16: Developer Personas & Journey Mapping
**Goal**: The team knows exactly who OpenClaw builders are, what drives their provider decisions, and where they get stuck in the adoption journey
**Depends on**: Phase 15 (competitive gaps inform persona pain points)
**Requirements**: MSG-01
**Success Criteria** (what must be TRUE):
  1. At least three developer persona cards exist with profiles, decision drivers, pain points, and adoption triggers -- grounded in community signals from GitHub, Discord, and Reddit
  2. Each persona has an AAARRRP journey map showing where they encounter Gonka and what objections arise at each stage
  3. Decision driver rankings are validated against real OpenClaw community discussions, not hypothesized in isolation
**Plans**: TBD

Plans:
- [ ] 16-01: TBD

### Phase 17: Positioning & Messaging
**Goal**: Gonka has a complete message house that translates its technical architecture into developer-facing value propositions, with vocabulary guidelines ensuring crypto-free developer language
**Depends on**: Phase 15 (competitive differentiation), Phase 16 (persona pain points)
**Requirements**: MSG-02, MSG-03
**Success Criteria** (what must be TRUE):
  1. A message house document exists with core positioning statement, 3-5 ranked value propositions, and per-persona differentiation statements
  2. An architecture-to-message mapping table translates every Gonka technical feature (sessions, tiering, memory, webhooks, Sprint Consensus) into a developer benefit statement
  3. Vocabulary guidelines define developer-facing language vs internal crypto terminology -- with explicit "never say" list and approved alternatives
  4. An agent-native pitch document explains why OpenClaw agents themselves (not just their developers) would autonomously prefer Gonka, with technical evidence
  5. An objection handling playbook addresses the top objections per persona with specific responses
**Plans**: TBD

Plans:
- [ ] 17-01: TBD

### Phase 18: Channel Strategy
**Goal**: The team knows exactly where to reach OpenClaw developers, what content to produce for each channel, and how to measure developer adoption (not vanity metrics)
**Depends on**: Phase 16 (persona locations), Phase 17 (messaging to deploy)
**Requirements**: GTM-01
**Success Criteria** (what must be TRUE):
  1. A channel matrix exists with priority tiers (P0/P1/P2/P3), specifying platform, content type, cadence, and expected reach for each channel
  2. Success metrics are defined with API-active developers (>100 calls/month) as the primary KPI, not follower counts or Discord members
  3. A content calendar framework maps content types to developer journey stages and channels, with the 70/30 split between AI/developer channels and crypto channels
**Plans**: TBD

Plans:
- [ ] 18-01: TBD

### Phase 19: Partnership & Ecosystem Strategy
**Goal**: The team has a concrete, sequenced plan for deepening Gonka's integration with the OpenClaw ecosystem -- from ClawHub listing to built-in provider status
**Depends on**: Phase 17 (positioning for partner conversations), Phase 18 (channel context)
**Requirements**: GTM-02
**Success Criteria** (what must be TRUE):
  1. A four-tier integration roadmap exists (Listed Provider -> Community Plugin -> Built-In Provider -> Preferred Partner) with prerequisites, effort estimates, and success criteria per tier
  2. A ClawHub submission plan is documented with required content, submission process, and timeline
  3. A built-in provider PR strategy outlines the technical requirements, community approach, and realistic timeline for getting Gonka merged into OpenClaw core
  4. Technical partnership requirements are defined -- what Gonka must deliver (SDK, docs, reliability SLA) before approaching OpenClaw maintainers for official partnership
**Plans**: TBD

Plans:
- [ ] 19-01: TBD

### Phase 20: Product-Led Growth & v1.4 Backlog
**Goal**: All GTM research converges into an actionable growth model with measurable funnel stages and a prioritized engineering backlog that tells v1.4 exactly what to build and in what order
**Depends on**: Phase 15-19 (synthesizes all prior research)
**Requirements**: GTM-03
**Success Criteria** (what must be TRUE):
  1. A PLG funnel model exists with defined stages (GitHub star -> docs -> API key -> first call -> 100th call -> paid) and target conversion rates per stage
  2. A free tier design spec defines what is included, usage limits, and the upgrade trigger -- requiring email-only signup with no wallet or crypto knowledge
  3. A time-to-first-inference optimization plan targets under 5 minutes from email to first API response, with the copy-paste OpenClaw config snippet as the atomic growth unit
  4. A prioritized v1.4 engineering backlog ranks all identified engineering work (provider plugin, docs site, self-serve signup, multi-model support, etc.) by GTM impact, with clear "must ship before marketing push" vs "nice to have" tiers
**Plans**: TBD

Plans:
- [ ] 20-01: TBD

## Progress

**Execution Order:** 15 -> 16 -> 17 -> 18 -> 19 -> 20

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 15. Competitive Analysis | v1.3 | 0/TBD | Not started | - |
| 16. Developer Personas | v1.3 | 0/TBD | Not started | - |
| 17. Positioning & Messaging | v1.3 | 0/TBD | Not started | - |
| 18. Channel Strategy | v1.3 | 0/TBD | Not started | - |
| 19. Partnership & Ecosystem | v1.3 | 0/TBD | Not started | - |
| 20. PLG & v1.4 Backlog | v1.3 | 0/TBD | Not started | - |

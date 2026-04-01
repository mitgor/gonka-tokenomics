# Gonka v1.4 Engineering Backlog

**Version:** 1.0
**Date:** 2026-04-01
**Classification:** Internal -- prioritized engineering roadmap for v1.4
**Dependencies:** Phase 15 (competitive analysis, gap analysis), Phase 16 (developer personas), Phase 17 (messaging), Phase 18 (channel strategy), Phase 19 (partnership playbook), Phase 20 (PLG growth model)
**Requirement:** GTM-03
**Companion document:** gonka_plg_growth_model.md (PLG funnel, free tier spec, time-to-first-inference plan)

---

## Executive Summary

This document is the single prioritized list of everything Gonka must build for v1.4, derived from six phases of GTM research (Phases 15-20). Every item traces to a specific research finding. Items are separated into must-ship (blocks developer acquisition) and nice-to-have (improves GTM but not a blocker), then ordered by GTM impact within each category.

The v1.4 engineering backlog consolidates 5 must-close infrastructure gaps from Phase 15, 28 NEEDED partnership requirements from Phase 19, PLG funnel blockers from Phase 20, feature gaps from the competitive matrix, and 4 tech debt items from v1.2. After de-duplication across sources, the backlog contains 18 must-ship items and 14 nice-to-have items.

The critical path runs through Sprint 1 infrastructure (public endpoint, docs site, self-serve signup, pricing page) and Sprint 2 product hardening (persistent sessions, OpenClaw plugin). Without these 6 items, Gonka cannot execute any developer-facing GTM activity -- developers literally cannot discover, evaluate, sign up for, or reliably use the service.

---

## Section 1: Source Inventory

Every engineering item in this backlog originates from one or more Phase 15-20 research outputs. This table shows the raw inventory before de-duplication.

| Source Phase | Document | Items Found | Category |
|--------------|----------|-------------|----------|
| Phase 15 | gonka_provider_landscape_map.md | 5 must-close gaps | Infrastructure |
| Phase 15 | gonka_provider_landscape_map.md | 6 can-defer gaps | Features / Tech Debt |
| Phase 15 | gonka_competitive_feature_matrix.md | 2 LOSE verdicts (Uptime/Reliability, Model Breadth) | Features |
| Phase 16 | gonka_developer_personas.md | Per-persona feature needs (3 personas x 6 AAARRRP stages) | Features / Content |
| Phase 17 | gonka_message_house.md | Vocabulary enforcement, landing page requirements | Content / Design |
| Phase 18 | gonka_channel_strategy.md | P0 channel prerequisites (docs site, Discord presence, GitHub PRs) | Infrastructure / Community |
| Phase 19 | gonka_partnership_playbook.md | 28 NEEDED items (5 DONE from v1.2) across 5 categories | Partnership |
| Phase 20 | gonka_plg_growth_model.md | PLG funnel blockers (7 time-to-first-inference steps, 6 of 7 need engineering) | PLG |
| v1.2 | PROJECT.md | 4 tech debt items (TF-IDF, in-memory sessions, JSON keys, no GPU load balancing) | Tech Debt |

### De-duplication Map

Several items appear in multiple sources. The table below shows which items were consolidated to avoid double-counting.

| Consolidated Item | Appears In | Treated As |
|-------------------|-----------|------------|
| Public docs site (docs.gonka.ai) | Phase 15 must-close gap #2, Phase 19 requirement #7, Phase 20 TTFI Step 1-2, Phase 18 P0 channel prerequisite | Must-Ship #2 |
| Self-serve API key signup | Phase 15 must-close gap #3, Phase 19 requirement #8, Phase 20 TTFI Steps 3-5, Phase 20 free tier spec | Must-Ship #3 |
| Published pricing page | Phase 15 must-close gap #4, Phase 19 requirements #9 and #29, Phase 20 funnel (Explore stage conversion driver) | Must-Ship #4 |
| Persistent sessions (Redis) | Phase 15 must-close gap #5, v1.2 tech debt, Phase 19 requirement #12, Phase 20 funnel (Habitual Use driver) | Must-Ship #6 |
| OpenClaw built-in provider | Phase 15 must-close gap #1, Phase 19 requirement #18 (Tier 3), Phase 18 P0 channel (GitHub PRs) | Must-Ship #5 (interim: plugin at Must-Ship #7) |
| Public endpoint (api.gonka.ai) | Phase 15 infrastructure prerequisite, Phase 19 requirement #6, Phase 20 TTFI Step 7 | Must-Ship #1 |
| Uptime/status page | Phase 15 can-defer, Phase 19 requirements #11 and #25, Phase 20 Startup CTO retention | Must-Ship #10 |
| Cost comparison calculator | Phase 19 requirement #33, Phase 20 Weekend Builder paid conversion driver | Nice-to-Have #4 |

After de-duplication, **32 unique engineering items** remain: 18 must-ship and 14 nice-to-have.

---

## Must-Ship Before Marketing Push

These 18 items MUST be complete before any developer-facing marketing, content publishing, or partnership outreach. They are ordered by GTM impact (highest first). Without these, the PLG funnel from Phase 20 cannot function -- developers cannot discover, evaluate, sign up for, or reliably use Gonka.

### GTM Impact and Effort Scale

- **GTM Impact:** Critical (blocks entire funnel) / High (blocks specific persona or stage) / Medium (degrades experience but not a blocker)
- **Effort:** S (1-2 days) / M (3-5 days) / L (1-2 weeks) / XL (2-4 weeks)

### Must-Ship Items

| # | Item | GTM Impact | Effort | Source | Rationale |
|---|------|-----------|--------|--------|-----------|
| 1 | **Publicly accessible production endpoint** (api.gonka.ai) | Critical | L | Phase 15 gap, Phase 19 #6, Phase 20 TTFI Step 7 | Without a live endpoint, nothing else matters. v1.2 infrastructure exists but is not publicly deployed. Requires domain, SSL, health-checked routing, warm K2.5 model. |
| 2 | **Public documentation site** (docs.gonka.ai) | Critical | L | Phase 15 must-close gap #2, Phase 19 #7, Phase 20 TTFI Steps 1-2, Phase 18 P0 | Blocks the PLG funnel at Step 1 (Discover). Developers make provider decisions based on documentation quality. No docs = no evaluation. Minimum 10 pages: quickstart, API reference, OpenClaw integration guide, pricing, troubleshooting. |
| 3 | **Self-serve API key signup** (email-only) | Critical | L | Phase 15 must-close gap #3, Phase 19 #8, Phase 20 TTFI Steps 3-5, Phase 20 free tier | Blocks the PLG funnel at Step 3 (Sign Up). Email-only form, no wallet, no OAuth, no credit card. API key displayed immediately after email verification. Free tier limits activated automatically. Per CONTEXT.md locked decision. |
| 4 | **Published pricing page** | Critical | M | Phase 15 must-close gap #4, Phase 19 #9/#29, Phase 20 Explore stage | Blocks funnel conversion and competitive evaluation. Developers cannot estimate costs or compare against Together AI ($0.50/$2.50) and DeepInfra ($0.45/$2.25) without published rates. Must include per-token rates for all K2.5 tiers. |
| 5 | **OpenClaw community plugin** (npm) | Critical | XL | Phase 15 must-close gap #1, Phase 19 #15, Phase 18 P0 channel | Gonka is invisible to ~95% of OpenClaw developers who use default/built-in providers. The plugin (`openclaw-plugin-gonka` on npm) is the interim step toward built-in provider status (Tier 3). Blocks ClawHub integration and Tier 1-2 partnership validation. |
| 6 | **Persistent sessions** (Redis migration) | Critical | L | Phase 15 must-close gap #5, v1.2 tech debt, Phase 19 #12 | Session persistence is Gonka's #1 competitive advantage (WIN in feature matrix) and the core of the 73% cost reduction claim. In-memory sessions are lost on restart -- first session loss event destroys developer trust permanently. Redis migration with TTL-based expiration and replication. |
| 7 | **OpenClaw integration guide** ("Add Gonka in 90 Seconds") | High | S | Phase 19 #14, Phase 20 TTFI Step 6 | The pre-filled openclaw.json config snippet is the atomic growth unit (Phase 20). Must show BOTH steps (provider definition AND model allowlisting) to prevent the silent failure gotcha documented in STACK.md. |
| 8 | **openclaw.json configuration template** | High | S | Phase 19 #13, Phase 20 TTFI Step 6 | Pre-filled config snippet generator on the docs site. Developer's specific API key is embedded in the snippet with copy button. This is the viral mechanism -- copy-pasteable, version-controlled, portable across environments. |
| 9 | **Terms of service** | High | M | Phase 19 #30 | Legal prerequisite for any public-facing service. Cannot accept signups without ToS. |
| 10 | **Privacy policy** | High | M | Phase 19 #31, Phase 16 Privacy-First Builder | Legal prerequisite. Must be inference-specific: what is logged, what is not, retention periods, node operator agreements. Privacy-First Builder reviews this before signup -- generic boilerplate causes drop-off. |
| 11 | **Public uptime/status page** (status.gonka.ai) | High | M | Phase 15 can-defer (upgraded), Phase 19 #11/#25, Phase 20 Startup CTO retention | Startup CTO requires visible reliability data before committing to production use. Real-time status with per-model availability and historical uptime. Incident report publication process. |
| 12 | **Rate limit documentation** (RPM/TPM per tier) | High | S | Phase 19 #10 | Developers need to know rate limits before integrating. Must document free tier (60 RPM, 1000 req/day) and paid tier limits. Required for Tier 2 partnership validation. |
| 13 | **Transactional email infrastructure** | High | M | Phase 20 TTFI Step 4 | Verification emails must arrive within 60 seconds. Requires SendGrid/Postmark/SES with dedicated IP, SPF, DKIM, DMARC. Delayed emails (>2 min) cause permanent developer abandonment. |
| 14 | **Support channels** (GitHub Issues + Discord) | High | S | Phase 19 #32, Phase 18 P0 channels | Developers expect a way to report issues and get help. GitHub Issues for bug reports, Discord for real-time support. OpenClaw Discord presence is a P0 channel requirement. |
| 15 | **Landing page design** (passes "is this crypto?" test) | High | M | Phase 17 VP3, Phase 20 TTFI Step 2 | Landing page must resemble Vercel/Supabase, not a DeFi protocol. Single CTA above the fold ("Get API Key"). No crypto terminology before the config snippet. Follows Phase 17 never-say list. |
| 16 | **Verification endpoint** (GET /v1/verify) | Medium | S | Phase 20 TTFI failure modes | Returns 200 if API key is valid. Helps developers verify their configuration before sending real requests. Prevents the "silent failure" scenario where misconfiguration goes undetected. |
| 17 | **Usage limit headers** (X-Gonka-Usage-Remaining) | Medium | S | Phase 20 free tier upgrade triggers | Every API response includes usage headers showing remaining requests/tokens. At 80% usage, upgrade URL included. Drives paid conversion without hard-blocking workflows. Already partially implemented in v1.2 rate limiting. |
| 18 | **Error messages overhaul** (actionable, no crypto terms) | Medium | M | Phase 17 vocabulary, Phase 20 free tier spec | All error messages must be actionable and specific. "Free tier daily limit reached. Resets at midnight UTC." not "Insufficient GNK balance." HTTP 429 responses must include reset time and upgrade URL. Follows never-say list. |

### Must-Ship Item Details

#### Must-Ship #1: Publicly Accessible Production Endpoint

- **Blocks:** Entire PLG funnel -- nothing works without a live API
- **Personas blocked:** All three (Weekend Builder, Startup CTO, Privacy-First Builder)
- **Definition of done:** `https://api.gonka.ai/v1/chat/completions` returns valid responses with sub-200ms TTFT. SSL certificate valid. Health check endpoint responds. K2.5 model loaded and warm on minimum N nodes.
- **Dependencies:** None (first item to build)
- **Source:** Phase 15 (gonka_provider_landscape_map.md: infrastructure prerequisite), Phase 19 (requirement #6: 1-2 weeks estimated), Phase 20 (TTFI Step 7)

#### Must-Ship #2: Public Documentation Site

- **Blocks:** PLG funnel at Discover stage (Step 1). Developers cannot evaluate Gonka without documentation.
- **Personas blocked:** All three -- each persona has a different docs entry point (Weekend Builder: quickstart; Startup CTO: architecture; Privacy-First: data handling policy)
- **Definition of done:** docs.gonka.ai live with SSL, CDN, sub-2s page load. Minimum 10 pages: quickstart guide (< 5 min to first API call), API reference (all endpoints), OpenClaw integration guide, migration guide from OpenRouter, pricing page, data handling policy, troubleshooting, architecture overview, status page link, support channels.
- **Dependencies:** Must-Ship #1 (endpoint must exist for quickstart to reference)
- **Source:** Phase 15 (must-close gap #2), Phase 19 (requirement #7: 2-3 weeks estimated), Phase 20 (TTFI Steps 1-2), Phase 18 (P0 channel prerequisite)

#### Must-Ship #3: Self-Serve API Key Signup (Email-Only)

- **Blocks:** PLG funnel at Sign Up stage (Step 3). Without self-serve signup, the conversion funnel cannot exist. Per Phase 16: 95% funnel drop at wallet step -- email-only eliminates this.
- **Personas blocked:** All three -- each persona expects different signup friction (Weekend Builder: zero friction; Startup CTO: team accounts; Privacy-First: privacy review before signup)
- **Definition of done:** Web form at docs.gonka.ai with single email field. Verification email sent within 60 seconds. API key displayed immediately after click-through with one-click copy. Free tier limits activated automatically. No approval queue, no waitlist.
- **Dependencies:** Must-Ship #1 (endpoint), Must-Ship #13 (email infrastructure)
- **Source:** Phase 15 (must-close gap #3), Phase 19 (requirement #8: 1-2 weeks), Phase 20 (TTFI Steps 3-5, free tier signup flow)

#### Must-Ship #4: Published Pricing Page

- **Blocks:** PLG funnel at Explore stage. Cost advantage claims are unverifiable without published rates. Developers cannot budget for Gonka usage or compare against Together AI ($0.50/$2.50) and DeepInfra ($0.45/$2.25).
- **Personas blocked:** Weekend Builder (cost comparison is #1 conversion driver), Startup CTO (needs to justify cost to co-founder)
- **Definition of done:** gonka.ai/pricing with per-token rates for K2.5 lite/mid/full tiers. Comparison table against OpenRouter, Together AI, DeepInfra. Free tier limits clearly shown. Upgrade path from free to paid.
- **Dependencies:** Leadership decision on pricing (Scenario B recommended: $0.35/$1.75)
- **Source:** Phase 15 (must-close gap #4), Phase 19 (requirements #9, #29: 1 week), Phase 20 (Explore stage conversion driver)

#### Must-Ship #5: OpenClaw Community Plugin (npm)

- **Blocks:** ClawHub integration, Tier 1-2 partnership validation. Gonka is invisible to developers who rely on built-in or plugin-based providers. The plugin is the interim step toward Tier 3 (built-in provider PR).
- **Personas blocked:** Weekend Builder (wants zero-config or near-zero-config), Startup CTO (needs validated integration path)
- **Definition of done:** `openclaw-plugin-gonka` published on npm. Installs via `npx openclaw install gonka`. Provides session management, model tiering, and memory API through OpenClaw's jiti-based plugin loading. 50+ npm installs for Tier 3 readiness.
- **Dependencies:** Must-Ship #1 (endpoint), Must-Ship #7 (integration guide), Phase 19 Tier 2 requirements
- **Source:** Phase 15 (must-close gap #1), Phase 19 (requirement #15: 2-3 weeks), Phase 18 (P0 channel)

#### Must-Ship #6: Persistent Sessions (Redis Migration)

- **Blocks:** Gonka's #1 competitive advantage claim. Session persistence is the foundation of the 73% heartbeat cost reduction (Phase 17 VP1). In-memory sessions lost on restart undermine this claim at first occurrence.
- **Personas blocked:** Startup CTO (infrastructure trust is their #1 concern), Weekend Builder (sessions are the cost savings mechanism)
- **Definition of done:** Sessions stored in Redis (or equivalent distributed cache). Sessions survive server restarts. TTL-based expiration with configurable retention. Session state replicated across nodes. Zero data loss on deploy/restart.
- **Dependencies:** Must-Ship #1 (endpoint must be live to test against)
- **Source:** Phase 15 (must-close gap #5), v1.2 tech debt, Phase 19 (requirement #12: 1-2 weeks)

---

## Nice-to-Have (Post-Launch)

These 14 items improve GTM effectiveness but are not blockers for initial developer acquisition. They are ordered by impact and grouped by suggested timeline.

### Within 30 Days of Launch

| # | Item | GTM Impact | Effort | Source | Timeline Rationale |
|---|------|-----------|--------|--------|-------------------|
| 1 | **MCP server for agent extensions** (sessions, memory, tiering) | Medium | XL | Phase 19 #16 | Tier 2 partnership requirement. ~500 LOC TypeScript per ARCHITECTURE.md. Enables richer agent integration beyond basic inference. |
| 2 | **Quickstart repository** (GitHub template) | Medium | M | Phase 19 #17, Phase 20 TTFI | Pre-built template repo showing Gonka + OpenClaw integration. Reduces time-to-first-inference for developers who learn by cloning rather than reading docs. |
| 3 | **Integration guide on dev.to or Medium** | Medium | M | Phase 19 #20 | Content piece that doubles as P1 channel presence. Tutorial format showing real agent use case with Gonka. |
| 4 | **Cost comparison calculator** | Medium | M | Phase 19 #33, Phase 20 Weekend Builder conversion | Interactive calculator: input messages/day + heartbeat interval, output estimated monthly cost vs OpenRouter vs Together AI. Drives paid conversion by making savings concrete. |

### Within 60 Days of Launch

| # | Item | GTM Impact | Effort | Source | Timeline Rationale |
|---|------|-----------|--------|--------|-------------------|
| 5 | **ClawHub skill submission** (SKILL.md) | Medium | M | Phase 19 #22 | Teaches agents session/tiering/memory usage. 1-2 weeks from Tier 1 completion. Requires plugin to be stable first. |
| 6 | **Video tutorial** ("OpenClaw + Gonka in 5 Minutes") | Medium | M | Phase 19 #21 | Visual learners. Production value matters -- low-quality video hurts more than no video. Wait until the flow is polished. |
| 7 | **Published benchmark results** (latency p50/p95, throughput) | Medium | M | Phase 19 #26 | Startup CTO needs performance data. Requires stable production environment to generate meaningful benchmarks. |
| 8 | **Non-Gonka PR contributions** to openclaw/openclaw | Medium | L | Phase 19 #23, Phase 18 P0 channel | 3-5 merged PRs build community trust before proposing built-in provider (3-6 month timeline per Phase 19). Bug fixes, docs improvements, test additions. |

### Within 90 Days of Launch

| # | Item | GTM Impact | Effort | Source | Timeline Rationale |
|---|------|-----------|--------|--------|-------------------|
| 9 | **Hashed API key storage** (DB migration from JSON) | Low | L | v1.2 tech debt, Phase 15 can-defer | Current JSON storage is acceptable for <100 keys. Must migrate before enterprise outreach or >100 active keys. Add key rotation and scoping. |
| 10 | **Vector embeddings for memory API** (replace TF-IDF) | Low | L | v1.2 tech debt, Phase 15 can-defer | TF-IDF search is functional but lower recall than vector-based. Quality gap becomes apparent when developers build sophisticated memory workflows. |
| 11 | **GPU load balancing** | Low | XL | v1.2 tech debt, Phase 15 can-defer | Single-node routing sufficient for launch (<10 concurrent users per node). Required before scaling beyond early adopter phase. |
| 12 | **Additional model support** (Llama 4, DeepSeek V3) | Low | XL | Phase 15 can-defer (Model Breadth: LOSE) | Position as "the best K2.5 agent experience" for launch. Add 1-2 models when scaling to Active/Heavy tiers (3-6 months post-GTM). |
| 13 | **Developer usage dashboard** (web UI) | Low | XL | Phase 15 can-defer, Phase 20 Habitual Use stage | CLI/API stats sufficient for early adopter developers. Dashboard needed when non-technical team members need spend visibility. |
| 14 | **SLA documentation** with uptime commitments | Low | M | Phase 15 can-defer, Phase 19 #27 | No SLA until proven uptime. Publish transparent uptime statistics as interim. Formal SLA terms required before enterprise/startup outreach. |

### Nice-to-Have Item Notes

**Items NOT included (out of scope for v1.4):**
- Smart contracts or on-chain governance (per REQUIREMENTS.md out-of-scope)
- Paid advertising or sponsored content (per REQUIREMENTS.md out-of-scope)
- Token economics changes (v1.0/v1.1 scope, not v1.4)
- TEE-based encrypted inference (roadmap item, not v1.4 engineering)
- Multi-region deployment (premature before single-region stability proven)

---

## Build Order Recommendation

The 18 must-ship items are organized into dependency-aware sprints. Items within each sprint can be parallelized where noted.

### Sprint 1: Foundation (Week 1-2)

**Goal:** Developers can discover Gonka, read documentation, and see pricing. The PLG funnel is open from Discover through Explore.

| Item | Must-Ship # | Effort | Parallel? | Dependencies |
|------|------------|--------|-----------|--------------|
| Publicly accessible production endpoint | #1 | L | Yes (independent) | None |
| Public documentation site | #2 | L | Yes (can build content while #1 deploys) | Final content references #1 URL |
| Published pricing page | #4 | M | Yes (parallel with docs) | Leadership pricing decision |
| Landing page design | #15 | M | Yes (part of docs site build) | Phase 17 vocabulary guidelines |
| Terms of service | #9 | M | Yes (legal can draft in parallel) | None |
| Privacy policy | #10 | M | Yes (legal can draft in parallel) | None |
| Rate limit documentation | #12 | S | Yes (part of docs content) | None |
| Support channels (GitHub Issues + Discord) | #14 | S | Yes (setup task) | None |

**Sprint 1 outputs:** api.gonka.ai live, docs.gonka.ai live with 10+ pages, pricing visible, legal pages published, support channels operational.

**Critical path item:** Must-Ship #1 (production endpoint) -- everything else references it.

### Sprint 2: Signup Flow (Week 3-4)

**Goal:** Developers can sign up, get an API key, and make their first inference. The PLG funnel is open from Discover through First Inference.

| Item | Must-Ship # | Effort | Parallel? | Dependencies |
|------|------------|--------|-----------|--------------|
| Transactional email infrastructure | #13 | M | Yes (start early in sprint) | Domain auth (SPF/DKIM/DMARC) |
| Self-serve API key signup (email-only) | #3 | L | After #13 email infra | #1 (endpoint), #13 (email) |
| openclaw.json configuration template | #8 | S | Yes (can build generator while signup deploys) | #1 (endpoint URL for template) |
| OpenClaw integration guide | #7 | S | Yes (content creation) | #8 (template to reference) |
| Verification endpoint (GET /v1/verify) | #16 | S | Yes (small API addition) | #1 (endpoint) |
| Usage limit headers | #17 | S | Yes (middleware addition) | #1 (endpoint) |
| Error messages overhaul | #18 | M | Yes (can audit concurrently) | Phase 17 vocabulary guidelines |

**Sprint 2 outputs:** Complete signup-to-first-inference flow operational. Time-to-first-inference target of 4m15s achievable. Config snippet with copy button on verification page.

**Critical path items:** Must-Ship #13 (email infra) -> Must-Ship #3 (signup flow). These are sequential -- signup cannot work without email delivery.

### Sprint 3: Product Hardening (Week 5-6)

**Goal:** Sessions are production-grade, OpenClaw plugin available, status page live. The PLG funnel is fully operational through Habitual Use.

| Item | Must-Ship # | Effort | Parallel? | Dependencies |
|------|------------|--------|-----------|--------------|
| Persistent sessions (Redis migration) | #6 | L | Yes | #1 (endpoint) |
| OpenClaw community plugin (npm) | #5 | XL | Yes (can develop in parallel with Redis work) | #1 (endpoint), #7 (integration guide) |
| Public uptime/status page | #11 | M | Yes | #1 (endpoint to monitor) |

**Sprint 3 outputs:** Sessions survive restarts (Redis-backed), OpenClaw plugin on npm, status.gonka.ai live. Gonka is ready for developer-facing marketing.

**Critical path item:** Must-Ship #6 (persistent sessions) -- cannot market "73% cost reduction via session persistence" if sessions are lost on restart.

### Sprint Timeline Summary

```
Week 1 -------- Week 2 -------- Week 3 -------- Week 4 -------- Week 5 -------- Week 6
|-- Sprint 1: Foundation -----||-- Sprint 2: Signup Flow ------||-- Sprint 3: Hardening -------|
   api.gonka.ai live              Email infra + signup flow         Redis sessions
   docs.gonka.ai live             Config template + guide           OpenClaw npm plugin
   Pricing page                   Verify endpoint + headers         Status page
   Legal pages + support          Error messages overhaul
```

**Total timeline:** 6 weeks for all 18 must-ship items.

**What can be parallelized across sprints:**
- Sprint 3 items (Redis migration, plugin development) can start during Sprint 2 if engineering capacity allows. The plugin has a 2-3 week estimate (Phase 19) and benefits from early start.
- Legal documents (ToS, privacy policy) from Sprint 1 can be drafted before Sprint 1 formally begins.
- Content creation (docs, guides, rate limit docs) can begin immediately if endpoint URLs are known in advance.

### Critical Path

The longest sequential dependency chain determines the minimum timeline:

```
Production endpoint (#1, 2 weeks)
  -> Email infrastructure (#13, 1 week)
    -> Self-serve signup (#3, 2 weeks)
      -> [GTM-ready for initial outreach]

Production endpoint (#1, 2 weeks)
  -> Persistent sessions (#6, 2 weeks)
    -> [Can market session persistence claim]

Production endpoint (#1, 2 weeks)
  -> OpenClaw plugin (#5, 3 weeks, can overlap with #6)
    -> [Partnership Tier 1-2 achievable]
```

**Minimum time to GTM-ready state:** 5 weeks (Sprint 1 + Sprint 2 + overlap start on Sprint 3).

**Minimum time to full v1.4 completion:** 6 weeks (all 3 sprints).

---

## Section 4: Partnership Requirement Coverage

All 28 NEEDED items from Phase 19 (gonka_partnership_playbook.md) are accounted for in this backlog. This table maps each requirement to its backlog location.

| Phase 19 # | Requirement | Backlog Location | Tier |
|------------|-------------|-----------------|------|
| 6 | Publicly accessible production endpoint | Must-Ship #1 | 1 |
| 7 | API documentation site | Must-Ship #2 | 1 |
| 8 | Self-service API key signup | Must-Ship #3 | 1 |
| 9 | Public pricing page | Must-Ship #4 | 1 |
| 10 | Rate limit documentation | Must-Ship #12 | 2 |
| 11 | Public uptime/status page | Must-Ship #11 | 3 |
| 12 | Persistent sessions (Redis) | Must-Ship #6 | 3 |
| 13 | openclaw.json configuration template | Must-Ship #8 | 1 |
| 14 | OpenClaw integration guide | Must-Ship #7 | 1 |
| 15 | npm provider plugin | Must-Ship #5 | 2 |
| 16 | MCP server for agent extensions | Nice-to-Have #1 | 2 |
| 17 | Quickstart repository | Nice-to-Have #2 | 2 |
| 18 | Gonka provider module for openclaw/openclaw PR | Deferred (Tier 3 gate: 50+ npm installs) | 3 |
| 19 | OpenClaw Discord presence | Must-Ship #14 | 1 |
| 20 | Integration guide on dev.to/Medium | Nice-to-Have #3 | 2 |
| 21 | Video tutorial | Nice-to-Have #6 | 2 |
| 22 | ClawHub skill submission | Nice-to-Have #5 | 2 |
| 23 | Non-Gonka PR contributions | Nice-to-Have #8 | 3 |
| 24 | GitHub Discussion RFC for built-in provider | Deferred (Tier 3 gate: community trust established) | 3 |
| 25 | Uptime monitoring | Must-Ship #11 (consolidated with #11) | 3 |
| 26 | Published benchmark results | Nice-to-Have #7 | 3 |
| 27 | SLA terms document | Nice-to-Have #14 | 4 |
| 28 | Security audit/practices statement | Deferred (Tier 4 gate: significant user base) | 4 |
| 29 | Public pricing page (Business) | Must-Ship #4 (consolidated with #9) | 1 |
| 30 | Terms of service | Must-Ship #9 | 1 |
| 31 | Privacy policy | Must-Ship #10 | 1 |
| 32 | Support channels | Must-Ship #14 | 1 |
| 33 | Cost comparison calculator | Nice-to-Have #4 | 2 |

**Coverage:** 28/28 NEEDED items accounted for. 14 in must-ship, 11 in nice-to-have, 3 deferred to Tier 3-4 gates (require community adoption milestones first).

---

## Section 5: Milestone Definition

### What "v1.4 Shipped" Means

**v1.4 is shipped when a developer can discover Gonka through documentation or the OpenClaw ecosystem, sign up with only an email address, receive an API key within 60 seconds, paste a pre-filled configuration snippet into their openclaw.json, and send their first inference request through Gonka's network -- all within 5 minutes, with sessions persisting across requests in Redis, pricing published and competitive with Together AI and DeepInfra, and the OpenClaw community plugin available on npm.**

Measurable criteria:

1. **api.gonka.ai** responds to `/v1/chat/completions` with sub-200ms TTFT and valid K2.5 inference
2. **docs.gonka.ai** is live with 10+ pages covering the complete developer journey
3. **Email-only signup** produces a working API key within 60 seconds of submission
4. **Pricing page** shows per-token rates for K2.5 lite/mid/full tiers with competitor comparison
5. **Sessions** are stored in Redis and survive server restarts with zero data loss
6. **`openclaw-plugin-gonka`** is published on npm and installable
7. **Time-to-first-inference** is under 5 minutes for a developer starting from docs.gonka.ai
8. **All 18 must-ship items** in this backlog are complete with passing verification

Items in the nice-to-have section are explicitly excluded from the v1.4 milestone. They improve the GTM experience but are not required for the "developer can go from zero to first inference" threshold. The nice-to-have items form the v1.4.x patch roadmap for the 90 days following v1.4 launch.

### What v1.4 Does NOT Include

- Additional models beyond K2.5 (single-model positioning for launch)
- GPU load balancing (single-node sufficient for early adopter traffic)
- Vector embeddings for memory API (TF-IDF is functional)
- Developer usage dashboard (CLI/API stats sufficient)
- SLA guarantees (no SLA until proven uptime history)
- TEE-based encrypted inference (roadmap, not v1.4)
- Built-in OpenClaw provider status (requires 3-6 months of community engagement per Phase 19)

---

## Cross-References

Every item in this backlog traces to specific Phase 15-20 research findings. This section lists each source document and what was drawn from it.

| Document | Phase | What Was Used |
|----------|-------|---------------|
| **gonka_provider_landscape_map.md** | Phase 15 | 5 must-close gaps (built-in provider, docs site, self-serve signup, pricing page, persistent sessions). 6 can-defer gaps (single model, JSON keys, TF-IDF, load balancing, dashboard, SLA). Gap closure definitions. |
| **gonka_competitive_feature_matrix.md** | Phase 15 | WIN verdicts (Agent Sessions, Model Tiering) confirming which features to lead with. LOSE verdicts (Uptime/Reliability, Model Breadth) identifying weaknesses to mitigate or defer. Feature comparison data for prioritization rationale. |
| **gonka_developer_personas.md** | Phase 16 | Three personas with distinct feature needs at each AAARRRP stage. Weekend Builder: cost-driven, needs zero-friction signup. Startup CTO: reliability-driven, needs status page and team accounts. Privacy-First Builder: privacy-driven, needs honest capabilities page. Per-persona drop-off risks informing must-ship vs nice-to-have classification. |
| **gonka_message_house.md** | Phase 17 | 16-item never-say list enforced in error messages and landing page design. VP1 (73% cost reduction) as the lead message requiring persistent sessions to be credible. Landing page design requirements (resembles Vercel/Supabase, not DeFi). |
| **gonka_channel_strategy.md** | Phase 18 | P0 channel prerequisites (docs site, Discord presence, GitHub PRs). 70/30 channel split confirming developer channels (70%) take priority. Primary KPI (API-active developers >100 calls/month) informing free tier limits and upgrade triggers. |
| **gonka_partnership_playbook.md** | Phase 19 | 28 NEEDED technical requirements with effort estimates and tier assignments. Four-tier integration roadmap defining the path from Listed (Tier 1) to Preferred Partner (Tier 4). Community-first PR strategy timeline (3-6 months). ClawHub submission requirements. |
| **gonka_plg_growth_model.md** | Phase 20 | PLG funnel stages with conversion rates. Free tier design spec (15M tokens/month, 1000 req/day, 2 sessions, email-only). Time-to-first-inference plan (7 steps, 4m15s target). Atomic growth unit (openclaw.json config snippet). Upgrade trigger mechanisms (X-Gonka-Usage-Remaining headers). Failure mode analysis for each TTFI step. |
| **PROJECT.md** | v1.2 | 4 tech debt items: TF-IDF search (needs vector embeddings), in-memory sessions (needs Redis), JSON key storage (needs DB), no GPU load balancing. |

---

*Document: gonka_v14_engineering_backlog.md | Version 1.0 | 2026-04-01*
*Capstone deliverable for Phases 15-20. Companion document: gonka_plg_growth_model.md (PLG funnel, free tier spec, time-to-first-inference plan)*

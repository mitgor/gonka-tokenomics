# Gonka v1.4 Engineering Backlog

**Version:** 1.3
**Date:** 2026-07-18 (revised; original 2026-04-01)
**Classification:** Internal -- prioritized engineering roadmap for v1.4
**Dependencies:** Phase 15 (competitive analysis, gap analysis), Phase 16 (developer personas), Phase 17 (messaging), Phase 18 (channel strategy), Phase 19 (partnership playbook), Phase 20 (PLG growth model)
**Requirement:** GTM-03
**Companion document:** gonka_plg_growth_model.md (PLG funnel, free tier spec, time-to-first-inference plan)

---

## Executive Summary

This document is the single prioritized list of everything Gonka must build for v1.4, derived from six phases of GTM research (Phases 15-20). Every item traces to a specific research finding. Items are separated into must-ship (blocks developer acquisition) and nice-to-have (improves GTM but not a blocker), then ordered by GTM impact within each category.

The v1.4 engineering backlog consolidates 5 must-close infrastructure gaps from Phase 15, 28 NEEDED partnership requirements from Phase 19, PLG funnel blockers from Phase 20, feature gaps from the competitive matrix, and 4 tech debt items from v1.2. After de-duplication across sources, the backlog contains 18 must-ship items and 14 nice-to-have items.

The critical path runs through Sprint 1 infrastructure (public endpoint, docs site, self-serve signup, pricing page) and Sprint 2 product hardening (persistent sessions, OpenClaw plugin). Without these 6 items, Gonka cannot execute any developer-facing GTM activity -- developers literally cannot discover, evaluate, sign up for, or reliably use the service.

### July 2026 Revision Notes

This revision re-baselines the backlog against the market as of 2026-07-18. Five changes ripple through the items below:

1. **Model baseline.** Kimi K2.5 (Jan 2026) has been superseded twice: Kimi K2.6 shipped April 20, 2026 (1T MoE, 32B active, ~256K context, multimodal) and Kimi K2.7-Code shipped June 12, 2026 (256K context, Modified MIT, +21.8% on Kimi Code Bench v2 over K2.6). Kimi K3 (2.8T MoE, 896 experts/16 active, 1M context, native multimodal) launched via app and API July 16, 2026, with full open weights scheduled by July 27 -- the largest open-weight release ever. All "K2.5 tiers" language now means the Kimi model family: K2.6 as workhorse tier, K2.7-Code for coding agents, K3 as frontier tier once weights land.
2. **Pricing anchors.** K2.5 is off the pricing map entirely: Moonshot discontinued the older kimi-k2-series API models on May 25, 2026, and Together has delisted K2.5. All comparisons must anchor on current-generation rates: K2.6 ($0.95/$4.00 per 1M official; DeepInfra $0.75/$3.50; Together $1.20/$4.50), K2.7-Code ($0.95 input / $0.19 cache-hit / $4.00 output), and K3 API ($3/$15). Any residual K2.5 rate (e.g., the old OpenRouter $0.375/$2.025) is a delisting-track artifact, not a live benchmark. Separately, DeepSeek's official V4 release (announced Jun 30 for mid-July 2026) introduces China's first time-of-day API pricing -- rates double during Beijing peak hours (9:00-12:00, 14:00-18:00): V4-Pro ≈$0.42/$0.84 off-peak vs ≈$0.84/$1.68 peak per 1M, with legacy deepseek-chat/deepseek-reasoner endpoints retired after July 24, 2026. Flat-rate DeepSeek cost floors elsewhere in the research understate 24/7 agent-workload cost by up to 2x during Beijing business hours; conversely, "no rush-hour pricing" is a new positioning lever for Gonka's pricing page.
3. **Model tiering is commoditized.** Cost-based routing is now a solved layer in the OpenClaw ecosystem (ClawRouter bundled with OpenClaw; multiple third-party routers claim 70-92% savings). Gonka's defensible advantage is server-side persistent sessions/memory, not routing.
4. **OpenClaw governance.** The OpenClaw Foundation formally launched July 8, 2026 as a 501(c)(3) (chaired by Dave Morin, with Peter Steinberger), with published leadership, paid maintainers, an MIT-license commitment, and 30+ partner/donor orgs (published major donors: OpenAI, Microsoft, NVIDIA, Offline Holdings, University of Michigan; partners include Microsoft, Tencent, Atlassian, Vercel, Cloudflare, GitHub). The foundation's donor page designates no "lead sponsor" -- that phrase is press shorthand. The precise conflict: OpenAI is one of five published major donors and employs the project's creator (Steinberger runs "Claw Labs" inside OpenAI), so the built-in-provider path runs through a foundation materially tied to a rival inference vendor. The foundation itself flags single-sponsor dependency as a risk. The foundation now publishes its own headline adoption metrics (Jul 2026): 4.5 million new claws (users/agents) per week, "fastest growing GitHub repository in history," and ~30,000 ClawCon registrations across 34 events in 16 countries in five months -- superseding the unverified ~3.2M active-user figure from the Apr 2026 research.
5. **Served-model lineup.** The Gonka network serves three model families -- Qwen3 235B, Kimi K2.6, and MiniMax M2.7 -- with GLM-5.2 (Z.ai, released June 13, 2026; 1M context, open weights, leads open agent benchmarks) listed as coming soon on the Gonka blog; reseller Gonka24 already publishes a GLM-5.2 rate card ($0.095/$0.30 per 1M discount vs $0.95/$3.00 list). The Kimi family remains the flagship positioning below, but GLM-5.2 as a fourth family partially answers the Model Breadth LOSE verdict's "no frontier-class option" criticism.

---

## Source Inventory

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
| 1 | **Publicly accessible production endpoint** (api.gonka.ai) | Critical | L | Phase 15 gap, Phase 19 #6, Phase 20 TTFI Step 7 | Without a live endpoint, nothing else matters. v1.2 infrastructure exists but is not publicly deployed. Requires domain, SSL, health-checked routing, warm Kimi K2.6 (workhorse tier) model. |
| 2 | **Public documentation site** (docs.gonka.ai) | Critical | L | Phase 15 must-close gap #2, Phase 19 #7, Phase 20 TTFI Steps 1-2, Phase 18 P0 | Blocks the PLG funnel at Step 1 (Discover). Developers make provider decisions based on documentation quality. No docs = no evaluation. Minimum 10 pages: quickstart, API reference, OpenClaw integration guide, pricing, troubleshooting. |
| 3 | **Self-serve API key signup** (email-only) | Critical | L | Phase 15 must-close gap #3, Phase 19 #8, Phase 20 TTFI Steps 3-5, Phase 20 free tier | Blocks the PLG funnel at Step 3 (Sign Up). Email-only form, no wallet, no OAuth, no credit card. API key displayed immediately after email verification. Free tier limits activated automatically. Per CONTEXT.md locked decision. |
| 4 | **Published pricing page** | Critical | M | Phase 15 must-close gap #4, Phase 19 #9/#29, Phase 20 Explore stage | Blocks funnel conversion and competitive evaluation. Developers cannot estimate costs or compare against current-generation anchors -- K2.6 ($0.95/$4.00 official, DeepInfra $0.75/$3.50, Together $1.20/$4.50), K2.7-Code ($0.95/$4.00), K3 API ($3/$15) -- without published rates. Must include per-token rates for every model served (Qwen3 235B, Kimi tiers, MiniMax M2.7, GLM-5.2 when live) -- reseller Gonka24 already publishes its own Gonka rate card, so first-party pricing must exist to anchor it. |
| 5 | **OpenClaw community plugin** (npm) | Critical | XL | Phase 15 must-close gap #1, Phase 19 #15, Phase 18 P0 channel | Gonka is invisible to OpenClaw developers who use the 18+ default/built-in providers. The plugin (`openclaw-plugin-gonka` on npm) is the interim step toward built-in provider status (Tier 3) -- a path that now runs through the OpenClaw Foundation, where OpenAI is one of five published major donors and employs the project's creator. Blocks ClawHub integration and Tier 1-2 partnership validation. |
| 6 | **Persistent sessions** (Redis migration) | Critical | L | Phase 15 must-close gap #5, v1.2 tech debt, Phase 19 #12 | Session persistence is Gonka's #1 competitive advantage and the core of the 73% cost reduction claim (Feb 2026 estimate) -- and with model tiering now commoditized by ClawRouter-class routers, it is the *only* remaining infrastructure-level WIN. In-memory sessions are lost on restart -- first session loss event destroys developer trust permanently. Redis migration with TTL-based expiration and replication. |
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
| 18 | **Error messages overhaul** (actionable, no crypto terms) | Medium | M | Phase 17 vocabulary, Phase 20 free tier spec | All error messages must be actionable and specific. "Free tier daily limit reached. Resets at midnight UTC." not "Insufficient GNK balance." HTTP 429 responses must include reset time and upgrade URL. Follows never-say list for the human Web2 personas; note the agent-as-customer segment now expects x402/USDC payment rails (see Nice-to-Have notes). |

### Must-Ship Item Details

#### Must-Ship #1: Publicly Accessible Production Endpoint

- **Blocks:** Entire PLG funnel -- nothing works without a live API
- **Personas blocked:** All three (Weekend Builder, Startup CTO, Privacy-First Builder)
- **Definition of done:** `https://api.gonka.ai/v1/chat/completions` returns valid responses with sub-200ms TTFT. SSL certificate valid. Health check endpoint responds. Kimi K2.6 loaded and warm on minimum N nodes (K2.7-Code and K3 per model-tier roadmap; K3's 2.8T params roughly quadruple the memory footprint and need their own hardware sizing).
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

- **Blocks:** PLG funnel at Explore stage. Cost advantage claims are unverifiable without published rates. Current market anchors (Jul 2026): Kimi K2.6 $0.95/$4.00 official (DeepInfra $0.75/$3.50, Together $1.20/$4.50), K2.7-Code $0.95 input / $0.19 cache-hit / $4.00 output, Moonshot K3 API $3/$15. K2.5 rates are no longer valid anchors (Moonshot discontinued older kimi-k2-series API models May 25, 2026; Together delisted K2.5). DeepSeek V4 enters the comparison set with time-of-day pricing: V4-Pro ≈$0.42/$0.84 off-peak, ≈$0.84/$1.68 during Beijing peak hours; V4-Flash ¥1.00/¥2.00 regular.
- **Personas blocked:** Weekend Builder (cost comparison is #1 conversion driver), Startup CTO (needs to justify cost to co-founder)
- **Definition of done:** gonka.ai/pricing with per-token rates for each model served (Qwen3 235B, Kimi K2.6 workhorse / K2.7-Code / K3 frontier, MiniMax M2.7, GLM-5.2 when live). Comparison table against OpenRouter, Together AI, DeepInfra. Free tier limits clearly shown. Upgrade path from free to paid.
- **Dependencies:** Leadership decision on pricing. The Apr 2026 Scenario B recommendation ($0.35/$1.75, anchored to K2.5) needs re-basing on K2.6/K2.7-Code cost floors, since K2.5 is delisted and current-generation rates run materially higher ($0.75-$1.20 input). The comparison table should also exploit DeepSeek V4's peak-hour surcharge: flat, always-on Gonka pricing vs a rival whose rates double during Beijing business hours is a concrete, verifiable differentiator for 24/7 agent workloads.
- **Source:** Phase 15 (must-close gap #4), Phase 19 (requirements #9, #29: 1 week), Phase 20 (Explore stage conversion driver)

#### Must-Ship #5: OpenClaw Community Plugin (npm)

- **Blocks:** ClawHub integration, Tier 1-2 partnership validation. Gonka is invisible to developers who rely on built-in or plugin-based providers. The plugin is the interim step toward Tier 3 (built-in provider PR) -- now a submission to the OpenClaw Foundation (501(c)(3) formally launched July 8, 2026; OpenAI is one of five published major donors alongside Microsoft, NVIDIA, Offline Holdings, and University of Michigan, and employs the project's creator), a gatekeeper with a structural conflict of interest toward a rival inference network. Plan for a longer Tier 3 timeline and treat plugin + MCP as the durable distribution channels.
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
| 1 | **MCP server for agent extensions** (sessions, memory, tiering) | High (upgraded Jul 2026) | XL | Phase 19 #16 | Priority upgraded: MCP is now the de facto interop standard (~97M monthly SDK downloads, 9,652 servers in the official registry as of May 24, 2026 with third-party registries indexing 16,000-20,000, first-party support in ChatGPT, Gemini, Copilot, VS Code, Cursor). MCP is also neutrally governed -- donated to the Agentic AI Foundation under the Linux Foundation in Dec 2025 (Anthropic, OpenAI, Block) -- so it sidesteps OpenClaw Foundation gatekeeping entirely. A registry-listed Gonka MCP server is a primary distribution channel across every major agent host, not a ~500-LOC afterthought; list on the larger third-party registries (PulseMCP, mcp.so, Smithery) too, since the official registry is still pre-GA. Build against the MCP 2026-07-28 specification release candidate (final spec ships July 28, 2026; lead maintainers David Soria Parra and Den Delimarsky) rather than the prior revision -- it lands days after this document's revision date, with Tier-1 SDK support expected within ten weeks. Two RC changes matter directly for Gonka. (a) Stateless transport: remote MCP servers become load-balancer-friendly (no sticky sessions, routing on an `Mcp-Method` header, cacheable `tools/list`), so the Gonka server must expose its stateful sessions/memory as MCP tools over a stateless transport -- server-side state keyed by Gonka session ID, not MCP connection state. (b) The new Tasks primitive: a server can answer `tools/call` with a task handle the client drives via `tasks/get`/`tasks/update`/`tasks/cancel`, standardizing async execution across every MCP-capable agent stack. The Gonka server should target Tasks for async/long-running work -- and note this narrows the inference-layer-webhook differentiator claimed elsewhere in the research, beyond just OpenAI background mode. The RC also adds an Extensions framework, MCP Apps, authorization hardening, and a formal deprecation policy. Recommend pulling forward to start alongside Sprint 3. |
| 2 | **Quickstart repository** (GitHub template) | Medium | M | Phase 19 #17, Phase 20 TTFI | Pre-built template repo showing Gonka + OpenClaw integration. Reduces time-to-first-inference for developers who learn by cloning rather than reading docs. |
| 3 | **Integration guide on dev.to or Medium** | Medium | M | Phase 19 #20 | Content piece that doubles as P1 channel presence. Tutorial format showing real agent use case with Gonka. |
| 4 | **Cost comparison calculator** | Medium | M | Phase 19 #33, Phase 20 Weekend Builder conversion | Interactive calculator: input messages/day + heartbeat interval, output estimated monthly cost vs OpenRouter vs Together AI. Drives paid conversion by making savings concrete. |

### Within 60 Days of Launch

| # | Item | GTM Impact | Effort | Source | Timeline Rationale |
|---|------|-----------|--------|--------|-------------------|
| 5 | **ClawHub skill submission** (SKILL.md) | Medium | L | Phase 19 #22 | Teaches agents session/tiering/memory usage. Requires plugin to be stable first. Effort raised from M: after the ClawHavoc supply-chain campaign (Koi Security's Feb 1, 2026 audit found 341 of 2,857 skills malicious; Antiy CERT later confirmed 1,184 illicit skills total, and ClawHub removed ~2,419 suspicious skills, shrinking the registry from 5,705 to 3,286), ClawHub now scans every published skill via VirusTotal and the community is especially suspicious of skills touching API keys or anything crypto-adjacent. Budget for security review, provenance/signing, and a longer approval cycle. |
| 6 | **Video tutorial** ("OpenClaw + Gonka in 5 Minutes") | Medium | M | Phase 19 #21 | Visual learners. Production value matters -- low-quality video hurts more than no video. Wait until the flow is polished. |
| 7 | **Published benchmark results** (latency p50/p95, throughput) | Medium | M | Phase 19 #26 | Startup CTO needs performance data. Requires stable production environment to generate meaningful benchmarks. |
| 8 | **Non-Gonka PR contributions** to openclaw/openclaw | Medium | L | Phase 19 #23, Phase 18 P0 channel | 3-5 merged PRs build community trust before proposing built-in provider (3-6 month timeline per Phase 19, likely longer now that acceptance runs through the OpenClaw Foundation with OpenAI as a major donor; ~2,900 existing contributors raise the visibility bar). Bug fixes, docs improvements, test additions. |

### Within 90 Days of Launch

| # | Item | GTM Impact | Effort | Source | Timeline Rationale |
|---|------|-----------|--------|--------|-------------------|
| 9 | **Hashed API key storage** (DB migration from JSON) | Low | L | v1.2 tech debt, Phase 15 can-defer | Current JSON storage is acceptable for <100 keys. Must migrate before enterprise outreach or >100 active keys. Add key rotation and scoping. |
| 10 | **Vector embeddings for memory API** (replace TF-IDF) | Low | L | v1.2 tech debt, Phase 15 can-defer | TF-IDF search is functional but lower recall than vector-based. Quality gap becomes apparent when developers build sophisticated memory workflows. |
| 11 | **GPU load balancing** | Low | XL | v1.2 tech debt, Phase 15 can-defer | Single-node routing sufficient for launch (<10 concurrent users per node). Required before scaling beyond early adopter phase. |
| 12 | **Additional model support** (GLM-5.2 on landing; Kimi K2.7-Code now; Kimi K3 when open weights land, scheduled by Jul 27, 2026) | Medium (upgraded Jul 2026) | XL | Phase 15 can-defer (Model Breadth: LOSE) | The network already serves Qwen3 235B, Kimi K2.6, and MiniMax M2.7; GLM-5.2 is listed as coming soon (fourth family, 1M context, leads open agent benchmarks -- partially closes the Model Breadth LOSE). Within the flagship Kimi family, track the current generation, not K2.5: K2.6 workhorse, K2.7-Code for coding agents, K3 as frontier tier (2.8T MoE, 1M context; #1 in Frontend Code Arena at 1,679, ahead of Claude Fable 5 and GPT-5.6 Sol -- the first open model at the closed-frontier tier). Serving only K2.5 means serving a model two generations behind competitors. |
| 13 | **Developer usage dashboard** (web UI) | Low | XL | Phase 15 can-defer, Phase 20 Habitual Use stage | CLI/API stats sufficient for early adopter developers. Dashboard needed when non-technical team members need spend visibility. |
| 14 | **SLA documentation** with uptime commitments | Low | M | Phase 15 can-defer, Phase 19 #27 | No SLA until proven uptime. Publish transparent uptime statistics as interim. Formal SLA terms required before enterprise/startup outreach. |

### Nice-to-Have Item Notes

**New candidate (surfaced Jul 2026, not yet scoped): x402 agent payments.** Agent-native payment rails went mainstream between April and July 2026. The Linux Foundation declared the x402 Foundation operationally live July 14, 2026 with 40 member organizations across three tiers -- now including Visa, Mastercard, American Express, Stripe, Ripple, Google, AWS, Shopify, Cloudflare, and Coinbase. Volume is no longer test noise: over the 30 days ending ~July 15, 2026, x402 processed ~75M transactions moving ~$24M (~$800K/day, ~29 tx/sec) between ~94,000 buyers and ~22,000 sellers, predominantly sub-dollar USDC payments. Distribution is commoditizing at the edge: AWS shipped x402 support in CloudFront and AWS WAF (GA, late June 2026), and Cloudflare opened a waitlist for its Monetization Gateway (charge for pages, APIs, datasets, or MCP tools via x402 with stablecoin settlement) -- meaning an x402-gated Gonka inference endpoint becomes deployable behind commodity edge infra. BlockRunAI's ClawRouter already pays for OpenClaw inference via USDC micropayments over x402, occupying the "agent-native payments for OpenClaw" position. The email-only/API-key funnel stays correct for human personas, but Gonka -- already a crypto network -- has a natural x402 story for the agent-as-customer segment. Scope an x402 payment endpoint for the next backlog revision.

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

## Partnership Requirement Coverage

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

## Milestone Definition

### What "v1.4 Shipped" Means

**v1.4 is shipped when a developer can discover Gonka through documentation or the OpenClaw ecosystem, sign up with only an email address, receive an API key within 60 seconds, paste a pre-filled configuration snippet into their openclaw.json, and send their first inference request through Gonka's network -- all within 5 minutes, with sessions persisting across requests in Redis, pricing published and competitive with OpenRouter, Together AI, and DeepInfra on current-generation Kimi models, and the OpenClaw community plugin available on npm.**

Measurable criteria:

1. **api.gonka.ai** responds to `/v1/chat/completions` with sub-200ms TTFT and valid Kimi K2.6 inference
2. **docs.gonka.ai** is live with 10+ pages covering the complete developer journey
3. **Email-only signup** produces a working API key within 60 seconds of submission
4. **Pricing page** shows per-token rates for each model served with competitor comparison
5. **Sessions** are stored in Redis and survive server restarts with zero data loss
6. **`openclaw-plugin-gonka`** is published on npm and installable
7. **Time-to-first-inference** is under 5 minutes for a developer starting from docs.gonka.ai
8. **All 18 must-ship items** in this backlog are complete with passing verification

Items in the nice-to-have section are explicitly excluded from the v1.4 milestone. They improve the GTM experience but are not required for the "developer can go from zero to first inference" threshold. The nice-to-have items form the v1.4.x patch roadmap for the 90 days following v1.4 launch.

### What v1.4 Does NOT Include

- Model families beyond the current served lineup (Qwen3 235B, Kimi K2.6, MiniMax M2.7, plus GLM-5.2 on landing); Kimi remains the flagship positioning, with K2.7-Code and K3 per Nice-to-Have #12
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
| **gonka_competitive_feature_matrix.md** | Phase 15 | WIN verdicts (Agent Sessions, Model Tiering) confirming which features to lead with. Note (Jul 2026): the Model Tiering WIN no longer holds -- routing is commoditized by ClawRouter-class routers; Agent Sessions is the remaining WIN to lead with. LOSE verdicts (Uptime/Reliability, Model Breadth) identifying weaknesses to mitigate or defer; Model Breadth is partially mitigated as of Jul 2026 by GLM-5.2 joining the network as a fourth family. |
| **gonka_developer_personas.md** | Phase 16 | Three personas with distinct feature needs at each AAARRRP stage. Weekend Builder: cost-driven, needs zero-friction signup. Startup CTO: reliability-driven, needs status page and team accounts. Privacy-First Builder: privacy-driven, needs honest capabilities page. Per-persona drop-off risks informing must-ship vs nice-to-have classification. |
| **gonka_message_house.md** | Phase 17 | 16-item never-say list enforced in error messages and landing page design. VP1 (73% cost reduction, Feb 2026 estimate -- re-verify against Jul 2026 pricing) as the lead message requiring persistent sessions to be credible. Landing page design requirements (resembles Vercel/Supabase, not DeFi). Note: message house's K2.5 benchmark claims are stale (open-weight agent-benchmark leaders are now MiniMax M2.7 and GLM-5.2). |
| **gonka_channel_strategy.md** | Phase 18 | P0 channel prerequisites (docs site, Discord presence, GitHub PRs). 70/30 channel split confirming developer channels (70%) take priority. Primary KPI (API-active developers >100 calls/month) informing free tier limits and upgrade triggers. |
| **gonka_partnership_playbook.md** | Phase 19 | 28 NEEDED technical requirements with effort estimates and tier assignments. Four-tier integration roadmap defining the path from Listed (Tier 1) to Preferred Partner (Tier 4). Community-first PR strategy timeline (3-6 months). ClawHub submission requirements. |
| **gonka_plg_growth_model.md** | Phase 20 | PLG funnel stages with conversion rates. Free tier design spec (15M tokens/month, 1000 req/day, 2 sessions, email-only). Time-to-first-inference plan (7 steps, 4m15s target). Atomic growth unit (openclaw.json config snippet). Upgrade trigger mechanisms (X-Gonka-Usage-Remaining headers). Failure mode analysis for each TTFI step. |
| **PROJECT.md** | v1.2 | 4 tech debt items: TF-IDF search (needs vector embeddings), in-memory sessions (needs Redis), JSON key storage (needs DB), no GPU load balancing. |

---

*Document: gonka_v14_engineering_backlog.md | Version 1.3 | 2026-07-18*
*Capstone deliverable for Phases 15-20. Companion document: gonka_plg_growth_model.md (PLG funnel, free tier spec, time-to-first-inference plan)*

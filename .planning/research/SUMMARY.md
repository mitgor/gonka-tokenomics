# Project Research Summary

**Project:** Gonka Network v1.3 -- OpenClaw Go-To-Market Strategy
**Domain:** B2D go-to-market strategy for decentralized AI inference targeting OpenClaw agent developers
**Researched:** 2026-04-01
**Confidence:** MEDIUM (GTM strategy inherently hypothesis-driven; OpenClaw technical facts HIGH)

## Executive Summary

Gonka v1.3 is a research-and-strategy milestone, not an engineering milestone. The goal is to produce actionable GTM documents that position Gonka.ai as the inference provider of choice for OpenClaw developers -- the 250K+ GitHub star ecosystem of self-hosted AI agent gateways. Gonka already has the right technical foundation from v1.2: OpenAI-compatible `/v1/chat/completions`, vLLM serving of Kimi K2.5, session persistence, auto-tiering, memory API, webhooks, and integration tests against OpenClaw. The gap is go-to-market, not product. The strategic opportunity is to claim the "agent-native inference" positioning before centralized providers add agent features or other decentralized networks build compatible APIs.

The recommended approach is a research-first, build-second strategy: produce six interlocking GTM documents (competitive analysis, developer personas, positioning/messaging, channel strategy, partnership roadmap, product-led growth plan) in a sequence where each informs the next. The most critical decision in this milestone is vocabulary: Gonka must lead with developer outcomes (cost, reliability, agent features) and frame decentralization as the mechanism, never the headline. The target audience is Web2-native OpenClaw builders, not crypto-native token holders. Every piece of content, every doc page, and every error message must pass the test "would a developer who has never heard of blockchain understand this?"

The primary risks are: (1) crypto-first messaging that alienates the mainstream OpenClaw developer audience, (2) unreliable inference that damages trust on first contact and takes 3-6 months to repair, and (3) missing the ecosystem formation window -- OpenClaw's integration defaults are being set NOW as the project hits 250K stars, and being absent from ClawHub and the provider directory means being permanently behind entrenched defaults. The single most time-sensitive action is submitting a Gonka provider listing to ClawHub and OpenClaw's community documentation before competitors occupy that position.

---

## Key Findings

### Recommended Stack

v1.3 produces documents, not software. The "stack" is research tooling: Markdown for all strategy documents (consistent with repo convention), openpyxl 3.1.5 for a competitive pricing tracker workbook (reusing the v1.1 stack), and Python 3.10+ if pricing analysis scripts are needed. No new dependencies are required.

The GTM documents must be informed by deep knowledge of OpenClaw's technical architecture. OpenClaw uses a declarative `openclaw.json` config with a two-step provider registration (define provider + allowlist models). Gonka already satisfies both API format requirements (`openai-completions`). The OpenClaw plugin system supports TypeScript plugins and ClawHub Markdown skills -- both are distribution vectors for Gonka adoption in a future engineering milestone (v1.4 candidate).

**Core technologies:**
- **Markdown**: All GTM research documents -- repo-native format, reviewable via GitHub
- **openpyxl 3.1.5**: Competitive pricing tracker workbook -- reuses v1.1 stack, portable .xlsx
- **OpenClaw `openclaw.json` config pattern**: The copy-paste provider config snippet is the "product" in Gonka's PLG motion -- every doc must include it

**Key technical facts verified (HIGH confidence):**
- OpenClaw: 250K+ stars, 1,075 contributors, 124K LOC, launched Jan 25 2026 (~3 months old)
- Built-in providers: ~20 (OpenRouter, OpenAI, Anthropic, Groq, Together, Ollama, vLLM, etc.)
- Gonka is NOT a built-in provider -- requires manual JSON config (friction + opportunity)
- Two API formats supported: `openai-completions` and `anthropic-messages` -- Gonka uses the former (already shipped)
- Gonka capabilities already built in v1.2: sessions, tiering, memory, webhooks, tool calling, multi-model routing

### Expected Features

Features are categorized by what OpenClaw developers actually need vs what would be premature to build.

**Must have (table stakes -- blockers for any GTM push):**
- OpenAI-compatible `/v1/chat/completions` and `/v1/models` endpoints -- BUILT (v1.2)
- Tool calling support (vLLM `--enable-auto-tool-choice` + `--tool-call-parser` flags) -- BUILT
- Streaming SSE responses -- BUILT
- API key authentication -- BUILT
- OpenAI-format error responses -- BUILT
- Provider documentation page (baseUrl, model IDs, capabilities, pricing, OpenClaw config snippet) -- NOT BUILT (critical gap)
- Self-serve API key signup (email + API key in under 2 minutes) -- NOT BUILT (critical gap)
- Developer usage visibility (spend, limits, error rates) -- PARTIAL (admin API exists, no developer-facing UI)
- At least 2-3 model options (K2.5-only is too narrow for multi-model workflows) -- NOT BUILT (gap)

**Should have (differentiators that motivate switching from OpenRouter):**
- Agent cost optimizer via auto-tiering (heartbeats to cheap model, reasoning to strong model) -- BUILT, undermarketed
- Session persistence (server-side context, eliminates re-sending full history) -- BUILT, undermarketed
- OpenClaw provider plugin for ClawHub (one-click setup, no manual JSON) -- NOT BUILT (high-value)
- Cost comparison calculator ("Your OpenClaw bill with OpenRouter vs Gonka") -- NOT BUILT
- Flat-rate or agent-specific pricing plans -- NOT BUILT (pricing strategy decision)
- GNK token payment with discount (20-30% off for paying in GNK) -- NOT BUILT (requires smart contracts; v2 candidate)

**Defer to v2+:**
- Vector-based memory (currently TF-IDF -- tech debt from v1.2; noticeable quality gap vs competitors)
- Open model marketplace (competing with OpenRouter's 290+ models is an unwinnable race; focus on depth not breadth)
- Privacy-preserving inference via TEE (requires confidential computing research)
- Agent swarm network parallelization (K2.5 native capability exists; network-level execution is complex)
- Earn-while-you-infer for OpenClaw developers with GPUs (requires full network integration)

**Never build (anti-features for this GTM stage):**
- Matching OpenRouter on model catalog breadth -- unwinnable race; position on depth instead
- Free tier with rate-limited/degraded models -- attracts price-sensitive non-converting users
- Web playground UI -- OpenClaw devs use CLI/API exclusively; curl quickstart is sufficient
- Fine-tuning service -- different product entirely
- Enterprise SSO/SAML -- wrong audience for early GTM

### Architecture Approach

The GTM research architecture has six interlocking components with explicit dependencies: Competitive Analysis feeds Positioning & Messaging, which feeds Channel Strategy and Content Strategy; Developer Personas feed Positioning, Channel Strategy, and Partnership Strategy; all six components converge into a Product-Led Growth plan. The research execution order must respect this dependency graph -- competitive analysis first, personas second, positioning third, channel fourth, partnership fifth, PLG sixth.

The architecture-to-message mapping table is the critical bridge between Gonka's technical reality and its marketing. Each technical feature must translate to a developer-facing benefit statement: "X-Gonka-Session-ID" becomes "your agent remembers context without paying for it twice"; "X-Gonka-Tier header" becomes "classification on the cheap model, reasoning on the strong one -- automatically"; "Sprint Consensus = 98% productive compute" becomes "every GPU cycle serves your requests, not mining puzzles."

**Major GTM research components:**
1. **Competitive Analysis** -- Market segmentation across four categories (centralized API, multi-provider routers, dedicated inference, decentralized GPU) and deep teardowns of OpenRouter (primary), Together AI, Groq, Akash
2. **Developer Persona & Journey** -- Three personas (OpenClaw Builder, Agent Framework Developer, AI Startup) mapped through AAARRRP stages with objection handling per stage
3. **Positioning & Messaging** -- Architecture-to-message table, USP ranking, vocabulary guidelines (crypto-free developer language), objection playbook
4. **Channel Strategy** -- P0: OpenClaw provider directory, GitHub, Discord; P1: technical blog, Twitter/X, Reddit r/LocalLLaMA; P2-P3: video, HackerNews, conferences (70/30 split: AI/developer vs crypto channels)
5. **Partnership Strategy** -- Four integration tiers: Listed Provider (immediate) -> Community Plugin (v1.4) -> Built-In Provider (medium-term) -> Preferred Partner (long-term)
6. **Product-Led Growth** -- Time-to-first-inference under 5 minutes as north star, free tier design principles, copy-paste OpenClaw config snippet as atomic growth unit

### Critical Pitfalls

1. **Leading with decentralization instead of developer experience** -- The OpenClaw audience is Web2-native. "Decentralized" alienates 99%+ of them before they see the value. Lead every piece of messaging with developer outcomes (cost savings, agent features, reliability); frame decentralization as the mechanism that delivers those outcomes, never the headline. The Gonka.ai website should look like Vercel or Supabase, not a DeFi protocol.

2. **Requiring crypto knowledge for basic usage** -- API key auth is already correct (v1.2). Accept Stripe/card payments alongside GNK discounts. Abstract all blockchain interactions behind the API gateway -- developers should never see a transaction hash unless they opt in. Target: under 5 minutes from email to first API response, no wallet required.

3. **Unreliable inference damaging trust on first contact** -- Decentralized compute networks are inherently more variable than centralized ones. First impressions are permanent -- OpenRouter and OpenAI have set the bar at sub-1-second TTFT with 99.9%+ uptime. Curate a premium verified-node tier for first-time users. Over-provision capacity in early days even at a loss. Publish real-time uptime stats. Reliability reputation takes 3-6 months to rebuild once damaged.

4. **Missing the OpenClaw ecosystem formation window** -- OpenClaw hit 250K stars in ~60 days. Integration defaults are being set right now, and late entrants face entrenched defaults requiring 3-5x the effort to displace. Submit a Gonka provider listing to ClawHub immediately, in parallel with any other GTM work. This is the single most time-critical action in v1.3.

5. **Competing on price alone in a race to the bottom** -- Every DePIN network claims "60-80% cheaper than AWS." Price is not a differentiator when all decentralized networks share the same structural cost advantage. Build positioning around OpenClaw-specific agent features (sessions, tiering, memory, webhooks) that centralized providers don't have and other decentralized networks haven't built. Ensure unit economics are profitable without token emission subsidies within 12 months.

6. **Community theater instead of developer adoption** -- Web3 marketing playbooks optimize for Discord members and airdrop hunters; real developer adoption is slow and unglamorous. Success metrics must be API-active developers (>100 calls/month), not follower counts. Build developer community on GitHub where OpenClaw developers already live. Target ratio: >1 API-active developer per 10 Discord members.

---

## Implications for Roadmap

The v1.3 GTM research should be structured as six sequential-but-overlapping phases. Earlier phases produce artifacts that later phases consume. All six phases together produce a prioritized engineering backlog that v1.4 executes.

### Phase 1: Competitive Analysis & Market Mapping
**Rationale:** Cannot position without knowing the field. All downstream GTM work references the feature comparison matrix and pricing analysis produced here. Must come first.
**Delivers:** Market segmentation map (four-category), per-competitor teardowns (OpenRouter, Together AI, Groq, Akash), feature comparison matrix (Gonka vs field), competitive pricing workbook (openpyxl)
**Addresses:** Feature gap identification (what to close before GTM vs what to defer); pricing strategy inputs (sustainable vs subsidy-dependent unit economics)
**Avoids:** Pitfall 4 (price-only positioning) -- analysis reveals where feature differentiation wins; ensures competitive set is accurate (OpenRouter, not just other DePIN networks)
**Research flag:** NEEDS RESEARCH -- pricing data moves weekly; competitor features change monthly; requires fresh data pull at execution time

### Phase 2: Developer Persona & Journey Mapping
**Rationale:** Cannot craft messages or select channels without knowing the audience. Persona definitions unblock all downstream messaging and channel work.
**Delivers:** Three persona cards (OpenClaw Builder, Agent Framework Developer, AI Startup), AAARRRP journey maps per persona, decision driver ranking, objection map per stage
**Addresses:** Developer decision criteria table from FEATURES.md -- personas explain the "why" behind each ranking; validates that the five messaging themes resonate with actual developer pain
**Avoids:** Pitfall 1 (crypto-first messaging) -- persona research confirms Web2-native audience; Pitfall 6 (ignoring OpenClaw ecosystem dynamics) -- persona journey maps the full ecosystem decision flow
**Research flag:** NEEDS RESEARCH -- developer decision criteria should be validated against live community signals (GitHub issues, Discord, Reddit r/LocalLLaMA) at execution time; confidence is currently MEDIUM

### Phase 3: Positioning & Messaging
**Rationale:** Synthesizes competitive analysis and personas into a message house. Must precede any content creation or channel work -- messaging frames every downstream artifact.
**Delivers:** Value proposition canvas, full architecture-to-message mapping table, USP ranking (5 ranked USPs), vocabulary guidelines (developer-facing vs internal crypto terminology), objection handling playbook, competitive differentiation statements per persona
**Addresses:** Five messaging themes from FEATURES.md; anti-patterns from ARCHITECTURE.md (feature-led messaging, crypto-first positioning, comparing to everyone)
**Avoids:** Pitfall 1 (leading with decentralization), Pitfall 7 (crypto jargon) -- vocabulary guidelines are a direct deliverable; all future content creation requires sign-off against these guidelines
**Research flag:** STANDARD PATTERNS -- message house creation is well-documented B2D practice; architecture-to-message mapping is internal synthesis work, not external research

### Phase 4: Channel Strategy & Community Playbook
**Rationale:** Uses personas and messaging to determine where and how to reach developers. Channel selection without persona clarity and message alignment is guesswork.
**Delivers:** Channel matrix with priority tiers (P0/P1/P2/P3), content calendar framework with journey-stage mapping, community engagement playbook, success metrics definition (API-active developers as primary KPI, not followers)
**Addresses:** ARCHITECTURE.md channel matrix and content strategy framework; FEATURES.md feature dependency tree (documentation and signup must exist before channel strategy can execute)
**Avoids:** Pitfall 5 (community theater) -- explicit metric: API-active developers, not Discord members; 70/30 budget split: AI/developer channels vs crypto channels
**Research flag:** STANDARD PATTERNS -- channel matrix and content frameworks are established B2D marketing patterns; channel priority is a judgment call informed by personas

### Phase 5: Partnership & Ecosystem Strategy
**Rationale:** OpenClaw ecosystem integration window is time-critical. Partnership strategy must be defined before execution, and engineering priorities for v1.4 (MCP plugin, built-in provider PR) depend on this output. Note: ClawHub submission itself should run in PARALLEL with earlier phases due to time urgency.
**Delivers:** Four-tier OpenClaw integration roadmap with prerequisites per tier, ClawHub submission plan and content, built-in provider PR strategy, technical partnership requirements checklist
**Addresses:** STACK.md GTM engineering artifacts table (Gonka provider plugin, ClawHub skill, openclaw.json template, integration guide); ARCHITECTURE.md partnership tier definitions
**Avoids:** Pitfall 6 (missing OpenClaw ecosystem formation window) -- ClawHub submission is a direct output; includes sequencing guidance (ship working integration first, then approach for official partnership)
**Research flag:** NEEDS RESEARCH -- ClawHub submission requirements and current registry state need verification; OpenClaw maintainer PR acceptance process requires community intelligence

### Phase 6: Product-Led Growth Plan & v1.4 Engineering Backlog
**Rationale:** Synthesizes all five preceding phases into an actionable growth model with metrics, plus a prioritized engineering backlog for v1.4. Capstone deliverable of the milestone.
**Delivers:** PLG model with funnel stages and metrics (GitHub star -> docs -> API key -> first call -> 100th call -> paid), free tier design spec, time-to-first-inference optimization plan (5-minute target), developer onboarding flow, prioritized v1.4 engineering backlog ranked by GTM impact
**Addresses:** FEATURES.md MVP recommendation (five must-haves before any marketing push); ARCHITECTURE.md PLG architecture (copy-paste config snippet as atomic growth unit, TTFI north star)
**Avoids:** Pitfall 4 anti-pattern (building before positioning) -- engineering backlog is produced AFTER research identifies what actually matters; Pitfall 2 (crypto knowledge required) -- free tier design specs email-only signup
**Research flag:** STANDARD PATTERNS -- PLG metrics and funnel design are established SaaS/B2D patterns; engineering backlog prioritization is internal decision informed by prior five phases

### Phase Ordering Rationale

- Competitive analysis precedes positioning: cannot position against an unknown field
- Personas precede channel strategy: cannot select channels without knowing audience location and decision behavior
- Positioning precedes all content creation: messaging frames every downstream artifact; content created without a message house will need to be rewritten
- Partnership strategy should begin in parallel with Phase 3-4 due to ecosystem window urgency: at minimum, ClawHub submission and basic OpenClaw config template can be prepared immediately since technical facts are known
- PLG plan comes last because it synthesizes all inputs, but the copy-paste OpenClaw config snippet (the core PLG artifact) can be drafted as early as Phase 1 since it depends only on technical facts already verified

### Research Flags

**Needs fresh research at execution time:**
- Phase 1 (Competitive Analysis): Pricing data moves weekly; competitor feature sets change monthly
- Phase 2 (Developer Personas): Community signal validation required against current Discord/GitHub/Reddit state
- Phase 5 (Partnership Strategy): ClawHub registry state and OpenClaw maintainer PR process need current verification

**Standard patterns (research optional):**
- Phase 3 (Positioning & Messaging): B2D message house is well-documented; work is internal synthesis
- Phase 4 (Channel Strategy): Channel matrix frameworks established; priority ranking is judgment call
- Phase 6 (PLG Plan): SaaS/B2D PLG patterns well-documented; backlog prioritization is internal

---

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH (OpenClaw technical) / MEDIUM (GTM tooling) | OpenClaw architecture verified against official docs and GitHub source; GTM tooling is straightforward reuse of v1.1 stack; no new dependencies needed |
| Features | HIGH (table stakes) / MEDIUM (differentiator impact) | Table stakes derived from OpenClaw official docs (provider config requirements); differentiator ranking from community pain points, not A/B tested with actual developers |
| Architecture | MEDIUM | GTM document architecture is inherently hypothesis-driven; technical Gonka components verified against v1.2 codebase; competitive landscape verified against current sources |
| Pitfalls | MEDIUM-HIGH | Multiple sources corroborate DePIN failure patterns; Akash/io.net/Render case studies provide strong evidence; OpenClaw-specific ecosystem dynamics are newer and less validated |

**Overall confidence:** MEDIUM

The research is sufficient to produce the six GTM documents described above. The primary uncertainty is developer response to specific messaging angles and actual cost savings in production OpenClaw workloads -- both require real developer interactions to validate. The research identifies what hypotheses to test, not pre-validated conclusions.

### Gaps to Address

- **Gonka pricing not finalized:** STACK.md shows Kimi K2.5 target pricing as TBD. The "cut your bill 70%" messaging cannot be validated until actual per-token pricing is set and compared against OpenRouter. Pricing finalization is a Phase 1 output, not an input.
- **Reliability metrics unproven at scale:** The "unreliable inference" pitfall cannot be fully addressed without published uptime data. GTM marketing push should be gated on demonstrated >99.5% uptime over a 30-day baseline.
- **Developer messaging unvalidated:** All five messaging themes (cost, agent-native, censorship-free, K2.5 benchmarks, earn-while-you-infer) are hypotheses derived from community pain points -- none A/B tested. Phase 2 persona work should include structured outreach to 5-10 real OpenClaw builders before scaling content creation.
- **OpenClaw version compatibility:** OpenClaw is evolving rapidly (250K stars in ~3 months). Integration guides must be pinned to a specific OpenClaw version and tested against new releases. PITFALLS.md flags silent breakage from version drift as a known failure mode.
- **GNK token payments scope boundary:** GNK token payments (20-30% discount) are flagged as a Tier 2 differentiator requiring smart contracts and payment rails. v1.3 must define which future milestone introduces this feature and what the rollout sequence looks like.

---

## Sources

### Primary (HIGH confidence -- official documentation)
- [OpenClaw Model Providers -- Official Docs](https://docs.openclaw.ai/concepts/model-providers) -- provider config two-step, API formats
- [OpenClaw Plugin System -- Official Docs](https://docs.openclaw.ai/tools/plugin) -- plugin vs skill distinction, ClawHub
- [OpenClaw GitHub Repository](https://github.com/openclaw/openclaw) -- 250K+ stars, built-in provider list, AGENTS.md
- [OpenRouter Pricing](https://openrouter.ai/pricing) -- 5.5% credit markup, per-token pass-through, 290+ models
- [Kimi K2.5 ArXiv](https://arxiv.org/html/2602.02276v1) -- 76.8% SWE-Bench Verified, technical benchmarks
- Gonka v1.2 codebase (gateway, sessions, tiering, memory, webhooks) -- verified against source

### Secondary (MEDIUM confidence -- multiple sources agree)
- [OpenClaw 250K Stars Milestone Blog](https://openclaws.io/blog/openclaw-250k-stars-milestone)
- [Kimi K2.5 Tech Blog](https://www.kimi.com/blog/kimi-k2-5) -- Agent Swarm, 200-300 sequential tool calls
- [LangChain State of Agent Engineering](https://www.langchain.com/state-of-agent-engineering) -- 76% multi-model usage
- [Haimaker Custom LLM Provider Setup](https://haimaker.ai/blog/integrating-custom-llm-providers-with-clawdbot/) -- two-step config walkthrough
- [OpenRouter Free API Changes 2026](https://www.marketingscoop.com/developer/openrouter-free-api-explained-what-it-is-what-changed-in-2026-and-the-tradeoffs-before-you-build-on-it/) -- free tier degradation, 20 RPM/200 RPD limits
- [Decentralized Compute Pricing](https://cryptonium.cloud/articles/decentralized-ai-compute-data-infrastructure-2026) -- 60-80% cheaper claim
- [io.net vs Akash vs Render](https://io.net/blog/io-net-vs-akash-vs-render-network-which-decentralized-platform-actually-delivers) -- DePIN reliability case studies
- [Akash 2025 Year in Review](https://akash.network/blog/akash-2025-year-in-review/) -- provider attrition lessons
- [OpenClaw Pricing Guide](https://www.thecaio.ai/blog/openclaw-pricing-guide) -- $5-300+/month typical cost range
- [Brian Gershon: Avoiding Runaway OpenClaw Costs](https://www.briangershon.com/blog/openclaw-avoid-runaway-api-costs) -- heartbeat cost pattern
- [developerrelations.com AAARRRP Framework](https://developerrelations.com/guides/mapping-the-developer-journey/)
- [Web3 Startup Failure Patterns](https://hackernoon.com/why-web3-projects-fail-with-growth-marketing-3-fundamental-mistakes) -- crypto-first messaging failure mode

### Tertiary (LOW confidence -- single source or inference)
- Gonka compute cost advantage of 50-70% (Gonka's own marketing claims; not independently verified)
- OpenClaw Discord server size and activity levels (inferred from documentation; not directly measured)
- Developer response to specific Gonka messaging themes (hypothesis from community pain points; not A/B tested)

---
*Research completed: 2026-04-01*
*Ready for roadmap: yes*

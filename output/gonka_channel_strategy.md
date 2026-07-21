# Gonka Channel Strategy: Reaching OpenClaw Developers

**Version:** 1.3
**Date:** 2026-07-18 (revised from 2026-04-01 original; model references, ecosystem data, and channel facts re-verified against live sources as of 2026-07-18)
**Classification:** Internal -- canonical channel strategy for all Gonka developer acquisition efforts
**Dependencies:** Phase 16 developer personas (gonka_developer_personas.md), Phase 17 messaging (gonka_message_house.md, gonka_objection_playbook.md)
**Requirement:** GTM-01

---

## Executive Summary

This document defines where, how, and how often Gonka communicates with OpenClaw developers to drive adoption of Gonka as their inference provider. It is the operational companion to the message house (what to say) and developer personas (who to say it to).

Key decisions:

- **Primary KPI: API-active developers (>100 API calls/month). Not follower counts. Not Discord members. Not GitHub stars.** A developer who makes 100+ calls/month has integrated Gonka into a real workflow -- they are retained, generating revenue, and likely to refer others. Every metric below ladders up to this number.
- **70/30 channel split:** 70% of P0+P1 channel investment targets AI/developer communities where OpenClaw builders already spend time; 30% targets crypto-native channels where GPU hosts and token holders live. Developer adoption drives network value; crypto channels support the supply side.
- **P0 channels are ecosystem channels:** OpenClaw GitHub, OpenClaw Discord, and the OpenClaw provider directory are where the target developers already are. Gonka must be present where developers make provider decisions, not where Gonka wishes they were.
- **Content leads with heartbeat cost reduction (73%)** per the Phase 17 message house positioning, not decentralization or token economics.
- **Anti-metrics are explicitly tracked** to prevent vanity metric theater from replacing adoption measurement.
- **A third-party broker/gateway retail layer now fronts developer access** (GonkaBroker, GonkaGate, JoinGonka, OpenGNK, gonka.to) with fixed-USD pricing. Treat these as distribution partners and attribution sources, and keep Gonka's own cost claims consistent with their published rates.
- **Security-first posture in all OpenClaw channels.** The early-2026 ClawHavoc supply-chain attack (1,184 malicious ClawHub skills per Antiy CERT -- characterized in current security write-ups as roughly one in five packages in the ecosystem at time of discovery -- ~247K confirmed installs, ~$2.3M in reported crypto theft, payloads including Atomic macOS Stealer and VMProtect-packed Windows infostealers; Koi Security's initial Feb 1, 2026 audit found 341 malicious skills, later revised upward to 824 before Antiy CERT's fuller 1,184+ count) plus the Clawdbot→Moltbot→OpenClaw rename churn left the community applying crypto-scam-level scrutiny to any new OpenClaw-adjacent tool -- especially anything crypto-adjacent. And the problem is not contained: despite ClawHub's VirusTotal/ClawScan integration, Unit 42's Feb-May 2026 analysis found malicious skills persistent and actively evading scanning (including a Base64 curl-pipe-bash dropper padded with 22 MB of filler to exceed content-analysis size limits). Every Gonka touchpoint in these channels must lead with provenance, open source, and verifiable claims -- a signed, provenance-verified Gonka skill/MCP listing is a trust asset precisely because registry scanning alone is demonstrably insufficient.

---

## Metrics Framework

### Primary KPI: API-Active Developers

**Definition:** Developers who make >100 API calls per month through the Gonka inference gateway.

**Why this metric:** 100 calls/month indicates a developer has moved past tire-kicking and integrated Gonka into a recurring workflow -- an always-on agent, a production service, or an active development project. Below 100 calls, the developer is likely testing or has abandoned the integration. Above 100, they are generating real usage, experiencing session persistence savings, and building switching costs that drive retention.

**Target trajectory:**
- Month 1 (launch): 10 API-active developers
- Month 3: 50 API-active developers
- Month 6: 200 API-active developers
- Month 12: 1,000 API-active developers

### Secondary KPIs

| Metric | What It Measures | AAARRRP Stage | Target |
|--------|-----------------|---------------|--------|
| API key signups per week | Acquisition velocity | Acquisition | 50+/week by Month 3 |
| First-call-within-24h rate | Activation friction | Activation | >60% of signups |
| Week-2+ retention rate | Stickiness after trial | Retention | >40% of activated users |
| Session creation rate | Agent-native feature adoption | Activation | >30% of active developers use sessions |
| Cost savings per developer | Value delivery proof | Retention | >50% reduction vs prior provider |

### Anti-Metrics (Vanity Metrics to Avoid)

These metrics feel good but do not predict developer adoption. Track them for context but never use them as success indicators or in leadership reports as evidence of traction.

| Vanity Metric | Why It Misleads | What to Track Instead |
|---------------|----------------|----------------------|
| Twitter/X follower count | Followers do not make API calls; bots inflate counts; followers on AI Twitter skew crypto-native, not developer-native | Referral traffic from Twitter to docs.gonka.ai that converts to API key signups |
| Discord member count | Most Discord members never interact; lurkers inflate numbers; "join our Discord" campaigns produce dead weight | Active Discord participants who also have API keys (cross-reference) |
| GitHub stars on gonka-ai-infrastructure | Stars are a one-click action that does not indicate usage; many stars come from crypto speculators, not developers | GitHub issues and PRs from developers who reference their Gonka integration |
| Blog post impressions | Impressions measure distribution, not interest; a developer who reads the headline and bounces is not a prospect | Blog-to-signup conversion rate (readers who create API keys within 7 days) |
| Newsletter subscribers | Subscribing is passive; most subscribers never open emails | Newsletter-to-activation rate (subscribers who make their first API call after a newsletter) |
| Conference badge scans | Badge scans measure foot traffic, not intent; most conference leads never follow up | Conference-to-API-key conversion rate within 30 days |

---

## Channel Matrix

Summary of all channels with priority tiers, personas, and success metrics.

| Channel | Priority | Primary Persona | Content Type | Cadence | Expected Reach | Success Metric | 70/30 Category |
|---------|----------|----------------|-------------|---------|---------------|----------------|---------------|
| OpenClaw Provider Directory | P0 | All | Provider listing, config docs | Always available | Direct to all OpenClaw users | Listed provider status; config page views | AI/Dev |
| OpenClaw GitHub (issues, discussions, PRs) | P0 | Weekend Builder, Startup CTO | PRs, issue responses, discussion posts | Daily monitoring | Direct to active OpenClaw contributors | Mentions in issues; PR for built-in support merged | AI/Dev |
| OpenClaw Discord | P0 | Weekend Builder | Help answers, config snippets, presence | Daily | Direct to active OpenClaw community | API key signups attributed to Discord | AI/Dev |
| MCP Registry (Gonka MCP server listing) | P1 | Startup CTO, Weekend Builder | MCP server + registry listing, integration docs | Always available | All major agent hosts (ChatGPT, Gemini, Copilot, VS Code, Cursor) | Registry-listing-to-signup conversion; MCP-originated API keys | AI/Dev |
| Technical Blog (docs.gonka.ai/blog) | P1 | Startup CTO | Tutorials, benchmarks, comparisons | Weekly | SEO + social sharing | Blog-to-signup conversion rate | AI/Dev |
| Twitter/X AI Developer Community | P1 | All | Benchmark results, cost comparisons, launch posts | 3-5x/week | Broad AI dev audience | Referral traffic to docs.gonka.ai | AI/Dev |
| Reddit (r/LocalLLaMA, r/OpenClaw) | P1 | Weekend Builder | Comparison posts, launch threads, help responses | 2-3x/week | Engaged AI dev community | Upvotes + API key signups from Reddit referrals | AI/Dev |
| dev.to / Hashnode | P1 | Weekend Builder | Cross-posted tutorials, quickstart guides | Bi-weekly | Developer blog aggregator audience | Cross-post-to-signup conversion rate | AI/Dev |
| YouTube Tutorials | P2 | Weekend Builder | "OpenClaw + Gonka in 5 Minutes" video guides | Bi-weekly | Medium (tutorial seekers) | View-to-signup conversion rate | AI/Dev |
| HackerNews | P2 | Startup CTO | Show HN posts, deep-dive articles | Monthly (when content warrants) | Tech-savvy early adopters | HN-to-signup conversion rate | AI/Dev |
| Crypto Twitter / DePIN Communities | P2 | Privacy-First Builder | Network updates, host earnings, ecosystem growth | 2-3x/week | Crypto-native GPU hosts, token holders | GPU host signups; token holder engagement | Crypto |
| Privacy-Focused Forums (Lobsters, security subreddits) | P2 | Privacy-First Builder | Privacy architecture deep-dives, audit results | Monthly | Security/privacy dev community | Privacy-page views; signups from privacy referrals | AI/Dev |
| AI/Web3 Conferences | P3 | Startup CTO | Talks, demos, booths | Quarterly | Targeted but expensive | Conference-to-API-key conversion within 30 days | Crypto |
| Paid Developer Ads (Carbon, BuySellAds) | P3 | All | Targeted ads on AI infra keywords | Continuous when budget allows | Broad but noisy | Cost per API key signup (target: <$25 CAC) | AI/Dev |
| DePIN / Web3 Dev Forums | P3 | Privacy-First Builder | Host onboarding guides, token utility explainers | Weekly | Crypto-native developers | Host signup conversion rate | Crypto |

---

## P0 Channels

P0 channels are where OpenClaw developers already make provider decisions. Gonka must be present in these channels before investing anywhere else. Zero awareness (developer personas: universal blocker #1) is solved here, not on Twitter or at conferences.

---

### OpenClaw Provider Directory

**Platform:** OpenClaw documentation site / provider configuration docs
**URL:** docs.openclaw.ai

**Why P0:** The provider directory is where developers go when they decide to add, change, or evaluate inference providers. If Gonka is not listed with a working configuration snippet, it does not exist to the OpenClaw developer. This is the single highest-leverage channel -- zero marginal cost, permanent presence, direct access to the moment of provider decision.

**Primary persona(s):** All three personas. Every developer who configures a custom provider checks the docs first.

**Content types:**
- Provider listing page with `openclaw.json` configuration snippet (3 fields: `baseUrl`, `apiKey`, `api: "openai-completions"`)
- Model cards for the current Kimi lineup: `gonka/kimi-k2.6` (workhorse tier) and `gonka/kimi-k2.7-code` (coding/agent tier), each with 256K context window and benchmark summary; add `gonka/kimi-k3` once open weights land (promised ~July 27, 2026)
- Troubleshooting guide addressing the two-step provider gotcha (provider definition + model allowlisting)

**Cadence:** Always available; updated with each Gonka feature release.

**Success metric:** Provider page views; percentage of page visitors who create a Gonka API key within 7 days.

**Example content piece:** "Gonka Provider Configuration" page with a copy-paste-ready `openclaw.json` block, a "verify it works" curl command, and a link to the quickstart guide. No mention of tokens, mining, or decentralization -- pure API configuration.

---

### OpenClaw GitHub (Issues, Discussions, PRs)

**Platform:** GitHub -- github.com/openclaw (organization repos)
**URL:** OpenClaw main repository issues, discussions, and PRs

**Why P0:** OpenClaw's GitHub is where active developers report issues, request features, and discuss provider options (375K+ stars as of mid-July 2026 -- re-pull the live count before citing -- GitHub's most-starred project and the fastest-growing repository in history, passing React's ~243K in ~60 days; 2,500+ contributors; the foundation's own July 2026 metrics report 4.5M new claws per week and ~30,000 ClawCon registrations across 34 events in 16 countries; the older ~3.2M monthly-active-user figure was an April 2026 estimate). A fork ecosystem is emerging around the repo -- sandboxed-execution security forks, Chinese adaptations wired to DeepSeek models and WeChat, and OpenClaw-based commercial services from Tencent and Z.ai (relevant because Z.ai's GLM-5.2 runs on Gonka's network) -- meaning "OpenClaw developers" increasingly includes fork and downstream-distribution users. Developers who search "custom provider" or "cheaper inference" in GitHub issues will find (or not find) Gonka. A merged PR adding Gonka as a built-in provider would eliminate the manual configuration barrier; built-in coverage now spans 18+ providers, and onboarding defaults to openrouter/auto (mediated by ClawRouter), which makes OpenRouter the path of least resistance.

**Governance reality check:** The OpenClaw Foundation formally launched July 8, 2026 as a 501(c)(3) (chaired by Dave Morin with Peter Steinberger; first full-time team of ten), with published leadership, paid maintainers, and an MIT-license commitment. Per the foundation's own launch post, the published major donors are Offline Holdings, Lobster Computer Company, University of Michigan (reported largest), and OpenAI, with more "in the pipeline" -- no "lead sponsor" is designated. Microsoft (Microsoft Scout) and NVIDIA (NemoClaw) are partners, not major donors; partners also include Tencent, GitHub, Red Hat (enterprise open source and supply-chain security), Atlassian, Vercel, Cloudflare, Blacksmith, and Convex. The conflicted-gatekeeper concern stands, stated precisely: OpenAI is a published major donor, employs the project's creator (Steinberger runs "Claw Labs" inside OpenAI), supports inference, and shipped Codex Security hardening -- and partner-maintainers ship their own OpenClaw distributions (NVIDIA NemoClaw, Microsoft Scout, Tencent maintaining security/stability/ClawHub). The built-in-provider PR path therefore still runs through a foundation whose largest corporate backers operate rival inference businesses. Plan for a slow or blocked PR: keep the custom-provider config path and the MCP server as parallel routes that need no gatekeeper approval. One new opening: the foundation is convening vendor-neutral standards councils on agent identity, agent profiles, evals, and enterprise deployment -- council participation (agent identity in particular intersects wallet-authenticated x402 payments) is an engagement route that does not run through the conflicted PR path.

**Primary persona(s):** Weekend Builder (searches for cost solutions in issues), Startup CTO (evaluates providers through GitHub discussions and PR quality).

**Content types:**
- PR submitting Gonka as a built-in provider (eliminates 3-field manual config for all developers)
- Helpful responses in issues where developers ask about inference costs, provider reliability, or model quality
- Discussion posts comparing provider options with honest benchmarks and cost data
- Config snippets in response to "how do I add a custom provider?" questions

**Cadence:** Daily monitoring; respond to relevant issues within 24 hours.

**Success metric:** Gonka mentions in OpenClaw GitHub issues and discussions; PR for built-in provider support merged; API key signups attributed to GitHub referrals.

**Example content piece:** A comment on an issue titled "OpenRouter costs too high for always-on agents" that says: "Session persistence can reduce heartbeat costs by ~80%. Here is a config snippet for Gonka that drops heartbeat token overhead from 460,800 tokens/day to ~92,000 tokens/day at the Casual tier: [snippet]. Full comparison: [link to blog post]."

---

### OpenClaw Discord

**Platform:** Discord
**URL:** Official OpenClaw Discord ("Friends of the Crustacean") -- discord.com/invite/clawd, ~175K members as of July 2026 (crossed 100K within ~6 weeks of its January 2026 founding)

**Why P0:** OpenClaw Discord is the real-time community where developers ask for help, share configurations, and discuss provider experiences. The Weekend Builder who is frustrated with their OpenRouter bill at 11pm on a Saturday asks for help here, not on Hacker News. Presence in this channel means being part of the conversation when provider decisions happen organically.

**Primary persona(s):** Weekend Builder (asks for help with costs and configuration), Privacy-First Builder (discusses provider privacy guarantees).

**Content types:**
- Pinned Gonka configuration snippet in the relevant channel (e.g., #providers or #configuration)
- Responses to cost-related questions with specific savings data (heartbeat overhead reduction)
- Troubleshooting help for developers configuring Gonka as a custom provider
- Session persistence explainers when developers ask about reducing agent costs

**Cadence:** Daily presence; respond to relevant questions within 4 hours during active hours.

**Success metric:** API key signups attributed to Discord conversations; number of developers who mention using Gonka in Discord.

**Example content piece:** Response to "my agent bill on OpenRouter keeps climbing and it only handles 50 messages/day": "Half your bill is heartbeats -- your agent resends full context every 30 minutes. Gonka keeps context server-side, so heartbeats send only new data. Same agent, same code, one config change. Gonka is currently the cheapest tracker-listed provider for K2.6/K2.7 [link to pricepertoken.com/endpoints/gonka] -- current rates reflect network subsidy and utilization and may change. Here is the config: [snippet]." Do not quote fixed dollar-per-month savings figures (the April 2026 "$40 to $13/month" scenario numbers are banned per pricing analysis v2.0); competitor baselines must be cached-adjusted since OpenRouter passes through prompt caching at 10-20% of input price.

---

## P1 Channels

P1 channels have broad reach into AI developer communities but require content creation investment. These channels build awareness beyond the OpenClaw ecosystem and establish Gonka's credibility through technical content.

---

### MCP Registry (Gonka MCP Server)

**Platform:** Official MCP Registry + Gonka-hosted MCP server
**URL:** MCP Registry listing (registry.modelcontextprotocol.io)

**Why P1:** MCP has become the de facto agent interoperability standard -- 110M monthly SDK downloads (per co-creator David Soria Parra, April 2026), 41% of surveyed software orgs in limited-or-broad production with MCP servers (Stacklok 2026), and first-party support across ChatGPT, Gemini, Microsoft Copilot, VS Code, Cursor, and GitHub. (The 110M downloads figure was presented at the 2026 MCP Dev Summit, up from 97M in December 2025.) MCP was donated to the Agentic AI Foundation (Linux Foundation) in December 2025 with multi-vendor governance (Anthropic, OpenAI, Block), and AAIF reported reaching 170 member organizations within four months of the donation -- so a registry listing gives Gonka discoverability inside every major agent host, independent of OpenClaw Foundation gatekeeping, under demonstrably neutral governance. Three caveats for execution: (1) the official registry is still pre-GA (preview since Sept 2025, API frozen at v0.1, no durability guarantees) and published server counts conflict (one May 2026 source says 8,400+ verified; re-pull from registry.modelcontextprotocol.io before citing); (2) most real-world discovery happens via larger third-party registries (as of July 2026: Glama 57,013 -- now by far the largest third-party directory and the top listing priority -- PulseMCP 18,240+, mcp.so ~20,200, Smithery 7,000+; one aggregate tracker counts 76,803 across all five as of Jul 17, 2026) -- list Gonka on those too; (3) build the Gonka MCP server against the 2026-07-28 spec revision (RC locked May 21, 2026; the FINAL spec ships July 28 -- ten days out -- with Tier 1 SDK support expected within the validation window). It is the largest revision since launch: stateless protocol core (runs behind plain round-robin load balancers), Extensions framework, Tasks for long-running work, MCP Apps (server-rendered UIs), OAuth/OIDC-aligned authorization hardening, and a formal deprecation policy -- the stateless core and Tasks features are directly relevant to an inference+sessions server design. This was ranked a nice-to-have in earlier planning (v1.4 backlog); as of mid-2026 it is a primary distribution channel.

**Primary persona(s):** Startup CTO (evaluates via standard tooling), Weekend Builder (discovers through host-native MCP browsers).

**Content types:**
- Gonka MCP server (inference + sessions tools) with registry listing and provenance/signing metadata
- Integration docs per host (Cursor, VS Code, ChatGPT)

**Cadence:** Always available; updated with each Gonka API release.

**Success metric:** Registry-listing-to-signup conversion; API keys created via MCP-originated flows.

---

### Technical Blog (docs.gonka.ai/blog)

**Platform:** Self-hosted blog on docs.gonka.ai
**URL:** docs.gonka.ai/blog

**Why P1:** The technical blog is the canonical source of Gonka content that all other channels link to. Comparison posts, benchmarks, and tutorials live here permanently with SEO value. Reddit posts, Twitter threads, and Discord responses all point back to blog posts for detailed evidence. Without the blog, every channel sends developers to API docs with no narrative context.

**Primary persona(s):** Startup CTO (evaluates through in-depth technical content), Weekend Builder (finds via Reddit/Google search for cost comparisons).

**Content types:**
- Cost comparison posts: "OpenClaw Inference Costs: Gonka vs OpenRouter vs Together AI" with heartbeat savings calculator
- Quickstart guides: "OpenClaw + Gonka in 5 Minutes"
- Deep-dive technical posts: "Agent Sessions: Why Your Agent Pays for Context Twice"
- Benchmark results: K2.7-Code performance (+21.8% on Kimi Code Bench v2 vs K2.6, ~30% fewer reasoning tokens), tool calling stability, latency measurements; K3 coverage once weights land

**Cadence:** Weekly (1 post per week minimum).

**Success metric:** Blog-to-signup conversion rate (readers who create API keys within 7 days); organic search traffic growth.

**Example content piece:** "Cut Agent Inference Costs 73% with Gonka" -- a launch post that walks through the heartbeat overhead problem (with token math from the pricing analysis), shows the session persistence solution, includes a before/after cost comparison at the Casual and Active tiers, and ends with a 90-second config snippet.

---

### Twitter/X AI Developer Community

**Platform:** Twitter/X
**URL:** twitter.com/gonka_ai (or equivalent)

**Why P1:** Twitter/X has the largest concentration of AI developers discussing inference providers, model benchmarks, and agent frameworks in real time. The AI developer Twitter community (verified AI-infra voices such as @_philschmid; build a vetted list before outreach -- earlier drafts named accounts that turned out to be corporate or unverifiable) drives conversations about model quality and infrastructure costs that reach tens of thousands of developers. Gonka's benchmark results and cost comparisons are shareable Twitter content by nature.

**Primary persona(s):** All three personas discover content on Twitter, but Weekend Builder and Privacy-First Builder are most likely to engage with cost and privacy threads respectively.

**Content types:**
- Benchmark result graphics: Kimi K2.7-Code / K3 vs GPT-5.x vs Claude Fable 5 / Opus 4.8 on coding and agent benchmarks -- the models K3 is itself benchmarked against (AA Index: K3 57, Opus 4.8 56, Fable 5 ~60). GPT-4o was retired from ChatGPT April 2026 and Opus 4.5 is superseded -- comparisons against either read as stale
- Cost comparison threads: heartbeat overhead breakdown with specific dollar amounts
- Launch announcements: new features, new blog posts, partnership milestones
- Community engagement: replies to developer questions about inference costs, provider comparisons

**Cadence:** 3-5 posts per week; daily monitoring and replies.

**Success metric:** Referral traffic from Twitter to docs.gonka.ai that converts to API key signups (not follower count, not impressions).

**Example content piece:** Thread: "Your OpenClaw agent sends 460,800 tokens/day in heartbeats -- half your bill, zero user-facing value. Here is what happens when you add server-side sessions: [before/after cost chart]. Config snippet in the thread. Full breakdown: [link to blog post]."

---

### Reddit (r/LocalLLaMA, r/OpenClaw)

**Platform:** Reddit
**URL:** reddit.com/r/LocalLLaMA, reddit.com/r/OpenClaw (and related subreddits)

**Why P1:** Reddit is where OpenClaw developers discover new providers through organic community discussion. r/LocalLLaMA (~775K members as of July 2026) is the largest community of developers interested in open-source model inference. r/OpenClaw hosts direct provider comparison discussions (a smaller r/OpenClawInstall also exists; member counts for both are unverified -- pull from Reddit directly before citing). The Weekend Builder persona's primary adoption trigger is seeing a cost comparison post on Reddit (developer personas: Weekend Builder, Adoption Triggers).

**Primary persona(s):** Weekend Builder (primary -- discovers through cost comparison posts), Privacy-First Builder (secondary -- discusses privacy in technical subreddits).

**Content types:**
- Provider comparison posts: "I compared OpenRouter, Together AI, and Gonka for my OpenClaw agent -- here are the real costs"
- Launch posts: "Show r/LocalLLaMA: Gonka -- agent-native inference with server-side sessions"
- Help responses: answers to "how do I reduce my OpenClaw inference costs?" threads
- AMA or Q&A posts addressing developer questions about the Kimi model lineup (K2.6/K2.7-Code/K3), sessions, privacy

**Cadence:** 2-3 posts/responses per week; daily monitoring for relevant threads.

**Success metric:** Upvotes (indicates community validation) plus API key signups from Reddit referral links.

**Example content piece:** Post in r/LocalLLaMA: "I tracked my OpenClaw agent costs for a month -- heartbeats were 51% of my bill. Switching to a provider with session persistence cut the heartbeat share to near zero; Gonka is currently the cheapest listed provider for K2.6/K2.7 on the public trackers [link], though current rates reflect network subsidy and utilization. Here is the config and full cost breakdown: [link]." (Use tracker-verified relative claims, not the April 2026 "$218 to $59/month" scenario figures, which are banned from external use per pricing analysis v2.0.)

---

### dev.to / Hashnode

**Platform:** Developer blog aggregators
**URL:** dev.to, hashnode.com

**Why P1:** dev.to and Hashnode aggregate developer content and surface it to developers who do not follow individual blogs. Cross-posting Gonka blog content here extends reach to developers who discover tutorials through these platforms' recommendation algorithms. Lower effort than original content creation since posts are cross-posted from the technical blog.

**Primary persona(s):** Weekend Builder (discovers tutorials through platform recommendations).

**Content types:**
- Cross-posted quickstart guides from docs.gonka.ai/blog
- Tutorial-style posts: "How to Add Session Persistence to Your OpenClaw Agent"
- Cost comparison posts adapted for the dev.to audience format

**Cadence:** Bi-weekly (cross-post every other blog post).

**Success metric:** Cross-post-to-signup conversion rate; dev.to/Hashnode referral traffic to docs.gonka.ai.

**Example content piece:** Cross-posted version of "OpenClaw + Gonka in 5 Minutes" quickstart guide with dev.to-friendly formatting and tags (#ai, #llm, #openai, #agents).

---

## P2 Channels

P2 channels have meaningful reach but higher production cost or lower conversion rates. Invest here after P0 and P1 channels are operational.

---

### YouTube Tutorials

**Platform:** YouTube
**URL:** youtube.com/@gonka_ai (or equivalent)

**Why P2:** Video tutorials have strong discovery through YouTube search ("OpenClaw tutorial," "cheap LLM inference," "agent cost reduction"). However, video production costs are 5-10x higher than blog posts and iteration cycles are slower (you cannot edit a published video). P2 because the content is high-value but expensive to produce.

**Primary persona(s):** Weekend Builder (watches tutorials on weekends while building), Startup CTO (shares with engineering team for evaluation).

**Content types:**
- "OpenClaw + Gonka in 5 Minutes" screencast tutorial
- Cost comparison walkthroughs with live API dashboard
- Session persistence deep-dive with code examples
- "Build an Agent with Sessions and Tiering" project tutorial

**Cadence:** Bi-weekly (1-2 videos per month).

**Success metric:** View-to-signup conversion rate (not view count); YouTube referral traffic to docs.gonka.ai.

**Example content piece:** 5-minute screencast: developer opens `openclaw.json`, adds Gonka config (3 fields), runs their agent, checks the dashboard showing heartbeat cost reduction. No crypto language, no blockchain diagrams -- just code and a cost dashboard.

---

### HackerNews

**Platform:** news.ycombinator.com
**URL:** news.ycombinator.com

**Why P2:** HackerNews reaches early-adopter technical decision-makers -- exactly the Startup CTO persona. A front-page post can drive thousands of qualified visitors. However, HN is unpredictable (posts may not gain traction), the audience is hostile to self-promotion, and posting cadence is limited by content quality. P2 because high potential but unreliable reach.

**Primary persona(s):** Startup CTO (evaluates infrastructure through HN discussions), Weekend Builder (discovers through HN front page).

**Content types:**
- "Show HN" launch post linking to a technical deep-dive
- Substantive comments on agent infrastructure threads with honest Gonka positioning
- Deep-dive posts: "The Hidden Cost of Agent Heartbeats" (technical enough for HN audience)

**Cadence:** Monthly or when content quality warrants a submission (never force low-quality posts to HN).

**Success metric:** HN-to-signup conversion rate; quality of HN comments (technical engagement, not drive-by reactions).

**Example content piece:** "Show HN: Gonka -- Server-side sessions cut OpenClaw agent costs by 73%" linking to a detailed blog post with token math, architectural diagrams (showing why heartbeats waste tokens), and a working config snippet.

---

### Crypto Twitter / DePIN Communities

**Platform:** Twitter/X (crypto segment), Telegram, DePIN-focused forums
**URL:** Various crypto community channels

**Why P2:** Crypto-native communities reach GPU hosts (supply side) and GNK token holders (ecosystem stakeholders). These audiences matter for network growth but are not the primary developer adoption channel. Content here uses Phase 17 vocabulary guidelines -- no developer-facing language; focus on host economics and network growth. This is the primary channel for the 30% crypto allocation.

Several 2026 developments give this channel concrete material: (1) Gonka's funding story -- ~$80M raised as of early 2026, including Bitfury's $12M strategic round (Nov 2025) and its $50M commitment (Dec 2025, first draw from Bitfury's $1B ethical-AI fund); (2) the GAIB × Gonka "GAIC" enrollment, now open to the public market -- GAIB handles GPU procurement (H100/H200/B200), node ops, and reward routing, with a 10%-of-mined-GNK insurance pool; (3) a third-party GPU-rental partner ecosystem: Spheron runs dedicated Gonka bare-metal pages and Gcore has a Gonka GPU rental landing page; (4) planned Asia expansion (Japan, South Korea) by end of 2026. All are credibility anchors for host recruitment.

**Watchlist -- agent-native payments (x402):** The x402 Foundation (Coinbase + Linux Foundation, announced April 2026) reached formal operational launch on July 14, 2026 with 40 member organizations across tiers -- premier members now span the card networks and major PSPs: Visa, Mastercard, American Express, Stripe, Adyen, Fiserv, plus AWS, Google, Cloudflare, Coinbase, Circle, Ripple, Shopify, MoonPay, and the Monad/Solana/Stellar foundations. Volume is no longer small: in the 30 days ending ~July 15, 2026 the protocol processed ~75M transactions moving ~$24M (~$800K/day) between ~94K buyers and ~22K sellers, and Chainalysis reports 95% of payment value is now in transactions above $1 -- the earlier "mostly testing/gamed micropayments" caveat is outdated. Settlement is predominantly USDC (all-USDC on Base; ~56.7% Base / ~37.1% Solana split by volume). x402 has also shipped at the edge: AWS added GA x402 support in CloudFront and AWS WAF (~late June 2026), and Cloudflare opened a waitlist for its Monetization Gateway -- meaning an x402-gated Gonka inference endpoint becomes deployable behind commodity edge infra. BlockRunAI's ClawRouter already sells OpenClaw inference via USDC micropayments over x402. Note that x402 is now one of three layers in the 2026 agentic-payments stack: x402 handles machine-to-machine execution/micropayments, AP2 -- originated by Google, donated to the FIDO Alliance in July 2026, so now community-led rather than Google-stewarded -- handles authorization via signed mandates (60+ partners; in production with Gemini Spark since May 2026), and OpenAI/Stripe's ACP handles agent checkout (live in ChatGPT). AP2 v0.2's "Human Not Present" payments let agents execute autonomously, which blurs the x402=execution / AP2=authorization line somewhat. For agent-procured inference, x402 is still the correct layer, but position the Gonka x402 story within this stack -- enterprise buyers will ask about AP2/ACP. The "API keys only, never crypto" rule stays absolute for human developer channels, but Gonka -- already a crypto network -- has a natural x402 story for the agent-as-customer segment. Track as a near-term channel, not just a watchlist item; a competitor is already occupying the "agent-native payments for OpenClaw" position.

**Primary persona(s):** Privacy-First Builder (overlaps with crypto-native privacy communities).

**Content types:**
- Network growth updates: host count, inference volume, geographic distribution
- Host economics content: earnings, hardware requirements, ROI projections
- Token utility explainers framed per vocabulary guidelines (host-facing, not developer-facing)
- Ecosystem partnerships and integration milestones

**Cadence:** 2-3 posts per week.

**Success metric:** GPU host signups; token holder engagement metrics (but not as proxy for developer adoption).

**Example content piece:** "Gonka network update: [X] GPU hosts serving [Y] inference requests/day across [Z] regions. Host earnings averaging [N] GNK/month on H100 hardware. Network capacity growing [%] month-over-month."

---

### Privacy-Focused Forums

**Platform:** Lobsters, security-focused subreddits (r/privacy, r/netsec), privacy mailing lists
**URL:** lobste.rs, reddit.com/r/privacy, reddit.com/r/netsec

**Why P2:** These forums reach the Privacy-First Builder persona who evaluates providers through security audits and privacy architecture analysis. Content here must be technically honest -- overclaiming privacy guarantees in security communities damages credibility permanently (PITFALLS.md: Pitfall 1). P2 because the audience is small but highly aligned with Gonka's privacy value proposition.

**Primary persona(s):** Privacy-First Builder.

**Content types:**
- Privacy architecture deep-dives: "How Decentralized Inference Protects Prompt Privacy -- Architecture, Not Promises"
- Honest limitations disclosure: current guarantees vs TEE roadmap
- Open-source audit invitations: "Review our inference pipeline at github.com/mitgor/gonka-ai-infrastructure"

**Cadence:** Monthly (quality over quantity; this audience detects and punishes low-effort content).

**Success metric:** Privacy-page views on docs.gonka.ai; signups from privacy-focused referral sources; sentiment in security community discussions.

**Example content piece:** "Gonka Privacy Audit: What We Guarantee Today and What We Do Not" -- a blog post linked from Lobsters that explains decentralized inference architecture, honestly states that TEE-based encrypted inference is not yet built, and invites the community to audit the open-source infrastructure code.

---

## P3 Channels

P3 channels are expensive, slow to convert, or dependent on prerequisites (published pricing, case studies) that do not yet exist. Defer investment until P0-P2 channels demonstrate traction.

---

### AI/Web3 Conferences

**Platform:** Token2049, ETHDenver, AI Engineer events, NeurIPS Industry Day, and the Agentic AI Foundation's 2026 events program -- AGNTCon and MCP Dev Summit / MCPCon North America and Europe
**URL:** Various conference venues

**Timing note:** AI Engineer World's Fair 2026 already ran June 29 - July 2, 2026 in San Francisco (Moscone West, ~6,000 attendees, 29 tracks). CFP targeting should aim at fall-2026 events and the 2027 cycle. Given this document elevates the MCP Registry to a primary distribution channel, AAIF's AGNTCon/MCPCon events (announced via Linux Foundation press, 2026) are the most directly on-target venues -- talks, hackathons, and registry visibility -- and belong at the top of the CFP list alongside AI Engineer events. Note the event ran pre-fair hackathons starting June 28 -- hackathon presence is now a standard low-cost devrel motion at AI Engineer events and fits the Weekend Builder persona better than a booth; include it in the fall-2026/2027 plan.

**Why P3:** Conferences provide high-quality networking with Startup CTOs and enterprise decision-makers, but cost $5,000-50,000+ per event (travel, sponsorship, booth). ROI is uncertain until Gonka has published pricing, case studies, and a production track record to present. P3 because prerequisites are not met.

**Primary persona(s):** Startup CTO (evaluates at conferences), Privacy-First Builder (attends security/privacy-focused events).

**Content types:**
- Technical talks: "Agent-Native Inference: Why Sessions Matter More Than Per-Token Pricing"
- Live demos: OpenClaw agent running on Gonka with real-time cost dashboard
- Booth conversations with pre-qualified leads

**Cadence:** Quarterly (1-2 conferences per quarter once prerequisites are met).

**Success metric:** Conference-to-API-key conversion within 30 days (not badge scans or booth traffic).

**Example content piece:** 20-minute talk at an AI Engineer event (2027 cycle): "The Hidden Cost of Agent Heartbeats" with live demo showing session persistence reducing costs in real time.

---

### Paid Developer Ads

**Platform:** Carbon Ads, BuySellAds, Google Ads (AI infra keywords)
**URL:** Various ad networks targeting developer audiences

**Why P3:** Paid ads can scale reach beyond organic channels but require clear CAC targets and conversion tracking that depend on published pricing and a functioning signup flow. P3 because the cost-per-acquisition is unknowable until organic channels establish baseline conversion rates.

**Primary persona(s):** All (ads are broad reach by design).

**Content types:**
- Targeted display ads on AI infrastructure sites: "Cut your OpenClaw inference costs by 73%"
- Google Ads on keywords: "OpenClaw inference provider," "cheap LLM API," "agent cost reduction"
- Retargeting ads for developers who visited docs.gonka.ai but did not create an API key

**Cadence:** Continuous when budget allows (after P0-P2 channels are operational).

**Success metric:** Cost per API key signup (target: <$25 CAC); cost per API-active developer (target: <$100 CAC).

**Example content piece:** Carbon Ads banner on a developer blog: "Your OpenClaw agent resends full context 48 times/day. Gonka keeps it server-side. Save 73%. [Get API Key]."

---

### DePIN / Web3 Developer Forums

**Platform:** DePIN-focused community forums, Web3 developer communities
**URL:** Various decentralized infrastructure community platforms

**Why P3:** These forums reach crypto-native developers who may be interested in building on decentralized infrastructure, but the audience overlap with OpenClaw developers is minimal. Content here uses crypto-native vocabulary (acceptable per Phase 17 context rules) but does not drive the primary KPI (API-active developers). P3 because this channel serves the supply side (hosts) more than the demand side (developers).

**Primary persona(s):** Privacy-First Builder (secondary channel for privacy-focused crypto-native developers).

**Content types:**
- Host onboarding guides: "Run a Gonka GPU Node: Hardware Requirements and Expected Earnings"
- Token utility explainers for existing DePIN community members
- Network architecture deep-dives using crypto-native vocabulary

**Cadence:** Weekly.

**Success metric:** Host signup conversion rate (supply-side metric, not demand-side).

**Example content piece:** "Gonka Host Guide: Earn GNK by serving Kimi inference on your H100/H200/B200" -- a guide targeting GPU operators in DePIN communities, using crypto-native vocabulary per Phase 17 context rules and referencing the GAIB partnership as the managed-hardware onramp.

---

## 70/30 Split Analysis

### Channel Allocation

Gonka's channel investment follows a 70/30 split: 70% of effort on AI/developer channels (where OpenClaw builders spend time) and 30% on crypto channels (where GPU hosts and token holders engage).

| Category | Channels | % of P0+P1 Investment | Rationale |
|----------|---------|----------------------|-----------|
| **AI/Developer (70%)** | OpenClaw Provider Directory, OpenClaw GitHub, OpenClaw Discord, MCP Registry, Technical Blog, Twitter/X AI Community, Reddit, dev.to/Hashnode | ~75% of P0+P1 channels | These channels reach the developers who will become API-active users. Developer adoption drives inference demand, which drives network value, which attracts GPU hosts. The flywheel starts with developers. |
| **Crypto (30%)** | Crypto Twitter/DePIN Communities, AI/Web3 Conferences, DePIN/Web3 Dev Forums | ~25% of P0+P1+P2+P3 channels | Crypto channels reach GPU hosts and token holders. Host supply is necessary for network reliability, but supply without demand is empty infrastructure. Crypto channel content focuses on host economics and network growth, not developer acquisition. |

### Why 70/30 and Not 50/50

Crypto channels reach GPU hosts and token holders, but developer adoption drives network value. The causal chain is:

1. Developers adopt Gonka as inference provider (demand side)
2. Inference volume grows, increasing fee revenue for GPU hosts
3. Profitable hosting attracts more GPU operators (supply side)
4. More GPU hosts improve reliability and reduce latency
5. Better reliability attracts more developers (flywheel)

Investing 50/50 or crypto-first inverts this flywheel: GPU hosts join an empty network, earn nothing, and leave (PITFALLS.md: Pitfall 3 -- Akash saw active providers drop below 100 without sustained demand). The 70/30 split ensures the demand side leads.

### Crypto Channel Content Guidelines

Content for the 30% crypto allocation follows Phase 17 vocabulary guidelines with one exception: crypto channels use crypto-native vocabulary because the audience expects it (Phase 17 context rules, acceptable context #4).

- **Use in crypto channels:** GNK rewards, mining, staking, epochs, network growth, token economics
- **Never use in developer channels:** wallet, staking, mining, DePIN, Web3, gas, smart contract, governance proposals
- **Frame crypto content around host economics:** "Earn GNK by serving inference" not "Buy GNK for passive income"
- **Rationale:** "Crypto channels reach GPU hosts and token holders, but developer adoption drives network value"

---

## Persona-Channel Map

Which channels reach which persona, and what content theme resonates on each.

| Channel | Weekend Builder | Startup CTO | Privacy-First Builder |
|---------|----------------|-------------|----------------------|
| OpenClaw Provider Directory | Config snippet (cost-focused) | Architecture overview (reliability-focused) | Data handling policy (privacy-focused) |
| OpenClaw GitHub | Cost-related issue responses | PR quality evaluation, discussion posts | Open-source code audit |
| OpenClaw Discord | Cost questions, config help | -- (less active in Discord) | Privacy discussions, provider comparisons |
| Technical Blog | Cost comparison posts | Deep-dive technical posts, benchmarks | Privacy architecture deep-dives |
| Twitter/X AI Community | Cost savings threads | Benchmark results, infrastructure analysis | Privacy-related threads |
| Reddit (r/LocalLLaMA, r/OpenClaw) | Provider cost comparison posts | -- (reads but rarely posts) | Privacy subreddit discussions |
| dev.to / Hashnode | Quickstart tutorials | -- | -- |
| YouTube | 5-minute setup tutorials | Share with engineering team | -- |
| HackerNews | -- (reads, does not post) | "Show HN" evaluation, technical discussion | -- |
| Crypto Twitter / DePIN | -- | -- | Decentralized privacy discussions |
| Privacy Forums | -- | -- | Privacy audit posts, architecture reviews |
| Conferences | -- | Technical talks, demos | Security/privacy events |

**Reading the map:**
- Weekend Builder: OpenClaw Discord, Reddit, YouTube (cost-focused content at every touchpoint)
- Startup CTO: Technical blog, HackerNews, conferences (reliability-focused content, evidence-driven evaluation)
- Privacy-First Builder: Crypto Twitter, privacy-focused forums, Reddit (privacy-focused content, honest limitations, audit invitations)

---

## Content Calendar Framework

Content production follows two organizing principles:

1. **AAARRRP mapping:** Every content piece targets one primary AAARRRP stage and one primary persona. This prevents "content for content's sake" and ensures each piece moves developers through the adoption journey.
2. **70/30 content split:** 70% of content is developer-education (tutorials, benchmarks, comparisons, quickstart guides) targeting the demand side. 30% is ecosystem/community content (network updates, host stories, token utility explainers) targeting the supply side and broader community. The 30% ecosystem content follows Phase 17 vocabulary guidelines -- developer-facing vocabulary in all cases, with crypto-native vocabulary only in explicitly crypto-targeted channels per Phase 17 context rules.

Content themes are drawn directly from the Phase 17 message house value propositions:
- **VP1:** Session persistence eliminates heartbeat waste (lead message -- 73% cost reduction)
- **VP2:** Automatic model tiering (classification on cheap model, reasoning on strong one)
- **VP3:** One config change, 90 seconds (drop-in OpenClaw compatibility)
- **VP4:** No content filters, no prompt logs (privacy-first builder message)
- **VP5:** Inference gets cheaper as network grows (long-term cost trajectory)

---

## Content-Journey Matrix

Every content piece maps to an AAARRRP journey stage, a content theme from the message house, and a primary channel for distribution.

| AAARRRP Stage | Content Theme | Content Type | Primary Channel | Cadence | Persona Focus |
|---------------|--------------|-------------|----------------|---------|---------------|
| **Awareness** | "Why Gonka exists" -- heartbeat overhead costs developers 44-85% of their bill | Comparison blog posts, benchmark graphics, Reddit threads | Blog, Reddit, Twitter/X | Weekly | All personas |
| **Awareness** | Current Kimi agent performance -- K2.7-Code (+21.8% on Kimi Code Bench v2 vs K2.6), K3 once weights land | Benchmark result graphics, comparison tables | Twitter/X, Blog | Bi-weekly | Weekend Builder, Startup CTO |
| **Awareness** | Privacy without self-hosting -- no content filtering, no central logging | Privacy architecture deep-dive, honest limitations | Blog, Privacy Forums, Lobsters | Monthly | Privacy-First Builder |
| **Acquisition** | "Add Gonka in 90 seconds" -- 3 fields in openclaw.json, no wallet, no tokens | Quickstart guide, config snippet with copy button | Docs, OpenClaw Discord, dev.to | Always available | Weekend Builder |
| **Acquisition** | Architecture for reliability-focused evaluation -- redundant nodes, health-checked routing | Architecture overview, staging deployment guide | Docs, Blog | Always available | Startup CTO |
| **Acquisition** | Data handling and privacy policy -- what is logged, what is not, audit guide | Privacy policy page, open-source audit walkthrough | Docs, GitHub | Always available | Privacy-First Builder |
| **Activation** | Working code examples -- OpenClaw config + agent template + session setup | Code examples, GitHub repo templates, docs snippets | GitHub, Docs, OpenClaw Discord | Bi-weekly updates | All personas |
| **Activation** | "OpenClaw + Gonka in 5 Minutes" video walkthrough | Screencast tutorial -- config, first call, cost dashboard | YouTube, Twitter/X | Bi-weekly | Weekend Builder |
| **Activation** | Staging-to-production migration guide with load testing results | Migration guide, test suite results, latency comparison | Blog, Docs | Updated quarterly | Startup CTO |
| **Retention** | Session persistence deep-dive -- how sessions work, cost savings math, advanced config | Deep-dive guide: "Agent Sessions: Why Your Agent Pays for Context Twice" | Blog, Docs | Bi-weekly | Startup CTO |
| **Retention** | Cost comparison calculator -- interactive tool showing savings vs OpenRouter/Together AI | Interactive web tool at docs.gonka.ai/calculator | Docs site | Always available, updated monthly | Weekend Builder, Startup CTO |
| **Retention** | Ongoing privacy posture monitoring -- changelog for privacy-relevant changes | Privacy changelog, audit script, community watchdog | Docs, GitHub | With each release | Privacy-First Builder |
| **Revenue** | ROI calculator -- total cost of ownership including heartbeat savings, tiering, engineering time | Interactive ROI tool, pricing comparison table | Blog, Docs | Monthly updates | Startup CTO |
| **Revenue** | Pricing comparison at each tier -- Casual, Active, Heavy vs OpenRouter, Together AI, DeepInfra | Pricing page with tier calculator | Docs site | Always available | All personas |
| **Referral** | Developer spotlight -- featured developer stories, cost savings testimonials | Blog interview, shareable cost savings badge/graphic | Twitter/X, Blog, Discord | Monthly | Weekend Builder |
| **Referral** | Community recognition -- contributor highlights, referral credit program | Referral program page, pre-written share templates | Docs, Twitter/X, Discord | Monthly | Weekend Builder |
| **Referral** | Engineering case study co-creation -- "How We Cut Costs 73% with Sessions" | Co-branded blog post with production customer | Blog, HackerNews | Quarterly | Startup CTO |
| **Product** | Feedback channels -- GitHub issues, feature request templates, advisory program | Public GitHub repo with issue templates, quarterly advisory calls | GitHub, Docs | Ongoing | All personas |

---

## Content Themes by Quarter (Template)

This framework provides a quarterly content allocation template. Actual dates are TBD at execution time -- this is a strategic framework, not a fixed calendar.

### Q1: Launch Quarter

**Content allocation:** 60% Awareness + Acquisition, 25% Activation, 15% Retention

The launch quarter prioritizes making developers aware Gonka exists and removing friction from first API call. Without Awareness and Acquisition content, all downstream stages are blocked (developer personas: AAARRRP Priority Ranking -- Awareness and Acquisition are P0 universal blockers).

| Week | Content Type | Channel | AAARRRP Stage |
|------|-------------|---------|---------------|
| 1-2 | Launch blog post: "Cut Agent Inference Costs 73% with Gonka" | Blog, Reddit, HN, Twitter/X | Awareness |
| 1-2 | OpenClaw provider listing + config snippet | Provider Directory, Discord | Acquisition |
| 3-4 | Quickstart guide: "OpenClaw + Gonka in 5 Minutes" | Blog, dev.to, Docs | Acquisition |
| 3-4 | Comparison post: "Gonka vs OpenRouter vs Together AI" | Reddit, Blog | Awareness |
| 5-6 | Video tutorial: config + first agent call | YouTube, Twitter/X | Activation |
| 5-6 | Session persistence deep-dive | Blog | Retention |
| 7-8 | Benchmark results: current Kimi (K2.7-Code/K3) agent performance | Twitter/X, Blog | Awareness |
| 7-8 | Privacy architecture post | Blog, Lobsters | Awareness (Privacy-First) |
| 9-10 | Cost calculator tool launch | Docs site | Retention |
| 9-10 | Reddit AMA / community Q&A | Reddit | Awareness + Acquisition |
| 11-12 | Developer spotlight: first power user | Blog, Twitter/X | Referral |
| 11-12 | Month 3 metrics review (internal) | Internal | -- |

### Q2: Growth Quarter

**Content allocation:** 25% Awareness, 50% Activation + Retention, 25% Revenue + Referral

Q2 shifts focus to converting acquired developers into API-active users and retaining them. Awareness continues at reduced cadence to sustain the top of funnel.

- Bi-weekly deep-dive blog posts on sessions, tiering, memory API, webhooks
- Monthly developer spotlights and cost savings case studies
- Launch pricing page and ROI calculator
- Begin conference evaluation (submit CFPs for fall-2026 and 2027-cycle events; AI Engineer World's Fair 2026 has already passed)
- Cross-post best-performing blog content to dev.to/Hashnode

### Q3+: Maturity Quarters

**Content allocation:** Balanced across all AAARRRP stages

- Content production is self-sustaining with established cadences per channel
- Community-generated content supplements official content (referral stage activating)
- Conference talks and case studies provide credibility at scale
- Quarterly 70/30 split audit ensures channel investment remains balanced
- Product stage feedback shapes content roadmap (address top feature requests in content)

---

## Content Production Guidelines

Every piece of Gonka developer-facing content must follow these rules, derived from the Phase 17 message house and vocabulary guidelines.

### Messaging Rules

1. **Reference the Phase 17 message house** (gonka_message_house.md) before writing any content piece. The message hierarchy is: lead with cost reduction (VP1), support with tiering (VP2) and ease of integration (VP3), use privacy (VP4) only for Privacy-First Builder audience.

2. **Never use the 16 crypto terms on the never-say list** in developer-facing content: wallet, staking, mining, DePIN, Web3, gas, slashing, governance proposals, epochs, validators, tokenomics, consensus mechanism, on-chain, smart contract, token (as cryptocurrency), decentralized (as headline). Use the approved alternatives from the vocabulary guidelines table.

3. **Lead with heartbeat cost reduction (73%) as primary hook** per the Phase 17 core positioning statement. Every awareness and comparison piece should open with the heartbeat overhead problem and the session persistence solution before mentioning any other Gonka feature.

4. **Include an OpenClaw config snippet in every tutorial and guide.** The "product" in every content piece is the 3-field `openclaw.json` configuration: `baseUrl`, `apiKey`, `api: "openai-completions"`. If the content does not show how to use Gonka with OpenClaw, it is not actionable.

5. **Address at least one objection from the playbook** (gonka_objection_playbook.md) in every comparison post. Use the ACE framework (Acknowledge, Counter, Evidence). The most common objections to address: "never heard of Gonka" (universal), "is this a crypto thing?" / "is this a scam?" (universal -- amplified post-ClawHavoc and the Clawdbot→Moltbot→OpenClaw rename churn; the community now applies scam-level scrutiny to any new OpenClaw-adjacent tool), "decentralized = unreliable" (Startup CTO).

6. **Each content piece targets one primary persona and one AAARRRP stage.** This is not optional. If a content piece tries to address all three personas simultaneously, it addresses none effectively. The Content-Journey Matrix above specifies which persona and stage each content type targets.

### Quality Standards

- All cost claims cite specific pricing analysis data (Section 3 for tier costs, Section 5 for Gonka hidden cost analysis, Section 6 for monthly projections)
- All benchmark claims cite competitive feature matrix (Section 3 for model benchmarks, Section 7 for uptime) -- the matrix was re-baselined July 2026 (GPT-5.4/5.5/5.6 GA, Opus 4.8/Sonnet 5/Fable 5 pricing, GPT-4o retirement, Together K2.6/K2.7-Code pricing) and is safe to cite as-is
- Honest concessions are included for Gonka's known weaknesses: narrow model lineup (Kimi family, plus Z.ai GLM-5.2), no published SLA, no published pricing, TEE not yet built
- Content that looks like a DeFi protocol page instead of a cloud platform page is rejected and rewritten
- Visual style reference: Vercel, Supabase, Cloudflare blog -- clean, developer-friendly, no crypto aesthetics

---

## Channel-Content Cross-Reference

For each P0 and P1 channel, the top 3 content pieces to produce first (prioritized backlog). This is the operational "what to build first" list.

### P0 Channels

**OpenClaw Provider Directory**
1. Provider configuration page with copy-paste `openclaw.json` snippet and model cards for `gonka/kimi-k2.6` and `gonka/kimi-k2.7-code` (add `gonka/kimi-k3` once weights land)
2. Troubleshooting guide for the two-step provider gotcha (provider definition + model allowlisting per STACK.md)
3. "Why Gonka?" comparison table on the provider page (sessions, tiering, cost savings -- no crypto language)

**OpenClaw GitHub**
1. PR adding Gonka as a built-in provider (eliminates manual config for all developers)
2. Discussion post: "Gonka: Agent-Native Inference with Session Persistence" introducing Gonka to the OpenClaw community
3. Template response for cost-related issues: config snippet + heartbeat savings data + link to blog comparison

**OpenClaw Discord**
1. Pinned config snippet in #providers or #configuration channel
2. "Gonka vs OpenRouter cost comparison" post with specific tier data and savings breakdown
3. Session persistence tutorial: "How to set up Gonka sessions for your always-on agent"

### P1 Channels

**Technical Blog (docs.gonka.ai/blog)**
1. "Cut Agent Inference Costs 73% with Gonka" -- launch post with heartbeat math, session persistence explanation, before/after cost comparison, config snippet
2. "OpenClaw + Gonka in 5 Minutes" -- quickstart guide with screenshots, curl verification, cost dashboard walkthrough
3. "Agent Sessions: Why Your Agent Pays for Context Twice" -- deep-dive explaining why heartbeats waste tokens, how sessions fix it, and the architectural difference vs prompt caching

**Twitter/X AI Developer Community**
1. Launch thread: heartbeat overhead problem + session persistence solution + cost comparison graphic + config snippet
2. Benchmark graphic: Kimi K2.7-Code / K3 vs GPT-5.x vs Claude Fable 5 / Opus 4.8 on coding and tool calling, with per-token cost comparison
3. "90-second setup" video clip: screen recording of adding Gonka to openclaw.json and making first call

**Reddit (r/LocalLLaMA, r/OpenClaw)**
1. "I compared OpenRouter, Together AI, and Gonka for my OpenClaw agent -- here are the real costs" comparison post with token math
2. "Show r/LocalLLaMA: Gonka -- agent-native inference with server-side sessions" launch post with config snippet
3. Monitoring + responses to "how do I reduce OpenClaw costs?" threads with specific data and config snippets

**dev.to / Hashnode**
1. Cross-posted "OpenClaw + Gonka in 5 Minutes" quickstart
2. Cross-posted "Cut Agent Inference Costs 73%" comparison post
3. "How to Add Session Persistence to Your OpenClaw Agent" tutorial adapted for dev.to format

---

## Measurement Cadence

### Weekly Review

- **API key signups:** total new signups, source attribution (which channel referred them)
- **First-call-within-24h rate:** percentage of new signups who make their first API call within 24 hours
- **Channel-specific engagement:** Reddit upvotes/comments, Twitter referral clicks, Discord Gonka mentions, blog unique visitors
- **Content performance:** which content pieces drove signups vs which drove only views

### Monthly Review

- **API-active developer count:** developers with >100 API calls in the past 30 days (the primary KPI)
- **Retention rate:** percentage of last month's API-active developers who remain API-active this month
- **Content-to-signup funnel:** full funnel from content view to signup to first call to API-active status, by content piece
- **Channel ROI ranking:** channels ranked by API-active developers attributed, not by engagement metrics
- **Session adoption rate:** percentage of API-active developers using the sessions API (indicates agent-native feature adoption)

### Quarterly Review

- **70/30 split audit:** actual channel investment (time, money, content pieces) measured against the 70/30 AI-dev/crypto target -- adjust if drifting
- **Persona reach assessment:** are all three personas being reached, or has content skewed to one? Check referral sources against persona indicators
- **Channel promotion/demotion:** should any P2 channel be promoted to P1 based on conversion data? Should any P1 channel be demoted?
- **Content theme effectiveness:** which message house value propositions (VP1-VP5) generate the most API-active developer conversions? Double down on winners
- **Quarterly content plan:** set next quarter's content calendar based on this quarter's data, maintaining AAARRRP stage allocation appropriate to the growth phase

---

*Document: gonka_channel_strategy.md | Version 1.3 | 2026-07-18*
*Dependencies: gonka_developer_personas.md (Phase 16), gonka_message_house.md (Phase 17), gonka_objection_playbook.md (Phase 17)*
*Sources: ARCHITECTURE.md (Component 4), PITFALLS.md, gonka_competitive_feature_matrix.md, gonka_agent_pricing_analysis.md*

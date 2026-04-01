# Gonka Channel Strategy: Reaching OpenClaw Developers

**Version:** 1.0
**Date:** 2026-04-01
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
**URL:** openclaw.dev/docs (or equivalent official docs)

**Why P0:** The provider directory is where developers go when they decide to add, change, or evaluate inference providers. If Gonka is not listed with a working configuration snippet, it does not exist to the OpenClaw developer. This is the single highest-leverage channel -- zero marginal cost, permanent presence, direct access to the moment of provider decision.

**Primary persona(s):** All three personas. Every developer who configures a custom provider checks the docs first.

**Content types:**
- Provider listing page with `openclaw.json` configuration snippet (3 fields: `baseUrl`, `apiKey`, `api: "openai-completions"`)
- Model card for `gonka/kimi-k2.5` with capabilities, context window (131K), and benchmark summary
- Troubleshooting guide addressing the two-step provider gotcha (provider definition + model allowlisting)

**Cadence:** Always available; updated with each Gonka feature release.

**Success metric:** Provider page views; percentage of page visitors who create a Gonka API key within 7 days.

**Example content piece:** "Gonka Provider Configuration" page with a copy-paste-ready `openclaw.json` block, a "verify it works" curl command, and a link to the quickstart guide. No mention of tokens, mining, or decentralization -- pure API configuration.

---

### OpenClaw GitHub (Issues, Discussions, PRs)

**Platform:** GitHub -- github.com/openclaw (organization repos)
**URL:** OpenClaw main repository issues, discussions, and PRs

**Why P0:** OpenClaw's GitHub is where active developers report issues, request features, and discuss provider options. Developers who search "custom provider" or "cheaper inference" in GitHub issues will find (or not find) Gonka. A merged PR adding Gonka as a built-in provider would eliminate the manual configuration barrier that currently makes OpenRouter the path of least resistance.

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
**URL:** OpenClaw community Discord server

**Why P0:** OpenClaw Discord is the real-time community where developers ask for help, share configurations, and discuss provider experiences. The Weekend Builder who is frustrated with their OpenRouter bill at 11pm on a Saturday asks for help here, not on Hacker News. Presence in this channel means being part of the conversation when provider decisions happen organically.

**Primary persona(s):** Weekend Builder (asks for help with costs and configuration), Privacy-First Builder (discusses provider privacy guarantees).

**Content types:**
- Pinned Gonka configuration snippet in the relevant channel (e.g., #providers or #configuration)
- Responses to cost-related questions with specific savings data (heartbeat overhead reduction)
- Troubleshooting help for developers configuring Gonka as a custom provider
- Session persistence explainers when developers ask about reducing agent costs

**Cadence:** Daily presence; respond to relevant questions within 4 hours during active hours.

**Success metric:** API key signups attributed to Discord conversations; number of developers who mention using Gonka in Discord.

**Example content piece:** Response to "my agent costs $40/month on OpenRouter and it only handles 50 messages/day": "Half your bill is heartbeats -- your agent resends full context every 30 minutes. Gonka keeps context server-side, so heartbeats send only new data. Same agent, same code, one config change -- your bill drops to ~$13/month. Here is the config: [snippet]."

---

## P1 Channels

P1 channels have broad reach into AI developer communities but require content creation investment. These channels build awareness beyond the OpenClaw ecosystem and establish Gonka's credibility through technical content.

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
- Benchmark results: K2.5 performance on SWE-Bench, tool calling stability, latency measurements

**Cadence:** Weekly (1 post per week minimum).

**Success metric:** Blog-to-signup conversion rate (readers who create API keys within 7 days); organic search traffic growth.

**Example content piece:** "Cut Agent Inference Costs 73% with Gonka" -- a launch post that walks through the heartbeat overhead problem (with token math from the pricing analysis), shows the session persistence solution, includes a before/after cost comparison at the Casual and Active tiers, and ends with a 90-second config snippet.

---

### Twitter/X AI Developer Community

**Platform:** Twitter/X
**URL:** twitter.com/gonka_ai (or equivalent)

**Why P1:** Twitter/X has the largest concentration of AI developers discussing inference providers, model benchmarks, and agent frameworks in real time. The AI developer Twitter community (accounts like @_philschmid, @kaboroevich, @laboroai) drives conversations about model quality and infrastructure costs that reach tens of thousands of developers. Gonka's benchmark results and cost comparisons are shareable Twitter content by nature.

**Primary persona(s):** All three personas discover content on Twitter, but Weekend Builder and Privacy-First Builder are most likely to engage with cost and privacy threads respectively.

**Content types:**
- Benchmark result graphics: K2.5 vs GPT-4o vs Claude on SWE-Bench, tool calling, agent tasks
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

**Why P1:** Reddit is where OpenClaw developers discover new providers through organic community discussion. r/LocalLLaMA (1M+ subscribers) is the largest community of developers interested in open-source model inference. r/OpenClaw hosts direct provider comparison discussions. The Weekend Builder persona's primary adoption trigger is seeing a cost comparison post on Reddit (developer personas: Weekend Builder, Adoption Triggers).

**Primary persona(s):** Weekend Builder (primary -- discovers through cost comparison posts), Privacy-First Builder (secondary -- discusses privacy in technical subreddits).

**Content types:**
- Provider comparison posts: "I compared OpenRouter, Together AI, and Gonka for my OpenClaw agent -- here are the real costs"
- Launch posts: "Show r/LocalLLaMA: Gonka -- agent-native inference with server-side sessions"
- Help responses: answers to "how do I reduce my OpenClaw inference costs?" threads
- AMA or Q&A posts addressing developer questions about K2.5, sessions, privacy

**Cadence:** 2-3 posts/responses per week; daily monitoring for relevant threads.

**Success metric:** Upvotes (indicates community validation) plus API key signups from Reddit referral links.

**Example content piece:** Post in r/LocalLLaMA: "I tracked my OpenClaw agent costs for a month -- heartbeats were 51% of my bill. Switching to a provider with session persistence dropped my Active tier cost from $218/month to $59/month. Here is the config and full cost breakdown: [link]."

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

**Platform:** Token2049, ETHDenver, AI Engineer Summit, NeurIPS Industry Day
**URL:** Various conference venues

**Why P3:** Conferences provide high-quality networking with Startup CTOs and enterprise decision-makers, but cost $5,000-50,000+ per event (travel, sponsorship, booth). ROI is uncertain until Gonka has published pricing, case studies, and a production track record to present. P3 because prerequisites are not met.

**Primary persona(s):** Startup CTO (evaluates at conferences), Privacy-First Builder (attends security/privacy-focused events).

**Content types:**
- Technical talks: "Agent-Native Inference: Why Sessions Matter More Than Per-Token Pricing"
- Live demos: OpenClaw agent running on Gonka with real-time cost dashboard
- Booth conversations with pre-qualified leads

**Cadence:** Quarterly (1-2 conferences per quarter once prerequisites are met).

**Success metric:** Conference-to-API-key conversion within 30 days (not badge scans or booth traffic).

**Example content piece:** 20-minute talk at AI Engineer Summit: "The Hidden Cost of Agent Heartbeats" with live demo showing session persistence reducing costs in real time.

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

**Example content piece:** "Gonka Host Guide: Earn GNK by serving K2.5 inference on your H100" -- a guide targeting GPU operators in DePIN communities, using crypto-native vocabulary per Phase 17 context rules.

---

## 70/30 Split Analysis

### Channel Allocation

Gonka's channel investment follows a 70/30 split: 70% of effort on AI/developer channels (where OpenClaw builders spend time) and 30% on crypto channels (where GPU hosts and token holders engage).

| Category | Channels | % of P0+P1 Investment | Rationale |
|----------|---------|----------------------|-----------|
| **AI/Developer (70%)** | OpenClaw Provider Directory, OpenClaw GitHub, OpenClaw Discord, Technical Blog, Twitter/X AI Community, Reddit, dev.to/Hashnode | ~75% of P0+P1 channels | These channels reach the developers who will become API-active users. Developer adoption drives inference demand, which drives network value, which attracts GPU hosts. The flywheel starts with developers. |
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

# Gonka Product-Led Growth Model

**Version:** 1.0
**Date:** 2026-04-01
**Classification:** Internal -- actionable growth model for Gonka developer acquisition
**Dependencies:** Phase 15 (competitive analysis), Phase 16 (developer personas), Phase 17 (messaging), Phase 18 (channel strategy), Phase 19 (partnership playbook)
**Requirement:** GTM-03

---

## Executive Summary

This document synthesizes all Phase 15-19 research into a single actionable growth model for Gonka's developer adoption. It defines the PLG funnel (how developers move from discovery to payment), the free tier design spec (what developers get without paying), and the time-to-first-inference plan (how developers go from zero to their first API response in under 5 minutes).

Every conversion rate, usage limit, and design decision is grounded in evidence from the research corpus. Where data is indirect (industry benchmarks rather than Gonka-specific measurements), confidence levels are noted. The model is designed so that leadership can read this document and know exactly what Gonka must build, what the targets are, and how to measure progress.

All developer-facing copy in this document follows the Phase 17 vocabulary guidelines (gonka_message_house.md Section 6). No terms from the 16-item never-say list appear in any developer-facing recommendation.

---

## PLG Funnel Model

### Funnel Overview

The PLG funnel maps Gonka's developer acquisition to the AAARRRP framework from Phase 16 (gonka_developer_personas.md). Six stages capture the complete journey from first encounter to paying customer, with each stage producing a measurable outcome and a clear handoff to the next.

| Stage | AAARRRP | Definition | Target Rate | Metric |
|-------|---------|------------|-------------|--------|
| **Discover** | Awareness | Developer encounters Gonka through OpenClaw ecosystem channels, Reddit, GitHub, or technical content | -- (top of funnel) | Unique visitors to docs.gonka.ai |
| **Explore** | Acquisition | Developer visits documentation, reads quickstart guide, reviews pricing page | 40-50% of Discover | Page views on docs.gonka.ai; time on site > 2 minutes |
| **Sign Up** | Acquisition | Email-only API key creation -- no wallet, no OAuth, no credit card | 15-25% of Explore | API keys created per week |
| **First Inference** | Activation | First successful API call through Gonka network | 70-80% of Sign Up | First API call within 24 hours of signup |
| **Habitual Use** | Retention | 100+ API calls in 30 days -- developer has integrated Gonka into a real workflow | 20-30% of First Inference | API-active developers per month (gonka_channel_strategy.md primary KPI) |
| **Paid Conversion** | Revenue | Developer exceeds free tier limits and upgrades to paid plan | 5-10% of Habitual Use | Paying users; monthly revenue per user |

**Why these rates:** The target conversion rates are calibrated against developer tool industry benchmarks (Stripe, Twilio, and Vercel report 10-25% signup-to-activation rates; Gonka targets higher because the activation step is a single config paste, not an SDK integration). The 5-10% paid conversion rate reflects the typical PLG pattern where most value is delivered free and only production-scale workloads trigger payment (gonka_developer_personas.md: Weekend Builder stays on free tier; Startup CTO converts to paid).

### Per-Persona Conversion Drivers

Each funnel stage has a different primary driver depending on the developer persona. Understanding these drivers determines what content, features, and messaging to prioritize at each stage.

#### Stage 1: Discover

| Persona | Primary Conversion Driver | #1 Drop-off Risk | Mitigation |
|---------|--------------------------|-------------------|------------|
| **Weekend Builder** | Reddit r/LocalLLaMA cost comparison post showing Gonka's heartbeat savings vs OpenRouter ($40/mo to $13/mo) | "Never heard of Gonka -- is this a crypto scam?" Landing page looks like a DeFi protocol | Landing page must resemble Vercel/Supabase, not a token project. Lead with "Cut your agent costs by 73%" not "Decentralized AI inference" (gonka_message_house.md VP1; PITFALLS.md Pitfall 1) |
| **Startup CTO** | Hacker News technical deep-dive on agent heartbeat overhead problem with Gonka cited as the session persistence solution | "Decentralized infrastructure means unreliable. Akash and Render both failed at scale" | Technical white paper with uptime data and p95 latency benchmarks. Must read like a Cloudflare blog post, not a crypto whitepaper (gonka_developer_personas.md Startup CTO Awareness stage) |
| **Privacy-First Builder** | GitHub repository README or technical article on privacy-preserving inference architectures, found while researching alternatives to self-hosted vLLM | "Every cloud provider claims no logging. How is Gonka different architecturally?" | Honest capabilities page: current guarantees (no central log aggregation, open-weight model, no content filtering) vs roadmap (TEE-based encrypted inference) (gonka_developer_personas.md Privacy-First Awareness stage) |

**Source:** gonka_developer_personas.md AAARRRP Journey Maps, Awareness stage for each persona.

#### Stage 2: Explore

| Persona | Primary Conversion Driver | #1 Drop-off Risk | Mitigation |
|---------|--------------------------|-------------------|------------|
| **Weekend Builder** | Quickstart page showing the 3-field openclaw.json snippet with a copy button -- "Add Gonka in 90 seconds" | Page mentions tokens, staking, or wallet before showing the config snippet | Docs homepage leads with the config snippet, not network architecture. Follow never-say list (gonka_message_house.md Section 6.1) |
| **Startup CTO** | Architecture overview explaining reliability through redundant nodes and health-checked routing, plus a cost comparison calculator | Docs lack uptime data, SLA information, or team account management | Enterprise evaluation page with p95 latency data, multi-key team accounts, and architecture explanation using cloud infrastructure language (gonka_developer_personas.md Startup CTO Acquisition stage) |
| **Privacy-First Builder** | Data handling policy page and open-source infrastructure code link (github.com/mitgor/gonka-ai-infrastructure) -- reviewable before signup | Privacy documentation is vague or makes claims without architectural backing | Published data handling policy: what is logged, what is not, retention periods, node operator agreements. Link to open-source code for independent audit (gonka_developer_personas.md Privacy-First Acquisition stage) |

**Source:** gonka_developer_personas.md AAARRRP Journey Maps, Acquisition stage for each persona.

#### Stage 3: Sign Up

| Persona | Primary Conversion Driver | #1 Drop-off Risk | Mitigation |
|---------|--------------------------|-------------------|------------|
| **Weekend Builder** | Single-CTA "Get API Key" button leading to email-only form. API key displayed immediately after email verification. Zero friction | Form asks for company name, use case, or any information beyond email address | Minimal form: email only. Verification link sent instantly. API key displayed on verification page with one-click copy. No approval queue, no waitlist (CONTEXT.md locked decision: email-only signup) |
| **Startup CTO** | Team account creation with multiple API keys for dev/staging/prod environments. Architecture docs reviewable pre-signup | Signup requires individual accounts for each team member; no team management | Team signup flow: one email creates team account, generates scoped API keys per environment. Billing attached to team, not individual (gonka_developer_personas.md Startup CTO Acquisition stage) |
| **Privacy-First Builder** | Data handling policy reviewed and satisfactory before email submission. Open-source code independently auditable | Privacy policy is generic boilerplate that does not address inference-specific concerns (prompt logging, content filtering, data residency) | Inference-specific privacy policy linked prominently on signup page. "We do not log your prompts" with architectural explanation, not just a policy claim (gonka_developer_personas.md Privacy-First Acquisition stage) |

**Source:** gonka_developer_personas.md AAARRRP Journey Maps; CONTEXT.md decisions.

#### Stage 4: First Inference

| Persona | Primary Conversion Driver | #1 Drop-off Risk | Mitigation |
|---------|--------------------------|-------------------|------------|
| **Weekend Builder** | Pre-built openclaw.json snippet on docs page with copy button. "Add Gonka to OpenClaw in 90 seconds" tutorial | The two-step provider gotcha: developer defines provider but forgets to add model to agent allowlist, causing silent failure | Quickstart guide explicitly shows both steps (provider definition AND model allowlisting) with a troubleshooting section for the gotcha (STACK.md Section 1: provider selection is a TWO-STEP process) |
| **Startup CTO** | Integration test results from v1.2 showing OpenClaw, CrewAI, and LangGraph compatibility. Staging deployment guide | First test request times out or returns unexpected error, destroying trust at first contact | Sub-200ms p95 latency on first call. Clear error messages with actionable troubleshooting. Integration test suite available for the team to run against their staging environment (gonka_developer_personas.md Startup CTO Activation stage; PITFALLS.md Pitfall 3) |
| **Privacy-First Builder** | Test prompt that would be blocked by OpenAI/Anthropic content filters completes successfully on Gonka. Aha moment: "It processed my prompt without filtering" | First prompt triggers an unexpected error or content filter, contradicting "no content policy" claim | K2.5 is open-weight with no built-in content filtering. Verify no content filtering middleware in the gateway. Test with adversarial prompts during QA (gonka_competitive_feature_matrix.md: Content filtering -- Gonka "None (open)") |

**Source:** gonka_developer_personas.md AAARRRP Journey Maps, Activation stage; STACK.md.

#### Stage 5: Habitual Use

| Persona | Primary Conversion Driver | #1 Drop-off Risk | Mitigation |
|---------|--------------------------|-------------------|------------|
| **Weekend Builder** | Usage dashboard showing session persistence savings: "$40/month on OpenRouter vs $13/month on Gonka for the same agent." Cost comparison is visceral and shareable | After initial excitement, the developer forgets about Gonka and defaults back to OpenRouter because it is built-in | Weekly email digest showing cost savings. X-Gonka-Usage-Remaining header in every response keeps savings visible. Cost comparison calculator in dashboard (gonka_developer_personas.md Weekend Builder Retention stage) |
| **Startup CTO** | Weekly cost report showing session persistence savings across all agents. Gradual migration from 2 agents to 4 to all 6 as confidence builds | One timeout or error during production usage triggers revert to previous provider. First impressions are permanent for infrastructure trust | Real-time status page (status.gonka.ai) with per-model availability and historical uptime. Incident report publication process. Gradual migration path with dual-provider configuration (gonka_developer_personas.md Startup CTO Retention stage; PITFALLS.md Pitfall 3) |
| **Privacy-First Builder** | Ongoing use for sensitive workloads with periodic privacy posture auditing via open-source verification tools | Gonka updates terms of service or infrastructure in a way that weakens privacy guarantees without communicating the change | Privacy-specific changelog (separate from feature releases). Automated privacy audit tool. Community-maintained watchdog (gonka_developer_personas.md Privacy-First Retention stage) |

**Source:** gonka_developer_personas.md AAARRRP Journey Maps, Retention stage.

#### Stage 6: Paid Conversion

| Persona | Primary Conversion Driver | #1 Drop-off Risk | Mitigation |
|---------|--------------------------|-------------------|------------|
| **Weekend Builder** | Exceeds free tier credit ($5-10 trial). Clear pricing page showing per-token rates with session savings calculator. Credit card entry with spending cap | Fear of runaway costs -- "OpenClaw agents can spike unpredictably, $300+ in 2 days" | Configurable daily spending cap. Usage alerts at 50%, 80%, 100% of limit. "No surprise bills" guarantee. Pricing comparison table: Gonka vs OpenRouter vs Together AI at Casual tier (gonka_developer_personas.md Weekend Builder Revenue stage) |
| **Startup CTO** | Commits to paid plan after 2-4 weeks of staging + gradual production rollout. Volume pricing for 161M+ tokens/month | Needs formal SLA with downtime credits to justify to co-founder and investors | Enterprise pricing tier with committed-use discounts. SLA framework: 99.5% uptime target with credit mechanism. Invoice and receipt system for accounting (gonka_developer_personas.md Startup CTO Revenue stage; gonka_competitive_feature_matrix.md Section 7) |
| **Privacy-First Builder** | Converts to paid plan valuing session persistence for reducing how often sensitive context traverses the network. Willing to pay premium for TEE when available | No privacy-specific pricing tier or TEE timeline commitment | Privacy tier with optional TEE-backed inference at premium when available. Roadmap commitment on encrypted inference with quarterly updates. Early access program for privacy beta features (gonka_developer_personas.md Privacy-First Revenue stage) |

**Source:** gonka_developer_personas.md AAARRRP Journey Maps, Revenue stage; gonka_agent_pricing_analysis.md.

### Funnel Math

If 1,000 developers discover Gonka (visit docs.gonka.ai or encounter Gonka in the OpenClaw ecosystem), here is how many become paying users at each scenario:

| Stage | Pessimistic | Target | Optimistic |
|-------|-------------|--------|------------|
| **Discover** | 1,000 | 1,000 | 1,000 |
| **Explore** (40-50% of Discover) | 400 | 450 | 500 |
| **Sign Up** (15-25% of Explore) | 60 | 90 | 125 |
| **First Inference** (70-80% of Sign Up) | 42 | 67 | 100 |
| **Habitual Use** (20-30% of First Inference) | 8 | 17 | 30 |
| **Paid Conversion** (5-10% of Habitual Use) | 0.4 (~0) | 1.3 (~1) | 3 |

**Interpretation:**

- **Pessimistic:** ~0.04% end-to-end conversion. From 1,000 developers who discover Gonka, zero to one becomes a paying customer. This scenario reflects a cold start with no ecosystem presence, minimal content, and the crypto perception barrier fully active. Recovery requires aggressive investment in P0 channels (OpenClaw Provider Directory, GitHub, Discord -- gonka_channel_strategy.md).

- **Target:** ~0.13% end-to-end conversion. From 1,000 discovers, approximately 1 paying user and 17 API-active developers generating usage data, cost savings testimonials, and referral potential. At the Month 6 target of 200 API-active developers (gonka_channel_strategy.md), this implies needing approximately 12,000 discover-stage developers.

- **Optimistic:** ~0.3% end-to-end conversion. From 1,000 discovers, 3 paying users and 30 API-active developers. Achievable if Gonka secures built-in OpenClaw provider status (Tier 3 in gonka_partnership_playbook.md), which eliminates the manual configuration friction at the Sign Up and First Inference stages.

**Key insight:** The funnel is widest at the top (Discover to Explore) and steepest at the Habitual Use stage. The 20-30% conversion from First Inference to Habitual Use is the critical gate -- this is where developers decide if Gonka's session persistence savings are real enough to justify switching from their default provider. The X-Gonka-Usage-Remaining header and cost comparison dashboard are the primary retention mechanisms at this stage.

**Revenue projection at target rates:**

- 17 API-active developers at Casual tier (~31.5M tokens/month each) at Scenario B pricing ($1.05/1M blended): ~$563/month total inference revenue
- 1 paying Startup CTO at Active tier (~161.5M tokens/month) at Scenario B pricing: ~$170/month
- Combined Month 6 revenue from 1,000 discover-stage cohort: ~$733/month

These projections use Scenario B pricing ($0.35/$1.75 per 1M tokens input/output) from gonka_agent_pricing_analysis.md. Revenue scales with discover-stage volume, which is driven by P0 channel investment (gonka_channel_strategy.md).

---

## Free Tier Design Spec

### Design Principles

The free tier must accomplish three goals simultaneously:

1. **Eliminate all friction for the Weekend Builder** -- generous enough that a solo developer running one agent on one channel can use Gonka indefinitely without paying, experiencing session persistence savings firsthand and becoming a referral source (gonka_developer_personas.md: Weekend Builder monthly spend $20-50 on OpenRouter; free tier must cover their reduced-cost Gonka usage)

2. **Create a natural upgrade trigger for the Startup CTO** -- limited enough that a team running multiple agents across channels hits the ceiling within their first week of serious evaluation, triggering the paid conversion conversation (gonka_developer_personas.md: Startup CTO monthly spend $200-500; free tier should cover approximately 1 agent, not 6)

3. **Remove the crypto barrier entirely** -- Email-only signup with no wallet, no token purchase, no OAuth complexity. The word "wallet" must never appear before "API key" on any page (gonka_message_house.md Section 6.1: Never-Say List -- "wallet" is the single most alienating word for Web2 developers)

### Signup Flow

```
Step 1: Developer lands on docs.gonka.ai
        Single CTA: "Get Your API Key" button
        No distracting navigation, no "Learn about our network" sidebar

Step 2: Email-only form
        One field: email address
        No company name, no use case, no phone number
        Submit button: "Send me my API key"

Step 3: Verification email arrives (target: under 60 seconds)
        Transactional email service (SendGrid, Postmark, or SES)
        Subject: "Your Gonka API Key"
        Body: One-click verification link, nothing else

Step 4: Developer clicks link, lands on key display page
        API key displayed prominently with one-click copy button
        Below the key: the exact openclaw.json snippet pre-filled with their key
        Below the snippet: "Paste this into ~/.openclaw/openclaw.json and you are done"

Step 5: Developer is using Gonka
        No approval queue. No waitlist. No manual review.
        Free tier limits active immediately.
```

**Per CONTEXT.md locked decision:** Email-only signup. No wallet or crypto knowledge required.

### Usage Limits

Free tier limits are calibrated against two data points:

1. **Competitor free tiers:** OpenRouter offers free-tier access with rate limiting and quality degradation under load. Google Gemini offers a generous free tier. No K2.5-specific free tier exists among compared providers (gonka_competitive_feature_matrix.md; gonka_provider_landscape_map.md Segment 3: Together AI and DeepInfra are pay-per-use only).

2. **Persona workload profiles:** The Weekend Builder consumes ~31.5M tokens/month at Casual tier with 30-minute heartbeats (gonka_agent_pricing_analysis.md Section 3). With Gonka's session persistence reducing effective token consumption by ~80%, the Weekend Builder's actual Gonka token usage would be approximately 12.6M tokens/month. The free tier should cover most of this.

| Limit | Free Tier Value | Rationale |
|-------|----------------|-----------|
| **Daily requests** | 1,000 requests/day | Covers 1 agent with 50 user messages + 150 tool calls + 48 heartbeats = ~248 requests/day. Generous buffer for burst testing. Startup CTO with 6 channel-agents needs ~1,488 requests/day -- exceeds limit within first day of serious evaluation (gonka_agent_pricing_analysis.md Section 3: Active tier daily breakdown) |
| **Monthly tokens** | 15,000,000 tokens/month | Covers Weekend Builder's session-optimized usage (~12.6M tokens/month) with headroom. Startup CTO at Active tier (~56.3M session-optimized tokens/month) exceeds this in week 1 (gonka_agent_pricing_analysis.md Section 5: Gonka hidden cost analysis) |
| **Concurrent sessions** | 2 active sessions | Covers 1 agent on 1-2 channels (Weekend Builder). Startup CTO with 6 channel-agents needs 6 concurrent sessions -- hits upgrade trigger immediately when deploying team workload |
| **Models available** | K2.5 lite and mid tiers only | Full-precision K2.5 reserved for paid tier. Lite and mid tiers are sufficient for the Weekend Builder's personal assistant workload. Startup CTO evaluating quality for production needs full tier access (gonka_competitive_feature_matrix.md: 3-tier K2.5 quantization) |
| **Rate limit** | 60 requests/minute | Prevents abuse while allowing burst testing (a developer testing their agent configuration may send 10-20 requests in quick succession). Production agents with 30-minute heartbeats generate ~1 request/minute baseline. 60 RPM provides comfortable headroom |
| **Context window** | 32,768 tokens | Reduced from K2.5's full 131,072. Sufficient for most agent workloads (system prompt + context is ~9,600 tokens). Startup CTO running complex multi-step workflows with deep context needs the full window |

### Upgrade Triggers

Three specific mechanisms notify developers when they approach or exceed free tier limits, driving paid conversion without hard-blocking their workflow:

**Trigger 1: Usage Limit Approaching**

When a developer reaches 80% of their daily request limit or monthly token limit, every API response includes a warning header:

```
X-Gonka-Usage-Remaining: 200
X-Gonka-Usage-Limit: 1000
X-Gonka-Usage-Reset: 2026-04-02T00:00:00Z
X-Gonka-Upgrade-URL: https://docs.gonka.ai/pricing
```

At 100%, requests return HTTP 429 with a clear message: "Free tier daily limit reached. Resets at midnight UTC. Upgrade at docs.gonka.ai/pricing for unlimited requests."

No cryptic error codes. No silent failures. The developer knows exactly what happened, when it resets, and how to fix it.

**Trigger 2: Session Limit Reached**

When a developer attempts to create a third concurrent session (free tier allows 2), the API returns HTTP 403 with:

```json
{
  "error": "session_limit_reached",
  "message": "Free tier supports 2 concurrent sessions. You have 2 active sessions. Upgrade to paid for unlimited sessions.",
  "current_sessions": 2,
  "max_sessions": 2,
  "upgrade_url": "https://docs.gonka.ai/pricing"
}
```

This trigger is designed specifically for the Startup CTO persona: they have proven Gonka works with 1-2 agents on staging and now want to add their production agents. The session limit creates a natural conversation point for team account and volume pricing discussion.

**Trigger 3: Model Tier Access**

When a developer requests the full-precision K2.5 model (available only on paid tier), the API routes to mid-tier K2.5 and includes a header:

```
X-Gonka-Tier-Served: mid
X-Gonka-Tier-Requested: full
X-Gonka-Tier-Upgrade: "Full-precision K2.5 available on paid tier. See docs.gonka.ai/pricing"
```

The request succeeds (no error) but with a lower-tier model, and the header transparently communicates the substitution. This avoids breaking the developer's workflow while making the quality difference discoverable.

### What Is NOT in the Free Tier

Features reserved for paid plans to create clear value differentiation:

| Feature | Free Tier | Paid Tier | Why Reserved |
|---------|-----------|-----------|--------------|
| **Full-precision K2.5** | No (lite and mid only) | Yes | Quality differentiation for production workloads |
| **Unlimited sessions** | 2 concurrent max | Unlimited | Multi-agent production requires paid commitment |
| **SLA guarantee** | Best effort | 99.5% uptime target with credits | SLA has cost implications; reserved for committed customers |
| **Priority routing** | Standard queue | Priority queue with dedicated capacity | Ensures paid customers get consistent low latency |
| **Webhook notifications** | No | Yes | Advanced agent feature for production use (gonka_competitive_feature_matrix.md: Tier 2 differentiator) |
| **Memory API** | No | Yes | Persistent key-value memory for long-running agents |
| **Usage API / Dashboard** | Basic (current usage only) | Full (historical trends, cost comparison, export) | Detailed analytics drive retention for paid users |
| **Team accounts** | No (individual only) | Yes (multi-key, scoped permissions) | Team management is an enterprise feature |
| **Spending caps** | N/A (free) | Configurable daily/monthly limits | Cost control for production workloads (addresses "$300+ in 2 days" fear -- gonka_developer_personas.md Weekend Builder Revenue stage) |

### Competitive Positioning of Free Tier

| Provider | Free Tier | Signup Friction | Limits |
|----------|-----------|-----------------|--------|
| **OpenRouter** | Free-tier access to select models | GitHub OAuth | Rate-limited; quality degraded under load; free requests queued behind paid (gonka_competitive_feature_matrix.md Section 5) |
| **Google Gemini** | Generous free tier | Google account | Rate limits vary by model; generous for experimentation |
| **Together AI** | No free tier | Credit card required | Pay-per-use only (gonka_provider_landscape_map.md Segment 3) |
| **DeepInfra** | No free tier | Credit card required | Pay-per-use only |
| **Gonka (proposed)** | 15M tokens/month, 1,000 requests/day, 2 sessions | Email only | Most generous free tier among K2.5 providers; lowest signup friction; session persistence active on free tier |

**Competitive advantage:** Gonka's free tier is the only one that (a) requires no credit card or OAuth, (b) includes session persistence (the primary cost-saving feature), and (c) provides enough capacity for a solo developer's always-on agent. The Weekend Builder can experience the full session persistence savings without paying, creating the cost comparison data point ("$40/month on OpenRouter vs free on Gonka") that drives organic referrals (gonka_developer_personas.md Weekend Builder Referral stage).

### Copy Guidelines

All developer-facing copy on signup pages, error messages, and upgrade prompts must follow the Phase 17 vocabulary guidelines (gonka_message_house.md Section 6). Specifically:

- **Never use:** wallet, staking, mining, DePIN, Web3, tokenomics, consensus mechanism, on-chain, smart contract, gas, slashing, governance proposals, epochs, validators, token (as cryptocurrency), decentralized (as headline)
- **Always use:** "API key" (not "wallet"), "account" (not "wallet"), "compute credits" (not "GNK tokens"), "GPU providers" (not "miners" or "validators")
- **Error messages:** Must be actionable and specific. "Free tier daily limit reached. Resets at midnight UTC." not "Insufficient GNK balance."

---

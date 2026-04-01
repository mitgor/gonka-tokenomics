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

## Time-to-First-Inference Plan

### Objective

Per CONTEXT.md locked decision: target under 5 minutes from email submission to first successful API response through the Gonka network. This is the single most important PLG metric -- every minute of friction between "I want to try Gonka" and "my agent is running on Gonka" loses developers who will never return (PITFALLS.md Pitfall 3: first impressions are permanent for infrastructure trust).

### Step-by-Step Breakdown

| Step | Action | Time Budget | Blocker Risk | What Must Be Built |
|------|--------|-------------|--------------|-------------------|
| 1 | Land on docs.gonka.ai | 0s (assumed) | Page must exist. Currently no docs site -- must-close gap from Phase 15 (gonka_provider_landscape_map.md: 5 critical gaps) | docs.gonka.ai with SSL, CDN, sub-2s page load. Single-page-app or static site (Hugo, Astro, or Next.js). Landing page with one CTA |
| 2 | Click "Get API Key" | 10s | Single CTA must be above the fold. No competing navigation, no "Learn about our network" distractions. Developer must not need to scroll to find the button | CTA button component. Landing page design that passes the "is this crypto?" test (gonka_message_house.md VP3; PITFALLS.md Pitfall 1) |
| 3 | Enter email, submit | 30s | Email-only form. No wallet creation, no OAuth redirect, no credit card. One field, one button. Any additional friction at this step causes the steepest drop-off in the funnel (gonka_developer_personas.md: 95% funnel drop at wallet step per PITFALLS.md Pitfall 2) | Email submission endpoint. Rate limiting on submissions (prevent abuse). CAPTCHA only if abuse is detected, not by default |
| 4 | Receive verification email | 60s | Must arrive within 60 seconds. Delayed verification emails (>2 minutes) cause developers to lose context and abandon. Use a transactional email service (SendGrid, Postmark, or AWS SES) with dedicated IP and domain authentication (SPF, DKIM, DMARC) to avoid spam folders | Email sending infrastructure. Transactional email template. Email deliverability monitoring |
| 5 | Click verification link, see API key | 15s | Key must be displayed immediately on the page with a one-click copy button. No "check your dashboard" redirect. No additional login step. The key is shown once, prominently, with a "Copy" button that provides visual confirmation | Key generation service. Key display page with clipboard API integration. Key storage (hashed) in database |
| 6 | Paste config into openclaw.json | 90s | The exact config snippet must be pre-filled with the developer's API key and ready to copy-paste. Show both steps of the two-step process (provider definition AND model allowlisting) to avoid the silent failure gotcha (STACK.md Section 1) | Pre-filled config snippet generator. Documentation page showing the exact JSON to paste |
| 7 | Send first message to agent | 60s | Agent responds via Gonka inference. The first response must arrive within 2-3 seconds (sub-200ms TTFT + streaming). Any timeout or error at this step permanently damages trust | Live API endpoint at api.gonka.ai. Health-checked GPU hosts. vLLM inference with K2.5 model loaded and warm |
| **Total** | | **~4 min 15s** | | |

### Step 6 Detail: The Config Snippet

After the developer copies their API key, the verification page displays the exact `openclaw.json` configuration they need to paste. This is not a generic template -- it is pre-filled with their specific API key:

```json5
// Step 1: Add this to your ~/.openclaw/openclaw.json under models.providers:
{
  "gonka": {
    "baseUrl": "https://api.gonka.ai/v1",
    "apiKey": "gnk_sk_abc123...",  // Your API key (already filled in)
    "api": "openai-completions",
    "models": [
      {
        "id": "kimi-k2.5",
        "name": "Kimi K2.5",
        "contextWindow": 131072,
        "maxTokens": 8192,
        "cost": { "input": 0.35, "output": 1.75 }
      }
    ]
  }
}

// Step 2: Add this to your agents.defaults.models to enable the model:
{
  "gonka/kimi-k2.5": { "alias": "k2.5" }
}
```

**Why both steps are shown:** OpenClaw requires both provider definition (Step 1) AND model allowlisting (Step 2). Missing Step 2 causes silent failure -- the agent ignores the provider entirely with no error message. This is a known gotcha in the OpenClaw community (STACK.md Section 1: "Missing either step causes silent failure"). Showing both steps on the same page with clear "Step 1" and "Step 2" labels prevents the most common configuration error.

**Config snippet format:** Based on the OpenClaw `openclaw.json` configuration format documented in STACK.md. The `api: "openai-completions"` value tells OpenClaw to use the standard `/v1/chat/completions` endpoint format, which Gonka's gateway already implements (shipped in v1.2). Cost values reflect Scenario B pricing ($0.35/$1.75 per 1M tokens input/output) from gonka_agent_pricing_analysis.md.

### Current Gaps vs Target Flow

| Step | Current Status | Gap | Engineering Work Required | Cross-Reference |
|------|---------------|-----|--------------------------|-----------------|
| 1 | No docs site exists | Must-close gap | Static site deployment (Hugo/Astro/Next.js) with domain, SSL, CDN | gonka_provider_landscape_map.md: critical gap #2 |
| 2 | No landing page exists | Must-close gap | Landing page design and implementation | gonka_provider_landscape_map.md: critical gap #2 |
| 3 | No signup flow exists | Must-close gap | Email submission API, rate limiting, form validation | gonka_provider_landscape_map.md: critical gap #3 |
| 4 | No email infrastructure | Must-close gap | Transactional email service integration, domain auth | New requirement (identified in this plan) |
| 5 | No key generation service | Must-close gap | API key generation, storage, display page | gonka_provider_landscape_map.md: critical gap #3 |
| 6 | Config snippet documented in STACK.md (research only) | Needs productization | Pre-filled snippet generator on docs site | gonka_partnership_playbook.md: requirement #13 |
| 7 | API endpoint exists (v1.2) but not publicly accessible | Must-close gap | Public deployment of api.gonka.ai with domain, SSL, health checks | gonka_provider_landscape_map.md: critical gap #1 |

**Key observation:** Steps 1-6 are entirely new engineering work. Only Step 7 (the actual inference) has existing infrastructure from v1.2. The entire developer onboarding flow -- from landing page to API key delivery -- must be built from scratch. This is why the gonka_provider_landscape_map.md identifies these as "not feature gaps but table-stakes infrastructure gaps that prevent developers from evaluating Gonka at all."

### The Atomic Growth Unit

The `openclaw.json` config snippet is Gonka's atomic growth unit -- the smallest shareable artifact that converts a non-user into a user.

**Why the config snippet is viral:**

1. **It is copy-pasteable.** A developer who has configured Gonka can share their provider config block (minus the API key) in a Reddit comment, Discord message, or GitHub issue. The recipient copies it, adds their own API key, and is running on Gonka in 90 seconds. No documentation reading required. No signup flow navigation. Just paste and go.

2. **It lives in version control.** `openclaw.json` is committed to Git repositories. When a developer adds Gonka as a provider, their teammates see the config change in the next pull request. The config snippet propagates through team workflows organically. When the Startup CTO adds Gonka to the team's shared config, all 3-8 engineers inherit it automatically (gonka_developer_personas.md: Startup CTO team size 3-8).

3. **It is portable across OpenClaw installations.** The same config snippet works on any OpenClaw deployment -- personal laptop, VPS, cloud server, Docker container. A developer who configures Gonka on their local machine can copy the same config to production. This portability means the snippet carries across environments without modification (STACK.md: OpenClaw's declarative configuration model).

4. **It embeds Gonka's cost advantage.** The `cost` field in the config snippet shows Gonka's per-token rates directly in the developer's configuration file. Every time a developer opens `openclaw.json`, they see Gonka's rates next to their other providers. If Gonka's rates are lower (Scenario B: $0.35/$1.75 vs Together AI: $0.50/$2.50 -- gonka_agent_pricing_analysis.md Section 4), the cost advantage is visible without visiting a pricing page.

5. **ClawHub skills amplify the snippet.** The Gonka Provider Skill submitted to ClawHub (gonka_partnership_playbook.md: ClawHub Submission Plan) teaches agents how to use Gonka-specific features. When a developer installs the skill, it includes the config snippet as part of the setup instructions. The skill and the snippet work together: the snippet connects the agent to Gonka, and the skill teaches the agent to use sessions, tiering, and memory (gonka_partnership_playbook.md: SKILL.md draft outline).

**The viral loop:**

```
Developer A configures Gonka (pastes config snippet)
  -> Saves 73% on heartbeat costs (session persistence)
  -> Shares cost comparison screenshot on Reddit/Twitter
  -> Developer B sees post, copies config snippet from comment
  -> Developer B configures Gonka in 90 seconds
  -> Developer B saves 73% on heartbeat costs
  -> Developer B shares their own comparison...
```

This loop is driven by the session persistence savings -- the cost reduction is dramatic enough (73% at Active tier -- gonka_agent_pricing_analysis.md Section 6) to motivate organic sharing, and the config snippet makes sharing frictionless. No referral program is needed to trigger the initial loop; the savings create natural word-of-mouth. The referral program (gonka_developer_personas.md Weekend Builder Referral stage: "$5 credit for each referred developer who makes 100+ API calls") amplifies an already-functioning viral mechanism.

### What Competitors Require

Gonka's time-to-first-inference target (under 5 minutes, email-only signup) creates a measurable friction advantage over the competitors that Weekend Builders and Startup CTOs are most likely evaluating.

#### OpenRouter (Weekend Builder's Current Provider)

| Step | OpenRouter Requirement | Time | Friction |
|------|----------------------|------|----------|
| 1 | Visit openrouter.ai | 0s | None |
| 2 | Click "Sign In" | 10s | None |
| 3 | GitHub OAuth login | 30-60s | Requires GitHub account. OAuth redirect. Permission grant screen. Some developers hesitate to grant OAuth permissions to unknown services |
| 4 | Credit card for paid tier | 120-180s | Credit card entry form. Address verification. Payment processing. **This step does not exist for Gonka's free tier** |
| 5 | Browse 500+ model catalog, select model | 60-120s | Model selection paralysis. "Which model do I pick?" No guidance for agent workloads. Developer must research models independently |
| 6 | Copy API key, configure application | 60-90s | API key is available immediately after signup (no email verification) |
| **Total** | | **~5-8 min (free tier) or ~8-12 min (paid)** | GitHub OAuth + credit card + model selection |

**Gonka advantage:** No OAuth, no credit card, no model selection paralysis. Gonka offers one model (K2.5) in three tiers with automatic routing -- the developer does not need to choose. Email-only signup eliminates the OAuth permission screen that causes hesitation. The free tier eliminates the credit card step entirely.

**Source:** gonka_competitive_feature_matrix.md (OpenRouter: 500+ models); gonka_developer_personas.md (Weekend Builder: OpenRouter is the default, zero-config provider).

#### Together AI (Startup CTO's Primary Alternative)

| Step | Together AI Requirement | Time | Friction |
|------|------------------------|------|----------|
| 1 | Visit api.together.ai | 0s | None |
| 2 | Click "Sign Up" | 10s | None |
| 3 | OAuth login (Google or GitHub) | 30-60s | OAuth redirect. Permission grant. Account creation |
| 4 | Credit card required for all usage | 120-180s | No free tier. Credit card is mandatory. Some developers abandon at this step for evaluation purposes |
| 5 | Select model from 200+ catalog | 60-120s | Less paralysis than OpenRouter (200 vs 500+ models) but still requires research. K2.5 is one of many options |
| 6 | Copy API key, configure application | 60-90s | API key generation is straightforward |
| **Total** | | **~5-8 min** | OAuth + mandatory credit card + model selection |

**Gonka advantage:** No credit card requirement (free tier exists). No model selection step (K2.5 with auto-tiering). Email-only signup (no OAuth). The Startup CTO can evaluate Gonka on staging without entering payment information or requesting procurement approval from their finance team.

**Source:** gonka_agent_pricing_analysis.md Section 4 (Together AI pricing: $0.50/$2.50); gonka_provider_landscape_map.md Segment 3 (Together AI: pay-per-use only, no free tier).

#### Self-Hosted vLLM (Privacy-First Builder's Current Approach)

| Step | vLLM Self-Hosting Requirement | Time | Friction |
|------|------------------------------|------|----------|
| 1 | Acquire GPU hardware ($2,000-10,000+) | Days to weeks | Hardware procurement. Budget approval. Delivery time |
| 2 | Install CUDA, Python, vLLM | 30-60 min | Driver compatibility issues. Python environment management. Dependency conflicts |
| 3 | Download K2.5 model weights | 20-60 min | Model weights are 10-50 GB depending on quantization. Requires HuggingFace account. Network bandwidth dependent |
| 4 | Configure vLLM server | 15-30 min | Configuration options for GPU memory, quantization, batch size. Trial and error for optimal settings |
| 5 | Start server, verify inference works | 5-10 min | Health checks, first inference warm-up, verify output quality |
| 6 | Configure OpenClaw to point to local vLLM | 5-10 min | Same openclaw.json config as Gonka, but with localhost URL |
| **Total** | | **Hours to days** | Hardware + software + model download + configuration |

**Gonka advantage:** Under 5 minutes vs hours to days. No hardware procurement. No driver installation. No model download. The Privacy-First Builder gets the same open-weight K2.5 model with no content filtering, served on distributed infrastructure with no central logging -- and they can start using it in 4 minutes instead of 4 hours. The tradeoff: Gonka's privacy guarantees are architectural (no central log aggregation) rather than absolute (no TEE yet). The honest capabilities page (gonka_developer_personas.md Privacy-First Activation stage) communicates this clearly.

**Source:** gonka_developer_personas.md Privacy-First Pain Point #2 (self-hosting costs and maintenance); gonka_competitive_feature_matrix.md (K2.5: open-weight, no content filtering).

### Failure Modes and Recovery

Each step in the time-to-first-inference plan has a specific failure mode that would break the under-5-minute target. These must be engineered against:

| Step | Failure Mode | Impact | Prevention |
|------|-------------|--------|------------|
| 3 | Email submission rate-limited or blocked by spam filter | Developer cannot sign up | Use transactional email service with dedicated IP. Monitor deliverability rates. Provide "did not receive email?" link with resend option |
| 4 | Verification email delayed >2 minutes | Developer loses context, opens new tab, forgets about Gonka | Alert on email delivery latency >30s. Use multiple email service providers with failover. Display "email sent, check your inbox" with a countdown timer |
| 5 | API key page fails to load or copy button does not work | Developer cannot retrieve their key | Client-side key display (no server round-trip after page load). Fallback: display key as selectable text if clipboard API fails. Email the key as backup |
| 6 | Developer pastes config but misses Step 2 (model allowlisting) | Silent failure -- agent ignores Gonka provider entirely | Show both steps on the same page with numbered instructions. Verification endpoint: `GET /v1/verify` that returns 200 if the key is valid, helping developers test before configuring their agent |
| 7 | First API call times out or returns 500 | Permanent trust damage -- developer will not try again (PITFALLS.md Pitfall 3) | Health-checked routing ensures requests go only to responsive nodes. Cold-start mitigation: keep K2.5 warm on minimum N nodes. Error response includes troubleshooting link |

---

## Cross-References

Every claim in this document traces to a specific Phase 15-19 output document. This section lists each source and what was drawn from it.

| Document | What Was Used |
|----------|---------------|
| **gonka_developer_personas.md** (Phase 16) | Three personas (Weekend Builder, Startup CTO, Privacy-First Builder) with decision drivers, pain points, adoption triggers, objections, and complete AAARRRP journey maps. Per-persona conversion drivers at each funnel stage. Drop-off risk analysis. Referral mechanisms. |
| **gonka_agent_pricing_analysis.md** (Phase 15) | Workload tier definitions (Casual: 31.5M tokens/month, Active: 161.5M, Heavy: 2.94B). Heartbeat overhead percentages (44%, 51%, 85%). Scenario B pricing ($0.35/$1.75). Session persistence savings (80% token reduction). Monthly cost projections per provider per tier. Competitor pricing data (Together AI, DeepInfra, OpenRouter, OpenAI, Anthropic). |
| **gonka_competitive_feature_matrix.md** (Phase 15) | 8-dimension competitive comparison. WIN verdicts on Agent Sessions and Model Tiering. LOSE verdicts on Model Breadth and Uptime/Reliability. Competitor free tier analysis. Content filtering comparison (Gonka: "None (open)"). K2.5 quantization tiers. |
| **gonka_provider_landscape_map.md** (Phase 15) | 5 critical must-close gaps (not built-in provider, no docs site, no self-serve signup, no pricing page, in-memory sessions). 4-segment landscape framework. Gonka's unique position as only decentralized provider with agent-native extensions. |
| **gonka_message_house.md** (Phase 17) | Core positioning statement (73% cost reduction via session persistence). 16-item never-say list. Approved vocabulary mapping. VP1-VP3 ranked value propositions. Competitive differentiation statements per persona. |
| **gonka_channel_strategy.md** (Phase 18) | Primary KPI: API-active developers (>100 calls/month). Target trajectory (10 Month 1, 50 Month 3, 200 Month 6, 1000 Month 12). 70/30 channel split. P0 channels (OpenClaw Provider Directory, GitHub, Discord). Anti-metrics (follower counts, Discord members, GitHub stars). |
| **gonka_partnership_playbook.md** (Phase 19) | Four-tier OpenClaw integration roadmap (Listed -> Plugin -> Built-In -> Preferred). ClawHub submission plan. Technical requirements checklist (33 items). Community-first PR strategy timeline (3-6 months). |
| **gonka_objection_playbook.md** (Phase 17) | ACE objection framework. 12 documented objections with persona mapping. P0 severity objections: awareness, crypto perception, SLA gap, prompt privacy. |
| **gonka_agent_native_pitch.md** (Phase 17) | Agent-as-customer thesis. 7 task profiles with provider match analysis. Gonka wins 3/7 (long-running agents, multi-agent systems, privacy-sensitive). |
| **.planning/research/STACK.md** | OpenClaw `openclaw.json` configuration format. Two-step provider selection process (provider definition + model allowlisting). Built-in vs custom provider distinction. Key rotation and failover behavior. |

---

*Document: gonka_plg_growth_model.md | Version 1.0 | 2026-04-01*
*Capstone deliverable for Phases 15-19. Companion document: gonka_v14_engineering_backlog.md (Plan 20-02)*

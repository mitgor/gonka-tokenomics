# Phase 16: Developer Personas & Journey Mapping - Research

**Researched:** 2026-04-01
**Domain:** B2D developer persona development and journey mapping for decentralized AI inference
**Confidence:** HIGH

## Summary

Phase 16 produces developer persona cards and AAARRRP journey maps for OpenClaw builders considering Gonka as their inference provider. This is a research/analysis phase -- no code, no software. The deliverables are analytical documents grounded in community signals from the OpenClaw ecosystem.

The prior phases (15) produced a competitive feature matrix, pricing analysis, and provider landscape map that contain rich data on developer decision criteria, cost profiles, pain points, and competitive positioning. These existing assets provide the factual foundation for persona construction. The persona phase synthesizes this data into actionable archetypes that downstream phases (17: Messaging, 18: Channels) consume directly.

**Primary recommendation:** Build 3-4 personas differentiated by workload scale and decision driver priority (cost vs features vs privacy), each with a full AAARRRP journey map. Ground every claim in the existing research corpus rather than inventing hypothetical developer profiles.

<user_constraints>

## User Constraints (from CONTEXT.md)

### Locked Decisions
- Create at least 3 distinct developer persona cards grounded in community signals from GitHub, Discord, and Reddit
- Each persona must include: profile, decision drivers, pain points, adoption triggers
- Personas should reflect the Web2-native audience finding from research (not crypto-native assumptions)
- Use AAARRRP framework (Awareness, Acquisition, Activation, Revenue, Retention, Referral, Product)
- Map objections at each stage per persona
- Validate decision driver rankings against real OpenClaw community discussions
- Reference competitive gaps from output/gonka_competitive_feature_matrix.md to inform persona pain points
- Use pricing analysis from output/gonka_agent_pricing_analysis.md for cost-driven personas

### Claude's Discretion
All formatting, persona naming, and analytical framework details are at Claude's discretion.

### Deferred Ideas (OUT OF SCOPE)
None.

</user_constraints>

## Standard Stack

This is a research/analysis phase. No libraries or software tools are needed.

### Core Inputs (Existing Assets)
| Asset | Location | What It Provides |
|-------|----------|-----------------|
| Competitive Feature Matrix | `output/gonka_competitive_feature_matrix.md` | 8-dimension comparison, Gonka wins/losses, key takeaways |
| Agent Pricing Analysis | `output/gonka_agent_pricing_analysis.md` | 3 workload tiers (Casual/Active/Heavy), token breakdowns, cost per provider |
| Provider Landscape Map | `output/gonka_provider_landscape_map.md` | 4-segment market map, gap analysis, competitive positioning |
| Feature Landscape | `.planning/research/FEATURES.md` | Developer decision criteria ranked by community evidence, messaging themes |
| Pitfalls Research | `.planning/research/PITFALLS.md` | 7 GTM pitfalls, trust barriers, crypto jargon alienation |
| Architecture Research | `.planning/research/ARCHITECTURE.md` | AAARRRP journey skeleton, 3 draft personas, objection map |
| Stack Research | `.planning/research/STACK.md` | OpenClaw technical architecture, provider selection flow |

### Output Format
| Deliverable | Format | Consumed By |
|-------------|--------|-------------|
| Developer persona cards | Markdown document in `output/` | Phase 17 (Messaging), Phase 18 (Channels) |
| AAARRRP journey maps | Markdown tables/diagrams per persona | Phase 17, Phase 18, Phase 19 (Partnerships) |

## Architecture Patterns

### Persona Card Structure

Each persona card should follow this template, derived from B2D best practices:

```markdown
## Persona: [Name]

### Profile
- **Role:** [job title / self-description]
- **Team size:** [solo / small team / company]
- **Technical level:** [junior / mid / senior]
- **Crypto familiarity:** [none / aware / active]
- **Current stack:** [what they use today for inference]
- **Monthly inference spend:** [range]
- **OpenClaw usage pattern:** [casual / active / heavy]

### Decision Drivers (Ranked)
1. [Primary driver] -- [evidence from community signals]
2. [Secondary driver] -- [evidence]
3. [Tertiary driver] -- [evidence]

### Pain Points
- [Pain 1] -- [how it manifests in their workflow]
- [Pain 2] -- [how it manifests]

### Adoption Triggers
- [What event/moment causes them to consider switching providers]

### Objections
- [What stops them from adopting Gonka]

### Gonka Value Proposition (for this persona)
- [Which Gonka features matter most to them and why]
```

### AAARRRP Journey Map Structure

Each persona gets a journey map with all 7 stages. The AAARRRP framework (Phil Leggetter, 2016) extends AARRR pirate metrics with Awareness (front) and Product (back). The stages are:

1. **Awareness** -- Developer becomes aware Gonka exists
2. **Acquisition** -- Developer signs up / gets API key
3. **Activation** -- Developer makes first successful inference call ("aha moment")
4. **Retention** -- Developer continues using Gonka beyond first day
5. **Revenue** -- Developer converts to paid usage
6. **Referral** -- Developer recommends Gonka to others
7. **Product** -- Developer feedback shapes Gonka's roadmap

For each stage, map:
- **Touchpoint:** Where/how the persona interacts with Gonka
- **Action:** What they do at this stage
- **Objection:** What might stop them progressing
- **Content/Asset needed:** What Gonka must provide
- **Key metric:** How to measure success at this stage

```markdown
| Stage | Touchpoint | Action | Objection | Content Needed | Metric |
|-------|-----------|--------|-----------|---------------|--------|
| Awareness | ... | ... | ... | ... | ... |
| Acquisition | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |
```

### Recommended Project Structure

```
output/
├── gonka_developer_personas.md          # All persona cards + journey maps
├── gonka_competitive_feature_matrix.md  # (exists -- input)
├── gonka_agent_pricing_analysis.md      # (exists -- input)
└── gonka_provider_landscape_map.md      # (exists -- input)
```

A single output document is preferable to multiple files because downstream phases (17, 18) need to reference all personas together when crafting messaging and channel strategy.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Persona data sourcing | Don't invent fictional developer profiles from imagination | Synthesize from existing research corpus (FEATURES.md decision criteria, PITFALLS.md trust barriers, pricing analysis workload tiers) | The research already contains community-grounded data; inventing details reduces credibility |
| Journey stage definitions | Don't create a custom funnel framework | Use AAARRRP as specified in CONTEXT.md | AAARRRP is purpose-built for developer relations; aligns with ARCHITECTURE.md skeleton |
| Decision driver ranking | Don't guess what developers prioritize | Use the ranked decision criteria from FEATURES.md (Section: Developer Decision Criteria) | Those rankings are derived from OpenClaw community analysis with cited sources |
| Workload tier profiles | Don't create new usage tiers | Map to the Casual/Active/Heavy tiers already defined in `gonka_agent_pricing_analysis.md` | Pricing analysis already modeled token consumption, monthly costs, and heartbeat overhead per tier |
| Objection mapping | Don't brainstorm objections from scratch | Start from ARCHITECTURE.md objection map + PITFALLS.md pitfall-to-phase mapping | These documents already catalog objections with evidence and responses |

**Key insight:** Phase 16's primary job is synthesis and structuring, not original research. The data already exists across 7+ research documents. The value is in organizing it into persona-shaped containers that downstream phases can consume directly.

## Common Pitfalls

### Pitfall 1: Creating Crypto-Native Personas Instead of Web2-Native
**What goes wrong:** Personas assume developers are familiar with tokens, staking, wallets, and DeFi concepts. This leads to messaging that alienates the actual target audience.
**Why it happens:** The Gonka team comes from crypto backgrounds. PITFALLS.md documents this extensively (Pitfalls 1, 2, and 7).
**How to avoid:** CONTEXT.md explicitly requires "Web2-native audience finding." Every persona should be a developer who has never held a token. Crypto familiarity should be "none" or "aware" for at least 2 of 3 personas.
**Warning signs:** Persona cards mention "staking rewards" or "governance participation" as motivations.

### Pitfall 2: Personas Too Similar to Each Other
**What goes wrong:** All 3 personas are variations of "developer who wants cheaper inference" -- same pain points, same drivers, different labels.
**Why it happens:** Cost is the easiest differentiator to articulate, so all personas converge on it.
**How to avoid:** Differentiate on primary decision driver, not just workload scale. The FEATURES.md decision criteria list 8 drivers -- each persona should lead with a different top driver (e.g., cost, reliability, privacy/censorship resistance).
**Warning signs:** All 3 personas have the same #1 decision driver.

### Pitfall 3: Journey Maps That Are Generic Funnels
**What goes wrong:** AAARRRP journey maps read as generic SaaS onboarding funnels with no OpenClaw-specific or Gonka-specific details.
**Why it happens:** Templates are filled in mechanically without grounding each stage in the specific OpenClaw developer experience.
**How to avoid:** Each touchpoint should reference specific OpenClaw artifacts (ClawHub, `openclaw.json`, heartbeat system). Each objection should reference specific competitive dynamics (OpenRouter as default, prompt caching as substitute for sessions).
**Warning signs:** Journey map could apply to any API product with find-and-replace of "Gonka" to "Twilio."

### Pitfall 4: Ignoring the Workload-to-Persona Alignment
**What goes wrong:** Personas don't map to the workload tiers (Casual/Active/Heavy) already defined in the pricing analysis. Downstream phases can't connect persona messaging to cost projections.
**Why it happens:** Personas are created in isolation from the pricing analysis.
**How to avoid:** Each persona should align with (or reference) one of the three workload tiers. The Casual tier developer has different objections than the Heavy tier developer.
**Warning signs:** No mention of monthly token consumption or cost ranges in persona cards.

### Pitfall 5: Decision Drivers Not Validated Against Community Evidence
**What goes wrong:** Decision driver rankings are asserted without citing the community evidence that supports them. MSG-01 explicitly requires validation against real OpenClaw community discussions.
**Why it happens:** Convenience -- it's easier to assert rankings than to trace them to sources.
**How to avoid:** Every decision driver ranking should cite the source from FEATURES.md or link to community evidence. Where evidence is weak, flag as LOW confidence.
**Warning signs:** Decision drivers have no citations or evidence column.

## Code Examples

Not applicable -- this is a research/analysis phase with no code deliverables.

### Template: Persona Card with Evidence Citations

```markdown
## Persona: The Weekend Builder

### Profile
- **Role:** Software engineer building personal AI agents as side projects
- **Team size:** Solo
- **Crypto familiarity:** None -- has heard of Bitcoin, never held a token
- **Current stack:** OpenClaw + OpenRouter (default, never changed it)
- **Monthly spend:** $5-30 (Casual tier, ~31.5M tokens/month)
- **OpenClaw usage:** Personal assistant on Telegram, casual coding helper

### Decision Drivers (Ranked)
1. **Cost per task** -- "I'm spending $20/month on a hobby project, that feels too high"
   Evidence: FEATURES.md #1 ranked criterion; "$300+ in 2 days" complaints common
2. **Ease of integration** -- "I don't want to spend a weekend changing my provider config"
   Evidence: FEATURES.md #4; "adding a custom provider = editing one JSON block"
3. **Model quality** -- "It needs to be as good as Claude for coding tasks"
   Evidence: FEATURES.md #3; 76% of teams use multiple models

### Pain Points
- Heartbeats cost nearly as much as actual messages (44% of tokens at Casual tier)
  Source: gonka_agent_pricing_analysis.md Section 3
- OpenRouter free tier is unreliable ("models appear, disappear, hit throttles")
  Source: FEATURES.md citing OpenRouter Free API Changes 2026

### Adoption Triggers
- Monthly bill crosses $30 threshold and they search for "cheaper OpenClaw provider"
- OpenRouter free tier degrades and they look for alternatives

### Objections
- "I've never heard of Gonka" (Awareness gap)
- "OpenRouter already works, why change?" (Switching inertia)
- "Is this a crypto thing? I don't want a wallet" (Crypto association)
```

### Template: AAARRRP Journey Map Row

```markdown
| Awareness | Reddit r/LocalLLaMA post comparing K2.5 providers | Reads comparison, clicks link to Gonka docs | "Never heard of Gonka -- is this legit or a crypto scam?" | Comparison blog post showing cost savings; landing page that looks like Vercel, not DeFi | Unique visitors to docs.gonka.ai from Reddit |
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Static persona PDFs | Living persona documents updated with community data | 2024-2025 | Personas stay relevant as market evolves |
| Generic AARRR funnel | AAARRRP with Awareness + Product stages | 2016 (Phil Leggetter) | Better fit for developer relations vs generic SaaS |
| Persona = demographics | Persona = decision drivers + pain points + workflow | 2023+ | More actionable for B2D; demographics matter less than technical context |
| Assumed crypto-native audience for DePIN | Web2-native first, crypto as optional benefit | 2025-2026 | Only 23K active Web3 devs vs 28M Web2 devs; broader market requires Web2-first approach |

## Open Questions

1. **How many personas?**
   - What we know: CONTEXT.md says "at least three." ARCHITECTURE.md defines 3 (OpenClaw Builder, Agent Framework Developer, AI Startup). The pricing analysis defines 3 workload tiers (Casual, Active, Heavy).
   - What's unclear: Whether the ARCHITECTURE.md personas are the right cut, or whether workload-tier-aligned personas would be more useful downstream.
   - Recommendation: Use the ARCHITECTURE.md personas as starting points but refine them. Align each to a workload tier. Consider adding a 4th persona for the privacy/censorship-driven developer (FEATURES.md shows this as a strong Gonka advantage).

2. **How to validate decision driver rankings "against real OpenClaw community discussions"?**
   - What we know: FEATURES.md already derived its rankings from community discussions, provider comparison guides, and OpenClaw Discord analysis (MEDIUM confidence).
   - What's unclear: Whether the planner should instruct agents to do additional community scraping or treat the FEATURES.md rankings as sufficient validation.
   - Recommendation: Treat FEATURES.md rankings as the primary source and cite them explicitly. If additional validation is needed, reference specific community threads/posts but don't require new scraping -- this is a research milestone, not a data collection sprint.

3. **Single document or multiple documents?**
   - What we know: Phase 15 produced 3 separate output documents. CONTEXT.md doesn't specify.
   - Recommendation: Single `output/gonka_developer_personas.md` document containing all persona cards and journey maps. Downstream phases need to reference all personas together.

## Data Synthesis Map

This shows which existing research data maps to which persona element, so the planner can instruct agents precisely where to find source material.

| Persona Element | Primary Source | Section/Data Point |
|----------------|---------------|-------------------|
| Decision drivers (ranked) | `.planning/research/FEATURES.md` | "Developer Decision Criteria" table -- 8 drivers ranked with evidence |
| Pain points (cost) | `output/gonka_agent_pricing_analysis.md` | Sections 3-5: workload tiers, token breakdowns, hidden costs |
| Pain points (features) | `output/gonka_competitive_feature_matrix.md` | Summary scores, dimension deep dives, key takeaways |
| Pain points (trust/reliability) | `.planning/research/PITFALLS.md` | Pitfalls 1, 3, 5, 7 |
| Competitive gaps | `output/gonka_competitive_feature_matrix.md` | Feature Gap Analysis section |
| Gonka advantages | `.planning/research/FEATURES.md` | "Differentiators" section (Tier 1, 2, 3) |
| Objections | `.planning/research/ARCHITECTURE.md` | Objection Map table |
| Journey stages | `.planning/research/ARCHITECTURE.md` | "Developer Journey Architecture" section (AAARRRP skeleton) |
| Messaging themes | `.planning/research/FEATURES.md` | "Messaging Themes" section (5 themes) |
| Anti-patterns | `.planning/research/FEATURES.md` | "Anti-Features" table |
| Vocabulary guidelines | `.planning/research/PITFALLS.md` | Pitfall 7: Crypto Jargon -- internal vs external vocabulary |
| OpenClaw config flow | `.planning/research/STACK.md` | Provider selection 2-step process, `openclaw.json` config |

## Sources

### Primary (HIGH confidence)
- `.planning/research/FEATURES.md` -- Developer decision criteria, messaging themes, feature gaps, differentiators
- `.planning/research/PITFALLS.md` -- 7 GTM pitfalls with evidence, recovery strategies, phase mapping
- `.planning/research/ARCHITECTURE.md` -- AAARRRP journey skeleton, 3 draft personas, objection map, architecture-to-message mapping
- `output/gonka_agent_pricing_analysis.md` -- 3 workload tiers, token breakdowns, per-provider cost comparison
- `output/gonka_competitive_feature_matrix.md` -- 8-dimension feature comparison, summary scores
- `output/gonka_provider_landscape_map.md` -- 4-segment market map, gap analysis

### Secondary (MEDIUM confidence)
- [AAARRRP Framework - Phil Leggetter](https://www.leggetter.co.uk/aaarrrp/) -- Framework definition and application guidance
- [B2D Marketing Best Practices - Snipcart](https://snipcart.com/blog/b2d-marketing-selling-to-developers) -- Developer-first GTM patterns
- [B2D Go-To-Market - Tomasz Tunguz](https://tomtunguz.com/b2d-go-to-market/) -- B2D company GTM challenges
- [Common Room B2D Strategies](https://www.commonroom.io/blog/b2d-best-business-to-developer-strategies/) -- Developer marketing and relations combination

### Tertiary (LOW confidence)
- None -- all findings grounded in existing research corpus or verified framework sources.

## Metadata

**Confidence breakdown:**
- Persona structure: HIGH -- grounded in existing research corpus with 7+ documents of source material
- AAARRRP framework: HIGH -- verified against Phil Leggetter's original definition
- Decision driver data: MEDIUM -- FEATURES.md rankings derived from community analysis, not direct interviews
- Journey map specifics: MEDIUM -- touchpoints and objections synthesized from research, not validated with actual developers

**Research date:** 2026-04-01
**Valid until:** 2026-05-01 (30 days -- stable domain, no rapidly changing dependencies)

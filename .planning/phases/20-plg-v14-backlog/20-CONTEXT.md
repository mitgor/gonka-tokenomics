# Phase 20: Product-Led Growth & v1.4 Backlog - Context

**Gathered:** 2026-04-01
**Status:** Ready for planning
**Mode:** Auto-generated (autonomous mode)

<domain>
## Phase Boundary

All GTM research converges into an actionable growth model with measurable funnel stages and a prioritized engineering backlog that tells v1.4 exactly what to build and in what order. Deliverables: PLG funnel model, free tier design spec, time-to-first-inference plan, prioritized v1.4 engineering backlog.

</domain>

<decisions>
## Implementation Decisions

### PLG Funnel
- Define stages: GitHub star -> docs -> API key -> first call -> 100th call -> paid
- Target conversion rates per stage
- Use AAARRRP journey stages from Phase 16

### Free Tier Design
- Email-only signup — no wallet or crypto knowledge required
- Define usage limits and upgrade trigger
- Reference competitive free tier offerings from Phase 15

### Time-to-First-Inference
- Target under 5 minutes from email to first API response
- Copy-paste OpenClaw config snippet as the atomic growth unit
- Reference OpenClaw provider configuration from .planning/research/STACK.md

### Engineering Backlog
- Rank all identified engineering work by GTM impact
- Separate "must ship before marketing push" from "nice to have"
- Consolidate from all phases: provider plugin, docs site, self-serve signup, multi-model support, v1.2 tech debt

### Claude's Discretion
All formatting, conversion rate targets, and prioritization framework at Claude's discretion.

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- All Phase 15-19 outputs in output/ directory
- .planning/research/STACK.md — OpenClaw config snippet format
- .planning/research/FEATURES.md — feature gap analysis
- output/gonka_provider_landscape_map.md — must-close vs can-defer gaps
- output/gonka_partnership_playbook.md — technical requirements checklist (33 items)
- .planning/PROJECT.md — v1.2 tech debt list

### Integration Points
- Phase 20 is the capstone — produces the v1.4 engineering backlog that bridges research to execution

</code_context>

<specifics>
## Specific Ideas

No specific requirements beyond roadmap success criteria.

</specifics>

<deferred>
## Deferred Ideas

None.

</deferred>

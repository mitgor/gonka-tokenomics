# Phase 15: Competitive Analysis & Market Mapping - Context

**Gathered:** 2026-04-01
**Status:** Ready for planning
**Mode:** Auto-generated (autonomous mode — user approved all defaults)

<domain>
## Phase Boundary

Leadership has a complete picture of the inference provider landscape for OpenClaw agents -- who competes, on what dimensions, and where Gonka's structural advantages create winnable positions. Deliverables: feature matrix, pricing analysis, and provider landscape map.

</domain>

<decisions>
## Implementation Decisions

### Competitive Dimensions
- Compare across agent-relevant dimensions: sessions, tiering, tool calling, streaming, memory, pricing model, uptime SLA, model breadth
- Include both direct competitors (OpenRouter, Together AI) and indirect (OpenAI, Anthropic direct API)
- Categorize providers: centralized API, multi-provider router, dedicated inference, decentralized GPU

### Pricing Analysis
- Model realistic OpenClaw agent workloads: heartbeat context resends every 30 min, 3-10x more calls than chatbots
- Calculate per-task cost, monthly spend at different usage tiers, and at-scale economics
- Include hidden costs: markup percentages, rate limiting impact, overage charges

### Gap Identification
- Explicitly separate "must close before GTM push" gaps from "can defer" gaps
- Reference v1.2 tech debt items as potential gaps (in-memory sessions, JSON keys, TF-IDF search)

### Claude's Discretion
All formatting, structure, and analytical framework choices are at Claude's discretion. Use research from .planning/research/ as foundation.

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- .planning/research/STACK.md — OpenClaw provider architecture, competitive pricing data
- .planning/research/FEATURES.md — Feature landscape, decision criteria, gap analysis
- .planning/research/ARCHITECTURE.md — GTM framework, competitive analysis structure
- .planning/research/PITFALLS.md — Common mistakes, trust barriers

### Established Patterns
- v1.0/v1.1 research deliverables used markdown with structured sections, tables, and citations
- Previous research docs averaged 3000-5000 words with source references

### Integration Points
- Phase 15 outputs feed into Phase 16 (persona pain points), Phase 17 (competitive differentiation), and Phase 20 (engineering backlog)

</code_context>

<specifics>
## Specific Ideas

No specific requirements — open to standard approaches. Research files in .planning/research/ provide foundation.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

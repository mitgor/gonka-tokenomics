---
phase: 15-competitive-analysis-market-mapping
plan: "01"
subsystem: competitive-analysis
tags: [research, competitive-analysis, market-mapping, gtm, gap-analysis]
dependency_graph:
  requires: []
  provides:
    - "output/gonka_competitive_feature_matrix.md"
    - "output/gonka_provider_landscape_map.md"
  affects:
    - "Phase 16: persona pain points reference OpenRouter as primary competitor"
    - "Phase 17: messaging leads with agent-native features, not decentralization"
    - "Phase 19: built-in OpenClaw provider is highest-impact GTM action"
    - "Phase 20: must-close gaps define minimum viable GTM checklist"
tech_stack:
  added: []
  patterns:
    - "Win/Lose/Tie scoring matrix for structured competitive comparison"
    - "2x2 landscape segmentation (centralized/decentralized x single/multi-provider)"
    - "Two-tier gap analysis (must-close vs can-defer) with priority levels"
key_files:
  created:
    - "output/gonka_competitive_feature_matrix.md"
    - "output/gonka_provider_landscape_map.md"
  modified: []
decisions:
  - "Gonka wins on 2/8 agent dimensions (sessions, tiering); OpenAI leads at 3/8"
  - "OpenRouter is the primary competitive threat (built-in OpenClaw, 500+ models)"
  - "5 must-close gaps identified before GTM: OpenClaw built-in, docs, signup, pricing, persistent sessions"
  - "6 can-defer gaps with timelines: single model, JSON keys, TF-IDF, load balancing, dashboard, SLA"
  - "Cost advantage claims must remain contingent until Gonka pricing is published"
metrics:
  duration: "8m 29s"
  completed: "2026-04-01"
  tasks: 2
  files_created: 2
---

# Phase 15 Plan 01: Competitive Feature Matrix and Provider Landscape Map Summary

Structured competitive analysis comparing Gonka against 4 providers across 8 agent-relevant dimensions, plus a 4-segment provider landscape map with prioritized gap analysis identifying 5 must-close and 6 can-defer items for GTM readiness.

## What Was Done

### Task 1: Competitive Feature Matrix (COMP-01)

Created `output/gonka_competitive_feature_matrix.md` (5,955 words) comparing Gonka vs OpenRouter vs OpenAI vs Anthropic vs Together AI across 8 agent-relevant dimensions:

1. **Agent Sessions** -- Gonka WIN (only provider with server-side session persistence on chat completions API)
2. **Model Tiering / Auto-Routing** -- Gonka WIN (3-tier auto-routing via X-Gonka-Tier header)
3. **Tool Calling** -- OpenAI WIN (structured outputs with guaranteed schema compliance)
4. **Streaming** -- Universal TIE
5. **Memory / Context Management** -- OpenAI WIN (50% prompt caching) and Anthropic WIN (90% prompt caching)
6. **Pricing Model** -- Together AI WIN (cheapest verified K2.5 at $0.50/$2.50)
7. **Uptime / Reliability** -- OpenAI WIN and Anthropic WIN (SLAs, proven track records)
8. **Model Breadth** -- OpenRouter WIN (500+ models)

Summary scores: Gonka 2/8, OpenRouter 1/8, OpenAI 3/8, Anthropic 2/8, Together AI 1/8.

Each dimension includes a 300-500 word deep dive with agent-as-customer framing. All Gonka pricing flagged as TBD. Key takeaways section frames findings from OpenClaw developer needs, not Gonka features.

### Task 2: Provider Landscape Map and Gap Analysis (COMP-03)

Created `output/gonka_provider_landscape_map.md` (5,102 words) with:

- 2x2 landscape segmentation (centralized/decentralized x single-provider/multi-provider) covering 15+ providers
- 4 segment analyses with threat levels per provider
- OpenRouter deepest analysis as primary competitor (built-in OpenClaw, same target market)
- AkashML identified as closest decentralized competitor (OpenAI-compatible since Nov 2025, but no agent features)
- Must-close gap table (5 items) with "closed" definitions
- Can-defer gap table (6 items) with timelines and priority tiers
- Recommendations mapped to phases 16, 17, 19, and 20

## Key Findings

1. **Gonka occupies a unique market position** -- the only provider combining decentralized infrastructure with agent-native API extensions. No competitor in any segment offers both.

2. **Gonka's biggest barriers are not feature gaps but infrastructure gaps.** Not being a built-in OpenClaw provider, having no docs/signup/pricing page -- these table-stakes items prevent developers from evaluating Gonka regardless of feature advantages.

3. **OpenRouter is the primary threat** because it occupies the "default OpenClaw provider" position with zero-config integration and 500+ models. Gonka's path is either becoming built-in or demonstrating compelling advantages that justify manual setup.

4. **Prompt caching (OpenAI 50%, Anthropic 90%) partially substitutes for Gonka's sessions**, weakening that differentiator on cost grounds. Gonka's session value must emphasize architectural simplicity (no context re-send) not just cost savings.

5. **Blackwell GPUs are narrowing decentralized cost advantages** -- Together AI and DeepInfra deploying Blackwell will push per-token costs down further, making cost-only positioning unsustainable.

## Deviations from Plan

None -- plan executed exactly as written.

## Commits

| Task | Commit | Files |
|------|--------|-------|
| Task 1: Competitive Feature Matrix | b953898 | output/gonka_competitive_feature_matrix.md |
| Task 2: Provider Landscape Map | 8642e95 | output/gonka_provider_landscape_map.md |

## Self-Check: PASSED

All artifacts verified:
- output/gonka_competitive_feature_matrix.md: FOUND (5,955 words)
- output/gonka_provider_landscape_map.md: FOUND (5,102 words)
- Commit b953898: FOUND
- Commit 8642e95: FOUND

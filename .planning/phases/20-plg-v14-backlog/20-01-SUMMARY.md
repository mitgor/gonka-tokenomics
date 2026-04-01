---
phase: 20-plg-v14-backlog
plan: 01
subsystem: gtm
tags: [plg, funnel, free-tier, onboarding, developer-experience, growth-model]

# Dependency graph
requires:
  - phase: 15-competitive-analysis
    provides: "competitive feature matrix, pricing analysis, provider landscape map"
  - phase: 16-developer-personas
    provides: "3 developer personas with AAARRRP journey maps"
  - phase: 17-messaging-positioning
    provides: "message house, never-say list, objection playbook, agent-native pitch"
  - phase: 18-channel-strategy
    provides: "channel matrix, API-active developer KPI, anti-metrics"
  - phase: 19-partnership-ecosystem
    provides: "four-tier integration roadmap, ClawHub plan, technical requirements"
provides:
  - "PLG funnel model with 6 stages and target conversion rates"
  - "Free tier design spec with email-only signup and concrete usage limits"
  - "Time-to-first-inference plan targeting under 5 minutes"
  - "Atomic growth unit concept (openclaw.json config snippet as viral mechanism)"
affects: [20-02-PLAN, v1.4-engineering-backlog]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "AAARRRP-mapped PLG funnel with per-persona conversion drivers"
    - "Upgrade trigger pattern via API response headers (X-Gonka-Usage-Remaining)"
    - "Atomic growth unit: config snippet as viral mechanism"

key-files:
  created:
    - output/gonka_plg_growth_model.md
  modified: []

key-decisions:
  - "Free tier: 15M tokens/month, 1000 requests/day, 2 concurrent sessions, K2.5 lite+mid only"
  - "Email-only signup with no OAuth, wallet, or credit card"
  - "Time-to-first-inference target: 4 minutes 15 seconds across 7 steps"
  - "Upgrade triggers via API headers, not hard blocks (transparent substitution for model tier)"
  - "Atomic growth unit is the openclaw.json config snippet, not a referral link"

patterns-established:
  - "PLG funnel stages: Discover -> Explore -> Sign Up -> First Inference -> Habitual Use -> Paid Conversion"
  - "Free tier designed to cover Weekend Builder fully while triggering upgrade for Startup CTO"
  - "Config snippet as viral mechanism: copy-pasteable, version-controlled, portable, cost-transparent"

requirements-completed: [GTM-03]

# Metrics
duration: 6min
completed: 2026-04-01
---

# Phase 20 Plan 01: PLG Growth Model Summary

**PLG funnel with 6 AAARRRP-mapped stages, email-only free tier (15M tokens/month), and 7-step time-to-first-inference plan targeting 4m15s**

## Performance

- **Duration:** 6 min
- **Started:** 2026-04-01T21:29:00Z
- **Completed:** 2026-04-01T21:35:24Z
- **Tasks:** 2
- **Files modified:** 1

## Accomplishments
- PLG funnel with 6 named stages, target conversion rates, per-persona drivers for all 3 personas at all 6 stages, and funnel math with pessimistic/target/optimistic projections
- Free tier design spec: email-only signup, 15M tokens/month, 1000 requests/day, 2 concurrent sessions, lite+mid K2.5 only, with 3 specific upgrade triggers via API response headers
- Time-to-first-inference plan: 7 steps totaling 4 minutes 15 seconds with pre-filled openclaw.json config snippet, gap analysis, failure modes, and competitor comparison (OpenRouter, Together AI, self-hosted vLLM)
- Atomic growth unit concept: the openclaw.json config snippet as the viral mechanism driving organic developer-to-developer sharing
- Cross-references section citing all 10 Phase 15-19 source documents with specific data drawn from each

## Task Commits

Each task was committed atomically:

1. **Task 1: PLG funnel model and free tier design spec** - `167e22a` (feat)
2. **Task 2: Time-to-first-inference plan** - `b093c77` (feat)

**Plan metadata:** (pending)

## Files Created/Modified
- `output/gonka_plg_growth_model.md` - 460-line PLG growth model with funnel, free tier spec, time-to-first-inference plan, and cross-references

## Decisions Made
- **Free tier limits calibrated to persona workloads:** 15M tokens/month covers Weekend Builder's session-optimized usage (~12.6M) with headroom while forcing Startup CTO (Active tier ~56.3M session-optimized) to upgrade in week 1
- **Three upgrade triggers, not hard blocks:** Usage limit approaching (via X-Gonka-Usage-Remaining header), session limit reached (403 with clear message), model tier access (transparent substitution with header notification). Requests succeed where possible rather than failing.
- **Config snippet pre-filled with developer's API key:** The verification page shows the exact JSON with the developer's specific key, not a generic template with placeholder
- **Competitor comparison frames Gonka's friction advantage:** OpenRouter requires GitHub OAuth + credit card + model selection (5-8 min). Together AI requires OAuth + mandatory credit card (5-8 min). vLLM self-hosting takes hours to days. Gonka targets 4m15s with email only.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- `output/` directory is in `.gitignore`; used `git add -f` to force-add the file. This is consistent with how prior Phase 15-19 output files were committed.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness
- PLG growth model complete, ready for Plan 20-02 (v1.4 engineering backlog)
- Plan 20-02 will consolidate all must-build engineering items identified across this document and Phase 15-19 into a prioritized backlog

---
*Phase: 20-plg-v14-backlog*
*Completed: 2026-04-01*

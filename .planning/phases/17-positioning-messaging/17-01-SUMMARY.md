---
phase: 17-positioning-messaging
plan: "01"
subsystem: marketing
tags: [messaging, positioning, personas, vocabulary, competitive-differentiation, gtm]

# Dependency graph
requires:
  - phase: 15-competitive-analysis
    provides: "Competitive feature matrix with WIN/TIE/LOSE verdicts"
  - phase: 16-developer-personas
    provides: "3 developer personas with decision drivers, objections, AAARRRP journey maps"
provides:
  - "Core positioning statement leading with developer outcomes"
  - "5 ranked value propositions with competitive evidence"
  - "Per-persona differentiation for 3 personas"
  - "Architecture-to-message mapping for 11 technical features"
  - "Never-say vocabulary list (16 crypto terms) with approved alternatives"
  - "Competitive differentiation statements vs OpenRouter, Together AI, Akash"
  - "Objection handling quick reference"
  - "Agent-native pitch"
affects: [channel-strategy, partnership-ecosystem, content-creation]

# Tech tracking
tech-stack:
  added: []
  patterns: ["message-house framework", "vocabulary-gating for developer content"]

key-files:
  created:
    - output/gonka_message_house.md

key-decisions:
  - "Lead with heartbeat cost reduction (73%) as primary positioning, not decentralization"
  - "16 crypto terms on never-say list including wallet, staking, mining, DePIN, Web3"
  - "Per-persona competitor focus: Weekend Builder vs OpenRouter, Startup CTO vs Together AI, Privacy-First vs Akash"
  - "Honest concessions included in every competitive differentiation statement"
  - "Privacy claims limited to architectural guarantees (no central logging); TEE not yet built"

patterns-established:
  - "Developer-outcomes-first messaging: always lead with what the developer gains, never with how the technology works"
  - "Vocabulary gating: all developer-facing content reviewed against never-say list before publishing"
  - "Honest concessions: every competitive claim includes an honest acknowledgment of Gonka's disadvantages"

requirements-completed: [MSG-02]

# Metrics
duration: 5min
completed: 2026-04-01
---

# Phase 17 Plan 01: Message House Summary

**Gonka message house with core positioning (73% agent cost reduction via sessions), 5 ranked value props, per-persona differentiation, architecture-to-message mapping for 11 features, and 16-term crypto never-say vocabulary list**

## Performance

- **Duration:** 5 min
- **Started:** 2026-04-01T20:33:14Z
- **Completed:** 2026-04-01T20:38:54Z
- **Tasks:** 1
- **Files created:** 1

## Accomplishments
- Core positioning statement that leads with developer outcomes (heartbeat cost reduction), not decentralization
- 5 ranked value propositions grounded in competitive matrix verdicts with per-persona resonance mapping
- Per-persona differentiation with tailored elevator pitches, lead-with/never-lead-with guidance for all 3 personas
- Complete architecture-to-message mapping table for all 11 Gonka technical features with proof points and competitive context
- Never-say vocabulary list with 16 crypto terms and approved developer-facing alternatives
- Competitive differentiation statements per-persona: Gonka vs OpenRouter, Together AI, Akash Network
- Objection handling quick reference with 8 objection-response pairs grounded in research evidence
- Agent-native pitch explaining why agents themselves prefer Gonka's API design
- 103 source citations throughout the document

## Task Commits

Each task was committed atomically:

1. **Task 1: Core positioning, per-persona value props, and architecture-to-message mapping** - `9dbd572` (feat)

## Files Created/Modified
- `output/gonka_message_house.md` - Canonical messaging framework (441 lines) with positioning, value props, persona differentiation, architecture mapping, vocabulary guidelines, competitive statements, objection handling, and agent-native pitch

## Decisions Made
- Led with heartbeat cost reduction (73% at Active tier) as the primary positioning angle rather than decentralization, agent-native features, or price -- this is the most quantifiable and defensible differentiator
- Created a 16-term never-say list (rather than the minimum 12 specified) to comprehensively cover crypto vocabulary that leaks into developer content
- Focused each persona's competitive differentiation on a single competitor (not all competitors) per ARCHITECTURE.md Anti-Pattern 3 guidance
- Included honest concessions in every competitive statement to build credibility (acknowledged Gonka's LOSE verdicts on Model Breadth and Uptime)
- Added privacy honesty note explicitly distinguishing architectural privacy (current) from cryptographic privacy (TEE, not yet built)

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness
- Message house is ready to feed Phase 18 (Channel Strategy) and Phase 19 (Partnership)
- All messaging grounded in Phase 15 competitive analysis and Phase 16 persona research
- Vocabulary guidelines ready for immediate application to any developer-facing content

---
*Phase: 17-positioning-messaging*
*Completed: 2026-04-01*

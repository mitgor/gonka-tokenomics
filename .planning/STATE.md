---
gsd_state_version: 1.0
milestone: v1.0
milestone_name: milestone
status: executing
stopped_at: Completed 17-02-PLAN.md (agent-native pitch & objection playbook) -- Phase 17 complete
last_updated: "2026-04-01T20:58:46.987Z"
last_activity: 2026-04-01 -- Phase 18 execution started
progress:
  total_phases: 14
  completed_phases: 14
  total_plans: 35
  completed_plans: 35
---

# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-14)

**Core value:** Leadership can tweak assumptions and instantly see the impact on tokenomics health across all dimensions
**Current focus:** Phase 18 complete — channel-strategy

## Current Position

Phase: 18 (channel-strategy) — COMPLETE
Plan: 1 of 1 (DONE)
Status: Phase 18 complete
Last activity: 2026-04-01 -- Phase 18 completed (channel strategy)

Progress: v1.0 SHIPPED | v1.1 SHIPPED | v1.2 SHIPPED | v1.3 IN PROGRESS

## Accumulated Context

### Decisions

See .planning/PROJECT.md Key Decisions table for full history.

### From v1.0

- 10 prioritized recommendations with specific parameters (capstone document)
- Emission decay: exp(-0.000475 x epochs), halving ~1,460 epochs (~4 years)
- Revenue split: 70% hosts / 20% AI Fund / 5% buyback-burn / 5% veGNK yield
- POL: 22M GNK across GNK/USDC (60%) + GNK/ETH (40%) on Uniswap v3

### From v1.1

- 5 Excel workbooks (1 master + 4 standalone) in output/
- 70 parameters with confidence levels (48 HIGH, 16 MED, 6 LOW)
- param_refs interface contract proven at scale (70+ parameters)

### From v1.2

- Infrastructure code in infrastructure/ directory (also at github.com/mitgor/gonka-ai-infrastructure)
- Serving: vLLM launcher, health checks, Dockerfile, docker-compose with 3 tiers
- Gateway: FastAPI proxy, API key auth, rate limiting, usage metering (SQLite), model routing, SSE streaming
- Agent extensions: Session persistence, memory API (TF-IDF search), webhooks, model tiering
- Admin: Usage stats, key management, model health, session management
- Tests: OpenClaw, CrewAI, LangGraph integration tests, API compatibility suite, load tests, Locust config
- Config: models.yaml registry, tiering rules, environment-based settings

### From v1.3 (in progress)

- Session persistence is Gonka's most defensible cost advantage (not per-token pricing)
- Heartbeat overhead accounts for 44-85% of agent token consumption depending on tier
- Recommended pricing: Scenario B ($0.35/$1.75) -- 30% below DeepInfra, competitive with sessions
- Gonka pricing TBD -- all cost projections are scenario-based
- 3 developer personas: Weekend Builder (cost-driven, Casual), Startup CTO (reliability-driven, Active), Privacy-First Builder (privacy-driven, cross-tier)
- Each persona has a different #1 decision driver -- cost, reliability, privacy/censorship
- 3 distinct adoption paths identified: self-service, trust-building, audit-driven
- AAARRRP priority: Awareness and Acquisition are P0 (universal blockers); Activation and Retention are P1
- Message house: lead with heartbeat cost reduction (73%), not decentralization
- 16 crypto terms on never-say list (wallet, staking, mining, DePIN, Web3, etc.)
- Per-persona competitor focus: Weekend Builder vs OpenRouter, Startup CTO vs Together AI, Privacy-First vs Akash
- Privacy claims limited to architectural guarantees; TEE not yet built
- Agent-native pitch: agents are "buyers" making runtime provider selection decisions -- Gonka wins 3/7 task profiles
- Gonka wins: long-running agents (sessions), multi-agent systems (sessions+tiering), privacy-sensitive (no filtering)
- Gonka loses: model diversity (OpenRouter), single-shot (Together AI), quality/uptime (OpenAI)
- ACE objection framework: Acknowledge concern, Counter with evidence, point to Evidence source
- 12 objections documented: P0 priorities are awareness, crypto perception, SLA gap, prompt privacy
- Channel strategy: 14 channels across P0-P3 tiers, API-active developers (>100 calls/month) as primary KPI
- 70/30 channel split: AI/developer channels (70%) lead demand side, crypto channels (30%) support supply side
- P0 channels: OpenClaw Provider Directory, GitHub, Discord -- meet developers where they already make provider decisions
- Anti-metrics explicitly documented: follower counts, Discord members, GitHub stars, impressions are vanity metrics
- Content calendar: AAARRRP-mapped framework with quarterly templates (Q1 launch 60% Awareness+Acquisition, Q2 growth 50% Activation+Retention)

### Pending Todos

None.

### Blockers/Concerns

None.

## Session Continuity

Last session: 2026-04-01
Stopped at: Completed 18-01-PLAN.md (channel strategy with matrix, metrics, content calendar) -- Phase 18 complete
Resume file: None

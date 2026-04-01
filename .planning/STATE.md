# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-14)

**Core value:** Leadership can tweak assumptions and instantly see the impact on tokenomics health across all dimensions
**Current focus:** Planning next milestone

## Current Position

Phase: 15-competitive-analysis-market-mapping
Plan: 2 of 3 in phase (15-02 complete)
Status: Executing v1.3 milestone
Last activity: 2026-04-01 — 15-02 agent workload pricing analysis complete

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

### Pending Todos

None.

### Blockers/Concerns

None.

## Session Continuity

Last session: 2026-04-01
Stopped at: Completed 15-02-PLAN.md (agent workload pricing analysis)
Resume file: None

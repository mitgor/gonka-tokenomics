# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-14)

**Core value:** Position Gonka as the inference provider of choice for OpenClaw developers through research-driven GTM strategy
**Current focus:** Phase 15 -- competitive analysis and market mapping

## Current Position

Phase: 15 (competitive-analysis-market-mapping) -- EXECUTING
Plan: 2 of 2
Status: Plan 15-01 complete, executing Plan 15-02
Last activity: 2026-04-01 -- Plan 15-01 completed

Progress: v1.0 SHIPPED | v1.1 SHIPPED | v1.2 SHIPPED | v1.3 [#.........] 10%

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

### From v1.3

- Gonka wins 2/8 agent dimensions (sessions, tiering); loses on model breadth and uptime
- OpenRouter is primary competitive threat (built-in OpenClaw, 500+ models, same target market)
- 5 must-close gaps before GTM: OpenClaw built-in, docs, signup, pricing, persistent sessions
- 6 can-defer gaps with timelines: single model, JSON keys, TF-IDF, load balancing, dashboard, SLA
- Cost advantage claims must remain contingent until Gonka pricing is published
- Blackwell GPUs narrowing decentralized cost advantages; non-price differentiation essential

### Pending Todos

None.

### Blockers/Concerns

- Gonka pricing not finalized -- cost advantage claims cannot be validated until per-token pricing is set
- OpenClaw ecosystem window is time-sensitive -- ClawHub submission should happen ASAP

## Session Continuity

Last session: 2026-04-01
Stopped at: Completed 15-01-PLAN.md
Resume file: None

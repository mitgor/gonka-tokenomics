# Gonka Tokenomics

## What This Is

Economic modeling tools, inference infrastructure, and go-to-market strategy for Gonka Network. Python scripts generate 5 Excel workbooks with 70 adjustable parameters for tokenomics analysis (v1.0-v1.1). Infrastructure code deploys Kimi K2.5 as an OpenAI-compatible inference endpoint with agent-aware extensions, API gateway, and multi-model routing (v1.2). GTM research provides competitive analysis, developer personas, messaging, channel strategy, partnership playbook, and PLG growth model targeting OpenClaw developers (v1.3).

## Core Value

Leadership can tweak assumptions and instantly see the impact on tokenomics health across all dimensions (price, emissions, host profitability, treasury).

## Requirements

### Validated

- Research: 10 prioritized tokenomics recommendations with specific parameters -- v1.0
- Research: 5 deep research documents (POL, real yield, veGNK, fee transition, GPU economics) -- v1.0
- Research: Updated synthesis documents (Macro Research v2.0, Deep Analysis v3.0, Explained v3.0) -- v1.0
- Research: Capstone Fine-Tuning Recommendations document -- v1.0
- Python scripts (openpyxl) that generate formatted .xlsx workbooks -- v1.1
- Token price scenario model with multiple growth trajectories -- v1.1
- Emission vs fee transition simulation with crossover analysis -- v1.1
- Host profitability model (ROI under varying GNK prices, network sizes, fee structures) -- v1.1
- Treasury & POL simulation (Community Pool depletion, POL returns, buyback impact) -- v1.1
- Master unified workbook with linked tabs and adjustable assumptions -- v1.1
- Standalone summary workbooks for each modeling area -- v1.1
- All models parameterized from v1.0 research (specific numbers, not placeholders) -- v1.1
- Kimi K2.5 inference serving via vLLM with OpenAI-compatible API -- v1.2
- API gateway (auth, rate limiting, usage metering, multi-model routing) -- v1.2
- Agent-aware inference extensions (session persistence, memory API, model tiering) -- v1.2
- Docker/container deployment configuration for GPU nodes -- v1.2
- Integration testing with OpenClaw, CrewAI, LangGraph agent frameworks -- v1.2
- Competitive feature matrix across 5 providers and 8 agent-relevant dimensions -- v1.3
- Agent workload pricing analysis with 3 tiers and session-adjusted cost modeling -- v1.3
- Provider landscape map with 4-segment categorization and gap analysis -- v1.3
- Developer persona cards (Weekend Builder, Startup CTO, Privacy-First Builder) with AAARRRP journey maps -- v1.3
- Message house with core positioning, architecture-to-message mapping, and vocabulary guidelines -- v1.3
- Agent-native pitch with programmatic provider selection test -- v1.3
- Channel strategy with P0-P3 tiered matrix and 70/30 AI-dev/crypto split -- v1.3
- Partnership playbook with four-tier OpenClaw integration roadmap -- v1.3
- PLG growth model with free tier spec and time-to-first-inference plan -- v1.3
- Prioritized v1.4 engineering backlog (18 must-ship, 14 nice-to-have) -- v1.3

### Active

## Current Milestone: v1.4 GTM Engineering Execution

**Goal:** Execute the v1.3 engineering backlog — build everything needed so a developer can go from zero to first Gonka inference in under 5 minutes via OpenClaw.

**Target features (18 must-ship items):**
- Sprint 1 (Foundation): Production endpoint, docs site, pricing page, landing page, legal pages, support channels
- Sprint 2 (Signup Flow): Email infra, self-serve signup, config template, integration guide, verify endpoint, usage headers, error messages
- Sprint 3 (Hardening): Persistent sessions (Redis), OpenClaw npm plugin, status page

### Out of Scope

- Smart contract implementation -- deferred to future milestone
- Governance proposal drafting -- deferred to future milestone
- Real-time dashboards or web interfaces -- spreadsheets are the delivery format (modeling)
- Monte Carlo / stochastic simulation -- deterministic scenario models for v1.1
- Full agent hosting (Option B) -- too complex; v1.2 uses agent-aware inference (Option C)
- GNK token payments -- separate milestone; v1.2 uses API keys
- Image/video model serving (FLUX, Wan) -- separate milestone; focus on LLM serving first
- Training/fine-tuning infrastructure -- inference-only
- Web dashboard UI -- admin API only; UI deferred
- Implementation of GTM strategy -- v1.3 produced research/strategy; execution is v1.4+
- Paid advertising -- developer-first organic strategy per v1.3 research

## Context

- **v1.0 research provides all input parameters** -- emission decay rate (-0.000475), revenue splits (70/20/5/5), POL allocation (22M GNK), veGNK lock ranges, fee transition scenarios, GPU pricing trajectories, etc.
- **v1.1 delivered 5 Excel workbooks** -- 1 master (8 tabs) + 4 standalone, 70 parameters with confidence levels, cell protection, print-ready, cross-platform validated
- **v1.2 delivered inference infrastructure** -- vLLM K2.5 serving, FastAPI gateway, agent extensions, multi-model routing, integration tests; 3,679 LOC Python, 27 requirements
- **Infrastructure also published as separate repo** -- github.com/mitgor/gonka-ai-infrastructure
- **Primary audience:** Gonka founders/leadership (strategy) + developers (integration code)
- **Tech stack (modeling):** Python 3.x with openpyxl==3.1.5, 5,643 LOC across 19 source files
- **Tech stack (infrastructure):** Python (FastAPI, vLLM), Docker, SQLite, OpenAI-compatible API
- **Open concerns from v1.0:** Oracle feed creation (critical path), POL paired asset shortage, governance concentration risk, developer adoption targets
- **Deferred from v1.1:** IL modeling, tornado charts, competitive benchmarks
- **Tech debt from v1.2:** TF-IDF search (needs vector embeddings), in-memory sessions (needs Redis), JSON key storage (needs DB), no GPU load balancing
- **v1.3 delivered 11 GTM research documents** -- competitive analysis, developer personas, message house, agent-native pitch, objection playbook, channel strategy, partnership playbook, PLG growth model, v1.4 engineering backlog; 4,955 lines total
- **v1.3 key findings:** Gonka wins 2/8 competitive dimensions (sessions, tiering), 73% cost savings at Active tier via session persistence, 5 must-close gaps before GTM push, lead with developer outcomes not decentralization
- **v1.4 backlog ready** -- 18 must-ship items in 3 sprints (6 weeks): docs site, self-serve signup, OpenClaw plugin, persistent sessions, pricing page

## Constraints

- **Tech stack (modeling)**: Python 3.x with openpyxl for Excel generation -- no external data dependencies
- **Tech stack (infrastructure)**: Python (FastAPI + vLLM), Docker -- GPU inference
- **Model serving**: vLLM v0.15.0+ with OpenAI-compatible API
- **Target hardware**: 4x H200 GPUs minimum for K2.5 production serving
- **API compatibility**: Must be OpenAI-compatible (drop-in for any existing integration)
- **Output format**: .xlsx files that work in Excel and Google Sheets (modeling)
- **Audience**: Non-technical leadership (strategy), developers (API/infrastructure)

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Python + openpyxl over Google Sheets API | No auth setup needed, generates portable .xlsx files | Good -- validated in v1.1 |
| Deterministic scenarios over Monte Carlo | Leadership needs clear scenario comparison, not probability distributions | Good -- validated in v1.1 |
| Master + standalone models | Master for integrated analysis, standalones for focused sharing | Good -- validated in v1.1 |
| param_refs dict as interface contract | All model builders receive cell addresses, no hardcoded values | Good -- scales to 70+ params |
| 70 params (vs ~50 estimated) | Include all research values without omission | Good -- more comprehensive |
| IL modeling deferred to v2 | Wrong IL estimate worse than none for concentrated liquidity | Pending -- still valid |
| Named ranges avoided | Industry anti-pattern; debugging complexity; openpyxl limitations | Good -- direct refs work well |
| openpyxl 3.1.5 with app.xml fix | Chart rendering bug workaround | Good -- no downgrade needed |
| Kimi K2.5 as flagship model | First-to-market on decentralized, native agentic + multimodal | Good -- shipped in v1.2 |
| Option C hybrid agent inference | Agent-aware extensions over standard API, not full agent hosting | Good -- shipped in v1.2 |
| vLLM over other serving frameworks | Industry standard, OpenAI-compatible, K2.5 officially supported | Good -- shipped in v1.2 |
| Lead with developer outcomes, not decentralization | Web2-native audience (28M devs vs 23K Web3); crypto-first messaging alienates 99.9% | Good -- validated in v1.3 research |
| OpenClaw as primary GTM target | 250K+ stars, fastest growing OSS project, forming ecosystem defaults NOW | Good -- validated in v1.3 |
| Session persistence as #1 differentiator | Only provider offering agent sessions; 73% cost reduction for Active tier agents | Good -- validated in v1.3 |
| Free tier: email-only, 15M tokens/month | No crypto knowledge required; removes adoption barrier for Web2 developers | Pending -- spec ready for v1.4 |

---
## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd:transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd:complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-02 after v1.4 milestone started*

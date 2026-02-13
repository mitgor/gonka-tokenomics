# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-13)

**Core value:** Leadership can tweak assumptions and instantly see the impact on tokenomics health across all dimensions
**Current focus:** v1.2 Kimi K2.5 Integration & Agent Inference

## Current Position

Phase: Not started (defining requirements)
Plan: --
Status: Defining requirements
Last activity: 2026-02-13 -- Milestone v1.2 started

Progress: v1.0 SHIPPED | v1.1 SHIPPED | v1.2 ACTIVE

## Performance Metrics

**v1.1 Velocity:**
- Total plans completed: 21
- Average duration: 2.7 min per plan
- Total execution time: ~57 min
- Phases: 9 (all verified PASSED)

## Accumulated Context

### Decisions

See .planning/PROJECT.md Key Decisions table for full history.

### From v1.0

- 10 prioritized recommendations with specific parameters (capstone document)
- Emission decay: exp(-0.000475 x epochs), halving ~1,460 epochs (~4 years)
- Revenue split: 70% hosts / 20% AI Fund / 5% buyback-burn / 5% veGNK yield
- POL: 22M GNK across GNK/USDC (60%) + GNK/ETH (40%) on Uniswap v3
- Fee transition crossover: Conservative 10-12 years, moderate 3-4 years
- Host profitability threshold: GNK >= $0.85-$3.30 at critical decay points

### From v1.1

- 5 Excel workbooks (1 master + 4 standalone) in output/
- 70 parameters with confidence levels (48 HIGH, 16 MED, 6 LOW)
- Cell protection, print-ready layout, cross-platform validated
- param_refs interface contract proven at scale (70+ parameters)
- openpyxl 3.1.5 with app.xml chart fix works reliably

### From v1.2 Research

- Top 5 models for Gonka.ai: DeepSeek R1, FLUX.2, Llama 4, Wan 2.1, Qwen3
- Kimi K2.5 selected as flagship: 1T params, native agentic, multimodal, MIT license
- K2.5 deployment: vLLM v0.15.0+, 4x H200 production, OpenAI-compatible API
- Agent inference opportunity: OpenClaw (145k stars), always-on agents drive 70%+ of compute spend
- Recommended approach: Hybrid Option C (standard inference + agent-aware extensions)

### Pending Todos

None.

### Blockers/Concerns

None.

## Session Continuity

Last session: 2026-02-13
Stopped at: Defining v1.2 requirements
Resume file: None

# Gonka Tokenomics

## What This Is

Economic modeling tools for Gonka Network's tokenomics, generating Excel workbooks with adjustable parameters for leadership decision-making. Built on the research foundation from v1.0 (10 prioritized recommendations covering POL, real yield, veGNK, fee transition, GPU economics, and more).

## Core Value

Leadership can tweak assumptions and instantly see the impact on tokenomics health across all dimensions (price, emissions, host profitability, treasury).

## Requirements

### Validated

- Research: 10 prioritized tokenomics recommendations with specific parameters — v1.0
- Research: 5 deep research documents (POL, real yield, veGNK, fee transition, GPU economics) — v1.0
- Research: Updated synthesis documents (Macro Research v2.0, Deep Analysis v3.0, Explained v3.0) — v1.0
- Research: Capstone Fine-Tuning Recommendations document — v1.0

### Active

- [ ] Python scripts (openpyxl) that generate formatted .xlsx workbooks
- [ ] Token price scenario model with multiple growth trajectories
- [ ] Emission vs fee transition simulation with crossover analysis
- [ ] Host profitability model (ROI under varying GNK prices, network sizes, fee structures)
- [ ] Treasury & POL simulation (Community Pool depletion, POL returns, buyback impact)
- [ ] Master unified workbook with linked tabs and adjustable assumptions
- [ ] Standalone summary workbooks for each modeling area
- [ ] All models parameterized from v1.0 research (specific numbers, not placeholders)

### Out of Scope

- Smart contract implementation — deferred to future milestone
- Governance proposal drafting — deferred to future milestone
- Real-time dashboards or web interfaces — spreadsheets are the delivery format
- Monte Carlo / stochastic simulation — deterministic scenario models for v1.1
- Backtesting against historical data — forward-looking projections only

## Context

- **v1.0 research provides all input parameters** — emission decay rate (-0.000475), revenue splits (70/20/5/5), POL allocation (22M GNK), veGNK lock ranges, fee transition scenarios, GPU pricing trajectories, etc.
- **Primary audience:** Gonka founders/leadership who need to evaluate trade-offs and make implementation decisions
- **Existing files:** Gonka_Tokenomics_Fine_Tuning_Recommendations.md has the 10 recommendations with specific parameters that feed into the models
- **Open concerns from v1.0:** Oracle feed creation (critical path), POL paired asset shortage, governance concentration risk, developer adoption targets

## Constraints

- **Tech stack**: Python 3.x with openpyxl for Excel generation — no external data dependencies
- **Data source**: All parameters from v1.0 research documents (no live API calls)
- **Output format**: .xlsx files that work in Excel and Google Sheets
- **Audience**: Non-technical leadership — models must be intuitive with clear labels and documentation tabs

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Python + openpyxl over Google Sheets API | No auth setup needed, generates portable .xlsx files | — Pending |
| Deterministic scenarios over Monte Carlo | Leadership needs clear scenario comparison, not probability distributions | — Pending |
| Master + standalone models | Master for integrated analysis, standalones for focused sharing | — Pending |

---
*Last updated: 2026-02-05 after v1.1 milestone start*

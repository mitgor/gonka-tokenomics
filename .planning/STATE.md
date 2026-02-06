# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-05)

**Core value:** Leadership can tweak assumptions and instantly see the impact on tokenomics health across all dimensions
**Current focus:** Phase 5 Plan 01 complete - Ready for Plan 02: Charts + Conditional Formatting

## Current Position

Phase: 5 of 9 (Host Profitability Model)
Plan: 1 of 2 in current phase
Status: In progress
Last activity: 2026-02-06 -- Completed 05-01-PLAN.md (data model + sensitivity sections)

Progress: [=========.] ~50% (Phase 1-4 complete, Phase 5 plan 1/2)

## Performance Metrics

**Velocity:**
- Total plans completed: 9
- Average duration: 2.6 min
- Total execution time: 24 min

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 1. Foundation | 2/2 | 7 min | 3.5 min |
| 2. Emission Schedule | 2/2 | 3 min | 1.5 min |
| 3. Token Price Scenarios | 2/2 | 5 min | 2.5 min |
| 4. Fee Transition | 2/2 | 6 min | 3.0 min |
| 5. Host Profitability | 1/2 | 3 min | 3.0 min |

**Recent Trend:**
- Last 5 plans: 03-02 (2 min), 04-01 (3 min), 04-02 (3 min), 05-01 (3 min)
- Trend: Consistent 2-3 min per plan

*Updated after each plan completion*

## Accumulated Context

### Decisions

Decisions are logged in PROJECT.md Key Decisions table.
Recent decisions affecting current work:

- [Roadmap]: 9 phases following architecture dependency layers (Layer 0 -> Layer 1 -> Layer 2 -> Layer 3)
- [Roadmap]: IL modeling explicitly deferred to v2 per research recommendation (wrong IL estimate worse than none)
- [Roadmap]: Named ranges avoided; using direct cell references per FEATURES.md anti-pattern finding
- [Roadmap]: Start with openpyxl 3.1.5, test charts in Phase 2, downgrade to 3.1.3 if needed
- [01-01]: 60 parameters (vs ~50 estimated) included -- all research values without omission
- [01-01]: 12 parameter groups match research document section structure
- [01-01]: Calibri 11pt single font throughout per financial modeling convention
- [01-01]: FORMAT_TO_STYLE bridge map connects parameter format strings to NamedStyle names
- [01-02]: param_refs dict proven as interface contract (60 entries, all correct cell addresses)
- [01-02]: input_cell style applied first, number_format overridden from FORMAT_TO_STYLE lookup
- [01-02]: Protection(locked=False) on input cells now, sheet protection deferred to Phase 9
- [01-02]: Source citations italic for visual distinction within single-font convention
- [02-01]: Literal 48 used for founder vesting months (not in parameters.py, whitepaper structural constant)
- [02-01]: First-period inflation rate left blank (no prior circulating supply for meaningful annualization)
- [02-01]: Static epoch values in B/C columns (deterministic from period structure)
- [02-02]: Simple bar series for ETH benchmark (not dual-axis overlay)
- [02-02]: Charts at K1/K17/K33, style 13, width=20 height=12 consistent sizing
- [02-02]: openpyxl 3.1.5 chart rendering confirmed working with app.xml fix
- [03-01]: Fee revenue placeholder at $1M/yr in BUYBACK PARAMETERS; Phase 4 replaces with actual model
- [03-01]: All 4 price columns always visible; Active Price column (CHOOSE-driven) used for FDV/market cap/buyback
- [03-01]: Buyback burn period-adjusted: /12 for monthly (i<24), /1 for annual (i>=24)
- [03-01]: Scenario selector pattern: DataValidation + MATCH + CHOOSE on Assumptions tab (reusable for Phases 4-6)
- [04-01]: Developer Count column B uses moderate growth rate as base projection
- [04-01]: Crossover year matrix uses INDEX/MATCH on H/I/J columns (Active Price) not full 3x3
- [04-01]: "text" format maps to None in FORMAT_TO_STYLE (no numeric style override)
- [04-01]: Tail emission toggle adds DataValidation to existing PARAM_GROUPS cell
- [04-01]: Revenue splits reference base fee revenue (column D) for consistency
- [04-02]: Charts at P1/P17/P33 (right of 14-column data + annotation column O)
- [04-02]: Stacked bar with overlap=100 for proper stacking (critical openpyxl gotcha)
- [04-02]: ColorScaleRule with fixed num anchors (0/1/2) not percentile for matrix heat map
- [04-02]: Danger zone red fill on all 14 columns, red font only on column A labels
- [05-01]: Lambda Labs on-demand rate ($2.49/hr) as primary traditional benchmark (most comparable to Gonka flexible hosting)
- [05-01]: Breakeven formula: IFERROR(MAX(0,(H-D)/B),99999) -- 0 when fees exceed rental, 99999 for zero-mining edge
- [05-01]: Sensitivity matrix uses static fee revenue (not scaled with GPU count) -- annotation explains
- [05-01]: Gross income comparison for churn (traditional rental already bundles electricity)

### From v1.0

- 10 prioritized recommendations with specific parameters (capstone document)
- Emission decay: exp(-0.000475 x epochs), halving ~1,460 epochs (~4 years)
- Revenue split: 70% hosts / 20% AI Fund / 5% buyback-burn / 5% veGNK yield
- POL: 22M GNK across GNK/USDC (60%) + GNK/ETH (40%) on Uniswap v3
- Fee transition crossover: Conservative 10-12 years, moderate 3-4 years
- Host profitability threshold: GNK >= $0.85-$3.30 at critical decay points

### Pending Todos

None.

### Blockers/Concerns

- openpyxl version decision resolved: 3.1.5 confirmed working with app.xml chart fix
- Target Excel version unknown (affects chart rendering compatibility)

## Session Continuity

Last session: 2026-02-06
Stopped at: Completed 05-01-PLAN.md -- Host Profitability data model with sensitivity sections
Resume file: None

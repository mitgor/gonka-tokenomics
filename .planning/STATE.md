# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-05)

**Core value:** Leadership can tweak assumptions and instantly see the impact on tokenomics health across all dimensions
**Current focus:** Phase 8: Standalone Workbook Generation -- Plan 02 complete, glossary and cover sheet builders ready.

## Current Position

Phase: 8 of 9 (Standalone Workbook Generation)
Plan: 2 of 4 in current phase
Status: In progress
Last activity: 2026-02-06 -- Completed 08-02-PLAN.md (Glossary & Cover Sheet Builders)

Progress: [================....] ~83% (15/18 plans complete)

## Performance Metrics

**Velocity:**
- Total plans completed: 15
- Average duration: 2.4 min
- Total execution time: 36.5 min

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 1. Foundation | 2/2 | 7 min | 3.5 min |
| 2. Emission Schedule | 2/2 | 3 min | 1.5 min |
| 3. Token Price Scenarios | 2/2 | 5 min | 2.5 min |
| 4. Fee Transition | 2/2 | 6 min | 3.0 min |
| 5. Host Profitability | 2/2 | 5 min | 2.5 min |
| 6. Treasury & POL | 2/2 | 4 min | 2.0 min |
| 7. Dashboard & Assembly | 2/2 | 5 min | 2.5 min |
| 8. Standalone Generation | 1/4 | 1.5 min | 1.5 min |

**Recent Trend:**
- Last 5 plans: 06-02 (2 min), 07-01 (2 min), 07-02 (3 min), 08-02 (1.5 min)
- Trend: Consistent 1.5-3 min per plan

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
- [05-02]: CoreWeave rate in chart title only (not separate series); Lambda is primary benchmark column
- [05-02]: Breakeven chart Y-axis capped at $15 to avoid 99999 sentinel distortion
- [05-02]: Sensitivity heat map anchors at -5000/0/5000 for monthly profit range
- [06-01]: CP waterfall starts at 120M minus POL (one-time) and defense (ongoing prorated)
- [06-01]: POL revenue uses midpoint of low/high LP fee revenue minus rebalancing cost
- [06-01]: Buyback burn cross-refs Token Price col K (not recalculated)
- [06-01]: AI Fund expenses prorated from monthly to period: *days/30
- [06-01]: Defense treasury accumulation-only in main data; spending scenarios in below-data table
- [06-01]: Net Treasury USD = CP*price + POL_GNK*price + cumul_POL_fees + defense_treasury + AI_Fund_balance
- [06-01]: Defense scenario table uses L26 (Year 2 end) as baseline
- [06-02]: Stacked area uses 3 USD components (AI Fund, POL Revenue, Defense) -- avoids mixing GNK/USD units
- [06-02]: CP balance formatting: >50M GNK green, <10M GNK red (health indicators)
- [06-02]: Defense treasury formatting: >$3M green, <$1M red (midpoint/minimum targets)
- [06-02]: Net treasury gradient: $0 red, $50M yellow, $200M green
- [06-02]: Charts at P1/P17/P33 consistent with plan, right of 14-column data table
- [07-01]: Dashboard excluded from back-to-doc links; Plan 02 adds its own at F1 after merged title
- [07-01]: Emission Schedule back-link at K2 (not K1) because K1 is chart anchor
- [07-01]: LINK_FONT constant and BACK_LINK_COL_ROW dict for consistent navigation styling
- [07-02]: All Dashboard values are formulas referencing model tabs (REQ-M5-01 verified)
- [07-02]: Cross-sheet chart References point to source worksheets (Host Profitability, Treasury & POL)
- [07-02]: Breakeven chart Y-axis capped at $15 matching host_profit.py pattern
- [08-02]: Terms dict passed as parameter to glossary builder (decoupled from config)
- [08-02]: Cover sheet scenario narratives iterate in fixed order [Conservative, Base, Aggressive]
- [08-02]: LINK_FONT redefined locally in cover_sheet.py (same pattern as documentation.py)

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
Stopped at: Completed 08-02-PLAN.md (Glossary & Cover Sheet Builders)
Resume file: None

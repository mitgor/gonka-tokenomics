# Project Research Summary

**Project:** Gonka Tokenomics v1.1 Economic Modeling
**Domain:** Python-generated Excel financial models for crypto tokenomics (leadership-facing)
**Researched:** 2026-02-05
**Confidence:** HIGH

## Executive Summary

This project generates professional-grade Excel workbooks (.xlsx) that model the Gonka Network's token economics for founder/leadership decision-making. The domain is well-understood: it combines Python-to-Excel code generation (openpyxl) with Wall Street financial modeling conventions (centralized assumptions, formula-driven calculations, scenario analysis). The recommended approach is a single-dependency Python codebase (`openpyxl` only) that writes Excel formulas -- not computed values -- into structured workbooks so leadership can adjust assumptions and see results recalculate live in Excel or Google Sheets.

The core deliverable is five workbooks: four standalone models (Token Price Scenarios, Emission vs Fee Transition, Host Profitability, Treasury and POL Simulation) plus a Master Unified Workbook that links all four via a shared Assumptions tab. Each workbook follows financial modeling best practices: blue-shaded input cells, formula-protected calculation cells, 3 named scenarios (Conservative/Base/Aggressive), inline charts, and a summary Dashboard tab. The architecture uses a layered dependency model where the Assumptions tab feeds into independent models (Emission, Token Price, Treasury) which then feed into dependent models (Fee Transition, Host Profitability) before everything rolls up into the Dashboard.

The primary risks are: (1) the reflexivity trap where token price is both an input and an output, requiring explicit scenario consistency checks; (2) floating-point precision errors in the exponential decay calculation compounding over 10-year horizons; (3) openpyxl formulas having no cached values, which can cause blank cells or errors in Google Sheets; and (4) a version conflict between researchers on openpyxl pinning (3.1.5 vs 3.1.3 for chart rendering). All four are addressable with specific prevention strategies documented in the research.

## Key Findings

### Recommended Stack

**Use openpyxl as the sole dependency.** The library handles every Excel feature needed for this project: charts (line, bar, area, scatter, pie), conditional formatting, named ranges, data validation dropdowns, cell protection, freeze panes, and custom number formats. It beats XlsxWriter for this use case because it can read/modify files (critical for debugging), does not inject misleading cached formula values, and provides NamedStyle for DRY formatting. No other libraries are needed -- all math uses Python's standard `math`, `decimal`, and `datetime` modules.

**Core technologies:**
- **openpyxl** (version TBD -- see Conflicts section): Excel .xlsx generation with read/write/modify, charts, conditional formatting, named ranges, data validation
- **Python 3.10+**: Runtime, matching existing project environment
- **Standard library only** for computation: `math.exp()` for decay, `decimal.Decimal` for precision, `pathlib` for file management

**What NOT to add:** pandas (pulls numpy, overkill for formula-driven models), XlsxWriter (cannot read files), matplotlib (embeds static images instead of interactive charts), numpy (unnecessary), xlwings (requires Excel installed).

### Expected Features

**Must have (table stakes) -- universal across all workbooks:**
- Cover/title sheet with version, date, disclaimer
- Centralized Assumptions tab (blue-shaded inputs, all hard-coded numbers live here)
- 3 named scenarios (Conservative/Base/Aggressive) with cell-driven scenario selector
- Executive summary tab with 3-5 KPIs and 2-3 charts
- Color-coded cell convention (blue=input, black=formula, green=cross-tab link)
- Consistent number formatting (currency, percentages, commas, units labeled)
- Time axis standardized: monthly for Year 1-2, annual for Year 3-10
- 2-3 chart visualizations per model
- Cell protection on formula cells
- Source references per assumption
- Definitions/glossary tab

**Must have (table stakes) -- per-model highlights:**
- Model 1 (Token Price): 3-5 price trajectories, market cap calculations, circulating supply schedule, inflation rate, buyback-burn impact
- Model 2 (Fee Transition): Emission decay curve, fee revenue projections (3 growth x 3 price = 9-cell matrix), crossover point identification, revenue split waterfall, danger zone flagging (Year 8-12), tail emission toggle
- Model 3 (Host Profitability): Dual income breakdown (mining + fees), breakeven GNK price, traditional rental comparison, network size sensitivity, electricity cost sensitivity, GPU amortization
- Model 4 (Treasury & POL): Community Pool depletion schedule, POL LP fee revenue, impermanent loss estimation, buyback-burn cumulative impact, AI Training Fund balance, floor defense scenarios, net treasury value
- Model 5 (Master): Linked assumptions across all sub-models, Dashboard tab, scenario comparison matrix, navigation (hyperlinked TOC)

**Should have (differentiators):**
- Two-variable sensitivity tables (host breakeven: price x network size; treasury runway: revenue x growth rate)
- Conditional formatting heat maps on crossover tables and profitability matrices
- Scenario narratives (2-3 sentence plain-English interpretations)
- Assumption audit trail (source + date + confidence level per assumption)
- Breakeven reference lines on charts
- Time-to-X calculations ("Community Pool depleted in 8.3 years")
- Cross-model consistency checks (hidden Checks tab with TRUE/FALSE flags)
- What-if toggle switches for policy decisions (buyback-burn Y/N, tail emissions Y/N)

**Defer (v2+):**
- Tornado charts (complex to implement in openpyxl)
- Impermanent loss modeling (high complexity, V3 concentrated liquidity math -- see Pitfalls)
- Competitive benchmark overlays (requires additional research data)
- Cross-model consistency checks (implement after models stabilize)

**Never build:**
- Monte Carlo / stochastic simulation
- Live API price feeds
- VBA macros
- Pivot tables
- Interactive dashboards
- Multiple fonts / decorative formatting
- Embedded images / logos

### Architecture Approach

The architecture follows a clean layered model: Python writes formulas (never computed values) into Excel, so workbooks are self-calculating. A `parameters.py` module defines all constants from v1.0 research. A `workbook_base.py` builds the Assumptions tab and returns a `param_refs` dictionary mapping parameter names to cell addresses. Each model module (`emission.py`, `token_price.py`, etc.) receives `param_refs` and writes formulas referencing Assumptions cells. A `styles.py` module defines all NamedStyles once per workbook. Generators (`master.py`, `standalone.py`) orchestrate assembly.

**Major components:**
1. **parameters.py** -- single source of truth for all ~50 input parameters from v1.0 research
2. **workbook_base.py** -- builds Assumptions tab, returns param_refs dict, registers styles
3. **emission.py** -- emission decay schedule (Layer 1, no cross-tab dependencies)
4. **token_price.py** -- multi-scenario price trajectories (Layer 1)
5. **treasury.py** -- treasury depletion, POL, buyback simulation (Layer 1)
6. **fee_transition.py** -- fee vs emission crossover (Layer 2, depends on emission + price)
7. **host_profit.py** -- host ROI model (Layer 2, depends on emission + price)
8. **charts.py + Dashboard builder** -- summary charts from all models (Layer 3)
9. **master.py** -- orchestrates master workbook generation
10. **standalone.py** -- generates 4 standalone workbooks as subsets of master logic

**Tab structure (Master Workbook, 8 tabs):**
Documentation (green) -> Assumptions (blue, editable) -> Emission Schedule (gray) -> Token Price (gray) -> Fee Transition (gray) -> Host Profitability (gray) -> Treasury & POL (gray) -> Dashboard (orange)

**Key architectural decisions:**
- All cross-sheet references use absolute cell addresses for assumptions (`Assumptions!$B$12`) and relative references within same-tab data
- Named ranges used sparingly (top 10-15 most-referenced parameters only)
- Standalones are subsets of master logic, not separate codebases
- Sheet protection with no password (prevents accidental overwrites, not malicious edits)
- Monthly or quarterly granularity for long horizons to keep file size under 5MB Google Sheets limit

### Critical Pitfalls

**Top 5 pitfalls ranked by severity and likelihood:**

1. **Reflexivity trap (CRITICAL)** -- GNK price is both input and output; model scenarios appear independent but are deeply coupled. **Prevention:** Single Assumptions tab drives all tabs; build a Scenario Consistency tab that cross-references price assumptions with growth/fee scenarios and flags contradictions. Label every price-dependent output with its price assumption.

2. **Exponential decay precision errors (CRITICAL)** -- Float representation of 0.000475 compounds over 3,650+ epochs, potentially shifting the crossover year by 1+ year. **Prevention:** Use `decimal.Decimal('0.000475')` for Python computation; use closed-form formula `E(t) = E0 * (1-r)^t` in Excel cells (not iterative); include a validation row comparing geometric series sum against cell-by-cell sum.

3. **openpyxl formulas not calculated (CRITICAL)** -- Generated files have no cached formula values. Google Sheets may show blanks or errors. **Prevention:** Restrict to common Excel/Sheets formula subset (no XLOOKUP, FILTER, LAMBDA); consider two-pass approach writing Python-computed values then overwriting with formulas; test every workbook in Google Sheets before delivery.

4. **openpyxl chart rendering bugs (MODERATE)** -- Versions 3.1.4+ changed the Application XML string, breaking chart labels/legends in Excel. **Prevention:** Version pinning decision required (see Conflicts section); test all chart types in target Excel version; minimize chart styling to reduce rendering bug surface area.

5. **Hardcoded assumptions scattered across tabs (MODERATE)** -- Each model script defines its own constants, creating divergence. **Prevention:** Single `parameters.py` config dict; Assumptions tab generated from this dict; all formula cells reference Assumptions tab only; Wall Street color coding makes hardcoded values visually obvious.

## Researcher Conflicts and Open Decisions

### Conflict: openpyxl Version -- 3.1.5 vs 3.1.3

**STACK.md recommends:** openpyxl 3.1.5 (latest stable, released 2024-06-28). Rationale: production-stable, no known API issues.

**PITFALLS.md recommends:** openpyxl 3.1.3 (pinned). Rationale: versions 3.1.4+ have a documented bug where the `app.xml` Application element breaks chart rendering in Microsoft Excel (chart labels disappear, legends misposition, axis formatting fails). The bug is documented in openpyxl user group reports.

**Recommendation:** Start with 3.1.5 and test chart rendering in the target Excel version during Phase 2 (first model with charts). If charts break, downgrade to 3.1.3 or apply the post-processing workaround (unzip .xlsx, fix Application string in `docProps/app.xml`, re-zip). The workaround is mechanical and can be automated in the generation script.

**Decision needed from user:** Which version of Excel does leadership use? This determines whether the chart bug is triggered.

### Conflict: Named Ranges -- Use vs Avoid

**STACK.md and ARCHITECTURE.md recommend:** Use named ranges sparingly (top 10-15 parameters) via openpyxl `DefinedName`. Makes formulas readable (`=initial_daily_emission*EXP(-decay_rate*B3)` vs `=Assumptions!$B$11*EXP(-Assumptions!$B$12*B3)`).

**FEATURES.md anti-features list says:** "Named ranges for cells" is an anti-feature -- "creates phantom references that are nearly impossible to debug. Industry anti-pattern confirmed by ICAEW and Wall Street Prep." Recommends standard cell references with clear labels instead.

**PITFALLS.md warns:** openpyxl named ranges cannot reference other named ranges or use complex expressions; broken references show `#REF!` errors.

**Recommendation:** Use direct cell references (`Assumptions!$B$12`) as the primary approach. Named ranges add debugging complexity and have openpyxl limitations. The formulas are generated by Python (not hand-typed), so readability in Excel is a secondary concern -- the Python code is the readable source. If named ranges are desired later for polish, they can be added in Phase 10 without changing formula logic.

### Conflict: Impermanent Loss Scope

**FEATURES.md** lists IL estimation as a table-stakes feature for Model 4 (Treasury & POL) but also defers it to post-first-release as high complexity.

**PITFALLS.md** warns that using the V2 IL formula for V3 concentrated positions is a critical pitfall (underestimates IL by 4-10x).

**Recommendation:** Defer IL modeling to v2. Getting the V3 concentrated liquidity IL formula right requires tick-range math that is complex and error-prone. Shipping a wrong IL estimate is worse than shipping none. For v1, show POL fee revenue projections with a clearly labeled caveat: "IL impact not modeled; see v2 for concentrated position risk analysis."

### Open Question: Sensitivity Tables -- Static vs Dynamic

**FEATURES.md** confirms that openpyxl cannot generate Excel's native Data Table (What-If Analysis) feature. Sensitivity tables must be pre-calculated in Python and written as static grids. This means if leadership changes an assumption, sensitivity tables do NOT update.

**Recommendation:** Accept static sensitivity tables for v1. Document clearly on the tab: "These tables are pre-calculated for the default assumptions. Regenerate the workbook to update." This is a reasonable tradeoff -- the alternative is not having sensitivity tables at all.

## Implications for Roadmap

Based on research, suggested phase structure follows the architecture's dependency layers:

### Phase 1: Foundation and Shared Infrastructure
**Rationale:** Everything depends on the shared parameter system, style definitions, and workbook base. Build the spine first.
**Delivers:** `parameters.py` with all ~50 v1.0 research parameters, `styles.py` with NamedStyles (currency, percent, header, input, formula), `workbook_base.py` with Assumptions tab builder and param_refs return pattern, `generate.py` CLI entry point skeleton.
**Addresses:** Table stakes universal features (assumptions tab, color coding, number formatting, cell protection)
**Avoids:** Pitfall #5 (hardcoded assumptions) by establishing single source of truth from day one

### Phase 2: Emission Schedule Model
**Rationale:** Simplest model. Upstream dependency for Fee Transition and Host Profitability. Validates the core formula-writing pattern.
**Delivers:** `emission.py`, first standalone workbook (`gonka_emission.xlsx`), inline emission decay chart
**Addresses:** Emission decay curve feature, circulating supply schedule
**Avoids:** Pitfall #2 (precision errors) by implementing closed-form formula and validation row from the start

### Phase 3: Token Price Scenarios Model
**Rationale:** Independent model (Layer 1). Tests multi-scenario pattern with 3-5 price trajectories. Upstream dependency for models that need price data.
**Delivers:** `token_price.py`, standalone workbook, price trajectory charts, market cap calculations, inflation rate
**Addresses:** Token Price table stakes features
**Avoids:** Pitfall #1 (reflexivity) by linking price scenarios to the shared Assumptions tab

### Phase 4: Fee Transition Crossover Model
**Rationale:** First Layer 2 model with cross-tab dependencies. Tests the cross-sheet formula reference pattern. Contains the project's most critical analysis (when do fees exceed emissions?).
**Delivers:** `fee_transition.py`, standalone workbook, crossover analysis with 2D sensitivity matrix (price x growth), revenue split waterfall, danger zone flagging
**Addresses:** Fee Transition table stakes features, crossover sensitivity tables (differentiator)
**Avoids:** Pitfall #7 (crossover depends on price) by showing crossover as a band/matrix, not a single point

### Phase 5: Host Profitability Model
**Rationale:** Most complex cross-tab dependencies (emission + price). High decision-making value for leadership (host economics is the network's competitive moat).
**Delivers:** `host_profit.py`, standalone workbook, dual income breakdown, breakeven price analysis, traditional rental comparison, network size sensitivity
**Addresses:** Host Profitability table stakes features
**Avoids:** Pitfall #8 (time-value) by including optional discount rate on Assumptions tab

### Phase 6: Treasury and POL Simulation
**Rationale:** Relatively independent (Layer 1) but has the most parameters. Defers IL modeling to v2.
**Delivers:** `treasury.py`, standalone workbook, Community Pool depletion schedule, POL fee revenue (without IL), buyback-burn cumulative, floor defense scenarios, net treasury value
**Addresses:** Treasury & POL table stakes features (except IL estimation, deferred)
**Avoids:** Pitfall #4 (wrong IL formula) by explicitly deferring IL to v2

### Phase 7: Charts, Dashboard, and Master Workbook
**Rationale:** All models must be complete before the Dashboard can pull from them. This phase assembles everything.
**Delivers:** `charts.py` helpers, Dashboard tab with 4-6 summary charts, `master.py` orchestrator, master workbook (`gonka_master_model.xlsx`) with all 8 tabs linked
**Addresses:** Master Unified table stakes (linked assumptions, dashboard, scenario comparison, navigation), chart differentiators (breakeven lines, direct labels)
**Avoids:** Pitfall #3 (Google Sheets formula issues) via testing; Pitfall #9 (file size) via monthly granularity

### Phase 8: Standalone Workbook Generation
**Rationale:** Standalones are subsets of master logic. Build after master stabilizes.
**Delivers:** `standalone.py`, 4 standalone workbooks with filtered Assumptions tabs, focused dashboards, Documentation tabs
**Addresses:** Standalone delivery requirement
**Avoids:** Pitfall #5 (assumption divergence) by generating from same config dict

### Phase 9: Polish, Documentation, and Validation
**Rationale:** Final pass for professional quality. Cross-model consistency checks, print optimization, Google Sheets validation.
**Delivers:** Documentation tab content, print-friendly layout, cross-model consistency checks (hidden Checks tab), scenario consistency matrix, version/changelog on cover sheet
**Addresses:** Remaining differentiators (consistency checks, print formatting, audit trail)
**Avoids:** Pitfall #3 (Google Sheets) via comprehensive testing; Pitfall #10 (formatting inconsistency) via audit

### Phase Ordering Rationale

- **Phases 1-3 build the foundation and independent models.** No cross-tab complexity. Each phase validates a core pattern (parameter system, formula writing, scenario handling).
- **Phases 4-5 introduce cross-tab dependencies.** By this point, the formula reference pattern is proven. Emission and Price data are available for downstream models.
- **Phase 6 is independent but delayed** because it has the most parameters and benefits from the patterns established in earlier phases. IL is explicitly deferred.
- **Phases 7-9 are integration and polish.** The master workbook and standalones are assembly tasks, not new logic. Polish comes last when the data model is stable.
- **This order matches the architecture's dependency graph exactly:** Layer 0 (parameters) -> Layer 1 (emission, price, treasury) -> Layer 2 (fee transition, host profit) -> Layer 3 (dashboard, master, standalones).

### Research Flags

Phases likely needing deeper research during planning:
- **Phase 4 (Fee Transition):** The crossover analysis is the project's centerpiece. The 2D sensitivity matrix (price x growth rate) needs careful formula design to avoid the reflexivity trap.
- **Phase 6 (Treasury & POL):** POL fee revenue projections require Uniswap V3 LP math. Even without IL modeling, fee accrual estimates need validated formulas.
- **Phase 7 (Charts & Dashboard):** Chart rendering compatibility between openpyxl, Excel, and Google Sheets needs hands-on testing. The openpyxl version decision will be resolved here.

Phases with standard patterns (skip research-phase):
- **Phase 1 (Foundation):** Well-documented openpyxl patterns for styles, parameters, workbook creation
- **Phase 2 (Emission):** Straightforward exponential decay formula; closed-form solution is textbook math
- **Phase 3 (Token Price):** Standard scenario modeling with line charts
- **Phase 8 (Standalones):** Subset extraction from master; no new patterns

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | openpyxl capabilities verified against official docs. Single dependency, well-maintained. Only uncertainty is version pinning (3.1.3 vs 3.1.5 for chart bugs). |
| Features | HIGH | Feature list cross-referenced against industry financial modeling standards (ICAEW, Wall Street Prep, FMI) and tokenomics-specific templates (InnMind, Foresight). openpyxl feasibility confirmed for all must-have features. |
| Architecture | HIGH | Layered dependency model, formula-writing pattern, and module structure all follow established financial modeling and software engineering best practices. Verified against openpyxl API docs. |
| Pitfalls | HIGH | Critical pitfalls sourced from openpyxl bug trackers, IEEE 754 documentation, DeFi protocol documentation (Uniswap V3), and industry financial modeling error catalogs. Prevention strategies are concrete and actionable. |

**Overall confidence:** HIGH

### Gaps to Address

- **openpyxl version decision:** Needs resolution via hands-on chart rendering test in target Excel version. Not a blocker for Phase 1-2 (no charts), becomes relevant in Phase 3+.
- **Google Sheets formula compatibility:** Research identifies the risk but the exact set of formulas that fail needs testing with the actual generated workbook. Plan for a Google Sheets validation pass in Phase 7-9.
- **Uniswap V3 LP fee estimation:** Even without IL modeling, POL fee revenue projections need a validated formula for concentrated liquidity fee accrual. This is deferred to Phase 6 planning.
- **Target Excel version:** Research identifies version-specific chart rendering. Need to know what version leadership uses (Excel 365, Excel 2021, Google Sheets only, etc.).
- **Time granularity decision:** Research recommends monthly for Year 1-2, annual for Year 3-10. Confirm with user whether daily granularity is needed for any period (impacts file size and Phase 2 row counts).
- **Named ranges vs direct cell references:** Research is split. Recommendation is to use direct references and revisit named ranges as a polish item. User may have a preference.

## Sources

### Primary (HIGH confidence)
- [openpyxl official documentation](https://openpyxl.readthedocs.io/en/stable/) -- API verification for charts, styles, named ranges, data validation, protection, formulas
- [openpyxl PyPI](https://pypi.org/project/openpyxl/) -- version 3.1.5 release info
- [Python decimal module](https://docs.python.org/3/library/decimal.html) -- precision arithmetic
- [Python floating-point docs](https://docs.python.org/3/tutorial/floatingpoint.html) -- IEEE 754 limitations

### Secondary (MEDIUM confidence)
- [Wall Street Prep Financial Modeling](https://www.wallstreetprep.com/knowledge/financial-modeling/) -- tab structure, color conventions, sensitivity analysis
- [CFI Excel Model Documentation](https://corporatefinanceinstitute.com/resources/excel/documenting-excel-models-best-practices/) -- assumptions tab patterns
- [FMI Financial Modeling Best Practices](https://fminstitute.com/modeling-resources/financial-modeling-best-practices/) -- professional Excel standards
- [ICAEW Financial Modelling Code](https://www.icaew.com/-/media/corporate/files/technical/technology/excel/financial-modelling-code.ashx) -- industry model governance
- [InnMind Tokenomics Spreadsheet](https://innmind.com/downloads/tokenomics-spreadsheet/) -- tokenomics model feature reference
- [Google Sheets import compatibility](https://support.google.com/docs/thread/219934507) -- formula and chart compatibility
- [openpyxl chart rendering bugs](https://groups.google.com/g/openpyxl-users/c/khC6BTqaH3Y) -- version 3.1.4+ chart issues

### Tertiary (LOW confidence)
- Google Sheets icon set / data bar rendering (community reports, not official docs)
- openpyxl Application string chart bug (user group reports, not official changelog)
- Uniswap V3 concentrated IL amplification factor (ranges cited as 4-10x; exact multiplier depends on position parameters)

---
*Research completed: 2026-02-05*
*Ready for roadmap: yes*

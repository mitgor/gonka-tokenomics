# Phase 6: Treasury & POL Simulation - Research

**Researched:** 2026-02-06
**Domain:** Excel financial model generation (openpyxl) for treasury/POL/buyback simulation
**Confidence:** HIGH

## Summary

Phase 6 is the "most parameters" phase -- it pulls from more parameter groups than any prior phase (TOKEN SUPPLY, REVENUE ALLOCATION, POL PARAMETERS, BUYBACK PARAMETERS, FLOOR DEFENSE) while also referencing three upstream tabs (Emission Schedule, Token Price, Fee Transition). The core challenge is organizing 6+ treasury components into a coherent worksheet that remains scannable by leadership. This is not a new technology problem; it is a composition and layout problem using patterns already proven in Phases 2-5.

The standard approach follows the established `build_*_tab(wb, param_refs, ...)` pattern with 32 data rows (24 monthly + 8 annual). The treasury tab differs from prior tabs in that it has more independent "sub-models" (Community Pool waterfall, POL revenue, buyback-burn cumulative, AI Training Fund balance, floor defense, net treasury value) that must coexist on one worksheet. The recommended layout uses column groups A-N for the main data table plus below-data summary sections for Time-to-X callouts, similar to how host_profit.py places sensitivity tables below the main data.

**Primary recommendation:** Build a single `generators/treasury.py` with `build_treasury_tab()` that follows the established 32-row pattern with ~14-16 data columns organized in logical groups: (A) Period, (B-D) Community Pool waterfall, (E-F) POL revenue, (G-H) Buyback-burn cumulative, (I-K) AI Training Fund, (L-M) Floor defense, (N) Net treasury value. Place Time-to-X callout cells and the IL caveat label in below-data sections (rows 36+).

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| openpyxl | 3.1.5 | Excel .xlsx generation | Sole dependency; already in use; chart rendering confirmed |
| Python stdlib | 3.10+ | math, decimal, pathlib | No external computation libraries per REQ-F05 |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| openpyxl.utils.quote_sheetname | 3.1.5 | Cross-tab formula references | When referencing Emission Schedule, Token Price, Fee Transition tabs |
| openpyxl.formatting.rule | 3.1.5 | CellIsRule, ColorScaleRule | Conditional formatting on treasury health indicators |
| openpyxl.chart | 3.1.5 | LineChart, AreaChart, BarChart | 2-3 charts for treasury visualization |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Single treasury tab | Separate tabs per component | Would bloat workbook; Phase 7 expects exactly one Treasury tab in 8-tab structure |
| Static column layout | Dynamic column generation | Unnecessary complexity; column count is known at design time |

## Architecture Patterns

### Recommended File Structure
```
generators/
  treasury.py          # NEW - build_treasury_tab() function
  emission.py          # Cross-ref: mining emission values
  token_price.py       # Cross-ref: active price per period
  fee_transition.py    # Cross-ref: fee revenue per period (buyback $, AI Fund $)
  ...existing files unchanged...
```

### Pattern 1: Function Signature Following Established Convention
**What:** `build_treasury_tab(wb, param_refs, emission_meta, price_meta, fee_meta) -> treasury_meta`
**When to use:** This is the only entry point for Phase 6.
**Why this signature:** Phase 6 depends on Phase 1 (param_refs), Phase 2 (emission_meta for period structure), Phase 3 (price_meta for active GNK price), and Phase 4 (fee_meta for fee revenue splits). This matches how `build_host_profit_tab` already receives all four upstream metas.
```python
# Source: Established pattern from generators/host_profit.py line 411
def build_treasury_tab(wb, param_refs, emission_meta, price_meta, fee_meta):
    ws = wb.create_sheet(title="Treasury & POL")
    ws.sheet_properties.tabColor = TAB_COLOR_CALC
    # ... build columns, charts, below-data sections ...
    return treasury_meta
```

### Pattern 2: Cross-Tab References via quote_sheetname
**What:** All references to other tabs use `quote_sheetname()` + meta dict column letters.
**When to use:** Every formula that reads Emission Schedule, Token Price, or Fee Transition data.
**Example:**
```python
# Source: Established pattern from generators/fee_transition.py lines 296-306
es_sheet = quote_sheetname(emission_meta["sheet_name"])
tp_sheet = quote_sheetname(price_meta["sheet_name"])
ft_sheet = quote_sheetname(fee_meta["sheet_name"])

# Fee Transition buyback share column
ft_buyback_col = fee_meta["cols"]["buyback_share"]   # "M"
ft_ai_fund_col = fee_meta["cols"]["ai_fund_share"]   # "L"

# Reference buyback $ for period i
f"={ft_sheet}!{ft_buyback_col}{ft_row}"
```

### Pattern 3: Period-Aware Formulas (days=30 vs days=365)
**What:** Monthly periods (i<24) use 30-day period; annual periods (i>=24) use 365-day period.
**When to use:** Any per-period calculation (Community Pool drawdown, defense spending, POL revenue).
**Example:**
```python
# Source: Established pattern across all generators
days = 30 if i < 24 else 365

# Community Pool unlock per period (linear over 10 years = 3650 days)
cp_formula = f"={cp_ref}/3650*{days}"

# POL revenue per period (annual revenue prorated)
pol_rev_formula = f"={pol_rev_ref}*{days}/365"
```

### Pattern 4: Below-Data Summary Sections
**What:** Place callout cells, matrices, and annotations below row 34 (after 32 data rows).
**When to use:** Time-to-X callouts (REQ-D06), IL caveat (REQ-M4-07).
**Example layout:**
```
Row 36: Section header "TIME-TO-X MILESTONES"
Row 37: "Community Pool depleted in:" | =formula | "years (Base scenario)"
Row 38: "Floor defense exhausted in:" | =formula | "months at Tier 1"
...
Row 42: IL caveat label
```
```python
# Source: Established pattern from generators/host_profit.py rows 36-55
ws.merge_cells("A36:F36")
header_cell = ws.cell(row=36, column=1, value="TIME-TO-X MILESTONES")
header_cell.style = "section_header"
```

### Pattern 5: Meta Dict Return for Downstream Tabs
**What:** Return a dict with sheet_name, row ranges, and column mappings.
**When to use:** Phase 7 Dashboard needs to reference Treasury tab cells.
```python
treasury_meta = {
    "sheet_name": "Treasury & POL",
    "header_row": 2,
    "data_start_row": 3,
    "data_end_row": 34,
    "cols": {
        "period_label": "A",
        "cp_balance": "B",
        # ... etc
        "net_treasury_usd": "N",
    },
    "time_to_x_start_row": 37,
    "il_caveat_row": 43,
}
```

### Anti-Patterns to Avoid
- **Named ranges**: Explicitly banned per FEATURES.md anti-pattern finding and STATE.md decision. Use direct cell references only.
- **Hardcoded parameter values in formulas**: All numbers must come from param_refs (Assumptions tab). Never write `22000000` directly; use `param_refs["POL GNK Allocation"]`.
- **IL modeling**: Explicitly deferred to v2. Do NOT include IL calculations. Only add the caveat label (REQ-M4-07).
- **Multiple treasury tabs**: Phase 7 expects exactly 8 tabs in order (Documentation -> Assumptions -> Emission Schedule -> Token Price -> Fee Transition -> Host Profitability -> Treasury & POL -> Dashboard). Treasury must be a single tab.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Period structure (24 monthly + 8 annual) | Custom period builder | Cross-ref from Emission Schedule tab (column A) | Period labels already exist; cross-ref ensures consistency |
| Fee revenue per period | Recalculate from developer count | Cross-ref from Fee Transition tab (column D = base fee revenue) | Already calculated with all growth rate logic |
| Buyback $ amount per period | Recalculate from fee revenue * 5% | Cross-ref from Fee Transition tab (column M = buyback share) | Fee Transition already computes the 70/20/5/5 split |
| AI Fund $ inflow per period | Recalculate from scratch | Cross-ref from Fee Transition tab (column L = AI Fund share) | Already calculated and scenario-aware |
| Active GNK price per period | Hardcode price curve | Cross-ref from Token Price tab (column F = active price) | Scenario selector drives this automatically |
| Chart rendering fix | Custom workaround | `fix_chart_rendering()` from chart_utils.py | Already handles the openpyxl 3.1.5 app.xml issue |

**Key insight:** Phase 6 is primarily a COMPOSITION phase -- it combines data that already exists in upstream tabs with a few new calculations (running balances, depletion schedules, cumulative burns). Resist the urge to recalculate what's already computed.

## Common Pitfalls

### Pitfall 1: Recalculating What Upstream Tabs Already Compute
**What goes wrong:** Writing formulas that re-derive fee revenue, buyback amounts, or emission values from scratch instead of cross-referencing existing columns.
**Why it happens:** Each generator file feels "independent" -- developer forgets that Fee Transition already has buyback $ in column M.
**How to avoid:** Before writing any formula, check if the value already exists in emission_meta, price_meta, or fee_meta column maps. If so, cross-reference it.
**Warning signs:** Formula strings that reference param_refs for revenue allocation percentages when those splits are already applied in Fee Transition.

### Pitfall 2: Community Pool Double-Counting
**What goes wrong:** The Community Pool (120M GNK) has multiple outflows: POL allocation (22M), dev grants, floor defense GNK allocation (6M/yr). If the emission tab's "Community Pool Unlock" (column E) already distributes the full 120M linearly, subtracting POL and defense again double-counts.
**Why it happens:** The Emission Schedule tab distributes 120M GNK / 3650 days linearly in column E. This is the RAW unlock rate. The Treasury tab needs to show: of those unlocked GNK, how much goes to POL (one-time), how much to defense (annual), how much remains as general community funds.
**How to avoid:** The Treasury tab should START with the Emission Schedule's cumulative CP unlock as the "gross unlocked" amount, then SUBTRACT POL allocation and defense allocation to show "available Community Pool balance." The POL allocation is a one-time draw (22M GNK at period 0 or early periods), while defense is an annual draw (6M GNK/yr).
**Warning signs:** Community Pool balance going negative earlier than expected because outflows are counted against both the general unlock AND separately.

### Pitfall 3: Floor Defense Spending Units Confusion (GNK vs USD)
**What goes wrong:** Floor defense has TWO dimensions: (1) GNK allocated annually from Community Pool (6M GNK/yr, to be converted to USDC), and (2) USDC treasury target ($2-5M) for actual buyback execution. Mixing up which column tracks GNK and which tracks USD creates nonsense numbers.
**Why it happens:** The defense mechanism converts GNK to USDC and then spends USDC on buybacks. The conversion depends on GNK price, which varies by scenario.
**How to avoid:** Use separate columns: one for "Defense GNK Allocated" (from Community Pool, in GNK) and one for "Defense Treasury USD" (converted at active GNK price, spent down during active defense). Label units explicitly.
**Warning signs:** A "defense balance" column showing values that don't match expected magnitude (millions of GNK vs millions of USD).

### Pitfall 4: Buyback-Burn Token Counting vs Dollar Counting
**What goes wrong:** REQ-M4-03 asks for "running total tokens burned" and "% of total supply." The Fee Transition tab's buyback column M is in DOLLARS. Converting $ to GNK tokens requires dividing by the active GNK price for that period. If price changes per period (it does -- linear interpolation), each period's burn in GNK is different even if the $ amount were constant.
**Why it happens:** The buyback $ is already computed in Fee Transition. But converting to GNK tokens is a new calculation specific to Treasury.
**How to avoid:** Buyback GNK per period = Fee Transition buyback $ / Token Price active price. This already exists in the Token Price tab (column K: Buyback Burn GNK). Cross-reference it rather than recalculating.
**Warning signs:** Buyback GNK values that differ between Token Price tab (column K) and Treasury tab.

### Pitfall 5: Time-to-X Formulas That Break on "Never Depleted" Scenarios
**What goes wrong:** "Community Pool depleted in: X years" uses a search formula (like MATCH or a manual calculation). Under aggressive growth scenarios, the Community Pool may never deplete within 10 years. The formula returns an error or a misleading number.
**Why it happens:** MATCH/INDEX assume the searched value exists in the range. If the balance never reaches 0, there's no match.
**How to avoid:** Wrap Time-to-X calculations in IFERROR: `=IFERROR(formula, "Not depleted within 10 years")`. This follows the same pattern as the IFERROR wrappers used throughout Phases 4-5.
**Warning signs:** #N/A errors in callout cells.

### Pitfall 6: Column Count Exceeding Single-Screen Width
**What goes wrong:** With 6 sub-models (CP, POL, buyback, AI Fund, defense, net value) each needing 2-3 columns, the tab could stretch to 16+ columns, making it hard to read.
**Why it happens:** Treasury has more components than any prior model.
**How to avoid:** Limit to ~14-15 data columns max (matching Fee Transition's 14). Combine where possible: net treasury value is a single summary column, not a breakdown. Place detailed breakdowns in below-data sections if needed.
**Warning signs:** Headers that wrap to 3+ lines because columns are too narrow.

## Code Examples

### Example 1: Community Pool Waterfall Balance
```python
# Column B: Community Pool Balance (GNK)
# Starting 120M, minus POL allocation (one-time, period 0), minus defense allocation (annual)
# minus general Community Pool unlock (linear over 10 years)
# The waterfall ACCUMULATES outflows and shows remaining balance

cp_ref = param_refs["Community Pool"]                    # 120M
pol_alloc_ref = param_refs["POL GNK Allocation"]         # 22M
defense_annual_ref = param_refs["Annual GNK Allocation for Defense"]  # 6M

# Period 0 (first month): Starting balance minus POL (one-time)
# Then each period subtracts defense allocation (prorated) and general unlock
if i == 0:
    # First period: deduct POL allocation immediately, plus first period's other outflows
    formula = (
        f"={cp_ref}-{pol_alloc_ref}"
        f"-{defense_annual_ref}*{days}/365"
    )
else:
    # Subsequent periods: prior balance minus period's outflows
    formula = (
        f"=B{row-1}"
        f"-{defense_annual_ref}*{days}/365"
    )
```

### Example 2: POL Revenue Per Period (Cross-Referenced from Parameters)
```python
# Column E: POL LP Fee Revenue (USD)
# Uses low/high range midpoint or separate columns for low/high
pol_rev_low_ref = param_refs["Expected LP Fee Revenue Low"]    # $550K/yr
pol_rev_high_ref = param_refs["Expected LP Fee Revenue High"]  # $1.1M/yr

# Midpoint approach (simple, matches "Base" scenario thinking):
pol_formula = f"=({pol_rev_low_ref}+{pol_rev_high_ref})/2*{days}/365"
```

### Example 3: Cumulative Buyback-Burn (Cross-Referenced)
```python
# Column G: Cumulative Tokens Burned (GNK) - running total
# Token Price tab already has per-period buyback in GNK (column K)
tp_buyback_col = price_meta["cols"]["buyback_burn"]  # "K"

if i == 0:
    formula = f"={tp_sheet}!{tp_buyback_col}{tp_row}"
else:
    formula = f"=G{row-1}+{tp_sheet}!{tp_buyback_col}{tp_row}"

# Column H: Burn as % of Total Supply
total_supply_ref = param_refs["Total Supply"]
pct_formula = f"=G{row}/{total_supply_ref}"
```

### Example 4: Net Treasury Value (USD)
```python
# Column N: Net Treasury Value (USD)
# = CP Balance (GNK) * Active Price + POL Position Value (USD) + Defense Treasury (USD)
# POL position value = POL GNK allocation * active price (simplified, IL deferred)
# + any accumulated USDC from LP fees

tp_active_col = price_meta["cols"]["active_price"]  # "F"
formula = (
    f"=B{row}*{tp_sheet}!{tp_active_col}{tp_row}"  # CP balance in USD
    f"+{pol_alloc_ref}*{tp_sheet}!{tp_active_col}{tp_row}"  # POL GNK value in USD
    f"+F{row}"  # Cumulative POL revenue (USDC)
    f"+M{row}"  # Defense treasury balance (USDC)
)
```

### Example 5: Time-to-X Callout Cell
```python
# Below-data section: Community Pool depletion year
# Find first period where CP balance <= 0
ws.cell(row=37, column=1, value="Community Pool depleted in:")
formula = (
    '=IFERROR('
    'INDEX($A$3:$A$34,MATCH(TRUE,INDEX($B$3:$B$34<=0,0),0))'
    ',"Not depleted within 10 years")'
)
ws.cell(row=37, column=2, value=formula).style = "formula_cell"
```

### Example 6: IL Caveat Label (REQ-M4-07)
```python
# Static label -- no formula, just a clear caveat
caveat_cell = ws.cell(
    row=caveat_row, column=1,
    value="IL impact not modeled; see v2 for concentrated position risk analysis",
)
caveat_cell.font = Font(name="Calibri", size=11, italic=True, color="9C0006")
ws.merge_cells(
    start_row=caveat_row, start_column=1,
    end_row=caveat_row, end_column=6,
)
```

### Example 7: generate.py Integration
```python
# In generate.py generate_all():
from generators.treasury import build_treasury_tab

# Phase 6: Treasury & POL Simulation
treasury_meta = build_treasury_tab(wb, param_refs, emission_meta, price_meta, fee_meta)
```

## Column Layout Recommendation

Based on the 8 requirements (REQ-M4-01 through REQ-M4-07 + REQ-D06), here is the recommended column layout for the 32-row data table:

| Col | Header | Source | Req | Style |
|-----|--------|--------|-----|-------|
| A | Period | Cross-ref Emission Schedule | -- | crossref_cell |
| B | CP Balance (GNK) | Waterfall: 120M - POL - defense - general | REQ-M4-01 | tokens |
| C | CP Outflows (GNK) | Period's Community Pool draws | REQ-M4-01 | tokens |
| D | POL Revenue ($) | Midpoint of low/high LP fee revenue, prorated | REQ-M4-02 | currency |
| E | Cumulative POL Revenue ($) | Running sum of column D | REQ-M4-02 | currency |
| F | Buyback Burn (GNK) | Cross-ref Token Price column K | REQ-M4-03 | tokens |
| G | Cumulative Burn (GNK) | Running sum of column F | REQ-M4-03 | tokens |
| H | Burn % of Supply | Cumulative burn / Total Supply | REQ-M4-03 | percent |
| I | AI Fund Inflows ($) | Cross-ref Fee Transition column L | REQ-M4-04 | currency |
| J | AI Fund Balance ($) | Running balance: inflows - estimated expenses | REQ-M4-04 | currency |
| K | Defense GNK Allocated | Annual 6M GNK prorated to period | REQ-M4-05 | tokens |
| L | Defense Treasury ($) | GNK converted to USD at active price, minus spending | REQ-M4-05 | currency |
| M | Net Treasury (GNK) | CP Balance + POL GNK + other GNK holdings | REQ-M4-06 | tokens |
| N | Net Treasury ($) | All assets valued in USD at active GNK price | REQ-M4-06 | currency |

**Total: 14 data columns (A-N)** -- matches the pattern of Fee Transition's 14 columns.

Below-data sections (row 36+):
- Row 36: Section header "TIME-TO-X MILESTONES"
- Row 37: Community Pool depletion callout (REQ-D06)
- Row 38: Floor defense exhaustion callout (REQ-D06)
- Row 39: Buyback 1% of supply milestone (REQ-D06)
- Row 40: blank
- Row 41: IL caveat label (REQ-M4-07)

## New Parameters Needed

Analysis of parameters.py shows most treasury parameters already exist. However, a few operational assumptions are needed for the AI Training Fund and floor defense models:

| Parameter | Suggested Value | Unit | Source | Why Needed |
|-----------|----------------|------|--------|------------|
| AI Fund Monthly Expenses | 50,000 | USD/month | Placeholder | REQ-M4-04 requires "inflows - expenses - surplus" |
| Defense Spending Rate (Tier 1) | 0.005 | of defense treasury/day | Rec #7 | REQ-M4-05 requires "X months of active defense" |
| Defense Active Duration | 6 | months | Scenario input | REQ-M4-05 configurable defense duration |

**Decision needed:** Whether to add these to parameters.py as new PARAM_GROUPS entries (following the "no constants outside parameters.py" rule) or compute them inline as derived values. Recommendation: add them to parameters.py in an existing group or a new "TREASURY OPERATIONS" group, maintaining the single-source-of-truth principle (REQ-F01).

Alternatively, for simplicity, the AI Fund expenses could be modeled as a fixed assumption on the Assumptions tab (added via parameters.py), and the defense spending rate is already implicit in the existing floor defense parameters. The planner should decide the exact approach.

## Formulas That Need Special Attention

### Community Pool Waterfall
The Emission Schedule tab already unlocks 120M GNK linearly (column E). The Treasury tab's Community Pool model must account for:
1. POL allocation (22M GNK) -- drawn from the pool at deployment (modeled as period 0 deduction)
2. Floor defense allocation (6M GNK/yr) -- ongoing annual draw
3. General community grants / ecosystem -- the "remaining" after POL and defense

The balance formula: `CP_Balance = 120M - 22M(POL) - 6M/yr*years_elapsed - other_draws`

This is separate from the emission schedule's CP unlock column, which shows gross unlock rate. The treasury tab shows the BALANCE of what remains after allocations.

### POL Revenue Projection
The POL parameters include a low ($550K/yr) and high ($1.1M/yr) fee revenue range. For the treasury model, use the midpoint ($825K/yr) as the base projection, prorated per period (monthly = /12, annual = /1). The fee tier, utilization, and price range inputs already exist in parameters.py; the revenue projection uses the pre-computed expected ranges rather than calculating LP fee mechanics from scratch (that would require AMM math that is overkill and verges on the deferred IL territory).

### Floor Defense Scenarios
The defense model has two phases:
1. **Accumulation**: 6M GNK/year converted to USDC at active GNK price, building toward $2-5M target
2. **Active defense**: Spending USDC from defense treasury at Tier 1/2/3 rates when price triggers activate

For the spreadsheet model, a simplified approach works: show the defense treasury accumulating from GNK conversion and depleting at a configurable monthly burn rate when "active." Since trigger-based activation is event-driven (not time-series), model a scenario where defense is active for a configurable number of months and show the impact on the treasury balance.

## Charts Recommendation

Following the 2-3 charts per model convention (style 13, width=20, height=12):

1. **Stacked Area: Treasury Composition Over Time** -- Community Pool (GNK value in USD) + POL position + defense treasury + AI Fund balance = total. Shows how the composition shifts over 10 years. (Addresses REQ-M4-06 visually)

2. **Line Chart: Community Pool Depletion + Defense Treasury** -- CP balance declining over time with defense treasury accumulating. Two-line chart showing the waterfall effect. (Addresses REQ-M4-01, REQ-M4-05)

3. **Bar Chart: Cumulative Buyback Burn** -- Running total of GNK burned with secondary axis showing % of total supply. (Addresses REQ-M4-03 visually)

Chart placement: Right of data table, starting at column P (or O if only 14 data columns). Positions at P1/P17/P33 (or O1/O17/O33).

## Conditional Formatting Recommendation

1. **Community Pool balance**: Red fill when CP Balance < 10M GNK (getting low). Green when > 50M GNK (healthy).
2. **Defense treasury**: Red when < $1M (below minimum target), green when > $3M (above midpoint target).
3. **Net treasury value**: ColorScaleRule from red (low) through yellow (medium) to green (high).

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Separate treasury columns across tabs | Single Treasury & POL tab consolidating all treasury components | Phase 6 design | Leadership sees unified treasury health |
| IL estimation in treasury model | IL explicitly deferred with caveat label | v1.0 Research / ROADMAP decision | Prevents wrong IL estimate misleading leadership |

**Deprecated/outdated:**
- V2 impermanent loss formula: Does not apply to V3 concentrated positions; deferred entirely rather than providing wrong estimate

## Cross-Tab Dependency Map

```
Emission Schedule (Phase 2)
  |-- Column A: Period labels (cross-ref for column A)
  |-- Column D: Mining emission GNK (needed for supply context)
  |-- Column H: Cumulative circulating supply (needed for burn % calculation)

Token Price (Phase 3)
  |-- Column F: Active Price (GNK price for USD conversion)
  |-- Column K: Buyback Burn GNK per period (cross-ref for buyback tracking)

Fee Transition (Phase 4)
  |-- Column D: Base Fee Revenue (context for AI Fund sizing)
  |-- Column L: AI Fund Share $ (inflow to AI Training Fund)
  |-- Column M: Buyback Share $ (dollar amount of buybacks)

Assumptions Tab
  |-- Community Pool: 120M GNK
  |-- POL GNK Allocation: 22M
  |-- Expected LP Fee Revenue Low/High: $550K/$1.1M
  |-- Total Supply: 1B (for burn % calculation)
  |-- Annual GNK Allocation for Defense: 6M
  |-- Defense Treasury Target Low/High: $2M/$5M
  |-- All other POL, buyback, and floor defense parameters
```

## Open Questions

1. **AI Fund expenses assumption**
   - What we know: REQ-M4-04 requires "inflows - expenses - surplus distribution = balance"
   - What's unclear: The v1.0 research mentions "6-month runway" for surplus calculation but doesn't specify the expense amount. The expense is operational (AI training costs) and not a token parameter.
   - Recommendation: Add an "AI Fund Monthly Expenses" parameter to parameters.py with a placeholder value (e.g., $50,000/month). This makes it adjustable by leadership. Alternatively, model expenses as a percentage of inflows (e.g., 60% spent, 40% accumulated).

2. **Floor defense active scenario modeling**
   - What we know: REQ-M4-05 asks for "treasury balance after X months of active defense at configurable trigger price levels"
   - What's unclear: Whether to show defense as a continuous time-series column (spending every period at a rate) or as a below-data scenario table (static analysis: "if defense active for 3/6/12 months at Tier 1/2/3, balance = X")
   - Recommendation: Use the main data column (L) to show defense treasury accumulation WITHOUT active spending (accumulation-only baseline). Place a defense scenario table in below-data rows showing depletion under different active-defense durations and tiers. This keeps the main data table clean while satisfying the scenario requirement.

3. **POL "position value" vs "GNK value"**
   - What we know: POL positions are LP tokens (GNK + USDC). IL is deferred.
   - What's unclear: How to value the POL position in the net treasury calculation without IL.
   - Recommendation: Value the POL GNK component at active price (as if no IL occurred) and note the USDC component as stable. This overestimates the position slightly but is explicitly labeled with the IL caveat. The net treasury formula becomes: CP_balance * price + POL_GNK * price + POL_USDC + cumulative_LP_fees + defense_USDC + AI_Fund_balance.

## Sources

### Primary (HIGH confidence)
- Codebase analysis: All 5 existing generator files (emission.py, token_price.py, fee_transition.py, host_profit.py, workbook_base.py) -- patterns verified by direct reading
- models/parameters.py -- all existing parameter values confirmed
- .planning/REQUIREMENTS.md -- REQ-M4-01 through REQ-M4-07, REQ-D06 requirements verified
- .planning/ROADMAP.md -- Phase 6 success criteria and dependencies confirmed
- .planning/STATE.md -- prior decisions on IL deferral, named ranges avoidance, revenue splits confirmed

### Secondary (MEDIUM confidence)
- .planning/research/ARCHITECTURE.md -- layer model (Treasury as Layer 1, though actual implementation needs Layer 2 cross-refs)
- .planning/research/FEATURES.md -- Model 4 feature expectations
- .planning/research/PITFALLS.md -- Pitfall 4 (V3 IL) confirms deferral decision; Pitfall 5 (hardcoded assumptions) confirms param_refs pattern

### Tertiary (LOW confidence)
- .planning/phases/01-deep-macro-tokenomics-research/research/01-pol-and-liquidity.md -- POL deployment parameters (used for context, not directly implemented)
- .planning/phases/01-deep-macro-tokenomics-research/research/02-real-yield-and-buybacks.md -- surplus distribution design (used for AI Fund modeling context)
- Gonka_Tokenomics_Fine_Tuning_Recommendations.md -- floor defense trigger architecture (simplified for spreadsheet model)

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- sole dependency is openpyxl 3.1.5, already proven in Phases 1-5
- Architecture: HIGH -- follows established patterns exactly (build_*_tab, param_refs, meta dict, 32-row structure, cross-tab references, below-data sections)
- Column layout: MEDIUM -- the exact column arrangement is a design choice; recommended layout may shift during planning based on formula complexity
- Pitfalls: HIGH -- all identified from direct codebase analysis and existing research documents
- New parameters: MEDIUM -- AI Fund expenses need a placeholder value; exact number is a leadership decision

**Research date:** 2026-02-06
**Valid until:** 2026-03-06 (stable domain; no external dependencies changing)

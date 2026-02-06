# Phase 3 Token Price Scenarios Model - Plan Check

**Phase Goal:** Leadership can compare 3-5 GNK price trajectories with market cap implications and see how buyback-burn affects net token supply across scenarios

**Status:** ISSUES FOUND
**Checked:** 2026-02-06
**Plans verified:** 2/2 (03-01, 03-02)

---

## Executive Summary

**Overall Assessment:** The plans are structurally sound and follow established Phase 2 patterns. However, there are **4 blockers** and **2 warnings** that must be addressed before execution.

**Critical Issues:**
1. Buyback-burn formula has monthly/annual period adjustment error (BLOCKER)
2. Missing number_format override for cross-ref columns (WARNING)
3. Missing column widths application in Plan 02 (WARNING)
4. Period alignment verification not specified (BLOCKER)

**Strengths:**
- Scenario selector pattern is well-designed and reusable
- Cross-sheet references correctly use quote_sheetname()
- Task structure is complete with files/action/verify/done
- Dependency graph is valid (Plan 02 depends on 01)

---

## Dimension 1: Requirement Coverage

### Status: PASSED

All 5 phase requirements have covering tasks:

| Requirement | Coverage | Plans | Tasks |
|-------------|----------|-------|-------|
| REQ-M1-01: 3-5 price trajectories | COVERED | 03-01 | Task 2 (columns B-E) |
| REQ-M1-02: Market cap calculations | COVERED | 03-01 | Task 2 (columns H-I) |
| REQ-M1-05: Buyback-burn net supply | COVERED | 03-01 | Task 2 (columns K-L) |
| REQ-M1-06: Dual-axis price/supply chart | COVERED | 03-02 | Task 1 (chart 2) |
| REQ-U03: Scenario selector | COVERED | 03-01 | Task 1 (DataValidation + MATCH/CHOOSE) |

**All 5 success criteria have task coverage:**
1. Price trajectory chart - 03-02 Task 1 (4 lines)
2. FDV and market cap calculations - 03-01 Task 2 (columns H-I)
3. Scenario selector dropdown - 03-01 Task 1 (Assumptions tab)
4. Net supply with conditional formatting - 03-01 Task 2 (column L) + 03-02 Task 1 (CellIsRule)
5. Dual-axis chart - 03-02 Task 1 (chart 2)

No missing requirements identified.

---

## Dimension 2: Task Completeness

### Status: PASSED

All tasks have required fields:

**Plan 03-01:**
- Task 1: Has files, action (2 steps A+B), verify, done ✓
- Task 2: Has files, action (complete column specs), verify, done ✓

**Plan 03-02:**
- Task 1: Has files, action (3 parts: charts + CF), verify, done ✓
- Task 2: Has files, action (4 steps in generate.py), verify, done ✓
- Task 3: Checkpoint (human-verify) - proper structure ✓

All actions are specific with formula patterns, column layouts, and function signatures. Verification commands are runnable Python snippets.

---

## Dimension 3: Dependency Correctness

### Status: PASSED

**Dependency graph:**
```
03-01 (Wave 1): depends_on: []
03-02 (Wave 2): depends_on: ["03-01"]
```

**Validation:**
- Plan 03-01 can execute independently (Wave 1) ✓
- Plan 03-02 correctly waits for 03-01 completion ✓
- No circular dependencies ✓
- No future references ✓
- Wave assignments consistent with dependencies ✓

**Cross-plan data flow:**
- 03-02 Task 1 uses `price_meta` from 03-01 Task 2 ✓
- 03-02 Task 2 imports `build_token_price_tab` from 03-01 output ✓

---

## Dimension 4: Key Links Planned

### Status: WARNING (1 issue)

**Key links from must_haves:**

| Link | From | To | Via | Planned? | Issue |
|------|------|----|----|----------|-------|
| 1 | workbook_base.py | param_refs | _add_scenario_selector adds keys | YES ✓ | None |
| 2 | token_price.py | Emission Schedule!H{row} | quote_sheetname + cross-ref | YES ✓ | See Issue #2 |
| 3 | token_price.py | param_refs | Active Price Low/High for formulas | YES ✓ | None |
| 4 | generate.py | token_price.py | import + call build_token_price_tab | YES ✓ | None |

**Issue #2: Cross-ref number_format override missing**

Plan 03-01 Task 2 specifies:
> "Column G (Circulating Supply): Cross-sheet reference. Apply crossref_cell style, then override number_format to "#,##0" (tokens format)."

However, the action text later states:
> "Style as crossref_cell."

Without the explicit override step, the tokens format may not apply correctly. The crossref_cell style uses green font but may not have the tokens number format.

**Recommendation:** Add explicit instruction in Task 2 action:
```python
circ_cell = ws.cell(row=row, column=7, value=f"={es_sheet}!{circ_col}{es_row}")
circ_cell.style = "crossref_cell"
circ_cell.number_format = "#,##0"  # Explicit override for tokens
```

Same applies to column J (Gross New Supply).

---

## Dimension 5: Scope Sanity

### Status: PASSED

**Plan 03-01:**
- Tasks: 2
- Files modified: 3 (parameters.py, workbook_base.py, token_price.py)
- Estimated context: ~30%

**Plan 03-02:**
- Tasks: 3 (2 auto + 1 checkpoint)
- Files modified: 2 (token_price.py, generate.py)
- Estimated context: ~20%

**Total phase context: ~50%** - within budget ✓

Both plans are well-scoped with 2-3 tasks each. The split between data model (Plan 01) and visualization (Plan 02) follows Phase 2 pattern.

---

## Dimension 6: Verification Derivation

### Status: PASSED

**must_haves analysis for Plan 03-01:**

**Truths (7 items):**
- ✓ "Scenario dropdown shows Conservative/Base/Aggressive" - user-observable
- ✓ "Changing dropdown updates Active Price Low/High" - testable interaction
- ✓ "4 price columns visible with linear interpolation" - verifiable in Excel
- ✓ "Active Price reflects selected scenario" - formula-driven, verifiable
- ✓ "FDV and Circ Market Cap calculated at 32 periods" - verifiable output
- ✓ "Circulating Supply uses green crossref_cell style" - visual verification
- ✓ "Net supply shows gross emission minus buyback burn" - formula verifiable

All truths are user-observable and testable. None are implementation-focused.

**Artifacts (3 items):**
- ✓ generators/token_price.py exports build_token_price_tab
- ✓ generators/workbook_base.py contains _add_scenario_selector
- ✓ models/parameters.py contains "Assumed Annual Fee Revenue"

All artifacts properly specify exports/contains for verification.

**Key links (3 items):**
- ✓ workbook_base → param_refs (adds scenario keys)
- ✓ token_price → Emission Schedule (cross-sheet refs)
- ✓ token_price → param_refs (price formulas)

All critical wiring is identified with pattern matching strings.

**must_haves analysis for Plan 03-02:**

**Truths (5 items):**
- ✓ "Chart showing all 4 price trajectories on single plot" - visual output
- ✓ "Dual-axis chart overlaying price + supply" - visual output
- ✓ "Net supply cells turn green when negative" - conditional formatting
- ✓ "python generate.py produces complete 3-tab workbook" - CLI verification
- ✓ "Generated workbook opens in Excel with charts rendering" - end-to-end test

All truths are user-observable. Good coverage of visual outputs.

**Artifacts (2 items):**
- ✓ token_price.py contains _create_price_scenarios_chart
- ✓ generate.py contains build_token_price_tab import

**Key links (2 items):**
- ✓ generate.py → token_price.py (import and call)
- ✓ token_price charts → price_meta cols (Reference objects)

---

## Critical Issues (Blockers)

### BLOCKER 1: Buyback-Burn Period Adjustment Formula Error

**Location:** Plan 03-01, Task 2, Column K formula

**Issue:**
The action specifies:
> "For monthly periods (i=0..23): divide annual fee by 12 -> `{fee_rev_ref}*{buyback_ref}/F{row}/12`"
> "For annual periods (i=24..31): use annual fee directly -> `{fee_rev_ref}*{buyback_ref}/F{row}`"

This creates two different formulas in the same column, requiring conditional logic. However, the implementation pattern shown earlier states:

```python
# K: Buyback burn tokens = (fee_revenue * buyback_pct) / price / periods_adjustment
```

**Problem:** The plan doesn't specify HOW to implement the conditional monthly vs annual adjustment. Options:

1. Use IF formula: `=IF(ROW()<=26, fee*buyback/price/12, fee*buyback/price)`
2. Use two separate loops in Python (rows 3-26 monthly, 27-34 annual)
3. Create a "period adjustment factor" column with 12 for monthly, 1 for annual

**Missing specification:** Which approach to use? The task action describes WHAT but not HOW to implement the conditional logic.

**Recommendation:** Add explicit instruction in Task 2:
```python
# Buyback burn: monthly adjustment for Y1-Y2, annual for Y3-Y10
for i in range(32):
    row = data_start_row + i
    periods_per_year = 12 if i < 24 else 1  # Monthly for first 24 rows, annual for rest
    ws.cell(row=row, column=11,
            value=f"={param_refs['Assumed Annual Fee Revenue']}*"
                  f"{param_refs['Buyback-Burn']}/F{row}/{periods_per_year}")
```

---

### BLOCKER 2: Period Alignment Verification Missing

**Location:** Plan 03-01, Task 2 verification

**Issue:**
The Token Price tab uses cross-sheet references to Emission Schedule columns G and H. The verification checks formulas exist but doesn't verify row alignment:

```python
# Check cross-sheet reference
g3 = ws.cell(row=3, column=7).value  # Circulating supply
assert "Emission Schedule" in g3, f"G3 should ref Emission Schedule: {g3}"
```

**Problem:** This only checks that row 3 references Emission Schedule. It doesn't verify:
1. Token Price row 3 maps to Emission Schedule row 3 (not row 4 or 5)
2. All 32 rows are correctly aligned
3. The `es_row` calculation matches row indices

**Risk:** If `emission_meta["data_start_row"]` is 3 and Token Price tab also starts at 3, but the loop index is off by 1, the entire dataset will be shifted.

**Missing verification:** No check that period labels match between tabs or that row indices align.

**Recommendation:** Add verification to Task 2:
```python
# Verify row alignment between tabs
es_ws = wb["Emission Schedule"]
tp_ws = wb["Token Price"]

for i in range(5):  # Check first 5 rows as sample
    es_row = emission_meta["data_start_row"] + i
    tp_row = price_meta["data_start_row"] + i
    
    es_label = es_ws.cell(row=es_row, column=1).value
    tp_label = tp_ws.cell(row=tp_row, column=1).value
    
    # If TP uses cross-ref for period labels, check they resolve to same values
    print(f"ES row {es_row}: {es_label}, TP row {tp_row}: {tp_label}")
```

---

### BLOCKER 3: Column Widths Not Applied in Plan 02

**Location:** Plan 03-02, Task 1

**Issue:**
Plan 03-01 Task 2 defines `_COL_WIDTHS` dict and the action implies it gets applied:
> "Column widths: [shows _COL_WIDTHS dict]"

However, the action in Task 2 doesn't show the loop to apply column widths:
```python
for col_letter, width in _COL_WIDTHS.items():
    ws.column_dimensions[col_letter].width = width
```

Plan 03-02 Task 1 adds charts and conditional formatting AFTER Task 2, implying column widths should already be set. But if Task 2 doesn't apply them, the columns will have default widths.

**Missing instruction:** Where in the code to apply column widths.

**Recommendation:** Add to Plan 03-01 Task 2 action (after the data row loop):
```python
# Apply column widths
for col_letter, width in _COL_WIDTHS.items():
    ws.column_dimensions[col_letter].width = width
```

---

### BLOCKER 4: Return Statement Placement Ambiguity

**Location:** Plan 03-01, Task 1, Step B

**Issue:**
The action states:
> "The function returns the updated `current_row` (for any future additions)."
> "At the end of the existing for-loop (after all PARAM_GROUPS are written, before column widths), call:"

But the current `build_assumptions_tab()` in workbook_base.py returns `param_refs`, not `current_row`. The scenario selector function returns `current_row`, but the calling function must then return `param_refs`.

**Missing specification:** After calling `_add_scenario_selector()`, does `build_assumptions_tab()` need to be modified to return both `param_refs` and `current_row`? Or just `param_refs` as before?

**Code ambiguity:**
```python
current_row = _add_scenario_selector(ws, current_row, param_refs)
# Then what? Is current_row used for anything?
# The function currently returns param_refs only
return param_refs
```

**Recommendation:** Clarify in Task 1 action:
```python
# At end of build_assumptions_tab(), before column width setting:
current_row = _add_scenario_selector(ws, current_row, param_refs)
# current_row is updated but not used further in Phase 3
# Future phases may add more sections using this current_row value

# Set column widths (existing code)
for col_letter, width in _COL_WIDTHS.items():
    ws.column_dimensions[col_letter].width = width

return param_refs  # No change to return signature
```

---

## Warnings (Should Fix)

### WARNING 1: Freeze Panes Not Specified

**Location:** Plan 03-01, Task 2

**Issue:**
The action states:
> "Row 2: Column headers (see below), header style"
> "Freeze panes at A3"

But no implementation code is shown for freeze panes. Phase 2 emission.py includes:
```python
ws.freeze_panes = "A3"
```

**Missing instruction:** Explicit placement of `ws.freeze_panes = "A3"` in the tab setup code.

**Recommendation:** Add after tab color and before header row:
```python
ws = wb.create_sheet(title="Token Price")
ws.sheet_properties.tabColor = TAB_COLOR_CALC
ws.freeze_panes = "A3"  # Explicit freeze
```

---

### WARNING 2: Import Organization Not Specified

**Location:** Plan 03-02, Task 1

**Issue:**
The action lists new imports needed:
```python
from openpyxl.chart import LineChart, Reference
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import PatternFill, Font
```

But doesn't specify whether to add these at the top of the file or organize them with existing imports. Phase 2 emission.py groups imports by source:
```python
from openpyxl.chart import LineChart, AreaChart, BarChart, Reference
from openpyxl.utils import get_column_letter
```

**Missing guidance:** Import organization pattern.

**Recommendation:** Add note in Task 1 action:
```python
# Add imports at top of token_price.py, grouped with existing openpyxl imports:
from openpyxl.chart import LineChart, Reference
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import PatternFill, Font
from openpyxl.utils import quote_sheetname  # Already exists from Task 2
```

---

## Formula Correctness Analysis

### Scenario Selector (MATCH + CHOOSE)

**MATCH formula:**
```excel
=MATCH(B{selector_row},{"Conservative","Base","Aggressive"},0)
```

**Analysis:**
- ✓ Curly braces are Excel array constant syntax (not Python format)
- ✓ Plan correctly uses f-string with doubled braces `{{` and `}}`
- ✓ MATCH returns 1-based index (1, 2, or 3)
- ✓ Compatible with Excel and Google Sheets

**CHOOSE formula:**
```excel
=CHOOSE($B${index_row},{param_refs["Conservative Price Low"]},{param_refs["Moderate Price Low"]},{param_refs["Aggressive Price Low"]})
```

**Analysis:**
- ✓ Absolute reference to index row ($B${index_row})
- ✓ CHOOSE takes 1-based index (matches MATCH output)
- ✓ All three scenario values from param_refs (no hardcoding)
- ✓ Formula structure is correct

### Price Interpolation

**Formula:**
```excel
={param_refs["Conservative Price Low"]}+({i}/31)*({param_refs["Conservative Price High"]}-{param_refs["Conservative Price Low"]})
```

**Analysis:**
- ✓ Linear interpolation formula is correct
- ✓ i/31 gives 0.0 at i=0, 1.0 at i=31 (32 data points)
- ✓ All parameter references use param_refs (no hardcoding)
- ⚠️ Division by 31 (not 32) is correct for interpolation endpoints

**Verification:** For i=0: price_low + 0 = price_low. For i=31: price_low + 1*(price_high - price_low) = price_high. ✓

### FDV and Market Cap

**FDV formula:**
```excel
={param_refs["Total Supply"]}*F{row}
```

**Analysis:**
- ✓ FDV = Total Supply × Active Price (correct definition)
- ✓ Uses absolute param_ref for Total Supply
- ✓ Uses relative row reference for Active Price (same row)

**Circ Market Cap formula:**
```excel
=G{row}*F{row}
```

**Analysis:**
- ✓ Circ Market Cap = Circulating Supply × Active Price (correct)
- ✓ Both references are same-row relative references
- ✓ Column G is cross-sheet reference (already resolved)

### Buyback-Burn

**Formula (as specified):**
```excel
={param_refs["Assumed Annual Fee Revenue"]}*{param_refs["Buyback-Burn"]}/F{row}/{periods_per_year}
```

**Analysis:**
- ✓ Fee revenue × 5% = buyback budget (correct)
- ✓ Divide by price to get GNK tokens (correct)
- ⚠️ periods_per_year conditional (12 vs 1) - see BLOCKER 1
- ⚠️ Assumes fee revenue is annual (needs to match period granularity)

**Concern:** If "Assumed Annual Fee Revenue" is $1M/year, then for monthly periods, we need $1M/12 per month. The formula divides by 12, which is correct. For annual periods (Y3-Y10), we use the full $1M annual fee, which is correct.

**Formula is conceptually correct** IF the periods_per_year conditional is implemented.

### Net Supply Change

**Formula:**
```excel
=J{row}-K{row}
```

**Analysis:**
- ✓ Net = Gross New Supply - Buyback Burn (correct)
- ✓ Negative value = deflationary (supply decreasing)
- ✓ Positive value = inflationary (supply increasing)
- ✓ Simple row-relative reference

### Cross-Sheet References

**Formula:**
```excel
='{es_sheet}'!{circ_col}{es_row}
```

**Analysis:**
- ✓ Uses quote_sheetname() to wrap "Emission Schedule" in single quotes
- ✓ Column letter from emission_meta["cols"]["cumulative_circulating"]
- ✓ Row index from emission_meta["data_start_row"] + i
- ⚠️ Assumes emission_meta row alignment matches price tab row alignment (see BLOCKER 2)

**Potential circular reference risk:** NONE. Token Price reads from Emission Schedule (one-way dependency). Emission Schedule doesn't reference Token Price. ✓

---

## Chart Specifications Review

### Chart 1: Price Scenarios Comparison

**Specification:**
- 4 data series (columns B-E)
- LineChart with style 13
- Width 20, Height 12
- Placement: N1

**Analysis:**
- ✓ All 4 price columns are always calculated (not dependent on dropdown)
- ✓ Chart shows all scenarios simultaneously for comparison
- ✓ Uses Reference with titles_from_data=True (header row provides series names)
- ✓ Categories from column A (period labels)
- ✓ Line width 25000 EMUs matches Phase 2 pattern

**Missing specification:** X-axis categories range. The action shows:
> "Categories: Column A (period labels), rows data_start_row to data_end_row"

But doesn't show the Reference() call. Should be:
```python
cats = Reference(ws, min_col=1, min_row=data_start_row, max_row=data_end_row)
c.set_categories(cats)
```

**Recommendation:** Add explicit categories code in Task 1 action.

### Chart 2: Price vs Supply Dual-Axis

**Specification:**
- Primary: Active Price (column F) on left Y-axis
- Secondary: Circulating Supply (column G) on right Y-axis
- LineChart for both, combined with c1 += c2
- c2.y_axis.axId = 200
- c1.y_axis.crosses = "max"
- Placement: N17

**Analysis:**
- ✓ axId = 200 is openpyxl convention for secondary axis
- ✓ crosses = "max" pushes secondary axis to right side
- ✓ Both charts use LineChart (not mixed types)
- ✓ Placement N17 leaves room for first chart (height 12)

**Openpyxl compatibility:** Verified in 03-RESEARCH.md. Pattern is correct. ✓

---

## Conditional Formatting

**Specification:**
```python
cell_range = f"L{meta['data_start_row']}:L{meta['data_end_row']}"
ws.conditional_formatting.add(
    cell_range,
    CellIsRule(
        operator="lessThan",
        formula=["0"],
        fill=green_fill,
        font=green_font,
    ),
)
```

**Analysis:**
- ✓ CellIsRule with operator="lessThan" checks if cell < 0
- ✓ Green fill/font for negative values (deflationary = positive signal)
- ✓ Applies to entire Net Supply Change column (L)
- ✓ Uses data_start_row and data_end_row from price_meta

**Color choice rationale:** Green for deflationary is correct (supply reduction is a feature, not a bug). ✓

---

## Anti-Pattern Check

### Hardcoded Values

**Status:** PASS ✓

All formulas reference param_refs:
- ✓ Price scenario bounds: param_refs["Conservative Price Low"], etc.
- ✓ Total Supply: param_refs["Total Supply"]
- ✓ Buyback percentage: param_refs["Buyback-Burn"]
- ✓ Fee revenue: param_refs["Assumed Annual Fee Revenue"]
- ✓ Bitfury price: param_refs["Bitfury Schelling Point"]

No magic numbers found in formulas.

### showDropDown Parameter

**Status:** PASS ✓

Plan 03-01 Task 1 action explicitly states:
> "Do NOT set showDropDown (leave default False to show arrow)"

03-RESEARCH.md documents this pitfall. Correctly avoided.

### Named Ranges

**Status:** PASS ✓

All references use absolute cell addresses via param_refs. No named ranges used. Consistent with project convention.

### Cross-Sheet References

**Status:** PASS ✓

Plan 03-01 Task 2 uses `quote_sheetname()` for all cross-sheet references:
```python
es_sheet = quote_sheetname(emission_meta["sheet_name"])
```

Correctly handles sheet names with spaces.

### Data Duplication

**Status:** PASS ✓

Column A (Period Label) uses cross-sheet reference:
```excel
='Emission Schedule'!A{es_row}
```

No data duplication. Period labels stay in sync automatically.

---

## Phase Goal Achievement Analysis

**Goal:** Leadership can compare 3-5 GNK price trajectories with market cap implications and see how buyback-burn affects net token supply across scenarios

### Will the plans achieve this?

**Price trajectory comparison (3-5 scenarios):**
- ✓ Plan 03-01 creates 4 price columns (Conservative, Moderate, Aggressive, Bitfury)
- ✓ Plan 03-02 creates chart showing all 4 trajectories on single plot
- ✓ Scenario selector allows switching active scenario

**Market cap implications:**
- ✓ FDV calculated at each time point (column H)
- ✓ Circulating market cap calculated at each time point (column I)
- ✓ Both update automatically when scenario changes

**Buyback-burn net supply:**
- ✓ Buyback burn tokens calculated per period (column K)
- ✓ Net supply change = gross - buyback (column L)
- ✓ Conditional formatting flags deflationary periods
- ⚠️ Buyback formula has implementation ambiguity (BLOCKER 1)

**Across scenarios:**
- ✓ Scenario selector switches between Conservative/Base/Aggressive
- ✓ All calculation columns (F-L) update based on active scenario
- ✓ Static price columns (B-E) always visible for comparison

**Verdict:** YES, the plans will achieve the phase goal IF the 4 blockers are resolved.

---

## Context Budget Impact

**Plan 03-01 estimated token usage:**
- Read 3 files (parameters.py, workbook_base.py, existing emission.py)
- Write 1 new file (token_price.py ~400 lines)
- Modify 2 files (parameters.py +10 lines, workbook_base.py +60 lines)
- Test generation + verification
- **Estimated: 30-35% of 200K budget**

**Plan 03-02 estimated token usage:**
- Read token_price.py, generate.py, emission.py (for pattern reference)
- Modify token_price.py (+100 lines for charts + CF)
- Modify generate.py (+10 lines)
- Test full generation + chart rendering
- **Estimated: 20-25% of 200K budget**

**Total phase: ~50-60%** - WITHIN BUDGET ✓

---

## Structured Issues

```yaml
issues:
  - plan: "03-01"
    task: 2
    dimension: "task_completeness"
    severity: "blocker"
    description: "Buyback-burn formula specifies monthly vs annual adjustment but doesn't show HOW to implement the conditional logic (IF formula vs Python conditional vs adjustment factor column)"
    fix_hint: "Add explicit Python code showing periods_per_year = 12 if i < 24 else 1 in the loop"

  - plan: "03-01"
    task: 2
    dimension: "task_completeness"
    severity: "blocker"
    description: "Period alignment verification missing - no check that Token Price row 3 maps to Emission Schedule row 3"
    fix_hint: "Add verification comparing period labels between tabs or es_row calculation check"

  - plan: "03-01"
    task: 2
    dimension: "task_completeness"
    severity: "blocker"
    description: "Column widths defined but application code not shown in action"
    fix_hint: "Add loop: for col_letter, width in _COL_WIDTHS.items(): ws.column_dimensions[col_letter].width = width"

  - plan: "03-01"
    task: 1
    dimension: "task_completeness"
    severity: "blocker"
    description: "_add_scenario_selector returns current_row but build_assumptions_tab return signature unclear"
    fix_hint: "Clarify that build_assumptions_tab still returns only param_refs (current_row not used further in Phase 3)"

  - plan: "03-01"
    task: 2
    dimension: "key_links_planned"
    severity: "warning"
    description: "Cross-ref columns (G, J) specify crossref_cell style but number_format override step not explicit"
    fix_hint: "Add circ_cell.number_format = '#,##0' after circ_cell.style = 'crossref_cell'"

  - plan: "03-01"
    task: 2
    dimension: "task_completeness"
    severity: "warning"
    description: "Freeze panes at A3 mentioned but no implementation code shown"
    fix_hint: "Add ws.freeze_panes = 'A3' after tab color setting"

  - plan: "03-02"
    task: 1
    dimension: "task_completeness"
    severity: "warning"
    description: "New imports listed but organization pattern not specified"
    fix_hint: "Group openpyxl imports together at top of file per Phase 2 pattern"

  - plan: "03-02"
    task: 1
    dimension: "task_completeness"
    severity: "warning"
    description: "Categories Reference for Chart 1 described but code not shown"
    fix_hint: "Add explicit cats = Reference(...) and c.set_categories(cats) in action"
```

---

## Recommendations

### Before Execution

**Must fix (blockers):**
1. Add explicit buyback-burn period adjustment implementation (Python conditional)
2. Add row alignment verification between Emission Schedule and Token Price tabs
3. Add column widths application code to Task 2 action
4. Clarify build_assumptions_tab return signature handling

**Should fix (warnings):**
1. Add explicit number_format override for cross-ref columns
2. Add ws.freeze_panes = "A3" to tab setup code
3. Specify import organization pattern
4. Add explicit categories Reference code for Chart 1

### After Execution

1. Verify workbook opens in both Excel and Google Sheets
2. Test scenario selector dropdown with all 3 scenarios
3. Verify cross-sheet references update when Emission Schedule changes
4. Verify conditional formatting triggers on negative net supply values
5. Check chart rendering after fix_chart_rendering() application

---

## Approval Status

**Status:** ISSUES FOUND - 4 blockers, 3 warnings

**Recommendation:** Return to planner with structured issues above. All issues are implementation clarifications (not architectural flaws). Plans are structurally sound.

**Next steps:**
1. Planner revises Plan 03-01 Task 1 and Task 2 with clarifications
2. Planner revises Plan 03-02 Task 1 with code details
3. Re-run plan checker to verify blockers resolved
4. Proceed to execution

---

## Metadata

**Checker:** gsd-plan-checker
**Method:** Goal-backward verification (Phase 3 goal -> success criteria -> requirements -> tasks)
**Confidence:** HIGH - All 6 dimensions checked, formulas validated, patterns verified against Phase 2
**Phase dependency:** Phase 2 (Emission Schedule) must be complete before Phase 3 execution

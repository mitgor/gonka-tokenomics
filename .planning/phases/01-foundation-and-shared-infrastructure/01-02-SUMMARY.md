---
phase: 01-foundation-and-shared-infrastructure
plan: 02
subsystem: infra
tags: [openpyxl, workbook, assumptions-tab, param-refs, cli, generate, xlsx]

# Dependency graph
requires:
  - "01-01: PARAM_GROUPS OrderedDict (60 params, 12 groups) and register_styles/FORMAT_TO_STYLE"
provides:
  - "build_assumptions_tab(wb) function returning param_refs dict (60 entries)"
  - "create_workbook() convenience function returning (wb, param_refs) tuple"
  - "param_refs dict mapping every parameter name to Assumptions!$B$N absolute cell reference"
  - "generate.py CLI entry point with --test flag support"
  - "requirements.txt with sole dependency openpyxl==3.1.5"
  - "Project scaffolding: .gitignore, output/.gitkeep"
affects:
  - "Phase 2+ (every model module imports create_workbook and consumes param_refs)"
  - "Phase 7 (master workbook assembly calls create_workbook then adds tabs)"
  - "Phase 8 (standalone workbooks follow same create_workbook pattern)"

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "param_refs dict as interface contract between Assumptions tab and all model modules"
    - "Lazy imports in generate.py (import at call site, not module level)"
    - "create_workbook() as single entry point for all workbook generation"
    - "FORMAT_TO_STYLE -> named_style.number_format lookup for per-cell format application"

key-files:
  created:
    - generators/workbook_base.py
    - generate.py
    - requirements.txt
    - .gitignore
    - output/.gitkeep
  modified: []

key-decisions:
  - "Merge section headers across A:D (not A:E) matching the 4-column data layout"
  - "Apply input_cell style first, then override number_format from FORMAT_TO_STYLE lookup"
  - "Protection(locked=False) applied to every input cell now, sheet protection deferred to Phase 9"
  - "Source citations in italic font for visual distinction from parameter names"

patterns-established:
  - "param_refs consumption: model modules receive dict and write formulas like =Assumptions!$B$12*EXP(-Assumptions!$B$13*B3)"
  - "Workbook creation flow: create_workbook() -> add model tabs -> wb.save()"
  - "CLI pattern: generate.py with --test for quick verification, default for full model"

# Metrics
duration: 5min
completed: 2026-02-05
---

# Phase 1 Plan 02: Workbook Base, CLI Entry Point, and Project Scaffolding Summary

**build_assumptions_tab() writes 60 parameters across 12 groups to a formatted Assumptions sheet and returns the 60-entry param_refs dict; generate.py CLI produces an 8KB .xlsx with blue-shaded input cells and consistent number formatting**

## Performance

- **Duration:** 5 min
- **Started:** 2026-02-05T22:48:10Z
- **Completed:** 2026-02-05T22:52:46Z
- **Tasks:** 3 (2 auto + 1 human-verify checkpoint)
- **Files created:** 5

## Accomplishments
- build_assumptions_tab(wb) writes all 60 v1.0 research parameters to a formatted Assumptions sheet (86 rows, 12 section groups) and returns the param_refs dict
- param_refs dict maps every parameter name to its Assumptions!$B$N absolute cell reference (60 entries verified)
- Blue-shaded input cells with Protection(locked=False) are visually distinct; number formatting consistent across all types (USD=$#,##0, percent=0.0%, tokens=#,##0, decay=0.000000, price_per_hour=$#,##0.00)
- generate.py CLI produces output/gonka_master_model.xlsx (8KB) with --test flag for quick verification
- Project scaffolding complete: requirements.txt (single dependency), .gitignore (output/, __pycache__/, venv/, IDE), output/.gitkeep

## Task Commits

Each task was committed atomically:

1. **Task 1: Create workbook_base.py with Assumptions tab builder and param_refs** - `50518d8` (feat)
2. **Task 2: Create generate.py CLI entry point and project scaffolding** - `185f2ed` (feat)
3. **Task 3: Visual verification of generated workbook** - Checkpoint approved by user

## Files Created/Modified
- `generators/workbook_base.py` - build_assumptions_tab(wb) and create_workbook() functions; writes all PARAM_GROUPS to Assumptions sheet, applies styles and number formats, returns param_refs dict
- `generate.py` - CLI entry point with --test and default modes; lazy imports, output directory creation
- `requirements.txt` - Single dependency: openpyxl==3.1.5
- `.gitignore` - Ignores output/, __pycache__/, venv/, IDE files, OS files
- `output/.gitkeep` - Tracks empty output directory in git (contents gitignored)

## Decisions Made
- Section header merges span A:D (4 columns) matching the data layout, not A:E as mentioned in some plan text for the title row -- title row merges A:E for visual emphasis
- Applied input_cell named style first to get blue fill and dark blue font, then overrode number_format by looking up the format from the registered named style via wb._named_styles -- this avoids duplicating format strings
- Freeze panes set at A4 so the title, instruction, and blank separator rows stay visible during scrolling
- Source citations use italic Calibri 11pt to visually distinguish from parameter names without breaking the single-font convention

## Deviations from Plan
None - plan executed exactly as written.

## Issues Encountered
- output/.gitkeep required `git add -f` since .gitignore ignores the output/ directory -- resolved by force-adding the .gitkeep file

## User Setup Required
None - no external service configuration required.

## Verification Results

**Programmatic verification (all passed):**
- param_refs has 60 entries (all parameters accounted for)
- Total Supply = 1,000,000,000 at B5 with #,##0 format
- Decay Rate = 0.000475 at B12 with 0.000000 format
- Host Share = 0.7 at B17 with 0.0% format
- H100 Current Price = 2.50 at B38 with $#,##0.00 format
- Input cells have Protection(locked=False)
- Tab color = 004472C4 (blue)
- Freeze panes = A4
- No constants outside parameters.py (grep verified)
- `python generate.py` produces 8KB .xlsx without error

**Visual verification (user approved):**
- Blue-shaded input cells visually distinct in Excel
- Section headers with dark blue bold text
- Number formatting consistent across all parameter types

## Next Phase Readiness
- Phase 1 Foundation is COMPLETE: parameters.py + styles.py + workbook_base.py + generate.py form a working end-to-end pipeline
- The param_refs pattern is proven and ready for Phase 2 (Emission Schedule Model) to consume
- Phase 2 will import create_workbook(), get param_refs, and add an Emission tab using formulas like `=Assumptions!$B$12*EXP(-Assumptions!$B$13*A{row})`
- generate.py is extensible: Phase 2+ will add model tab builders between create_workbook() and wb.save()

---
*Phase: 01-foundation-and-shared-infrastructure*
*Completed: 2026-02-05*

# Phase 9 Plan 02: Print Setup & Cell Protection Summary

**One-liner:** Centralized print_setup.py with per-tab print areas, orientation, fit-to-page, footers, and sheet protection across all 5 workbooks (33 tabs total)

---
phase: "09"
plan: "02"
subsystem: "print-protection"
tags: ["openpyxl", "print-setup", "sheet-protection", "page-layout"]
dependency-graph:
  requires: ["01-02"]
  provides: ["REQ-U09 cell protection", "REQ-U12 print-friendly layout"]
  affects: ["09-03"]
tech-stack:
  added: []
  patterns: ["dict-based dispatch for tab configs", "centralized utility module"]
key-files:
  created: ["generators/print_setup.py"]
  modified: ["generate.py", "generators/standalone.py"]
decisions:
  - id: "09-02-01"
    description: "Dict-based dispatch for print configs (not if/elif)"
  - id: "09-02-02"
    description: "Dynamic max_row detection for Documentation, Assumptions, Definitions tabs"
  - id: "09-02-03"
    description: "Protection password 'gonka' with cell selection allowed for copy/view"
  - id: "09-02-04"
    description: "Print order: apply_all_print_settings() then apply_sheet_protection() then wb.save()"
metrics:
  duration: "3.8 min"
  completed: "2026-02-07"
---

## Tasks Completed

| Task | Name | Commit | Key Files |
|------|------|--------|-----------|
| 1 | Create print_setup.py with protection and print utilities | 1630c10 | generators/print_setup.py |
| 2 | Integrate protection and print setup into generate.py and standalone.py | a948235* | generate.py, generators/standalone.py |

*Task 2 changes were committed alongside concurrent 09-01 agent changes due to Wave 1 parallel execution (both agents editing the same files on disk).

## What Was Built

### generators/print_setup.py (new)

Two public functions:

1. **`apply_sheet_protection(wb, password='gonka')`** -- Enables sheet-level protection on ALL worksheets. Allows cell selection (for copy/view) and formatting operations. Input cells with `Protection(locked=False)` from Phase 1 remain editable.

2. **`apply_all_print_settings(wb)`** -- Applies per-tab print configuration using a dict-based dispatch pattern:

| Tab | Print Area | Orientation | Title Rows | Fit Height |
|-----|-----------|-------------|------------|------------|
| Documentation | A1:F{max_row} | portrait | None | 1 (single page) |
| Assumptions | A1:E{max_row} | portrait | 1:3 | 0 |
| Emission Schedule | A1:J38 | landscape | 1:2 | 0 |
| Token Price | A1:L34 | landscape | 1:2 | 0 |
| Fee Transition | A1:N47 | landscape | 1:2 | 0 |
| Host Profitability | A1:M55 | landscape | 1:2 | 0 |
| Treasury & POL | A1:N49 | landscape | 1:2 | 0 |
| Dashboard | A1:E22 | portrait | None | 1 (single page) |
| Definitions | A1:B{max_row} | portrait | None | 0 |
| Fallback (unknown) | Auto-detect | landscape | None | 0 |

Common settings on all tabs: Letter paper, fit-to-width=1, margins (0.5/0.5/0.75/0.75), header with sheet name, footer with page number and "Gonka Tokenomics v1.1".

### Integration Points

- **generate.py** `generate_test()` -- print + protection before save
- **generate.py** `generate_all()` -- print + protection after `_add_back_to_doc_links(wb)` before `wb.save()`
- **generators/standalone.py** `generate_standalone()` -- print + protection as steps 8-9 before save (step 10)

Critical ordering preserved: print settings -> protection -> save -> fix_chart_rendering.

## Decisions Made

| ID | Decision | Rationale |
|----|----------|-----------|
| 09-02-01 | Dict-based dispatch for print configs | Extensible, no if/elif chains, easy to add tabs |
| 09-02-02 | Dynamic max_row for 3 tabs | Documentation, Assumptions, Definitions have variable row counts |
| 09-02-03 | Password 'gonka' with cell selection allowed | Users need to select/copy cells for analysis |
| 09-02-04 | Print then protect then save | Print settings write to worksheet properties; protection must lock everything last |

## Deviations from Plan

None -- plan executed exactly as written. The only notable artifact is that Task 2 file changes were committed alongside 09-01 due to Wave 1 concurrent execution.

## Verification Results

- `python generate.py --test` -- passes, test workbook has protection + print settings
- `python generate.py` -- all 5 workbooks (1 master + 4 standalone) generated successfully
- All 33 tabs across 5 workbooks verified: protection=True, print_area=set, orientation=correct, footer="Gonka Tokenomics v1.1"
- Input cells (Assumptions column B) confirmed `locked=False` under sheet protection

## Success Criteria

- [x] Every worksheet in the master workbook has print_area set covering its data columns
- [x] Every worksheet in all 4 standalone workbooks has print_area set
- [x] All formula cells are locked (sheet protection enabled on all tabs)
- [x] All input cells (blue-shaded column B on Assumptions) remain editable when sheet is protected
- [x] Model data tabs print in landscape orientation fitted to page width
- [x] Every worksheet has a footer with page number and "Gonka Tokenomics v1.1"

## Next Phase Readiness

No blockers. print_setup.py is a standalone utility module with no dependencies beyond openpyxl. Integration into generate.py and standalone.py is clean and non-invasive.

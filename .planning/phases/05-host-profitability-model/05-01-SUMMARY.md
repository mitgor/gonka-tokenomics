---
phase: 05-host-profitability-model
plan: 01
subsystem: host-profitability
tags: [host-economics, breakeven, sensitivity-analysis, cross-sheet, gpu-amortization]

dependency_graph:
  requires:
    - 01-foundation (parameters.py, styles, workbook_base)
    - 02-emission-schedule (emission_meta, mining emission data)
    - 03-token-price (price_meta, active price data)
    - 04-fee-transition (fee_meta, host share data)
  provides:
    - Host Profitability tab with 13 columns x 32 rows
    - host_meta dict for downstream chart/formatting in 05-02
    - HOST ROI sensitivity matrix (6x5)
    - Electricity cost sensitivity (3 tiers)
    - GPU hardware amortization (months-to-breakeven, ROI)
  affects:
    - 05-02 (charts and conditional formatting)
    - Phase 6+ (any tab needing host profitability data)

tech_stack:
  added: []
  patterns:
    - Triple cross-tab dependency (Emission Schedule + Token Price + Fee Transition)
    - Below-data analysis sections (sensitivity matrix, electricity, amortization)
    - IFERROR protection on breakeven division
    - Days factor switching (30 monthly, 365 annual)

key_files:
  created:
    - generators/host_profit.py
  modified:
    - models/parameters.py
    - generate.py

decisions:
  - id: hp-01
    decision: "Lambda Labs rate ($2.49/hr) as primary traditional benchmark over CoreWeave ($2.06/hr)"
    reason: "Lambda on-demand pricing most comparable to Gonka's flexible hosting model"
  - id: hp-02
    decision: "Breakeven formula uses MAX(0, (traditional - fee_income) / mining_GNK) with IFERROR(,99999)"
    reason: "Returns 0 when fees alone exceed rental (already profitable), 99999 for division by near-zero mining"
  - id: hp-03
    decision: "Sensitivity matrix uses static fee revenue (not scaled with network size)"
    reason: "Avoids circular assumption; annotation notes larger networks may generate more fees"
  - id: hp-04
    decision: "Churn risk flag uses gross Gonka income (E) vs traditional rental (H), not net income"
    reason: "Traditional rental prices already include provider electricity costs"

metrics:
  duration: "3 min"
  completed: "2026-02-06"
  tasks_completed: 2
  tasks_total: 2
---

# Phase 5 Plan 01: Parameters, Host Profitability Data Model, and Sensitivity Sections Summary

**One-liner:** 13-column host profitability model with triple cross-tab dependencies (Emission Schedule + Token Price + Fee Transition), breakeven price calculation, 6x5 sensitivity matrix, electricity/amortization analysis sections

## What Was Built

### Task 1: 3 New HOST ECONOMICS Parameters
Added to `models/parameters.py` after Host Collateral Rate:
- **Traditional Rental Rate (Lambda)** = $2.49/hr (Lambda Labs Q1 2026, on-demand)
- **Traditional Rental Rate (CoreWeave)** = $2.06/hr (CoreWeave 3yr reserved Q1 2026)
- **GPU Power Draw** = 400W (H100 inference average)

HOST ECONOMICS group now has 11 parameters (was 8). Total parameter count: 70.

### Task 2: Host Profitability Data Model + Pipeline Wiring
Created `generators/host_profit.py` with `build_host_profit_tab()` returning `host_meta`.

**Primary data table (13 columns x 32 rows):**

| Column | Content | Formula Pattern |
|--------|---------|-----------------|
| A | Period Label | Cross-ref from Emission Schedule |
| B | Mining GNK/Host | Emission!D / Current Hosts |
| C | Mining Income/Host ($) | B * Active Price |
| D | Fee Income/Host ($) | Fee Transition!K / Current Hosts |
| E | Total Gonka Income ($) | C + D |
| F | Electricity Cost ($) | Rate * Power * 24 * days / 1000 * GPUs/host |
| G | Net Income ($) | E - F |
| H | Traditional Rental ($) | Lambda * 24 * days * GPUs/host |
| I | Gonka vs Traditional ($) | E - H |
| J | Breakeven GNK Price ($) | IFERROR(MAX(0,(H-D)/B), 99999) |
| K | Breakeven Ref Low ($) | Static 0.85 |
| L | Breakeven Ref High ($) | Static 3.30 |
| M | Churn Risk | IF(E<H, 1, 0) |

**Below-data sections:**
1. **HOST ROI SENSITIVITY** (rows 37-43): 6 GNK prices ($0.50-$10) x 5 GPU counts (1K-50K) at Year 10
2. **ELECTRICITY COST SENSITIVITY** (rows 47-50): $0.05/$0.08/$0.12 per kWh with monthly cost and net profit
3. **GPU HARDWARE AMORTIZATION** (rows 53-55): $25K/$40K hardware with months-to-breakeven and 3/5yr ROI

**Pipeline wiring:** `build_host_profit_tab(wb, param_refs, emission_meta, price_meta, fee_meta)` called in `generate.py` after Fee Transition, receiving all 5 arguments.

## Decisions Made

1. **Lambda as primary benchmark** (hp-01): Lambda Labs on-demand rate ($2.49/hr) used for column H traditional rental comparison. CoreWeave ($2.06/hr) available as parameter but not used in primary comparison since its 3-year reserved pricing is less comparable to Gonka's flexible model.

2. **Breakeven formula design** (hp-02): `IFERROR(MAX(0, (H-D)/B), 99999)` -- when fee income alone exceeds traditional rental, breakeven is 0 (already profitable from fees). IFERROR handles late-period near-zero mining division.

3. **Static fee in sensitivity matrix** (hp-03): Fee revenue in the 6x5 sensitivity matrix does not scale with network GPU count. Annotation notes "Larger networks may generate proportionally more fees." This avoids the circular assumption that more GPUs = proportionally more fee revenue.

4. **Gross income for churn comparison** (hp-04): Column I (Gonka vs Traditional) compares gross Gonka income (E) to traditional rental (H), not net income (G). Traditional cloud rental prices already bundle provider electricity costs, making gross-to-gross the appropriate comparison.

## Deviations from Plan

None -- plan executed exactly as written.

## Commit Log

| Task | Commit | Description |
|------|--------|-------------|
| 1 | 356df98 | feat(05-01): add 3 HOST ECONOMICS parameters for host profitability |
| 2 | 36c73c8 | feat(05-01): create Host Profitability data model with triple cross-tab dependencies |

## Next Phase Readiness

**Phase 5 Plan 02 (Charts + Conditional Formatting):**
- `host_meta` dict provides all coordinates needed for chart series references
- Sensitivity matrix at rows 37-43 ready for ColorScaleRule heat map
- Churn Risk column M ready for CellIsRule conditional formatting
- Breakeven vs reference columns J/K/L ready for line chart overlay
- Income composition columns C/D ready for stacked area chart

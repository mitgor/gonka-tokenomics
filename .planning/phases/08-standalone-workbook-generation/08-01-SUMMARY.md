# Phase 8 Plan 1: Standalone Foundation Infrastructure Summary

**One-liner:** Toggle parameters, filtered assumptions builder, and standalone config data providing the complete foundation for 4 standalone workbooks.

## What Was Done

### Task 1: Add toggle parameters and create standalone_config.py
- Added WHAT-IF TOGGLES group to PARAM_GROUPS with 2 new parameters (Buyback-Burn Active, Deploy POL Active) with default "Y" values
- Created generators/standalone_config.py with all standalone configuration data:
  - 5 parameter name sets (EMISSION_PARAMS, TOKEN_PRICE_PARAMS, FEE_TRANSITION_PARAMS, HOST_PROFITABILITY_PARAMS, TREASURY_POL_PARAMS) built compositionally via frozenset unions
  - 20 glossary terms covering all tokenomics domain concepts
  - 4 scenario narrative dicts (3 scenarios each: Conservative, Base, Aggressive)
  - VERSION_INFO with v1.0 and v1.1 changelog entries
  - STANDALONE_CONFIGS master dict mapping 4 standalone names to full config (title, filename, params, narratives, builders, toggles, include_tail_toggle)

### Task 2: Build filtered assumptions tab function
- Added build_filtered_assumptions_tab(wb, param_names, include_scenario_selector, include_tail_toggle, include_toggles) to workbook_base.py
- Added _add_what_if_toggle() helper for Y/N DataValidation on toggle parameter cells
- Filtered builder writes only parameters in param_names with correctly remapped row numbers
- Scenario selector auto-skipped with warning if required price scenario params are missing
- Existing build_assumptions_tab() and create_workbook() completely unchanged

## Commits

| Task | Commit | Description |
|------|--------|-------------|
| 1 | 52d7dad | feat(08-01): add toggle parameters and standalone configuration |
| 2 | eb3bf4c | feat(08-01): add build_filtered_assumptions_tab function |

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Toggle params placed before veGNK PARAMETERS group | Near other model controls for logical grouping | Toggle cells appear near top of Assumptions tab |
| frozenset for parameter name sets | Immutability prevents accidental modification | Config data is pure and reliable |
| Y/N for what-if toggles (not ON/OFF) | Distinct from existing Tail Emission Toggle (ON/OFF); research recommendation | Consistent convention for new toggles |
| Scenario selector auto-skip with warning | Graceful degradation if param set missing price params | Won't crash, just logs |
| 20 glossary terms (universal, not filtered) | All standalones get full glossary; extra terms don't harm | Single source of truth |

## Verification Results

- parameters.py: 70 params (68 original + 2 new toggles)
- standalone_config.py: 4 configs, 20 glossary terms, version v1.1
- All param name strings match PARAM_GROUPS entries exactly (verified programmatically)
- Token Price filtered refs: 19 entries (15 params + 4 scenario selector)
- Fee Transition filtered refs: 29 entries
- Host Profitability filtered refs: 38 entries
- Treasury & POL filtered refs: 37 entries (includes Deploy POL Active)
- Master workbook generation: unchanged (74 parameters, all tabs)
- Deploy POL Active confirmed in TREASURY_POL_PARAMS
- All 6 price scenario params confirmed in TOKEN_PRICE_PARAMS

## Deviations from Plan

None -- plan executed exactly as written.

## Key Files

### Created
- generators/standalone_config.py - Parameter sets, glossary, narratives, version info, STANDALONE_CONFIGS

### Modified
- models/parameters.py - Added WHAT-IF TOGGLES group with 2 toggle parameters
- generators/workbook_base.py - Added build_filtered_assumptions_tab() and _add_what_if_toggle()

## Duration

~3 min

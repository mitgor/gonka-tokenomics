# Phase 8: Standalone Workbook Generation - Research

**Researched:** 2026-02-06
**Domain:** openpyxl Excel generation, parameter filtering, multi-workbook architecture
**Confidence:** HIGH

## Summary

Phase 8 requires generating 4 standalone workbooks alongside the master workbook, each containing only the model tabs and parameters relevant to a specific domain. The central challenge is the **param_refs remapping problem**: all existing model builder functions write Excel formulas with hardcoded cell addresses from the master Assumptions tab (e.g., `Assumptions!$B$12`). When a standalone workbook contains only a filtered subset of parameters, those row numbers change, breaking every formula.

The recommended approach is **"rebuild, don't copy"**: create each standalone workbook from scratch using the same builder functions but with a modified `build_assumptions_tab` that writes only the relevant parameter groups and returns a new `param_refs` dict with correct cell addresses. Since the builders already use `param_refs` as their sole interface to the Assumptions tab, this remapping is clean. No formula rewriting or cell-address patching is needed.

Additional requirements include a Glossary/Definitions tab (REQ-U11), scenario narratives (REQ-D03), what-if toggle switches for buyback-burn and deploy-POL (REQ-D07), and a versioned cover sheet with changelog (REQ-D08). These are new tabs/features not present in the master workbook.

**Primary recommendation:** Build a `build_filtered_assumptions_tab(wb, param_names)` function that writes only specified parameters and returns correctly-addressed param_refs. Each standalone reuses the existing model builders unchanged, passing the filtered param_refs. New modules handle Glossary, scenario narratives, what-if toggles, and versioned cover sheets.

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| openpyxl | 3.1.5 | Excel .xlsx generation | Already in use across entire codebase; confirmed working with chart fix |
| Python | 3.x (existing) | Runtime | Already the project language |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| collections.OrderedDict | stdlib | Parameter ordering | Already used for PARAM_GROUPS |
| copy | stdlib | Deep-copying parameter dicts | When building filtered PARAM_GROUPS subsets |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Rebuild approach | openpyxl copy_worksheet() | copy_worksheet CANNOT copy between workbooks (openpyxl limitation). Even within a workbook, it doesn't handle formula reference remapping |
| Rebuild approach | Post-process formula rewriting | Fragile regex on formula strings, breaks on edge cases, hard to maintain |
| Per-model param lists in code | Auto-detection via AST/import analysis | Over-engineered; 4 static lists are maintainable and explicit |

**Installation:**
```bash
# No new dependencies needed. Existing openpyxl 3.1.5 is sufficient.
pip install openpyxl==3.1.5  # Already installed
```

## Architecture Patterns

### Recommended Project Structure
```
generators/
  standalone.py          # NEW: standalone workbook orchestrator
  standalone_config.py   # NEW: per-model parameter lists, glossary terms, scenario narratives
  glossary.py            # NEW: build_glossary_tab(wb, terms) -> None
  cover_sheet.py         # NEW: build_cover_sheet(wb, model_name, version, changelog) -> None
  workbook_base.py       # MODIFIED: add build_filtered_assumptions_tab()
  # ... existing builders unchanged
generate.py              # MODIFIED: add standalone generation after master
```

### Pattern 1: Filtered Assumptions Tab (THE Key Pattern)

**What:** A new function `build_filtered_assumptions_tab(wb, param_subset)` that writes only specified parameters to the Assumptions tab, returning a correctly-addressed `param_refs` dict.

**When to use:** Every standalone workbook uses this instead of `build_assumptions_tab()`.

**Why it works:** All existing builders receive `param_refs` as input and use it as the sole interface to the Assumptions tab. They never hardcode row numbers. The builders are completely agnostic to which other parameters exist on the Assumptions tab -- they only care about the entries in `param_refs` that they look up by name.

**Example:**
```python
# Source: Analysis of existing workbook_base.py and model builders

def build_filtered_assumptions_tab(wb, param_names, include_scenario_selector=True,
                                     include_toggles=None):
    """Build Assumptions tab with only specified parameters.

    Args:
        wb: openpyxl Workbook (styles already registered).
        param_names: set of parameter names to include.
        include_scenario_selector: Whether to add the scenario selector section.
        include_toggles: List of toggle names to include (e.g., ["Tail Emission Toggle"]).

    Returns:
        dict: param_refs mapping parameter name -> "Assumptions!$B$N"
              with correct row numbers for the filtered layout.
    """
    from models.parameters import PARAM_GROUPS
    from generators.styles import register_styles

    register_styles(wb)
    ws = wb.active
    ws.title = "Assumptions"
    # ... standard header rows (rows 1-3) same as master

    param_refs = {}
    current_row = 4

    for group_name, params in PARAM_GROUPS.items():
        # Filter: only include groups that have at least one matching param
        filtered_params = [p for p in params if p["name"] in param_names]
        if not filtered_params:
            continue

        # Write section header
        ws.merge_cells(start_row=current_row, start_column=1,
                       end_row=current_row, end_column=4)
        ws.cell(row=current_row, column=1, value=group_name).style = "section_header"
        current_row += 1

        # Write parameter rows
        for param in filtered_params:
            ws.cell(row=current_row, column=1, value=param["name"])
            value_cell = ws.cell(row=current_row, column=2, value=param["value"])
            value_cell.style = "input_cell"
            # ... format, unit, source same as build_assumptions_tab
            param_refs[param["name"]] = f"Assumptions!$B${current_row}"
            current_row += 1

        current_row += 1  # blank separator

    # Add toggles and scenario selector as in master
    if include_toggles and "Tail Emission Toggle" in include_toggles:
        _add_tail_emission_toggle(ws, param_refs)
    if include_scenario_selector:
        current_row = _add_scenario_selector(ws, current_row, param_refs)

    return param_refs
```

### Pattern 2: Standalone Workbook Orchestrator

**What:** A function per standalone model that creates a fresh workbook, builds filtered Assumptions, calls the same model builders used in the master, and adds new tabs (Glossary, Cover Sheet).

**When to use:** Called by `generate.py` for each of the 4 standalone workbooks.

**Example:**
```python
# Source: Architectural analysis of existing generate.py

def generate_token_price_standalone():
    """Generate the Token Price standalone workbook."""
    wb = Workbook()

    # 1. Build filtered Assumptions tab (only params used by Emission + Token Price)
    param_refs = build_filtered_assumptions_tab(
        wb,
        param_names=TOKEN_PRICE_PARAMS,  # defined in standalone_config.py
        include_scenario_selector=True,
        include_toggles=[],
    )

    # 2. Build model tabs using SAME builders as master
    emission_meta = build_emission_tab(wb, param_refs)
    price_meta = build_token_price_tab(wb, param_refs, emission_meta)

    # 3. Add standalone-specific tabs
    build_glossary_tab(wb, TOKEN_PRICE_GLOSSARY_TERMS)
    build_cover_sheet(wb, "Token Price Model", VERSION, CHANGELOG,
                      scenario_narratives=TOKEN_PRICE_NARRATIVES)

    # 4. Add what-if toggles (if applicable to this model)
    # Token Price has no what-if toggles

    wb.save("output/gonka_token_price.xlsx")
    fix_chart_rendering("output/gonka_token_price.xlsx")
```

### Pattern 3: What-If Toggle Switches

**What:** New DataValidation dropdown parameters (Y/N) that ripple through calculations via IF() formulas in the Assumptions tab.

**When to use:** REQ-D07 requires three toggles: buyback-burn Y/N, tail emissions Y/N, deploy POL Y/N.

**Implementation approach:** The existing Tail Emission Toggle is already a Y/N toggle in PARAM_GROUPS. Two new toggles need to be added to PARAM_GROUPS (or a separate section):

```python
# New parameters to add to models/parameters.py
# WHAT-IF TOGGLES group
("WHAT-IF TOGGLES", [
    {
        "name": "Buyback-Burn Active",
        "value": "Y",
        "unit": "",
        "source": "Toggle",
        "format": "text",
    },
    {
        "name": "Deploy POL Active",
        "value": "Y",
        "unit": "",
        "source": "Toggle",
        "format": "text",
    },
])

# The Tail Emission Toggle already exists in FEE TRANSITION group.
# For standalone workbooks, expose it as part of the what-if toggles section.
```

**Formula impact:** Existing formulas that reference buyback or POL values need to be wrapped in IF checks:
- Buyback-Burn: `=IF(buyback_toggle="Y", <existing formula>, 0)` in Token Price col K, Treasury col F
- Deploy POL: `=IF(pol_toggle="Y", <existing POL formula>, 0)` in Treasury cols B, D, E, M, N
- Tail Emissions: Already handled via existing Tail Emission Toggle

**Critical decision:** These toggles should be added to the **master workbook too** (not just standalones) so behavior is consistent. The master builders would need minor updates to wrap relevant formulas in IF checks.

### Pattern 4: Dependency Chain for Each Standalone

Each standalone workbook must include ALL upstream model tabs because formulas use cross-sheet references. The dependency chain is:

```
Token Price Standalone:
  Tabs: Documentation, Assumptions, Emission Schedule, Token Price, Glossary
  Upstream: Emission Schedule (Token Price cross-refs it)

Fee Transition Standalone:
  Tabs: Documentation, Assumptions, Emission Schedule, Token Price, Fee Transition, Glossary
  Upstream: Emission Schedule + Token Price (Fee Transition cross-refs both)

Host Profitability Standalone:
  Tabs: Documentation, Assumptions, Emission Schedule, Token Price, Fee Transition, Host Profitability, Glossary
  Upstream: Emission + Token Price + Fee Transition (Host Profit cross-refs all three)

Treasury & POL Standalone:
  Tabs: Documentation, Assumptions, Emission Schedule, Token Price, Fee Transition, Treasury & POL, Glossary
  Upstream: Emission + Token Price + Fee Transition (Treasury cross-refs all three)
```

### Anti-Patterns to Avoid

- **Copy-and-modify formulas:** Never try to regex-replace cell addresses in formula strings. The builders already produce correct formulas from param_refs.
- **Shared workbook object:** Never try to delete sheets from the master workbook to create standalones. Build each workbook independently.
- **Duplicating builder code:** Never copy-paste from existing builders. Reuse them directly with filtered param_refs.
- **Hardcoded row numbers in standalone logic:** Always let build_filtered_assumptions_tab compute row numbers dynamically.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Parameter filtering | Manual param lists per group | Filter from PARAM_GROUPS using a set of param names | PARAM_GROUPS is single source of truth; manual lists go stale |
| Glossary sorting | Custom sort | Python's built-in `sorted()` on term dicts | Alphabetical sort is trivial |
| Version/changelog | Hardcoded strings in builder | A `VERSION_INFO` dict in a config module | Single source of truth for all 5 workbooks |
| DataValidation dropdowns | Custom input validation | openpyxl DataValidation(type="list") | Already proven pattern in workbook_base.py |
| Excel formula construction | String concatenation with manual escaping | f-strings with param_refs (existing pattern) | Already working across all builders |

**Key insight:** The existing codebase already solved the hardest problem (formula generation via param_refs). The standalone generation is an orchestration problem, not a formula problem.

## Common Pitfalls

### Pitfall 1: Forgetting Upstream Tab Dependencies
**What goes wrong:** A standalone workbook is missing a tab that another tab's formulas reference (e.g., Fee Transition without Token Price), causing #REF! errors everywhere.
**Why it happens:** Developer thinks "Fee Transition standalone" means only the Fee Transition tab, not realizing its formulas reference Emission Schedule and Token Price.
**How to avoid:** Always include the full dependency chain. Map out which tabs' formulas reference which other tabs. The dependency chains are documented above in Pattern 4.
**Warning signs:** #REF! errors when opening the standalone in Excel.

### Pitfall 2: Missing Scenario Selector Params
**What goes wrong:** The scenario selector section at the bottom of the Assumptions tab is omitted from standalones, but model builders reference "Active Price Low", "Active Price High", and "Scenario Index" from param_refs.
**Why it happens:** These are computed/formula params added by `_add_scenario_selector()`, not regular PARAM_GROUPS entries.
**How to avoid:** The `build_filtered_assumptions_tab()` must replicate the scenario selector section (MATCH + CHOOSE formulas). Include the 6 price scenario params, Active Scenario dropdown, Scenario Index, Active Price Low, and Active Price High.
**Warning signs:** KeyError on "Active Price Low" or "Active Price High" in token_price.py or other builders.

### Pitfall 3: Tail Emission Toggle Missing from param_refs
**What goes wrong:** Fee Transition builder fails with KeyError because "Tail Emission Toggle" is not in filtered param_refs.
**Why it happens:** Tail Emission Toggle is in PARAM_GROUPS["FEE TRANSITION"] but the DataValidation dropdown is added separately by `_add_tail_emission_toggle()`. If the FEE TRANSITION group is included in filtered params, the toggle value is there, but the DataValidation must also be applied.
**How to avoid:** When a standalone includes the Fee Transition tab, ensure "Tail Emission Toggle" is in the param_names set AND `_add_tail_emission_toggle()` is called.
**Warning signs:** No dropdown appears on the Tail Emission Toggle cell, or KeyError at runtime.

### Pitfall 4: Chart Rendering Fix Forgotten
**What goes wrong:** Charts don't render in Excel when opening standalone workbooks.
**Why it happens:** `fix_chart_rendering()` must be called on every .xlsx file after save, not just the master.
**How to avoid:** Call `fix_chart_rendering()` on each standalone workbook after saving.
**Warning signs:** Charts appear as blank boxes in Excel.

### Pitfall 5: Param_refs Keys That Come From Non-PARAM_GROUPS Sources
**What goes wrong:** Builders crash with KeyError because they reference param_refs entries that aren't direct PARAM_GROUPS parameters.
**Why it happens:** `workbook_base.py` adds computed entries to param_refs: "Active Scenario", "Scenario Index", "Active Price Low", "Active Price High". These are formula cells, not PARAM_GROUPS entries.
**How to avoid:** The filtered assumptions builder must add these computed entries too. They depend on: Conservative/Moderate/Aggressive Price Low/High params being present.
**Warning signs:** KeyError for "Active Price Low" or similar at builder call time.

### Pitfall 6: What-If Toggles Breaking Master Workbook
**What goes wrong:** Adding IF() wrappers to existing formulas in master builders changes the master workbook behavior when toggles default to "Y".
**Why it happens:** Default value "Y" means no behavioral change, but the formulas become more complex. If implemented incorrectly (e.g., wrong toggle name string comparison), formulas evaluate to 0.
**How to avoid:** Test the master workbook output after adding toggle support. Ensure IF("Y"="Y",...) evaluates to the existing formula path. Add toggles to master PARAM_GROUPS with default "Y" values so formulas are always correct.
**Warning signs:** Master workbook values change after adding toggle support.

### Pitfall 7: Glossary Tab Position Conflicts
**What goes wrong:** Tab ordering is wrong when Glossary and Cover Sheet are inserted.
**Why it happens:** openpyxl creates sheets at the end by default. Documentation/Cover Sheet must be at index 0, Glossary can be at the end or before model tabs.
**How to avoid:** Create all model tabs first, then insert Documentation at index 0 and append Glossary at the end. Verify tab order with an assertion (existing pattern from generate.py).
**Warning signs:** Documentation tab is not the first tab when opening in Excel.

## Code Examples

### Building a Complete Parameter Map Per Standalone

```python
# Source: Codebase analysis of param_refs usage in each builder

# Each set includes ALL params needed by ALL builders in that standalone's chain.
# Emission Schedule params are needed by every standalone (it's always included).

EMISSION_PARAMS = {
    "Initial Daily Emission",
    "Decay Rate",
    "Community Pool",
    "Founder Allocation",
}

TOKEN_PRICE_PARAMS = EMISSION_PARAMS | {
    "Conservative Price Low",
    "Conservative Price High",
    "Moderate Price Low",
    "Moderate Price High",
    "Aggressive Price Low",
    "Aggressive Price High",
    "Bitfury Schelling Point",
    "Total Supply",
    "Assumed Annual Fee Revenue",
    "Buyback-Burn",
    # Scenario selector deps (Active Price Low/High are computed, not in PARAM_GROUPS)
}

FEE_TRANSITION_PARAMS = TOKEN_PRICE_PARAMS | {
    "Base Active Developers",
    "Conservative Dev Growth",
    "Moderate Dev Growth",
    "Aggressive Dev Growth",
    "Revenue Per Developer (Annual)",
    "Host Share",
    "AI Training Fund",
    "veGNK Yield Pool",
    "Tail Emission Toggle",
    "Tail Emission Rate (Contingency)",
}

HOST_PROFITABILITY_PARAMS = FEE_TRANSITION_PARAMS | {
    "Current Hosts",
    "Current GPUs",
    "Electricity Cost Low",
    "Electricity Cost Mid",
    "Electricity Cost High",
    "GPU Power Draw",
    "Traditional Rental Rate (Lambda)",
    "H100 Hardware Cost Low",
    "H100 Hardware Cost High",
}

TREASURY_POL_PARAMS = FEE_TRANSITION_PARAMS | {
    "Community Pool",         # already in EMISSION_PARAMS
    "POL GNK Allocation",
    "Total Supply",           # already in TOKEN_PRICE_PARAMS
    "Expected LP Fee Revenue Low",
    "Expected LP Fee Revenue High",
    "POL Rebalancing Cost",
    "Annual GNK Allocation for Defense",
    "Defense Treasury Target Low",
    "AI Fund Monthly Expenses",
}
```

### Glossary Tab Builder

```python
# Source: REQ-U11 requirements + openpyxl patterns from existing codebase

GLOSSARY_TERMS = {
    "TWAP": "Time-Weighted Average Price. An average price calculated over a "
            "fixed interval (e.g., 15 minutes) to smooth out short-term volatility.",
    "veGNK": "Vote-Escrowed GNK. GNK tokens locked for a period (30-730 days) to "
             "gain governance voting power and yield boost multipliers.",
    "POL": "Protocol-Owned Liquidity. Liquidity pool positions owned by the Gonka "
           "protocol treasury rather than third-party LPs.",
    "FDV": "Fully Diluted Valuation. Total Supply multiplied by current token price.",
    "EIP-1559": "Ethereum Improvement Proposal 1559. A fee mechanism with a base fee "
                "that adjusts dynamically based on network utilization.",
    "Buyback-Burn": "Protocol mechanism where fee revenue is used to purchase GNK tokens "
                    "on the open market, which are then permanently removed from circulation.",
    "Crossover Ratio": "Fee revenue divided by emission value. When ratio >= 1.0, "
                       "fee revenue exceeds emission costs (sustainability threshold).",
    "Tail Emission": "A minimum daily emission rate (contingency) that activates when "
                     "natural exponential decay falls below the threshold.",
    # ... additional terms
}

def build_glossary_tab(wb, terms=None):
    """Build a Definitions/Glossary tab with alphabetical entries.

    Args:
        wb: openpyxl Workbook.
        terms: dict of {term: definition}. If None, uses full GLOSSARY_TERMS.
    """
    if terms is None:
        terms = GLOSSARY_TERMS

    ws = wb.create_sheet("Definitions")

    # Title
    ws.merge_cells("A1:C1")
    ws.cell(row=1, column=1, value="DEFINITIONS / GLOSSARY").style = "section_header"

    # Headers
    ws.cell(row=2, column=1, value="Term").style = "header"
    ws.cell(row=2, column=2, value="Definition").style = "header"

    # Alphabetical entries
    row = 3
    for term in sorted(terms.keys()):
        ws.cell(row=row, column=1, value=term).font = Font(bold=True)
        ws.cell(row=row, column=2, value=terms[term])
        row += 1

    ws.column_dimensions["A"].width = 25
    ws.column_dimensions["B"].width = 80
```

### Scenario Narratives

```python
# Source: REQ-D03 requirements

TOKEN_PRICE_NARRATIVES = {
    "Conservative": (
        "Under conservative assumptions, GNK price grows from $0.50 to $1.00 over "
        "10 years, reflecting cautious adoption. Market cap reaches ~$900M by Year 10 "
        "with modest buyback-burn impact on supply."
    ),
    "Base": (
        "The base scenario projects GNK price growth from $1.00 to $3.00, driven by "
        "steady developer onboarding and network utilization. Buyback-burn reduces "
        "circulating supply meaningfully by Year 5-6."
    ),
    "Aggressive": (
        "Aggressive adoption drives GNK from $3.00 to $10.00, assuming rapid GPU "
        "network expansion and strong demand. FDV exceeds $9B by Year 10 with "
        "significant deflationary pressure from buyback-burn."
    ),
}
# Similar narrative dicts for fee_transition, host_profitability, treasury
```

### What-If Toggle Integration in Builder Formulas

```python
# Source: Analysis of existing toggle pattern in fee_transition.py

# Existing pattern for tail emission toggle (already in codebase):
g_cell = ws.cell(
    row=row, column=7,
    value=(
        f'=IF({tail_toggle_ref}="ON",'
        f"MAX(...),"
        f"F{row})"
    ),
)

# New pattern for buyback-burn toggle in token_price.py:
# K: Buyback Burn (GNK)
buyback_toggle_ref = param_refs["Buyback-Burn Active"]
k_cell = ws.cell(
    row=row, column=11,
    value=(
        f'=IF({buyback_toggle_ref}="Y",'
        f'{fee_rev_ref}*{buyback_ref}/F{row}/{periods_per_year},'
        f'0)'
    ),
)

# New pattern for deploy POL toggle in treasury.py:
# D: POL Revenue
pol_toggle_ref = param_refs["Deploy POL Active"]
d_formula = (
    f'=IF({pol_toggle_ref}="Y",'
    f'({pol_rev_low_ref}+{pol_rev_high_ref})/2*{days}/365'
    f'-{pol_rebal_ref}*{days}/365,'
    f'0)'
)
```

### Cover Sheet with Version and Changelog

```python
# Source: REQ-D08 requirements + existing documentation.py patterns

VERSION_INFO = {
    "version": "v1.1",
    "changelog": [
        ("v1.1", "2026-02-XX", "Added standalone workbooks, glossary, what-if toggles"),
        ("v1.0", "2026-02-06", "Initial release with master workbook"),
    ],
}

def build_cover_sheet(wb, model_name, version_info, scenario_narratives=None):
    """Build versioned cover sheet for standalone workbook.

    Adapts the existing documentation.py pattern but adds:
    - Model-specific title (e.g., "Token Price Model")
    - Version number and changelog table
    - Scenario narratives section (REQ-D03)
    """
    ws = wb.create_sheet("Documentation", index=0)
    # ... title, version, date (same pattern as documentation.py)

    # Changelog section
    row = changelog_start
    ws.cell(row=row, column=1, value="CHANGELOG").style = "section_header"
    row += 1
    for ver, date, description in version_info["changelog"]:
        ws.cell(row=row, column=1, value=ver)
        ws.cell(row=row, column=2, value=date)
        ws.cell(row=row, column=3, value=description)
        row += 1

    # Scenario narratives section (if provided)
    if scenario_narratives:
        row += 1
        ws.cell(row=row, column=1, value="SCENARIO NARRATIVES").style = "section_header"
        row += 1
        for scenario, narrative in scenario_narratives.items():
            ws.cell(row=row, column=1, value=scenario).font = Font(bold=True)
            ws.cell(row=row, column=2, value=narrative)
            row += 1
```

## Detailed Parameter Mapping Per Standalone

This is the critical data the planner needs to define tasks correctly.

### Parameters from PARAM_GROUPS (68 total, by standalone usage)

| Standalone | PARAM_GROUPS params needed | Count | Groups touched |
|-----------|--------------------------|-------|----------------|
| Token Price | EMISSION_PARAMS + price/buyback params | 17 | TOKEN SUPPLY, EMISSION PARAMETERS, PRICE SCENARIOS, BUYBACK PARAMETERS |
| Fee Transition | TOKEN_PRICE_PARAMS + fee/growth params | 28 | Above + REVENUE ALLOCATION, DEVELOPER GROWTH, FEE TRANSITION |
| Host Profitability | FEE_TRANSITION_PARAMS + host/GPU params | 39 | Above + GPU ECONOMICS, HOST ECONOMICS |
| Treasury & POL | FEE_TRANSITION_PARAMS + treasury/POL params | 37 | TOKEN_PRICE + REVENUE ALLOCATION + DEVELOPER GROWTH + FEE TRANSITION + POL PARAMETERS, BUYBACK PARAMETERS, FLOOR DEFENSE, TREASURY OPERATIONS |

### Tabs Per Standalone

| Standalone | Model Tabs | New Tabs | Total |
|-----------|-----------|----------|-------|
| Token Price | Assumptions, Emission Schedule, Token Price | Documentation, Definitions | 5 |
| Fee Transition | Assumptions, Emission Schedule, Token Price, Fee Transition | Documentation, Definitions | 6 |
| Host Profitability | Assumptions, Emission Schedule, Token Price, Fee Transition, Host Profitability | Documentation, Definitions | 7 |
| Treasury & POL | Assumptions, Emission Schedule, Token Price, Fee Transition, Treasury & POL | Documentation, Definitions | 7 |

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Manual Excel workbook splitting | Programmatic generation from shared builders | This phase | Consistent, reproducible, error-free |
| Static PDF documentation | Interactive Excel with glossary tabs | This phase | Users can explore definitions in-context |
| No toggles for what-if | DataValidation Y/N dropdowns with IF() formulas | This phase | Non-technical users can toggle mechanisms on/off |

**Deprecated/outdated:**
- openpyxl `copy_worksheet()` between workbooks: Not supported and never was. Don't attempt this approach.

## Open Questions

1. **Should what-if toggles be added to the master workbook too?**
   - What we know: REQ-D07 says "what-if toggle switches" in the context of standalone workbooks. The tail emission toggle already exists in the master.
   - What's unclear: Whether buyback-burn Y/N and deploy POL Y/N should also appear in the master.
   - Recommendation: Add them to the master too for consistency. The default "Y" value means zero behavioral change unless the user toggles. This keeps master and standalone behavior identical.

2. **Should the Dashboard tab be included in any standalone?**
   - What we know: Success criteria says "1 master + 4 standalone workbooks". Dashboard is a cross-model summary.
   - What's unclear: Whether any standalone should include a simplified dashboard.
   - Recommendation: No. Dashboard references all model tabs and is inherently a master-only feature. Standalones have their own scenario narratives for context.

3. **How to handle the Emission Schedule as a "shared dependency"?**
   - What we know: All 4 standalones need Emission Schedule because every model cross-references it.
   - What's unclear: Whether this makes "standalone" a misnomer (each file still has 5-7 tabs).
   - Recommendation: Accept this as architectural necessity. The alternative (embedding emission data as static values) would break the live-formula model. Each standalone having Emission Schedule is correct.

4. **Exact glossary terms per standalone vs. universal glossary?**
   - What we know: REQ-U11 says "alphabetical glossary of terms (TWAP, veGNK, POL, etc.)".
   - What's unclear: Whether each standalone should have a filtered glossary (only relevant terms) or the full glossary.
   - Recommendation: Full glossary in each standalone. It's a reference tab -- having extra terms doesn't harm, and it ensures users always find what they need.

5. **Filename convention for standalone workbooks?**
   - What we know: Master is `gonka_master_model.xlsx`.
   - Recommendation: `gonka_token_price.xlsx`, `gonka_fee_transition.xlsx`, `gonka_host_profitability.xlsx`, `gonka_treasury_pol.xlsx`

## Sources

### Primary (HIGH confidence)
- **Codebase analysis:** Direct reading of all 10 generator modules, models/parameters.py, and generate.py. This is the authoritative source for param_refs usage, formula patterns, and architectural contracts.
- **openpyxl 3.1.5 documentation:** [Validating cells](https://openpyxl.readthedocs.io/en/3.1/validation.html) -- DataValidation patterns for toggle switches
- **openpyxl workbook API:** [Workbook module](https://openpyxl.readthedocs.io/en/3.1/api/openpyxl.workbook.workbook.html) -- confirmed copy_worksheet limitation (within-workbook only)
- **openpyxl worksheet copier:** [Copier module](https://openpyxl.readthedocs.io/en/stable/_modules/openpyxl/worksheet/copier.html) -- confirms no cross-workbook copy support

### Secondary (MEDIUM confidence)
- **WebSearch:** openpyxl copy_worksheet limitations confirmed by multiple sources and official docs
- **WebSearch:** openpyxl version 3.1.5 confirmed as latest via PyPI

### Tertiary (LOW confidence)
- None. All findings verified against codebase or official documentation.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - same openpyxl 3.1.5 already in use, no new dependencies
- Architecture: HIGH - based on thorough analysis of existing codebase patterns and param_refs contract
- Pitfalls: HIGH - derived from direct code analysis of formula dependencies and builder interfaces
- Parameter mapping: HIGH - traced every param_refs["..."] call in every builder module

**Research date:** 2026-02-06
**Valid until:** 2026-03-06 (stable -- openpyxl and codebase architecture unlikely to change)

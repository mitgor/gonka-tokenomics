# Domain Pitfalls: Tokenomics Economic Modeling Workbooks

**Domain:** Python-generated Excel workbooks for tokenomics economic modeling
**Researched:** 2026-02-05
**Project:** Gonka Network tokenomics (emission decay, fee transition, host ROI, treasury/POL simulation, IL modeling)
**Audience:** Non-technical leadership decision-makers

---

## Critical Pitfalls

Mistakes that cause incorrect decisions, model rewrites, or loss of stakeholder trust. These must be addressed during initial design, not patched later.

---

### Pitfall 1: The Reflexivity Trap -- Token Price as Both Input and Output

**What goes wrong:** The model takes GNK price as an input assumption, but the model's outputs (emission value, host profitability, treasury value, buyback impact) all influence GNK price in reality. Leadership sees "at $1 GNK, host ROI is 3.2x" and treats $1 as independent of the model's other assumptions. In truth, if developer growth is 10% instead of 25%, the fee transition fails, hosts leave, and $1 GNK is unachievable. The model's scenarios appear independent when they are deeply coupled.

**Why it happens:** Spreadsheet models are inherently feed-forward (inputs produce outputs). Real token economies are reflexive (outputs feed back into inputs). Breaking the circular dependency is impossible in a deterministic spreadsheet, so modelers treat price as exogenous when it is endogenous.

**Consequences:** Leadership picks the "moderate" scenario as most likely, treats it as a plan, and is blindsided when a single variable (developer growth) invalidates the price assumption underlying every other calculation. Decisions made on one model tab (e.g., POL allocation at $1 GNK) become nonsensical if the price assumption on another tab (fee transition) implies $0.30 GNK.

**Warning signs:**
- Price scenarios on different tabs use different GNK price assumptions without cross-referencing
- No tab shows "what happens to host ROI if the fee transition scenario plays out at this price"
- The model has no internal consistency checks across tabs

**Prevention:**
- Create a master assumptions tab where GNK price is defined ONCE and flows to ALL model tabs via cell references. Never hardcode price in any calculation tab.
- Build a "scenario consistency matrix" showing which price trajectory is compatible with which growth/fee/emission scenario. If conservative growth implies $0.50 GNK but the host ROI tab models $1 GNK as "conservative," flag the inconsistency explicitly.
- Label every price-dependent output with its price assumption: "Host ROI: 3.2x (assumes $1.00 GNK)" -- never present a number without its price context.
- Add a dedicated "Scenario Consistency" tab that cross-references assumptions across all models and flags contradictions with conditional formatting.

**Affected models:** ALL -- every model depends on GNK price. Most critical for host profitability and fee transition crossover.

**Severity:** CRITICAL

---

### Pitfall 2: Exponential Decay Precision Errors Compound Over Long Time Horizons

**What goes wrong:** Gonka's emission schedule uses exponential decay at rate -0.000475 per epoch. Over 10+ years (3,650+ epochs), tiny floating-point errors in the decay calculation compound. Python's `float` type stores 0.1 as 0.1000000000000000055511151231257827021181583404541015625. When computing `323000 * (1 - 0.000475) ** 3650`, the error from float representation of the decay rate propagates through 3,650 multiplications. By Year 10, cumulative emission totals can diverge from the mathematically correct value by thousands of GNK.

**Why it happens:** IEEE 754 double-precision floating point cannot exactly represent 0.000475. Each epoch's calculation multiplies the previous result (with its accumulated error) by a slightly wrong decay factor. The error is multiplicative, not additive, so it grows faster than intuition suggests.

**Consequences:** Cumulative emission totals (which inform circulating supply, inflation rate, and the fee-to-emission crossover point) are wrong at exactly the time horizon that matters most: Year 8-12, when Gonka's "danger zone" for fee transition occurs. If the model shows crossover at Year 8 but the real math says Year 9, leadership has one fewer year than they think.

**Warning signs:**
- Year 10 cumulative emissions differ between Python calculation and Excel formula by more than 100 GNK
- No validation cell comparing Python-computed cumulative emissions against closed-form sum formula
- Epoch-by-epoch emission values are computed iteratively (each row depends on previous) rather than from the closed-form `E(t) = E0 * (1 - r)^t`

**Prevention:**
- Use Python's `decimal.Decimal` module for all emission calculations: `Decimal('0.000475')` represents the decay rate exactly. Convert to float only at the final step when writing to Excel.
- Use the closed-form formula `E(t) = 323000 * (1 - 0.000475)^t` in Excel cells rather than iterative `=A_prev * (1 - 0.000475)`. The closed-form avoids error accumulation because each cell is computed independently from the base values.
- Include a validation row: compute cumulative emissions using both the geometric series sum formula `S = E0 * (1 - (1-r)^n) / r` and the sum of individual epoch values. Display the difference. It should be zero (or within Excel's 15-digit precision).
- For the crossover analysis specifically, compute the crossover point algebraically (solve for t where fee revenue equals emission value) and compare against the spreadsheet's interpolated crossover row.

**Affected models:** Emission decay curve, fee transition crossover, host profitability (all depend on epoch reward values).

**Severity:** CRITICAL

---

### Pitfall 3: openpyxl Formulas Are Not Calculated -- Stale Values Mislead Readers

**What goes wrong:** openpyxl writes Excel formula strings (e.g., `=SUM(B2:B100)`) to cells but never evaluates them. The generated .xlsx file contains formulas with no cached result values. When the file is opened in Excel, formulas calculate correctly. But when opened in Google Sheets, some complex formulas may show `#NAME?` errors or fail to evaluate. When read back by Python (without Excel opening the file first), all formula cells return `None`. And critically: if the file is opened in Google Sheets and then re-downloaded, some formula results may be wrong because Google Sheets handles certain Excel functions differently.

**Why it happens:** openpyxl is a file-format library, not a spreadsheet engine. It writes the XML representation of formulas but has no calculation engine. The OOXML standard allows formula cells to have no cached value, but many non-Excel consumers expect cached values to exist.

**Consequences:** Leadership opens the file in Google Sheets (the project requirement says "works in Excel and Google Sheets") and sees blank cells, error values, or incorrect results. Trust in the model evaporates. Worse: if Google Sheets silently computes a formula differently, leadership makes decisions on wrong numbers without knowing they are wrong.

**Warning signs:**
- Summary cells show $0 or blank when opened in Google Sheets
- Named ranges referenced in formulas show `#NAME?` in Google Sheets
- CUBE functions, XLOOKUP, or other Excel-specific functions are used
- No testing was done in Google Sheets after file generation

**Prevention:**
- For every formula cell, ALSO write the Python-computed value as a fallback. Use a two-pass approach: first compute all values in Python, write them as static values, then overwrite formula cells with the formula string. This ensures Google Sheets shows correct cached values even if it cannot evaluate the formula.
- Restrict formulas to the common subset supported by both Excel and Google Sheets. Avoid: XLOOKUP (use INDEX/MATCH), FILTER, SORT, UNIQUE, LET, LAMBDA, STOCKHISTORY, and any dynamic array functions. Stick to: SUM, IF, VLOOKUP, INDEX, MATCH, MIN, MAX, AVERAGE, basic arithmetic.
- Test every generated workbook in Google Sheets before delivery. Automate this by using the Google Sheets API to upload the file, read back computed values, and compare against Python-computed expected values.
- Add a "Model Integrity" tab that shows checksums (e.g., total emissions should equal X, total revenue should equal Y). If Google Sheets computes different values, the checksum tab makes the discrepancy visible.

**Affected models:** ALL -- any model using formulas is affected. Most critical for the master unified workbook with cross-tab references.

**Severity:** CRITICAL

---

### Pitfall 4: Concentrated Liquidity IL Model Uses V2 Formula Instead of V3

**What goes wrong:** The POL simulation models impermanent loss for Uniswap v3 concentrated liquidity positions but uses the standard V2 impermanent loss formula `IL = 2*sqrt(r)/(1+r) - 1`. For concentrated liquidity in Uniswap V3, impermanent loss within a tick range is amplified by the capital efficiency multiplier -- it can be 4-10x higher than V2 IL for the same price movement. The model dramatically underestimates IL, making POL returns look better than they are.

**Why it happens:** The V2 IL formula is simple, well-known, and appears in every DeFi tutorial. The V3 concentrated IL formula requires knowing the tick range boundaries (pA, pB) and the current price, and the formula is substantially more complex. It is easy to grab the V2 formula from a tutorial and not realize it does not apply to concentrated positions.

**Consequences:** The POL model shows "IL is only 2.5% if GNK drops 20%" when the real concentrated-position IL is closer to 10-15%. Leadership approves POL deployment based on understated risk. When GNK price moves and actual IL is 4x the modeled amount, treasury value drops more than projected, and confidence in all models erodes.

**Warning signs:**
- IL column uses a formula with only one variable (price ratio) and no range parameters
- IL at 50% price drop shows ~5.7% (this is the V2 number; V3 concentrated is 20-30%)
- No reference to tick range, price boundaries, or capital efficiency factor in the IL calculation
- Model does not show IL increasing as the position range narrows

**Prevention:**
- Use the Uniswap V3 concentrated liquidity IL formula that accounts for the position range [pA, pB]. For the GNK/USDC position at +/-25/+35% from $1.00 (range $0.75-$1.35), compute IL using the concentrated position formula, not the full-range formula.
- Show IL sensitivity to range width: model the same price movement with +/-10%, +/-25%, +/-50% ranges so leadership can see the tradeoff between capital efficiency and IL exposure.
- Include fee income offset: IL alone is misleading. Show "net IL" = gross IL minus accumulated LP fees. Uniswap V3 concentrated positions earn higher fees precisely because of higher capital efficiency. The relevant metric for decision-making is net P&L, not gross IL.
- Compare against the V2 full-range IL as a reference point. Show both numbers explicitly so leadership understands the amplification effect of concentration.

**Affected models:** POL/treasury simulation, impermanent loss workbook.

**Severity:** CRITICAL

---

## Moderate Pitfalls

Mistakes that cause confusion, rework, or reduced model credibility, but do not necessarily produce wrong decisions if caught.

---

### Pitfall 5: Hardcoded Assumptions Scattered Across Tabs

**What goes wrong:** The decay rate (0.000475) appears in cell B7 of the emission tab, is hardcoded as a number in a formula on the fee transition tab, appears as a Python constant that generates a third copy in the host ROI tab, and is defined differently (rounded to 0.0005) in the treasury tab. When leadership asks "what if we change the decay rate?", four values need updating but only one gets changed.

**Why it happens:** Each model is built as a separate script. Each script defines its own constants. When they are combined into a master workbook, the constants are duplicated rather than linked. Financial modeling best practice (separate inputs from calculations) is not followed because the developer thinks of each script as independent.

**Consequences:** Model tabs contradict each other. The emission tab shows 71,929 GNK/day at Year 8 but the fee transition tab (using the rounded rate) shows 68,000 GNK/day. Leadership notices the discrepancy and loses trust in all numbers. Or worse: they do not notice, and different teams use different tabs to make incompatible decisions.

**Prevention:**
- Create a dedicated "Assumptions" tab as the SINGLE source of truth. Every parameter from the Fine-Tuning Recommendations (decay rate, revenue splits 70/20/5/5, POL allocation 22M GNK, initial emission 323,000 GNK/day, etc.) lives here and ONLY here.
- All other tabs reference the Assumptions tab via cell references (e.g., `=Assumptions!B7`). Never type a parameter value into a formula on a calculation tab.
- Use Excel Named Ranges (openpyxl `DefinedName`) for key parameters: `DECAY_RATE`, `INITIAL_EMISSION`, `REVENUE_SPLIT_HOST`, etc. Named ranges make formulas self-documenting (`=INITIAL_EMISSION * (1-DECAY_RATE)^A2` vs `=323000*(1-0.000475)^A2`).
- Follow Wall Street color-coding conventions: blue font for input assumptions, black for same-sheet formulas, green for cross-sheet references. This makes it visually obvious when a value is hardcoded vs. linked.
- In the Python generation scripts, define all parameters in a single config dictionary. Every script imports from this dictionary. The Assumptions tab is generated from this same dictionary, ensuring Python constants and Excel cells match exactly.

**Affected models:** ALL -- every model uses shared parameters.

**Severity:** MODERATE (but becomes CRITICAL if models are used for decision-making without cross-tab consistency checks)

---

### Pitfall 6: openpyxl Chart Compatibility Breaks Across Versions

**What goes wrong:** Charts generated by openpyxl 3.1.4+ display incorrectly in Microsoft Excel due to a known bug where the `app.xml` Application element contains "Microsoft Excel Compatible / Openpyxl" instead of just "Microsoft Excel". Chart labels, axis formatting, and legends render incorrectly or disappear. The same file opens correctly in LibreOffice but looks broken in the tool leadership actually uses.

**Why it happens:** openpyxl versions after 3.1.3 changed the Application string in the generated OOXML package. Microsoft Excel uses this string to determine rendering behavior. The openpyxl developers documented this as a known issue but have not resolved it in all subsequent versions.

**Consequences:** Leadership opens the workbook and sees broken charts: missing labels, overlapping text, incorrect colors. The data is correct but the visual presentation -- which is the primary way non-technical users consume the model -- is damaged. First impressions matter; if charts look broken, the entire model is perceived as unreliable.

**Warning signs:**
- Charts look correct in LibreOffice/Google Sheets but broken in Excel
- Chart axis labels overlap or disappear
- Legend text is cut off or mispositioned
- Using openpyxl version 3.1.4 or later

**Prevention:**
- Pin openpyxl to version 3.1.3 in `requirements.txt` (`openpyxl==3.1.3`). This is the last version with reliable chart rendering in Excel. The performance and feature differences between 3.1.3 and later are negligible for this project's needs.
- If a later version is required for other reasons, post-process the generated .xlsx file: unzip it, replace the Application string in `docProps/app.xml` with "Microsoft Excel", re-zip. This is a documented workaround.
- Test every chart type used (line charts for emission curves, bar charts for revenue comparison, area charts for crossover visualization) in the exact version of Excel leadership uses. Screenshot the expected appearance and include it in the test plan.
- Consider generating charts with minimal openpyxl formatting and relying on Excel's auto-formatting when the file is opened. Over-specifying chart styles in openpyxl increases the surface area for rendering bugs.

**Affected models:** ALL models with charts. Most critical for emission curve visualization and fee transition crossover charts, which are the primary communication tools.

**Severity:** MODERATE

---

### Pitfall 7: Fee Transition Crossover Point Depends on USD Revenue, Not GNK Revenue

**What goes wrong:** The model computes fee revenue in USD and emission value in GNK, then converts emissions to USD at the scenario's assumed GNK price to find the crossover. But the crossover point itself shifts based on GNK price -- at $0.50 GNK, the crossover is earlier (because emissions are worth less in USD) and at $5 GNK, the crossover is later (because emissions are worth more). A single "crossover at Year 6" statement is meaningless without specifying the price at which it occurs. This is a special case of the reflexivity trap (Pitfall 1) but is common enough to warrant its own entry.

**Why it happens:** The crossover analysis naturally involves comparing two curves. It is tempting to plot them on the same chart and find the intersection. But one curve (fee revenue) is in USD and the other (emission rewards) is in GNK, so the conversion factor (GNK price) is itself a variable that changes the intersection point.

**Consequences:** The v1.0 research already identifies this correctly (crossover ranges from Year 4 at $1 GNK to Year 8-9 at $5 GNK), but the Excel model could present a single crossover point without the price context, leading leadership to anchor on one number.

**Warning signs:**
- Crossover chart has a single intersection point rather than a crossover band
- No sensitivity table showing crossover year vs. GNK price
- The chart title says "Fee Transition Crossover" without specifying the price scenario

**Prevention:**
- Build the crossover analysis as a 2D sensitivity table: one axis is GNK price ($0.25, $0.50, $1, $2, $5), the other is developer growth rate (10%, 15%, 25%). Each cell shows the crossover year. This makes the full landscape visible.
- On the crossover chart, plot a crossover BAND (shaded region) rather than a single line, showing the range across price scenarios. This communicates uncertainty visually.
- Add a clear label: "Crossover Year depends on GNK price. At $1 GNK with 15% growth: Year 6. At $5 GNK with 10% growth: Year 9."

**Affected models:** Fee transition crossover, emission vs. fee simulation.

**Severity:** MODERATE

---

### Pitfall 8: Missing Time-Value Adjustments Make Long-Term Projections Misleading

**What goes wrong:** The model projects 10-year treasury values, cumulative buyback amounts, and total host earnings without discounting for the time value of money. "$500K in LP fees over 10 years" sounds impressive until you realize that $50K/year for 10 years is worth less than $500K today. Leadership may compare undiscounted 10-year totals against present-day investment costs and overestimate returns.

**Why it happens:** Crypto tokenomics models rarely include discount rates because there is no agreed-upon risk-free rate for the crypto ecosystem. Traditional financial models use Treasury rates; crypto has no equivalent. So modelers omit discounting entirely rather than choosing an arbitrary rate.

**Consequences:** POL allocation decision is based on "22M GNK generates $550K-$1.1M in LP fees annually" but does not account for the opportunity cost of those 22M GNK. If GNK appreciates 50% in Year 1, the opportunity cost of locking GNK in LP positions dwarfs the fee revenue. Leadership approves POL deployment without understanding the full economic picture.

**Prevention:**
- Include an optional discount rate on the Assumptions tab (default 10-15% for crypto-native projects, adjustable). Show both undiscounted and discounted cumulative totals side-by-side.
- For POL specifically, show the "break-even" analysis: at what GNK price appreciation does the opportunity cost of locking GNK exceed LP fee revenue? This is the decision-relevant metric.
- Label all multi-year totals clearly: "Cumulative LP Fees (undiscounted): $5.5M" and "Present Value at 10% discount: $3.4M".

**Affected models:** Treasury simulation, POL returns, host profitability (long-term projections).

**Severity:** MODERATE

---

### Pitfall 9: Google Sheets 5MB File Size Limit Truncates Large Workbooks

**What goes wrong:** Google Sheets has a 5MB limit for imported .xlsx files. A master workbook with 8+ tabs, each containing 3,650 rows (10 years of daily data), multiple charts, conditional formatting, and data validation can easily exceed this limit. Google Sheets silently drops data, charts, or formatting when the file is too large, or refuses to open it entirely.

**Why it happens:** openpyxl generates verbose XML. Charts add significant file size. Conditional formatting rules are stored per-cell in the XML (not as range rules). A workbook that feels small in Excel terms can be large in raw XML bytes.

**Consequences:** Leadership cannot open the master workbook in Google Sheets. They request standalone workbooks, but those were not prioritized because "the master workbook handles everything." Or worse: Google Sheets opens the file but drops a chart or truncates a data range, and leadership makes decisions on incomplete data.

**Warning signs:**
- Generated .xlsx file size exceeds 3MB (leaves minimal headroom for Google Sheets)
- Master workbook has more than 6 chart objects
- Daily granularity data spans 10+ years (3,650+ rows per tab)

**Prevention:**
- Use monthly or quarterly granularity for long time horizons instead of daily. Emission data can be aggregated to monthly epochs (365 rows for 30 years instead of 10,950 for daily). This reduces file size by 90% with minimal information loss for leadership decision-making.
- Generate standalone workbooks for each model area as first-class deliverables, not afterthoughts. The master workbook is the integrated view; standalones are the sharing format.
- Monitor generated file size in the Python script. Add a warning if the file exceeds 3MB. Log file size in the generation script's output.
- Minimize chart complexity: use data-driven color scales instead of multiple chart series where possible. Each additional series adds XML weight.

**Affected models:** Master unified workbook primarily. Standalone workbooks are unlikely to hit the limit.

**Severity:** MODERATE

---

## Minor Pitfalls

Mistakes that cause annoyance, minor rework, or polish issues, but do not affect model correctness.

---

### Pitfall 10: Number Formatting Inconsistency Across Tabs

**What goes wrong:** The emission tab shows GNK amounts as "323,000" (no decimals), the host ROI tab shows them as "323000.00" (two decimals), and the treasury tab shows "$323,000" (with dollar sign, treating GNK as USD). Percentages appear as "0.15" on one tab and "15%" on another. The model is correct but looks unprofessional and confusing.

**Why it happens:** Each Python script sets number formats independently. One developer uses `'#,##0'`, another uses the default format, a third uses `'$#,##0.00'`. There is no shared formatting specification.

**Prevention:**
- Define a formatting constants module in Python with named formats: `FMT_GNK = '#,##0'`, `FMT_USD = '$#,##0.00'`, `FMT_PCT = '0.00%'`, `FMT_YEAR = '0'`, `FMT_RATIO = '0.00x'`. Every script imports from this module.
- Create a "Formatting Guide" comment on the Assumptions tab listing the conventions (GNK amounts: no decimals with comma separator; USD: two decimals with $ prefix; percentages: two decimals with % suffix).
- Use openpyxl `NamedStyle` objects to define reusable styles (font, fill, number format, alignment) and apply them by name rather than setting properties cell-by-cell.

**Affected models:** ALL -- cosmetic issue across all tabs.

**Severity:** MINOR

---

### Pitfall 11: Unprotected Input Cells Allow Accidental Formula Overwrites

**What goes wrong:** Leadership opens the workbook, clicks on a cell in the calculation area, types a note or number, and accidentally overwrites a formula. The model now produces wrong results, but the overwrite is invisible because the cell looks the same. When the file is shared or revisited, no one knows a formula was destroyed.

**Why it happens:** Excel files generated by openpyxl have no sheet protection by default. All cells are editable. Leadership is told "change the blue cells to adjust assumptions" but nothing prevents them from editing non-blue cells.

**Prevention:**
- Use openpyxl's `worksheet.protection` to lock all cells by default, then unlock only the designated input cells (blue-colored assumption cells). Set a simple password (e.g., "edit") that prevents accidental overwrites but does not frustrate intentional edits.
- Apply `Protection(locked=False)` to input cells and `Protection(locked=True)` to everything else.
- Add a note on the Assumptions tab: "Blue cells are adjustable. All other cells are formula-protected to preserve model integrity."
- Note: Google Sheets respects .xlsx sheet protection, so this works in both target platforms.

**Affected models:** ALL -- any model with adjustable inputs.

**Severity:** MINOR

---

### Pitfall 12: openpyxl Named Range Limitations Break Cross-Tab References

**What goes wrong:** openpyxl cannot resolve defined names that reference other defined names, tables, or use complex expressions. If you create a named range `TOTAL_EMISSIONS` that references another named range `INITIAL_EMISSION`, openpyxl will skip the definition and raise a warning. The generated file may have broken named range references that show `#REF!` errors in Excel.

**Why it happens:** openpyxl's defined name resolution is limited to simple cell/range references. It does not evaluate formulas within defined names. This is a documented limitation.

**Prevention:**
- Keep named ranges simple: they should reference cell ranges only (e.g., `=Assumptions!$B$7`), never formulas or other named ranges.
- For calculated values that need names, create the calculation in a cell first, then point the named range at that cell.
- Test all named ranges by opening the generated file in Excel and checking Name Manager for errors.
- Use `localSheetId` parameter when creating worksheet-scoped named ranges to avoid name collisions across tabs.

**Affected models:** Master unified workbook (relies heavily on cross-tab named ranges).

**Severity:** MINOR

---

### Pitfall 13: Styling Performance Degrades With Large Workbooks

**What goes wrong:** Applying unique style objects (Font, PatternFill, Alignment) to thousands of cells creates thousands of distinct style records in the OOXML file. Excel has practical limits on the number of unique styles (~64,000) and performance degrades well before that limit. The generated file opens slowly, scrolling lags, and leadership perceives the model as broken.

**Why it happens:** Creating a new `Font()` or `PatternFill()` object inside a loop generates a new style record for each cell, even if the style parameters are identical. openpyxl does not deduplicate style objects automatically in all cases.

**Prevention:**
- Define all style objects ONCE at the top of the script (outside any loop). Reuse the same object references for all cells that share a style.
- Use `NamedStyle` for common patterns (header style, input cell style, calculation cell style, output cell style). Apply by name: `cell.style = 'HeaderStyle'`.
- For large data ranges, apply styles to columns or rows rather than individual cells where possible.
- Test that the generated file opens within 3 seconds on a typical machine.

**Affected models:** ALL -- relevant whenever styling more than a few hundred cells.

**Severity:** MINOR

---

## Phase-Specific Warnings

Mapping pitfalls to the specific models being built, ordered by build priority.

| Model / Phase Topic | Most Likely Pitfall | Secondary Pitfall | Mitigation Priority |
|---|---|---|---|
| **Emission decay curve** | #2 Float precision compounds over 10yr horizon | #5 Decay rate hardcoded instead of referenced | Build Assumptions tab FIRST; use Decimal for computation |
| **Fee transition crossover** | #7 Crossover point depends on GNK price | #1 Reflexivity: growth rate and price are coupled | Always show crossover as 2D matrix, not single point |
| **Host profitability / ROI** | #1 Reflexivity: ROI depends on price which depends on ROI | #8 Multi-year ROI shown undiscounted | Include opportunity cost and discount rate |
| **Treasury / POL simulation** | #4 V2 IL formula used for V3 concentrated positions | #8 Undiscounted multi-year returns overstate value | Use correct V3 IL formula with range parameters |
| **Master unified workbook** | #3 Formulas not calculated in Google Sheets | #9 File exceeds 5MB Google Sheets limit | Test in Google Sheets; use monthly granularity |
| **Standalone summary workbooks** | #5 Assumptions diverge from master | #10 Inconsistent number formatting | Generate from same config dict; shared format module |
| **All chart-heavy outputs** | #6 openpyxl chart rendering bugs | #13 Style objects bloat file size | Pin openpyxl 3.1.3; define styles once |
| **All adjustable-input models** | #11 Users overwrite formulas accidentally | #12 Named ranges break on complex refs | Sheet protection; simple named range references |

---

## Pre-Delivery Checklist

Before any workbook is delivered to leadership, verify:

- [ ] **Assumption consistency**: Every parameter on the Assumptions tab matches its usage in every calculation tab. No hardcoded values in formulas.
- [ ] **Cross-tab coherence**: Price scenarios used on one tab are compatible with growth/fee assumptions on other tabs. Scenario consistency matrix reviewed.
- [ ] **Google Sheets test**: File opened in Google Sheets. All formulas evaluate. All charts render. No `#NAME?` or `#REF!` errors. File size under 5MB.
- [ ] **Excel test**: File opened in the version of Excel leadership uses. Charts render correctly. No macro warnings.
- [ ] **Precision validation**: Cumulative emission totals match closed-form sum formula within 1 GNK. Crossover year matches algebraic solution.
- [ ] **IL formula verification**: POL impermanent loss uses V3 concentrated formula with tick range parameters, not V2 full-range formula.
- [ ] **Number format audit**: GNK amounts, USD amounts, percentages, and ratios formatted consistently across all tabs.
- [ ] **Input protection**: All non-input cells are formula-protected. Input cells are clearly labeled and unlocked.
- [ ] **File size check**: Master workbook under 5MB. Standalone workbooks under 2MB.

---

## Sources

### Tokenomics Modeling
- [Tokenomics and Financial Modeling for Web3 Startups](https://fortress-accounting.com/tokenomics-financial-modeling-web3-startups/) -- common design mistakes
- [Tokenomics Design: Essential Principles](https://hacken.io/discover/tokenomics-design-principles/) -- supply-side vs demand-side neglect
- [Building Sustainable Tokenomics Model](https://rocknblock.medium.com/comprehensive-guide-to-building-sustainable-tokenomics-model-466dba084dfe) -- vesting and allocation pitfalls
- [Solidly Emissions Deep Dive](https://jumpcrypto.com/solidly-emissions-a-deep-dive/) -- gap between documented and actual emission implementation
- [Token Value Assessment -- Reflexivity](https://www.inweb3.com/tokenomics-fundamentals-part-vi-token-value-assessment/) -- reflexivity in token price models
- [New Tokenomics Standards in 2026](https://malcolmtan.net/investment-guide/new-tokenomics-standards-in-2026-what-investors-expect/) -- current investor expectations

### openpyxl and Excel Generation
- [openpyxl Documentation](https://openpyxl.readthedocs.io/en/stable/) -- official docs, formula handling, chart support
- [openpyxl Formula Cache Issue](https://foss.heptapod.net/openpyxl/openpyxl/-/issues/578) -- formula cells return None without Excel evaluation
- [openpyxl Chart Rendering Bugs](https://groups.google.com/g/openpyxl-users/c/khC6BTqaH3Y) -- version 3.1.4+ chart problems
- [openpyxl Defined Names](https://openpyxl.readthedocs.io/en/stable/defined_names.html) -- named range limitations
- [openpyxl Number Formatting](https://openpyxl.readthedocs.io/en/stable/_modules/openpyxl/styles/numbers.html) -- format string reference

### Financial Model Integrity
- [Financial Modeling Mistakes Playbook](https://www.alphaapexgroup.com/blog/financial-modeling-mistakes) -- hardcoding, structural errors
- [Financial Model Color Formatting](https://www.wallstreetoasis.com/resources/financial-modeling/financial-model-color-formatting) -- Wall Street color coding conventions
- [Sensitivity Analysis in Excel](https://www.datacamp.com/tutorial/sensitivity-analysis-in-excel) -- scenario analysis best practices
- [Top Excel Mistakes in Budgeting](https://www.golimelight.com/blog/top-excel-mistakes-in-budgeting) -- formula errors, outdated models
- [Excel Financial Model Formatting Guide](https://www.alexanderjarvis.com/excel-financial-model-formatting-guide/) -- input/calculation separation

### Floating Point and Precision
- [Python Floating-Point Limitations](https://docs.python.org/3/tutorial/floatingpoint.html) -- official Python docs on float precision
- [Python Decimal Module](https://docs.python.org/3/library/decimal.html) -- exact decimal arithmetic for financial calculations

### Impermanent Loss and DeFi Modeling
- [Impermanent Loss in Uniswap V3](https://medium.com/auditless/impermanent-loss-in-uniswap-v3-6c7161d3b445) -- concentrated IL amplification
- [Why IL Calculators Are Wrong](https://dedotfi-guides.medium.com/why-impermanent-loss-calculators-are-wrong-and-how-to-avoid-incorrect-assessment-of-the-money-waste-d349607706fc) -- fee exclusion and asset assumption errors
- [Excel Liquidity Pool Simulator](https://github.com/ApopheniaPays/excel-liquidity-pool-simulator) -- reference implementation for AMM modeling

### Google Sheets Compatibility
- [Excel Formulas Not Working in Google Sheets](https://support.google.com/docs/thread/219934507) -- function incompatibilities
- [Incompatible Functions Between Sheets and Excel](https://help.openasapp.com/incompatible-functions) -- function compatibility reference
- [Google Sheets Import File Size Limits](https://support.google.com/docs/thread/261177081) -- 5MB import limit

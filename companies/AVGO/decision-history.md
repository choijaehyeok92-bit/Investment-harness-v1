
# Decision History — AVGO

Append-only. Do not erase prior decisions.

## 2026-09-04 — Initial underwriting

- **Decision:** `WATCH` · **Position band:** `NONE`
- **Total score:** **68 / 100** — *Starter / Watch* (business quality **57/75**;
  expectation gap 7/15; asymmetry 4/10)
- **Hard Veto status:** `INVESTIGATE` — no FAIL. One HIGH-severity item:
  `fatal_concentration`. MEDIUM: `management_or_accounting_integrity`,
  `persistent_dilution`, `moat_shrinkage`, `price_requires_unrealistic_bull_case`.
- **Red team:** `PASS`, confidence **0.70** — **concurs with the decision**, dissents
  on one score
- **Macro pacing:** `slow` · **Decision confidence:** 0.62

### Source basis

Three tier-1 SEC filings supplied: **10-K FY2025** (FY ended 2025-11-02), **10-Q Q2
FY2026** (quarter ended 2026-05-03), **DEF 14A** (2026-03-02).

**Currency caveat:** Broadcom released **Q3 FY2026 on 2026-09-02**, after all supplied
filings — headline only (revenue, adjusted EPS, AI revenue). **The FY2026 GAAP earnings
figures are the analyst's own estimates** and are the weakest input in this file.

### What the analysis found

**Operating economics are excellent.** FY2025 revenue $63,887M (+23.9%); capex **$623M
— 1.0% of revenue**, the most asset-light in this harness; FCF $26,914M at a **42.1%
margin**. Semiconductor operating margin 55.7% → 57.6% → **61.8%** (Q2 FY2026);
infrastructure software **78.7%**. Q3 FY2026 AI semiconductor revenue **$16.7B, +221%
YoY**, with Q4 guided to **$21.7B** and consolidated **$34.8B (+93%)** — FY2026 revenue
near **$105.9B, +65.8%**. `low_quality_growth` and `incremental_roic_collapse` both PASS.

**Three things hold this at WATCH.**

**1. Concentration — the primary gate.** One distributor customer went **29% → 42% of
TOTAL revenue in one year** (32% in FY2025); top five to 45%; distributors to 56%.
**The most extreme in this harness** — worse than NVDA's 22% and TSM's 19% — and
amplified by **~$47.1B of net debt**, the only material leverage among the four names.

**2. The per-share test fails.** Share count **4,139M → 4,686M → 4,741M → 4,758M**.
In H1 FY2026 it **rose 17M despite $8,450M of buybacks**, because SBC of $4,268M
(10.3% of revenue) issued more than repurchases retired. *In fairness*, most of the
multi-year rise was the 544M VMware shares — which is why `persistent_dilution` is
MEDIUM, not HIGH.

**3. Valuation.** ~**38x estimated FY2026 GAAP** earnings (highest of the four), 29x
non-GAAP. **GAAP is used because roughly half the non-GAAP add-back is SBC**, which the
rising share count proves is a real cost. Weighted five-year return **+9.6% total
(1.8%/yr)**.

**Also flagged:** FY2025 **net income ($23,126M) exceeds pretax income ($22,729M)** on a
**$397M tax benefit**; goodwill + intangibles **$130,074M of a $171,092M** asset base
against **$81,292M** equity — tangible book deeply negative; infrastructure software
decelerated from +26% to **+5.1%**.

### Why WATCH — and why that differs from NVDA and TSM

| | 005930 | NVDA | TSM | **AVGO** |
|---|---|---|---|---|
| Score | 69 | 75 | 79 | **68** |
| Business quality (of 75) | 59 | 62 | 66 | **57** |
| Share count | falling | falling | flat | **RISING** |
| Balance sheet | net cash | net cash | net cash | **net debt $47.1B** |
| Top customer | — | 22% | 19% | **42%** |
| Weighted 5-yr return | +5.8% | +21.2% | +37.9% | **+9.6%** |
| Verdict | WATCH | STARTER | STARTER | **WATCH** |

The gap is **positive but the thinnest of the four**. And the decisive distinction:
unlike TSM — whose dominant gate is geopolitical and therefore **unresearchable**,
which argued for *sizing* rather than waiting — **AVGO's primary gate is a disclosure
question with a definite answer**: identify the 42% customer and establish whether the
XPU programmes are contracted multi-year.

**When a gate can be resolved by waiting, and the expected return does not compensate
for acting early, the disciplined call is to wait.**

### Red team — concurs, with one scoring dissent

**First name in this harness where the red team does not dissent from the position
decision.** Confidence 0.70, its highest, because its attacks rest on disclosed tier-1
facts rather than unknowable probabilities.

**Dissent (scoring only):** `incremental_roic_and_fcf_per_share` at 11/15 is too
generous — the category asks *"Is long-term FCF per share increasing?"* and *"Is
dilution controlled during growth?"* and the answers are **no** and **no**. At 9/15 the
total is 66, still *Starter / Watch*, verdict unchanged. Recorded for re-examination.

Two points the analyst accepts: **serial-acquirer risk is the business model, not a
tail** — treating VMware dilution as "one-time" at a serial acquirer is a category
error; and the **~6.5% after-hours decline on a +221% AI print** is information about
what is already priced that the file records but does not weigh.

### What would change the decision next

**To `STARTER` (1–2%)** — both answerable:
1. The 42% distributor and its end customers identified, and XPU programmes confirmed
   as contracted multi-year rather than re-bid per generation
2. Q3/Q4 FY2026 **GAAP** actuals confirming the estimated ~$45B FY2026 GAAP net income

Plus at least one of: concentration below ~30%; share count actually falling over four
consecutive quarters; infrastructure software re-accelerating above ~10%.

**To `REJECT`:** concentration above ~45% or the 42% customer in-sourcing; share count
still rising through the AI revenue peak; semiconductor margin below ~55%; a goodwill
impairment.

**Explicitly not a reason to act either way:** price movement alone.

### Next scheduled review

Q4 FY2026 results and the FY2026 10-K (December 2026). Per `policy/monitoring.yaml` the
review checks thesis-critical KPIs only and does **not** evaluate price. Critical KPIs,
in order: single-customer concentration percentage, share count, GAAP segment margins,
and infrastructure software growth.


> 최신 판단: **2026-09-05 / WATCH / 71/100 / INVESTIGATE**. [한글 재평가](re-evaluation-2026-09-05.md)가 아래 과거 서술보다 우선합니다. 아래 원문은 이력 비교를 위해 보존합니다.


# Investment Thesis — AVGO (Broadcom Inc.)

As of: 2026-09-04 · Price: US$357.16 · Position: NONE (`WATCH`)
Prepared under `agents/deep-analyst.md`. Expectation gap and asymmetry are scored by
`agents/valuation.md`, not here.

---

## Sourcing note

Three **tier-1 SEC filings** were supplied:

| Filing | Period | Role |
|---|---|---|
| **10-K FY2025** | FY ended 2025-11-02 | Primary annual source |
| **10-Q Q2 FY2026** | Quarter ended 2026-05-03 | Current-state source |
| DEF 14A | Filed 2026-03-02 | Governance / compensation |

**Important currency caveat:** Broadcom released **Q3 FY2026 results on 2026-09-02**,
two days before this analysis and *after* all supplied filings. Those figures are
**headline-only** — revenue, adjusted EPS and AI revenue, with no GAAP income
statement or segment detail. **The FY2026 GAAP earnings figures in `valuation.json`
are therefore the analyst's own estimates and are the weakest input in this file.**

---

## 1. Structural change and market leadership — 13/15

| | FY2023 | FY2024 | FY2025 | H1 FY2026 |
|---|---|---|---|---|
| Net revenue | $35,819M | $51,574M | **$63,887M** | $41,498M (+38.7%) |
| Operating income | $16,207M | $13,463M | **$25,484M** | $19,351M |

**Q3 FY2026 (released 2026-09-02):** revenue **$29.6B**; **AI semiconductor revenue
$16.7B, +221% YoY, +54% QoQ**. Q4 guidance: **AI semi $21.7B (+236%)**, consolidated
**$34.8B (+93%)**. Combining actuals and guidance, **FY2026 revenue lands near
$105.9B, +65.8%** — and the Q4 AI run-rate annualises to **$86.8B**.

Custom AI silicon (XPU) is the hyperscalers' **structural hedge against merchant GPU
pricing**. Broadcom therefore participates on a different axis from NVDA rather than
as a correlated proxy — it wins precisely when customers want out of merchant economics.

**Scored 13, not 14 like NVDA and TSM**, because Broadcom largely *executes* customer
architectures rather than defining them, and because the software engine has stalled
(below). The stock fell ~6.5% after hours on a +221% AI print — the market already
discounts a demanding path.

## 2. Customer value and product strength — 8/10

| Operating margin | FY2024 | FY2025 | Q2 FY2026 |
|---|---|---|---|
| Semiconductor solutions | 55.7% | 57.6% | **61.8%** |
| Infrastructure software | 65.1% | 76.8% | **78.7%** |

Margins expanding while semiconductor revenue grew **78.5% YoY** is the clearest proof
growth is not bought. Once an XPU design is won, the customer has co-invested
engineering years into the silicon.

Capped at 8 because that value is concentrated in very few relationships, and because
**XPU sockets are re-competed at each generation** — unlike a platform with an
installed software ecosystem.

## 3. Moat trajectory — 10/15

**The lowest moat score of the four names**, and for two measured reasons.

**Concentration is deteriorating fast:**

| | FY2024 | FY2025 | H1 FY2026 |
|---|---|---|---|
| **One distributor customer** | 28% | 32% | **42%** |
| Top five end customers | 40% | 40% | **45%** |
| Distributors overall | — | 48% | **56%** |

A **13-point jump in single-customer share in one year** is the most extreme
concentration trajectory in this harness — worse than NVDA's 12%→22% and TSM's 19%.

**And the second engine has stalled.** Infrastructure software grew +26% in FY2025 but
only **+5.1% in H1 FY2026** and +8.8% in Q2. The VMware subscription conversion is
largely complete. A two-engine story is becoming a one-engine story — and the
remaining engine is the more contestable one.

Against this: semiconductor margin expanding to 61.8%, R&D at 17% of revenue, and AI
revenue +221%. There is no evidence of *contraction* — only of a **narrowing base**.

## 4. Incremental ROIC and FCF/share — 11/15

**The most asset-light business in this harness.** FY2025 capex of **$623M on
$63,887M of revenue — 1.0%** (versus NVDA 2.8%, Samsung ~19%, TSMC 33.4%). Operating
cash flow **$27,537M**, free cash flow **$26,914M**, a **42.1% FCF margin**. Broadcom
is fabless, so wafer capacity risk sits on TSMC's balance sheet, not its own.

**But the per-share test fails, uniquely in this harness:**

| Shares outstanding | FY2023 | FY2024 | FY2025 | Q2 FY2026 |
|---|---|---|---|---|
| | 4,139M | 4,686M | 4,741M | **4,758M** |

**In H1 FY2026 the company repurchased $8,450M of stock and the share count still rose
17M** — SBC of $4,268M (10.3% of revenue) issued more stock than buybacks retired.
Samsung is −1.24%, NVDA −2.3%; Broadcom is up.

*In fairness:* most of the multi-year rise was the **544M shares issued as VMware
currency** — a deliberate one-time M&A decision. Underlying net dilution is nearer
**0.7%/yr** against gross SBC issuance of ~1.8%.

## 5. Management and capital allocation — 7/10

**The VMware playbook works on its own terms:** infrastructure software delivered
**$20,765M of FY2025 operating income on 42% of revenue at a 76.8% margin**, up 49%.
Debt principal was reduced $69,847M → $67,120M → $66,720M while paying $11,142M of
FY2025 dividends.

**But the balance sheet is goodwill.** Goodwill **$97,801M** plus intangibles
**$32,273M** = **$130,074M of the $171,092M asset base (76%)** against equity of
**$81,292M**. **Goodwill alone exceeds book equity by ~$16.5B**; tangible book value is
deeply negative. PP&E is just $2,530M.

**And an unexplained earnings item:** FY2025 **net income ($23,126M) exceeds pretax
income ($22,729M)** because of a **$397M tax benefit**, against a $3,748M provision the
prior year. Combined with $8,062M of acquisition amortisation (32% of operating
income) and $7,570M of SBC, the **GAAP-to-non-GAAP margin gap is ~20 percentage
points**.

## 6. Financial survivability — 8/10

Operating cash flow of $27,537M against **$2,672M of cash interest paid** is ~10x
coverage; cash rose to **$19,628M**. Debt is being reduced, not grown.

Scored 8 rather than 9 because **net debt of ~$47.1B is the only material leverage in
this harness** — Samsung, NVDA and TSM all hold net cash — and because a large goodwill
impairment would eliminate book equity.

**Business-quality subtotal (§1–6): 57/75 — the lowest of the four**
(TSM 66, NVDA 62, 005930 59).

## 7. Key risks and concentration dependencies

**One customer at 42% of revenue, amplified by $47.1B of net debt.** Losing or halving
that relationship is not a margin event — it is a business-model event. The
infrastructure software base (~$28B revenue at 78% margin) is the floor that keeps the
bear from being worse.

The demand behind the concentration is hyperscaler AI capex now funded **from balance
sheet rather than operating cash flow** — per this harness's own screening work.

---

## Earnings quality — why this file uses GAAP

Management guides to non-GAAP. Roughly **half the add-back is SBC**, and SBC is
demonstrably a *real* cost here: **the share count rose despite $8,450M of H1
buybacks.** Every valuation test in this file therefore uses GAAP, with non-GAAP shown
alongside:

| At $357.16 | |
|---|---|
| On **estimated** FY2026 GAAP EPS $9.39 | **38.0x** — highest of the four |
| On estimated FY2026 non-GAAP EPS $12.26 | 29.1x |

---

## Most important unknowns

1. **Identity and contract structure of the 42% customer.** Are the XPU programmes
   contracted multi-year or re-bid per generation? **This gates everything.**
2. Q3/Q4 FY2026 **GAAP** earnings — only headline revenue and adjusted EPS are public.
3. The tax-footnote explanation of the FY2025 $397M benefit.
4. Competitive win rate versus Marvell at the next XPU node transition.
5. Whether buybacks will be sized to offset SBC issuance.

## Evidence that would strengthen the thesis

- Single-customer concentration below ~30%, or multi-year XPU contracts confirmed
- Share count actually falling over four consecutive quarters
- Q3/Q4 GAAP actuals confirming the estimated ~$45B FY2026 GAAP net income
- Infrastructure software re-accelerating above ~10%
- Semiconductor margin holding above 60% through a generation transition

## Evidence that would weaken the thesis

- Concentration above ~45%, or the 42% customer in-sourcing or dual-sourcing
- Share count still rising through the AI revenue peak
- Semiconductor margin below ~55% — sockets defended on price
- Infrastructure software declining rather than merely decelerating
- A goodwill impairment, or market cap sustained below net book value

---

## Why WATCH — and why that differs from NVDA and TSM

All four names sit at `INVESTIGATE`. What separates them is the **size of the gap**
and **what kind of question is open**.

| | 005930 | NVDA | TSM | **AVGO** |
|---|---|---|---|---|
| Score | 69 | 75 | 79 | **68** |
| Business quality (of 75) | 59 | 62 | 66 | **57** |
| Share count | falling | falling | flat | **RISING** |
| Balance sheet | net cash | net cash | net cash | **net debt $47.1B** |
| Top-customer share | — | 22% | 19% | **42%** |
| GAAP multiple | ~7x | 23x | 40x | **38x** |
| Weighted 5-yr return | +5.8% | +21.2% | +37.9% | **+9.6%** |
| Verdict | WATCH | STARTER | STARTER | **WATCH** |

The expectation gap here is **positive but the thinnest of the four**, at ~1.8%
annualised expected return.

**And the decisive point:** unlike TSM — whose dominant gate is geopolitical and
therefore *unresearchable*, which argued for sizing rather than waiting — **AVGO's
primary gate is a disclosure question with a definite answer.** Identify the 42%
customer; establish whether the programmes are contracted. That is knowable within one
or two quarters.

**When a gate can be resolved by waiting, and the expected return does not compensate
for acting early, the disciplined call is to wait.** Band `NONE`.

Macro pacing is **slow**: the AI-capex complex remains a single correlated exposure per
the 2026-09-04 screening run.
=======

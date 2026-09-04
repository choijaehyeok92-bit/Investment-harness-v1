# Decision History — 012450 한화에어로스페이스

Append-only. Do not erase prior decisions.

## 2026-09-04 — Initial underwriting

- **Decision:** `REJECT` · **Position band:** `NONE`
- **Total score:** **47 / 100** — *Reject* (business quality **41/75**; expectation gap
  3/15; asymmetry 3/10)
- **Hard Veto status:** `INVESTIGATE` — **no FAIL**. Three HIGH-severity items:
  `external_capital_dependence`, `incremental_roic_collapse`,
  `price_requires_unrealistic_bull_case`
- **Red team:** **`REVISE`** — confidence 0.50, disputes the *confidence* not the
  direction
- **Macro pacing:** `company_specific` · **Decision confidence:** 0.65

### Source basis

Two tier-1 DART filings: **반기보고서** (제50기 반기, 기준일 2026-06-30, 제출
2026-08-14) — all decisive figures — and the **[정정]영업보고서** (FY2025, 2026-03-19),
used for context only. Share price is press-sourced.

### The screening run was wrong about what this company is

The 2026-09-04 screen ranked 012450 **fifth for deep work** as a European-rearmament
defence play *"uncorrelated with AI capex."* The filings show that by revenue it is now
**64% shipbuilding**: H1 2026 해양 KRW 9,614.2B (63.91%) against 방산 KRW 4,465.2B
(29.68%) — and marine has overtaken defence on operating profit too. Correcting that
misidentification is the main work of this analysis.

Also flagged: the FY2024→FY2025 revenue jump from KRW 11.24T to KRW 26.70T (+137%) is
**not organic** — it is the consolidation of Hanwha Ocean.

### The decisive finding — cash

**H1 2026 operating cash flow was NEGATIVE KRW 370.7B** against **POSITIVE
KRW 1,014.3B** in H1 2025 — a KRW 1.39T swing — while reporting **KRW 2,004.4B of
operating profit**. Investing consumed a further KRW 3,403.0B. Borrowings rose
**KRW 12.39T → KRW 15.44T (+24.6%)** in six months. Interest of KRW 264.7B was paid
out of financing, not operations.

This follows a **13.1% dilution in 2025** — 5,982,240 new shares (1,715,040
third-party placement 2025-04-29; 4,267,200 rights issue 2025-07-10). **Equity raised,
then debt raised, while operations consumed cash.**

**Resolves the screening's PRIMARY GATE** (`persistent_dilution`): confirmed at 13.1%,
but a **discrete 2025 event** — the count has been flat at 51,563,401 for twelve
months. That is why it reads MEDIUM, not HIGH.

### The moat leg is shrinking

Defence revenue **−14%** versus the FY2025 half-year run-rate **and** defence margin
**21.9% → 20.2%**, while lower-moat marine grows. Mix went marine 54.5% → 63.9%,
defence 38.9% → 29.7% in twelve months.

### What is genuinely good

Order backlog **KRW 114.92T — about 3.8 years of revenue**, defence alone KRW 46.85T.
Group operating margin **11.6% → 13.3%**; marine margin **7.7% → 12.0%**. And
non-controlling interests take ~44% of profit, so the parent's economic exposure to
marine is smaller than consolidated revenue implies.

### Why the price makes it REJECT

Market cap **KRW 64.14T** = **5.35x** owners' equity (BPS KRW 232,703) and **35.8x**
H1 2026 annualised owners' earnings. Reverse-engineered, even a generous 22x requires
owners' net income to rise ~60% and stay there; at 15–18x it requires a doubling.

| Scenario | 5-yr return |
|---|---|
| Bear (30%) | −81% to −72% |
| Base (50%) | −44% to −30% |
| **Bull (20%)** | **+9% to +40%** |
| **Weighted** | **≈ −37%** (−8.7%/yr) |

**The only negative expected return in this harness**, and robust to reweighting —
even at bear 0.15 / base 0.45 / bull 0.40 it stays around −18%. **The bull case barely
beats cash.**

REJECT is a statement about the **investment at this price**, not about the company.
**No veto reads FAIL** — the label follows the score and the negative expected return.

### Harness comparison

| | 005930 | AVGO | NVDA | TSM | **012450** |
|---|---|---|---|---|---|
| Score | 69 | 68 | 75 | 79 | **47** |
| Business quality (of 75) | 59 | 57 | 62 | 66 | **41** |
| Operating cash flow | positive | positive | positive | positive | **NEGATIVE** |
| Balance sheet | net cash | net debt | net cash | net cash | **net debt, CR 1.08** |
| Weighted 5-yr | +5.8% | +9.6% | +21.2% | +37.9% | **−36.6%** |
| Verdict | WATCH | WATCH | STARTER | STARTER | **REJECT** |

### Red-team dissent — REVISE, and it is a fair hit

The red team returns **REVISE**, not PASS: the analysis reaches a strong, fairly
permanent label on evidence it itself calls incomplete. Its central point stands:

**FY2025 full-year operating cash flow was available in the supplied
[정정]영업보고서 and was not extracted.** That is the decisive number for the
`external_capital_dependence` gate and it was on hand. Recorded as the file's real
weakness.

It also argues, fairly, that (a) one negative half-year against a positive prior half
in a percentage-of-completion business may be timing; (b) the REJECT is a **valuation
disagreement with the market**, not an informational edge, and should say so; and
(c) the base case never models marine *sustaining* 12% margins if US naval MRO proves
structural.

**Not disputed by the red team:** the shipbuilding misidentification, the defence
decline on both revenue and margin, the 13.1% dilution, and that leverage plus negative
cash generation plus a cyclical revenue majority is the weakest combination in this
harness.

### What would change the decision

**To `WATCH` or better** — one prerequisite above all:
- **FY2025 full-year and H2 2026 operating cash flow turning clearly positive**,
  establishing that negative H1 2026 OCF was contract-asset timing. **Without this
  nothing else matters.** Extract it from the supplied [정정]영업보고서 at the next
  review.

Then: defence revenue and margin re-accelerating on order intake; borrowings stabilising
without a further raise; marine margin sustaining ≥12%; and the KRW 1.42T capital
surplus movement explained.

**Confirming the REJECT** (moving `external_capital_dependence` to **FAIL**, making it
veto-driven rather than score-driven): FY2026 full-year operating cash flow negative;
any further equity raise; defence **backlog** declining; borrowings above ~KRW 18T or
current ratio below 1.0.

**Explicitly not a reason to act either way:** price movement alone.

### Next scheduled review

**Immediate follow-up warranted** rather than the normal quarterly cadence — extract
FY2025 operating cash flow from the [정정]영업보고서 already on hand. Then Q3 2026
분기보고서 (November 2026): operating cash flow first, then defence order intake,
marine margin, and borrowings.

---

## 2026-09-04 (same-day correction) — red-team premise checked, two corrections applied

- **Decision:** `REJECT` · **Band:** `NONE` — **unchanged**
- **Total score:** 47 → **48 / 100** — still *Reject*
- **Red team:** `REVISE` → **`PASS`** (withdrew one of its two grounds)
- **Decision confidence:** 0.65 → 0.62

### Correction 1 — the red team's premise was false

The red team returned `REVISE` partly on the ground that FY2025 operating cash flow
*"was provided and the analyst did not extract it."*

**That is wrong.** The supplied **[정정]영업보고서 is an image-based PDF** — text
extraction returns only the correction notice and page markers, with no financial
statements. The **반기보고서 carries only H1 comparatives** (H1 2026 vs H1 2025), not
FY2025 full-year figures. **The number is not obtainable from anything supplied.**

The substantive point stands — it is decisive and unknown — but it is a **sourcing
gap, not an analytical failure**. The red team has withdrawn the accusation and
upgraded to `PASS`.

**Bonus resolution:** the March 2026 amendment changed **기업결합 사항, 타회사
출자현황 and the 이사회 결의서** — administrative items, **not a restatement**. That
closes one of the two `management_or_accounting_integrity` concerns.

### Correction 2 — the leverage characterisation was too harsh

FACT (tier-3, KIS Rating): **net debt/EBITDA 1.6x at 2025-09-30** with financial
coverage rated *excellent*; on the current annualised run-rate, roughly **1.2–1.3x**.
**That is conservative leverage by any conventional standard.**

`financial_survivability` raised **6 → 7**; total 47 → **48**. The earlier draft's
"weakest survivability in the harness" framing overstated the debt problem.

**The genuine concern is narrower and unchanged:** not solvency or debt quantum, but
**cash conversion** — a 1.08 current ratio and negative operating cash flow while
borrowings rose 24.6% in six months. That sits in category 4 and under
`external_capital_dependence`, where it belongs.

### What did not change

Score 48 remains firmly in the Reject band. Probability-weighted five-year return of
about **−37%** is unaffected — it was never driven by the leverage level. The
misidentification (64% shipbuilding, not a defence play), the shrinking defence leg,
the 13.1% dilution, and the negative operating cash flow all stand.

### Accepted framing, now on the record

The `REJECT` is a **valuation disagreement with the market**, not an informational
edge. The market pays 5.35x book and 35.8x earnings because it prices a KRW 114.9T
backlog and a decade of European rearmament. Disagreeing with that discount rate is
legitimate; claiming an edge would not be.

### Primary gate — restated with the sourcing reality

**FY2025 and FY2026 full-year operating cash flow.** It **cannot** be obtained from
the documents supplied. The FY2025 사업보고서 or the audited cash flow statement is
required. Until then the `external_capital_dependence` veto stays at `INVESTIGATE`
rather than resolving either way.

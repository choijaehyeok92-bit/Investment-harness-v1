# Decision History — 005930 삼성전자

Append-only. Do not erase prior decisions.

## 2026-09-04 — Initial underwriting

- **Decision:** `WATCH`
- **Position band:** `NONE`
- **Total score:** 66 / 100 — *Starter / Watch* (business quality 55/75; expectation gap 6/15; asymmetry 5/10)
- **Hard Veto status:** `INVESTIGATE` — no FAIL. Two open items:
  - `incremental_roic_collapse` — **HIGH** severity, the primary gate
  - `price_requires_unrealistic_bull_case` — MEDIUM
  - `fatal_concentration` — MEDIUM
  - Six vetoes PASS, including `moat_shrinkage` (direction positive) and
    `management_or_accounting_integrity` (Supreme Court acquittal confirmed 2025-07-17)
- **Expectation gap:** Thin. Price requires sustained mid-cycle operating profit of
  KRW 145–180T, some 2.5–3.1x the prior all-time peak of KRW 58.9T (2018).
  Probability-weighted 5-year return ≈ +11% total (≈2.2%/yr) on explicitly
  subjective weights of bear 0.30 / base 0.50 / bull 0.20.
- **Asymmetry:** Low permanent-loss risk (3–5% subjective) but structurally capped
  upside. At ≈KRW 1,634T of equity value a power-law outcome is arithmetically
  implausible. Bull ≈ +70–105% over five years.
- **Macro pacing:** `slow` — per `policy/macro-overlay.yaml` this adjusts pacing
  only and did **not** alter any company score. Rationale: the AI-capex complex is
  treated as a single correlated exposure, and Samsung's end demand sits inside it.

### Evidence change since prior review

First underwriting; the prior state is the `screening/2026-09-04` run, which
returned `SCREEN_IN` and ranked this name **#1** for deep work.

**Material correction to that run.** The screen argued the price did not require the
cycle peak to persist, resting on a broker figure of ~1.4x forward P/B. That figure
appears to reference 2025 and is stale. Corrected forward P/B is ≈**2.29x**
(2026E BPS KRW 109,313 against KRW 250,000), at or above the top of Samsung's
historical 0.9x–2.1x range and computed on peak-inflated book. This removes the
screen's central valuation argument in the strong form it was stated.

**New evidence not available at screening**, from the user-supplied tier-1 DART
filing of 2026-08-21 and follow-up research:

- KRW 222.6T distributable-profit headroom; KRW 254.3T separate-basis net assets *(tier-1)*
- 2026 shareholder return of KRW 90–110T approved — >5x the prior record — a 5.5–6.7% yield
- The KRW 15T buyback in the filing is for **employee share compensation, not
  cancellation** — it offsets dilution rather than reducing share count
- Real cancellation did occur separately: 73,359,314 common + 13,603,461 preferred
  on 2026-04-02 (≈KRW 14.58T), common outstanding −1.24%
- Samsung passed HBM4 qualification at NVIDIA and AMD **first**, on the Rubin
  platform; SK hynix HBM4 slipped to Q3 2026 on interface sync issues
- Industry 2027 capex projected at US$146B, ≈3.4x 2024 — the primary bear mechanism
- Lee Jae-yong acquittal confirmed by the Supreme Court on 2025-07-17, closing the
  integrity veto

### Thesis change versus the screening run

Business quality is **stronger** than the screen assumed — the HBM4 qualification
lead and the competitor's stumble are more decisive than the share numbers alone
conveyed. The **expectation gap is materially thinner** than assumed. Net effect:
the name is a better *business* and a worse *investment* than the screen concluded.

Direction of travel is favourable; the price for it is not yet.

### Why WATCH rather than STARTER or REJECT

- Not `STARTER`: `Hard Veto > Score`. The HIGH-severity `incremental_roic_collapse`
  gate is open, and the industry is committing US$146B of 2027 capex at the peak.
- Not `REJECT`: no veto reads FAIL, business evidence direction is positive, and
  permanent-loss risk is low.
- Score 66 sits in the *Starter / Watch* band. **This is a close call.** It rests on
  subjective probability weights: at bear 0.20 / base 0.50 / bull 0.30 the weighted
  return is ≈+30% and the total rises to 68–69, which would support a `STARTER`
  position. Recorded so a future reviewer can see exactly what judgement was made.

### Red team

Verdict `PASS`, confidence 0.65. Required revision before any position: re-score
`moat_trajectory` after Q4 2026, decomposing the 21%→33% HBM share move into Samsung
advance versus SK hynix retreat. If mostly the latter, moat trajectory falls to
~7/15 and the total drops below the Reject boundary.

### What would change the decision next

**To `STARTER` (1–2%)** — the primary gate must close first: a completed normalised
mid-cycle earnings model showing operating profit durably above ~KRW 180T against
the announced 2027–2029 capacity additions. Then at least two of:
HBM share ≥33% in Q4 2026 *after* SK hynix HBM4 volume arrives; disclosure of
multi-year capacity-reserved HBM contracts; January 2027 board delivering the return
materially as buyback-and-cancel exceeding the KRW 15T employee tranche; foundry
sustained quarterly operating profit with a second large external customer.

**To `REJECT`** — HBM share below 28% once SK hynix HBM4 reaches volume; or contract
prices rolling over while 2027 capex is still being spent; or CXMT demonstrating
leading-edge DRAM at volume.

**Explicitly not a reason to act either way:** price movement alone. Per
`policy/position-sizing.yaml` and `policy/monitoring.yaml`, a further decline does
not create a position and a rally does not remove one.

### Next scheduled review

Q3 2026 results (late October 2026) — per `policy/monitoring.yaml` quarterly review
checks thesis-critical KPIs only and does **not** evaluate price. Critical KPIs:
HBM share, HBM4 volume at NVIDIA, foundry operating result, capex guidance.

---

## 2026-09-04 (revision) — 반기보고서 tier-1 evidence incorporated

- **Decision:** `WATCH` — **unchanged**
- **Position band:** `NONE` — **unchanged**
- **Total score:** **66 → 68** / 100 — still *Starter / Watch*
  (business quality 55 → 57 / 75; expectation gap 6/15 and asymmetry 5/10 unchanged)
- **Hard Veto status:** `INVESTIGATE` — unchanged. `incremental_roic_collapse`
  remains the HIGH-severity primary gate.
- **Red team:** `PASS`, confidence **0.65 → 0.70**

### Evidence change since prior review

New source: **`삼성전자 2026년 반기보고서` (제58기 반기, 2026-06-30), DART — tier-1.**
Supplied by the user as two Google Drive links; the files are identical (same title
and byte size), so this is one document, not two.

The filing cut both ways, with the two principal findings of comparable weight.

**Favourable — Samsung is harvesting the cycle, not racing it**

| H1 | 2026 | 2025 | Δ |
|---|---|---|---|
| Operating cash flow | KRW 145.36T | KRW 33.94T | +328% |
| Tangible capex | KRW 31.23T | KRW 26.83T | +16.4% |
| Free cash flow | KRW 112.39T | KRW 5.07T | 22x |

This corrects a real error. The prior version scored category 4 down for "enormous
capital absorption" and applied the industry's projected US$146B of 2027 capex to
Samsung's own conduct. Operating cash flow grew twenty times faster than capex.
FCF/share ≈ KRW 17,116 in the half year — a 13.7% annualised yield at KRW 250,000.
**Category 4 raised 10 → 12.**

Also resolved: **net cash KRW 167.54T** (previously unknown), **controlling-interest
equity KRW 565.06T** (previously unknown), and share counts confirmed *exactly* as
derived before this document was available. H1 treasury purchases of KRW 13,248,625M
reconcile precisely to the 2026-08-21 filing — an independent tier-1 cross-check.

**Favourable — an internal hedge not previously credited.** DX operating margin fell
6.8% (FY2025) → 2.1% (H1 2026): Samsung's own set business absorbs the memory rent.
On normalisation DX recovers as DS falls. SK hynix and Micron have no such offset.
Bear floor improves from ≈−50% to ≈−45%.

**Unfavourable — the surge is price, and it is now a fact.** Memory ASP **+220%** in
H1 2026 vs the FY2025 average (smartphone +7%, OLED +1%, TV −4%, digital cockpit −3%).
Converts the cycle-peak argument from INFERENCE to FACT.

**Unfavourable — concentration measured, not inferred.** DS produced KRW 142.86T of
the group's KRW 146.73T H1 operating profit — **97.4%**, at a **68.3%** divisional
margin. DS margin history: 13.6% (FY2024) → 19.1% (FY2025) → 68.3% (H1 2026).

**Unfavourable — second P/B correction, same direction.**

| Estimate | Basis | Forward P/B |
|---|---|---|
| Screening run | stale broker figure (2025 reference) | ~1.4x |
| First deep analysis | broker year-end BPS est. KRW 109,313 | ~2.29x |
| **This revision** | **measured book, tier-1** | **~2.89x current / ~2.51x fwd** |

Every successive correction has moved in the same direction. Recorded explicitly as
a pattern, and flagged by the red team as a one-directional bias rather than noise.
The one remaining unverified input — preferred-share price, ESTIMATE KRW 215,000 —
sits in the same category.

### Thesis change

Business quality is **confirmed stronger** than the prior version credited; the
capex-discipline finding removes a bear argument that was mis-specified. The
valuation categories are **unchanged**, because the ASP and P/B findings offset the
cash-flow findings almost exactly. Probability-weighted five-year return improves
from ≈+11% to ≈**+15% total (≈2.8%/yr)** — still below a Korean risk-free rate.

The EV/EBIT method, now computable with real net cash, independently reproduces the
required normalised operating profit range of **KRW 147–183T** against the
equity-based KRW 145–180T. **The conclusion is robust to method.**

Cleanest formulation on measured figures: at ≈2.5x forward book the price requires
**sustainable through-cycle ROE near 25%** versus a 2010s average of 12–15%; H1 2026
annualised ROE was ≈47.9%. The price requires roughly **half** of the current return
on equity to be permanent.

### Why the decision did not change

The position stays at zero **not because of doubt about the business — which this
filing largely settles — but because of expected return.** The primary gate is still
open, and Samsung's own capex restraint does not close it: industry supply sets the
price Samsung receives, and a 68.3% divisional margin is a rent.

This is now a **closer call** than at initial underwriting. Evidence quality improved
materially and the downside is better established (−45% drawdown against a solvent,
cash-generative business with KRW 167.54T of net cash). A reasonable analyst could
take a `STARTER` position here. The judgement that holds it at `NONE` is the
subjective probability weighting, which is disclosed in `valuation.json`.

### Scope note

Note 27 (segment reporting), Note 29 (subsequent events) and Section 6 (dividends)
were beyond the retrieved text extract of the filing and were **not read**. Segment
figures used above come from Section II-7-라 (사업부문별 요약 재무 현황), which was
within the extract.

### What would change the decision next

Unchanged from initial underwriting, plus two additions:

- **New increase trigger:** full-year capex landing near the H1 run-rate
  (≈KRW 62–70T annualised) rather than stepping toward the announced KRW 110T+
  programme — confirming H1 restraint is policy, not timing.
- **New exit trigger:** capex stepping up sharply in H2 2026 / 2027 while memory ASP
  rolls over — the combination that confirms `incremental_roic_collapse`.
- **Counter-intuitive, worth stating:** a *further* memory ASP spike is bad news, not
  good. It raises the rent being capitalised and deepens the eventual reversion.

---

## 2026-09-04 (revision 2) — FY2025 사업보고서 tier-1; normalisation baseline established

- **Decision:** `WATCH` — unchanged · **Position band:** `NONE` — unchanged
- **Total score:** **68 → 69** / 100 — *Starter / Watch*
- **Hard Veto:** `INVESTIGATE` — unchanged; `incremental_roic_collapse` **materially advanced but not closed**
- **Red team:** `PASS`, confidence **0.70 → 0.78**
- **Decision confidence:** 0.65 → **0.72**

### Evidence change

New source: **`삼성전자 사업보고서 제57기` (FY2025, filed 2026-03-10), DART — tier-1.**

**Against the position — the primary gate finally has its baseline.**

DS operating margin, full cycle: **−22.3% (FY2023, a KRW 14.88T LOSS) → 13.6%
(FY2024) → 19.1% (FY2025) → 68.3% (H1 2026)** — roughly a KRW 158T swing in
half-year-equivalent profit in three years. Memory ASP: **+14% FY2025, +220% H1 2026,
≈3.65x FY2024 compounded** in eighteen months.

First-pass normalisation, on assumptions tilted toward the company (DS revenue
KRW 250–300T at 30–38% margin): **group normalised operating profit KRW 93–132T
versus a price requirement of KRW 145–183T.**

**The expectation gap is negative, not merely thin** — a change in kind from the two
prior reviews. `expectation_gap_and_valuation` 6/15 → **5/15**; bear weight 0.30 →
**0.35**; weighted five-year return **+14.9% → ≈+8.4%** total (1.6%/yr).

**For the position — genuinely, and I had under-weighted both.**

- **1,934,188,242 common shares cumulatively retired — 24.9% of all ever issued**
  (plus 392,300,147 preferred), across many cycles. Materially offsets the
  "buying at the peak" criticism, which judged a multi-decade policy on one tranche.
- **FY2025 investment of KRW 90.4T** (capex 52.65 + R&D 37.75) against **KRW 43.6T**
  of operating profit — 2.07x — sustained through the FY2023 DS loss. The 2026
  windfall was pre-funded.
- Categories 4 (12 → **13**) and 5 (7 → **8**) raised.

**Self-correction:** the DX hedge, described in revision 1 as raising the bear floor,
is now sized at **KRW 8–10T/yr against a DS swing exceeding KRW 150T — 6–7%**. The
earlier framing implied more than the data supports.

### Thesis change

**The business is confirmed better than three successive reviews had credited. The
price is confirmed worse.** Business-quality subtotal 57 → **59/75**; valuation
categories 11 → **10/25**.

Unlike revision 1, this is **no longer a close call on subjective weights** — the
normalised model lands below the requirement on generous assumptions. Decision
confidence rises accordingly.

Stated fairly: the gate is closed against the current **price**, not against the
company. At DS revenue near KRW 320T and a margin above 40%, the requirement is met.

### Red-team dissent recorded

The red team argues the normalised model is **still too kind**: DS revenue of
KRW 250–300T is ~2x FY2025 and embeds a permanently larger market at the outset. A
history-anchored mid-cycle (FY2024–25: revenue KRW 111–130T, margin 13.6–19.1%)
gives group operating profit of KRW 35–45T. Recorded as dissent, not adopted — the
AI demand shift is real — but it means **the true bear is worse than the recorded
bear**.

### Scope note

Section III (financial statements), Section 6 (dividends) and the notes were beyond
the retrieved text extract and were **not read**. FY2025 balance-sheet and
income-statement figures come from the interim report's comparative columns. Segment,
ASP, capex, R&D and share-count data are from Section II, within the extract.

### What would change the decision next

- **To `STARTER`:** the normalised model must rise above ≈KRW 145T of group operating
  profit on defensible assumptions — requiring disclosed multi-year capacity-reserved
  HBM contract terms, or evidence that normalised DS margin sustains above 40% on
  revenue near KRW 320T. **Absent that, the price must fall to meet the KRW 93–132T
  range.**
- **To `REJECT`:** DS reverting toward the FY2024–25 band faster than modelled,
  putting group operating profit below the KRW 93T lower bound (red-team falsifier F9).
- **Outstanding from initial underwriting:** the `moat_trajectory` re-score after Q4
  2026 — decompose the 21%→33% HBM share move into Samsung advance versus SK hynix
  retreat, discounted for having occurred inside a 220% ASP environment.

---

## 2026-09-04 (revision 3) — FY2025 별도재무제표 (tier-1, pp.194–199)

- **Decision:** `WATCH` — unchanged · **Band:** `NONE` — unchanged
- **Total score:** **69** / 100 — **held** (see "on not raising the score")
- **Hard Veto:** `INVESTIGATE` — unchanged
- **Red team:** `PASS`, confidence **0.78 → 0.80**
- **Decision confidence:** 0.72 → **0.76**

### Evidence change

Source: FY2025 사업보고서 **별도재무제표 4-1~4-5 (pp.194–199)**, supplied as filing
screenshots — the section beyond the earlier text extract.

**For the position.** Parent capex fell **16.2%** across FY2023–25
(KRW 45.03T → 38.25T → 37.75T) while parent operating cash flow doubled
(34.46 → 68.73). The capex discipline is a **three-year pattern**, not one half-year.
SBC quantified at **KRW 0.71T** in FY2025 (zero in FY2023–24), closing a data gap
open since initial underwriting.

**Against the position, and more important.** FY2023 parent operating result was a
**LOSS of KRW 11.53T**; FY2023 segment operating profits sum to roughly **KRW 6.25T**.
Against H1 2026 annualised **KRW 293.45T** that is a **≈47x swing**, three years old.
The modelled bear (KRW 70–90T normalised) is the **modal** bear, not the tail.
Bear return worsened to **−55/−45**; weighted five-year return **+8.4% → ≈+5.5%**
total (**1.1%/yr**).

**Two-edged, recorded as such.** The FY2023–25 underinvestment is part of *why* the
shortage exists; the 2027 industry capex tripling corrects it.

**Verification.** Parent equity **KRW 254,330,083M** matches *to the won* the
2026-08-21 filing's net-asset figure — a **third independent tier-1 reconciliation**.
Method check: parent debt KRW 39.05T > consolidated KRW 25.24T (intercompany loans
eliminate on consolidation), confirming net cash of KRW 167.54T was correctly taken
on a consolidated basis.

### On not raising the score

The capex evidence would support `incremental_roic_and_fcf_per_share` 13 → 14. **It
was held at 13.** The category has already moved 10 → 12 → 13 across two prior
updates, and the red team's critique that consistent one-directional revision is a
bias applies symmetrically to upward moves. Held pending Q4 2026 data. Recorded so a
future reviewer can see the judgement was deliberate.

### Red-team dissent recorded — new

**The dividend baseline reframes the return programme.** The parent dividend was
**KRW 9.81T in each of FY2023, FY2024 and FY2025** — flat, through a swing from
−KRW 11.53T to +KRW 23.6T of parent operating profit. The FY2026 plan of KRW 90–110T
is roughly **10x** that baseline. The red team argues this is more consistent with a
**one-off distribution of windfall rent** than a permanent policy change — in which
case the 5.5–6.7% shareholder yield partly supporting the base case is **not durable
and should not be capitalised**. Recorded as dissent; it sharpens the existing
January 2027 trigger from "dividend vs buyback" to "**does any of it recur at a
normalised earnings level**".

New falsifier **F10**: FY2027 shareholder return reverting toward the KRW 10–20T
historical baseline as memory normalises.

### Expected-return trajectory across four tier-1 documents

| Review | Weighted 5-yr total return |
|---|---|
| Initial underwriting | +11.4% |
| Rev 1 (반기보고서) | +14.9% |
| Rev 2 (사업보고서 §II) | +8.4% |
| **Rev 3 (별도재무제표)** | **+5.5%** |

The single upward move was itself data-driven and was partly reversed by better data.
Every material input is now audited except the preferred-share price.

### Outstanding

Unchanged and now the last open item where the analysis rests on evidence collected
inside the rent: the **`moat_trajectory` re-score after Q4 2026** — decompose the
21%→33% HBM share move into Samsung advance versus SK hynix retreat, discounted for
the +220% ASP environment in which all capacity cleared.

---

## 2026-09-04 (price update) — 보통주 KRW 255,500

- **Decision:** `WATCH` · **Band:** `NONE` · **Score:** **69** — all unchanged
- Price: KRW 250,000 (2026-09-03 close) → **KRW 255,500** (user-supplied, unverified)

### What moved

| | KRW 250,000 | KRW 255,500 |
|---|---|---|
| Total equity value | 1,634T | **1,670T** |
| Enterprise value | 1,467T | **1,502T** |
| P/B (2026-06-30 book 565.06T) | 2.892x | **2.955x** |
| Annualised P/E | 6.98x | **7.14x** |
| Annualised FCF yield | 13.7% | **13.4%** |
| **Required normalised OP** | 147–183T | **150–188T** |
| Model normalised OP | 93–132T | **93–132T (unchanged)** |
| **Shortfall** | — | **≈18–95T, widened** |

Weighted five-year return **+5.5% → +4.0%** (0.8%/yr). Two causes, separated: about
−1.5pp from the higher price, the remainder from a **precision fix** — the bear range
previously read "−55 to −45", conflating the modal bear (equity KRW 850–950T) with
the deep tail. Modal bear at the new price is **−49% to −43%**; the deep tail sits
below and outside that range.

### What did not move, and why

**Nothing about the business changed.** `expectation_gap_and_valuation` was **held at
5/15**: the gap moved against the position, but a 2.2% price tick is not a basis for
re-scoring, and the category already reflects a negative gap.
`policy/monitoring.yaml` and `policy/position-sizing.yaml` both forbid letting price
alone drive the decision — in either direction.

### Price at which the gap closes — computed

Solving for the common price where required normalised OP meets the KRW 93–132T
model range, at 8–10x mid-cycle EV/EBIT, using the **measured** preferred/common
ratio of 0.7205:

**Range KRW 142,000–232,000 · central estimate ≈ KRW 183,700** (9x on the KRW 112.5T
midpoint) — about **28% below** KRW 255,500.

This is **not a target price** and must not be used as one. It is the level at which
the normalised model would stop being an argument against a position; the
`incremental_roic_collapse` gate would still need separate resolution.

**Corrections logged.** An early draft of `decision.json` asserted KRW 150,000–165,000
without computing it — wrong. A computed version using the *estimated* preferred ratio
of 0.860 gave a central KRW 180,538. The table above, on the measured ratio, supersedes
both.

---

## 2026-09-04 (preferred price resolved) — 삼성전자우 KRW 184,100

- **Decision:** `WATCH` · **Band:** `NONE` · **Score:** **69** — all unchanged

**The last unverified valuation input in this file is now closed.** Every material
input is either audited tier-1 or a supplied market price.

The measured preferred/common ratio is **0.7205 (a 27.9% discount)** against the
**0.860 (14.0%)** assumed — the estimate was **19.3% too high**.

| | Estimated preferred | **Measured preferred** |
|---|---|---|
| Preferred market cap | 176.28T | **147.72T** |
| Total equity value | 1,670.01T | **1,641.44T** (−1.7%) |
| Enterprise value | 1,502.47T | **1,473.90T** |
| P/B (book 565.06T) | 2.955x | **2.905x** |
| Forward P/B | 2.57x | **2.525x** |
| Required normalised OP | 150–188T | **147–184T** |
| Shortfall vs model 93–132T | 18–95T | **15–91T** |
| Weighted 5-yr return | +4.0% | **+5.8%** (1.1%/yr) |

### Why the verdict does not change

A 1.7% revision to a valuation input does not move a category that already reflects a
**clearly negative** expectation gap. The shortfall against the normalised model is
still KRW 15–91T. Score held at 69; `expectation_gap_and_valuation` held at 5/15.

### One thing worth recording about direction

This is the **first valuation input in this file to resolve in the company's favour.**
Every prior correction moved against the position — three successive P/B revisions
(1.4x → 2.29x → 2.89x), the memory ASP finding, the FY2023 trough. The red team
flagged that pattern as possible **one-directional bias rather than noise**.

That the last remaining estimate moved the *other* way once measured is weak but real
evidence the earlier corrections were data-driven rather than a drift. Recorded so a
future reviewer can weigh it.

### Outstanding

Only one item remains open across the whole file: the **`moat_trajectory` re-score
after Q4 2026** — decompose the 21%→33% HBM share move into Samsung advance versus
SK hynix retreat, discounted for the +220% ASP environment in which all capacity
cleared. Every valuation input is now resolved.

## 2026-09-05 — Astra 재심사

- 과거: 69; 현재: 68/100, WATCH, INVESTIGATE, 포지션 밴드 NONE.
- DS 마진의 전년·전전년 대비 급등은 기술 우위와 메모리 가격효과를 분리해야 한다. Capex와 R&D 지출 합계는 투입액이지 증분 ROIC 자체가 아니므로 재투자 점수를 13→12로 조정한다.
- [현재 재평가](re-evaluation-2026-09-05.md). 이전 판정은 역사이며 주문·거래는 실행하지 않았다.

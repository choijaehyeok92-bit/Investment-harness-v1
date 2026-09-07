> 최신 판단: **2026-09-05 / WATCH / 68/100 / INVESTIGATE**. [한글 재평가](re-evaluation-2026-09-05.md)가 아래 과거 서술보다 우선합니다. 아래 원문은 이력 비교를 위해 보존합니다.

# Investment Thesis — 005930 삼성전자 (Samsung Electronics)

As of: 2026-09-04 · Price: KRW 250,000 (common, 2026-09-03 close) · Position: NONE
Prepared under `agents/deep-analyst.md`. Scores for expectation gap and asymmetry are
set by `agents/valuation.md`, not here.

---

## Sourcing note

The trigger document for this analysis is a **tier-1 primary filing** —
`주요사항보고서 / 자기주식 취득 결정`, DART, 2026-08-21. Under
`policy/source-policy.yaml` that outranks every other source used here. Everything
traceable to it is marked **FACT (tier-1)**. Company IR releases are tier 2; press
and broker figures are tier 3–5 and are marked ESTIMATE where they are not
independently corroborated.

**Updated 2026-09-04** with `삼성전자 2026년 반기보고서` (제58기 반기, 2026-06-30) —
also tier-1. Two of the three inputs previously recorded as unknown are now
resolved: **consolidated net cash (KRW 167.54T)** and **controlling-interest equity
(KRW 565.06T)**. One remains unverified: the preferred-share price (ESTIMATE
KRW 215,000), which moves total equity value by roughly ±KRW 20T per KRW 25,000.

Note 27 (segment reporting), Note 29 (subsequent events) and Section 6 (dividends)
were beyond the retrieved text extract of the filing and were **not read**.

---

## 1. Structural change and market leadership — 11/15

AI accelerator demand has structurally repriced memory. The scale is easy to
understate: **Q2 2026 revenue of KRW 171.5T exceeds half of FY2025's entire
revenue of KRW 333.61T**, and H1 2026 operating profit of KRW 146.7T is 3.4x the
full-year FY2025 figure of KRW 43.60T.

Samsung's position inside that change improved decisively in 2026. It passed final
**HBM4 qualification at NVIDIA and AMD first**, began shipping in Q2 2026, and
secured a position on the NVIDIA Rubin platform. When customers raised the HBM4
speed requirement in Q4 2025, Samsung's part passed **without a redesign** because
it had been specified at top speed — that is engineering headroom, not luck.

The score is 11 and not higher because Samsung is a *recovering* leader, not the
category definer. It forfeited HBM leadership entirely for roughly three product
generations; SK hynix defined HBM. Foundry remains a distant second to TSMC, whose
Q2 2026 revenue was US$40.20B with 7nm-and-below at 77% of wafer revenue.

**The under-appreciated structural point:** Samsung is the only company holding
leading-edge memory, logic foundry and advanced packaging under one roof. As the
HBM base die becomes a logic product, that integration is a position neither
SK hynix, Micron nor TSMC can replicate. It is the strongest argument in the bull
case and it is not yet reflected in reported numbers.

## 2. Customer value and product strength — 7/10

HBM is a hard bottleneck on accelerator performance, and memory is now capturing a
rising share of system value — Meta explicitly cited **memory pricing** when raising
its 2026 capex guidance to $125–145B from $115–135B. Passing a raised speed
specification without redesign is real, quantifiable customer value.

The cap at 7 is deliberate. Stickiness here is **qualification-based, not
preference-based**: it resets at each generation. That is precisely how Samsung lost
HBM3E and precisely how it is now regaining share at HBM4. And customers' revealed
preference actively works against Samsung — hyperscalers *want* multiple qualified
suppliers in order to break memory pricing power.

## 3. Moat trajectory — 11/15

`policy/scorecard.yaml` asks one question: will the moat be wider in five years?
`agents/deep-analyst.md` requires direction over level. Direction is clearly positive:

| Signal | Direction |
|---|---|
| HBM share (Counterpoint) | 21% Q1'26 → **33%** Q2'26 |
| SK hynix HBM share | 64% a year earlier → **50%** |
| HBM4 qualification | Samsung **first**; SK hynix slipped to Q3'26 on interface sync issues |
| HBM4 yield | approx. **80%** (TrendForce, Aug 2026) |
| Foundry utilisation | **>80%** in Q1'26, highest in about a year |
| Foundry breakeven | pulled forward **2027 → 2026** |

Two honest deductions keep this at 11 rather than 13+.

**Source conflict, disclosed.** Counterpoint reports Q2 2026 as SK hynix 50% /
Samsung 33%. A separate report cites Samsung 38% / SK hynix 25%, which appears to
conflate a *year-end target* with an actual. Counterpoint is preferred — a named
house with a consistent quarterly series, corroborated by Businesspost. Direction
agrees across sources; level does not.

**A gain partly caused by a competitor's stumble is not yet a durable lead.**
SK hynix's HBM4 delay is a real cause of Samsung's Q2 gain. The test is whether
Samsung holds ≥33% *after* SK hynix reaches HBM4 mass production. That is the
single cleanest falsifier in this thesis.

## 4. Incremental ROIC and FCF/share — 10/15

**What supports it.** Share count is genuinely falling: on 2026-04-02 Samsung
cancelled 73,359,314 common and 13,603,461 preferred shares (approx. KRW 14.58T),
taking common outstanding from 5,919,637,922 to **5,846,278,608 (−1.24%)** — a
figure cross-verified against the tier-1 filing's statement that 1% of common
equals 58,462,786 shares. The 2026-08-21 board then approved a **KRW 90–110T**
shareholder return, over 5x the prior record of KRW 20.3T (2020), a **5.5–6.7%
one-year yield** on approximately KRW 1,634T of total equity value.

**What contradicts it, and it is serious.** Capital absorption is enormous:
KRW 110T+ of planned facility and R&D investment, Pyeongtaek P5 fab1 at KRW 60T+
with fab2 similar (2029), and a US$37B Taylor commitment. Industry-wide, combined
2027 capex for Samsung, SK hynix and Micron is projected at **US$146B — about 3.4x
the US$43B of 2024**, with meaningful shipment expansion arriving from H2 2027.
This is the exact mechanism by which memory incremental ROIC has collapsed in every
prior cycle, and it is being committed *now, at the peak*.

**A distinction that matters and is easy to miss.** The KRW 15T buyback in the
trigger filing is for **employee share compensation** — performance incentives and
performance-conditioned stock — and is explicitly **not for cancellation**. At the
KRW 281,500 reference price that is 53,285,968 shares, about 0.91% of common per
year. It offsets dilution; it does not reduce share count. It also marks a real
policy change, converting what was historically cash bonus into equity. Counting it
as shareholder return would overstate the FCF-per-share case.

## 5. Management and capital allocation — 7/10

Returns are being **executed, not announced**: KRW 14.58T of stock was actually
cancelled on 2026-04-02, and the trigger filing is the *confirmed* version of a
June 2026 press report the company had twice answered only as unconfirmed. Two
long-standing operational failures are being corrected under current management —
HBM competitiveness and foundry. Legal overhang is closed: on **2025-07-17** the
Supreme Court confirmed acquittal on all 19 charges relating to the Samsung C&T /
Cheil Industries merger and Samsung Biologics accounting.

Against that: the three-generation HBM miss was itself a capital-allocation and
roadmap failure by the same organisation, and the base rate is not erased by the
recovery. **Repurchase price discipline is an explicit scorecard indicator, and
buying back stock at a cyclical earnings peak — when the share price embeds peak
book — is the weakest point in the buyback cycle.** Public reporting on the
multi-year commitment also conflicts (a June report described KRW 90T of buyback
over three years; three-year totals are separately reported at KRW 120–140T against
KRW 90–110T for 2026 alone). These cannot all be right; recorded as unresolved.

## 6. Financial survivability — 9/10

**FACT (tier-1):** distributable-profit headroom of **KRW 222,623,486,825,081**,
from separate-basis net assets of **KRW 254,330,082,981,146**. The KRW 110T+
investment programme and the KRW 90–110T return are funded from operating cash
flow, not external financing. Survivability is simply not the risk here. The risk
is that a fortress balance sheet is deployed into a capex race at the top of a cycle.

**Business-quality subtotal (categories 1–6): 55/75.**

## 7. Key risks and concentration dependencies

- **Profit concentration is extreme.** At a 52.2% company-wide operating margin,
  essentially all incremental profit is semiconductor; within that, memory; within
  that, HBM4 allocation at a few accelerator customers. MX, VD and Harman are no
  longer profit-material at the margin.
- **The end-demand funding source is itself concentrated and deteriorating.**
  Hyperscaler 2026 capex guided above $725B now exceeds those customers' operating
  cash flow — Alphabet posted its first negative-FCF quarter since 2004 and Meta's
  cash generation fell 91% YoY. Samsung's customer is spending from balance sheet.
- **Geopolitical footprint:** Chinese fabs under US export-control policy; a US$37B
  single-site commitment at Taylor.
- **CXMT.** Every scenario here assumes a three-player oligopoly. A state-subsidised
  fourth entrant at leading-edge DRAM would invalidate all of them.

---

## Most important unknowns

1. Normalised mid-cycle operating profit against the announced 2027–2029 capacity
   additions. **Everything depends on this.**
2. Whether HBM's contracted, capacity-reserved structure genuinely dampens cycle
   amplitude or merely delays it.
3. Segment-level DS profit split (DRAM / NAND / HBM / foundry) — not disclosed at
   the granularity required.
4. Preferred-share price and consolidated net cash — both unverified, both material
   to the valuation.
5. Annual SBC expense under the new performance-conditioned stock programme.

## Evidence that would strengthen the thesis

- HBM share holding ≥33% in Q3/Q4 2026 **after** SK hynix HBM4 reaches mass production.
- Disclosure of multi-year, capacity-reserved, price-fixed HBM agreements.
- January 2027 board delivering the return materially as buyback-and-cancel, with
  cancellations exceeding the KRW 15T employee-compensation tranche.
- Foundry posting sustained quarterly operating profit with a second large external
  logic customer at Taylor.

## Evidence that would weaken the thesis

- HBM share reversing toward the low 20s once SK hynix HBM4 volume arrives.
- DRAM or HBM contract prices rolling over while the US$146B of 2027 capex is still
  being spent.
- Capex guidance rising further while operating cash flow falls.
- The return delivered predominantly as dividend while employee buybacks continue,
  leaving net share count flat.
- CXMT demonstrating credible leading-edge DRAM at volume.

---

## Update — 2026 반기보고서 (tier-1), read 2026-09-04

The interim report cut both ways, with the two principal findings of comparable
weight. Score moves **66 → 68**; label, Hard Veto status and position band are
unchanged.

### Favourable — Samsung is harvesting the cycle, not racing it

| H1 | 2026 | 2025 | Δ |
|---|---|---|---|
| Operating cash flow | **KRW 145.36T** | KRW 33.94T | **+328%** |
| Tangible capex | **KRW 31.23T** | KRW 26.83T | **+16.4%** |
| Free cash flow | **KRW 112.39T** | KRW 5.07T | 22x |

**This corrects a real error in the prior version.** That version scored
`incremental_roic_and_fcf_per_share` down for "enormous capital absorption" and
applied the industry's projected US$146B of 2027 capex to Samsung's own conduct.
The filing shows operating cash flow growing **twenty times faster than capex**.
FCF per share was ~KRW 17,116 in the half year — a **13.7% annualised FCF yield**
at KRW 250,000. Category 4 raised **10 → 12**.

Two further resolutions:

- **Net cash measured at KRW 167.54T** (cash 92.92 + short-term FI 97.04 − total
  debt 22.41). EV falls to ~KRW 1,466T, ~10% below equity value.
- **Share counts confirmed exactly** as derived before this document was available:
  common 5,846,278,608 / preferred 802,371,203 / treasury 82,086,705 common.
  H1 treasury purchases of KRW 13,248,625M reconcile precisely to the 2026-08-21
  filing's "KRW 13,248,624,510,410 since prior fiscal year end".

### Favourable — an internal hedge not previously credited

DX operating margin fell **6.8% (FY2025) → 2.1% (H1 2026)**: Samsung's own set
business is absorbing the memory rent. On normalisation **DX profit recovers as DS
falls**. SK hynix and Micron have no such offset. This raises the bear floor from
roughly −50% to −45% and is a genuine structural difference versus the pure-plays.

### Unfavourable — the surge is price, and that is now a fact

**Memory ASP rose ~220%** in H1 2026 versus the FY2025 average. Comparators in the
same disclosure: smartphone +7%, OLED +1%, TV −4%, digital cockpit −3%.

This converts the cycle-peak argument from INFERENCE to **FACT**. The earnings
surge is overwhelmingly price — not volume, not mix, not competitive gain.

Segment profit confirms the concentration that was previously only inferred:

| H1 2026 | Revenue | Operating profit | Margin | % of group OP |
|---|---|---|---|---|
| **DS** | KRW 209.23T | **KRW 142.86T** | **68.3%** | **97.4%** |
| DX | KRW 100.68T | KRW 2.15T | 2.1% | 1.5% |
| SDC | KRW 14.18T | KRW 1.04T | — | 0.7% |
| Harman | KRW 8.39T | KRW 0.64T | — | 0.4% |

DS operating margin: **13.6% (FY2024) → 19.1% (FY2025) → 68.3% (H1 2026)**. A 68.3%
divisional margin is a rent, and rents get competed away. Samsung's own capex
restraint does not protect it — **industry supply sets the price Samsung receives.**

### Unfavourable — a second P/B correction, same direction

Controlling-interest equity is **KRW 565.06T** (from KRW 424.31T at 2025-12-31).
BPS ≈ **KRW 86,051** ex-treasury. At KRW 250,000 and ~KRW 1,634T total equity value:

| Estimate | Source | Forward P/B |
|---|---|---|
| Screening run | stale broker figure (2025 reference) | ~1.4x |
| First deep analysis | broker year-end BPS estimate KRW 109,313 | ~2.29x |
| **This version** | **measured book, tier-1** | **~2.89x current / ~2.51x forward** |

**Every successive correction has made the stock look less cheap.** Stated plainly
so the pattern is visible rather than buried.

### What did not change

The EV/EBIT method independently reproduces the same requirement: at ~KRW 1,466T EV
and 8–10x mid-cycle EV/EBIT, the price requires normalised operating profit of
**KRW 147–183T** — matching the equity-based range of KRW 145–180T. The conclusion
is robust to method.

Cleanest formulation, using measured figures: at ~2.5x forward book the price
requires **sustainable through-cycle ROE near 25%**, against a 2010s average of
12–15%. H1 2026 annualised ROE was ~47.9%. **The price requires roughly half of the
current return on equity to be permanent.**

Quality-of-earnings check passes: inventory +35.6% while revenue annualises to
+83% — inventory days falling, consistent with genuine shortage rather than channel
loading. Receivables +88.6% broadly track revenue.

### Net effect

Business quality is **confirmed stronger** than the prior version credited
(category 4: 10 → 12). The valuation categories are **unchanged** at 6/15 and 5/10,
because the favourable and unfavourable findings offset. Total 66 → 68, still
*Starter / Watch*. Probability-weighted five-year return improves to ~+15% total
(~2.8%/yr) — still below a Korean risk-free rate.

**The position stays at zero not because of doubt about the business, which this
filing largely settles, but because of expected return.**

---

## Update 2 — FY2025 사업보고서 (tier-1), read 2026-09-04

The annual report supplied the **normalisation baseline the primary gate had been
asking for**. Score **68 → 69**; label unchanged. But the character of the verdict
changed: the expectation gap is now **negative**, not merely thin.

### The series that settles the amplitude question

**DS 부문 operating margin, full cycle:**

| | FY2023 | FY2024 | FY2025 | H1 2026 |
|---|---|---|---|---|
| Revenue | KRW 66.59T | KRW 111.07T | KRW 130.13T | KRW 209.23T |
| Operating profit | **−KRW 14.88T** | KRW 15.09T | KRW 24.86T | **KRW 142.86T** |
| Margin | **−22.3%** | 13.6% | 19.1% | **68.3%** |

DS posted an **outright operating loss three years ago** and roughly a **KRW 158T
swing** in half-year-equivalent profit since. That is the empirical amplitude of
this business.

**And the ASP path compounds:**

| Memory ASP | vs prior-year average |
|---|---|
| FY2025 | **+14%** |
| H1 2026 | **+220%** |
| Compounded vs FY2024 | **≈3.65x** |

FY2025 was an ordinary recovery year. The entire extraordinary move is an **H1 2026
event** — 3.65x in eighteen months. FY2025 comparators: TV −5%, smartphone −3%,
OLED −6%.

### First-pass normalisation — it lands below the price

Assumptions deliberately tilted **in the company's favour**: DS revenue of
**KRW 250–300T** (roughly 2x FY2025) at a **30–38%** margin (well above the 13.6%
and 19.1% actually achieved in FY2024–25, crediting a richer HBM mix).

| | KRW T |
|---|---|
| DS normalised | 75–114 |
| DX recovered | 12–13 |
| SDC | 4 |
| Harman | 1.5 |
| **Group normalised operating profit** | **93–132** |
| **What the price requires** | **145–183** |

**The gap is negative.** To meet the requirement, DS needs roughly **KRW 320T of
revenue — 2.5x FY2025 — at above a 40% margin, sustained.** Equivalently, about
**60% of the current extraordinary condition must become permanent.**

This is a change in kind from the two prior reviews, which described the gap as
tight. `expectation_gap_and_valuation` cut **6/15 → 5/15**; bear weight raised
0.30 → 0.35; probability-weighted five-year return falls **+14.9% → ≈+8.4%** total
(1.6%/yr).

**Stated fairly:** the gate is closed against the current **price**, not against the
company. The model's mid-cycle inputs remain ESTIMATE and have not yet been tested
against announced 2027–2029 capacity additions or against HBM contract terms, which
are not public.

### Correcting my own prior overstatement — the DX hedge

The previous update called the DX hedge a bear-floor raiser without sizing it.
Sized against the three-year series (DX operating profit KRW 14.38T → 12.44T →
12.85T → ≈4.3T annualised), the recovery is worth **KRW 8–10T/yr** against a DS
downside swing exceeding **KRW 150T** annualised — roughly **6–7% of the swing**.
Real, but the earlier framing implied more than the data supports.

### Cutting genuinely the other way

**Cumulative share cancellation: 1,934,188,242 common shares retired — 24.9% of all
7,780,466,850 ever issued** (plus 392,300,147 preferred). This is a multi-decade,
repeated buy-and-cancel record across many cycles, and it **materially offsets the
"buying at the peak" criticism**, which judged the policy on the timing of a single
tranche.

**Counter-cyclical reinvestment.** FY2025 capex **KRW 52.65T** (DS 47.48 / SDC 2.80 /
other 2.12) plus R&D **KRW 37.75T** (11.3% of revenue; 10.9% / 11.6% / 11.3% across
FY2023–25) = **KRW 90.4T of investment against KRW 43.6T of operating profit —
2.07x** — sustained *through* the year DS lost KRW 14.88T. The 2026 windfall was
pre-funded, not lucky. Categories 4 (12 → 13) and 5 (7 → 8) raised.

Capex discipline also confirmed on a second basis: H1 2026 annualises to ≈KRW 62.5T
against FY2025's KRW 52.65T (**+19%**), consistent with the +16.4% measured
H1-over-H1.

### Net

**The business is confirmed better than three successive reviews had credited. The
price is confirmed worse.** Unlike the prior revision, this is no longer a close
call on subjective weights — the normalised model lands below the requirement on
assumptions already generous to the company.

### Scope note

Section III (financial statements), Section 6 (dividends) and the notes were beyond
the retrieved text extract of this filing and were **not read**. FY2025 balance-sheet
and income-statement figures used here come from the interim report's comparative
columns instead. Segment, ASP, capex, R&D and share-count data above are from
Section II, which was within the extract.

---

## Update 3 — FY2025 별도재무제표 (tier-1, pp.194–199), read 2026-09-04

Supplied as filing screenshots — precisely the section beyond the earlier text
extract. Score **held at 69**; verdict unchanged. Three findings, and the most
important one is against the position.

### The capex discipline is a three-year pattern, not one half-year

**Parent (별도) basis, KRW trillion:**

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Revenue | 170.37 | 209.05 | 238.04 |
| Operating profit | **−11.53** | 12.36 | 23.60 |
| Operating cash flow | 34.46 | 52.49 | **68.73** |
| **Tangible capex** | **45.03** | **38.25** | **37.75** |
| Dividends paid | 9.81 | 9.81 | 9.81 |
| Treasury purchases | 0 | 1.81 | 8.19 |
| Share-based comp | 0 | 0 | **0.71** |
| Basic EPS (KRW) | 3,739 | 3,472 | 5,027 |

**Parent capex fell 16.2% while parent operating cash flow doubled.** The discipline
identified in H1 2026 extends back three full years — direction-of-change evidence
of the kind `agents/deep-analyst.md` prioritises.

**But it is two-edged, and that matters.** Samsung's own underinvestment across
FY2023–25 is part of *why* the current shortage exists. The industry's projected
capex tripling into 2027 is the correction of exactly that underinvestment.
Discipline here is a cycle mechanic, not only a virtue.

### SBC quantified — a data gap open since initial underwriting is now closed

**주식기준보상: KRW 0.71T in FY2025, zero in FY2023 and FY2024.** The
performance-conditioned stock programme began in FY2025 and is small so far. Context
that matters: the FY2026 employee-compensation buyback authorisation is **KRW 15T**,
implying a very large step-up in programme scale. And the dividend held flat at
**KRW 9.81T for three consecutive years** frames the FY2026 plan of KRW 90–110T as
roughly a **10x step-change**, not a continuation.

### The left tail is fatter than the modelled bear — this is the important finding

**FY2023 parent operating result: a LOSS of KRW 11.53T** on KRW 170.37T of revenue.
FY2023 segment operating profits sum to roughly **KRW 6.25T** before eliminations
(DX 14.38 − DS 14.88 + SDC 5.57 + Harman 1.17).

Against H1 2026 annualised group operating profit of **KRW 293.45T**, that is a
**≈47x swing** — and the trough is only three years old.

The recorded bear case (normalised group operating profit KRW 70–90T) is therefore
the **modal** bear, sitting well above what this business actually produced in 2023.
Bear return worsened to **−55% to −45%**; weighted five-year return falls
**+8.4% → ≈+5.5%** total (**1.1%/yr**).

This is the red team's "the true bear is worse than the recorded bear" — now
evidenced rather than asserted.

### Two verification results worth recording

**Third independent tier-1 reconciliation.** Parent total equity of
**KRW 254,330,083M** matches *to the won* the KRW 254,330,082,981,146 net-asset
figure in the 2026-08-21 treasury filing. Three separate documents now reconcile
exactly.

**Method check passed.** Parent interest-bearing debt of **KRW 39.05T** *exceeds*
consolidated debt of **KRW 25.24T**, because parent borrowings include intercompany
loans that eliminate on consolidation. This confirms the KRW 167.54T net-cash figure
was correctly computed on a **consolidated** basis — a parent-basis calculation would
have understated it by roughly KRW 14T.

### On not raising the score

The capex evidence would support raising `incremental_roic_and_fcf_per_share` from
13 to 14. **It was held at 13.** That category has already moved 10 → 12 → 13 across
two prior updates as tier-1 documents arrived, and the red team's critique — that
consistent one-directional revision is a bias rather than noise — applies
symmetrically to upward moves. Held pending Q4 2026 data.

Total remains **69/100**. Decision confidence rises **0.72 → 0.76**: a fourth tier-1
document has reconciled against the previous three, and the expected-return
conclusion has survived every one of them.

---

## Correction to the 2026-09-04 screening run

The screening run ranked 005930 first for deep work, resting substantially on a
broker figure of **approximately 1.4x forward P/B**. That figure appears to
reference 2025 and is **stale**. Against a 2026E BPS of KRW 109,313 and a price of
KRW 250,000, forward P/B is approximately **2.29x** — at or above the top of
Samsung's historical 0.9x–2.1x range, and computed on book that peak earnings have
themselves inflated.

This is a material correction. It does not overturn the business-quality analysis,
which is if anything stronger than the screen assumed. It does remove the
"price does not require the peak to persist" argument in the strong form it was
originally stated, and it is the reason `expectation_gap_and_valuation` scores 6/15
rather than the 8–10 the screening note implied. See `valuation.json`.

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

Two material inputs remain **unknown** and are recorded as such rather than
estimated away: the preferred-share price and the current consolidated net cash
position. Both move the valuation.

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

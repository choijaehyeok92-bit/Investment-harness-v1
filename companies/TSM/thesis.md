# Investment Thesis — TSM (Taiwan Semiconductor Manufacturing Company)

As of: 2026-09-04 · Price: US$414.00 per ADS · Position: STARTER (1–2%)
Prepared under `agents/deep-analyst.md`. Expectation gap and asymmetry are scored by
`agents/valuation.md`, not here.

---

## Sourcing note

Every financial figure below is **tier-1**, from the **2025 Form 20-F** (FY ended
2025-12-31) supplied for this analysis. The **Form SD (CY2025)** conflict-minerals
report was also supplied; it is recorded for completeness with low analytical weight.

Current-year trading figures come from TSMC's monthly revenue disclosures (Form 6-K,
tier-2). **The ADS price is the only non-primary input in this valuation.**

TSM is a **US-listed foreign issuer** (Taiwan-incorporated, NYSE-listed ADS at 1 ADS
= 5 common shares), consistent with how it was labelled in the 2026-09-04 screening run.

---

## 1. Structural change and market leadership — 14/15

| | 2023 | 2024 | 2025 |
|---|---|---|---|
| Net revenue (NT$M) | 2,161,736 | 2,894,308 | **3,809,054** (US$121,423M) |
| ≤7nm % of wafer revenue | 58% | 69% | **74%** (77% in Q2 2026) |
| HPC % of revenue | 43% | 51% | **58%** |
| Smartphone % of revenue | 38% | 35% | 29% |

2025 revenue grew **+31.6%**; January–July 2026 is running **+37.0% YoY** against
company guidance of *slightly above +40% in USD*. **2nm entered volume production in
2025**; A16 risk production is expected in 2026.

TSMC is the physical precondition for the entire AI build-out — NVIDIA's
accelerators, AMD's, Broadcom's custom ASICs and Google's TPUs are all fabricated
here. It scores 14 rather than 15 because it does not define the architecture; it
defines what is physically possible.

**The deduction is concentration.** North America went **68% → 70% → 75%** of
revenue; China fell 12% → 9%. And **every 1% USD depreciation against the NT dollar
costs ~0.3pp of operating margin** — sales are USD-denominated, much of the cost base
is not.

## 2. Customer value and product strength — 9/10

The proof is in the margin, not the narrative: **gross margin expanded 54.4% → 56.1%
→ 59.9% while revenue grew 76% cumulatively.** Customers are paying *more* per wafer,
voluntarily, in a market with alternatives. The company attributes 2025 growth to
*"an increase in ASP due to a higher proportion of advanced technology revenue and an
increase in wafer shipments"* — mix and volume, not discounting.

Switching costs are among the highest in any industry: a design is bound to a
specific process design kit, and changing foundries means a full redesign and
requalification measured in years. Advanced packaging (CoWoS, SoIC, 3DFabric) is a
second value layer that did not exist a decade ago and has stayed **sold out**
through the 2026 capacity ramp.

Capped at 9 by rising customer concentration — see §3.

## 3. Moat trajectory — 13/15

**The highest moat-trajectory score assigned in this harness**, and the reasoning is
the direction-of-change evidence `agents/deep-analyst.md` demands:

| | 2023 | 2024 | 2025 | Δ |
|---|---|---|---|---|
| Gross margin | 54.4% | 56.1% | **59.9%** | **+5.5pp** |
| Operating margin | 42.6% | 45.7% | **50.8%** | **+8.2pp** |
| R&D (NT$M) | 182,370 | 204,182 | **246,427** | rising |
| R&D as % of revenue | 8.5% | 7.1% | **6.5%** | falling |

Margins expanding *during* volume growth is the signature of a strengthening
position, not a cyclical rent. R&D rising in absolute terms while falling as a share
of revenue is operating leverage **on the moat itself**. The node lead is *extending*
— 2nm in volume production, A16 risk production due 2026 — with 2nm booked into 2028.

**Against:** top-ten customers are **70% → 76% → 78%** of revenue, so the moat is
increasingly rented to fewer tenants. And geographic dispersion (Arizona, Kumamoto,
Dresden) structurally raises cost and dilutes the Hsinchu/Tainan cluster advantage.
Intel 18A and Samsung SF2 are the watch items; a moat scored on the absence of a
successful challenge is scored on a negative.

## 4. Incremental ROIC and FCF/share — 12/15

**Incremental ROIC is rising**, which is what this category actually asks: operating
margin expanded 8.2pp over two years while capital intensity stayed roughly flat
(capex 44.0% / 33.0% / **33.4%** of revenue). More profit per unit of capital, three
years running. Operating cash flow reached **US$72,521M**; free cash flow US$31.6B.

**The structural limitation is capital intensity.** TSMC must spend roughly a third
of revenue every year simply to hold position — the opposite of NVIDIA's
2.8%-of-revenue model. **FY2026 capex guidance is US$52–56B**, a 27–37% step-up, and
D&A of NT$688,096M will keep climbing as that capex lands.

And there are **no buybacks**. Share count is flat at 25,932,524,521; capital return
is dividend-only at roughly a **0.85% ADS yield**. This is the one category where
TSMC scores *below* both 005930 (13) and NVDA (13), both of which are retiring stock.

## 5. Management and capital allocation — 9/10

**The best capital-allocation record in this harness.** 2025 capex of NT$1,272,411M
was funded against only **NT$86,900M of bonds — roughly 93% from operating cash
flow**. Short-term loans **nil**; long-term debt at **0.41–4.63% fixed** with
maturities to 35 years. The dividend was raised **20% per share within 2025**
(NT$5.00 → NT$6.00 quarterly) *in the same year as record capex*.

Overseas expansion is structured to share risk rather than absorb it: **JASM**
(Kumamoto) 72.6% TSMC with Sony, DENSO and Toyota; **ESMC** (Dresden) 70.0% TSMC with
Bosch, Infineon and NXP at 10% each — partners who are also customers. Incentives
secured: **US$6.6B direct + US$5B loans** (CHIPS Act, Arizona) and **EUR5B** (Germany).

**Against:** TSMC gave the DOC an *"irrevocable, absolute and unconditional
guarantee"* of TSMC Arizona's obligations — full recourse — and the subsidies carry
clawback conditions plus restrictions on expansion in "foreign countries of concern."

## 6. Financial survivability — 9/10

**Net cash ≈ US$64.9B**: cash and current marketable securities **US$97,820M** against
long-term debt **US$32,929M**, short-term loans **nil**. Operating cash flow of
US$72.5B exceeds total debt outstanding. No refinancing wall.

Survivability in the ordinary financial sense is not in question. The survivability
risk here is physical, and is scored in §7.

**Business-quality subtotal (§1–6): 66/75 — the highest in this harness**
(005930: 59, NVDA: 62).

## 7. Key risks and concentration dependencies

**Taiwan is the position.** Nine fabs in Hsinchu Science Park, two in Central Taiwan,
seven in Southern Taiwan, plus Fab 22 in Kaohsiung. Overseas capacity — Fab 11
(Washington), Fab 21 (Arizona), Fab 23 (Kumamoto), Fab 24 (Dresden, under
construction), Fab 10 (Shanghai), Fab 16 (Nanjing) — is material but **not a
leading-edge substitute**. The Taiwan fab land is **leased** from science-park
administrations, with **Kaohsiung Fab 22 leases up for renewal by December 2026** and
some Southern Taiwan leases from March 2026.

Customer concentration (top ten 78%) and revenue geography (North America 75%) layer
on top.

**Why this differs from every other name in this harness.** 005930's bear is a cycle;
NVDA's is a demand pause. Both are drawdowns against solvent businesses. **TSMC's
tail is a genuine loss of the asset base** — and it is *unhedgeable* and
*unresearchable*.

---

## Most important unknowns

1. **The Taiwan contingency probability.** Estimated 3–7% over five years, confidence
   deliberately set at 0.40. This is a judgement, not a measurement, and no amount of
   analysis will make it one.
2. FY2026 net margin — TSMC does not guide margin, so the forward multiple rests on
   an analyst assumption (47%; at FY2025's 44.6% the forward P/E is 28.3x not 26.8x).
3. Overseas fab gross margin versus Taiwan fabs, and overseas share of the FY2026
   US$52–56B capex.
4. Yield comparison versus Intel 18A and Samsung SF2 at equivalent nodes.
5. Return on invested capital by fab vintage.

## Evidence that would strengthen the thesis

- Overseas advanced-node capacity rising to a materially larger share of leading-edge
  output — the only development that genuinely reduces the single-point exposure
- FY2026 reported net margin confirming at or above 47%
- Gross margin holding above ~55% as 2025–26 capex depreciation lands in 2027–28
- A16 moving from risk to volume production on schedule
- Initiation of buybacks, or a higher payout ratio — improving the one category where
  TSMC is weakest

## Evidence that would weaken the thesis

- A credible second source winning a leading-edge design from a top-five customer
- Gross margin below ~55% outside a node transition
- FY2027 capex guidance rising again while revenue growth decelerates
- Advanced-node mix stalling, or A16 slipping materially past 2026
- Sustained NT dollar strength (each 1% USD depreciation ≈ −0.3pp operating margin)

---

## Why STARTER — and why the reasoning differs from NVDA

All three deep analyses in this harness now sit at `INVESTIGATE`. What separates them
is *what kind* of question is open.

| | 005930 Samsung | NVDA | **TSM** |
|---|---|---|---|
| Score | 69 | 75 | **79** |
| Business quality (of 75) | 59 | 62 | **66** |
| `low_quality_growth` | PASS | **INVESTIGATE (HIGH)** | **PASS** |
| `moat_shrinkage` | PASS | INVESTIGATE | **PASS** |
| Expectation gap | **negative** | positive, thin | positive, thin |
| Weighted 5-yr return | +5.8% | +21.2% | **+37.9%** |
| Verdict | WATCH / NONE | STARTER | **STARTER** |

**The decisive point on sizing.** NVDA's open gates are *disclosure questions with
definite answers* — quantify equity-affiliated revenue, establish commitment
cancellability. Waiting a quarter genuinely resolves them.

TSMC's dominant gate is **not researchable**. No further work converts geopolitical
probability into a measurement. A risk that can only be *sized*, never *resolved*,
argues for a small position held with discipline rather than for waiting indefinitely
for information that will never arrive.

`policy/position-sizing.yaml` sizes on evidence. The business evidence here is the
strongest in this harness; the dominant risk is bounded by position size. **STARTER at
1–2%** is the correct expression — and the asymmetry category still scores only 4/10,
below NVDA's 5, because a high probability of a good-but-bounded outcome plus a small
probability of near-total loss is a worse outcome *shape* than a wider band with no
catastrophic tail.

Macro pacing is **slow**: the AI-capex complex remains a single correlated exposure
per the 2026-09-04 screening run, and TSMC sits underneath all of it.

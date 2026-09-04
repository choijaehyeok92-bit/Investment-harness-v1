# Decision History — TSM

Append-only. Do not erase prior decisions.

## 2026-09-04 — Initial underwriting

- **Decision:** `STARTER` · **Position band:** `STARTER` (1–2%)
- **Total score:** **79 / 100** — *Emerging Outlier* (business quality **66/75**;
  expectation gap 9/15; asymmetry 4/10)
- **Hard Veto status:** `INVESTIGATE` — no FAIL. **Five PASS**, the most of any name
  in this harness. Two HIGH-severity items — `fatal_concentration` and
  `permanent_loss_probability` — which reduce to **the same underlying exposure: Taiwan**.
- **Red team:** `PASS`, confidence **0.55**, with two dissents recorded
- **Macro pacing:** `slow` · **Decision confidence:** 0.68

### Source basis

All financials are **tier-1** from the **2025 Form 20-F** (FY ended 2025-12-31).
The **Form SD (CY2025)** conflict-minerals report was also supplied and is recorded
with low analytical weight. Current-year trading is from TSMC monthly disclosures
(Form 6-K, tier-2). **The ADS price is the only non-primary input.**

### What the analysis found

**The defining fact — margins expanded while volume grew.** Gross margin
**54.4% → 56.1% → 59.9%** and operating margin **42.6% → 45.7% → 50.8%** across
2023–25, on revenue up **76% cumulatively** (FY2025 NT$3,809,054M / US$121,423M,
+31.6%). Growth bought with price or subsidy compresses margin; this does the
opposite. **This is why `low_quality_growth` and `moat_shrinkage` both read PASS —
the only company in this harness where both do.**

**Node leadership extending.** ≤7nm went 58% → 69% → **74%** of wafer revenue (77% by
Q2 2026); 2nm entered **volume production** in 2025 with A16 risk production due 2026;
2nm booked into 2028 and CoWoS sold out. R&D rose in absolute terms every year
(NT$182bn → 246bn) while *falling* as a share of revenue (8.5% → 6.5%).

**Best capital-allocation record in this harness.** Capex ~93% self-funded; short-term
loans **nil**; debt at 0.41–4.63% fixed out to 35 years; net cash **≈US$64.9B**;
dividend raised **20% per share within 2025** in the same year as record capex;
overseas expansion partner-structured (JASM 72.6% with Sony/DENSO/Toyota; ESMC 70.0%
with Bosch/Infineon/NXP).

**The structural limitation.** Capex is **33.4% of revenue** with FY2026 guidance of
**US$52–56B** (+27–37%). Free cash flow was only US$31.6B on US$121.4B of revenue.
**No buybacks** — share count flat at 25,932,524,521, dividend yield ~0.85%. This is
the one category where TSMC scores *below* both 005930 and NVDA.

**Source conflict resolved.** Aggregators reported market cap of both US$1.93T and
US$2.15–2.16T. Computing from the tier-1 share count (5,186.5M ADS × US$414.00) gives
**US$2,147B**, confirming the higher figure.

### Why STARTER — and why the reasoning differs from NVDA

| | 005930 | NVDA | **TSM** |
|---|---|---|---|
| Score | 69 | 75 | **79** |
| Business quality (of 75) | 59 | 62 | **66** |
| `low_quality_growth` | PASS | INVESTIGATE (HIGH) | **PASS** |
| `moat_shrinkage` | PASS | INVESTIGATE | **PASS** |
| Expectation gap | **negative** | positive, thin | positive, thin |
| Weighted 5-yr return | +5.8% | +21.2% | **+37.9%** |
| Verdict | WATCH / NONE | STARTER | **STARTER** |

**The decisive point on sizing.** NVDA's open gates are *disclosure questions with
definite answers* — quantify equity-affiliated revenue, establish commitment
cancellability. Waiting a quarter genuinely resolves them.

**TSMC's dominant gate is not researchable.** No analysis converts geopolitical
probability into a measurement. A risk that can only be *sized*, never *resolved*,
argues for a small position held with discipline rather than for waiting indefinitely
for information that will never arrive.

Asymmetry still scores only **4/10** — *below* NVDA's 5 despite the better business —
because a high probability of a good-but-bounded outcome plus a small probability of
near-total loss is a worse outcome **shape** than a wider band with no catastrophic tail.

### Red-team dissents — recorded, not adopted

1. **Scoring.** `incremental_roic_and_fcf_per_share` at 12/15 is a point too generous
   given 33% capex intensity, 1.47% FCF yield, no buybacks, and an **unmodelled
   2027–28 depreciation wall**. At 11/15 the total is 78 — changes nothing, recorded
   as a quibble.
2. **Sizing logic, and this one matters.** The analyst argues that because the Taiwan
   gate is unresearchable, waiting adds nothing, so size small and hold. The red team
   notes this cuts both ways: if the dominant risk cannot be reduced by work, it also
   cannot be reduced by conviction, and the position should be sized off the *tail*
   rather than off business quality. A 1–2% STARTER is consistent with both readings.

The red team also flags two items the analyst accepts: the **2027–28 depreciation
wall** is named as counter-evidence but not modelled, and **overseas fabs may
diversify revenue without diversifying the risk that matters**.

### What would change the decision next

**To `NORMAL` (2–4%)** — two prerequisites, one of which the file has not yet done:
1. Model the 2027–28 depreciation impact on margins explicitly (arithmetic, not judgement)
2. Establish overseas advanced-node capacity as a share of total leading-edge output —
   **the only increase trigger that touches the risk that actually matters**

Plus at least one of: FY2026 reported net margin confirming ≥47%; gross margin holding
above ~55% as new depreciation lands; A16 reaching volume production on schedule;
initiation of buybacks.

**To `REDUCE` / `EXIT`:** a credible second source winning a leading-edge design from a
top-five customer; gross margin below ~55% outside a node transition; FY2027 capex
guidance up again while growth decelerates; A16 slipping materially past 2026; any
material adverse change in the Taiwan security situation — acted on as a **risk-budget
decision**, not a research finding.

**Explicitly not a reason to act either way:** price movement alone.

### Next scheduled review

Q3 2026 results (October 2026). Per `policy/monitoring.yaml` the quarterly review
checks thesis-critical KPIs only and does **not** evaluate price. Critical KPIs, in
order: gross margin (against the ~55% floor), advanced-node mix, FY2026 capex actual
versus the US$52–56B guidance, and any FY2027 capex signal.

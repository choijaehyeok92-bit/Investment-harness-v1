
# Decision History - NVDA

Append-only. Do not erase prior decisions.

## 2026-09-03

- Decision: WATCH
- Position band: NONE
- Total score: 76/100 (Emerging Outlier)
- Hard Veto status: INVESTIGATE
- Price: $227.23 at 2026-09-03 16:54:51 UTC
- Expectation gap: Base value approximately $221 versus current price $227.23; no margin of safety
- Asymmetry: Bear/Base/Bull $92/$221/$447; subjective probability-weighted value $227.5
- Evidence change since prior review: Initial repository coverage using the supplied FY2026 10-K, 2026 Proxy, FY2027 Q2 10-Q and 8-K, executive Form 4, Form 144 and proxy voting materials.
- Thesis change: Initial coverage. The AI platform-leader thesis is conditioned on independent customer cash generation, working-capital conversion and disciplined ecosystem commitments.
- What would change the decision next: Multiple simultaneous improvements in DSO, FCF/share, third-party cloud utilization, Rubin transition, customer diversification and expectation gap.
- Macro pacing: company_specific; macro did not change the company score.
=======
# Decision History — NVDA

Append-only. Do not erase prior decisions.

## 2026-09-04 — Initial underwriting

- **Decision:** `STARTER`
- **Position band:** `STARTER` (1–2% per `policy/position-sizing.yaml`)
- **Total score:** **75 / 100** — *Emerging Outlier* (business quality 62/75;
  expectation gap 8/15; asymmetry 5/10)
- **Hard Veto status:** `INVESTIGATE` — no FAIL. **Three HIGH-severity items open:**
  - `low_quality_growth` — circular investment/revenue structure
  - `incremental_roic_collapse` — $279B supply commitments
  - `fatal_concentration` — Data Center 89.7%, top-2 customers 36%
  - `management_or_accounting_integrity` and `moat_shrinkage` at MEDIUM
  - `price_requires_unrealistic_bull_case` **PASS** — the key differentiator
- **Red team:** `PASS`, confidence 0.60, **with a recorded dissent on position size**
- **Macro pacing:** `slow` — AI-capex complex treated as one correlated exposure
- **Decision confidence:** 0.62

### Source basis

All financials are **tier-1 SEC XBRL** parsed from the supplied filing packages:
10-K FY2026 (FY ended 2026-01-25), 10-Q Q2 FY2027 (quarter ended 2026-07-26), plus
DEF 14A, 8-K and Forms 3/4. The **price anchor is also tier-1** — $226.27, the last
reported transaction in the 2026-09-02 Form 4.

### What the analysis found

**Exceptional business quality.** Revenue $60.9B → $130.5B → $215.9B (FY2024–26) and
$177.8B in H1 FY2027 (+95.8%), on **capex of 2.8% of revenue**, ROE near 100%, gross
margin recovered to 75.0%, networking 3.7x in two years — and **share count DOWN 2.3%**
during the fastest growth phase in company history, with $113B of buybacks against
SBC of 3.0% of revenue.

**An earnings-quality adjustment that changes the multiple.** Reported H1 net income
($118,010M) *exceeds* operating income ($117,270M) because of **$23,707M of gain on
investments** ($12,500M explicitly unrealised). Roughly 17–20% of reported net income
is investment revaluation. Stripping it and taxing at the actual 16.5% rate gives core
annualised EPS of ~$8.08 — so the multiple is **28.0x, not the headline 23.3x**.

**The central risk, newly quantified.** Future commitments total **$366B**, of which
**supply and capacity is $279B** — up from **$95.2B six months earlier (+193%)** — 
against a recorded excess-inventory accrual of only **$2,138M**. Equity stakes held
went from ~$5B to **$90.7B** in twelve months, with $25B more committed and $29B of
committed cloud purchases from the same ecosystem. Long-term debt went $7.5B → $32.4B.

**Concentration is rising, not falling.** Customer One: 13% → 12% → **22%** of
Compute & Networking revenue. Top two 36% (from 23%). Top five = ~70% of receivables.
Data Center 89.7% of revenue. US 69.3%. China down to ~7%.

### Why STARTER rather than WATCH

`Hard Veto > Score` applies, and three HIGH-severity gates are open. The deciding
factor is the **expectation gap**, which is where this differs from 005930 Samsung
(WATCH / NONE, same date):

| | Samsung 005930 | **NVDA** |
|---|---|---|
| Score | 69 (Starter/Watch) | **75 (Emerging Outlier)** |
| Normalised model vs price requirement | model **below** requirement | requirement ≈ **current core base** |
| Expectation gap | **negative** | **positive, thin** |
| Weighted 5-yr return | +5.8% | **+21.2%** |
| Verdict | WATCH / NONE | **STARTER / 1–2%** |

For Samsung no position was justified at any veto status because the gap itself was
negative. Here a 25x mature multiple requires roughly the **current core earnings base
to persist with no growth** — a positive gap. `policy/position-sizing.yaml` defines
STARTER as *"attractive thesis, but evidence is still limited"*, which describes this
precisely.

### Red-team dissent — recorded, not adopted

The red team would hold at `WATCH` / `NONE`: three open HIGH-severity vetoes plus a
3.9%/yr probability-weighted return is a thin case for committing capital today rather
than waiting one quarter for the commitments note. It also makes two points the
analyst accepts:

1. **NVIDIA discloses no units or ASP.** The price/volume decomposition that convicted
   Samsung's earnings **cannot be run here at all** — NVDA's earnings quality is *less*
   verifiable on the dimension that mattered most, not more.
2. **The circular-revenue bound is loose.** Bounding at "<10% worst case" uses the
   $25B *commitment* against $356B revenue — it does not bound the cumulative $90.7B
   already deployed.

### What would change the decision next

**To `NORMAL` (2–4%)** — both are disclosure questions with definite answers, not
judgement calls:
1. Equity-affiliated revenue quantified below ~5% of total and stable
2. Cancellability of the $279B supply commitments established as materially flexible

Plus at least one of: top-customer concentration stabilising below 22%; gross margin
holding ≥75% through the Rubin ramp; investment gains falling as a share of net income.

**To `REDUCE` / `EXIT`** — the excess-inventory accrual rising materially from $2,138M
(management's own signal); supply commitments rising while sequential revenue
decelerates; gross margin below ~70% outside a transition; a hyperscaler capex
guidance cut.

**Explicitly not a reason to act either way:** price movement alone.

### Next scheduled review

Q3 FY2027 results (late November 2026). Per `policy/monitoring.yaml` the quarterly
review checks thesis-critical KPIs only and does **not** evaluate price. Critical
KPIs, in order: the commitments note (supply and capacity total, and the
excess-inventory accrual), customer concentration, gross margin, gain on investments
as a share of net income.

## 2026-09-05 — Astra 재심사

- 과거: 76 WATCH / 75 STARTER 충돌; 현재: 73/100, WATCH, INVESTIGATE, 포지션 밴드 NONE.
- 서로 다른 76점 WATCH와 75점 STARTER를 하나의 판정으로 복구한다. 새 점수 73, WATCH. 플랫폼 우위는 유지되지만 고객 금융지원·공급약정과 큰 기준 지분가치가 비대칭을 제한한다.
- [현재 재평가](re-evaluation-2026-09-05.md). 이전 판정은 역사이며 주문·거래는 실행하지 않았다.

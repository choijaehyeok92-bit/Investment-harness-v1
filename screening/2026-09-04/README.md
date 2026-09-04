# Screening Run — 2026-09-04 · US + Korea

Executed under `agents/screener.md` and `policy/screening.yaml`.
Authority order applied: `policy/investment-philosophy.md` > `policy/hard-veto.yaml` >
`policy/scorecard.yaml` > `policy/source-policy.yaml` > `agents/screener.md`.

## Scope and stated assumptions

The request was "screen US and Korean stocks per the harness guidelines" without a
supplied universe. `screening/universe.example.csv` contains only a placeholder row,
so a universe was constructed for this run. Assumptions, stated explicitly:

- The universe was built from companies with a *plausible* long-duration
  expectation-gap case, not from an index. It is therefore pre-filtered for
  quality — see "Why zero SCREEN_OUT" below.
- 32 names screened (18 US-listed, 14 Korea-listed). 12 further names are listed in
  `screening/universe-2026-09.csv` with status `DEFERRED`: current-period evidence
  could not be established in this run, and `policy/source-policy.yaml` prefers
  `unknown` to invented precision.
- `TSM` and `MELI` are US-listed **foreign issuers**, not US companies. They are
  included as US-listed instruments and labelled as such rather than silently
  counted as US.
- All figures are as-reported for the most recent disclosed period (largely
  calendar Q2 2026). No figure here has been independently recomputed from primary
  filings; `www.sec.gov` and several issuer IR domains are blocked by this
  environment's network egress proxy, so most quantitative claims rest on
  source-policy tier 2–4 (IR press coverage / financial press), not tier 1
  (primary filings). **Confidence is capped accordingly and marked per record.**

## Outputs

| File | Contents |
|---|---|
| `screen-results.jsonl` | One machine-readable record per screened name |
| `candidates.md` | SCREEN_IN narratives (14) |
| `watchlist.md` | WATCH narratives (18) |
| `../universe-2026-09.csv` | Full universe incl. deferred names |

`screen-results.jsonl` record fields follow the `agents/screener.md` output contract:
`ticker, company_name, market, listing, run_date, verdict, reason, positive_signals[],
uncertainties[], veto_flags[], research_priorities[], evidence_confidence, sources[]`.

No JSON Schema exists for screening output under `schemas/` (only scorecard,
valuation, decision, hard-veto, evidence). `scripts/validate_outputs.py` therefore
does not cover these files. Noted as a harness gap, not fixed in this run.

## Macro overlay — pacing only, not scoring

Per `policy/macro-overlay.yaml`, none of the following altered any company verdict.

**FACT.** US: S&P 500 +9% YTD 2026; consensus FY26 revenue +11%, earnings +23%; AI
infrastructure ~half of that earnings growth; strategist year-end target average
7,555. Forward P/E entered the year at 22, among the most expensive on record.
Korea: KOSPI has held ~6,000 for roughly a month; 2026 aggregate operating profit
forecast ~KRW 397T (+38% YoY), driven by margin expansion rather than revenue.

**FACT.** Amazon, Alphabet, Microsoft, Meta and Oracle have guided to >$725B of 2026
capex (AMZN ~$200B, MSFT ~$190B, GOOGL $175–185B, META $125–145B — raised from
$115–135B citing memory pricing). Alphabet reported its first negative-FCF quarter
since its 2004 IPO; Meta's cash generation fell 91% YoY; Amazon FCF is projected
negative. The four hyperscalers bought $433.9B of PP&E in the four quarters to
March 2026 against roughly $149B of reported depreciation.

**INFERENCE.** The dominant earnings driver in both markets is one funding source —
hyperscaler capex — that is now being paid for out of balance sheet rather than
operating cash flow, with a multi-year depreciation wave still ahead of the income
statement. That is a *correlated* dependency running through most AI-infrastructure
names in this screen, and through Korean memory, equipment, and power names.

**Regime call: `neutral`.** Signals are mixed, not risk-off: credit is not
stressed and earnings are growing. Action per policy: `purchase_pacing:
company_specific`, `risk_budget: normal`. One addition, which is a pacing rule and
not a score adjustment: **inside the AI-capex-derived complex, pace purchases
slowly and treat the cluster as a single risk exposure for budgeting purposes.**

## Cross-cutting lens applied to this run

`policy/investment-philosophy.md` §1 explicitly refuses to reward "cyclical peaks
misidentified as structural growth." Two facts made this the governing question:

- SK hynix Q2 2026 operating margin **76%**; Samsung Electronics company-wide
  operating margin **52.2%**; Micron guiding to ~**81%** gross margin.
- These are shortage rents, not steady-state economics. Any name whose current
  earnings are a derivative of memory pricing was screened on *normalized* earning
  power and on *moat trajectory*, never on peak profit.

## Results

| Verdict | US-listed | Korea-listed | Total |
|---|---|---|---|
| SCREEN_IN | 8 | 6 | 14 |
| WATCH | 10 | 8 | 18 |
| SCREEN_OUT | 0 | 0 | 0 |
| DEFERRED (not screened) | 6 | 6 | 12 |

### Why zero SCREEN_OUT

`policy/screening.yaml` permits screen-out only on five narrow conditions (obvious
hard veto, no structural growth path, no credible customer value, no survival path,
evidence too sparse for a testable thesis) and explicitly forbids rejecting on high
P/E, low P/E, prior price appreciation, a single EPS miss, or current losses. No
name in this universe met a screen-out condition. Zero rejections reflects how the
universe was constructed plus a deliberately permissive gate — the harness's actual
rejection mechanism is the Hard Veto at the deep-analyst stage, not the screener.

Every one of the 32 names carries at least one `INVESTIGATE`-level Hard Veto flag —
that is the screener working as designed, not an anomaly. Seven names carry a flag
marked **PRIMARY GATE**, meaning the deep-analyst stage must resolve that single
question before any other work is worth doing:

| Ticker | Company | Primary gate |
|---|---|---|
| 000660 | SK hynix | `moat_shrinkage` — HBM share 64% → 50% YoY |
| PLTR | Palantir | `price_requires_unrealistic_bull_case` — ~53x forward revenue |
| 012450 | Hanwha Aerospace | `persistent_dilution` — capital-raise history |
| 035420 | NAVER | `moat_shrinkage` — search moat under generative interfaces |
| 259960 | Krafton | `fatal_concentration` — single-franchise dependence |
| ASTS | AST SpaceMobile | `external_capital_dependence` — runway to constellation |
| 141080 | LigaChem Bio | `external_capital_dependence` — sustained operating losses |

These flags, not the verdict counts, are the signal in this run.

## Ranked next actions

Run `/analyze-stock` in this order:

1. **005930 Samsung Electronics** — largest gap between measurable moat improvement
   and what price requires.
2. **214450 PharmaResearch** — high-margin, accelerating export mix, uncorrelated
   with AI capex, small enough for power-law upside.
3. **034020 Doosan Enerbility** — scarce asset at the AI power bottleneck, with
   orders already booked rather than narrated.
4. **NVDA** — duration-of-demand question dominates; forward P/E ~24 does not itself
   require the bull case.
5. **012450 Hanwha Aerospace** — decade-length rearmament driver; dilution history
   must be checked first.

Highest-priority WATCH to resolve: **000660 SK hynix** — HBM share fell 64% → 50%
YoY while P/B made new highs. See `watchlist.md`.

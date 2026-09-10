# TSM 2026-09-10 Deep Research Checkpoint

## Decision

- WATCH / P1
- buy_authorized: false
- position_band: NONE
- business quality: 68/75
- total score: 75/100 — Emerging Outlier
- required return: 9%
- reference price: US$427.18 (2026-09-10 secondary completed-session reference; not exchange-audited)
- retained Bear / Base / Bull: US$96.28 / US$309.90 / US$702.08
- reverse expectation: ~15.01% annual revenue growth in years 2-10 after Base year-1 revenue US$185B

## What changed versus 2026-09-06 canonical

Operational evidence strengthened. Q2 2026 revenue was NT$1.270T, parent net income NT$706.6B, gross margin 67.7%, operating margin 60.3%, HPC 66% of revenue and 2nm 3% of wafer revenue. Official August revenue reached NT$514.8B, up 53.3% YoY, and January-August revenue rose 39.3%. TrendForce estimated Q2 foundry share at 72.5%.

Business quality rises from 66/75 to 68/75 through stronger structural-leadership and moat evidence. Total score rises from 73 to 75, moving the score classification to Emerging Outlier. Priority rises P2 to P1 because evidence is stronger and monthly/quarterly checkpoints are decision-relevant.

However, valuation remains unattractive. The price is materially above retained Base value, and a 9% hurdle still requires about 15% annual revenue growth for nine years under strong Base margins.

## Capital-return discipline

Harness-rule TTM diagnostics in native NTD:

- revenue NT$4.440T
- parent net income NT$2.237T
- operating cash flow NT$2.635T
- disclosed PPE purchases NT$1.491T
- mechanical OCF-PPE NT$1.144T

OCF-PPE is not normalized owner FCF. 2026 capex guidance is US$60-64B and the Arizona program has expanded to about US$265B. Overseas fabs and new nodes have known early margin dilution and their post-ramp subsidy-adjusted incremental ROIC is not yet observable.

## Open Hard Veto gates

- incremental_roic_collapse — INVESTIGATE: newly opened because the scale of N2/A14, advanced-packaging and overseas capital deployment requires cohort-level return evidence.
- fatal_concentration — INVESTIGATE: 2025 top ten customers were 78% of revenue, top two 36%, while leading-edge production/R&D remains Taiwan-heavy.
- permanent_loss_probability — INVESTIGATE: geopolitical discontinuity plus valuation duration can cause permanent or very long capital impairment despite strong ordinary solvency.

All other vetoes are PASS on current evidence. In particular, price_requires_unrealistic_bull_case is PASS because ~15.01% reverse growth is demanding but not demonstrably impossible given current operating evidence; this does not make the stock attractively valued.

## Repository safety

This run is additive-only. It must not modify:

- `companies/TSM/latest.json`
- `registry/companies.json`
- `reviews/latest.json`
- canonical raw-data
- `harness/baseline-lock.json`
- frozen deterministic outputs

The current canonical authority remains `2026-09-06-deep` pending a separate reviewed authority-promotion run. No claim is made that a local frozen deterministic validator was executed for this additive checkpoint.

# MPWR 2026-09-10 Deep Research Checkpoint

## Decision

- WATCH / P1
- buy_authorized: false
- position_band: NONE
- business quality: 62/75
- total score: 69/100 — Starter / Watch
- required return: 9%
- reference price: $1,186.08 (2026-09-10 completed U.S. session)
- Bear / Base / Bull: ~$218.71 / ~$680.08 / ~$1,569.06
- reverse expectation: ~19.35% annual revenue growth in years 2-10 after Base year-1 revenue of $4.4B

## What changed versus 2026-09-06 canonical

The canonical record was only PRELIMINARY_REVIEW with no established score or valuation. This checkpoint completes all eight scorecard categories, all nine Hard Veto items, a three-scenario valuation, reverse expectations, permanent-loss case, red-team attacks, falsifiers and increase/sell evidence.

Operational evidence is strong: Q2 revenue was $980.6M (+47.6% YoY), Enterprise Data $380.6M (+164.3%), GAAP operating margin 31.0%, and Q3 revenue guidance midpoint approximately $1.15B. MPS is sampling high-voltage AC-to-DC products for 800V data-center architectures and has entered a long-term GlobalFoundries manufacturing partnership with volume production planned for early 2027.

## Why the score is only 69 despite strong growth

Harness rules separate business quality from market expectations and accounting reliability. MPWR receives 62/75 on business quality, but only 3/15 on expectation gap and 4/10 on asymmetry. At $1,186.08, the stock trades about 74% above the modeled Base value and requires roughly 19.35% annual growth for nine years under Base cash economics.

The 2024 financial statements were materially restated for deferred-tax accounting and the related material weakness remained unremediated as of June 30, 2026. EY's financial-statement opinion was unqualified and no intentional misconduct is established, but accounting-control reliability therefore remains an open Hard Veto gate.

## Cash-quality discipline

Harness-rule TTM diagnostics:

- revenue: ~$3.273B
- operating income: ~$0.940B
- net income: ~$0.802B
- operating cash flow: ~$0.822B
- PPE purchases: ~$0.237B
- SBC: ~$0.209B
- mechanical OCF-PPE: ~$0.586B
- conservative OCF-PPE-SBC diagnostic: ~$0.377B

Neither cash subtotal is normalized owner FCF. H1 OCF declined despite higher earnings, working-capital needs rose, and inventory remained significant. New manufacturing capacity also requires a separate post-ramp incremental-return test.

## Open Hard Veto gates

- management_or_accounting_integrity — INVESTIGATE: material 2024 deferred-tax restatement and unremediated material weakness at June 30, 2026.
- incremental_roic_collapse — INVESTIGATE: no collapse is established, but new capacity and working capital require cohort-level return validation.
- price_requires_unrealistic_bull_case — INVESTIGATE: reverse growth is extremely demanding but current AI growth prevents an outright impossible-case conclusion.
- permanent_loss_probability — INVESTIGATE: insolvency risk is low, but valuation, design-win, control and capacity risks can create long-duration capital impairment.

Other vetoes are PASS on current evidence. Persistent dilution is PASS with monitor rather than a failure: share count rose, but the evidence does not yet establish structurally excessive long-duration dilution.

## Key red-team concern

The market may be capitalizing current AI power demand as if MPWR will hold design share through multiple accelerator and power-architecture transitions. A shift to 800V, broader grid-to-core competitors, underutilized new capacity, working-capital absorption or another accounting-control failure can simultaneously compress owner cash and the valuation multiple.

## Repository safety

This run is additive-only. It must not modify:

- `companies/MPWR/latest.json`
- `registry/companies.json`
- `reviews/latest.json`
- canonical `companies/MPWR/raw-data/*`
- `harness/baseline-lock.json`
- frozen deterministic outputs

The current canonical authority remains the 2026-09-06 PRELIMINARY_REVIEW pending a separate reviewed authority-promotion run. No claim is made that the local frozen deterministic validator was executed for this additive checkpoint.

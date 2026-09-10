# 2026-09-10 Samyang Foods deep research checkpoint

## Result

- Ticker: `003230`
- Company: Samyang Foods
- Research status: `FULL_ANALYSIS_CHECKPOINT`
- Decision: `WATCH`
- Priority: `P1`
- Buy authorized: `false`
- Position band: `NONE`
- Business quality: `61/75`
- Total score: `80/100` — Emerging Outlier
- Hard Veto: `INVESTIGATE`
- Open veto items: `incremental_roic_collapse`, `fatal_concentration`

## What changed from the 2026-09-08 preliminary checkpoint

The prior checkpoint established primary financial, cash-flow, balance-sheet, audit and capacity evidence but withheld expectation-gap and asymmetry scoring. This run adds a synchronized September 10 close, TTM bridge, reverse expectations, Bear/Base/Bull owner-cash scenarios, Q2 regional growth, Buldak scale/demand evidence, KRX Value-Up capacity evidence and the July controlling-group pledge disclosure.

The business-quality score remains 61/75 rather than being raised simply because Q2 growth was strong. The new information mainly closes the valuation gate: at KRW 1.264m, current price does not require an obviously unrealistic Bull case under reasonable normalized owner-cash assumptions. However, maintenance capex is not separately disclosed and mature incremental ROIC for Miryang Plant 2 / the future China plant is not yet demonstrated. Exact Buldak revenue/profit concentration also remains unknown.

## Valuation checkpoint

Using a 10% required return and explicit owner-cash assumptions:

- Bear: ~KRW 0.591m/share
- Base: ~KRW 1.696m/share
- Bull: ~KRW 3.281m/share
- Reverse expectation at 15% normalized owner-cash margin and 18x terminal multiple: ~7.25% annual revenue growth for ten years
- Reverse expectation at 12% owner-cash margin: ~10.17%

These are analyst estimates, not company guidance or target prices. Mechanical TTM OCF minus PPE is only about KRW 221bn and is not treated as normalized owner FCF.

## Investment interpretation

Samyang is increasingly consistent with a global branded-food outlier: Buldak scale, broad regional growth, mainstream distribution expansion and sustained 20%+ operating margin provide strong evidence that the franchise is more than a one-quarter trend. The remaining hurdle is durability of per-share cash compounding. Position authorization therefore waits for evidence on plant-level incremental returns, maintenance capex, brand-level concentration and end-consumer sell-through rather than reacting to price alone.

## Repository safety

This run is additive-only. It intentionally does **not** change:

- `companies/003230/latest.json`
- `registry/companies.json`
- `reviews/latest.json`
- `companies/003230/raw-data/*`
- `harness/baseline-lock.json`
- frozen deterministic outputs

Current canonical authority remains the 2026-09-06 preliminary review pending a separate reviewed authority-promotion run. The deep checkpoint is preserved for that future promotion without silently breaking current harness reproducibility.

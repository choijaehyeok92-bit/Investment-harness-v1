# PWR 2026-09-10 Deep Research Checkpoint

## Decision
- WATCH / P1
- buy_authorized: false
- position_band: NONE
- business quality: 60/75
- total score: 68/100 (Starter / Watch score-band only)
- open Hard Veto: incremental_roic_collapse, permanent_loss_probability

## Evidence update
Q2 2026 revenue was $9.56B and common net income $451.4M. H1 revenue reached $17.432B, up 34% YoY, while acquired businesses contributed roughly $1.73B of the increase. June RPO was $33.55B and non-GAAP backlog $53.44B. The distinction matters: backlog additionally contains estimated MSA orders, estimated renewals and certain non-fixed-price contracts.

Harness-rule TTM diagnostics are approximately $32.906B revenue, $1.327B common net income, $3.178B CFO, $0.787B capex and $2.391B mechanical OCF-capex. After one-time economic recognition of TTM SBC (~$0.226B), conservative cash diagnostic is ~$2.165B. This is not normalized owner FCF.

## Valuation
September 10 completed-session close: $618.73.

9% hurdle scenarios:
- Bear: $118.96
- Base: $479.64
- Bull: $1,094.14

At the current price, Base is about 22.5% below market. Holding Base owner-margin and 18x terminal assumptions requires approximately 11.86% annual revenue growth in years 2-10 after $39.5B year-1 revenue. This is demanding but not demonstrably impossible; therefore `price_requires_unrealistic_bull_case` remains PASS with valuation monitor rather than becoming an open veto.

## Capital allocation
2025 acquisition cash spending was about $3.05B; H1 2026 acquisition cash spending was about $0.93B. The Q2-July Phalcon/Percheron/PSD/Enerfab transactions carried about $1.24B upfront consideration and up to $0.242B contingent consideration. The strategic logic is coherent, but post-close incremental ROIC is not yet observable. Accordingly `incremental_roic_collapse` remains INVESTIGATE.

## Contract-quality note
Approximately 63.8% of FY2025 revenue used over-time percentage-of-completion accounting, and $983.6M of revenue at year-end was associated with unapproved change orders and claims under negotiation. This does not imply low-quality revenue, but it makes contract estimate revisions, claims collection and DSO mandatory monitoring items.

## Repository safety
This run is additive-only. It does not change companies/PWR/latest.json, registry/companies.json, reviews/latest.json, canonical raw-data, harness/baseline-lock.json or frozen deterministic outputs. Canonical authority remains the 2026-09-06 preliminary review until a separate reviewed promotion.

## Validation note
GitHub-side structural compare is used to verify additive-only scope. No claim is made that a local deterministic validator was executed for this checkpoint.

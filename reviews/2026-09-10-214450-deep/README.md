# PharmaResearch (214450) 2026-09-10 Deep Research Checkpoint

## Decision

- WATCH / P1
- buy_authorized: false
- position_band: NONE
- business quality: 60/75
- total score: 81/100 — Emerging Outlier
- required return: 10%
- reference price: KRW349,500 (2026-09-10 completed-session secondary reference)
- retained Bear / Base / Bull: KRW160,183 / KRW633,662 / KRW1,541,105
- reverse expectation: ~4.53% annual revenue growth in years 2-10 after Base year-1 revenue KRW0.78T

## What changed versus 2026-09-06 canonical

The canonical assessment was WATCH / P1 at 55/75 business quality and 74/100 total score. This checkpoint raises business quality to 60/75 and total score to 81/100.

The evidence upgrade comes from international commercialization rather than narrative alone:
- H1 exports KRW142.8B, +47% YoY, 44% of consolidated sales
- Q2 export share 47%
- VIVACY 22-country European distribution framework and 2026 physician rollout
- CG USA acquisition agreement establishing U.S. cosmetics manufacturing/localization
- Plant 5 capacity build for raw materials and cosmetics
- stronger shareholder-return policy

The price also fell from the prior KRW386,500 reference to KRW349,500, reducing the reverse-growth requirement from ~5.90% to ~4.53%.

## Cash-quality discipline

Harness-rule TTM:
- revenue KRW0.604T
- operating income KRW0.238T
- net income KRW0.195T
- OCF KRW0.173T
- PPE purchases KRW0.035T
- mechanical OCF-PPE KRW0.138T

OCF-PPE is not normalized owner FCF. H1 net income grew roughly 34.5% YoY while OCF fell roughly 13.8%, so working capital, distributor sell-through and growth investment remain explicit gates.

## Preferred-share discipline

The CVC/Polish Company RCPS remains outstanding as a material preferred claim. Primary valuation uses the current common denominator and deducts the preferred redemption claim once. The alternate conversion sensitivity removes that claim before adding conversion shares. The two treatments are never stacked.

This keeps `persistent_dilution` at INVESTIGATE even though the current price remains below Base under either treatment.

## Open Hard Veto gates

- `persistent_dilution` — INVESTIGATE: 1.175647M RCPS can materially change the common-share denominator/claim structure.
- `incremental_roic_collapse` — INVESTIGATE: Plant 5 and CG USA have not yet produced observable post-ramp returns.
- `fatal_concentration` — INVESTIGATE: geographic and product-category diversification is improving, but economic value remains heavily tied to the REJURAN brand/PN ecosystem.

All other vetoes are PASS on current evidence. In particular, current price no longer requires a Bull-only path.

## Key red-team concern

The market may correctly see a global aesthetics winner while still overestimating how much of early export shipment becomes durable sell-through. A simultaneous slowdown in physician adoption, adverse U.S. regulatory path, lower post-expansion ROIC and unfavorable RCPS resolution could reduce per-share owner cash even if reported revenue keeps growing.

## Repository safety

This run is additive-only. It must not modify:
- `companies/214450/latest.json`
- `registry/companies.json`
- `reviews/latest.json`
- canonical `companies/214450/raw-data/*`
- `harness/baseline-lock.json`
- frozen deterministic outputs

Current canonical authority remains `2026-09-06-deep` pending a separate reviewed authority-promotion run. No claim is made that the local frozen deterministic validator was executed for this additive checkpoint.

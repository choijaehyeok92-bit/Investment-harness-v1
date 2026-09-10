# ANET — 2026-09-10 Deep Research Checkpoint

## Status

- Decision: **WATCH**
- Priority: **P1**
- Business quality: **68/75**
- Total score: **79/100**
- Classification: **Emerging Outlier**
- Buy authorized: **false**
- Position band: **NONE**
- Hard Veto overall: **INVESTIGATE**
- Open gates: `fatal_concentration`, `permanent_loss_probability`

This is an **additive-only research checkpoint**. It intentionally does not update `companies/ANET/latest.json`, `registry/companies.json`, `reviews/latest.json`, canonical raw-data, `harness/baseline-lock.json`, or frozen deterministic outputs. Current canonical authority remains `2026-09-06-deep` until a separate reviewed authority-promotion run.

## What changed versus 2026-09-06

The prior deep run already identified Arista as a high-quality AI/data-center network platform but left several filing details as missing evidence. This checkpoint resolves those items and adds independent AI-Ethernet market-share evidence.

Key updates:

- Q2 revenue: **$3.036B**, +37.7% YoY; GAAP operating margin **45.4%**.
- FY2026 management revenue guide: approximately **$12.6B**, roughly +40%.
- Etherlink cumulative AI-fabric customers: **>100** per management commentary.
- 1.6T Etherlink expands scale-up, scale-out and scale-across; production ramp expected primarily in 2027.
- H1 OCF **$2.777B**; H1 SBC **$241.3M**.
- June cash + marketable securities **$13.343B**.
- Non-cancellable purchase commitments **$9.7B**, including **$9.4B due for receipt within 12 months**.
- No share repurchases in H1 2026; **$817.9M** authorization remained.
- July 30 shares outstanding **1.2612B** versus 1.2565B at 2025 year-end.
- Two FY2025 end customers were **26% and 16%** of revenue.
- Dell'Oro ranked Arista third in 2Q 2026 AI back-end Ethernet switch sales behind Celestica and NVIDIA, while noting deferred Arista AI revenue would narrow the gap.
- September 9 close: **$192.93**.

## Harness-rule TTM diagnostics

Using `FY2025 + H1 2026 - H1 2025`:

- Revenue: **$10.5408B**
- Operating income: **$4.5469B**
- GAAP net income: **$4.0446B**
- OCF: **$5.3066B**
- Mechanical OCF minus disclosed capex-line: **$5.1553B**
- SBC: **$0.5023B**
- Mechanical OCF minus disclosed capex-line minus SBC: **$4.6530B**

The last measure is a diagnostic, **not normalized owner FCF**. H1 OCF benefited from working-capital timing, especially deferred revenue, and the FY2025 versus H1 capex-line definitions are not perfectly identical.

## Valuation

Retain the 2026-09-06 long-horizon scenario economics for comparability and update the price/reverse expectations only.

- Bear: **$57.05** / current price = 0.30x
- Base: **$166.11** / current price = 0.86x
- Bull: **$358.00** / current price = 1.86x
- 9% hurdle reverse growth, years 2-10: **~16.82% annually**
- Two-state Bear/Bull price-position diagnostic: **~45.2% Bull weight**, not a probability estimate

Current price is still above the retained Base value and the margin of safety is inadequate. The reverse-growth requirement is demanding but not sufficiently unrealistic to trip the `price_requires_unrealistic_bull_case` veto because 2026 revenue guidance is still growing around 40% and AI networking has strong structural tailwinds.

## Hard Veto interpretation

### `fatal_concentration` — INVESTIGATE

Two end customers represented 26% and 16% of FY2025 revenue. Large customers receive more favorable pricing and contract terms, and customer capex/vendor-allocation changes can affect both growth and gross margin. The gate remains open until genuine diversification is visible in revenue and cash, not merely customer-count announcements.

### `permanent_loss_probability` — INVESTIGATE

The permanent-loss mechanism is not bankruptcy. It is a combination of customer concentration, AI-Ethernet competitive share shifts, $9.7B of non-cancellable purchase commitments, working-capital reversal and valuation-duration compression.

All other hard vetoes are PASS with monitoring. The purchase commitments do not meet the harness definition of `low_quality_growth`, which is subsidy/marketing-dependent growth, and current evidence does not demonstrate structural `incremental_roic_collapse` or persistent `moat_shrinkage`.

## Red-team result

**REVISE_NOT_REJECT.** The company quality thesis survives, but the evidence does not justify buy authorization at the current expectation gap.

## Evidence required for upgrade

Upgrade requires multiple confirming signals: 1.6T conversion from trials into 2027 production, durable AI-Ethernet share, lower economic customer concentration, supply commitments converting into shipments/cash without inventory charges, and continued growth in SBC-adjusted cash per share. Price decline alone is not sufficient.

## Repository safety

The checkpoint is designed to preserve the deterministic current-authority surface. A separate reviewed promotion should be used if this run is later selected as canonical authority.

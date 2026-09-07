# SNOW raw extraction + preliminary review — 2026-09-08

This directory is a **non-current research checkpoint** created from user-supplied primary filings.

## Sources reviewed

- FY2026 Form 10-K, fiscal year ended 2026-01-31
- Q2 FY2027 Form 10-Q, quarter/six months ended 2026-07-31
- 2026-09-02 Form 8-K + Exhibit 99.1 earnings release
- 2026 annual-meeting proxy supplement
- 2026-09-04 Form 144 — Mark S. Garrett
- 2026-09-04 Form 144 — Michael L. Speiser

Raw facts and derived mechanical metrics are stored in `raw-data.json`.

## Preliminary conclusion

- **Research state:** PARTIAL_ANALYSIS
- **Decision:** WATCH
- **Priority:** P1
- **Business quality:** 55/75
- **Buy authorized:** false
- **Valuation gate:** open; no synchronized quote/reverse DCF

Snowflake's operating evidence improved materially versus the prior screen-only checkpoint. Q2 FY2027 product revenue grew about 37%, NRR was 126%, RPO was $9.0B (+30% YoY), and customers above $1M TTM product revenue reached 828. Management raised FY2027 product-revenue guidance to 36% growth.

The central unresolved issue is per-share owner economics. FY2026 stock-based compensation of $1.60B exceeded company-defined FCF of $1.12B. H1 FY2027 company FCF was $316.6M versus $826.1M SBC, while $327.7M of cash taxes on net share settlement were classified in financing cash flow and therefore excluded from the company's FCF definition. Ending shares rose about 3.0% in FY2026 and another 2.5% in H1 FY2027 despite repurchases.

AI adoption is a positive structural signal, but third-party cloud infrastructure including AI inference/GPU costs increased to about 75% of product cost in Q2 FY2027. The amended AI-service minimum-spend commitment totals $390M, with $270M remaining at July 31, 2026. This keeps incremental AI ROIC open for investigation.

## Authority / reproducibility guardrail

This PR is intentionally **additive-only**. It must not modify:

- `companies/SNOW/latest.json`
- current registry authority
- `harness/baseline-lock.json`
- canonical `companies/SNOW/raw-data/`
- `reviews/latest.json`
- frozen deterministic harness outputs

The existing 2026-09-06 PRELIMINARY_REVIEW remains current authority until a separate canonical harness run promotes this checkpoint.

## Next work

1. Current quote + 9% reverse DCF / Bear-Base-Bull.
2. Eight-quarter gross dilution bridge.
3. Owner FCF/share model avoiding SBC/dilution double counting.
4. AI workload contribution margin and cloud commitment utilization.
5. Independent competitive-share and retention evidence.
6. Observe/Natoma acquisition cash ROIC.

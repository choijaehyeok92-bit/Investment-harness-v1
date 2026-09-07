# 003230 / 삼양식품 — 2026-09-08 raw extraction & preliminary review

## Scope

사용자 제공 DART PDF 2건을 기반으로 원자료를 구조화하고, 비권위 초벌분석 체크포인트를 생성했다.

### Sources

1. `[삼양식품]사업보고서(2026.03.18).pdf`
   - FY2025
   - 318 pages
   - SHA256 `60408796281d15127879d81a68a071cd4c4b1e50529a31e8be74d30ac6f9abc5`
2. `[삼양식품]반기보고서(2026.08.14).pdf`
   - H1 2026
   - 196 pages
   - SHA256 `dff8b65d50dfe4b8ff3cd6f7178a9dd14433503813fbcc85b7b699f847123b17`

## Checkpoint conclusion

- Research state: `PARTIAL_ANALYSIS`
- Decision: `WATCH`
- Priority: `P1`
- Buy authorized: `false`
- Business quality: `61/75`
- Valuation: withheld pending synchronized market price and 10% reverse DCF

### Key positives

- FY2025 revenue +36.1%, operating income +52.1%.
- H1 2026 revenue +37.2%, operating income +39.1%, net income +54.1%.
- H1 2026 OCF +107.6% YoY and simple OCF-PPE diagnostic recovered to about KRW 164.9bn.
- Export product sales were mechanically about 82.9% of H1 2026 total sales.
- Cash + short-term financial assets exceeded borrowings excluding leases at 2026-06-30.
- FY2025 audit and internal accounting-control audit were unqualified; no material weakness was reported.
- Issued shares remained 7,533,015 from 2025 year-end to 2026-06-30.

### Open gates

- Exact Buldak brand concentration and independent regional sell-through are not disclosed.
- Milyang second-factory / follow-on capex requires post-ramp incremental ROIC validation.
- Noodle/snack is about 90.6% of H1 2026 sales, so concentration remains material.
- Headquarters property acquisition of KRW 227bn and related-party economics require capital-allocation review.
- No synchronized quote, reverse DCF, or Bear/Base/Bull scenario was run.

## Hard-veto disposition

PASS:
- management_or_accounting_integrity
- external_capital_dependence
- persistent_dilution
- low_quality_growth

INVESTIGATE:
- incremental_roic_collapse
- moat_shrinkage
- price_requires_unrealistic_bull_case
- fatal_concentration
- permanent_loss_probability

## Authority / reproducibility guardrail

This review is intentionally **additive-only**.

It does **not** change:
- `companies/003230/latest.json`
- current registry authority
- `harness/baseline-lock.json`
- canonical `companies/003230/raw-data/`
- `reviews/latest.json`
- frozen/generated current-run outputs

The structured extraction is staged under this review directory, so merely adding supplied evidence does not silently change current deterministic harness outputs. A separate canonical run is required to promote the checkpoint.

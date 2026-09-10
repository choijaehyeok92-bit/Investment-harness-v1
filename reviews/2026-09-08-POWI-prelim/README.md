# POWI raw extraction / preliminary review checkpoint — 2026-09-08

## Scope correction

The user request said `PWR`, but all six supplied documents are filings of **Power Integrations, Inc. (NASDAQ: POWI)**. The repository already uses `companies/PWR` for **Quanta Services**. To prevent issuer contamination, this checkpoint is stored entirely under `reviews/2026-09-08-POWI-prelim/` and does **not** alter `companies/PWR` or create canonical POWI authority.

## Files

- `raw-data.json` — structured extraction from the six supplied documents, including source hashes and mechanical diagnostics.
- `assessment.json` — non-current PARTIAL_ANALYSIS assessment; WATCH / P1; business-quality subtotal 53/75; valuation withheld.
- `thesis.ko.md` — Korean preliminary investment thesis and falsifiers.

## Source set

1. Form 3 — Andrew S. Hughes initial beneficial ownership, event 2026-07-28.
2. FY2025 Form 10-K.
3. 2026 definitive additional proxy materials.
4. Form 8-K — Sunil Gupta resignation notice, event 2026-08-11.
5. Q2/H1 2026 Form 10-Q.
6. 2026 definitive proxy statement.

## Preliminary findings

- FY2025 revenue $443.5M, +5.9%; gross margin 54.5%; GAAP operating income $10.2M, -43.1%.
- FY2025 OCF $111.5M and simple FCF $87.1M; SBC $39.7M, about 45.6% of simple FCF.
- FY2025 repurchases $98.1M and dividends $47.2M; total capital return about 1.67x simple FCF. Year-end share count fell about 2.6%.
- H1 2026 revenue $227.2M, +2.6%; gross margin 53.5% vs 55.2%; OCF $42.0M, -24.2%; simple FCF $35.7M, -18.4%.
- H1 2026 industrial end-market mix rose to 42% from 37%, but distributor mix was 72% and Asia bill-to mix 81%.
- H1 2026 largest customer represented 31% of revenue; top-ten customers represented 90% of accounts receivable.
- PowiGaN is a material strategic option: company reports up to 1700V technology and targets AI data-center power, communications infrastructure and EV applications; higher-power vertical-GaN work remains multi-year.
- Strong liquidity: $262.6M cash + short-term investments, $98.5M total liabilities, $404.5M working capital, unused $100M revolver.
- Dilution needs a dedicated bridge: H1 shares rose about 0.8%, Aug. 3 share count was about 1.0% above year-end, and the 2026 proxy requested an additional 2.0M-share incentive reserve (~3.6% of record-date shares).
- Deloitte issued unqualified opinions on FY2025 financial statements and ICFR; H1 2026 disclosure controls were effective.
- CogniPower patent matter was closed in April 2026 without payment by Power Integrations. A former-employee wrongful-termination judgment remains on appeal; approximately $11.3M was reserved.
- Operations SVP Sunil Gupta resigned effective 2026-08-25; the company stated there was no disagreement over operations, policies or practices.

## Preliminary decision

- `research_state`: PARTIAL_ANALYSIS
- `decision`: WATCH
- `priority`: P1
- `buy_authorized`: false
- `business_quality_75`: 53
- `total_score_100`: withheld because synchronized price / reverse DCF is missing
- US required-return hurdle for next valuation run: 9%

## Hard-veto checkpoint

PASS:
- management/accounting integrity
- external-capital dependence

INVESTIGATE:
- persistent dilution
- low-quality growth
- incremental ROIC collapse
- moat shrinkage
- price requires unrealistic bull case
- fatal concentration
- permanent-loss probability

## Reproducibility / authority safety

This PR is intentionally **additive-only**. It does not modify:

- `companies/PWR/**`
- any `companies/POWI/raw-data/**` canonical path
- any issuer `latest.json`
- registry/current-authority files
- `harness/baseline-lock.json`
- `reviews/latest.json`
- frozen deterministic outputs

Therefore this checkpoint should not promote POWI into the canonical universe or alter the current Quanta Services (`PWR`) assessment. A later canonical run can explicitly register POWI after synchronized valuation and validator-compatible current artifacts are generated.

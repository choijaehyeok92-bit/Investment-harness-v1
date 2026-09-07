# APP raw extraction / preliminary review - 2026-09-08

## Status

- Ticker: `APP`
- Research checkpoint: `PARTIAL_ANALYSIS`
- Decision: `WATCH`
- Priority: `P1`
- Buy authorized: `false`
- Business-quality subtotal: `61/75`
- Valuation / expectation-gap score: withheld
- Current registry authority: unchanged (`companies/APP/latest.json` remains 2026-09-06 PRELIMINARY_REVIEW)

## Files added in this checkpoint

- `reviews/2026-09-08-app-prelim/raw-data.json`
- `companies/APP/analyses/2026-09-08-prelim/assessment.json`
- `companies/APP/analyses/2026-09-08-prelim/thesis.ko.md`
- this README

## Source package

The supplied package contained a 2026 definitive proxy, definitive additional proxy materials, Q2 2026 earnings Form 8-K / Exhibit 99.1, five Form 4 filings dated around the 2026-08-20 vesting event, and one Form 144 for Vasily Shikin.

One additional upload, `d6d59334-570b-453f-8c55-30d0bda96a8e(1).pdf`, is 1,104,599 zero bytes and is not a readable PDF. It was hashed and recorded in `raw-data.json`, but no factual inference was made from it. Because no readable supplied 10-K or 10-Q was available, this checkpoint does not claim direct audit/ICFR or full quarterly-risk-factor verification.

## Key extracted observations

- Q2 2026 revenue: $1.924B, about +53% YoY
- Q2 GAAP operating income: $1.494B, mechanically about 77.7% operating margin
- Q2 net income: $1.267B
- Q2 Adjusted EBITDA: $1.614B, 84% reported margin
- Q2 OCF: $869.0M; company-defined FCF: $863.3M
- Q2 SBC: $85.8M, about 4.5% of revenue
- H1 2026 revenue: $3.766B, about +56% YoY
- H1 net income: $2.472B, about +77% YoY
- H1 OCF: $2.160B, about +35% YoY
- H1 common-stock repurchases: $1.533B
- Ending shares: 335.3M versus 338.3M at 2025 year-end, about -0.9%
- H1 diluted weighted-average shares: about -1.6% YoY
- Cash: $3.053B; long-term debt: $3.515B; net debt about $462M
- Q3 revenue guidance: $2.055B-$2.085B; Adjusted EBITDA margin 83%

## Governance / insider observations

- 6 of 9 director nominees are independent, the chair is independent, and standing committees are fully independent.
- Adam Foroughi has about 61.6% total voting power; Voting Agreement parties have about 66.9%.
- Class B carries 20 votes per share versus one vote for Class A.
- The board opposed a stockholder proposal requesting vote-result disclosure by share class.
- The five supplied 2026-08-20 Form 4 transactions are issuer tax-withholding transactions (`F` code), explicitly not sales by the reporting persons.
- Vasily Shikin filed a Form 144 for a proposed 117,598-share sale. The supplied filing does not disclose a Rule 10b5-1 plan adoption date, so no preplanned-sale or bearish characterization is inferred.

## Why additive-only

This checkpoint intentionally does **not** modify:

- `companies/APP/latest.json`
- current registry files
- `harness/baseline-lock.json`
- `companies/APP/raw-data/`
- `reviews/latest.json`
- frozen deterministic outputs

The raw extraction is staged under `reviews/` rather than canonical `companies/APP/raw-data/` so the current harness authority and reproducibility remain unchanged until a separate canonical promotion run is performed.

## Next gate

A full APP promotion should obtain a readable FY2025 10-K and Q2 2026 10-Q, then complete synchronized current-price work, 9% reverse DCF, Bear/Base/Bull scenarios, independent advertiser ROAS/retention validation, customer/platform concentration, and an eight-quarter share-count bridge.

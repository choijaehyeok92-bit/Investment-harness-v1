# 2026-09-08 Hugel (145020) preliminary research checkpoint

## Purpose

User-requested raw-data extraction and preliminary review from three supplied DART filings:

1. FY2025 business report filed 2026-03-20
2. H1 2026 half-year report filed 2026-08-14
3. Treasury-stock disposition report filed 2026-08-06

This is an **additive-only, non-current research checkpoint**. It intentionally does not modify:

- `companies/145020/latest.json`
- the current registry authority
- `harness/baseline-lock.json`
- canonical `companies/145020/raw-data/`
- frozen deterministic build outputs
- global `reviews/latest.json`

The current canonical authority therefore remains the 2026-09-06 `PRELIMINARY_REVIEW` until a separate harness promotion run.

## Files

- `reviews/2026-09-08-145020-prelim/raw-data.json`
- `companies/145020/analyses/2026-09-08-prelim/assessment.json`
- `companies/145020/analyses/2026-09-08-prelim/thesis.ko.md`

## Preliminary result

- Research state: `PARTIAL_ANALYSIS`
- Decision: `WATCH`
- Priority: `P1`
- Buy authorized: `false`
- Business quality: **61 / 75**
- Valuation score: withheld
- Total score: withheld
- KR required-return gate: **10%**

### What improved materially

- FY2025 revenue +14.0% and operating income +20.8%.
- H1 2026 revenue +27.2%, toxin +45.7%, Americas +109.5%, OCF +46.9%.
- Export mix is about 65% and Letybo has approval footprints across the U.S., Europe and China.
- H1 balance sheet held about KRW 601.1bn of cash plus short-term deposits against about KRW 104.1bn of total liabilities.
- Remaining convertible bonds were converted after period end and extinguished.

### Why this is still WATCH

- H1 operating margin fell from about 47.8% to 40.7% while SG&A expanded rapidly.
- Hugel America and subsidiaries grew revenue about 36.7% but swung to an H1 net loss.
- H1 stock-compensation expense rose to about KRW 9.6bn; post-period CB conversion added 211,140 shares and option/RSU treasury-share delivery remains part of the capital structure.
- Korean Pharmaceutical Affairs Act / MFDS litigation and the U.S. ITC appeal remain open legal/regulatory gates.
- No synchronized quote, reverse DCF or Bear/Base/Bull analysis was run.

## Hard-veto checkpoint

- `management_or_accounting_integrity`: INVESTIGATE — clean audit but real legal/regulatory cases remain open.
- `external_capital_dependence`: PASS.
- `persistent_dilution`: INVESTIGATE.
- `low_quality_growth`: PASS.
- `incremental_roic_collapse`: INVESTIGATE.
- `moat_shrinkage`: INVESTIGATE.
- `price_requires_unrealistic_bull_case`: INVESTIGATE.
- `fatal_concentration`: INVESTIGATE.
- `permanent_loss_probability`: INVESTIGATE.

## Next research

1. Synchronize current quote, market cap, net cash and fully diluted shares.
2. Run 10% reverse DCF and Bear/Base/Bull cases.
3. Validate independent U.S./Europe/China sell-through, physician adoption, market share and ASP.
4. Build Hugel America contribution-margin and break-even bridge.
5. Check current Korean administrative/criminal appellate dockets and U.S. Federal Circuit ITC appeal status.
6. Build 8-quarter share/SBC/option/RSU/CB/treasury-cancellation bridge.
7. Separate maintenance vs growth capex and assess capitalized development spending.

## Source integrity

The raw extraction records supplied-document SHA-256 hashes and distinguishes filing facts from calculations and investment inference. Company claims about competitive position, market leadership and procedure repeat behavior remain company assertions until independently verified.

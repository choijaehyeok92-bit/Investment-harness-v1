# AMD raw-data extraction and preliminary analysis — 2026-09-08

## Scope

This review packet records a user-requested AMD raw-data extraction and preliminary harness analysis from four supplied SEC XBRL archives and two user-specified AMD IR filing URLs.

Files:

- `raw-data.json`: structured extraction plus explicitly labeled mechanical derived metrics.
- `companies/AMD/analyses/2026-09-08-prelim/assessment.json`: preliminary evidence/score/veto checkpoint.
- `companies/AMD/analyses/2026-09-08-prelim/thesis.ko.md`: Korean research memo.

## Important authority boundary

This packet is intentionally **not** wired into `companies/AMD/latest.json`, `registry/companies.json`, the frozen 2026-09-06 baseline, or `reviews/latest.json`. The current canonical harness authority therefore remains unchanged.

Reason: the frozen renderer and baseline lock treat `companies/<ticker>/raw-data/*.json` as part of the reproducible 2026-09-06 run. Mutating that historical run for a new September 8 input would rewrite prior research history. This packet is stored as a dated review artifact so it can be merged without breaking historical reproducibility. A future canonical AMD run can promote the verified extraction through a new dated renderer/run rather than silently altering the old one.

## Key preliminary findings

- FY2025 revenue $34.639B; Data Center revenue $16.635B.
- Q2 2026 revenue $11.536B; Data Center revenue $6.718B (+107% YoY).
- H1 2026 continuing OCF $5.321B; capex $1.197B; SBC $0.990B.
- Cash + short-term investments $13.111B versus about $3.3B aggregate principal debt at June 27, 2026.
- Unconditional commitments increased from about $12.2B at FY2025 to $30.3B at June 27, 2026.
- OpenAI and Meta each received conditional warrants for up to 160M AMD shares at $0.01; no tranches had vested or become exercisable by June 27, 2026.
- Preliminary business-quality score: 56/75. Expectation-gap and asymmetry scores are withheld pending synchronized valuation and a fully diluted share bridge.
- Decision remains WATCH; no buy authorization.

## Validation expectation

Because the packet does not alter frozen raw-data directories or current authority pointers, the existing harness reproducibility/validation contract should remain unchanged. The branch should therefore be mergeable without rewriting the 2026-09-06 baseline.

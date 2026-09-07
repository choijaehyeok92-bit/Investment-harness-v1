# MPWR primary-source checkpoint - 2026-09-08

## Scope

사용자 제공 자료 4건을 구조화해 MPWR의 기존 `PRELIMINARY_REVIEW`를 보강하는 **비권위 PARTIAL_ANALYSIS 체크포인트**를 작성했다.

### Supplied documents

1. `MPS_2025_Form_10-K.pdf` - FY2025 Form 10-K, 83 pages, SHA256 `7fb80ea5e8de46cc2580e80a93d1e043c49f43011ee0b552afe559ec0c5619be`
2. `2025_Proxy_Final_IR_Website_.pdf` - 2026 Definitive Proxy Statement, 58 pages, SHA256 `fc659161bb91a070b194b61886e8cd94ef2e98b2fcba80e9eb7e26e71d893153`
3. `MPWR_Q2_26_10-Q.pdf` - Q2/H1 2026 Form 10-Q, 34 pages, SHA256 `8ba0f2bfdb74f8b3e3d89951a0044d95f58cc832c7cfeecd1189b81eaf747d70`
4. `Q2_2026_Earnings_Release_8-K.pdf` - July 30, 2026 Form 8-K Item 2.02 wrapper, 3 pages, SHA256 `8f93a80d635bc9c6bf2196832bf68a1ef475a107fc82ca0f7af439794520599b`

**8-K limitation:** 제공된 3페이지 PDF에는 Exhibit 99.1 earnings release 본문이 포함되어 있지 않다. 따라서 해당 wrapper에서 Q3 guidance나 별도 non-GAAP 수치를 추정하지 않았다.

## Files added

- `reviews/2026-09-08-mpwr-prelim/raw-data.json`
- `companies/MPWR/analyses/2026-09-08-prelim/assessment.json`
- `companies/MPWR/analyses/2026-09-08-prelim/thesis.ko.md`
- `reviews/2026-09-08-mpwr-prelim/README.md`

## Preliminary result

- `research_state`: `PARTIAL_ANALYSIS`
- `decision`: `WATCH`
- `priority`: `P1`
- `business_quality_75`: `61`
- `total_score_100`: `null`
- `buy_authorized`: `false`

Valuation/expectation gap과 power-law/asymmetry는 동기화 현재가, fully diluted shares, reverse DCF 및 Bear/Base/Bull 없이는 점수화하지 않았다.

## Key evidence promoted from screening to primary-source review

- Q2 2026 revenue +47.6% YoY; Enterprise Data +164.3%, company-attributed primarily to AI/server power-management demand.
- Q2 gross margin 55.2%; H1 operating income +63.4% while H1 revenue +37.1%.
- FY2025 OCF $838.2M vs PPE purchases $172.0M; H1 2026 OCF $478.2M vs PPE purchases $153.3M.
- H1 OCF fell 3.2% YoY despite revenue growth because working-capital requirements increased, especially receivables and inventory.
- June 2026 cash + short-term investments $1.414B versus total liabilities $790.8M.
- FY2024/2025 deferred-tax restatement created a material weakness that remained unremediated at June 30, 2026.
- FY2025 shares outstanding increased about 1.85%; H1 2026 increased another 0.89% from year-end while SBC remained material.
- H1 2026 distribution channel share was 88%; direct-customer Asia share was 93%; June receivable concentration was 33%/20%/15% across three counterparties.

## Hard-veto posture

- `management_or_accounting_integrity`: INVESTIGATE
- `external_capital_dependence`: PASS
- `persistent_dilution`: INVESTIGATE
- `low_quality_growth`: INVESTIGATE
- `incremental_roic_collapse`: INVESTIGATE
- `moat_shrinkage`: INVESTIGATE
- `price_requires_unrealistic_bull_case`: INVESTIGATE
- `fatal_concentration`: INVESTIGATE
- `permanent_loss_probability`: INVESTIGATE

## Reproducibility / authority guardrail

This change is **additive-only**. It intentionally does **not** modify:

- `companies/MPWR/latest.json`
- current registry files
- `harness/baseline-lock.json`
- canonical `companies/MPWR/raw-data/`
- `reviews/latest.json`
- any frozen/deterministically generated current-authority output

Reason: placing supplied evidence directly under canonical `companies/MPWR/raw-data/` can change deterministic source-path inputs before a canonical promotion run. This checkpoint therefore stages extracted source data under the dated review directory and leaves current authority unchanged.

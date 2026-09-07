# 2026-09-08 리노공업(058470) raw extraction / preliminary review

## 목적

사용자 제공 DART 1차 원문 2건을 구조화하고, `companies/058470`의 기존 2026-09-06 `PRELIMINARY_REVIEW`를 덮어쓰지 않는 비권위 `PARTIAL_ANALYSIS` 체크포인트를 추가한다.

## 입력

1. `[리노공업]사업보고서(2026.03.18)(4).pdf`
   - FY2025
   - 205 pages
   - SHA256 `220070fe382dc74ec73bb15a9443c718becb013ebe383bda6a9235a05fc46e30`
2. `[리노공업]반기보고서(2026.08.14)(4).pdf`
   - H1 2026
   - 160 pages
   - SHA256 `f32c0bd17661294cb939fd85408f8ef76ffb7ae7a8d3f19769db2d60a790385a`

## 산출물

- `reviews/2026-09-08-058470-prelim/raw-data.json`
- `companies/058470/analyses/2026-09-08-prelim/assessment.json`
- `companies/058470/analyses/2026-09-08-prelim/thesis.ko.md`
- 본 README

## 핵심 숫자

- FY2025: 매출 3,725억원(+33.9%), 영업이익 1,770억원(+42.5%), 순이익 1,520억원(+34.2%)
- H1 2026: 매출 2,430억원(+27.3%), 영업이익 1,208억원(+36.7%), 순이익 1,063억원(+50.9%)
- H1 영업이익률 49.7%, Q2 51.3%
- FY2025 OCF-PPE 단순 진단 1,195억원; H1 2026 272억원(-43.7% YoY)
- 2026-06-30 차입금 0원, 금융자산 5,622억원, 총부채 801억원
- H1 수출 비중 83.7%, 반도체 관련 제품/상품 비중 91.8%
- 상위 3개 고객 비중 55.9% (A 23.8%, B 19.6%, C 12.5%)
- 신공장 계획 971.8억원 중 785.5억원 집행
- 최대주주 이채윤 지분 34.66% → 25.48% (700만주 시간외매매)

## 판정

- `WATCH / P1`
- 사업품질 `61/75`
- valuation / asymmetry score withheld
- `buy_authorized=false`
- 주요 INVESTIGATE: 신규 공장 incremental ROIC, moat durability, customer concentration, valuation/permanent-loss case

## Authority / reproducibility guardrail

이 PR은 **additive-only research checkpoint**로 유지한다.

다음 항목은 변경하지 않는다:
- `companies/058470/latest.json`
- current registry
- `harness/baseline-lock.json`
- canonical `companies/058470/raw-data/`
- `reviews/latest.json`
- frozen deterministic outputs

따라서 이 체크포인트 병합만으로 current authority가 승격되거나 신규 매수 승인이 발생하지 않는다.

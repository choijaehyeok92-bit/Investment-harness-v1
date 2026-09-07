# ETN 2026-09-08 원자료 추출 및 초벌분석 체크포인트

## 목적

사용자가 지정한 Eaton Corporation plc (ETN) 공시 4건을 정규화하고, 하네스 투자 원칙에 따라 원자료 기반 초벌분석을 수행한다.

## 입력 소스

- FY2025 Form 10-K — 2026-02-26
- Q2/H1 2026 Form 10-Q — 2026-07-31
- Q2 2026 earnings Form 8-K / Exhibit 99 — 2026-07-31
- Shawn M. Black Form 4 — 2026-09-03

QuoteMedia URL은 동일 날짜·형식의 SEC EDGAR 원문으로 해소하여 사용했다.

## 산출물

- `raw-data.json`: 보고 수치·회사 가이던스·인수·부채·backlog/order·Form 4 추출 및 제한적 기계 계산
- `companies/ETN/analyses/2026-09-08-prelim/assessment.json`: 하네스 8개 항목과 9개 hard-veto 초벌평가
- `companies/ETN/analyses/2026-09-08-prelim/thesis.ko.md`: 0~6단계 한글 초벌분석

## 현재 판단

- Decision: `WATCH`
- Research priority: `P1`
- Business quality: `59/75`
- Total score: `WITHHELD`
- Buy authorized: `false`
- Hard veto overall: `INVESTIGATE`

핵심 긍정 증거는 Electrical Americas/Global의 double-digit organic growth, 강한 orders/backlog, 높은 segment margin이다.

핵심 미해결 위험은 Boyd Thermal $9.55B 인수 이후 급증한 차입과 무형자산이 9% 미국 허들을 넘는 증분 ROIC를 만들 수 있는지 여부다.

## 저장 방식

이 체크포인트는 **additive-only**다. 다음 frozen/current authority 파일은 변경하지 않는다.

- `companies/ETN/latest.json`
- `registry/companies.json`
- `reviews/latest.json`
- `harness/baseline-lock.json`
- 2026-09-06 deterministic run outputs

따라서 이 체크포인트는 기존 하네스 재현성을 깨지 않으면서 후속 정밀분석의 입력으로 사용한다.

## 다음 게이트

1. backlog cancellation/termination terms 및 conversion history
2. Electrical price/volume 및 lead-time normalization
3. Boyd stand-alone cash ROIC
4. Mobility separation pro-forma
5. synchronized quote + reverse DCF
6. debt-service/deleveraging 포함 Bear/Base/Bull owner-cash model

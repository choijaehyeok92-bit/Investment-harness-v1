# PWR 원자료 추출 및 초벌분석 체크포인트 — 2026-09-08

## 목적

사용자 제공 Quanta Services, Inc. (`PWR`) SEC 공시 5건을 바탕으로 원자료 핵심치를 구조화하고, 하네스 기준의 초벌 투자논지와 Hard Veto 상태를 정리한다.

이 디렉터리는 **additive-only / non-current research checkpoint**다. 현재 authority를 승격하거나 deterministic build input을 바꾸지 않는다.

## 사용한 원문

| Form | 기간/일자 | SHA256 |
|---|---|---|
| 10-K | FY ended 2025-12-31, filed 2026-02-19 | `124ae931428b7c6206dc4be8fd4822bd5dc35aa0d46b748a66f714c7de94a80f` |
| 10-Q | quarter/H1 ended 2026-06-30, filed 2026-07-30 | `ab297234a4ba6b91c73a71550ce914d2409ef30e78ec0cbf07bea126faf670f3` |
| DEF 14A | filed 2026-04-10 | `0985006900ca1c7ead7ac339146c757c80a3f7658d0e2afda01540ae5d94d8e1` |
| DEFA14A | filed 2026-04-10 | `bad1f0fd64a8c8cf735ed46141d0bc6a6466066616b036cc52ea55006212dde7` |
| 8-K | event 2026-08-06 | `7bd3b392c816dbcd4c70a4594e255a00fb3e68f6be672cd934a417a9c716d26e` |

## 생성 파일

- `raw-data.json` — 원문에서 추출한 수치·사실, 계산치, 미확인 항목을 분리한 구조화 데이터
- `assessment.json` — PARTIAL_ANALYSIS 후보 초벌 평가, 점수 및 9개 Hard Veto
- `thesis.ko.md` — 한국어 초벌 투자논지
- `README.md` — 범위·안전성·핵심 결론

## 핵심 결과

- **Decision:** WATCH
- **Buy authorization:** 없음
- **Next research priority:** P1 후보
- **Business quality subtotal:** 60/75
- **Total score:** 밸류에이션 gate 미완료로 보류
- **가장 중요한 열린 veto:** `incremental_roic_collapse`
- **추가 열린 veto:** `price_requires_unrealistic_bull_case`, `permanent_loss_probability`

### 확인된 강점

1. 2025 매출 $28.48B(+20.3%), 영업이익 $1.61B(+19.7%).
2. Q2 2026 매출 +41.1%, 영업이익 +87.6%; 연결 및 두 segment 모두 margin 상승.
3. 2026-06-30 backlog $53.44B(+21.5% vs 2025 YE), RPO $33.55B(+41.2%).
4. 계산상 2025 단순 FCF 약 $1.62B; 2023~2025 CAGR 약 19.2%.
5. 단일 고객 10% 이상 매출/매출채권 노출이 없음.
6. 2025 감사 및 ICFR 무수정, Q2 2026 disclosure controls effective.

### 핵심 리스크

1. 2025 인수 현금 약 $3.05B, H1 2026 약 $1.09B 현금 + 주식 추가 투입: cohort ROIC 미검증.
2. 2026-06-30 장기부채 의무 약 $6.10B 이후 8월에 추가 $2.0B senior notes 발행.
3. 제공된 8-K만으로는 8월 채권의 use of proceeds를 확정할 수 없음.
4. H1 2026 OCF 증가는 약 $455M의 우호적 YoY working-capital swing 영향을 받음.
5. 고정가 대형 프로젝트의 원가·claim·일정·노무 리스크.
6. Proxy에 일부 related-party lease 및 가족 고용 거래가 공시됨. 현재 integrity failure 근거는 아니지만 지속 모니터링 필요.

## 재현성 / authority 안전성

이번 변경은 다음을 **수정하지 않는다.**

- `companies/PWR/**`
- `companies/PWR/latest.json`
- canonical `raw-data/`
- `harness/baseline-lock.json`
- current registry/latest
- `reviews/latest`
- frozen deterministic outputs

따라서 현재 `companies/PWR/analyses/2026-09-06` authority와 하네스 재현성을 그대로 유지하면서 신규 원문 근거를 별도 checkpoint로 보존한다.

## 다음 승격 조건

Canonical deep run에서 아래를 완료한 뒤 PWR current authority 승격 여부를 판단한다.

1. 동기화 가격 및 9% reverse DCF
2. Bear/Base/Bull valuation
3. CEI, Dynamic Systems, 2026 acquisitions의 사후 ROIC/FCF cohort 분석
4. 2026-08 note issuance 이후 pro-forma net debt 및 use-of-proceeds bridge
5. backlog/RPO → revenue → cash conversion 및 working-capital 정상화
6. fixed-price loss project / claim aging
7. SBC·M&A 주식발행·환매·FCF/share bridge

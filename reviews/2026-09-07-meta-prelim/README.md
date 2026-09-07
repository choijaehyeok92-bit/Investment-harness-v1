# META 원자료 추출 및 초벌분석 — 2026-09-07

## 상태

이 실행은 사용자 제공 SEC PDF 8개를 비권한 staging 증거로 구조화하고, 이를 바탕으로 비가격 초벌분석을 기록한 증거 보강 실행이다.

- staged 원자료: `reviews/2026-09-07-meta-prelim/raw/META-2025-2026-supplied-filings.json`
- 원자료 구성: FY2025 10-K, Q2 2026 10-Q, Q2 2026 8-K/실적발표, 2026 Proxy 및 추가자료, Form 4 3개
- 잠정 연구 상태: `PARTIAL_ANALYSIS`
- 잠정 판정: `WATCH`
- 사업품질(가격 제외 앞 6개 항목): `56/75`
- 매수 승인: 없음
- 기대차/가치평가: 보류 — 동시점 시장가격과 reverse DCF 미실행

## 핵심 원자료 판독

1. Q2 2026 매출은 608.01억 달러로 전년 대비 28% 증가했고, 광고 노출은 14%, 평균 광고가격은 12% 증가했다.
2. FY2025 회사 정의 FCF는 435.85억 달러였으나 H1 2026은 131.70억 달러, Q2 2026은 7.84억 달러로 압축됐다. 원인은 AI/핵심 사업 인프라 투자 확대가 핵심이다.
3. 2026년 Capex 가이던스는 1,300~1,450억 달러다. 2026-06-30 미개시 리스는 2,789.9억 달러, 비취소 계약약정은 3,493.1억 달러이며 7월 추가 데이터센터 리스 약정은 680억 달러다.
4. H1 2026 SBC는 136.90억 달러이고 합산 주식 수는 2025년 말 대비 1,800만 주 증가했다. H1에는 자사주 매입이 없었다.
5. Reality Labs는 FY2025 영업손실 191.93억 달러, Q2 2026 영업손실 46.19억 달러를 기록했다. 현재 선택권 투자 재원은 Family of Apps의 현금창출력에 의존한다.
6. FY2025 감사의견과 내부회계관리제도 의견은 적정(unqualified)이다. 2026 Proxy 기준 Mark Zuckerberg는 총 의결권 60.8%를 통제한다.
7. 제공된 8월 Form 4의 CLO/CFO/CTO 매도는 모두 사전에 채택된 Rule 10b5-1 계획에 따른 거래이므로 초벌분석에서 재량적 약세 신호로 사용하지 않는다.

## 초벌 투자판독

사업 측면의 1차 증거는 강하다. 3.60B Family DAP를 유지하면서 광고 노출과 단가가 동시에 상승해 추천·타게팅·측정 기술의 고객가치 개선 가능성을 보여준다.

반면 투자경제성은 2026년에 다른 국면으로 들어갔다. 광고 플랫폼의 초과현금이 데이터센터, 클라우드, 서버, 네트워크의 장기 고정 약정으로 전환되는 속도가 빨라졌다. 따라서 다음 정밀분석의 결합 질문은 `AI 인프라 추가 1달러가 9% 요구수익률을 충분히 넘는 장기 세후 현금수익을 만드는가`이다.

핵심 Hard Veto는 `incremental_roic_collapse = INVESTIGATE`이며, `persistent_dilution`, `moat_shrinkage`, `price_requires_unrealistic_bull_case`, `fatal_concentration`, `permanent_loss_probability`도 열려 있다. 가격 게이트가 닫히지 않았으므로 총점/매수 승인을 만들지 않는다.

## 하네스 권한 처리

이번 실행은 **staging review**다. 새 원자료는 canonical renderer가 자동 수집하는 `companies/<ticker>/raw-data/*.json` 아래에 두지 않고 review 디렉터리에 격리했다. 따라서 현재 권한 파일인 `companies/META/latest.json`, `registry/companies.json`, `reviews/latest.json` 및 2026-09-06 재현 가능한 산출물은 변경하지 않는다.

`harness/baseline-lock.json`도 기존 2026-09-06 frozen baseline으로 복원했다. 이 방식으로 새 증거를 보존하면서도 `harness.build --check`, `harness.deep_report --check`, `harness.validate`가 현재 권한 스냅샷과 다른 META 산출물을 암묵적으로 재생성하는 문제를 피한다.

META를 공식 `PARTIAL_ANALYSIS` 또는 `FULL_ANALYSIS` 현재 상태로 승격할 때에는 별도 canonical run에서 staged raw를 정식 raw-data로 승격하고 registry/latest/observations/derived/reverse-DCF 산출물을 함께 생성한 뒤 전체 검증을 통과시킨다. 과거 판단을 덮어쓰지 않고 기록을 보존한다.

## 다음 조사 순서

1. AI/핵심 인프라의 유지 Capex와 성장 Capex 분리
2. 리스·계약약정의 연도별 현금 고정비와 가동률
3. 광고주 ROI·유지율 및 경쟁 플랫폼 대비 engagement share 독립 검증
4. SBC·총발행·환매·완전희석 주식 수의 4개 분기 브리지
5. Reality Labs 손실의 FoA 현금흐름 대비 축소 경로
6. 동시점 가격을 사용한 9% 허들 reverse DCF 및 Bear/Base/Bull

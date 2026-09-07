# MPWR 초벌분석 체크포인트 - 2026-09-08

> **비권위 연구 체크포인트**: 이 문서는 현재 `companies/MPWR/latest.json` 또는 registry authority를 대체하지 않는다. 사용자 제공 2025 10-K, 2026 Proxy, Q2 2026 10-Q 및 3페이지 8-K wrapper를 구조화한 후 만든 PARTIAL_ANALYSIS다.

## 판정

- **Decision:** WATCH
- **Priority:** P1
- **Business quality:** 61/75
- **Total score:** 보류
- **Buy authorization:** 없음
- **Valuation gate:** 미완료 - 동기화 현재가, reverse DCF, Bear/Base/Bull 필요

## 1. 구조적 논지

MPWR은 단순 아날로그 반도체 공급업체라기보다 시스템 수준의 전력관리 설계, 반도체 공정, 시스템 통합과 패키징을 결합하는 팹리스 전력반도체 기업으로 본다. 제조·조립·테스트를 제3자에게 맡기는 구조는 고정자본 부담을 상대적으로 낮추면서 내부 자원을 설계와 응용 엔지니어링에 집중하게 한다.

2026년 2분기에는 이 구조가 AI·서버 전력관리 수요와 맞물렸다. Q2 매출은 전년 동기 대비 47.6% 증가한 9.806억 달러였고, Enterprise Data 매출은 3.806억 달러로 164.3% 증가했다. 회사는 이를 AI와 서버용 power-management solutions 수요 증가로 설명했다. Communications도 78.3% 증가했다. 동시에 Q2 gross margin은 55.2%로 전년 55.1%와 사실상 동일했고 영업이익은 84.4% 증가했다. 가격·믹스·규모 확장의 조합이 현재까지는 마진 훼손 없이 작동하고 있다.

2025년에도 매출은 27.90억 달러로 26.4% 성장했고, 회사 Proxy 기준 14년 연속 매출 성장을 기록했다. Storage & Computing, Automotive, Communications, Consumer, Industrial 다수가 두 자릿수 이상 성장했다. 따라서 현재 성장은 한 개 최종시장만으로 설명되지는 않는다. 다만 2026년에는 Enterprise Data 비중이 Q2 38.8%까지 급상승했으므로 AI 수요의 지속성과 최종고객 집중은 새 핵심 변수다.

## 2. 현금창출과 재투자

FY2025 영업현금흐름은 8.382억 달러, 유형자산 취득은 1.720억 달러였다. 단순 `OCF - PPE purchases` 진단치는 약 6.662억 달러, 매출의 23.9%다. 이 수치는 완전한 owner FCF가 아니지만 MPWR의 높은 현금창출력을 보여준다.

그러나 H1 2026은 주의가 필요하다. 매출은 37.1%, 영업이익은 63.4%, 순이익은 66.8% 증가했지만 OCF는 4.782억 달러로 3.2% 감소했다. 매출채권이 8,800만 달러, 재고가 1.112억 달러의 현금을 흡수했다. 유형자산 취득도 1.533억 달러로 전년 동기 대비 73% 증가했다. H1 `OCF - PPE purchases`는 3.249억 달러로 여전히 양호하지만, 이익 성장과 현금 성장의 괴리는 추적해야 한다.

따라서 incremental ROIC의 판단은 현재 "높아 보인다"보다 "증설과 운전자본 증가 이후에도 9% hurdle을 충분히 상회하는지 검증 중"이 정확하다.

## 3. 재무 생존성

재무 생존성은 매우 강하다. 2026년 6월 말 현금 10.056억 달러와 단기투자 4.082억 달러를 합치면 14.138억 달러다. 총부채는 7.908억 달러, 운전자본은 19.795억 달러다. 제공된 대차대조표에는 별도 차입금·부채성 금융조달 라인이 표시되지 않는다. 이는 외부자금 의존 Hard Veto를 현재 **PASS**로 두는 핵심 근거다.

다만 "부채 라인이 없음"을 모든 금융의무가 0이라는 뜻으로 확장하지 않는다. 공급망 계약, 임대, 보상부채 등은 별도 검토 대상이다.

## 4. SBC와 주당가치

자본배분은 사업 품질보다 약한 부분이다. FY2025 GAAP stock-based compensation expense는 2.274억 달러였고, 기말 발행주식은 47.823M에서 48.709M으로 약 1.85% 증가했다. 같은 해 실제 자사주매입 현금은 770만 달러 수준이었다.

H1 2026에도 발행주식은 48.709M에서 49.142M으로 0.89% 증가했다. H1 SBC는 9,428만 달러였다. 2026년 7월에는 임직원에게 성과조건에 따라 최대 약 697,000주를 받을 수 있는 MPSU가 추가 승인됐다. 반면 이사회는 기존 5억 달러 자사주매입 한도에 5억 달러를 추가했지만, Q2 실제 매입은 400만 달러에 불과했다.

따라서 **buyback authorization과 실제 주당 희석 상쇄를 구분**해야 한다. `persistent_dilution`은 아직 FAIL은 아니지만 INVESTIGATE다.

## 5. 회계·내부통제

가장 중요한 Hard Veto는 회계 무결성이다. FY2025 10-K는 외국 자회사의 일회성 세제 인센티브와 관련된 deferred tax accounting 오류 때문에 FY2024 감사재무제표와 2025 분기재무제표를 재작성했다. 2024년 세금효과 조정은 1.946억 달러였다.

회사는 이를 의도하지 않은 비현금 오류라고 설명했고 Proxy는 임직원의 misconduct가 없었으며 매출·gross margin·operating expense와 주요 non-GAAP 운영지표에는 영향이 없었다고 설명한다. 그러나 회계오류가 **material**했고 관련 deferred-tax 내부통제의 material weakness가 2026년 6월 말에도 remediation되지 않았다는 점은 무시할 수 없다. Q2 10-Q에서 회사는 이 때문에 disclosure controls and procedures가 effective하지 않다고 결론 내렸다.

따라서 `management_or_accounting_integrity`는 **PASS가 아니라 INVESTIGATE**다. FY2026 말 실제 remediation과 감사인 검증이 필요하다.

## 6. 고객·채널 집중

H1 2026 매출의 88%는 distributor/value-added reseller를 통한 판매였고 direct-customer 기준 아시아 매출 비중은 93%였다. 2026년 6월 말 매출채권은 Distributor A 33%, Value-added Reseller A 20%, Distributor B 15%에 집중됐다.

이 집중은 즉시 치명적이라고 보기는 어렵다. 회사는 유통계약 종료 시 대체 채널을 비교적 빠르게 확보할 수 있다고 설명하고, 제품의 실제 최종수요는 여러 시장에 걸쳐 있다. 그러나 우리는 distributor 숫자와 **실제 AI 서버/가속기 최종고객 집중도를 분리해서** 봐야 한다. 후자는 제공 공시만으로 충분히 검증되지 않았다.

## 7. 경영진과 지배구조

Michael Hsing은 1997년 창업 이후 Chairman, President, CEO를 겸임한다. 장기 founder-led 구조는 기술·문화 연속성 측면의 장점이다. 동시에 독립적 견제가 필요한 구조다. 7인 이사회 중 6명이 NASDAQ 기준 independent director로 분류됐고 Herbert Chang이 Lead Independent Director다.

Hsing의 2026년 4월 기준 beneficial ownership은 1,034,099주, 약 2.1%다. 창업자이지만 지분지배 구조는 아니다. 2025년 CEO 총보수는 약 1,993만 달러로 높으며 상당 부분이 주식보상·성과급이다. 성과연동성은 있지만 SBC와 주당가치 관점에서 지속 모니터링이 필요하다.

## 8. 가장 강한 Bull / Bear

### Bull

AI 서버와 데이터센터의 전력 밀도가 구조적으로 상승하면서 power-management content per system이 장기간 증가한다. MPWR이 시스템 통합·공정·패키징 능력으로 design wins를 늘리고 55%대 gross margin을 유지한다면, 높은 영업레버리지와 낮은 재무레버리지 때문에 현금복리 성장이 비선형적으로 커질 수 있다.

### Bear

2026년 Enterprise Data 급증이 소수 AI 고객과 유통채널에 집중된 일시적 capex 사이클일 수 있다. 동시에 재고·채권·증설 capex가 늘고, SBC 희석이 누적되며, 내부통제 문제가 재발할 경우 회계상 고성장이 owner cash per share로 이어지지 않는다. 더구나 시장 가격이 이미 장기 AI hypergrowth를 요구한다면 사업 실패가 없어도 투자수익률은 낮아질 수 있다.

## 9. 다음 검증 순서

1. 동기화 현재가 + 완전희석 주식수로 9% reverse DCF
2. Bear/Base/Bull 10년 owner-cash 모델
3. AI 서버/가속기 최종고객별 design-win 지속률, content per system, ASP
4. 최근 8개 분기 distributor inventory, sell-through, A/R, inventory와 OCF 브리지
5. wafer/manufacturing capacity 증설의 세후 cash ROIC
6. FY2026 deferred-tax control remediation 및 감사인 평가
7. SBC·RSU·MPSU·주식발행·실제 buyback을 연결한 diluted owner-cash-per-share 브리지

## 결론

**WATCH / P1. 사업 품질 61/75.** 사업 자체는 이전 PRELIMINARY_REVIEW보다 훨씬 강한 1차 증거를 확보했다. 특히 AI/Enterprise Data 가속, 55%대 gross margin, 강한 영업레버리지, 순유동성은 높은 질을 지지한다.

하지만 지금은 매수 승인 단계가 아니다. **미해결 material weakness, 이익 대비 둔화된 OCF, SBC/희석, 채널·최종고객 집중, 그리고 무엇보다 valuation 미검증**이 남아 있다. 다음 단계는 가격을 붙여 기대치를 역산하는 것이다.

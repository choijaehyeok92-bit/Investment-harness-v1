# ServiceNow (NOW) — 2026-09-10 Deep Research Checkpoint

## 결론

ServiceNow는 여전히 엔터프라이즈 워크플로의 강한 **system of action**이다. Q2 2026 구독매출은 38.77억달러로 24.5% 성장했고, cRPO는 132억달러로 21% 증가했으며, AI ACV는 10억달러를 넘어섰다. 다만 이 사업 강도는 이미 2026-09-06 canonical에 상당 부분 반영돼 있다. 이번 체크포인트의 핵심 변화는 가격이 141.26달러에서 131.24달러로 내려 expectation gap이 개선됐다는 점과, GPT-6 Astra 같은 강한 범용 에이전트가 SaaS의 UI·검색·오케스트레이션 가치를 잠식할 수 있다는 경쟁 리스크가 더 선명해졌다는 점이다.

최종 판정은 **WATCH / P1 / business quality 56/75 / total 73/100 / Starter-Watch / buy_authorized=false**다.

## 사업의 질

ServiceNow의 핵심 경제가치는 기록 시스템 자체보다 복잡한 기업 승인·권한·감사·업무흐름을 실제로 실행하는 계층에 있다. AI가 자연어 인터페이스를 대체하더라도, 실제 엔터프라이즈 작업은 권한과 데이터 문맥, 승인체계, 규제 추적성을 필요로 한다. ServiceNow의 AI Control Tower, Otto, Action Fabric, Autonomous Security는 이 지점을 방어하려는 전략이다.

Q2에는 100만달러 이상 net-new ACV 거래가 123건으로 약 40% 늘었고, 500만달러 이상 ACV 고객이 658개로 약 23% 증가했다. 이는 대형 고객 확장 증거다. 반면 갱신율 98%는 NRR이 아니며, AI ACV는 매출이나 현금이 아니다. AI가 실제로 고객당 지출과 owner cash를 높이는지 추가 검증이 필요하다.

## AI 해자

AI는 ServiceNow에 기회이자 위협이다. 강한 범용 모델은 사용자가 ServiceNow 화면을 직접 탐색할 필요를 줄일 수 있다. 2026년 9월 GPT-6 Astra 출시 이후 소프트웨어 주가가 하락한 것은 이 우려를 반영했다. 그러나 주가 반응 자체는 moat shrinkage의 증거가 아니다.

방어 논리는 ServiceNow가 외부 모델을 막는 것이 아니라 오히려 외부 에이전트를 자사 워크플로와 권한체계 안에서 통제하는 방향으로 움직인다는 점이다. 9월 10일 재출시된 AI Gateway는 MCP 연결에 runtime policy를 적용하는 제어층이다. 성공한다면 frontier model이 강해질수록 ServiceNow가 governance/execution control plane으로 남을 가능성이 있다.

따라서 `moat_shrinkage`는 PASS가 아니라 **INVESTIGATE**다. 핵심은 모델 성능이 아니라 실제 고객 코호트에서 ServiceNow의 가격, NRR, workflow attach와 실행 점유가 유지되는지다.

## 성장의 질

Q2 구독매출 +24.5%, CC +23%는 강하지만 회사는 미국 연방정부의 on-premise 매출 일부가 Q3에서 Q2로 앞당겨졌다고 명시했다. 또한 2026년 대형 인수 효과가 있다. 따라서 Q2 headline을 유기적 steady-state growth로 외삽하지 않는다.

Q3 이후 cRPO와 구독성장이 선반영 효과를 흡수한 뒤에도 20% 안팎을 유지하고 현금수금이 따라오는지 확인해야 한다. 그래서 `low_quality_growth`는 여전히 **INVESTIGATE**다.

## SBC와 주당 현금

TTM 산식 `FY2025 + H1 2026 - H1 2025`를 적용하면 매출 147.32억달러, OCF 53.08억달러, PPE 취득 7.28억달러다. 기계적 OCF-PPE는 45.80억달러다.

하지만 TTM SBC는 약 21.85억달러다. 기타 무형자산까지 반영한 보수적 owner-cash 진단은 약 23.72억달러다. 이를 definitive normalized FCF로 부르지 않는다. 인수통합비용, 이자, hyperscaler 비용, 운전자본과 미래 SBC 정상화가 남아 있기 때문이다.

H1 2026 기간말 기본주식수는 약 10.34억주로 감소했다. 그러나 이는 22.25억달러의 환매 현금이 투입된 결과다. SBC가 매출의 약 16%인 상황에서 환매를 순수한 자본환원으로 전부 인정하면 경제적 희석을 과소평가한다. `persistent_dilution`은 **INVESTIGATE**다.

## 인수와 자본배분

Armis는 약 76억달러, Veza는 약 12억달러에 인수됐고 H1 business-combination cash outflow는 87.76억달러였다. 보안·아이덴티티를 워크플로와 결합하는 전략 논리는 합리적이지만, 아직 분리된 매출·현금·세후 incremental ROIC를 확인할 수 없다.

ServiceNow는 이를 위해 장기채와 commercial paper를 사용했다. 6월말 commercial paper는 21억달러, 평균 잔존기간은 81일이었다. 운영 생존을 위한 외부자금 의존은 아니므로 `external_capital_dependence`는 PASS지만, 인수수익률과 차환은 자본배분 리스크다.

## 밸류에이션

9월 10일 종가 131.24달러, 10.33862억주 기준 분석 시가총액은 약 1,356.8억달러다. TTM GAAP 순이익 약 16.70억달러 대비 약 81배, OCF-PPE 대비 약 29.6배, 보수적 owner-cash 진단 대비 약 57.2배다.

기존 장기 시나리오는 비교가능성을 위해 유지했다.

- Bear: **$58.49**
- Base: **$188.18**
- Bull: **$409.78**
- Permanent-loss diagnostic: **$18.75**

현재가는 Base 대비 약 30% 할인이고, Base까지 약 43% upside가 있다. 9% hurdle, 15% 시작 owner margin, 24% 성숙 margin, 23배 terminal multiple을 고정하면 현재가를 맞추는 10년 매출 CAGR은 약 **11.50%**다. 이전 141.26달러 기준 12.41%보다 낮아졌다.

이 조건은 demanding하지만 Q2 cRPO와 구독성장보다 낮으므로 `price_requires_unrealistic_bull_case`는 PASS다. 그러나 Base PV의 약 78%가 terminal value이고, 24% owner margin은 아직 검증되지 않았다. PASS는 저평가 확정이나 매수 승인이 아니다.

## Hard Veto

PASS: management/accounting integrity, external capital dependence, price requires unrealistic bull case, fatal concentration, permanent loss probability.

INVESTIGATE: **persistent dilution, low-quality growth, incremental ROIC collapse, moat shrinkage**.

한 문장으로 요약하면 다음과 같다.

> ServiceNow는 가격이 이전보다 매력적으로 내려왔고 AI monetization 증거도 강하지만, 현재 신규매수의 핵심 병목은 밸류에이션보다 SBC가 주당 owner cash로 실제 정상화되는지, Armis/Veza가 9% 이상의 증분수익률을 만드는지, 그리고 강한 범용 AI 에이전트 시대에도 ServiceNow가 workflow control plane을 유지하는지다.

가격 하락만으로 STARTER를 열지 않는다. 최소 두 차례의 clean cRPO/owner-cash 증거와 SBC·인수 ROIC·AI 경쟁 증거의 복수 개선이 필요하다.

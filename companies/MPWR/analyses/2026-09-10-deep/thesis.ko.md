# Monolithic Power Systems (MPWR) 심층분석 체크포인트 — 2026-09-10

## 결론

**WATCH / P1 / buy_authorized=false / Starter / Watch 69/100**.

MPWR은 AI 데이터센터의 전력밀도 상승, 전력변환 효율 요구, 자동차 전장화, 통신·산업 전력관리의 복잡성 증가를 동시에 수혜받는 고품질 아날로그/전력반도체 기업이다. Q2 2026 매출 $980.6M(+47.6% YoY), Enterprise Data $380.6M(+164.3%), GAAP 영업이익률 31.0%는 제품 경쟁력과 AI 노출이 실제 실적으로 이어지고 있음을 보여준다.

그러나 현재 주가는 이 사업의 질보다 훨씬 공격적인 장기 실행을 요구한다. 2026-09-10 종가 $1,186.08에서 새 Base 가치 약 $680 대비 약 74% 프리미엄이며, 9% 요구수익률로 Base의 현금경제를 유지할 경우 2~10년 매출이 연평균 약 19.35% 성장해야 한다. 좋은 기업과 좋은 가격을 분리해야 한다.

## 구조적 성장과 고객가치

MPS는 단일 regulator 공급자를 넘어 시스템 수준의 power solution provider로 이동하고 있다. AI accelerator의 전력밀도 증가와 rack-level 전력변환 효율 요구는 core power, memory power, high-voltage conversion, intelligent power stages의 콘텐츠 기회를 넓힌다. Q2 회사는 800V 데이터센터 구조를 겨냥한 High Voltage AC-to-DC 제품을 sampling 중이라고 밝혔다. 자동차에서도 연초 이후 1,500개가 넘는 신규 socket에 제품을 출하했다고 설명했다.

Enterprise Data의 Q2 매출은 $380.6M으로 전년 대비 164.3% 증가해 전체 매출의 38.8%가 됐다. Communications도 78.3% 성장했고 Automotive는 8.2% 성장했다. 즉 AI가 성장을 주도하지만 회사 전체가 한 end-market만으로 구성된 것은 아니다.

다만 800V는 아직 양산 실적이 아니라 sampling 단계다. Infineon 등 경쟁사는 Si, SiC, GaN을 포함한 grid-to-core 포트폴리오를 확대하고 NVIDIA의 800V 생태계에도 적극 참여하고 있다. 따라서 MPWR을 800V 독점 승자로 평가하지 않는다.

## 해자

MPS의 해자는 단일 특허보다 proprietary process technology, package, control architecture, system engineering, 빠른 design cycle의 결합에 있다. 고객 입장에서는 전력 효율, board area, thermal performance와 qualification risk가 중요하다. 이 조합이 높은 영업마진과 다수 시장의 반복적인 design win으로 이어져 왔다.

2026년 9월 GlobalFoundries와 장기 제조계약을 맺고 싱가포르 300mm fab에서 MPS proprietary process를 구현하기로 한 점은 공급망 다변화와 생산능력 확장의 긍정적 증거다. 초기 volume production은 2027년 초를 목표로 한다. 다만 새로운 공급능력은 해자 강화 가능성이자 신규 투자자본이다. 실제 가동률과 증분 현금수익을 확인하기 전까지 이를 가치에 선반영하지 않는다.

## 회계·내부통제

이번 분석에서 가장 중요한 비사업 리스크다. MPWR은 FY2024의 특정 해외 세제 인센티브 관련 deferred-income-tax 회계처리를 재작성했고, 이 과정에서 약 $194.6M 규모의 세금효과가 수정됐다. 관련 material weakness는 2025년 말에도 존재했고 2026년 6월 30일 기준 아직 remediation이 완료되지 않았다.

EY는 재무제표에 대해 무수정 의견을 냈고, 현재 증거에서 의도적 회계부정이나 경영진 비위가 확인된 것은 아니다. 그러나 Hard Veto는 misconduct만 보는 것이 아니라 accounting reliability의 중대한 훼손도 본다. 따라서 `management_or_accounting_integrity`는 **INVESTIGATE**다. remediation 완료와 반복 오류 부재가 확인될 때까지 PASS로 낮추지 않는다.

## 현금창출과 SBC

하네스 규칙 `FY2025 + H1 2026 - H1 2025`로 계산한 TTM은 다음과 같다.

- 매출: 약 **$3.273B**
- 영업이익: 약 **$0.940B**
- 순이익: 약 **$0.802B**
- OCF: 약 **$0.822B**
- 유형자산 취득: 약 **$0.237B**
- SBC: 약 **$0.209B**
- 기계적 OCF-PPE: 약 **$0.586B**
- 기계적 OCF-PPE-SBC: 약 **$0.377B**

마지막 두 수치를 normalized owner FCF로 부르지 않는다. H1 2026 OCF는 순이익 급증에도 전년 동기보다 감소했고 회사도 더 큰 working-capital 필요를 주요 원인으로 설명했다. 재고는 Q2 말 $675.8M이었고 current-quarter 기준 140일 수준이다. 신규 fab/공급능력, 무형투자, 운전자본 정상화까지 반영해야 실제 owner cash를 판단할 수 있다.

SBC 역시 무시할 수 없다. 발행주식은 2024년 말 47.823M에서 2025년 말 48.709M, 2026년 6월 49.142M으로 증가했다. 이 정도 증가를 현재 바로 `persistent_dilution` Hard Veto 실패로 판단하지는 않지만, 경영진 자본배분 점수에는 감점했다. Q2 이사회가 총 $1B의 자사주 매입 권한을 마련했지만 H1 실제 repurchase는 약 $4M에 그쳤다.

## 재무생존력

2026년 6월 현금·현금성자산과 단기투자자산은 합계 약 $1.414B이다. 검토한 Q2 10-Q의 재무상태표에서 별도 debt line은 식별되지 않았고 OCF도 강하다. 따라서 외부자본 의존과 파산 위험은 낮다. MPWR의 핵심 위험은 생존이 아니라 **높은 가격에서 예상한 성장·마진·증분수익률을 실제로 달성하지 못할 때 발생하는 영구적 자본손실**이다.

## 고객·채널 집중

Q2 매출의 88%가 distribution arrangement를 통해 발생했고, 단일 distributor A/B/D가 각각 Q2 매출의 28%/15%/10%를 차지했다. 6월 말 매출채권도 distributor A 33%, VAR A 20%, distributor B 15%로 집중되어 있다.

회사는 주요 distributor가 종료돼도 상대적으로 짧은 기간 안에 대체 가능하다고 설명한다. 또한 실제 end market은 Enterprise Data, Storage & Computing, Automotive, Communications, Consumer, Industrial로 분산돼 있다. 따라서 현재 `fatal_concentration`은 PASS다. 다만 distributor concentration과 underlying AI end-customer concentration은 다른 문제이며, 후자는 충분히 공시되지 않았으므로 지속 추적한다.

## 밸류에이션

2026-09-10 종가 $1,186.08과 49.3M valuation shares를 사용하면 단순 시가총액은 약 $58.47B이다. 이는 TTM 순이익의 약 72.9배, 기계적 OCF-PPE의 약 99.9배, OCF-PPE-SBC 진단의 약 155.2배다. 이 배수들은 normalized FCF 배수가 아니라 현재 가격이 요구하는 expectation의 크기를 보기 위한 진단이다.

새로 수립한 9% 요구수익률 시나리오는 다음과 같다.

- Bear: **$218.71**
- Base: **$680.08**
- Bull: **$1,569.06**

Bear는 AI design-share 정상화, 낮은 capacity utilization, 12% mature owner margin을 가정한다. Base는 AI·자동차·통신에서 높은 성장을 이어가되 장기 성장률과 cash margin이 점진적으로 정상화된다고 본다. Bull은 MPWR이 800V와 grid-to-core에서 핵심 플랫폼으로 부상하고 장기 24% owner margin까지 달성하는 시나리오다.

현재가는 Base보다 약 74% 높고 Bull 대비 남은 upside도 약 32%다. Bear/Bull 두 끝점만 놓은 단순 가격 위치는 Bull 쪽 약 71.6% 지점이다. 이는 확률 추정이 아니라 가격의 위치 진단이다.

Reverse DCF는 Base의 1년차 매출 $4.4B, owner margin 14%→20%, terminal 25배, 9% 요구수익률을 유지한다. 현재 가격을 맞추려면 2~10년 매출이 매년 약 **19.35%** 성장해 10년 차 매출 약 **$21.6B**에 도달해야 한다. Q2 성장률을 보면 수학적으로 불가능하지는 않지만, 아날로그/전력반도체 기업이 이런 duration을 달성하려면 AI design share, 800V 전환, 자동차·산업 성장, 신규 생산능력 ROIC가 동시에 장기간 성공해야 한다.

## Hard Veto

PASS: external capital dependence, persistent dilution, low-quality growth, moat shrinkage, fatal concentration.

INVESTIGATE: management/accounting integrity, incremental ROIC collapse, price requires unrealistic bull case, permanent-loss probability.

`persistent_dilution`은 현재 실패가 아니라 monitor다. 반대로 회계 material weakness는 실제 확인된 미해결 통제 문제이므로 별도의 INVESTIGATE가 맞다.

## 증액 조건

가격 하락 하나만으로 증액하지 않는다. 우선 material weakness가 완전히 remediation되고 반복 오류가 없어야 한다. 800V 샘플이 복수 고객의 양산 design win으로 전환되고, GlobalFoundries 등 신규 생산능력의 세후 incremental return이 9%를 넘으며, OCF/share가 PPE와 SBC 이후에도 최소 두 보고기간 개선되어야 한다. 실제 자사주 매입도 주식보상에 따른 share-count 증가를 경제적으로 상쇄하는지 확인한다.

이러한 사업·현금 증거가 개선된 상태에서 가격이 보수적/Base 가치 대비 충분한 할인으로 내려오거나 normalized owner cash가 크게 상승해야 STARTER 이상의 실제 매수 승격을 검토한다. 현재 분류명 `Starter / Watch`는 점수 구간명일 뿐 매수 승인이나 STARTER 포지션을 뜻하지 않는다.

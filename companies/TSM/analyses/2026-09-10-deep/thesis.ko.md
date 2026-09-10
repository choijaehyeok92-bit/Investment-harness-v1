# TSM 심층분석 체크포인트 — 2026-09-10

## 결론

**WATCH / P1 / buy_authorized=false / Emerging Outlier 75/100**.

TSMC의 기업 품질은 이번 재검토에서 더 강해졌다. Q2 2026 매출 NT$1.270조, 순이익 NT$706.6B, gross margin 67.7%, operating margin 60.3%였고 HPC가 매출의 66%, 2nm가 첫 매출 분기부터 wafer revenue의 3%를 차지했다. 공식 8월 매출은 NT$514.8B로 전년동월 대비 53.3% 증가했고 1~8월 누적은 39.3% 증가했다. TrendForce는 Q2 foundry 매출 점유율을 72.5%로 추정했다. 구조적 리더십과 해자 증거는 전보다 강하다.

그러나 좋은 기업과 좋은 주식 가격은 다르다. 2026-09-10 ADR 참고가 US$427.18은 기존 Base 가치 US$309.90보다 약 38% 높다. 9% 요구수익률, Base 첫해 매출 US$185B, owner-margin 25%에서 27%, terminal 22x를 유지하면 2~10년 동안 약 15.01%의 연매출 성장이 필요하다. 최근 성장률보다 낮지만, 이미 세계 최대급 제조기업이 9년 동안 두 자릿수 중반 성장과 높은 owner margin을 유지해야 하는 duration이다.

## 구조적 성장과 고객가치

Q2 2026의 핵심은 단순한 매출 증가가 아니다. 7nm 이하 advanced technology가 wafer revenue의 77%였고 2nm가 첫 매출을 시작했다. HPC가 66%까지 확대되면서 AI GPU/XPU, CPU, custom silicon과 advanced packaging 수요가 TSMC의 선단 노드 경제성을 강화하고 있다. Q3 매출 가이던스도 US$44.6~45.8B로 높게 제시됐다.

8월 월매출 NT$514.8B는 네 달 연속 기록 경신 흐름을 이어갔다. 다만 월매출은 고객의 prebuild, 스마트폰 계절성, 가격 인상과 믹스를 포함하므로 AI 최종수요의 순수한 독립 지표로 보지 않는다. 성장 자체보다 장기적으로 N2/A14 수율, 고객 design share, CoWoS/3DFabric attach, pricing power가 더 중요하다.

## 해자

TrendForce는 Q2 2026 TSMC foundry share를 약 72.5%로 추정했다. Samsung은 약 5.9%로 큰 격차가 있다. TSMC의 해자는 단일 공정 특허가 아니라 선단 공정 수율, 대규모 고객 공동개발, EDA/IP 생태계, 생산규모, advanced packaging, 공급망 및 반복적인 node execution의 결합이다.

이번에는 moat_trajectory를 13/15에서 14/15로 올렸다. 그러나 독점이라고 보지는 않는다. Samsung과 Intel Foundry는 계속 투자하고 있고, 고객은 특정 세대에서 dual-source 또는 자체 packaging/accelerator 전략을 확대할 수 있다. 해외공장 확대가 전략적 복원력을 높이는 대신 Taiwan 대비 원가우위를 일부 희석할 가능성도 있다.

## 현금과 자본집약도

하네스 규칙 `FY2025 + H1 2026 - H1 2025`로 계산한 TTM은 대략 다음과 같다.

- 매출: **NT$4.440조**
- 지배주주 순이익: **NT$2.237조**
- 영업현금흐름: **NT$2.635조**
- 유형자산 취득: **NT$1.491조**
- 기계적 OCF-PPE: **NT$1.144조**

이 NT$1.144조를 normalized owner FCF라고 부르지 않는다. TSMC는 N2/A14, advanced packaging, Arizona/Japan 및 Taiwan 증설이 겹치는 이례적으로 큰 투자기에 있다. 감가상각과 실제 유지·성장 CAPEX의 차이, 보조금, 운전자본, fab별 ramp economics를 정상화하지 않은 OCF-PPE는 진단치일 뿐이다.

2026 CAPEX 가이던스는 US$60~64B로 상향됐다. Arizona 투자계획도 총 US$265B 수준으로 커졌다. 이것이 이번 분석에서 `incremental_roic_collapse`를 새로 INVESTIGATE로 연 이유다. 실제 붕괴가 확인된 것이 아니라, 이전 Taiwan 중심 자본의 높은 ROIC를 향후 해외·첨단노드 자본에 자동 적용할 수 없기 때문이다.

## 해외생산과 지정학

Arizona는 공급망 복원력을 높인다. 첫 fab은 양산 중이고 후속 fab과 packaging/R&D 확장이 진행된다. 그러나 TSMC는 동시에 Taiwan에서 다수의 선단 및 advanced-packaging fab을 건설 중이다. 핵심 R&D와 최대 규모의 선단 생태계는 여전히 Taiwan에 집중돼 있다.

따라서 해외증설을 Taiwan tail risk의 완전한 hedge로 보지 않는다. 대만 해협 봉쇄·충돌·자산접근 제한은 ordinary Bear DCF로 표현하기 어려운 비연속적 위험이다. 이를 임의 확률로 할인해 false precision을 만들기보다 `fatal_concentration`과 `permanent_loss_probability`를 INVESTIGATE로 유지한다.

## 고객집중

2025 Form 20-F 기준 top 10 고객은 매출의 78%, 최대 고객 19%, 2위 고객 17%였다. 단일 고객이 20%를 넘지는 않았지만 top 2 합계 36%는 의미 있는 경제적 집중이다. AI/HPC에서는 고객별 제품주기와 자본지출이 크기 때문에 한두 고객의 roadmap 변화가 단기 매출과 utilization에 영향을 줄 수 있다.

TSMC는 2025년에 534개 고객과 12,682개 제품을 생산했다고 공시했으므로 고객 기반 자체는 넓다. 하지만 매출 기여도는 상위 고객에 집중돼 있다. `fatal_concentration`은 customer concentration과 Taiwan geographic concentration을 합쳐 조사 상태로 둔다.

## 회계와 재무생존력

2025 Form 20-F에서 management는 ICFR이 유효하다고 평가했고 Deloitte도 내부통제 및 연결재무제표에 무수정 의견을 냈다. 현재 검토 증거에서 accounting-integrity failure는 발견하지 못했다. `management_or_accounting_integrity`는 PASS다.

재무생존력도 강하다. 영업현금흐름이 매우 크고 대규모 CAPEX를 내부 현금창출로 상당 부분 감당할 수 있다. 다만 Taiwan의 물리적 생산중단은 conventional balance-sheet solvency와 다른 차원의 위험이다.

## 밸류에이션

2026-09-10 ADR secondary completed-session reference는 **US$427.18**이다. Filing 기반 ordinary-share 수를 5로 나눈 5,186.505M ADS를 유지하면 단순 시가총액은 약 **US$2.216T**다.

기존 시나리오는 비교가능성을 위해 유지한다.

- Bear: **US$96.28**
- Base: **US$309.90**
- Bull: **US$702.08**

현재가는 Base보다 약 37.9% 높다. Base 관점에서는 현재가격 대비 약 -27.5%의 가치차가 있다. Bull upside는 약 +64.4%, ordinary Bear downside는 약 -77.5%다. Bear/Bull 두 상태만 존재한다고 가정한 가격 위치는 Bull 쪽 약 54.6%지만 이는 확률 추정이 아니다.

Reverse DCF에서 Base 첫해 매출 US$185B, owner-margin path 25%→27%, terminal 22x, 9% hurdle을 고정하면 2~10년 매출이 **연 15.01%** 성장해야 한다. 10년차 매출은 약 US$651B, owner cash는 약 US$176B가 된다. 관리진의 FY2026 +40% 이상 성장 전망 및 2029년까지의 고성장 프레임을 보면 수학적으로 불가능한 Bull-only 조건은 아니므로 `price_requires_unrealistic_bull_case`는 PASS다. 그러나 기대차 점수는 4/15로 낮다.

## Hard Veto

PASS:
- management_or_accounting_integrity
- external_capital_dependence
- persistent_dilution
- low_quality_growth
- moat_shrinkage
- price_requires_unrealistic_bull_case

INVESTIGATE:
- **incremental_roic_collapse** — US$60~64B 연 CAPEX와 US$265B Arizona 계획의 post-ramp 경제성 미검증
- **fatal_concentration** — top 10 고객 78%, top 2 36%, Taiwan 생산·R&D 집중
- **permanent_loss_probability** — 지정학 tail risk와 valuation duration의 결합

따라서 사업품질 68/75, 총점 75/100이어도 Hard Veto가 점수를 우선하므로 **WATCH / buy_authorized=false / position_band=NONE**이다.

## 증액 조건

가격 하락만으로 증액하지 않는다. N2/3nm와 advanced packaging의 현금전환, 해외 fab의 수율·가동률·세후 incremental ROIC >9%, OCF-PPE per ADS의 정상화 이후 증가, 상위 고객 집중 완화, 해외 capacity의 실질적 대체가능성 개선이 최소 두 가지 이상 확인되어야 한다. 그 상태에서 Base 대비 충분한 할인까지 확보되어야 STARTER 이상을 검토한다.

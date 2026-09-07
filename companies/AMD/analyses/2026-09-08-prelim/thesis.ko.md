# AMD — 2026-09-08 원자료 기반 초벌분석

판정: **WATCH**  
연구 상태: **PARTIAL_ANALYSIS checkpoint**  
매수 승인: **없음**  
조사 우선순위: **P1**

> 이 문서는 사용자 제공 SEC XBRL 원자료와 사용자가 지정한 AMD IR 공시 URL을 기반으로 한 초벌분석이다. 현재 하네스의 `companies/AMD/latest.json` 또는 `registry/companies.json`을 대체하지 않는 연구 체크포인트이며, 가격 역산·완전 희석 주식수·10년 현금모형이 끝나기 전에는 매수 판단으로 승격하지 않는다.

## 0. 분석 전략

핵심 질문은 단순히 "AMD가 AI 성장주인가"가 아니다.

1. EPYC와 Instinct의 성장이 실제 현금과 마진으로 연결되는가.
2. ROCm·네트워킹·Helios·ZT Design을 포함한 풀스택 확대가 해자를 강화하는가.
3. 대규모 AI 고객 확보의 대가로 제공한 warrant와 공급·클라우드·리스 약정이 주당 경제가치를 훼손하지 않는가.
4. 현재 가격이 요구하는 성장률과 기간을 충족하고도 9% 요구수익률을 남길 수 있는가.

이번 회차는 1~3번의 기초 증거를 확보했고, 4번은 의도적으로 보류한다.

## 1. 기본정보와 원자료

원자료는 2025 10-K, Q2 2026 10-Q, 2026 Proxy, 2026-08-19 8-K, Jean Hu CFO의 2026-08-27 Form 4, 2026-03-27 DEFA14A다. 숫자와 공시 문구는 `reviews/2026-09-08-amd-prelim/raw-data.json`에 구조화했다.

가장 중요한 원자료 변화는 다음과 같다.

- FY2025 매출 **$34.639B**, 영업이익 **$3.694B**, 순이익 **$4.335B**.
- FY2025 Data Center 매출 **$16.635B**, 전년 대비 32% 증가.
- Q2 2026 매출 **$11.536B**, 전년 대비 약 50% 증가.
- Q2 2026 Data Center 매출 **$6.718B**, 전년 대비 107% 증가.
- H1 2026 continuing OCF **$5.321B**, PPE 구매 **$1.197B**, SBC **$0.990B**.
- 2026-06-27 현금+단기투자 **$13.111B**, 총 원금부채 약 **$3.3B**.

## 2. 기업·산업 분석

### 구조적 성장

AMD는 이제 CPU 단일 축의 점유율 회복 스토리만으로 보기 어렵다. 2025년 이후 회사가 설명하는 제품 스택은 EPYC CPU, Instinct GPU, DPU/AI NIC, FPGA, 네트워킹, ROCm 소프트웨어, rack-scale 설계까지 확장됐다.

Q2 2026 Data Center 매출은 $6.718B로 전체 매출의 약 **58.2%**를 차지했고, 해당 부문 영업이익률은 약 **31.3%**였다. 이는 AI/서버 수요가 단순 매출 성장뿐 아니라 부문 수익성에도 기여하고 있음을 보여준다.

또한 OpenAI와 Meta는 각각 최대 **6GW**의 AMD 데이터센터 GPU 배치를 의도하는 다년 계약을 맺었다. 첫 1GW는 MI450 계열이 대상이다. 이는 향후 수요 가시성의 강한 긍정 신호다.

### 그러나 고객 확보 비용이 매우 크다

두 고객은 각각 최대 **1.6억 주**, 합계 **3.2억 주**의 AMD 주식을 주당 $0.01에 살 수 있는 조건부 warrant를 받았다. 2026-06-27 발행주식 16.32억 주와 단순 비교하면 최대 주식수는 약 **19.6%**에 해당한다.

이 19.6%를 예상 희석률로 해석하면 안 된다. 실제 vesting에는 GPU 구매, 주가 또는 성과, 기술·상업 조건이 걸려 있고 2026-06-27 현재 어느 tranche도 vest/exercise되지 않았다. 다만 **고객 확보의 경제적 대가가 상당할 수 있다는 사실 자체**는 투자자가 반드시 모델링해야 한다.

### 해자

EPYC의 서버 CPU 경쟁력과 MI350의 초기 상업 성과는 긍정적이다. 더 중요한 변화는 AMD가 CPU/GPU 공급업체에서 시스템 설계와 소프트웨어까지 범위를 넓히고 있다는 점이다. ZT Systems 인수 후 제조부문은 Sanmina에 매각하고 설계부문을 유지한 것도 이 방향과 맞는다.

반대로 아직 제출된 원자료만으로 ROCm이 CUDA 수준의 개발자 전환비용을 만들었다고 볼 수 없다. 제품 세대마다 다시 경쟁해야 하고 파운드리는 외부에 의존한다. 따라서 **해자는 강화 중이라는 가설은 성립하지만, 완성된 해자라고 판정할 증거는 부족하다.**

## 3. 재무 분석

### FY2025

- 매출 성장률: 약 **34.3%**
- gross margin: 약 **49.5%**
- operating margin: 약 **10.7%**
- R&D/매출: 약 **23.4%**
- continuing OCF - capex: **$5.519B**
- continuing OCF - capex - SBC 보수적 프록시: **$3.881B**
- diluted share 기준 위 프록시: 약 **$2.37/share**

2025 전체 OCF $7.709B 중 $1.216B는 매각된 ZT Manufacturing의 discontinued operations에서 발생했다. 따라서 지속사업 경제성을 볼 때 이를 제거한다.

### H1 2026

- 매출: **$21.789B**, 전년 대비 약 **44.1%** 증가
- gross margin: 약 **53.3%**
- operating margin: 약 **15.9%**
- continuing OCF - capex: **$4.124B**
- continuing OCF - capex - SBC 프록시: **$3.134B**
- diluted share 기준 프록시: 약 **$1.89/share**, **연율화하지 않음**

현금창출의 방향은 분명 개선되고 있다. 특히 Q2 영업이익 $1.990B와 Data Center 영업이익 $2.103B은 AI 수요가 경제적 이익으로 연결되고 있음을 보여준다.

### 자본부담과 운전자본

반대편에는 훨씬 빠르게 커지는 약정이 있다.

- FY2025 unconditional commitments: 약 **$12.2B**
- 2026-06-27 unconditional commitments: 약 **$30.3B**
- 이 중 2026 잔여기간: **$17.4B**
- 이미 개시된 lease commitments: 약 **$1.2B**
- 미개시 lease future payments: **$4.5B**
- data-center lease guarantee 최대노출: **$4.1B**
- 6월말 이후 조건부 investment commitments: 최대 **$5.0B**
- 6월말 이후 장기 data-center lease future payments: **$9.5B**

이 숫자들은 모두 동일한 성격의 부채가 아니므로 합산해 "총부채"로 부르면 안 된다. 하지만 AI 성장에 필요한 공급·클라우드·데이터센터 자본의 전진배치가 매우 커졌다는 사실은 명확하다. 따라서 다음 단계의 핵심은 매출 성장률이 아니라 **incremental ROIC와 owner cash/share**다.

## 4. 시장·거시 및 공급망

AMD는 국제매출 비중이 Q2 2026 기준 70%이고, wafer foundry와 assembly/test를 제3자에게 크게 의존한다. 공시는 Taiwan 기반 foundry/manufacturing disruption을 명시적 위험으로 제시한다.

또한 MI308은 2025년 미국 수출통제로 약 $440M의 순재고 및 관련 비용이 발생했다. 2026년에는 MI325의 일부 중국 수출 license가 허가됐으나 검사·관세 조건이 붙는다. 따라서 AI 수요 확대가 있더라도 지정학·수출통제·공급망 위험을 별개로 할인해야 한다.

## 5. 운영진·자본배분

Lisa Su 체제의 제품·사업 실행력은 높은 평가를 받을 근거가 충분하다. 다만 이번 원자료에서 가장 중요한 자본배분 논점은 환매가 아니라 **희석의 전체 구조**다.

H1 2026 AMD는 $221M의 주식을 환매했지만, 동시에 SBC $990M가 있었고 OpenAI·Meta warrant라는 매우 큰 조건부 잠재 희석이 생겼다. 2026 Proxy에서는 2023 Equity Incentive Plan에 추가 **65M shares**를 승인받는 안도 제시됐다. 환매액만 보고 주주환원을 평가하면 경제적 희석을 놓친다.

Jean Hu CFO는 2026-08-25 총 15,000주를 평균 약 $474.08에 매도했다. 그러나 공시는 이 매도가 **2026-05-19 채택된 Rule 10b5-1 plan**에 따른 것이라고 명시한다. 따라서 이 거래를 경영진의 재량적 약세 신호로 분류하지 않는다.

2026-08-19에는 Joe Householder가 이사회에서 은퇴하고 Tim Ryan이 독립이사로 합류했다. 회사는 Householder의 은퇴가 회사와의 의견불일치 때문이 아니라고 공시했다.

## 6. 하네스 결론

### 사업품질 점수: **56/75**

| 항목 | 점수 | 핵심 판단 |
|---|---:|---|
| 구조 변화·리더십 | 14/15 | AI·서버 성장과 풀스택 전환이 실제 매출에 반영 |
| 고객 가치·제품 | 8/10 | 대형 고객 수요 강함, 독립 TCO/retention 검증은 부족 |
| 해자 방향 | 10/15 | EPYC/Instinct/ROCm 개선, CUDA급 전환비용은 미입증 |
| 증분 ROIC·FCF/share | 8/15 | 현금 개선은 강하지만 약정·lease·AI 투자 수익률 미완료 |
| 경영진·자본배분 | 7/10 | 실행력 높음, warrant·SBC 경제비용 검증 필요 |
| 재무 생존 | 9/10 | 순유동성 강하지만 약정 규모 급증 |
| 기대차·가치 | 보류/15 | 동시점 가격·완전희석주식·reverse DCF 없음 |
| 파워로·비대칭 | 보류/10 | 사업 upside는 크나 가격·warrant를 포함해야 산정 가능 |

### Hard Veto

종합: **INVESTIGATE**

가장 중요한 미해결 항목은 다음 네 가지다.

1. **persistent dilution** — OpenAI/Meta warrant + SBC + equity plan overhang.
2. **incremental ROIC** — $30.3B unconditional commitments와 lease/investment 확대의 현금수익률.
3. **moat trajectory** — ROCm과 rack-scale이 실제 고객 lock-in을 만드는지.
4. **price requires unrealistic bull case** — 아직 reverse DCF 미수행.

### 현재 투자 논지

AMD는 이제 단순한 "NVIDIA의 2등 GPU" 프레임보다 넓게 봐야 한다. EPYC, Instinct, networking, system design, ROCm을 묶어 **AI compute의 두 번째 대형 플랫폼**이 될 가능성이 존재하고, H1 2026 실적은 이 가능성이 매출·영업이익·현금에 실제 반영되고 있음을 보여준다.

그러나 하네스의 투자원칙상 좋은 성장률만으로는 부족하다. OpenAI·Meta warrant와 급증한 공급·클라우드·lease 약정은 **성장 자체가 아니라 주당 현금복리의 질**을 다음 검증 대상으로 만든다.

따라서 초벌 결론은 **정밀분석 가치가 매우 높은 WATCH / P1**이다. 다음 단계는 가격을 붙이는 것이 아니라 먼저 warrant dilution waterfall, committed-cash schedule, 독립 고객 ROCm/MI450 증거를 완성한 후 reverse DCF로 넘어가는 것이다.

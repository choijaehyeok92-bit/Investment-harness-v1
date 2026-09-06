> 최신 판단: **2026-09-05 / WATCH / 73/100 / INVESTIGATE**. [한글 재평가](re-evaluation-2026-09-05.md)가 아래 과거 서술보다 우선합니다. 아래 원문은 이력 비교를 위해 보존합니다.


# NVIDIA (NVDA) 투자 논지

기준일: 2026-09-03
가격 스냅샷: $227.23 (2026-09-03 16:54:51 UTC)
최종 상태: **WATCH**
하드 베토: **INVESTIGATE**
총점: **76/100 - Emerging Outlier**

## 0. 분석 전략과 핵심 결론

이 분석은 저장소의 `screener -> deep analyst -> hard veto -> reverse valuation -> red team -> portfolio monitor` 순서를 따랐다. 사용자가 제공한 FY2026 10-K, 2026 Proxy, FY2027 Q2 10-Q와 실적 8-K, 임원 Form 4, Form 144 및 추가 의결권 자료를 우선 사용했다. 현재 가격과 공식 온라인 공시 링크만 기준일에 맞춰 보완했다.

- **Fact:** FY2027 Q2 매출은 962억 달러로 전년 동기 대비 106% 증가했고 Data Center 매출은 890억 달러로 117% 증가했다. 총마진은 75.0%, 영업마진은 66.2%였다.
- **Fact:** Q3 매출 가이던스는 1,080억 달러 ±2%이며 중국 데이터센터 컴퓨팅 매출을 포함하지 않는다.
- **Fact:** TTM 매출은 약 3,030억 달러, 영업이익은 1,976억 달러, 회사 정의 단순 FCF는 1,269억 달러다. 발행주식수는 2025년 1월 244.77억 주에서 2026년 7월 241.47억 주로 줄었다.
- **Fact:** Q2 DSO는 전분기 45일에서 60일로 늘었고, H1 AR은 246억 달러, 재고는 102억 달러 증가했다.
- **Fact:** 2026년 7월 말 공급·클라우드·미개시 리스·지분투자·CapEx 약정은 3,660억 달러이고, 별도 AI 클라우드·제3자 리스 약정은 560억 달러다. 최대 보증 노출은 1,085억 달러다.
- **Inference:** GPU 성능만이 아니라 CUDA, NVLink, 네트워킹, 랙 시스템과 개발자 생태계를 함께 제공하는 구조가 해자를 계속 넓히고 있다.
- **Inference:** 고객이 NVIDIA 인프라를 구입하고 NVIDIA가 그 고객에게 클라우드 구매약정·지분투자·리스·보증을 제공하는 모델은 수요 창출과 고객 금융지원의 경계를 흐린다. 매출의 독립적 현금 품질을 추적해야 한다.
- **Estimate:** 현재가 227.23달러는 중앙 DCF에서 약 14.2%~17.1%의 10년 매출 CAGR과 35%~45%의 장기 FCF 마진을 요구한다. Base 가치 221달러와 거의 같아 기대격차가 없다.
- **Opinion:** NVIDIA는 탁월한 기업이지만 현재 가격의 안전마진과 대규모 생태계 약정의 검증이 부족하다. 신규 포지션 없이 `WATCH`가 적절하다.

## 1. Screener

판정: **SCREEN_IN**

### 선별 근거

NVIDIA는 가속 컴퓨팅과 AI 데이터센터의 구조적 확장을 직접 주도하며, 반도체·시스템·네트워킹·소프트웨어를 하나의 플랫폼으로 판매한다. 제품 전환 중에도 세 자릿수 데이터센터 성장과 75% 총마진을 기록해 고객가치와 가격결정력이 확인된다. 현금창출과 재무생존성도 강하다.

### 조사 플래그

1. Q2 매출의 92.5%가 Data Center이고 H1 직접 고객 세 곳이 각각 16%, 15%, 13%를 차지한다.
2. 현재 시가총액 약 5.52조 달러는 장기간 높은 성장과 마진 지속을 요구한다.
3. 4,220억 달러의 미래약정과 최대 1,085억 달러 보증이 고객 수요와 자본배분의 질을 어떻게 바꾸는지 검증되지 않았다.
4. AR·DSO 상승과 지분투자를 제외하는 회사 FCF 정의 때문에 주당 현금경제성이 표면 수치보다 약할 수 있다.

## 2. 기업 및 산업 분석

### 2.1 구조적 변화와 시장 리더십

**Fact:** NVIDIA는 데이터센터 플랫폼을 GPU 단품이 아니라 GPU·CPU·DPU·NVLink·InfiniBand/Ethernet·랙 시스템과 CUDA 소프트웨어의 공동 설계로 제공한다. FY2026에는 Blackwell Ultra를 출시·확대했고 FY2027 Q3에는 Rubin 생산 출하를 시작했다. 750만 명 이상의 개발자가 CUDA 및 관련 도구를 사용한다고 회사가 공시했다.

**Inference:** AI 학습에서 추론·에이전트·물리 AI로 워크로드가 넓어질수록 시스템 전체 병목을 최적화하는 가치가 커진다. NVIDIA는 단순한 GPU 공급자가 아니라 AI 데이터센터의 사실상 아키텍처 설계자로 이동했다.

**Counter-evidence:** 현재 수요는 최종 AI 수익화보다 인프라 선점에 의해 앞당겨졌을 수 있다. 대형 클라우드 사업자는 자체 CPU·XPU·ASIC을 설계하며, AMD·Huawei·Intel과 네트워킹 경쟁사도 가격·성능을 개선하고 있다.

### 2.2 고객가치와 제품력

Q2 Data Center 매출은 890억 달러로 전년 동기 대비 117% 늘었다. Hyperscale 매출은 487억 달러로 102%, AI Clouds, Industrial & Enterprise는 403억 달러로 138% 증가했다. 이는 Blackwell Ultra의 성능과 CUDA 생태계가 하이퍼스케일러 외 고객에게도 경제적 가치를 제공한다는 강한 신호다.

고객 전환비용은 훈련된 개발자, CUDA-X 라이브러리, 모델·SDK, NVLink와 네트워킹 설계, 운영 도구에 걸쳐 누적된다. 반면 고객별 GPU 가동률, 토큰당 총비용, 재구매율과 AI 프로젝트 수익률은 공시되지 않았다. 대형 고객은 자체 칩으로 일부 워크로드를 옮기거나 멀티벤더 조달로 가격을 낮출 수 있다.

### 2.3 해자 궤적

해자는 **강화 중**으로 판단한다. FY2026 Compute & Networking 매출은 67%, Q2 FY2027에는 114% 증가했다. Blackwell Ultra 비중 개선으로 Q2 총마진이 75%로 높아졌고, Rubin을 연간 제품주기에 맞춰 조기 양산하면서 기존 Blackwell도 병행한다. GPU·네트워킹·소프트웨어를 함께 최적화하는 범위의 경제와 개발자 생태계가 서로를 강화한다.

다만 수출통제로 중국 데이터센터 시장에서 사실상 배제된 기간이 길어지면서 현지 경쟁자가 생태계를 키우고 있다. 회사가 NVLink Fusion으로 고객 자체 XPU를 수용하는 전략은 네트워킹 해자를 넓힐 수 있지만, 장기적으로 GPU 단품 점유율과 경제적 이익의 일부를 고객에게 양보할 수도 있다.

### 2.4 증분 ROIC와 FCF/주

FY2025에서 FY2026로 매출은 854억 달러, 영업이익은 489억 달러 증가했다. 약 57%의 증분 영업마진은 역사적으로 매우 높은 재투자 생산성을 보여준다. 단순 FCF는 FY2025 약 607억 달러에서 FY2026 약 966억 달러로 늘었고, TTM FCF는 약 1,269억 달러다. H1 FY2027 SBC는 40억 달러였지만 자사주 매입 398억 달러로 실제 주식 수가 감소했다.

그러나 현재 변화의 방향은 더 복잡하다.

- H1 FY2027 OCF 744억 달러는 영업이익 1,173억 달러의 약 63%다.
- AR은 반년 동안 246억 달러 증가했고, 회사는 투자등급 고객의 대형 다분기 계약에 90일~1년의 결제조건을 제공했다.
- 재고는 214억 달러에서 316억 달러로 증가했고 공급 약정은 6개월 만에 952억 달러에서 2,790억 달러로 확대됐다.
- H1 지분증권 매입 424억 달러는 회사가 제시하는 FCF에서 차감되지 않는다.

**Inference:** 과거 증분 ROIC는 탁월하지만 현재의 고객·공급 생태계 확장 자본에 같은 수익률을 적용할 근거는 아직 없다. 향후 분석의 핵심은 매출 성장보다 `현금 회수 + 약정 대비 총이익 + 주당 FCF`다.

### 2.5 경영진과 자본배분

Jensen Huang은 1993년 창업 이후 GPU, CUDA, Mellanox, Blackwell로 반복적인 제품·플랫폼 전환을 수행했다. 2026년 3월 기준 8.706억 주, 3.58%를 보유한다. 이사회 10명 중 9명이 독립 이사이며 독립 Lead Director, clawback, 임원 주식보유 지침과 헤지·담보 금지정책이 있다.

자본배분에는 긴장이 생겼다. H1 FY2027 회사는 자사주 398억 달러와 배당 63억 달러를 지급하고 지분증권을 424억 달러 매입했으며, Q2에 250억 달러의 선순위채를 발행했다. 2026년 7월 말 시장성·비시장성·지분법 투자자산은 약 990억 달러, 추가 지분투자 약정은 250억 달러다.

AI 클라우드가 NVIDIA 인프라를 구매하면 NVIDIA가 그 클라우드의 서비스를 최대 360억 달러 약정하고, 제3자 리스와 신용보증을 제공한다. 이는 시장 확대에 전략적으로 유효할 수 있으나 고객 신용위험과 수요 앞당김을 NVIDIA 대차대조표로 끌어오는 행위다. 따라서 R&D 실행력은 최고 수준이지만 현재 자본배분 점수는 6/10으로 제한한다.

2026년 8월 24일 Ajay Puri의 Worldwide Field Operations EVP 은퇴는 승계·영업 실행 모니터링 항목이다. Form 4에는 증권 거래가 없었다. Timothy Teter의 8월 31일 Form 144는 3만 주의 **매도 예정 통지**이며 완료 거래가 아니다. 발행주식의 약 0.0001% 규모로 투자논지 신호는 미미하다.

### 2.6 재무 생존성

2026년 7월 말 현금·현금성자산과 시장성 채무증권은 566억 달러, 공개 지분증권은 장기 락업분을 포함해 약 477억 달러였다. 총 차입금 약 334억 달러보다 유동 금융자산이 많고 TTM 영업현금흐름은 1,344억 달러다. 단기 지급불능이나 외부자본 의존 위험은 낮다.

하지만 미래 고정성 노출은 커졌다.

| 미래 노출 | 금액 | 성격 |
| --- | ---: | --- |
| 공급·생산능력 | $279B | 메모리·제조시설 중심, 일부 조정 가능 |
| 클라우드 서비스 | $29B | 자체 R&D용 |
| 미개시 데이터센터 리스 | $25B | 최장 20년 |
| 지분투자 약정 | $25B | 모델사·금융사 등 |
| CapEx 약정 | $8B | 엔지니어링·제조 인프라 |
| AI 클라우드 서비스 약정 | $36B | 고객이 제3자에 판매하면 감소 가능 |
| 제3자용 미개시 리스 | $20B | 재양도 예정 |
| 최대 보증 노출 | $108.5B | SB Energy/OpenAI 관련 $105B 포함 |

SB Energy 보증은 데이터센터가 가동되는 단계부터 효력이 생기며 첫 단계는 FY2029로 예상된다. 즉 1,050억 달러를 현재 부채처럼 단순 합산하는 것은 과도하지만, OpenAI의 신용등급 개선 또는 리스 종료 전까지 장기 꼬리위험이 된다.

## 3. 재무 요약

단위: USD billions, 주당 항목 제외.

| 항목 | FY2024 | FY2025 | FY2026 | TTM / 최근 |
| --- | ---: | ---: | ---: | ---: |
| 매출 | 60.9 | 130.5 | 215.9 | 303.0 TTM |
| 영업이익 | 33.0 | 81.5 | 130.4 | 197.6 TTM |
| 영업현금흐름 | 28.1 | 64.1 | 102.7 | 134.4 TTM |
| 단순 FCF | 26.9 | 60.7 | 96.6 | 126.9 TTM |
| SBC | 3.5 | 4.7 | 6.4 | 7.2 TTM |
| 발행주식수 | 246.43억 | 244.77억 | 243.04억 | 241.47억 Q2 |
| 총마진 | 72.7% | 75.0% | 71.1% | 75.0% Q2 |
| Data Center 매출 | 미표시 | 미표시 | 핵심 성장축 | 89.0 Q2 |

TTM은 FY2026에 H1 FY2027을 더하고 H1 FY2026을 뺀 값이다. FCF는 OCF에서 유형·무형자산 취득과 관련 원금지급을 뺀 회사 정의다. 지분투자, AI 클라우드 약정과 보증은 이 FCF에서 차감되지 않으므로 이를 완전한 소유주 현금흐름으로 보지 않았다.

Q2 GAAP 순이익 597억 달러에는 지분증권 평가이익 78억 달러가 포함됐다. H1 순이익 1,180억 달러에는 지분증권 이익 237억 달러가 포함된다. 따라서 GAAP P/E보다 영업이익과 FCF 기반 평가를 우선한다.

## 4. 시장 기대와 가치평가

가치평가는 목표가에서 시작하지 않고 현재가가 요구하는 미래를 역산했다. 기준은 TTM 매출 3,030억 달러, TTM FCF 1,269억 달러, 시가총액 5.518조 달러다. 현금·시장성 채무증권·공개 지분증권에서 차입금을 차감한 순금융자산 710억 달러를 반영하고, 비시장성·지분법 증권 512억 달러에는 시나리오별 할인율을 적용했다.

### 현재 가격의 내재 기대

9% 할인율, 3% 영구성장률에서 10년 차 FCF 마진을 달리하면 현재가가 요구하는 10년 매출 CAGR은 다음과 같다.

| 10년 차 FCF 마진 | 요구되는 매출 CAGR |
| ---: | ---: |
| 35% | 약 17.1% |
| 40% | 약 15.5% |
| 45% | 약 14.2% |

현재 TTM FCF 마진 41.9%는 낮은 CapEx, 높은 선급·현금수익과 성장기에 발생한 운전자본 변동의 조합이다. 이 마진을 장기간 유지하면서 10년 매출을 약 4배 이상 늘리는 것은 가능하지만 이미 큰 성공을 가격에 포함한다.

### Bear / Base / Bull

| 시나리오 | 핵심 가정 | 추정가치/주 | 현재가 대비 |
| --- | --- | ---: | ---: |
| Bear | 1년 25% 후 5년 6%, 장기 4% 성장; FCF 마진 32%; 할인율 10.5% | $92 | -60% |
| Base | 1년 32% 후 5년 13%, 장기 8.5% 성장; FCF 마진 38%; 할인율 9.0% | $221 | -3% |
| Bull | 1년 40% 후 5년 20%, 장기 12% 성장; FCF 마진 43%; 할인율 8.5% | $447 | +97% |

주관적 확률 Bear 30%, Base 50%, Bull 20%의 확률가중가치는 약 227.5달러다. 현재가와 사실상 같아 모델 오차와 실행위험을 보상하지 않는다.

### 영구손실 사례

AI 인프라 지출이 최종 고객 수익보다 빠르게 선구매됐음이 드러나고, 자체 ASIC·AMD·Huawei가 가격을 낮추며, NVIDIA의 클라우드·리스·보증 지원이 손실로 전환되는 경우다. 수출통제로 일부 지역의 개발자 생태계까지 약해지면 FCF 마진과 종단가치가 동시에 하락한다. 이때 주당 가치는 65~105달러 범위로 낮아질 수 있다. 핵심은 파산이 아니라 높은 진입가격과 장기약정으로 인한 회복 불가능한 가치 훼손이다.

## 5. Red Team 반영 후 핵심 리스크

1. AI 인프라 수요가 최종 고객 매출보다 선구매·고객금융에 의해 앞당겨짐
2. Data Center 92.5% 및 소수 직접·간접 고객에 대한 집중
3. 자체 ASIC과 경쟁 GPU가 CUDA 이식성을 개선하며 가격·점유율을 압박
4. Rubin 연간 전환, 메모리·CoWoS·전력 병목, 수요 오판으로 재고·구매의무 손실 발생
5. 중국 수출통제와 현지 경쟁 생태계 확대
6. 4,220억 달러 약정과 최대 1,085억 달러 보증의 장기 꼬리위험
7. 지분증권 평가이익이 GAAP 이익과 금융자산 완충력을 동시에 부풀릴 가능성
8. 창업자·핵심 영업인력 승계와 조직 복잡성

### 가장 중요한 반증 조건

- 데이터센터 매출·총마진·시장점유율이 경쟁 제품 또는 자체 ASIC으로 4개 분기 이상 구조적으로 하락
- DSO가 60일 이상에서 계속 상승하거나 매출채권 손실·연체가 증가하며 OCF/영업이익이 70% 미만에 장기 고착
- AI 클라우드의 제3자 사용이 늘지 않아 360억 달러 서비스 약정이 줄지 않고 NVIDIA가 사실상 미사용 용량을 떠안음
- 공급 약정과 재고가 매출보다 빠르게 늘고 재고·구매의무 충당금이 반복적으로 매출의 3%를 초과
- SB Energy/OpenAI 또는 다른 고객의 채무불이행으로 보증·리스 손실이 현실화
- 주당 FCF가 2년 이상 감소하고 자사주 매입 후에도 발행주식수가 순증가
- 회계·경영진 신뢰성 훼손 또는 공시 투명성의 구조적 악화

## 6. 최종 판단과 포트폴리오 규칙

### 결정

**WATCH / 신규 포지션 없음**

저장소에 기존 NVDA 보유와 원가가 기록되어 있지 않아 신규 커버리지로 판단했다. 기업 품질은 76점의 Emerging Outlier지만 Hard Veto가 `INVESTIGATE`이고 현재 가격은 Base 가치와 거의 같다. 가격 하락만으로 매수하지 않으며, 아래 사업 증거가 여러 개 동시에 개선되고 기대격차가 남아야 한다.

### 포지션 확대를 정당화할 증거

- 최소 2개 분기 동안 DSO와 AR/매출이 안정되며 OCF·FCF/주가 증가
- AI 클라우드의 제3자 사용으로 서비스 약정이 감소하고 제품대금이 정상 회수
- Rubin 전환 중 총마진 72% 이상, 재고충당금과 공급약정 손실 통제
- 최종 고객과 워크로드가 다변화되어 상위 직접·간접 고객 집중이 낮아짐
- 동일한 사업 가정에서 Base 가치 대비 20% 이상 할인되거나 실적 상향으로 내재 장기 성장 요구가 12% 이하로 하락

### 축소·회수를 정당화할 증거

- 반증 조건 중 하나가 일시적 변동이 아니라 구조적으로 확인
- 증분 ROIC가 자본비용 아래로 하락하거나 FCF/주 경로가 장기적으로 붕괴
- 회계·경영진 신뢰성 문제 또는 Hard Veto `FAIL`
- 가격이 현실적인 Bull Case 이상의 실행을 요구

Macro는 점수에 반영하지 않았다. 매수 속도는 `company_specific`이며 기업 증거와 기대격차로만 변경한다.

## 7. 출처와 품질

### 우선 사용한 첨부 자료

- `e361e58a-7483-44f5-bc62-a9080ae6ec72 (1)(1).pdf`: NVIDIA FY2026 Form 10-K, 2026-02-25. PwC 감사 재무제표·사업·경쟁·위험을 담은 최상위 1차 자료.
- `63577fdf-5779-45e3-898c-79c006610770(1).pdf`: 2026 Proxy, 2026-05-12. 소유구조·이사회·보상정책의 회사 1차 공시. 보상위원회와 회사의 자기평가라는 한계가 있다.
- `NVDA-2027-Q2-10Q-Final-including-exhibits(1).pdf`: FY2027 Q2 Form 10-Q, 2026-08-27. 최신 재무·약정·보증·위험을 담은 공식 1차 자료지만 미감사 수치다.
- `f5480f45-6334-4bc0-8d27-1daea2e78598(1).pdf`: FY2027 Q2 Form 8-K와 실적발표·CFO Commentary, 2026-08-26. 최신 KPI와 가이던스의 회사 자료이며 8-K 본문이 명시하듯 실적자료는 Section 18 목적상 furnished이고 filed가 아니다.
- `1bbc227b-f339-440d-a2ef-bc3373909515(1).pdf`: Ajay Puri Form 4, 2026-08-24. 은퇴 사실에는 높은 신뢰도. 거래표가 비어 있어 매도 공시로 해석하지 않았다.
- `fae7a27f-7dd3-40e4-a819-acd2441b87e7(1).pdf`: Timothy Teter Form 144, 2026-08-31. 3만 주의 매도 예정 통지이며 실제 체결 증거가 아니다.
- `015ffc59-32cd-45df-9a21-588e215e033a(1).pdf`: 추가 Proxy 자료, 2026-05-12. 투표안내 카드로 새 재무·운영 정보는 없다.

### 공식 온라인 원문

- [NVIDIA FY2027 Q2 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- [NVIDIA FY2027 Q2 results](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx)
- [NVIDIA FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- [NVIDIA 2026 Proxy](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000036/nvda-20260512.htm)
- 가격은 2026-09-03 16:54:51 UTC 시장 데이터 스냅샷. 장중 값이므로 실제 주문 전 재확인이 필요하다.

### 데이터 한계

- 고객별 현금회수, 최종 GPU 가동률, AI 프로젝트 수익률과 CUDA 이탈률은 공시되지 않는다.
- 공급·클라우드·리스·보증의 일부는 취소·감소·재양도가 가능하지만 프로젝트별 확률과 회수권 가치는 없다.
- 회사 정의 FCF는 지분투자와 생태계 금융지원을 차감하지 않는다.
- 현재 포트폴리오 내 NVDA 실제 비중, 원가, 세금·통화 조건이 입력되지 않아 포지션 크기 판단에 반영하지 않았다.
=======
# Investment Thesis — NVDA (NVIDIA Corporation)

As of: 2026-09-04 · Price: $226.27 · Position: STARTER (1–2%)
Prepared under `agents/deep-analyst.md`. Expectation gap and asymmetry are scored by
`agents/valuation.md`, not here.

---

## Sourcing note

Every financial figure below is **tier-1 SEC primary filing data**, parsed directly
from the XBRL instance documents supplied:

| Filing | Period | Filed |
|---|---|---|
| **10-K FY2026** | FY ended 2026-01-25 | 2026-02-25 |
| **10-Q Q2 FY2027** | Quarter ended 2026-07-26 | 2026-08-26 |
| DEF 14A (additional materials) | — | 2026-05-12 |
| 8-K | 2026-09-02 | 2026-09-02 |
| Form 4 (director Stevens) | 2026-08-31 → 09-02 | 2026-09-02 |
| Form 3 (EVP Parker) | 2026-08-24 | 2026-09-03 |

The **price anchor is also tier-1**: $226.27 is the last reported transaction in the
Form 4. The 8-K carried only cover-page XBRL (substance sits in an unfiled exhibit).

Two material unknowns remain, disclosed rather than estimated away: **cancellability
terms of the $279B supply commitments**, and **revenue share from equity-affiliated
entities**.

---

## 1. Structural change and market leadership — 14/15

| | FY2024 | FY2025 | FY2026 | H1 FY2027 |
|---|---|---|---|---|
| Revenue | $60,922M | $130,497M | $215,938M | $177,837M |
| Data Center | $47,525M | $115,186M | $193,737M | — |
| Operating income | $32,972M | $81,453M | $130,387M | $117,270M |
| Diluted EPS | $1.19 | $2.94 | $4.90 | $4.85 |

H1 FY2027 revenue grew **+95.8% YoY** and annualises to roughly **$356B**. Data
Center is **89.7%** of FY2026 revenue; within it Networking has gone **$8,575M →
$31,376M in two fiscal years (3.7x)**.

This scores at the category's top anchor — *"clear leader directly driving structural
change"*. NVIDIA does not benefit from the AI build-out; it defines its technical
standard (CUDA, NVLink, rack-scale systems, an annual architecture cadence).

**The deduction is geographic.** Concentration is intensifying, not diversifying: US
revenue **51.8% → 59.4% → 69.3%**. China including Hong Kong fell **$25,048M
(FY2025) → $19,677M (FY2026) → $12,430M (H1 FY2027)** — declining in absolute terms
while the total nearly doubled, now ~7% of revenue. A large market has closed. And
**76% of Taiwan-billed FY2026 revenue was to US/Europe end customers**, so the
geographic split *understates* US end-demand concentration.

## 2. Customer value and product strength — 8/10

Gross margin of **72.7% → 75.0% → 71.1% → 75.0%** on a near-doubling revenue base is
direct evidence customers are not extracting the value. CUDA plus the framework
ecosystem creates switching costs measured in engineering-years. Networking attach
growing faster than compute is the clearest proof of expanding product value.

Capped at 8 because **customer concentration is rising sharply** (below), FY2026
gross margin *fell* to 71.1% during the Blackwell ramp, and the largest customers are
precisely those funding custom-silicon alternatives.

## 3. Moat trajectory — 11/15

`agents/deep-analyst.md` demands direction over level. Direction here is **genuinely
mixed**, which is why this is the widest gap between quality and score in the file.

**Widening:** networking 3.7x in two years; rack-scale delivery turns a chip sale
into a data-centre-unit sale; R&D $8,675M → $18,497M funding a cadence no competitor
matches; gross margin recovered to 75.0% in H1 FY2027.

**Narrowing:**

| Customer One, % of Compute & Networking revenue | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| | 13% | 12% | **22%** |

Customer Two reached 14%. **Top two = 36% of segment revenue, from 23% a year
earlier.** H1 FY2027 receivables concentration is 22/14/13/11/10 — roughly **70% in
five names**. Rising concentration is the standard signature of buyer power
increasing.

**And the moat's success funds its challengers.** A 75% gross margin *is* the
business case for every customer's internal silicon programme.

## 4. Incremental ROIC and FCF/share — 13/15

Exceptional and tier-1 verified:

- **Capex is 2.8% of revenue** ($6,042M on $215,938M in FY2026); D&A $2,843M
- FY2026 operating cash flow **$102,718M**; H1 FY2027 **$74,421M**
- **Share count DOWN 2.3%** — 24,661M (2023-01-29) → **24,100M** (2026-08-21) —
  during the fastest growth phase in company history
- Buybacks $9.5B / $33.7B / $40.1B across FY2024–26, plus **$39,044M in H1 FY2027**
- SBC modest at $6,386M, **3.0% of revenue**, more than offset by repurchases
- ROE roughly **100%** in FY2026

**But the capital is committed off the balance sheet.** See §7 — this is what holds
the score at 13 rather than 15.

## 5. Management and capital allocation — 7/10

Repurchase execution is genuinely strong: **$113B across FY2024–H1 FY2027 with share
count falling**. R&D productivity is demonstrable, not asserted.

**The central question is the investment programme.** Equity stakes held have gone
from roughly **$5B to $90.7B in twelve months** ($42,783M public + $47,898M
non-marketable), with **$25B more committed** and **$29B of committed cloud-service
purchases**. NVIDIA is simultaneously supplier to, investor in, and customer of parts
of its own ecosystem.

That is defensible as ecosystem seeding. It is also a very large bet made with
shareholder capital at undisclosed hurdle rates, and it materially affects earnings
quality (§ *Earnings quality* below).

Recorded, not omitted: director Mark A. Stevens sold **1,848,501 shares (~$410M)**
2026-08-31 → 09-02. Weak evidence alone — trust-held, and NVIDIA insiders have sold
steadily for years.

## 6. Financial survivability — 9/10

Assets **$320,272M**, liabilities **$91,288M**, equity **$228,984M**. Cash $22,443M
plus $42,783M of publicly held equity securities against $32,366M of long-term debt.
H1 operating cash flow of $74,421M dwarfs every fixed obligation. **No plausible
insolvency path.**

Two flags: long-term debt went **$7,469M → $32,366M** in six months ($25B notes at
2026-06-30) — the first material leverage in the company's modern history; and
product warranty liabilities went **$306M → $1,290M → $2,807M** (9x in two years) as
rack-scale systems replace chips.

---

## Earnings quality — the adjustment that changes the multiple

**Reported H1 net income ($118,010M) EXCEEDS operating income ($117,270M).** The
reason is gain on investments:

| Gain on investments | FY2024 | FY2025 | FY2026 | H1 FY2027 |
|---|---|---|---|---|
| | $238M | $1,030M | $8,918M | **$23,707M** |

Of the H1 figure, **$12,500M is explicitly unrealised marks on publicly held
equity securities**. Roughly **17–20% of reported net income is investment
revaluation, not operations** — and the revalued assets are stakes in companies whose
spending is itself NVIDIA revenue.

Stripping it: H1 pretax $141,410M − $23,707M = $117,703M core pretax; taxed at the
actual 16.5% effective rate gives **core net income ≈ $98,282M** for the half,
**$196.6B annualised**, or **~$8.08 core annualised EPS**.

| Multiple at $226.27 | |
|---|---|
| On reported annualised EPS $9.70 | **23.3x** |
| **On core annualised EPS $8.08** | **28.0x** |

This is GAAP-compliant and disclosed. It is not an integrity failure. But every
valuation test in this file uses the **core** figure.

## 7. Key risks and concentration dependencies

**$366B of future commitments** at 2026-07-26 — the single most important risk
datapoint in this file:

| | Rem. FY27 | FY28 | FY29 | FY30 | FY31 | FY32+ | **Total** |
|---|---|---|---|---|---|---|---|
| **Supply and capacity** | 92 | 87 | 88 | 6 | 5 | 1 | **$279B** |
| Cloud service agreements | 3 | 8 | 7 | 6 | 4 | 1 | $29B |
| DC leases not commenced | — | 1 | 1 | 2 | 1 | 20 | $25B |
| Equity investments | 18 | 3 | 2 | 2 | — | — | $25B |
| Capital expenditures | 7 | 1 | — | — | — | — | $8B |
| **Total** | **120** | **100** | **98** | **16** | **10** | **22** | **$366B** |

**Supply and capacity rose from $95.2B (2026-01-25) to $279B (2026-07-26) — +193% in
six months.** That is ~78% of annualised revenue, and it is the *real* capital
commitment of a business reporting 2.8%-of-revenue capex. The recorded
excess-inventory purchase accrual is only **$2,138M** — the accounts assume full
consumption.

**Three concentrations compound:** end market (Data Center 89.7%), customer (top two
36% of segment revenue, top five 70% of receivables), geography (US 69.3%). And per
this harness's own screening work, those customers are funding purchases **from
balance sheet rather than operating cash flow** — hyperscaler 2026 capex is guided
above $725B while Alphabet posted its first negative-FCF quarter since 2004 and
Meta's cash generation fell 91% YoY.

**Critically, the risks are correlated, not independent.** The same demand pause that
triggers the supply write-down also marks down the $90.7B investment portfolio and
hits the customers behind the concentration. That is why the modelled bear is
−56% to −68% despite a fortress balance sheet.

---

## Most important unknowns

1. **Cancellability terms of the $279B.** The 10-K says these agreements are *"in
   certain instances"* cancellable, reschedulable or adjustable — without
   quantifying. This determines whether the bear is a margin event or a
   balance-sheet event.
2. **Revenue share from equity-affiliated entities.** Bounded below ~10% on a
   worst-case assumption, but unquantified.
3. Realised/unrealised split and cost basis of the $47,898M non-marketable portfolio.
4. Identity and funding structure of the 22% customer.
5. Merchant-GPU versus custom-ASIC share of total accelerator deployments.

## Evidence that would strengthen the thesis

- Equity-affiliated revenue quantified below ~5% and stable
- Supply commitments disclosed as materially cancellable
- Top-customer concentration stabilising or falling from 22%
- Gross margin holding ≥75% through the Rubin ramp
- Investment gains falling as a share of net income

## Evidence that would weaken the thesis

- Equity-affiliated revenue above ~10%, or growing faster than third-party revenue
- Supply commitments rising while sequential revenue decelerates
- The excess-inventory accrual rising materially from $2,138M — management's own signal
- Gross margin below ~70% outside a product transition
- A hyperscaler capex guidance cut

---

## Why STARTER here and NONE for Samsung

Both carry unresolved HIGH-severity vetoes. The difference is the **expectation gap**.

For 005930 the normalised model landed **below** what the price required — the gap
was negative, so no position was justified at any veto status. For NVDA, at 23.3x
reported / **28.0x core** annualised earnings, a 25x mature multiple requires roughly
the **current core earnings base to persist with no growth**. The gap is positive,
though thin.

`policy/position-sizing.yaml` defines STARTER as *"attractive thesis, but evidence is
still limited."* That describes this exactly: exceptional business quality (75/100,
Emerging Outlier — the highest in this harness to date), a positive gap, bounded
risks, 2–3% permanent-loss probability — against three open HIGH-severity gates and a
probability-weighted five-year return of only **+21% total (3.9%/yr)**.

Macro pacing is **slow**: per the 2026-09-04 screening run the AI-capex complex is
treated as a single correlated exposure, and NVDA is its centre of gravity.

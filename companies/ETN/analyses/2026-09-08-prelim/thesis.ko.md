# Eaton Corporation plc (ETN) — 2026-09-08 원자료 기반 초벌분석

판정: **WATCH** · 연구 상태: `PARTIAL_ANALYSIS` 체크포인트 · 매수 승인: 없음 · 후속 조사: **P1**

> 이 문서는 사용자가 지정한 2025 Form 10-K, 2026 Q2 Form 10-Q, 2026 Q2 실적 8-K/Exhibit 99, 2026-09-03 Form 4를 기반으로 한 초벌분석이다. QuoteMedia 링크는 동일 날짜·형식의 SEC EDGAR 원문으로 해소해 검증했다. 현재 `companies/ETN/latest.json` 및 2026-09-06 frozen harness authority를 덮어쓰지 않는다. 가격 동기화·reverse DCF가 없으므로 기대차/비대칭 점수와 매수 승인은 보류한다.

## 0. 분석 전략

이번 단계의 목적은 세 가지다.

1. **수요의 질**: 데이터센터·전력설비 수요가 단순 사이클인지, firm orders/backlog로 이어지는 구조적 수요인지 확인한다.
2. **현금 귀속**: 높은 주문과 매출이 정상화 마진·운전자본·Capex를 거쳐 주당 owner cash로 이어지는지 확인한다.
3. **Boyd 인수 리스크**: 2026년 대규모 차입과 $9.55B Boyd Thermal 인수가 9% 미국 허들을 넘는 증분 ROIC를 만드는지 별도 검증한다.

핵심 원칙은 `Hard Veto > Score`이며, backlog·조정 EPS·회사 가이던스를 현금 가치와 동일시하지 않는다.

## 1. 기본 정보 및 원자료

원자료 정규화 파일:

- `reviews/2026-09-08-etn-prelim/raw-data.json`

확인한 공시는 다음과 같다.

- FY2025 Form 10-K — 2026-02-26
- Q2/H1 2026 Form 10-Q — 2026-07-31
- Q2 2026 earnings Form 8-K / Exhibit 99 — 2026-07-31
- Shawn M. Black Form 4 — 2026-09-03

Form 4는 4,605 RSU 부여를 보고한 것이며 시장 매도가 아니다. 따라서 내부자 약세 신호로 분류하지 않는다.

## 2. 기업·산업 분석

### 구조적 성장

Q2 2026 총매출은 **$8.531B**, 전년 동기 $7.028B 대비 약 **21.4% 증가**했다. 회사가 제시한 organic growth는 **14%**다.

핵심은 Electrical의 주문이다.

| 항목 | Electrical Americas | Electrical Global | Aerospace |
|---|---:|---:|---:|
| Q2 매출 | $3.951B | $2.517B | $1.222B |
| Organic growth | 18% | 18% | 7% |
| Organic orders 변화 | +41% | +33% | +17% |
| Backlog | $15.175B | $3.602B | $5.164B |
| Backlog YoY | +33% | +103% | +28% |
| Book-to-bill | 1.3x | 1.1x | 1.2x |

Eaton은 backlog를 **customers are firmly committed인 orders**로 정의한다. 이는 단순 관심지표보다 강한 수요 증거다. 다만 이번 공시만으로 모든 backlog가 취소 불가능하거나 현금매출과 동일한 경제적 권리를 가진다고 볼 수는 없다.

Electrical Americas와 Electrical Global 모두 데이터센터와 machine OEM을 핵심 성장 동력으로 명시했다. Aerospace도 commercial OEM/aftermarket 수요가 강하다. 따라서 현재 수요는 단일 사업 하나가 아니라 여러 핵심 부문에서 동시에 확인된다.

### 고객가치와 해자

현재 공시가 지지하는 해자 가설은 다음과 같다.

- 전력분배·보호·제어 제품의 설치 기반과 프로젝트 사양 편입
- 데이터센터·산업·항공 고객의 높은 신뢰성 요구
- 전기 + 열관리 제품 포트폴리오 결합
- 글로벌 채널·서비스 능력
- 고객 분산: 2025년 단일 고객이 연결 매출의 10%를 초과하지 않음

다만 primary filing만으로 전환비용, 경쟁사 대비 총소유비용, bid win-rate, lead-time 기반 가격결정력을 직접 입증할 수는 없다. 따라서 moat trajectory는 강하게 보되 완료 판정은 하지 않는다.

## 3. 재무 분석

### FY2025

- 매출: **$27.448B**
- Eaton 주주 귀속 순이익: **$4.087B**
- 희석 EPS: **$10.45**
- OCF: **$4.472B**
- Capex: **$0.919B**
- 제한적 `OCF - Capex` 프록시: **$3.553B**
- 희석 가중평균 주식수: **391.2M**
- 제한적 프록시/희석주: 약 **$9.08**

이 프록시는 완전한 owner FCF가 아니다. 인수지출, 정상화 운전자본, 주식보상, 부채서비스 등을 별도로 연결해야 한다.

### H1 2026

- 매출: **$15.982B**, 전년 대비 약 **+19.2%**
- 주주 귀속 순이익: **$1.687B**, 전년 $1.945B
- OCF: **$1.634B**, 전년 $1.156B
- Capex: **$0.446B**
- 제한적 `OCF - Capex` 프록시: **$1.188B**
- 희석 가중평균 주식수: **389.4M**

매출과 OCF는 증가했지만 순이익은 감소했다. 주요 이유는 인수 관련 비용, 무형자산 상각, 높은 이자비용과 세율이다. 따라서 조정 EPS만으로 현금 복리성을 평가하면 안 된다.

### 마진

Q2 segment margin은 회사 기준 **23.1%**였다.

- Electrical Americas: **27.5%**
- Electrical Global: **19.8%**
- Aerospace: **22.8%**
- Mobility: **13.0%**

Electrical Americas Q2 margin은 전년 29.5%에서 27.5%로 하락했고 H1은 29.7%에서 26.6%로 하락했다. 회사는 주된 원인으로 commodity inflation을 제시했다. Electrical Global은 H1 기준 19.4%에서 19.6%, Aerospace는 22.6%에서 24.7%로 개선됐다.

중요한 질문은 commodity 압력이 정상화될 때 Americas 마진이 회복되는지, 반대로 현재 높은 수요가 경쟁 공급 확대로 가격 압력을 받는지다.

## 4. Boyd Thermal과 자본배분

2026-03-12 Eaton은 Boyd Thermal을 현금 순액 **$9.549B**에 인수했다.

6월 말 기준 잠정 PPA:

- 식별 순자산: **$5.817B**
- Goodwill: **$3.733B**
- 기타 무형자산: **$7.190B**
- Boyd 취득 후 6월 말까지 매출: **$524M**
- 동일 기간 segment operating profit: **$121M**
- 단순 취득 후 segment operating margin: 약 **23.1%**

Goodwill은 현금대가의 약 39%, 기타 무형자산은 약 75%다. 이 비율을 서로 합산해 인수 프리미엄이라고 해석하면 안 된다. 식별 자산·부채를 포함한 PPA 구조상 중복 오해가 생기기 때문이다.

현재 하네스에서 가장 중요한 리스크는 **인수 후 증분 ROIC**다. Boyd가 데이터센터 thermal-management content를 늘려 사업 해자를 강화할 가능성은 분명하지만, 매출 성장만으로 $9.55B 투자수익률을 정당화할 수 없다.

### 차입 증가

2026년 6월 말:

- Cash: **$483M**
- Short-term investments: **$212M**
- Short-term debt: **$2.091B**
- Current long-term debt: **$11M**
- Long-term debt: **$18.509B**

단순 합산 debt는 약 **$20.611B**, cash + short-term investments는 **$695M**이다.

Eaton은 2026년에 $8.5B U.S. notes와 €1.2B euro notes를 발행했고 commercial paper $2.088B가 남아 있었다. $4B revolver에는 차입이 없었으며 debt covenants는 준수 중이다.

즉 **생존 위험은 낮지만 자본배분 위험은 높아졌다.** 외부자본 의존 hard veto는 회사 존속 문제가 아니라 Boyd의 투자수익률과 디레버리징 경로를 검증하기 위해 `INVESTIGATE`로 남긴다.

## 5. 운영진·자본배분

긍정적 요소:

- Mobility를 Dana와 Reverse Morris Trust로 분리하여 Electrical/Aerospace 중심으로 포트폴리오를 집중
- Boyd 인수 이후 2026년 buyback을 중단해 차입과 환매를 동시에 확대하지 않음
- FY2025 재무제표와 ICFR에 대해 감사인이 무수정 의견을 제시

주의 요소:

- Boyd + Ultra PCS 취득으로 H1 acquisition cash outflow가 약 **$11.1B**
- 이자비용이 H1 전년 $103M에서 $307M으로 증가
- Boyd PPA가 잠정치이며 향후 조정 가능
- 2025 취득 법인들은 당시 ICFR 감사 범위에서 일부 제외됨

9월 Form 4에서 Aerospace Group President Shawn M. Black에게 4,605 RSU가 부여됐다. 이는 주식 매도가 아니므로 별도의 bearish insider signal로 처리하지 않는다.

## 6. 초벌 결론

### 정책 점수

| 항목 | 점수 |
|---|---:|
| 구조 변화·리더십 | 14/15 |
| 고객 가치·제품 | 9/10 |
| 해자 방향 | 12/15 |
| 증분 ROIC·주당 현금 | 9/15 |
| 경영진·자본배분 | 7/10 |
| 재무 생존 | 8/10 |
| 기대차·밸류에이션 | 보류/15 |
| 파워로·비대칭 | 보류/10 |

**사업품질: 59/75**

총점은 보류한다. 가격과 reverse DCF가 없는 상태에서 좋은 기업을 좋은 투자라고 승격하지 않는다.

### Hard Veto

- management_or_accounting_integrity: **PASS**
- external_capital_dependence: **INVESTIGATE**
- persistent_dilution: **PASS**
- low_quality_growth: **PASS**
- incremental_roic_collapse: **INVESTIGATE**
- moat_shrinkage: **INVESTIGATE**
- price_requires_unrealistic_bull_case: **INVESTIGATE**
- fatal_concentration: **PASS**
- permanent_loss_probability: **INVESTIGATE**

종합: **INVESTIGATE**

### 핵심 투자 가설

Eaton의 수요 증거는 현재 상당히 강하다. 특히 Electrical Americas의 order +41%, backlog +33%, Electrical Global order +33%, backlog +103%는 단순 매출 성장보다 더 중요한 선행지표다.

하지만 지금부터의 핵심은 **수요가 있느냐가 아니라, 그 수요를 위해 투입한 $9.55B Boyd 자본과 늘어난 부채가 주당 현금복리를 얼마나 만들어내는가**다.

### 가장 강한 Bear 논지

시장이 데이터센터·전력설비 초과수요의 긴 지속기간을 이미 가격에 반영한 상태에서 Eaton이 Boyd를 위해 레버리지를 크게 높였을 수 있다. 공급 증설과 commodity 정상화 이후 수주 성장과 가격력이 둔화하고, Boyd의 현금 ROIC가 낮으면 매출 성장에도 불구하고 주당 owner cash는 시장 기대를 밑돌 수 있다.

### 다음 정밀분석 우선순위

1. Electrical backlog의 취소권·해지조건·선수금·실제 매출 전환율
2. Electrical 가격/물량 분해와 lead-time 정상화
3. Boyd stand-alone 매출·영업현금·운전자본·Capex·인수금융비용
4. Mobility 분리 후 pro-forma 재무와 주식권리
5. 최신 가격 동기화 후 reverse DCF
6. Bear/Base/Bull에서 디레버리징과 정상화 마진을 결합한 owner-cash 모델

현재 판정은 **WATCH / P1**이다. 연구 우선순위가 높다는 의미이며 매수 승인이나 포지션 추천이 아니다.

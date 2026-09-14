# Salesforce (CRM) 심층 투자 논지 — 2026-09-14

## Harness 판정

- Research state: **FULL_ANALYSIS**
- Decision: **WATCH**
- Priority: **P2**
- Score: **76 / 100 — Emerging Outlier**
- Business quality: **60 / 75**
- Hard Veto: **INVESTIGATE — moat_shrinkage**
- Buy authorized: **false**
- Reference price: **$247.72 (2026-09-11)**

## 한 문장 논지

Salesforce는 전통적인 좌석 기반 CRM에서 기업의 데이터·메타데이터·권한·업무흐름을 기반으로 인간과 AI 에이전트가 실제 행동을 수행하는 **enterprise action/orchestration layer**로 진화할 수 있는 유력 후보지만, 현재 주가는 Q2 이후 상당히 재평가됐고 AI가 오히려 Salesforce 인터페이스와 좌석 경제를 우회할 가능성, 그리고 $25B 부채조달 자사주매입으로 높아진 레버리지를 함께 감수해야 한다.

## 1. 사업과 구조적 변화

Salesforce의 장기 자산은 단순 CRM UI가 아니다. 고객 데이터, 메타데이터, 권한체계, 영업·서비스·마케팅 업무흐름, MuleSoft API, Slack 협업 인터페이스, Data 360, 그리고 Informatica의 데이터 품질·거버넌스가 한 플랫폼에 연결돼 있다. Agentforce가 성공하면 LLM의 추론 능력을 기업의 실제 데이터와 결정론적 업무 규칙에 연결해 **말하는 AI를 행동하는 AI로 전환하는 레이어**가 될 수 있다.

Q2 FY2027 기준 Agentforce + Data 360 ARR은 약 $3.9B로 전년 대비 210% 이상 증가했고 Agentforce ARR만 $1.5B를 넘었다. 누적 Agentic Work Units는 7B, Q2만 3.2B로 전분기 대비 97% 증가했다. 이는 단순 데모 단계를 넘어 실제 사용량이 빠르게 늘고 있음을 보여준다.

그러나 Q2부터 Agentforce ARR 정의가 AI offerings, Slackbot, Headless 360까지 넓어졌기 때문에 240%+ 성장률을 순수 standalone Agentforce의 동질적 성장률로 볼 수는 없다.

## 2. 기존 코어의 건강성

FY2026 매출은 $41.5B로 10% 증가했고 OCF는 $15.0B로 15% 증가했다. cRPO는 $35.1B로 16% 증가했으며 attrition은 약 8%로 안정적이었다. FY2027 상반기에도 매출은 12%, cRPO는 14% 증가했다.

Q2 subscription/support revenue는 $10.8B로 12% 증가했으며 회사는 이 증가가 가격이 아니라 신규 고객, 업그레이드, 기존 고객의 추가 구독 등 **volume driven**이라고 설명했다. 고객 기반이 가격 인상만으로 버티는 구조는 아니다.

다만 Q2 매출 $11.345B에는 Informatica $456M이 포함됐다. 이를 기계적으로 제외하면 Q2 성장률은 약 6.4%, 상반기는 약 7.5%다. 이는 공식 organic growth 지표가 아니라 진단용 계산이지만, 현재의 두 자릿수 headline 성장에서 M&A 기여를 분리해야 함을 보여준다.

## 3. 해자 — 강하지만 방향은 아직 미확정

강점은 명확하다.

1. 기업의 customer system-of-record.
2. 데이터·메타데이터·권한·감사추적.
3. MuleSoft/통합 생태계.
4. Data 360와 Informatica를 통한 데이터 품질·거버넌스.
5. Slack을 통한 conversational interface.
6. 수년간 구축된 고객별 업무규칙과 자동화.

이 자산들은 범용 LLM 자체가 쉽게 복제하기 어렵다. AI 에이전트가 실제 기업 업무를 수행하려면 어떤 데이터에 접근할 수 있는지, 어떤 행동이 허용되는지, 결과를 어떻게 기록하고 감사할지를 알아야 하기 때문이다.

반대 시나리오는 매우 중요하다. OpenAI·Anthropic·Microsoft 등의 범용 에이전트가 사용자의 주 인터페이스를 차지하고 Salesforce를 단순 데이터베이스/API로 호출하게 된다면 Salesforce의 데이터 중요성은 유지되면서도 **가치 포착은 약해질 수 있다.** 좌석 수와 UI 중심 가격결정력이 감소할 수 있기 때문이다.

따라서 `moat_shrinkage`는 현재 실패 판정이 아니라 **INVESTIGATE**다. 현 cRPO/retention은 해자 붕괴를 보여주지 않지만, 3~5년 뒤 agentic interface의 가치 포착 주체가 누구인지 아직 확정되지 않았다.

## 4. 현금창출과 SBC

TTM은 FY2026 + H1 FY2027 - H1 FY2026 방식으로 계산했다.

- Revenue: 약 $43.94B
- OCF: 약 $15.75B
- Capex: 약 $0.60B
- 단순 OCF-capex: 약 $15.15B
- SBC: 약 $3.67B
- 정상화 owner cash: **$10.5B-$11.5B, 중앙 $11.0B**

OCF-capex $15.15B를 그대로 FCF로 사용하지 않는다. OCF는 SBC를 비현금비용으로 다시 더하기 때문이다. 주주 관점에서 SBC는 실제 경제비용이며, 이를 상쇄하려면 자사주 매입 현금이 필요하다.

중앙 owner cash $11B는 매출의 약 25%다. Salesforce는 여전히 매우 높은 현금창출력을 가진 소프트웨어 사업이다.

## 5. 자사주 매입과 자본배분

FY2026에는 약 $12.7B를 자사주 매입에 사용했다. 2026년 3월에는 더 공격적으로 **$25B의 장기채를 발행해 $25B accelerated share repurchase를 실시**했다. 초기 103M주를 평균 $198.34에 인도받았다.

결과적으로 Q2 diluted share count는 전년 962M에서 821M으로 크게 감소했고, 2026년 2월 약 923M이던 실발행주식 수도 8월 약 823M으로 감소했다.

$198.34라는 매입가격 자체는 현재 $247.72보다 낮았고 내재가치 추정과 비교해도 합리적인 수준일 수 있다. 그러나 **부채를 늘려 주식을 사는 행위와 영업 자체의 개선은 구분해야 한다.**

7월 말 debt는 약 $39.3B로 상승했고 cash + marketable securities는 $11.4B다. 신규 이자비용 때문에 FY2027 OCF/FCF 성장 가이던스는 약 4%-5%에 그친다. 따라서 management & capital allocation은 6/10으로 제한한다.

## 6. Informatica와 M&A

Informatica는 약 $9.6B에 인수됐고 Salesforce의 agentic 전략과 논리적으로 맞는다. AI 에이전트의 정확도와 신뢰는 결국 기업 데이터의 품질·계보·거버넌스에 달려 있기 때문이다.

그러나 전략적 적합성과 투자수익률은 다르다. Salesforce는 과거 Slack, Tableau, MuleSoft 등 대형 인수를 반복했다. Informatica, Qualified, 향후 Contentful/Fin까지 이어지는 M&A가 실제 incremental ROIC를 높이는지는 향후 별도로 검증해야 한다.

## 7. 재무 생존성

레버리지는 높아졌지만 생존성 자체는 강하다.

- cash + marketable securities: 약 $11.4B
- debt: 약 $39.3B
- TTM OCF: 약 $15.75B
- $5B revolver: 미사용
- 부채 만기: 2028~2066년으로 분산
- subscription/support: 약 매출의 95%
- attrition: 약 8%

또한 strategic investments는 $11.3B이며 Anthropic 지분 평가액이 약 $5.1B다. 다만 private-market valuation은 변동성이 크므로 이를 현금과 동일하게 보지 않는다.

## 8. 밸류에이션과 시장 기대

기준가격 $247.72, 중앙 owner cash $11B, 823M주 기준:

- Market cap: 약 $203.9B
- Owner-cash multiple: 약 **18.5x**
- Owner-cash yield: 약 **5.4%**

Reverse DCF에서 10% 요구수익률과 16x terminal multiple을 사용하면 현재 가격이 요구하는 10년 owner-cash/share CAGR은 약 **5.5%**다.

이는 비현실적 기대는 아니다. cRPO가 14% 성장하고 있고 share count가 크게 감소했기 때문이다. 반면 현재 가격은 Adobe처럼 장기 정체를 가정한 가격도 아니다. 특히 Q2 발표 다음 날 주가가 약 22.6% 급등하며 AI 회복 기대가 상당 부분 반영됐다.

### 시나리오

- Permanent-loss stress: **$89** (-64%)
- Bear: **$148** (-40%)
- Base: **$278** (+12%)
- Bull: **$435** (+76%)
- 주관적 확률가중 가치: **약 $258** (+4%)

Base는 첫 5년 owner-cash/share +7%, 다음 5년 +5%, 10% 할인율, 18x terminal을 사용한다. 현 주가에서는 충분히 좋은 사업이어도 **큰 안전마진은 아니다.**

## 9. Scorecard

| 항목 | 점수 |
|---|---:|
| Structural change & leadership | 13 / 15 |
| Customer value & product | 9 / 10 |
| Moat trajectory | 11 / 15 |
| Incremental ROIC & FCF/share | 12 / 15 |
| Management & capital allocation | 6 / 10 |
| Financial survivability | 9 / 10 |
| Expectation gap & valuation | 10 / 15 |
| Power-law & asymmetry | 6 / 10 |
| **Total** | **76 / 100** |

## 10. Red Team 핵심

가장 강한 Bear 논지는 Salesforce가 사라지는 것이 아니다. Salesforce의 고객 데이터와 레코드는 계속 남아 있지만 사용자가 직접 접하는 인터페이스와 의사결정은 범용 AI 에이전트가 차지하고, Salesforce는 backend/API로 가격이 재평가되는 시나리오다.

동시에 headline 성장의 일부는 Informatica 인수이고, Agentforce ARR 정의도 확대됐다. 대규모 부채조달 자사주매입은 EPS와 주당 FCF를 빠르게 개선하지만 영업 자체의 경쟁력이 향상됐다는 뜻은 아니다.

따라서 다음 두 가지를 분리해서 추적해야 한다.

1. **Organic operating improvement** — cRPO, organic revenue, retention, Agentforce/Data paid consumption, owner cash.
2. **Financial engineering** — ASR에 따른 share-count 감소와 추가 leverage.

## 11. 판정을 올릴 증거

- 인수효과 제외 매출 성장률이 8%-10%로 재가속하고 cRPO가 12% 이상 유지.
- Agentforce/Data 360 지표 정의가 안정된 후에도 높은 성장이 유지되고 사용량이 NNAOV·ARR·owner cash로 연결.
- ASR 이후 owner-cash/share가 추가 leverage 없이 high-single-digit 이상 성장.
- 내부 현금으로 net debt를 줄이기 시작.
- 고객 증거에서 Salesforce가 범용 모델을 불문하고 enterprise system-of-record 및 action/governance layer로 남음.

## 12. 논지를 깨는 증거

- cRPO <8%가 2개 분기 지속되고 attrition >10%.
- 인수효과 제외 매출 성장 <5%가 2개 분기 지속.
- Agentforce usage는 늘지만 net-new orders/cRPO/owner cash가 개선되지 않음.
- AI 에이전트가 Salesforce 좌석과 인터페이스를 대체하면서 가격결정력 악화.
- debt가 높은 상태에서 또 대규모 debt-funded buyback 또는 고가 M&A 실행.

## 결론

Salesforce는 AI에 의해 즉시 파괴될 구형 SaaS라기보다, 오히려 기업의 데이터·업무규칙·권한·행동을 연결한다는 점에서 agentic AI 시대의 중요한 인프라 후보에 가깝다. 현재 실적도 cRPO 14%, 안정적인 8% attrition, 빠른 Agentforce/Data 360 사용 증가로 이를 지지한다.

그러나 현재 $247.72에서는 Q2 이후 재평가가 상당히 진행됐고, Base 가치 대비 여유가 약 12%에 불과하다. 또한 $25B debt-funded ASR 때문에 주당지표 개선의 일부는 금융구조 변화다.

따라서 현재 Harness 판정은 **FULL_ANALYSIS / WATCH / P2 / 76점**이다. 신규 집중매수보다 organic AI monetization과 debt-adjusted owner-cash/share의 추가 증거를 기다리는 것이 적절하다.

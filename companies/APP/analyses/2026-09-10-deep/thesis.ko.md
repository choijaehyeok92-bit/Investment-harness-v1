# APP(AppLovin) 심층분석 체크포인트 — 2026-09-10

## 판정

- Decision: **WATCH**
- Priority: **P1**
- Buy authorized: **false**
- Business quality: **60/75**
- Total score: **76/100 — Emerging Outlier**
- Hard Veto overall: **INVESTIGATE**
- 미국 요구수익률: **9%**
- 기준가격: **$305.06 (2026-09-09 research reference)**

이 파일은 심층분석 결과를 저장한 비권위 연구 체크포인트다. `companies/APP/latest.json`이나 registry를 갱신하지 않으며, 별도의 전체 authority run과 validator 통과 전에는 canonical current 판단을 대체하지 않는다.

## 투자 논지

AppLovin의 핵심은 AI라는 테마가 아니라 **Axon이 광고주에게 더 높은 경제가치를 만들어 그 가치의 일부를 매우 높은 현금마진으로 포착할 수 있는가**이다. Apps 사업 매각 후 광고플랫폼에 집중했고, Q2 2026 매출은 약 $1.924B로 전년 대비 53% 성장했으며 영업이익은 약 $1.494B였다. 회사 정의 FCF도 약 $863M이다.

최근 성장의 질은 강하다. 설치량 자체보다 설치당 monetization이 급증했고, SBC가 매출 대비 낮은 한 자릿수에 머무는 동안 실제 희석주식수와 기말 주식수가 감소했다. 이는 단순한 회계상 성장보다 FCF/share 성장에 가까운 패턴이다.

다만 광고 inventory 비용을 publisher 지급액 차감 후 순액으로 인식하는 agent accounting을 사용하므로 70%대 영업마진을 Meta 등 gross-revenue 광고회사와 직접 비교하면 안 된다. 절대 현금창출력이 매우 강하다는 결론과 peer margin comparability는 별개다.

## 해자

현재 gaming 영역의 moat는 데이터·모델·inventory·광고주가 상호 강화되는 flywheel과 독립 industry data에 의해 어느 정도 뒷받침된다. 그러나 e-commerce는 아직 제2의 확정 엔진이 아니라 옵션으로 다룬다. 필요한 증거는 advertiser-level ROAS, cohort retention, traffic quality, 경쟁 플랫폼 대비 spend share 및 switching behavior다.

Apple, Google, Meta 등 외부 플랫폼의 정책은 APP가 통제할 수 없는 핵심 control point다. 따라서 높은 현재 monetization이 곧 영구적 해자를 의미하지 않는다.

## 자본배분

Apps 사업을 정리하고 더 높은 수익성이 확인된 광고플랫폼으로 자원을 집중한 결정은 긍정적이다. 반면 H1 2026 자사주 매입은 3.275M주, $1.533B로 기계적 평균 약 $468/주이며 FY2025도 기계적 평균 약 $399/주다. 현재 reference $305보다 훨씬 높은 가격에서 대규모 환매가 이루어졌다.

주가 하락만으로 과거 환매가 가치파괴였다고 단정할 수 없지만, 하네스의 `repurchase_price_discipline` 기준에서는 감점 요인이다. 따라서 Management & Capital Allocation은 5/10으로 평가한다.

## SEC·거버넌스

FY2025 감사 및 ICFR, Q2 2026 disclosure controls에서 회계 신뢰성을 직접 훼손하는 증거는 확인되지 않았다. 그러나 Reuters는 2026년 2월 AppLovin 관련 SEC 조사가 여전히 진행 중이라고 보도했다. 이는 위법의 증거가 아니지만 conduct/integrity veto를 닫지 못하게 하는 충분한 불확실성이다.

또 Adam Foroughi와 Voting Agreement parties의 높은 의결권 집중은 Class A minority owner에게 구조적 governance risk다. 독립이사회와 위원회는 완충장치지만 지배권 자체를 상쇄하지 못한다.

## 밸류에이션

TTM deep-review bridge는 대략 매출 $6.83B, 영업이익 $5.29B, continuing net income $4.41B, company-defined FCF $4.51B, SBC $0.284B, 보수적 `FCF-SBC` proxy $4.22B를 사용한다.

9% 요구수익률, 5년 명시기간, terminal growth 3% 기준 reverse DCF에서 현재 가격이 요구하는 성장률은 company FCF 기준 약 9.5%, `FCF-SBC` 기준 약 11.1%다. 즉 현재 가격이 현행 50%대 매출성장을 장기간 요구하는 것은 아니다. 문제는 출발점인 2026년 FCF와 margin이 정상화된 수준인지 여부다.

| Scenario | Starting owner FCF | 5Y CAGR | Terminal g | 가치/주 | 기준가 대비 |
|---|---:|---:|---:|---:|---:|
| Bear | $3.50B | 5% | 2.0% | ~$173 | -43% |
| Base | $4.225B | 12% | 3.0% | ~$317 | +4% |
| Bull | $4.225B | 20% | 3.5% | ~$469 | +54% |

Base가 현재가와 거의 겹치므로 명백한 margin of safety는 아니다. 반면 `price_requires_unrealistic_bull_case` veto는 PASS가 타당하다.

## Scorecard

| 항목 | 점수 |
|---|---:|
| Structural Change & Leadership | 14/15 |
| Customer Value & Product | 8/10 |
| Moat Trajectory | 11/15 |
| Incremental ROIC & FCF/share | 13/15 |
| Management & Capital Allocation | 5/10 |
| Financial Survivability | 9/10 |
| Expectation Gap & Valuation | 10/15 |
| Power Law & Asymmetry | 6/10 |
| **Total** | **76/100** |

## Hard Veto

- management_or_accounting_integrity: **INVESTIGATE** — SEC/conduct matter unresolved
- external_capital_dependence: **PASS**
- persistent_dilution: **PASS**
- low_quality_growth: **PASS**
- incremental_roic_collapse: **PASS**
- moat_shrinkage: **PASS / monitor**
- price_requires_unrealistic_bull_case: **PASS**
- fatal_concentration: **INVESTIGATE** — Axon/mobile-platform dependency
- permanent_loss_probability: **INVESTIGATE**

점수 76은 Hard Veto를 덮어쓰지 못한다. 따라서 WATCH를 유지한다.

## 무엇이 상향 조건인가

Q3 가이드 충족/상회와 Axon re-acceleration, 독립적인 e-commerce ROAS·cohort retention, SEC 이슈의 중대한 제재 없는 종결, owner FCF/share 12~15% 이상의 지속 성장, 보수적 내재가치 이하 환매가 함께 확인되어야 한다.

## 반증

Axon advertiser economics가 악화하면서 매출·margin이 동시에 둔화하거나, 주요 플랫폼 정책이 targeting/traffic 접근을 훼손하거나, SEC 조사 결과가 경영진 신뢰성에 중대한 손상을 주거나, 현재 owner cash가 peak였음이 드러나면 논지를 다시 작성한다.

## 결론

APP는 현재 가격에서 valuation 자체가 가장 큰 문제는 아니다. **경제적 지속성·플랫폼 종속·conduct/governance가 핵심 위험**이다. 현재 cash economics가 구조적이라는 증거가 강화되면 $305는 합리적인 가격이 될 수 있으나, 그 증거가 부족한 상태에서 concentration과 integrity veto를 무시한 신규 매수는 하네스 규칙에 맞지 않는다.

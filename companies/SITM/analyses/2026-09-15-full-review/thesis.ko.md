# SiTime (SITM) 심층 분석 — 2026-09-15

## 0. 분석 전략

사용자 제공 FY2025 10-K, Q2/H1 2026 10-Q, 2026-08-05 8-K를 1차 원천자료로 사용했다. 2026-09-08 제출된 Renesas Timing Product Business 8-K/A와 취득사업 재무, SiTime 공식 실적·제품 자료, 2026-09-09 경영진 컨퍼런스 발언, 2026-09-14 종가를 보완했다. 회사 품질과 가격을 분리하고, 8개 점수·9개 Hard Veto·역산 가치평가·Bear/Base/Bull·레드팀을 적용했다. NVIDIA/Tesla/Palantir/Google/Amazon 초기형 비교는 기존 100점 점수를 변경하지 않는 보조 혁신 렌즈다.

## 1. 기본 정보와 핵심 결론

**판정: WATCH / P1 / Emerging Outlier / 75점.**

SiTime은 더 이상 단순 MEMS oscillator 공급자로 평가하면 안 된다. 회사가 만든 `Precision Timing`이라는 범주에서 oscillator를 기반으로 clock IC, resonator, synchronization software로 수직·수평 확장해 왔고, 2026년 7월 Renesas Timing Product Business 인수로 550개 이상의 clock 제품을 추가했다. 현재 투자논지는 **quartz 중심의 파편화된 timing 시장이 semiconductor MEMS 기반 full-stack timing으로 이동하는가, 그리고 SiTime이 그 전환의 사실상 표준 공급자가 될 수 있는가**다.

가장 강한 증거는 인수 전 Q2 2026 organic 매출이 $157.4M로 127% YoY 성장했고 GAAP gross margin이 63%, GAAP operating income이 $8.2M으로 흑자 전환했다는 점이다. 특히 Communications/Enterprise/Datacenter(CED)는 181% 성장했다. 이는 단순 M&A 성장이나 보조금 성장과 다르다.

반면 가장 큰 약점은 **자본배분과 가격**이다. Renesas timing 사업의 FY2025 매출은 약 $207.7M이었는데 closing-date 공정가치 기준 인수대가는 약 $4.006B였다. H1 2026 취득사업 매출은 57% 성장했고 회사는 12개월 post-close $300M 매출과 약 70% gross margin을 기대하지만, 이 거래가 실제로 두 자릿수 after-tax cash return을 만들 수 있는지는 아직 전혀 검증되지 않았다.

## 2. 기업·산업 분석

### 구조적 변화

SiTime의 논리는 'timing 부품의 quartz → semiconductor 전환'이다. AI datacenter, high-speed networking, optical modules, autonomous/physical AI, automotive와 rugged industrial systems는 온도 변화, 진동, shock, latency와 synchronization 요구가 높다. 기존 quartz가 충분했던 시스템에서 timing이 점차 성능 병목이 되면, 시스템당 timing content와 ASP가 동시에 상승할 수 있다.

회사는 FY2025 공시에서 전체 timing market을 약 $11B로 추정했다. 기술 스택은 proprietary MEMS process, analog/mixed-signal, advanced packaging/system integration, programmable architecture와 software다. 전통적인 quartz vendor와 달리 resonator와 electronics를 함께 설계하고, 전통 clock IC 업체와 달리 reference resonator까지 내부에서 통합할 수 있는 것이 핵심 차별점이다.

Aura 인수로 network synchronizer, jitter cleaner, clock generator, buffer를 확보했고 TimeFabric으로 synchronization software를 추가했다. Titan은 sixth-generation FujiMEMS 기반 standalone/bare-die resonator로, 회사는 quartz 대비 크기·전력·shock/vibration·aging의 우위를 주장한다. Renesas Timing Product Business는 이 portfolio를 대규모 clock catalogue와 10,000+ 고객으로 확장한다.

### 고객가치와 lock-in

Timing device는 시스템 BOM에서 작지만 qualification failure의 비용이 크다. SiTime 공시상 고객 design cycle은 6개월~3년, product life는 10년 이상일 수 있다. 한 번 design-in되면 재qualification friction이 생긴다. 그러나 이는 software network effect와 다르며, 동일한 application에서 quartz 또는 경쟁 analog clock solution이 충분하면 switching cost가 절대적이지 않다.

FY2025 Apple은 약 17%의 최종고객 매출을 차지했고, 상위 3 distributor가 59%였다. H1/Q2 2026 상위 3 distributor 비중은 약 66%로 올랐다. Renesas 사업의 10,000+ 고객 기반은 장기적으로 이 집중도를 낮출 수 있지만 아직 실적 증거가 필요하다.

## 3. 재무 분석

FY2025 매출은 $326.7M(+61%), gross profit $175.0M, GAAP gross margin 약 53.6%, operating loss $67.0M이었다. OCF는 $87.2M, capex $52.0M으로 기계적 OCF-capex는 $35.1M이었다.

그러나 FY2025 SBC는 $103.5M, 매출의 약 31.7%였다. 단순히 OCF-capex에서 SBC를 경제적 보상으로 차감하는 보수적 진단은 -$68.4M이다. 이는 formal owner FCF가 아니지만, non-GAAP EPS를 그대로 주주경제로 해석하면 안 된다는 경고다.

H1 2026은 매출 $271.0M(+109%), OCF $71.0M, capex $25.8M, SBC $61.8M이었다. OCF-capex는 $45.2M이지만 SBC까지 단순 차감한 진단은 -$16.6M이다. 다만 Q2 SBC/revenue는 약 19.7%로 FY2025보다 크게 개선됐고, Q2 GAAP operating margin도 약 5.2%로 플러스가 됐다. 방향은 좋아지고 있다.

### Renesas 인수 후 재무 구조

회사는 2031년 만기 0% convertible notes $1.35B를 발행했고, acquisition에 $1.5B 현금과 3.559M주를 지급했다. pro forma post-close cash는 약 $389M, note carrying value와의 차이는 약 $928M의 net-debt proxy다. Q3 non-GAAP diluted share guidance는 약 32.8M이다.

8-K/A의 preliminary purchase-price allocation은 acquired intangibles 약 $2.12B와 goodwill 약 $1.88B를 기록한다. 따라서 향후 GAAP 이익은 대규모 amortization 영향을 받고, 경제적 판단에서는 integration cash return과 per-share cash economics가 더 중요하다.

## 4. 시장·거시·수요 구조

핵심 수요는 AI infrastructure다. Q2 CED 매출은 $101.2M으로 181% YoY 성장했다. management는 inference systems, optical modules, switches, accelerators와 high-performance networking에서 timing content가 증가한다고 설명한다. 이 추세가 맞다면 SiTime은 GPU/ASIC 수량 증가뿐 아니라 **시스템당 timing content 증가**라는 두 번째 레버를 가진다.

그러나 AI capex가 telecom overbuild처럼 주기적으로 과잉투자가 될 가능성을 배제할 수 없다. SiTime 공시 역시 AI/datacenter spending의 기간을 예측할 수 없다고 명시한다. 따라서 최근 triple-digit CED 성장률을 장기 normalized growth로 외삽하지 않는다.

## 5. 경영진·자본배분

Rajesh Vashist 경영진은 2010년 전후부터 commodity timing을 `Precision Timing`이라는 고부가 범주로 재정의하는 전략을 밀어왔다. 기술·R&D·제품 확장 성과는 높게 평가한다. Q1/Q2 2026에서 과거 장기 목표였던 25%-30% 성장, 65% gross margin, 30% non-GAAP operating margin을 이미 상회했다.

그러나 $4.0B Renesas 거래는 평가를 어렵게 만든다. 전략적 적합성은 매우 높다. SiTime에 부족했던 clock catalogue와 고객 기반을 단번에 얻고 cross-sell이 가능하다. 하지만 FY2025 취득사업 매출 대비 약 19x trailing sales라는 가격은 **좋은 자산을 샀는가보다 너무 비싸게 샀는가**가 더 중요한 질문이 되게 한다. 이 거래의 3~5년 cash return이 경영진 점수를 결정할 것이다.

## 6. 가치평가·결론

2026-09-14 종가 $567.68, Q3 diluted-share guide 32.8M을 적용하면 diluted equity value는 약 $18.6B이다. post-close net-debt proxy를 더한 EV는 약 $19.5B다. Q3 revenue guide midpoint $290M을 단순 연율화한 $1.16B 대비 EV는 약 16.9x다.

10년 reverse-expectations model에서 owner-cash margin이 18%에서 28%로 성숙하고 terminal 25x를 적용하면 현재 가격은 약 17.4% 10-year revenue CAGR을 요구한다. 더 보수적으로 15%→25% margin, terminal 22x면 약 20.2% CAGR이 필요하다. 즉 현재 가격은 실패를 가격에 거의 넣지 않은 수준은 아니지만, **매우 장기간의 category-winner 실행**을 요구한다.

시나리오 값은 Bear 약 $142, Base 약 $604, Bull 약 $1,411이다. Base는 5년간 24%, 이후 5년 14% 성장과 장기 owner margin 27%를 가정한다. 현재가는 Base 부근이어서 큰 expectation gap은 없다. 반면 기술적 표준화와 full-stack cross-sell이 성공하면 Bull upside는 크다. 그래서 valuation 6/15, power-law 8/10으로 본다.

## 혁신기업 초기형 렌즈

**종합 8.5/10 — STRONG EARLY INNOVATOR PATTERN. 가장 가까운 것은 초기 NVIDIA다.**

초기 NVIDIA와의 유사성은 단순히 AI 수혜주라는 점이 아니다. 과거 NVIDIA가 graphics processor를 programmable architecture와 platform으로 격상시키며 OEM의 성능 기준을 바꿨듯, SiTime도 commodity timing을 programmable semiconductor timing으로 바꾸고 전체 clock tree에서 더 많은 system value를 가져오려 한다. 제품 성능이 올라갈수록 시스템당 content가 증가하고, 한 underlying technology를 여러 end market으로 확장한다는 점도 유사하다. 다만 SiTime에는 CUDA와 같은 developer ecosystem/network effect가 없다.

Amazon형 특성은 장기 category control을 위해 adjacency에 과감히 재투자한다는 점에서 강하다. 그러나 Renesas 거래의 가격은 Amazon식 '투자하되 수익률을 검증한다'는 기준에서 아직 미결이다.

Tesla형은 legacy physical technology(quartz)를 새로운 architecture(MEMS silicon)로 치환하고 시스템 integration을 강화한다는 측면에서 중간 이상이다. Palantir형은 mission-critical design-in, 높은 기술 embeddedness, 높은 초기 SBC 면에서 일부 닮았으나 software system-of-action은 아니다. Google형 network/data flywheel은 거의 없다.

따라서 `초기 혁신기업처럼 보이는가?`에 대한 답은 **예, 상당히 강하게 보인다. 특히 NVIDIA형 인프라 category disruption의 특징이 있다.** 그러나 `그 결과가 NVIDIA처럼 될 확률이 높은가?`는 별개의 질문이며, 현재 valuation과 M&A 가격 때문에 투자 매력은 그보다 낮다.

## 최종 점수

- Structural change & leadership: **15/15**
- Customer value & product: **9/10**
- Moat trajectory: **13/15**
- Incremental ROIC & FCF/share: **9/15**
- Management & capital allocation: **7/10**
- Financial survivability: **8/10**
- Expectation gap & valuation: **6/15**
- Power-law & asymmetry: **8/10**
- **Total: 75/100 — Emerging Outlier**

## 무엇이 점수를 높이는가

Renesas clock 제품과 SiTime MEMS/resonator의 양방향 cross-sell이 실제 매출로 확인되고, post-deal gross margin이 65% 이상 유지되며, SBC/revenue가 12% 이하 방향으로 내려가고 owner FCF/share가 20% 이상 성장해야 한다. Titan의 대형 SoC/MCU embedded design wins가 구체적인 production revenue로 나타나면 moat와 power-law 점수를 올릴 수 있다.

## 무엇이 논지를 깨는가

organic growth가 AI capex가 건강한 상태에서도 두 분기 연속 20% 아래로 내려가거나, Renesas 사업이 $300M 12-month revenue 목표를 의미 있게 넘지 못하고 cash return이 낮거나, Titan/TimeFabric이 기술홍보를 넘어 수익화되지 않거나, SBC가 15% 이상에 고착되면서 희석주식수가 지속적으로 5% 이상 증가하면 논지는 크게 약화된다.

**현재 행동 라벨은 WATCH다.** 품질 때문에 P1 우선순위로 계속 추적하지만, 현재 가격에서 신규 매수승인을 만들 정도의 expectation gap은 확인되지 않았다.

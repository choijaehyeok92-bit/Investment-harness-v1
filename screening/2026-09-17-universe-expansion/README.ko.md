# 유니버스 확장 — 검색 기반 신규 후보 38종목

- 생성 2026-09-17 · 기존 registry 96종목(US 53 / KR 43)과 **중복 없음**
- 신규: **US 18 · KR 20**
- 산출물: `candidates.jsonl`, `manifest.json`
- **점수 없음 · 매수 승인 없음 · registry 미갱신.** 리드 제너레이션 단계다.

## 왜 SCREEN_IN 판정이 없는가

8개 점수 도메인 중 어느 것도 정식 평가되지 않았고, 기대차·비대칭은 산출하지 않았다.
`harness.py` 기준 `coverage_weight = 0` → `INCOMPLETE`.
따라서 전 종목 `PENDING_EVIDENCE`이며, **직전 스크린(2026-09-17-outlier-gap-screen)의 SCREEN_IN 9종목과 같은 층위가 아니다.**

증거 계층은 전부 **4-5(언론·2차 스크리너)**다. 1차 공시 확인은 수행하지 않았다.

## 미국 18

| 티커 | 기업 | 테마 | 우선순위 | 코드검증 | 사전 veto 플래그 |
|---|---|---|:--:|:--:|---|
| `CDNS` | Cadence Design Systems | EDA | **P1** | ✅ | — |
| `SNPS` | Synopsys | EDA + IP | **P1** | ✅ | — |
| `TER` | Teradyne | semiconductor test + robotics | **P1** | ✅ | — |
| `BKNG` | Booking Holdings | travel marketplace | **P2** | ✅ | — |
| `EQIX` | Equinix | interconnection REIT | **P2** | ✅ | external_capital_dependence, persistent_dilution |
| `FTNT` | Fortinet | network security | **P2** | ✅ | — |
| `GMED` | Globus Medical | surgical robotics | **P2** | ✅ | — |
| `MCK` | McKesson | healthcare distribution | **P2** | ✅ | — |
| `PATH` | UiPath | agentic automation | **P2** | ✅ | — |
| `ZS` | Zscaler | zero trust security | **P2** | ✅ | — |
| `ADSK` | Autodesk | design software | **P3** | ✅ | — |
| `AEP` | American Electric Power | regulated utility / AI power | **P3** | ✅ | — |
| `CAT` | Caterpillar | capital goods / backup power | **P3** | ✅ | — |
| `DLR` | Digital Realty | data center REIT | **P3** | ✅ | external_capital_dependence, persistent_dilution |
| `FTV` | Fortive | industrial tech | **P3** | ✅ | — |
| `MCHP` | Microchip Technology | embedded semis | **P3** | ✅ | — |
| `ROK` | Rockwell Automation | factory automation | **P3** | ✅ | — |
| `SOFI` | SoFi Technologies | digital bank | **P3** | ✅ | external_capital_dependence, persistent_dilution, low_quality_growth |

## 한국 20

| 티커 | 기업 | 테마 | 우선순위 | 코드검증 | 사전 veto 플래그 |
|---|---|---|:--:|:--:|---|
| `036930` | 주성엔지니어링 Jusung Engineering | semi equipment | **P1** | ✅ | price_requires_unrealistic_bull_case, incremental_roic_collapse |
| `240810` | 원익IPS Wonik IPS | semi equipment | **P1** | ✅ | fatal_concentration |
| `277810` | 레인보우로보틱스 Rainbow Robotics | robotics / humanoid | **P1** | ✅ | — |
| `353200` | 대덕전자 Daeduck Electronics | FC-BGA substrate | **P1** | ✅ | incremental_roic_collapse, external_capital_dependence |
| `403870` | HPSP | semi equipment | **P1** | ✅ | fatal_concentration |
| `039030` | 이오테크닉스 EO Technics | laser equipment | **P2** | ✅ | — |
| `052690` | 한전기술 KEPCO E&C | nuclear engineering | **P2** | ✅ | fatal_concentration |
| `108490` | 로보티즈 Robotis | robot actuator | **P2** | ⚠️ | — |
| `222800` | 심텍 Simmtech | semi substrate | **P2** | ✅ | incremental_roic_collapse |
| `307950` | 현대오토에버 Hyundai AutoEver | automotive software | **P2** | ⚠️ | fatal_concentration |
| `319660` | 피에스케이 PSK | semi equipment | **P2** | ✅ | — |
| `389500` | 에스비비테크 SBB Tech | robot reducer | **P2** | ✅ | — |
| `000990` | DB하이텍 DB HiTek | specialty foundry | **P3** | ✅ | — |
| `015760` | 한국전력 KEPCO | utility | **P3** | ⚠️ | fatal_concentration |
| `042670` | HD현대인프라코어 HD Hyundai Infracore | construction equipment | **P3** | ⚠️ | — |
| `046890` | 서울반도체 Seoul Semiconductor | LED | **P3** | ⚠️ | moat_shrinkage |
| `051600` | 한전KPS KEPCO KPS | power plant O&M | **P3** | ⚠️ | — |
| `064960` | SNT모티브 SNT Motiv | motor / defense | **P3** | ✅ | — |
| `084370` | 유진테크 Eugene Technology | semi equipment | **P3** | ✅ | — |
| `103590` | 일진전기 Iljin Electric | power equipment | **P3** | ⚠️ | — |

⚠️ 표시 7종목(`108490` `307950` `051600` `015760` `103590` `042670` `046890`)은 검색으로 코드가 확인되지 않았다. 사용 전 KRX 원천 확인이 필요하다.

## P1 우선조사 8종목

### `TER` Teradyne

- **구조적 변화**: AI 반도체 복잡도 상승으로 테스트 강도가 구조적으로 증가. 협동로봇 사업 별도 축.
- **해자 신호**: 테스트 플랫폼은 고객 생산라인에 고정되어 재인증 부담이 크다.
- **핵심 불확실성**: 반도체 장비 사이클 진폭이 매우 크다. 로봇 부문 수익성 미확립.

### `CDNS` Cadence Design Systems

- **구조적 변화**: 칩 설계 복잡도와 커스텀 실리콘 확산이 EDA 좌석 수요를 구조적으로 늘림.
- **해자 신호**: EDA 3사 과점 + 설계 플로우 락인 + IP 포트폴리오. 해자 궤적이 매우 뚜렷하다.
- **핵심 불확실성**: 가격이 이미 품질을 반영했을 가능성. 기대차 검증이 핵심.

### `SNPS` Synopsys

- **구조적 변화**: 동일 구조. IP 블록 재사용이 커스텀 칩 확산의 직접 수혜.
- **해자 신호**: EDA 과점 + 실리콘 IP 라이브러리.
- **핵심 불확실성**: Ansys 인수 통합 리스크와 규제 심사. 가격 기대차 미확인.

### `036930` 주성엔지니어링 Jusung Engineering

- **구조적 변화**: ALD/증착 장비의 첨단 메모리·파운드리 적용 확대.
- **해자 신호**: 장비 재인증 부담과 공정 레시피 락인.
- **핵심 불확실성**: ★ 주가는 2026년 급등(코스닥 시총 63위→4위, 보도상 +773%)했으나 실적은 역행. 가격과 증거의 괴리가 이 종목의 핵심 쟁점이다.
- **확인된 수치 (계층4-5)**:
  - 2026 1분기 매출 548.79억원 -54.6% YoY, 영업손실 -70.31억원 적자전환
  - 2026 2분기 매출 598.82억원 -24.0% YoY, 영업이익 14.23억원 -78.4% YoY
  - 2026 상반기 누계 매출 1,147.61억원, 영업손실 -56.08억원 (전년 동기 +404.83억원)
  - 주가 196,500원 (최근 거래일 기준, 2차 시세)
- **사전 veto 플래그**: price_requires_unrealistic_bull_case, incremental_roic_collapse

### `240810` 원익IPS Wonik IPS

- **구조적 변화**: 반도체 전공정 장비 국산화와 고객 투자 재개.
- **해자 신호**: 삼성 공급망 내 지위.
- **핵심 불확실성**: 단일 고객 집중도가 매우 높을 가능성 — fatal_concentration 사전점검 필요.
- **확인된 수치 (계층4-5)**:
  - 주가 112,000원 (2차 시세)
- **사전 veto 플래그**: fatal_concentration

### `403870` HPSP

- **구조적 변화**: 고압 수소 어닐링 장비 — 미세공정 필수 스텝.
- **해자 신호**: 사실상 독점에 가까운 니치 + 특허. 해자 궤적이 KR 장비주 중 가장 뚜렷하다.
- **핵심 불확실성**: 특허 만료·대체기술 진입과 단일 제품 종속.
- **확인된 수치 (계층4-5)**:
  - 주가 52,700원 (2차 시세)
- **사전 veto 플래그**: fatal_concentration

### `353200` 대덕전자 Daeduck Electronics

- **구조적 변화**: AI 서버용 FC-BGA 기판 국산화.
- **해자 신호**: 고다층 기판 수율 노하우.
- **핵심 불확실성**: 2026년에만 7,100억원 투자 집행 — 대규모 선제 증설의 회수 증거가 없다.
- **확인된 수치 (계층4-5)**:
  - 2026 1분기 매출 3,463억원 +60.8% YoY (2차)
  - 2027년 12월까지 추가 4,970억원 기판 증설 투자 발표, 5월 발표 2,130억원 합산 시 2026년 총 7,100억원 (2차)
- **사전 veto 플래그**: incremental_roic_collapse, external_capital_dependence

### `277810` 레인보우로보틱스 Rainbow Robotics

- **구조적 변화**: 협동로봇·휴머노이드의 피지컬 AI 전환.
- **해자 신호**: 삼성전자 편입으로 자본·유통 접근이 크게 개선.
- **핵심 불확실성**: 매출 규모가 아직 작고 수익성 미확립. 삼성 편입 후 소수주주 이해상충 점검 필요.
- **확인된 수치 (계층4-5)**:
  - 2025년 3월 삼성전자가 인수 (2차)
  - 매출 전년 대비 약 2배 증가 보도 (2차, 기간 불명확)


## 가장 중요한 발견 — 주성엔지니어링

`036930`은 2026년 코스닥 시가총액 63위에서 **4위**로 급등했고 보도상 주가 상승률이 **+773%**다.
그런데 같은 기간 실적은 반대 방향이다.

| 기간 | 매출 | YoY | 영업이익 |
|---|--:|--:|--:|
| 2026 1Q | 548.79억원 | **-54.6%** | **-70.31억원** (적자전환) |
| 2026 2Q | 598.82억원 | **-24.0%** | 14.23억원 (-78.4%) |
| 2026 상반기 | 1,147.61억원 | — | **-56.08억원** (전년 +404.83억원) |

전략 원칙5는 "가격이 아니라 증거에 반응한다"이고, 원칙2는 "좋은 기업이 아니라 기대차를 산다"이다.
주가가 8배 오르는 동안 영업이익이 흑자에서 적자로 돌아섰다면, 현재가에 내재된 기대는 현재 증거와 크게 괴리돼 있다.

`price_requires_unrealistic_bull_case`와 `incremental_roic_collapse`를 사전 플래그로 기록한다.
단 **역산 DCF 없이 SCREEN_OUT으로 확정하지 않는다** — 장비주의 수주-매출 인식 시차가 크고,
`agents/screener.md`는 단기 실적 부진·적자만으로 탈락시키는 것을 금지한다.

## 금지된 지름길 준수

고PER·저PER·주가상승·단기EPS·적자 단독 판정 없음.
주성엔지니어링도 **적자를 사유로 탈락시키지 않았다** — 플래그 사유는 가격과 증거의 괴리(원칙2·5)다.

## 다음 단계

1. P1 8종목의 **1차 공시 수집** (사업보고서/10-K, 분기보고서/10-Q)
2. 주당 오너현금 산출 → 역산 DCF → Bear/Base/Bull
3. Hard Veto 9종 정식 판정
4. `coverage_weight` 100 달성 후 직전 스크린과 동일 기준으로 재랭킹
5. 통과 종목만 `registry/companies.json` 편입 — **현 단계에서는 편입하지 않았다**

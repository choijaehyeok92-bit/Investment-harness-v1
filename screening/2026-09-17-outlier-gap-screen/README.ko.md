# Outlier Expectation Gap Screen — US 20 / KR 20

- 기준일 **2026-09-15** · 생성 2026-09-17
- 기준: `outlier-expectation-gap-harness/config/strategy.json` (Long Outlier Expectation Gap Strategy v2.0)
- 산출물: `screen-results.jsonl`, `manifest.json`
- **매수 승인 없음. latest 포인터 승격 없음. 심층조사 우선순위 판정이다.**

## 기준 매핑

outlier 하네스의 8개 점수 도메인과 가중치가 Investment-harness-v1의 8개 카테고리와 정확히 1:1 대응한다.

| outlier 도메인 | 가중 | Investment-harness-v1 카테고리 |
|---|--:|---|
| structural_leadership | 15 | structural_change_and_leadership |
| customer_product | 10 | customer_value_and_product |
| moat_trajectory | 15 | moat_trajectory |
| reinvestment_fcf | 15 | incremental_roic_and_fcf_per_share |
| management_allocation | 10 | management_and_capital_allocation |
| financial_survival | 10 | financial_survivability |
| expectation_valuation | 15 | expectation_gap_and_valuation |
| asymmetry | 10 | power_law_and_asymmetry |

따라서 기존 심사 점수를 재계산 없이 그대로 사용했다.

## 스크린 규칙

```
SCREEN_OUT  ← Bull 가치 < 현재가
            | 비대칭 < 0.5          (원칙4 Power Law/Asymmetry 위반)
            | 총점 < 60 AND Base 상승여력 < 0

SCREEN_IN   ← 총점 >= 70 AND Base 상승여력 > 0 AND 비대칭 >= 1.5  (동시 충족)

WATCH       ← 나머지
INCOMPLETE  ← coverage_weight < 100 (기대차·비대칭 미평가)
```

- 비대칭 = (Bull − 현재가) / (현재가 − Bear)
- 우선순위 지표 = 품질(총점/100) × 기대차(1+Base상승) × 비대칭(min(asym,6)/2) × veto감쇄(1−0.05×미해소veto)
  - **순위 정렬용이며 점수도 매수근거도 아니다.**

### 금지된 지름길 준수 (`agents/screener.md`)

고PER 단독 탈락 없음 · 저PER 단독 통과 없음 · 주가 상승 단독 탈락 없음 · 단기 EPS 부진 단독 탈락 없음 · **적자 단독 탈락 없음** (ASTS·TEM·RKLB를 적자를 사유로 탈락시키지 않았다).

## 미국 20

| # | 티커 | 기업 | 총점 | Base 상승 | Bull | Bear | 비대칭 | 미해소veto | 우선순위 | 판정 |
|--:|---|---|--:|--:|--:|--:|--:|--:|--:|---|
| 1 | `MELI` | MercadoLibre, Inc. | 82 | +51.5% | +353.6% | -72% | 4.89 | 3 | 2.580 | **SCREEN_IN** |
| 2 | `TMDX` | TransMedics Group, Inc. | 74 | +34.4% | +341.4% | -79% | 4.32 | 4 | 1.718 | **SCREEN_IN** |
| 3 | `NOW` | ServiceNow, Inc. | 73 | +42.0% | +209.2% | -56% | 3.74 | 4 | 1.552 | **SCREEN_IN** |
| 4 | `AVGO` | Broadcom | 81 | +9.0% | +149.6% | -63% | 2.38 | 5 | 0.787 | **SCREEN_IN** |
| 5 | `NVDA` | NVIDIA | 79 | +1.1% | +154.7% | -69% | 2.25 | 4 | 0.720 | **SCREEN_IN** |
| 6 | `META` | Meta Platforms, Inc. | 75 | +3.2% | +102.5% | -66% | 1.54 | 3 | 0.507 | **SCREEN_IN** |
| 7 | `ASTS` | AST SpaceMobile | 54 | +64.1% | +540.2% | -100% | 5.40 | 6 | 1.676 | **WATCH** |
| 8 | `CRDO` | Credo Technology Group Holding Ltd | 73 | -2.9% | +274.9% | -84% | 3.27 | 4 | 0.926 | **WATCH** |
| 9 | `MSFT` | Microsoft | 78 | -7.4% | +104.5% | -70% | 1.49 | 2 | 0.483 | **WATCH** |
| 10 | `VRT` | Vertiv | 69 | -14.3% | +145.2% | -79% | 1.83 | 3 | 0.459 | **WATCH** |
| 11 | `ANET` | Arista Networks | 79 | -16.8% | +79.4% | -71% | 1.11 | 2 | 0.329 | **WATCH** |
| 12 | `APP` | AppLovin Corporation | 76 | -2.2% | +44.8% | -47% | 0.96 | 3 | 0.304 | **WATCH** |
| 13 | `ISRG` | Intuitive Surgical | 79 | -18.0% | +65.0% | -66% | 0.98 | 2 | 0.286 | **WATCH** |
| 14 | `PLTR` | Palantir Technologies Inc. | 72 | -31.4% | +112.9% | -84% | 1.35 | 4 | 0.266 | **WATCH** |
| 15 | `GOOGL` | Alphabet | 70 | -22.9% | +77.8% | -77% | 1.01 | 4 | 0.217 | **WATCH** |
| 16 | `LLY` | Eli Lilly | 69 | -31.3% | +82.9% | -83% | 1.00 | 3 | 0.202 | **WATCH** |
| 17 | `PWR` | Quanta Services, Inc. | 68 | -26.3% | +68.2% | -82% | 0.83 | 2 | 0.188 | **WATCH** |
| 18 | `TSM` | Taiwan Semiconductor Manufacturing Company (ADR) | 75 | -28.5% | +62.1% | -78% | 0.80 | 3 | 0.182 | **WATCH** |
| 19 | `AXON` | Axon Enterprise | 64 | -32.9% | +92.0% | -88% | 1.05 | 4 | 0.181 | **WATCH** |
| 20 | `DDOG` | Datadog | 69 | -37.1% | +89.6% | -87% | 1.02 | 4 | 0.178 | **WATCH** |

## 한국 20

| # | 티커 | 기업 | 총점 | Base 상승 | Bull | Bear | 비대칭 | 미해소veto | 우선순위 | 판정 |
|--:|---|---|--:|--:|--:|--:|--:|--:|--:|---|
| 1 | `214450` | PharmaResearch | 81 | +85.3% | +350.6% | -53% | 6.59 | 3 | 3.827 | **SCREEN_IN** |
| 2 | `145020` | Hugel, Inc. | 79 | +46.5% | +171.1% | -35% | 4.85 | 4 | 2.245 | **SCREEN_IN** |
| 3 | `003230` | Samyang Foods | 80 | +32.7% | +156.7% | -54% | 2.91 | 2 | 1.392 | **SCREEN_IN** |
| 4 | `035420` | NAVER | 69 | +27.4% | +182.4% | -55% | 3.30 | 4 | 1.159 | **WATCH** |
| 5 | `278470` | APR | 68 | +15.2% | +247.5% | -78% | 3.17 | 3 | 1.056 | **WATCH** |
| 6 | `005380` | Hyundai Motor | 68 | +22.2% | +167.7% | -58% | 2.87 | 3 | 1.014 | **WATCH** |
| 7 | `267260` | HD Hyundai Electric | 76 | -12.8% | +117.1% | -72% | 1.62 | 3 | 0.455 | **WATCH** |
| 8 | `012450` | Hanwha Aerospace | 67 | -2.8% | +125.1% | -72% | 1.73 | 5 | 0.423 | **WATCH** |
| 9 | `005930` | Samsung Electronics | 68 | -23.6% | +118.8% | -76% | 1.56 | 3 | 0.344 | **WATCH** |
| 10 | `058470` | LEENO Industrial | 76 | -10.6% | +66.8% | -68% | 0.98 | 3 | 0.284 | **WATCH** |
| 11 | `207940` | Samsung Biologics | 68 | -18.1% | +69.5% | -73% | 0.95 | 4 | 0.211 | **WATCH** |
| 12 | `196170` | Alteogen | 61 | -48.7% | +107.8% | -96% | 1.12 | 4 | 0.140 | **WATCH** |
| 13 | `000660` | SK Hynix | 68 | -44.8% | +60.8% | -86% | 0.71 | 3 | 0.113 | **WATCH** |
| 14 | `042700` | Hanmi Semiconductor | 63 | -62.0% | +19.5% | -91% | 0.21 | 4 | 0.022 | **SCREEN_OUT** |
| 15 | `034020` | Doosan Enerbility | 49 | -83.1% | -41.3% | -100% | -0.41 | 4 | 0.008 | **SCREEN_OUT** |
| 16 | `010120` | LS ELECTRIC | (62/75) | — | — | — | — | 3 | — | **INCOMPLETE** |
| 17 | `259960` | Krafton | (62/75) | — | — | — | — | 3 | — | **INCOMPLETE** |
| 18 | `009150` | Samsung Electro-Mechanics | (58/75) | — | — | — | — | 3 | — | **INCOMPLETE** |
| 19 | `068270` | Celltrion | (58/75) | — | — | — | — | 3 | — | **INCOMPLETE** |
| 20 | `257720` | SILICON2 | (58/75) | — | — | — | — | 4 | — | **INCOMPLETE** |

Tier B 5종목(`010120` `259960` `009150` `068270` `257720`)은 6개 카테고리(가중 75)만 평가되어
기대차·비대칭 도메인이 `unknown`이다. coverage_weight 75 < 100이므로 100점 환산과 SCREEN_IN 판정이 불가하며,
`INCOMPLETE`는 부정 판정이 아니라 **미완료** 상태다.

## Hard Veto 상태

Tier A 43종목 **전부** `hard_veto = INVESTIGATE`(미해소)다.
outlier 하네스 기계 판정상 미해소 veto는 최대 `WATCH` · 비중 `0% until veto cleared`로 제한된다.
따라서 **SCREEN_IN 9종목도 매수 대상이 아니라 심층조사 우선순위**다.

## 한계

- 신규 종목 발굴이 아니라 기존 심사 유니버스(US 53 / KR 43) 재선별이다.
- 가격·점수 모두 2026-09-12 스냅샷 기준이며 2026-09-15~17 변동은 반영하지 않았다.
- 가격은 금융 시세 피드(장외시간 포함 가능)이며 거래소 원천 감사 자료가 아니다.
- 실제 포트폴리오 비중·위험예산이 제공되지 않아 포지션 사이징을 수행하지 않았다.

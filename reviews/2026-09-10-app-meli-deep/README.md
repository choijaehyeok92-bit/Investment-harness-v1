# 2026-09-10 APP + MELI Deep Research Checkpoints

이 실행은 두 작업을 함께 저장한다.

1. 2026-09-10에 완료한 **APP(AppLovin) 심층분석 결과 반영**
2. 하네스 규칙에 따른 **MELI(MercadoLibre) 신규 심층분석 및 현재 가격 기준 valuation 재평가**

## 결과 요약

| Ticker | Decision | Priority | Quality /75 | Total /100 | Buy | Main open vetoes |
|---|---|---|---:|---:|---|---|
| APP | WATCH | P1 | 60 | 76 | false | management/conduct integrity, fatal concentration, permanent loss |
| MELI | WATCH | P1 | 63 | 82 | false | low-quality growth, incremental ROIC, permanent loss |

## APP

APP는 Q2 2026의 50%대 매출성장, 70%대 GAAP operating margin, 강한 FCF와 순주식수 감소로 사업품질이 높다. $305.06 reference price에서 9% reverse DCF는 보수적 FCF-minus-SBC starting proxy 기준 약 11.1%의 5년 성장을 요구해 `price_requires_unrealistic_bull_case`는 PASS로 평가한다.

그러나 SEC investigation이 unresolved이고, Axon/mobile platform 집중 및 founder voting control이 남아 있다. 또한 2025~H1 2026 대규모 buyback은 현재 reference price보다 훨씬 높은 수준에서 집행되어 repurchase-price discipline에 감점했다. 따라서 76점이 Hard Veto를 덮어쓰지 않으며 WATCH를 유지한다.

## MELI

MELI는 Q2 2026 revenue +49.8%, GMV +44% reported, TPV +56%로 구조적 성장과 ecosystem engagement가 매우 강하다. Independent e-commerce research도 지역 리더십을 지지한다. 반면 Q2 operating income은 -17.3%, operating margin 6.7%, H1 provision for doubtful accounts는 $2.520B, H1 adjusted FCF는 $158M으로 전년 $512M보다 낮다.

Credit portfolio는 $16B를 넘어 +75% YoY이고 card NIMAL은 -2.5%이므로, credit/free-shipping reinvestment가 9% hurdle 이상의 after-loss/after-required-capital cash ROIC를 만드는지가 핵심이다. 2026-09-09 $1,876.33 reference close에서 기존 owner-cash model의 reverse required growth는 약 9.56%이며 retained scenarios는 Bear ~$524 / Base ~$2,875 / Bull ~$8,607 per share다. 범위가 넓기 때문에 Base upside를 buy signal로 사용하지 않는다.

## 저장 파일

- `source-manifest.json`
- `companies/APP/analyses/2026-09-10-deep/assessment.json`
- `companies/APP/analyses/2026-09-10-deep/valuation.json`
- `companies/APP/analyses/2026-09-10-deep/evidence-ledger.json`
- `companies/APP/analyses/2026-09-10-deep/thesis.ko.md`
- `companies/MELI/analyses/2026-09-10-deep/assessment.json`
- `companies/MELI/analyses/2026-09-10-deep/valuation.json`
- `companies/MELI/analyses/2026-09-10-deep/evidence-ledger.json`
- `companies/MELI/analyses/2026-09-10-deep/thesis.ko.md`
- `README.md`

## Authority / reproducibility guardrail

현재 하네스 validator는 `reviews/latest.json -> registry/companies.json -> companies/<ticker>/latest.json`의 단일 authority와 baseline-locked canonical raw set, 그리고 frozen deep outputs의 재현성을 함께 검증한다. 개별 종목만 `latest.json` 또는 registry를 갱신하면 frozen authority run과 불일치할 수 있다.

따라서 이번 변경은 **additive-only research checkpoint**로 병합한다. 다음 파일은 변경하지 않는다.

- `companies/APP/latest.json`
- `companies/MELI/latest.json`
- `registry/companies.json`
- `reviews/latest.json`
- `companies/*/raw-data/*`
- `harness/baseline-lock.json`
- deterministic / frozen current-run outputs

즉 두 심층분석은 main에 저장된 최신 연구 체크포인트이지만, canonical current authority를 조용히 교체하지 않는다. 향후 전체 reviewed authority run을 재생성하고 validators를 통과할 때 latest/registry promotion을 함께 수행한다.

## Policy consistency

- Macro/theme overlays do not directly change company scores.
- Hard Veto overrides numeric score.
- Credit-company cash must distinguish customer funds/restricted cash from surplus owner cash.
- SBC cost and dilution are not double-counted in the same valuation model.
- Price decline alone is not a buy signal; price increase alone is not a sell signal.
- Unknown evidence remains INVESTIGATE rather than being converted to FAIL or guessed precision.

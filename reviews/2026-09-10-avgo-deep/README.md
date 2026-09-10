# AVGO 2026-09-10 심층분석 체크포인트

Broadcom (AVGO)을 Investment Harness v1.1의 `business quality → hard veto → reverse expectations → Bear/Base/Bull → red team → portfolio monitor` 순서로 재평가했다.

이 디렉터리는 **additive-only research checkpoint**다. `companies/AVGO/latest.json`, `registry/companies.json`, `reviews/latest.json`, canonical raw-data, `harness/baseline-lock.json` 또는 frozen deterministic outputs를 수정하지 않는다. 현재 canonical authority는 별도 reviewed promotion 전까지 `companies/AVGO/analyses/2026-09-06-deep/assessment.json`이다.

## 결론

- Decision: **WATCH**
- Priority: **P1**
- Buy authorized: **false**
- Business quality: **65/75**
- Total score: **81/100 — Emerging Outlier**
- Price reference: **$364.38, 2026-09-09 close**
- Retained Bear / Base / Bull: **$134.01 / $394.69 / $903.67**
- Base/price: **1.083x**
- Reverse required growth: **약 12.08%/yr, years 2-10 at 9% hurdle under retained base economics**

## 핵심 변화

Q3 FY2026 매출은 $29.591B(+86% YoY), AI semiconductor revenue는 $16.7B(+221%), Infrastructure Software는 $8.752B(+29%), reported FCF는 $13.665B였다. Q4 AI semiconductor revenue guide는 약 $21.7B다.

Q4 FY2025~Q3 FY2026 TTM은 매출 약 $89.104B, GAAP 순이익 $38.265B, company-defined FCF $39.403B다. TTM SBC 약 $8.484B를 한 번 차감한 보수적 owner-cash diagnostic은 $30.919B다. 이 진단값은 customer financing, working capital, acquisition economics까지 완전히 정상화한 owner earnings는 아니다.

사업품질은 기존 61/75에서 65/75로 상승했다. AI custom silicon과 networking의 성장 가시성, VMware software growth, 현금창출이 강화됐다. 그러나 점수 상승이 Hard Veto를 덮지 않는다.

## 새로 중요해진 위험

가장 중요한 변화는 AI 수요와 financing이 일부 결합하기 시작했다는 점이다. Broadcom은 2026년 6월 특정 AI rack 구매/lease 구조에 투자 파트너를 주선하고 고객 lease 의무에 대해 최대 $29B의 5년 backstop을 제공했다. 이를 현재 부채나 확정 손실로 처리하지 않지만, AI demand quality와 incremental ROIC 검증에 포함한다.

Q2 10-Q 기준 한 semiconductor distributor가 매출의 42%, top five end customers가 약 45%를 차지했다. 동시에 Marvell-Google, Qualcomm-Amazon custom-silicon 계약은 hyperscaler design share가 contestable하다는 직접 증거다.

VMware는 Q3 +29% 성장하며 두 번째 cash engine으로 기능하지만 유럽 cloud/business 단체들은 pricing/licensing/access 정책을 문제 삼아 EU interim measures를 요구했다. Broadcom은 이를 반박하고 있다.

## Hard Veto

PASS: management/accounting integrity, external capital dependence, persistent dilution, price requires unrealistic bull case.

INVESTIGATE: **low_quality_growth, incremental_roic_collapse, moat_shrinkage, fatal_concentration, permanent_loss_probability**.

따라서 score 81에도 불구하고 buy authorization은 false다.

## 가치평가 해석

9월 9일 $364.38과 4.758B valuation shares 기준 equity value는 약 $1.734T다. 이는 TTM reported FCF의 약 44.0배, conservative FCF-minus-SBC diagnostic의 약 56.1배다.

기존 Bear/Base/Bull 장기모형은 새 Q3 실적 하나만으로 terminal economics를 임의 재작성하지 않고 그대로 유지했다. 대신 현재 가격을 동기화해 reverse expectations를 재계산했다. 9% hurdle에서 years 2-10 요구 성장률은 약 12.08%다. 이는 현재 AI trajectory에 비춰 unrealistic bull case는 아니지만, Base 대비 약 8% 할인은 open veto들을 보상할 충분한 margin of safety도 아니다.

Management가 제시한 FY2027 AI semiconductor revenue 약 $115B, FY2028 약 $230B는 upside evidence이지만 forecast다. Base 가치에 관측 사실처럼 기계적으로 삽입하지 않았다.

## 증액 조건

가격 하락만으로 증액하지 않는다. AI rack backstop/financing이 제한적이고 회수 가능한 구조라는 추가 공시, 경쟁사의 hyperscaler design wins에도 Broadcom accelerator/networking share 유지, VMware renewal/cash conversion 지속, net debt 하락과 SBC 이후 FCF/share 상승이 함께 확인되어야 한다. 동시에 보수적 Base 대비 약 20% 이상의 명확한 기대차 또는 이에 상응하는 owner-cash 상향이 필요하다.

## 검증 범위

이 run은 GitHub-side additive diff guardrail을 수행한다. Q3 FY2026 10-Q는 checkpoint 시점에 아직 확인 가능한 정기보고서로 사용하지 않았으므로 Q3 commitment/customer-concentration footnote 전체를 감사했다고 표현하지 않는다. 최신 상세 commitment와 concentration은 Q2 10-Q, Q3 실적은 회사 IR/8-K 수준의 공식 발표를 사용했다.

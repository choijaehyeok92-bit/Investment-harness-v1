# PANW raw extraction + preliminary review — 2026-09-08

## Scope

사용자가 제공한 Palo Alto Networks IR/SEC 링크 5개를 기준으로 원자료를 구조화하고 초벌분석 체크포인트를 작성했다.

제공 링크:

- `https://investors.paloaltonetworks.com/node/20786/html`
- `https://investors.paloaltonetworks.com/node/20781/html`
- `https://investors.paloaltonetworks.com/node/19656/html`
- `https://investors.paloaltonetworks.com/node/20771/html`
- `https://investors.paloaltonetworks.com/node/20571/html`

## Source resolution

- `node/19656`: 직접 크롤링은 403이었으나 Palo Alto Networks filing detail과 SEC accession `0001327567-25-000027`을 통해 FY2025 10-K로 동일 공시를 확인했다.
- `node/20571`: 직접 열람 가능. 2026-04-30 종료 Q3 FY2026 Form 10-Q.
- `node/20771`: 직접 node는 cache miss. 회사 SEC filing index에서 2026-09-01 Form 8-K, accession `0001327567-26-000019`, Exhibit 99.1 Q4/FY2026 earnings release를 대응 공식 공시로 확보했다. direct node mapping은 별도 검증하지 않았다.
- `node/20781`, `node/20786`: 직접 node는 cache miss. 회사 filing index에는 2026-09-03 Form 4 두 건(`0002055370-26-000007`, `0001882285-26-000022`)이 존재하며 두 건 모두 추출했다. 어느 node가 어느 accession인지는 추정하지 않았다.

## Added files

- `reviews/2026-09-08-panw-prelim/raw-data.json`
- `reviews/2026-09-08-panw-prelim/README.md`
- `companies/PANW/analyses/2026-09-08-prelim/assessment.json`
- `companies/PANW/analyses/2026-09-08-prelim/thesis.ko.md`

## Preliminary conclusion

- Decision: **WATCH**
- Priority: **P1**
- Business quality: **58/75**
- Buy authorized: **false**
- Valuation: **withheld until synchronized price + 9% reverse DCF**

핵심 긍정:

- FY2026 잠정 매출 $11.48B, 약 +24.5% YoY.
- Q4 NGS ARR $9.10B, +63%; RPO $21.2B, +34%.
- FY2026 company-defined FCF $4.113B; adjusted FCF $4.414B, 38.4% margin.
- FY2027 가이던스: 매출 $14.1–14.2B(+23~24%), NGS ARR $11.075–11.175B(+22~23%).
- 2026-07-31 잠정 cash+investments $7.906B vs long-term convertible notes $1.774B.
- FY2025 audited 10-K: unqualified financial-statement opinion and effective ICFR opinion.

핵심 리스크:

- CyberArk 인수 구매대가 $21.1B. 2026-04-30 purchase accounting에서 goodwill $14.802B + identified intangibles $6.279B.
- FY2026 잠정 goodwill+intangibles는 총자산의 약 59.9%.
- FY2026 GAAP 영업마진은 약 6.1%로 FY2025 약 13.5%에서 하락. Q3 FY2026는 -6.1%.
- FY2026 9개월 GAAP SBC $1.355B, Q3 단독 $684M. 높은 SBC와 M&A 주식발행을 분리해 주당 가치 추적 필요.
- FY2026 weighted-average diluted shares는 FY2025 대비 약 +7.8%; CyberArk 인수 주식 약 112M주 영향이 커 직원 희석과 M&A 발행을 구분해야 한다.
- FY2026 NGS ARR에는 대형 LLM 고객의 Chronosphere migration이 9자리 달러 규모 기여를 했다는 경영진 설명이 있어 headline ARR 성장률을 순수 유기적 성장으로 간주하지 않는다.

## Hard-veto checkpoint

PASS:
- management_or_accounting_integrity — FY2025 감사 근거에 한정.
- external_capital_dependence
- low_quality_growth
- fatal_concentration

INVESTIGATE:
- persistent_dilution
- incremental_roic_collapse
- moat_shrinkage
- price_requires_unrealistic_bull_case
- permanent_loss_probability

가장 중요한 현재 veto는 **incremental_roic_collapse**다. CyberArk 및 후속 M&A의 3–5년 세후 증분 현금수익률이 미국 9% hurdle을 유의하게 넘어서는지 확인해야 한다.

## Authority / reproducibility

이 변경은 **additive-only research checkpoint**다. 다음 파일은 변경하지 않는다.

- `companies/PANW/latest.json`
- current registry
- `harness/baseline-lock.json`
- canonical `companies/PANW/raw-data/`
- `reviews/latest.json`
- frozen/generated current-authority outputs

따라서 2026-09-06 PANW `PRELIMINARY_REVIEW`는 별도 canonical harness run이 승격하기 전까지 current authority로 유지된다.

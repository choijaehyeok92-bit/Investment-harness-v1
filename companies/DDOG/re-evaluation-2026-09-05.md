# 데이터독 (DDOG) — 2026-09-05 재평가

판정 **WATCH**, 점수 **68/100**, Hard Veto **INVESTIGATE**, 신규 포지션 **NONE**.

관측·보안 플랫폼의 성장과 충분한 현금은 인정한다. 다만 TTM SBC가 보고 FCF의 약 79%이므로 보고 FCF 마진을 그대로 높은 재투자 품질로 해석했던 점수를 10→8로 조정한다.

## 근거와 반대근거

첨부 공시의 TTM 매출 약 39.67억 달러, 보고 FCF 약 10.73억 달러와 순현금은 생존성 및 제품 확장을 지지한다.

TTM SBC 약 8.51억 달러, 연간 기본주식수 증가 약 2.97%. 보고 FCF-보상비용 프록시는 약 2.22억 달러다. 이 차액은 정확한 경제적 SBC 공정가치 측정이 아니라 민감도 지표다.

사실은 원문/공시에서 온 관측값, 미래 성장·마진·손실 범위는 추정, 인과관계는 추론, 점수와 판정은 의견이다. 숫자 모델은 확률 예측이나 목표주가가 아니다.

## 동일 100점 체계

| 항목 | 재평가 | 배점 | 근거·한계 |
|---|---:|---:|---|
| structural_change_and_leadership | 14 | 15 | 기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조. |
| customer_value_and_product | 9 | 10 | 기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조. |
| moat_trajectory | 12 | 15 | 기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조. |
| incremental_roic_and_fcf_per_share | 8 | 15 | GAAP 영업이익률 약 0.4%와 SBC/보고 FCF 약 79%를 반영: 10→8. |
| management_and_capital_allocation | 7 | 10 | 기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조. |
| financial_survivability | 10 | 10 | 기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조. |
| expectation_gap_and_valuation | 4 | 15 | 기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조. |
| power_law_and_asymmetry | 4 | 10 | 기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조. |

[현재 8개 항목의 근거·반대근거·신뢰도](../../reviews/2026-09-05-astra/company-reassessments.jsonl). 50점 스크리닝과 합산·비례 환산하지 않는다.

## Hard Veto

| 항목 | 상태 | 해소 조건 |
|---|---|---|
| management_or_accounting_integrity | PASS | 현재 중대한 반증 미확인; 다음 공시에서 계속 점검 |
| external_capital_dependence | PASS | 현재 중대한 반증 미확인; 다음 공시에서 계속 점검 |
| persistent_dilution | INVESTIGATE | Establish a sustained path to SBC below 15% of revenue and annual net dilution at or below 1.5%, while diluted FCF per share grows faster than revenue. |
| low_quality_growth | PASS | 현재 중대한 반증 미확인; 다음 공시에서 계속 점검 |
| incremental_roic_collapse | INVESTIGATE | Confirm sustained GAAP operating leverage, stable or improving gross margin and diluted owner FCF per share growth after the economic cost of SBC. |
| moat_shrinkage | INVESTIGATE | Observe normalized retention, usage and competitive win rates after the largest-customer reduction for at least two quarters. |
| price_requires_unrealistic_bull_case | INVESTIGATE | Require either a price at least 20% below refreshed Base value or evidence strong enough to reduce the implied ten-year revenue CAGR below 18% without aggressive dilution or margin assumptions. |
| fatal_concentration | INVESTIGATE | Disclose or demonstrate the largest customer's normalized revenue contribution and show that diversified customer growth offsets the reduction without material retention or margin damage. |
| permanent_loss_probability | PASS | 현재 중대한 반증 미확인; 다음 공시에서 계속 점검 |

## 가격과 시나리오

기준 가격 **213.81** (USD)는 기존 분석 가격이다. 실시간 또는 동일 일자 종가 비교가 아니다. 원래 시각은 [가치평가 기록](valuation.json)의 legacy 필드 참조.

동일 9% 허들·3% 회사 말기 FCF 성장률의 **방법론 진단**이다. 비상장투자 제외, 무상 환매효과 제거, 말기 양의 희석 반영으로 과거 모형과 달라진다. 보상비용/환매 재원이 완성된 owner-FCFE 가치는 아니다.

| 시나리오 | 진단 PV/주 (USD) | 기준가 대비 |
|---|---:|---:|
| bear | 71.61 | -66.5% |
| base | 152.09 | -28.9% |
| bull | 275.64 | +28.9% |

현재 핵심 모델 한계: 큰 AI 고객의 최적화 영향을 분리한 성장, 총발행·환매 주식수와 주당 owner-FCF를 4개 분기 추적한다.

## 영구손실과 반증

하이퍼스케일러·오픈소스 대체, 특정 AI 고객 축소와 희석이 겹치면 사업이 생존해도 주당 가치의 회복이 장기간 막힌다.

**논지 반증:** 대형고객 최적화 이후에도 매출 성장·다중제품 채택이 지속 둔화하고 SBC 이후 FCF/주가 2년 정체한다.

**증액 전 필요한 증거:** 큰 AI 고객의 최적화 영향을 분리한 성장, 총발행·환매 주식수와 주당 owner-FCF를 4개 분기 추적한다. 사업 개선과 가격 기대차를 함께 확인해야 하며 가격 하락만으로 매수하지 않는다.

**축소·매도 재검토:** 논지 반증이 지속되거나 경영진·회계 신뢰가 중대하게 훼손되는 경우. 실제 보유 여부를 확인하지 않았으므로 이는 조건부 모니터링 규칙이며 거래 지시가 아니다.

## 출처·완료 범위

[evidence.jsonl](evidence.jsonl), [출처 감사](../../reviews/2026-09-05-astra/source-audit.md), [전체 비교](../../reviews/2026-09-05-astra/README.md).

재심사 판단 신뢰도 70%. 종목 재평가 기록은 완료했지만 열린 가치평가·증거 게이트까지 해소됐다는 뜻은 아니다. 원문 전체 재실사·실시간 시세 갱신·거래 실행은 하지 않았다.

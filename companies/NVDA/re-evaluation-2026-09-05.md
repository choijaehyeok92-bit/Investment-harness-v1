# 엔비디아 (NVDA) — 2026-09-05 재평가

판정 **WATCH**, 점수 **73/100**, Hard Veto **INVESTIGATE**, 신규 포지션 **NONE**.

서로 다른 76점 WATCH와 75점 STARTER를 하나의 판정으로 복구한다. 새 점수 73, WATCH. 플랫폼 우위는 유지되지만 고객 금융지원·공급약정과 큰 기준 지분가치가 비대칭을 제한한다.

## 근거와 반대근거

공식 FY2027 Q2 매출 962.21억 달러, 영업이익 637.34억 달러. CUDA·네트워크·랙 단위 시스템은 단일 칩을 넘어선 고객 전환비용의 근거다.

첨부 Q2 10-Q의 공급·용량 약정 2,790억 달러와 8월 SB Energy 보증 최대 1,050억 달러를 분리해야 한다. 보증은 조건부·장기 노출이며 전액 즉시 손실도, 무위험도 아니다. 투자자산 평가이익을 반복 영업이익으로 자본화하지 않는다.

사실은 원문/공시에서 온 관측값, 미래 성장·마진·손실 범위는 추정, 인과관계는 추론, 점수와 판정은 의견이다. 숫자 모델은 확률 예측이나 목표주가가 아니다.

## 동일 100점 체계

| 항목 | 재평가 | 배점 | 근거·한계 |
|---|---:|---:|---|
| structural_change_and_leadership | 14 | 15 | 최종 AI 수요의 자생성과 순환성 불확실성을 반영해 만점 15→14. |
| customer_value_and_product | 9 | 10 | 기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조. |
| moat_trajectory | 14 | 15 | 기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조. |
| incremental_roic_and_fcf_per_share | 12 | 15 | Fabless라는 이유로 공급·클라우드 약정/고객지원에 투입된 자본을 제외할 수 없음: 13→12. |
| management_and_capital_allocation | 6 | 10 | 기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조. |
| financial_survivability | 8 | 10 | 기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조. |
| expectation_gap_and_valuation | 6 | 15 | 기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조. |
| power_law_and_asymmetry | 4 | 10 | 크게 성장한 지분가치와 서로 연동된 꼬리손실을 반영: 5→4. |

[현재 8개 항목의 근거·반대근거·신뢰도](../../reviews/2026-09-05-astra/company-reassessments.jsonl). 50점 스크리닝과 합산·비례 환산하지 않는다.

## Hard Veto

| 항목 | 상태 | 해소 조건 |
|---|---|---|
| management_or_accounting_integrity | PASS | 현재 중대한 반증 미확인; 다음 공시에서 계속 점검 |
| external_capital_dependence | PASS | 현재 중대한 반증 미확인; 다음 공시에서 계속 점검 |
| persistent_dilution | PASS | 현재 중대한 반증 미확인; 다음 공시에서 계속 점검 |
| low_quality_growth | INVESTIGATE | 공급·클라우드 약정 만기/취소권, 보증 발동·회수 조건과 투자관계 고객 매출을 대조하고 고객 최종 현금창출로 수요를 검증한다. |
| incremental_roic_collapse | INVESTIGATE | Rubin 전환 이후 공급약정 대비 매출·총이익·현금회수, 재고충당금, 파트너 투자수익을 코호트로 확인한다. |
| moat_shrinkage | PASS | 현재 중대한 반증 미확인; 다음 공시에서 계속 점검 |
| price_requires_unrealistic_bull_case | PASS | 현재 중대한 반증 미확인; 다음 공시에서 계속 점검 |
| fatal_concentration | INVESTIGATE | 공급·클라우드 약정 만기/취소권, 보증 발동·회수 조건과 투자관계 고객 매출을 대조하고 고객 최종 현금창출로 수요를 검증한다. |
| permanent_loss_probability | INVESTIGATE | 공급·클라우드 약정 만기/취소권, 보증 발동·회수 조건과 투자관계 고객 매출을 대조하고 고객 최종 현금창출로 수요를 검증한다. |

## 가격과 시나리오

기준 가격 **227.23** (USD)는 기존 분석 가격이다. 실시간 또는 동일 일자 종가 비교가 아니다. 원래 시각은 [가치평가 기록](valuation.json)의 legacy 필드 참조.

동일 9% 허들·3% 회사 말기 FCF 성장률의 **방법론 진단**이다. 비상장투자 제외, 무상 환매효과 제거, 말기 양의 희석 반영으로 과거 모형과 달라진다. 보상비용/환매 재원이 완성된 owner-FCFE 가치는 아니다.

| 시나리오 | 진단 PV/주 (USD) | 기준가 대비 |
|---|---:|---:|
| bear | 117.32 | -48.4% |
| base | 219.93 | -3.2% |
| bull | 374.00 | +64.6% |

현재 핵심 모델 한계: 공급·클라우드 약정 만기/취소권, 보증 발동·회수 조건과 투자관계 고객 매출을 대조하고 고객 최종 현금창출로 수요를 검증한다.

## 영구손실과 반증

수요 감속, 재고·공급약정 손실, 투자자산 평가하락과 보증 실행이 같은 고객군에서 함께 발생한다. 이 위험을 독립 확률로 곱해 축소하지 않는다.

**논지 반증:** 고객의 자금조달 약화와 가동률 저하, 주문 취소가 동시에 발생하고 공급/보증 약정이 순현금과 정상화 FCF를 훼손한다.

**증액 전 필요한 증거:** 공급·클라우드 약정 만기/취소권, 보증 발동·회수 조건과 투자관계 고객 매출을 대조하고 고객 최종 현금창출로 수요를 검증한다. 사업 개선과 가격 기대차를 함께 확인해야 하며 가격 하락만으로 매수하지 않는다.

**축소·매도 재검토:** 논지 반증이 지속되거나 경영진·회계 신뢰가 중대하게 훼손되는 경우. 실제 보유 여부를 확인하지 않았으므로 이는 조건부 모니터링 규칙이며 거래 지시가 아니다.

## 출처·완료 범위

[evidence.jsonl](evidence.jsonl), [출처 감사](../../reviews/2026-09-05-astra/source-audit.md), [전체 비교](../../reviews/2026-09-05-astra/README.md).

[이번 직접 확인한 회사 공식 자료](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx).

재심사 판단 신뢰도 68%. 종목 재평가 기록은 완료했지만 열린 가치평가·증거 게이트까지 해소됐다는 뜻은 아니다. 원문 전체 재실사·실시간 시세 갱신·거래 실행은 하지 않았다.

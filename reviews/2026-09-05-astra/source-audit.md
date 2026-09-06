# 출처·원자료 감사 — 2026-09-05

이번 작업은 기존 40개 종목 판단의 재심사다. 모든 종목의 최신 10-K·10-Q·DART 원문과 가격을 새로 수집한 전면 실사는 아니다. **직접 확인한 출처, 첨부 원문, 과거 분석에서 승계한 주장, 분석가 가정**을 구별한다. 모델명이 달라졌다는 이유로 증거의 신뢰도를 높이지 않았다.

## 직접 열람·대조한 중요 출처

| 대상 | 출처 | 확인 범위 | 현재 반영 |
|---|---|---|---|
| AVGO | [회사 공식 Q3 FY2026 발표](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-third-quarter-fiscal-year-2026-financial) | 2026-09-02 발표, GAAP 재무제표·현금흐름·부문매출·주식수 표 | 'GAAP 표 없음' 철회. 소프트웨어 성장 확인. Q3 차입과 현금·SBC를 별도 기록 |
| CRWD | [회사 공식 Q2 FY2027 발표](https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-reports-second-quarter-fiscal-year-2027-financial) | 2026-08-26 발표, 매출·ARR·FCF 및 FY27 희석주식수 가이던스 | 성장 가설과 가격 기대를 분리. 회사의 분할 반영 주식수 단위를 확인하고 임의로 다시 4배 보정하지 않음 |
| NOW | [회사 공식 Q2 2026 발표](https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx) | 구독·cRPO, 온프레미스 연방 매출 선반영, 비용·FCF 정의 | 모멘텀과 기대차의 과도한 확신 축소. 조정 FCF의 법률·인수 관련 가산을 owner-FCF로 오인하지 않음 |
| NVDA | [회사 공식 Q2 FY2027 발표](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx) | 매출·영업이익·Data Center 성장 및 전망 | 플랫폼 가치 지지. 전망은 실제 실적과 별도 |
| NVDA | 첨부 `NVDA-2027-Q2-10Q-Final-including-exhibits(1).pdf`, Note 10 Commitments and Contingencies / Guarantees | 공급·용량 약정, 기존 보증, 8월 후속 보증 및 부속 계약 | 공급 $279B는 7월 26일, SB Energy 최대 $105B는 8월 체결. 기존 보증 $3.5B와 합계 최대 $108.5B. 전액 즉시 손실 또는 현금성 부채로 가산하지 않음 |
| SK하이닉스 | [공식 Q2 2026 실적](https://news.skhynix.com/en/q2-2026-business-results/), [공식 FY2025 실적](https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/) | 공식 실적과 기초 정상화 기준 | 높은 당기이익의 존재를 확인하되, 그 숫자로 임의 정상화 FCF를 검증했다고 하지 않음 |
| 크래프톤 | [델라웨어 형평법원 의견](https://courts.delaware.gov/Opinions/Download.aspx?id=392880) | 2026-03-16 판결의 Unknown Worlds 계약·경영권 관련 판단. 손해배상 단계와 본안 사실판단 구분 | 경영진 신뢰 veto는 투자 의견. 범죄·분식 확정 주장 아님 |

크래프톤 관련 후속 합의는 [2026-07-01 후속 보도](https://www.theverge.com/games/960354/krafton-subnautica-2-settlement-bonuses-unknown-worlds)와 [회사 설명을 인용한 업계 보도](https://www.gamedeveloper.com/business/krafton-agrees-to-pay-bonuses-to-subnautica-2-studio-as-ceo-resigns)를 구별해 검토했다. 합의 사실만으로 과거 판단이 취소되거나 경영진 신뢰 문제가 해소됐다고 추정하지 않는다. 합의 원문·종전 판단 취소 여부·개선 조치에는 미확인 부분이 남아 있다. 법률적 권리 판단 또는 법률 자문이 아니다.

## 첨부 PDF와 승계 기록

- NVDA·GOOGL·NET·DDOG·ISRG의 첨부 공시와 기존 추출본/증거 장부를 사용했다. 업로드 이름의 연도·분기만 믿지 않고 내부 표의 보고기간을 기준으로 삼았다. 업로드 파일을 수정하거나 중복 업로드하지 않았다.
- 수치의 연결은 회사별 `valuation.json`의 과거 입력, `evidence.jsonl`, 기존 thesis와 PDF 표를 따라간다. TTM과 반기·단일 분기, 기본/가중평균/희석주식수를 혼합하지 않는다.
- 삼성전자·한화·TSM의 모든 원천 공시를 이번 회차에 새로 확보·독립 인증한 것은 아니다. 과거 장부의 공시 수치와 복구한 모형을 재심사했고 그 한계를 신뢰도·missing_data에 반영했다.
- Wave 20개의 기본 사업 근거는 `screening/2026-09-us-kr/evidence-wave-01.md`, `evidence-wave-02.md`, 기존 잠정 스코어카드다. 위 표에 없는 모든 원문을 새로 읽었다고 주장하지 않는다.
- Wave 재무 입력의 일부는 StockAnalysis 등 표준화 2차 자료다. 고정 입력의 산술 재현과 원문 인증은 다르다. 현금흐름 정의·희석주식수·인수/리스·소수주주 조정은 미해결 게이트로 기록했다.
- ANET·MU·PLTR·MELI·ASTS·RKLB·두산에너빌리티·파마리서치·한미반도체·한화오션·HD한국조선해양·리가켐바이오는 과거 정성 스크린의 판단과 근거 수준을 재심사했다. 원문과 가격 게이트가 충족되지 않아 새 정량 점수는 부여하지 않았다. 과거 보도의 모든 숫자를 이번에 검증된 사실로 다시 발표하지 않았다.

## 중요한 회계·모형 구분

1. SBC를 현금대체비용으로 차감한다면 동일 보상 주식의 미래 희석을 다시 전부 차감하지 않는다. 반대로 보고 FCF를 사용하면서 환매로 낮춘 순희석만 적용하고 환매 재원을 빼지 않으면 과대평가될 수 있다. 두 방식 모두 총발행·환매·재원의 브리지가 필요하다.
2. 회사 전체의 말기 현금성장률과 **주당** 말기 성장률은 다르다. 양의 희석이 계속되면 주당 성장률은 `(1+g)/(1+d)-1`이다. 기존 다섯 회사 DCF에 이 일관성 진단을 추가했다.
3. 할인율 9%·영구성장률 3% 통일은 분석가의 비교 가정이다. 비상장 투자 제외·무상 환매효과 제거 등도 함께 바뀌므로 이전 가치와의 차이를 순수한 할인율 효과라고 설명하지 않는다.
4. Hanwha의 SOTP는 원리상 적절하지만 모회사 순부채·제한현금·미집행 투자·보증 조정의 원천 근거가 약하다. Wave의 연결 FCF를 그대로 지분가치에 대응시키는 모형은 별개로 부적절하다.
5. 현대차 연결 순이익·금융 자산/부채는 제조 FCFE와 같지 않다. 알테오젠·리가켐의 최대 계약금액은 확정 수취액이 아니다. 임상·특허·파트너 위험의 상관을 반영해야 한다.
6. 잠정 Base/Bull은 확률이 아니다. 특히 대만 사건 확률과 NVDA 고객·보증 손실의 확률은 직접 관측할 수 없으며 임의의 작은 확률로 '낮은 영구손실'을 확정하지 않는다.

## 가격과 저장소 복구

기준 가격은 기존 종목별 시각을 유지했다. 일부는 9월 1일/3일 또는 4일 장중 가격이고 Wave 가격과 다르다. 실제 주문 전에는 동일 시점의 가격·완전희석 주식수·인수/증자 후 재무상태를 다시 맞춰야 한다.

기준 Git 커밋은 `367f55843d769da7e7b123007d78ac0b83eb83ef`. 오류는 13개 파일, 3개 기업에서 확인했다. NVDA는 `f09c7b0`, AVGO는 `1404eec`, 한화 점수는 `b5810b5`의 정상 JSON과 대조했다. 한화의 첫 SOTP 블록은 분리해 닫는 괄호를 복원했고, 다른 충돌 버전은 `18bc9b2`에서 확인했다. **구문 복구가 특정 과거 결론을 승인하는 것은 아니다.** 두 버전의 판단 차이를 현재 재평가에서 별도로 판정했다.

검증 통과는 JSON·합계·상태·계산·범위가 정합하다는 뜻이지, 미래 실적·공정가치·원문 진위 전체를 증명한다는 뜻이 아니다. 정책 파일과 점수 스키마는 변경하지 않았다.

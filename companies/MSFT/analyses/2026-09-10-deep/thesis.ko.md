# Microsoft (MSFT) — 2026-09-10 Deep Research Checkpoint

## 결론

- Decision: **WATCH**
- Priority: **P1**
- Business quality: **66/75**
- Total score: **78/100 — Emerging Outlier**
- Buy authorized: **false**
- Open Hard Veto: **incremental_roic_collapse, permanent_loss_probability**

Microsoft의 핵심 해자는 Azure 단독이 아니라 M365·Entra·Security·GitHub·Dynamics·데이터·클라우드의 결합 배포력이다. FY2026에는 Azure 성장, Copilot 유료좌석, GitHub Copilot 사용, 상업 RPO가 모두 개선돼 AI가 단순 데모에서 실제 매출·사용량으로 이동하고 있다는 증거가 강화됐다.

그러나 투자 논지의 병목은 제품수요가 아니라 **AI 인프라 투자수익률**이다. FY2026 OCF는 $182.935B로 강했지만 현금 PPE가 $115.948B로 급증했다. OCF-PPE $66.987B와 여기서 SBC $12.405B를 차감한 $54.582B는 유용한 진단치일 뿐, 운영·금융리스와 성장/유지투자 구분이 끝나지 않았으므로 normalized owner FCF라고 부르지 않는다.

## 사업과 해자

Q4 FY2026 Azure와 기타 클라우드 매출은 43% 증가했다. Microsoft 365 Copilot은 3천만 개 이상의 유료좌석, GitHub Copilot은 5천만 사용자를 기록했다. Copilot의 과금도 단순 좌석에서 좌석+사용량 구조로 확대되고 있어 고객가치가 매출로 전환되는 경로가 이전보다 명확하다.

Commercial RPO는 $678B다. 중요하게도 Q4 순증 RPO는 frontier-model 고객 외부에서 발생했고 OpenAI 제외 RPO도 25% 증가했다. Microsoft Cloud 매출의 거의 90%가 frontier-model 고객 외부라는 회사 설명까지 감안하면, OpenAI는 중요한 경제관계이지만 Microsoft 전체의 fatal concentration으로 보기는 어렵다.

## 재투자 경제성

반론은 자본집약도다. Microsoft Cloud Q4 gross margin은 65%까지 낮아졌다. 회사는 AI 인프라 믹스와 사용 증가를 주된 원인으로 설명한다. 달력연도 2026 CAPEX 예상도 리스분류 변경 후 약 $175B 수준이다. 용량부족 상태에서 새 용량이 빠르게 monetization되는 점은 긍정적이지만, 현재의 투자 코호트가 9% 요구수익률을 넘는 after-tax incremental ROIC를 장기적으로 낸다는 사실은 아직 관측되지 않았다.

따라서 `incremental_roic_collapse`는 실제 붕괴 판정이 아니라 **INVESTIGATE**다. 향후 핵심 지표는 Azure 매출성장 자체보다 증분 gross profit, cloud gross margin 안정화, 리스 포함 owner cash/share, datacenter utilization이다.

## 밸류에이션

2026-09-09 종가 $491.65와 7.443B valuation shares를 사용한다. 분석상 시가총액은 약 $3.659T이다.

기존 2026-09-06 장기모델을 보존하면 Bear/Base/Bull은 각각 약 **$147.02 / $458.83 / $1,013.59**다. 현 주가는 Base보다 약 7% 높다. Base의 첫해 매출 $400B, owner-margin 경로, 25x terminal multiple, 9% 요구수익률을 유지하면 2~10년 매출성장률 약 **11.79%**가 필요하다.

이 성장률은 Microsoft의 현재 Azure 속도를 보면 비현실적 bull-only 조건은 아니다. 그러나 회사 규모와 CAPEX 강도를 감안하면 충분한 margin of safety도 아니다. 사업품질과 기대수익률을 분리하면 기업은 매우 우수하지만 주식은 아직 WATCH가 맞다.

## Red Team

1. AI CAPEX가 구조적으로 높은데 감가상각·리스 비용은 후행해 현재 이익이 경제적 비용보다 좋아 보일 수 있다.
2. Azure 성장률이 높아도 hyperscaler 경쟁이 가격·마진을 제한할 수 있다.
3. Copilot 좌석 성장은 inference cost를 고려할 때 owner margin으로 동일하게 전환되지 않을 수 있다.
4. OpenAI 계약과 투자회계가 bookings·RPO·other income을 왜곡할 수 있다.
5. 자체 AI 가속기/모델 전환이 GPU 비용을 낮출 수도 있지만 실행실패 시 오히려 중복투자가 된다.
6. M365는 높은 switching cost가 있지만 규제와 경쟁제품이 번들 pricing power를 제한할 수 있다.
7. GitHub/개발자 플랫폼은 강하지만 coding-agent 인터페이스가 저장소와 IDE의 가치포착을 바꿀 수 있다.
8. 사이버보안 사고가 클라우드·identity 사업 전체의 신뢰에 비선형 손상을 줄 수 있다.
9. 대규모 RPO는 장기 수요증거이지만 모든 계약이 동일한 마진·현금전환을 보장하지 않는다.
10. 현 가격은 사업 실패가 아니라 성장 duration 단축만으로도 장기간 저수익이 가능하다.

## 증액 조건

Azure 성장, Microsoft Cloud gross margin, lease-aware owner cash/share가 최소 두 보고기간 동시에 개선되는지 확인한다. FY2026-FY2027 datacenter 투자 코호트의 after-tax incremental return이 9%를 넘는다는 증거가 필요하다. Copilot은 좌석수뿐 아니라 사용량 매출과 unit economics를 확인한다. OpenAI 외부 RPO가 계속 성장하고 실제 청구·현금으로 전환되어야 한다. 마지막으로 사업증거 개선과 함께 valuation이 Base 대비 명확한 할인으로 내려와야 한다. 가격 하락만으로 증액하지 않는다.

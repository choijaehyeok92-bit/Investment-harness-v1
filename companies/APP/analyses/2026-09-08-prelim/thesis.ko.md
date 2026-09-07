# APP 초벌분석 체크포인트 - 2026-09-08

> **NON-CURRENT RESEARCH CHECKPOINT**  
> 이 문서는 `companies/APP/latest.json` 또는 current registry authority를 변경하지 않는다. 현재 canonical authority는 별도 정식 harness run이 승격하기 전까지 2026-09-06 PRELIMINARY_REVIEW다.

## 0. 결론

- **판정:** WATCH
- **우선순위:** P1
- **매수 승인:** 없음
- **사업품질 점수:** 61/75
- **총점:** 미산정 - 현재가/9% reverse DCF/시나리오 미완료
- **핵심 메시지:** AppLovin의 현재 운영 성과는 매우 강하다. 하지만 이 종목의 다음 단계는 “성장이 진짜인가?”보다 **“Axon의 광고 성과 우위가 독립적으로 검증되고, 그 우위가 현재 주가에 얼마나 이미 반영돼 있는가?”**를 확인하는 것이다.

## 1. 이번 원자료 범위

사용자 제공 자료 중 읽을 수 있었던 자료는 다음과 같다.

- 2026 Definitive Proxy Statement
- 2026 Definitive Additional Proxy Materials
- 2026-08-05 Q2 earnings Form 8-K / Exhibit 99.1
- 2026-08-20 Form 4: Matthew Stumpf, Adam Foroughi, Corina Cacovean, Victoria Valenzuela, Xiaochuan Ge
- 2026-08-21 Form 144: Vasily Shikin

추가로 제공된 `d6d59334-570b-453f-8c55-30d0bda96a8e(1).pdf`는 1,104,599바이트 전체가 0x00인 손상 파일이라 읽을 수 없었다. 따라서 이번 체크포인트는 **읽을 수 있는 10-K/10-Q 직접 검증 없이** earnings 8-K와 proxy 중심으로 작성했다. FY2025 수치는 proxy가 직접 반복 제시한 범위만 사용했다.

## 2. 사업 및 성장

2025년에 Apps 사업을 매각하면서 회사는 핵심 광고 플랫폼에 더 집중했다. Proxy는 2025년 매출 약 $5.5B(+70%), Adjusted EBITDA 약 $4.5B(+87%), FCF 약 $4.0B(+91%)를 제시했고, 회사는 Axon Ads Manager와 Axon AI recommendation engine 개선, 그리고 web-based e-commerce 광고주 초기 확장을 강조했다.

Q2 2026에는 매출 $1.924B로 전년 대비 약 53% 증가했다. GAAP 영업이익은 $1.494B, 계산상 영업이익률은 약 77.7%다. 순이익은 $1.267B, 조정 EBITDA는 $1.614B, 조정 EBITDA margin은 84%였다. Q3 매출 가이던스는 $2.055B~$2.085B로, midpoint 기준 Q2 대비 약 7.6%의 추가 순차 성장을 시사한다.

이 조합은 단순 매출 성장보다 강하다. **매출 성장, GAAP 이익, 현금흐름, 낮은 물리적 자본투자**가 동시에 나타나고 있다. 다만 이러한 결과가 Axon의 구조적 경쟁우위에서 나온 것인지, 광고시장·트래픽 믹스·특정 채널 최적화의 일시적 효과인지 독립 검증은 아직 없다.

## 3. 현금창출과 주당 경제성

Q2 2026 OCF는 $869.0M, 회사 정의 FCF는 $863.3M이었다. 회사 FCF 정의는 OCF에서 PPE 구매와 finance-lease principal을 차감한다. Q2 해당 두 항목의 합은 약 $5.7M에 불과해 매우 asset-light한 구조를 보여준다.

SBC는 Q2 $85.8M, H1 $169.3M으로 매출의 약 4.5% 수준이다. Snowflake처럼 SBC가 FCF를 압도하는 구조가 아니다. 더 중요한 점은 **주식 수가 실제로 감소했다는 것**이다.

- Q2 diluted weighted-average shares: 337.0M vs 342.2M, 약 -1.5% YoY
- H1 diluted weighted-average shares: 337.9M vs 343.5M, 약 -1.6% YoY
- Ending shares: 335.3M vs 2025 year-end 338.3M, 약 -0.9%
- H1 common-stock repurchases: $1.533B

따라서 현재 자료만 보면 `persistent_dilution`은 hard veto가 아니라 **PASS** 쪽이다. 다만 이것은 repurchase 가격이 합리적이었다는 뜻은 아니다. 고평가 구간의 buyback은 주당 가치 훼손이 될 수 있으므로 reverse DCF 이후 repurchase IRR을 별도 점검해야 한다.

## 4. FCF 성장 속도의 작은 경고

Q2 매출은 약 53% 늘었지만 회사 FCF는 $768.1M에서 $863.3M으로 약 12.4% 증가하는 데 그쳤다. H1 OCF는 약 35% 증가했다. H1 현금소득세 지급은 $639.8M으로 전년 동기 $100.6M보다 크게 늘었다.

즉 현재 현금창출력 자체는 매우 높지만, **매출 증가율과 현금 증가율 사이의 격차**는 정규화가 필요하다. 손상된 첨부 파일 대신 읽을 수 있는 10-Q를 확보해 매출채권, 세금, 기타 운전자본의 정상 수준을 확인해야 한다.

## 5. 재무 생존성

2026-06-30 기준 현금은 약 $3.05B, 장기부채는 약 $3.52B다. 순부채는 약 $462M이다. H1 Adjusted EBITDA $3.171B를 단순 연율화하면 순부채는 약 0.07배 수준이다.

따라서 현재 관찰되는 문제는 생존성이나 자금조달 의존이 아니라 **성장의 질, 해자의 지속성, 그리고 가격**이다. readable 10-K/10-Q를 확보하면 만기 구조·covenant·금리 조건은 정식으로 재검증해야 한다.

## 6. 경영진과 지배구조

긍정적 요소:

- 9명 이사 후보 중 6명 independent
- independent Chairperson
- standing committee 전부 independent
- H1 $1.53B buyback에도 실제 share count 감소
- 2026년 equity-plan evergreen 자동 증가를 사용하지 않음

반면 지배구조 집중은 명확한 리스크다.

- Adam Foroughi 총 voting power 약 61.6%
- Voting Agreement parties 총 voting power 약 66.9%
- Class B는 1주당 20표, Class A는 1표
- 회사는 share-class별 투표결과 공개를 요구한 주주제안에 반대를 권고

즉 소수주주 관점에서는 **운영 실행력은 매우 강하지만 통제권 견제는 약하다.** 이는 사업품질 점수를 바로 훼손하는 hard veto는 아니지만, management/capital allocation 점수를 제한하는 요소다.

## 7. 내부자 거래 해석

2026-08-20 Form 4 다섯 건은 모두 `F` 코드다. 각 공시는 RSU/PSU vesting과 관련된 세금 및 원천징수 의무를 충족하기 위해 회사가 주식을 withheld한 것이며 **보고자의 주식 매도가 아니라고 명시**한다. 따라서 bearish insider-sale signal로 처리하지 않는다.

Vasily Shikin의 2026-08-21 Form 144는 117,598주, 신고 시장가치 약 $35.6M의 proposed sale이다. 최근 2026-05-22에도 89,720주를 약 $43.5M에 매도했다. 제공 Form 144에는 Rule 10b5-1 plan adoption date가 기재돼 있지 않다. 다만 Form 144는 proposed-sale notice이고, Shikin은 `associated, still within 90 window`로 기재돼 있으므로 이 사실만으로 재량적 약세 판단을 확정하지 않는다.

## 8. 초벌 점수

| 항목 | 점수 | 핵심 이유 |
|---|---:|---|
| 구조적 변화·리더십 | 14/15 | 50%+ 성장과 80%대 EBITDA margin, 플랫폼 집중 및 e-commerce 확장 |
| 고객가치·제품 | 8/10 | 결과는 강하나 독립 ROAS/retention 미검증 |
| 해자 추세 | 11/15 | 비정상적으로 높은 margin과 성장, 그러나 플랫폼·트래픽 의존성 검증 필요 |
| 증분 ROIC·FCF/share | 13/15 | asset-light, 높은 FCF, 낮은 SBC, 실제 주식 수 감소 |
| 경영진·자본배분 | 6/10 | buyback 효과는 긍정적이나 66.9% voting control과 valuation discipline 미검증 |
| 재무 생존성 | 9/10 | 순부채 미미, 현금창출력 매우 강함 |
| **사업품질** | **61/75** | |
| 기대차·밸류에이션 | 보류 | 현재가/reverse DCF 없음 |
| Power-law·비대칭 | 보류 | 가격 없는 asymmetry 판정 금지 |

## 9. Hard Veto

- `management_or_accounting_integrity`: **INVESTIGATE** - readable 10-K/10-Q가 없어 감사·ICFR·10-Q controls 직접 검증 미완료
- `external_capital_dependence`: **PASS**
- `persistent_dilution`: **PASS**
- `low_quality_growth`: **PASS**, 단 Q2 FCF 성장률 격차 설명 필요
- `incremental_roic_collapse`: **INVESTIGATE** - Axon/e-commerce 증분 ROIC와 buyback IRR 미측정
- `moat_shrinkage`: **INVESTIGATE** - 독립 ROAS/retention/traffic quality 없음
- `price_requires_unrealistic_bull_case`: **INVESTIGATE** - valuation gate open
- `fatal_concentration`: **INVESTIGATE** - customer/platform/traffic concentration 미확인
- `permanent_loss_probability`: **INVESTIGATE** - 가격·지배구조 downside 미완료

## 10. 다음 조사 우선순위

1. readable FY2025 10-K와 Q2 2026 10-Q 확보
2. 현재가 동기화 후 9% reverse DCF
3. 광고주 ROAS, retention, cohort expansion의 독립 검증
4. customer / traffic source / platform policy concentration
5. 8개 분기 gross issuance - withholding - repurchase - ending share bridge
6. buyback average price와 intrinsic value 비교
7. 법률·규제·광고 측정·traffic quality 관련 리스크 검증

현재 단계에서 APP는 **“사업은 강하게 통과 중이지만 가격과 해자 독립검증이 아직 열려 있는 P1 WATCH”**로 분류한다.

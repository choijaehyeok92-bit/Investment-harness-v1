# 후속 체크포인트 — 전용모형·Red Team

- 기준일: 2026-09-04
- 범위: 미국 10개, 한국 10개
- 상태: **20개 총점 완료, Red Team 20개 완료, `WATCH` 18개, `SCREEN_OUT` 2개, `SCREEN_IN` 0개**
- 목적: 하네스의 다음 승격 게이트를 정하는 조사 산출물이며 매수 추천이나 목표주가가 아니다.

## 결론

**사실(Fact)**

- SK하이닉스의 공식 2026년 2분기 현금 88.0조 원과 부채 18.6조 원으로 이전 순현금 입력 충돌을 69.4조 원으로 조정했다.
- 현대자동차는 2025년 지배기업 소유주 귀속이익 9.446조 원과 자동차·금융부문 손익을 확인해 공통 제조업 FCF 모형에서 분리했다.
- 알테오젠은 Qlex의 실제 매출과 계약별 조건부 대가를 확인해 최대 마일스톤을 평활 매출로 사용하지 않았다.
- 델라웨어 형평법원은 크래프톤이 Unknown Worlds 핵심인력을 정당한 사유 없이 해임하고 운영통제권을 부당하게 탈취해 인수계약을 위반했다고 판결했다. 당사자들이 이후 합의해 소송을 종료했지만 합의금은 공개되지 않았다.

**추정(Estimate)**

- SK하이닉스는 정상화 시작 FCF 25조 원에서 종료 FCF까지 선형으로 움직이는 사이클 모형을 사용했다. 현대차는 귀속이익 성장·배당·종료 PER을, 알테오젠은 주관적 30%/50%/20% Bear/Base/Bull 확률을 사용했다.
- 미국 요구수익률 9%, 한국 요구수익률 10%를 유지했다. 모든 시나리오 값과 확률은 회사 가이던스가 아니라 스트레스 테스트다.

**추론(Inference)**

- 세 종목의 구조적 입력 공백은 의사결정 가능한 범위로 바뀌었다. 다만 SK하이닉스의 정상화 FCF와 알테오젠의 계약 확률은 낮은 신뢰도의 범위이므로 `INVESTIGATE`가 남는다.
- 크래프톤 판결은 단순 소송 노이즈가 아니라 인수계약·운영통제에 관한 경영진 행위의 사법적 판단이다. 이는 `management_or_accounting_integrity` Hard Veto의 물적 훼손 조건에 해당한다.

**의견(Opinion)**

- SK하이닉스 38점(B), 현대차 31점(WATCH), 알테오젠 37점(B)으로 총점을 확정한다. 셋 모두 즉시 승격하지 않는다.
- 크래프톤은 40점(B)과 좋은 가격 기대차에도 `FAIL`이 점수를 이기므로 `SCREEN_OUT`한다. CRWD의 가격 Hard Veto도 유지한다.
- Red Team의 `PASS`는 NOW와 NAVER 두 곳뿐이다. 이는 매수 통과가 아니라 현재 투자논리가 1차 반증 공격을 견뎠다는 뜻이며, 두 종목 모두 열린 Hard Flag 때문에 `WATCH`다.

## 세 전용모형

| 종목 | 공통모형을 쓰지 않은 이유 | 역산 요구 | Bear IRR | Base IRR | Bull IRR | 기대차 | 총점 | 판정 |
|---|---|---|---:|---:|---:|---:|---:|---|
| SK하이닉스 | 피크 이익과 설비투자의 메모리 사이클 | 10년 종료 FCF 167.5조 원; 종료 FCF 마진 20%이면 매출 837.6조 원 | -11.8% | -1.3% | 10.5% | 1/6 | 38(B) | `WATCH` — 가격·사이클 |
| 현대자동차 | 자동차 제조와 캡티브 금융, 복수 주식종류 | 9배 종료 PER·35% 배당에서 10년 귀속이익 CAGR 7.85% | -2.8% | 5.5% | 12.0% | 2/6 | 31(WATCH) | `WATCH` — 마진·증분 ROIC |
| 알테오젠 | 계약별 조건부 마일스톤·로열티·임상·IP 확률 | 확률가중 10년 종료 부 20.11조 원 대 현재 지분가치 20.20조 원 | -14.5% | -3.3% | 11.1% | 1/6 | 37(B) | `WATCH` — 계약·IP·가격 |

SK하이닉스 Bull은 10년 종료 FCF 150조 원, 종료 15배를 가정한다. 2026년 2분기의 이익 급증 때문에 이를 불가능하다고 단정하지는 않지만, 장기 사이클 평균으로 입증되기 전까지 가격 Hard Veto는 `INVESTIGATE`다. 현대차는 가격 자체가 비현실적 Bull을 요구하지 않아 가격 게이트는 `PASS`지만 Base가 10% 허들을 넘지 못한다. 알테오젠은 여러 파트너 성공이 겹치는 Bull에서만 허들을 넘으므로 확률가중 안전마진이 없다.

기계 판독 가능한 전체 입력·산식·시나리오는 `special-models-wave-01-02.jsonl`에 있다.

## Red Team 판정

| 시장 | 종목 | 가장 강한 반대논리 | 가장 위험한 숨은 가정 | 판정 | 결정 영향 |
|---|---|---|---|---|---|
| US | NOW | AI 에이전트가 워크플로 계층을 우회하고 SBC가 주당가치를 잠식 | ServiceNow가 계속 오케스트레이션 통제면을 유지 | `PASS` | `WATCH` 유지 |
| US | AMZN | AWS·물류의 자본집약도가 영구 상승해 성장보다 현금전환이 약함 | AI 설비 고가동률과 가격 방어 | `REVISE` | `WATCH` 유지 |
| US | LLY | tirzepatide 물량이 가격·접근성 악화와 투자피크를 가림 | 장기 복약·급여·후속약 성공 | `REVISE` | `WATCH` 유지 |
| US | MSFT | AI 인프라 상품화로 감가·리스·파트너 몫이 주당 FCF를 흡수 | Copilot·Azure의 증분 현금수익 | `REVISE` | `WATCH` 유지 |
| US | VRT | 희소성 주문·선수금·마진이 공급확대 후 함께 정상화 | 잔고가 취소·이중주문 없이 확정수요 | `REVISE` | `WATCH` 유지 |
| US | META | AI와 Reality Labs 두 자본 프로그램이 광고해자보다 먼저 현금을 소모 | AI 투자 회수와 자본배분 중단 규율 | `REVISE` | `WATCH` 유지 |
| US | AXON | SBC·ATM·취소가능 bookings가 주당 경제를 과대 표시 | 계약전환과 희석 정상화 | `REVISE` | `WATCH` 유지 |
| US | VRTX | CF 성숙 전에 비CF 출시·대형인수가 현금을 대체하지 못함 | 제품별 상업화와 Crinetics 성공 | `REVISE` | `WATCH` 유지 |
| US | ETN | 후기 사이클 주문과 고가 Boyd 인수가 성장·마진을 부풀림 | 인수 ROIC와 전력사이클 지속 | `REVISE` | `WATCH` 유지 |
| US | CRWD | 신뢰 훼손·희석·성장둔화와 고배수 정상화가 겹침 | Bull-plus 성장과 30배 종료배수 | `REJECT` | `SCREEN_OUT` 유지 |
| KR | NAVER | 생성형 인터페이스가 검색 진입점을 약화시키는 동안 AI 자산·희석이 남음 | 검색해자와 AI 투자 후 주당 FCF | `PASS` | `WATCH` 유지 |
| KR | 삼성바이오로직스 | 가격이 신공장 고가동률·인수 성공·고객 프로그램 성공을 함께 요구 | 용량이 실제 고수익 계약으로 전환 | `REVISE` | `WATCH` 유지 |
| KR | 현대자동차 | 자동차 마진과 금융 신용이 투자피크에서 동시에 악화 | 8%에 가까운 장기 귀속이익 성장 | `REVISE` | 점수 완료, `WATCH` |
| KR | APR | 바이럴·영웅제품 성장을 장기 브랜드 해자로 오인 | 재구매·CAC·채널 sell-through | `REVISE` | `WATCH` 유지 |
| KR | 알테오젠 | 조건부 계약 최대액을 확정가치로 자본화 | Qlex 외 복수 파트너 성공과 IP/FTO | `REVISE` | 점수 완료, `WATCH` |
| KR | SK하이닉스 | HBM 희소성과 피크 이익을 장기 현금경제로 자본화 | 리더십·현금전환·15배 종료배수 | `REVISE` | 점수 완료, `WATCH` |
| KR | HD현대일렉트릭 | 변압기 공급부족이 풀리며 가격·마진·배수가 동시 정상화 | 잔고 확정성과 25% 마진 지속 | `REVISE` | `WATCH` 유지 |
| KR | 한화에어로스페이스 | 안전·납기·국가집중 위험과 과거 희석이 주당가치를 훼손 | 사고 재발 방지와 계약 현금전환 | `REVISE` | `WATCH` 유지 |
| KR | LS ELECTRIC | 북미 희소성을 10년 성장으로 외삽하는 동안 운전자본이 현금을 고정 | 증설 후 가동률과 FCF 마진확대 | `REVISE` | `WATCH` 유지 |
| KR | 크래프톤 | 법원이 확인한 인수계약 위반·운영통제 탈취가 자본배분 신뢰를 훼손 | 행위가 일회성이며 합의가 비용을 종결 | `REJECT` | **`SCREEN_OUT` 전환** |

Red Team의 종목별 세 가지 숨은 가정, 반증 조건, 누락 근거, 영구손실 사건은 `red-team-wave-01-02.jsonl`에 있다.

## Hard Veto와 최신 상태

| 구분 | 종목 | Hard Veto | 최신 판정 |
|---|---|---|---|
| 신규 `FAIL` | 크래프톤 | `management_or_accounting_integrity` | `SCREEN_OUT` |
| 유지 `FAIL` | CRWD | `price_requires_unrealistic_bull_case` | `SCREEN_OUT` |
| 가격 `INVESTIGATE` | VRT, SK하이닉스, LS ELECTRIC, HD현대일렉트릭, 알테오젠 | 현재 가격이 강한 Bull에 인접 | `WATCH` |
| 기타 `INVESTIGATE` | 나머지 13개 | 해자·증분 ROIC·집중·희석 등 | `WATCH` |

총점은 20개 모두 완료됐지만 Hard Veto 선순위 규칙 때문에 `SCREEN_IN`은 없다. 최신 20개 결정 객체는 `stage1-decisions-wave-01-02.jsonl`이 단일 기준이다. 이전 `expectation-overlays-wave-01-02.jsonl`은 직전 체크포인트의 역사적 스냅샷으로 유지한다.

## 조건부 심층조사 큐

아래는 승격이나 매수 후보가 아니라, 각 시장 최대 5개의 **다음 조사 순서**다. 열린 `INVESTIGATE`가 해소되기 전에는 심층분석 완료 또는 `SCREEN_IN`으로 올리지 않는다.

| 순위 | 미국 | 우선 반증 | 한국 | 우선 반증 |
|---:|---|---|---|---|
| 1 | NOW | AI 우회·SBC 차감 주당 FCF | NAVER | 검색해자·AI 투자 후 주당 FCF |
| 2 | AMZN | AWS 리스 가동률·세그먼트 ROIC | 현대자동차 | 제조 마진·금융 신용손실 |
| 3 | MSFT | AI 투하자본·Copilot 현금수익 | 삼성바이오로직스 | 공장별 가동률·고객집중 |
| 4 | LLY | 제품별 접근성·증설/인수수익 | APR | 코호트 재구매·CAC·sell-through |
| 5 | VRTX | 비CF 제품 확률·인수수익 | 알테오젠 | 계약별 현금·로열티·IP/FTO |

## 다음 체크포인트

1. 조건부 큐 10개에 저장소의 전체 기업분석 워크플로를 순차 적용한다.
2. 증분 ROIC와 주당 FCF를 공통 필수 산출물로 만들고, 기업별 핵심 반증을 먼저 검증한다.
3. `INVESTIGATE`를 증거로 해소한 종목만 재판정한다. 점수만으로 `SCREEN_IN`하지 않는다.
4. CRWD는 가격 또는 주당 현금경제가, 크래프톤은 독립적 지배구조 개선 증거가 구조적으로 바뀔 때만 재진입시킨다.

## 주요 원천

- SK하이닉스: [2026년 2분기 실적](https://news.skhynix.com/en/q2-2026-business-results/), [2025년 연간 실적](https://news.skhynix.com/en/sk-hynix-announces-fy25-financial-results/)
- 현대자동차: [2026년 2분기 실적](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001234), [2025년 연결 감사보고서](https://www.hyundai.com/content/dam/hyundai/ww/en/images/company/investor-relations/financial-Information/report-en/2025/2025-q4-consolidated-audit-report-en.pdf)
- 알테오젠: [2026년 2분기 잠정실적](https://www.alteogen.com/en/sub/ir/notice.php?bid=15&idx=348&mode=view), [Novartis 계약](https://www.alteogen.com/en/sub/ir/news.php?bid=13&idx=359&mode=view&page=1), [FDA의 Keytruda Qlex 승인](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-pembrolizumab-and-berahyaluronidase-alfa-pmph-subcutaneous-injection), [Merck 2025 10-K](https://www.merck.com/wp-content/uploads/sites/124/2026/02/MRK-12.31.2025-10K-FINAL.pdf)
- 크래프톤: [델라웨어 형평법원 판결문](https://courts.delaware.gov/Opinions/Download.aspx?id=392880), [2026년 2분기 실적](https://www.krafton.com/en/uncategorized/krafton-announces-second-quarter-2026-results/), [합의 보도](https://www.theverge.com/games/960354/krafton-subnautica-2-settlement-bonuses-unknown-worlds)
- 나머지 16개 기업의 1차 자료 맵: `evidence-wave-01.md`, `evidence-wave-02.md`

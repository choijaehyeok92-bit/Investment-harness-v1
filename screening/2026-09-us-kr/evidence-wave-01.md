# Stage 1 증거 노트 — Wave 01

- 기준일: 2026-09-04
- 범위: 미국 5개, 한국 5개
- 상태: 원천자료 매핑 및 최근 사업 신호 1차 판독 완료
- 주의: 아래 평가는 스크리닝 중간 산출물이며 매수 추천 또는 최종 점수가 아니다.

## 요약

| 시장 | 종목 | 1차 신호 | 잠정 Hard Red Flag | 조사 우선순위 |
|---|---|---|---|---|
| US | MSFT | Azure·Cloud·Copilot의 성장과 계약잔고가 강함 | AI capex의 증분 ROIC·투자이익 조정 | 계속 조사 |
| US | AMZN | AWS·광고·리테일 이익이 동시에 개선 | AI capex로 TTM FCF 적자·Anthropic 평가이익 | 계속 조사 |
| US | META | 광고 물량과 가격이 함께 성장 | capex 급증·부채 증가·Reality Labs 손실 | 계속 조사 |
| US | NOW | 구독·cRPO·대형계약·AI ACV 동반 성장 | 인수·SBC·AI 대체 위험 | 계속 조사 |
| US | CRWD | ARR 재가속·모듈 확장·FCF 개선 | GAAP 수익성·SBC·장애 후 장기 비용 | 계속 조사 |
| KR | 000660 | AI 메모리·HBM4·장기계약·순현금 개선 | 비경상 순이익·사이클·고객/설비 집중 | 계속 조사·수치 검증 |
| KR | 207940 | 높은 설비가동·계약가치·Plant 5 확장 | 인수·증설의 증분 ROIC·고객 집중 | 계속 조사 |
| KR | 005380 | 하이브리드 믹스와 북미 점유율은 견조 | 판매량 감소·마진 압박·금융부문/관세 | 보수적 계속 조사 |
| KR | 012450 | 방산 수출 잔고와 납품 가시성이 높음 | 안전사고·유상증자 전력·대규모 투자·국가 집중 | Red Flag 우선 조사 |
| KR | 010120 | 북미 전력기기 주문·잔고·마진 동반 확대 | 증설·운전자본·사이클 정상화 | 계속 조사 |

## 미국

### MSFT — Microsoft

**사실**

- FY2026 매출은 3,318억 달러로 18%, 영업이익은 1,552억 달러로 21% 증가했다.
- 4분기 Azure 및 기타 클라우드 서비스 매출은 43% 증가했고, 상업용 RPO는 6,780억 달러로 84% 늘었다.
- Azure 연간 매출은 처음 1,000억 달러를 넘었고 Microsoft 365 Copilot 유료 좌석은 3,000만 개를 넘었다.
- 분기 순이익에는 Anthropic 투자 관련 32억 달러 이익이 포함되어, 보고 이익과 핵심 영업이익을 분리해야 한다.

**1차 추론**

- Azure·Microsoft 365·보안·개발도구를 한 계약 구조 안에서 교차판매하는 해자는 강화되는 방향이다.
- 수요와 RPO는 강하지만, GPU 중심의 짧은 내용연수 자산 투자 속도가 매출보다 빨라질 경우 주당 FCF 전환이 지연될 수 있다.

**잠정 Red Flag**

- `incremental_roic_collapse: INVESTIGATE`
- `low_quality_earnings: INVESTIGATE` — 투자평가이익을 핵심 이익과 분리
- 외부자본 의존이나 생존성 문제는 현재 자료에서 관찰되지 않음

**다음 증거**

- FY2026 10-K에서 데이터센터 capex, 감가상각, 계약부채와 OpenAI 관련 약정 추출
- Azure AI와 비AI 성장, Copilot ARPU/좌석 유지율, 주당 FCF 증가율을 분리
- 완전희석 주식수와 현재 가격을 사용한 역산 기대치 계산

출처: [Microsoft FY2026 Q4 실적](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast), [Microsoft FY2026 10-K](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm)

### AMZN — Amazon

**사실**

- 2026년 2분기 매출은 2,006억 달러로 20%, 영업이익은 275억 달러로 43% 증가했다.
- AWS 매출은 422억 달러로 37%, AWS 영업이익은 166억 달러로 전년 102억 달러 대비 증가했다.
- 광고 매출은 26% 성장했고 북미·인터내셔널 부문도 모두 영업흑자를 기록했다.
- TTM 영업현금흐름은 1,614억 달러로 33% 증가했지만, AI 관련 자산투자가 크게 늘어 TTM FCF는 76억 달러 유출이었다.
- 분기 순이익에는 Anthropic 투자 관련 534억 달러의 세전 기타이익이 포함됐다.

**1차 추론**

- AWS·광고·물류 네트워크가 서로 다른 이익원을 제공하며, AWS의 성장 재가속은 해자 약화보다 수요 확대 쪽 증거다.
- 현재 핵심 쟁점은 성장의 존재가 아니라 AI 설비가 장기 사용률과 주당 FCF로 전환되는 속도다.

**잠정 Red Flag**

- `incremental_roic_collapse: INVESTIGATE`
- `low_quality_earnings: INVESTIGATE` — Anthropic 평가이익 영향
- `external_capital_dependence: PASS`로 보이나 리스·구매약정 포함 재검증 필요

**다음 증거**

- AWS AI/칩 사업의 내부·외부 매출 중복과 투자자산 거래관계 확인
- 현금 capex, 금융리스, 구매약정 및 데이터센터 내용연수 정규화
- 리테일 배송속도 개선이 단위당 비용과 반복구매에 미치는 효과 확인

출처: [Amazon 2026년 2분기 SEC 실적자료](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm), [Amazon 2025 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm)

### META — Meta Platforms

**사실**

- 2026년 2분기 매출은 608억 달러로 28% 증가했다. 광고 노출은 14%, 광고당 평균가격은 12% 늘었다.
- 일간활성이용자는 36억 명으로 3% 증가해 이용자 증가보다 수익화 개선의 기여가 컸다.
- 분기 capex는 311억 달러였고 회사는 2026년 capex 전망을 1,300억~1,450억 달러로 제시했다.
- 분기 FCF는 7.84억 달러, 현금·유가증권은 902.6억 달러, 장기부채는 836.6억 달러였다.
- Reality Labs는 분기 46.2억 달러의 영업손실을 기록했다.

**1차 추론**

- 광고 네트워크의 가격과 물량이 동시에 증가해 현재 해자는 약화보다 강화 쪽이다.
- 다만 AI 투자액이 급증하면서 광고 효율 개선과 신규 제품 선택가치가 실제 FCF를 얼마나 창출하는지 입증 부담도 커졌다.

**잠정 Red Flag**

- `incremental_roic_collapse: INVESTIGATE`
- `capital_allocation: INVESTIGATE` — Reality Labs와 AI 인프라의 합산 수익률
- 규제·법률 비용은 계속 조사하되 현재 단계에서 경영진 신뢰성 FAIL 근거는 없음

**다음 증거**

- AI 추천 개선이 광고 전환율·가격·노출에 미친 효과를 사용자 성장과 분리
- GPU/데이터센터 감가상각과 장기 구매약정을 반영한 정상화 FCF 산출
- Reality Labs 누적 손실과 제품별 상업화 마일스톤 점검

출처: [Meta 2026년 2분기 실적](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/default.aspx), [Meta 2025 10-K](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm)

### NOW — ServiceNow

**사실**

- 2026년 2분기 구독매출은 38.77억 달러로 24.5%, 총매출은 39.87억 달러로 24% 증가했다.
- cRPO는 132억 달러로 21%, 총 RPO는 290억 달러로 21% 증가했다.
- 순신규 ACV 100만 달러 초과 거래는 123건으로 약 40% 증가했고, ACV 500만 달러 초과 고객은 658곳으로 23% 늘었다.
- ServiceNow AI의 ACV는 10억 달러를 넘어섰다.

**1차 추론**

- 대형고객·계약잔고·AI 계약이 함께 늘어 기존 워크플로 전환비용이 AI로 훼손됐다는 증거는 아직 없다.
- AI가 기능을 대체하기보다 여러 시스템을 연결·통제하는 계층으로 작동한다면 플랫폼 해자가 더 강해질 수 있다.

**잠정 Red Flag**

- `moat_shrinkage: INVESTIGATE` — 독립 AI 에이전트의 워크플로 대체 가능성
- `persistent_dilution: INVESTIGATE` — SBC와 자사주 상쇄를 주당 기준으로 검증
- 대형 인수의 가격과 통합 리스크 조사 필요

**다음 증거**

- 갱신율·순매출유지율과 AI 신규 ACV의 기존 제품 잠식 여부 확인
- SBC/매출·완전희석주식수·주당 FCF 3년 추세 추출
- 연방정부 계약의 분기 당김 효과와 민간 수요를 분리

출처: [ServiceNow 2026년 2분기 실적](https://investor.servicenow.com/news/news-details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx), [ServiceNow 2026년 2분기 10-Q](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000076/now-20260630.htm), [ServiceNow 2025 10-K](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000007/now-20251231.htm)

### CRWD — CrowdStrike

**사실**

- FY2027 2분기 매출은 14.7억 달러로 26%, 구독매출은 14.0억 달러로 27% 증가했다.
- ARR은 58.4억 달러로 25% 증가했고 분기 순신규 ARR은 3.328억 달러였다.
- GAAP 구독 총마진은 78%, 분기 FCF는 3.774억 달러, 현금은 50.1억 달러였다.
- 6개·7개·8개 이상 모듈 채택률은 각각 51%·35%·26%였다.
- GAAP 영업손실은 3,320만 달러로 전년 1.055억 달러 손실보다 축소됐다.

**1차 추론**

- ARR 재가속과 다중 모듈 채택은 2024년 장애 이후 플랫폼 통합 해자가 회복되고 있다는 긍정 신호다.
- 높은 구독 총마진과 FCF는 생존성을 지지하지만, 주당가치 창출은 SBC·희석·고객보상 비용을 포함해야 한다.

**잠정 Red Flag**

- `persistent_dilution: INVESTIGATE`
- `management_operational_integrity: INVESTIGATE` — 과거 장애의 반복 방지와 장기 고객보상 비용
- `external_capital_dependence: PASS`로 보임

**다음 증거**

- 장애 관련 고객보상·소송·보험회수의 총액과 잔여 기간 추출
- ARR 정의, Falcon Flex 계약의 현금회수 및 RPO 전환 확인
- SBC/매출과 환매 후 발행주식수 변화 검증

출처: [CrowdStrike FY2027 2분기 SEC 실적자료](https://www.sec.gov/Archives/edgar/data/1535527/000153552726000029/crwd-20260826xex991.htm), [CrowdStrike FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1535527/000153552726000010/crwd-20260131.htm)

## 한국

### 000660 — SK하이닉스

**사실**

- 회사 발표 기준 2026년 2분기 매출은 79.32조 원, 영업이익은 60.54조 원이며 전년 대비 각각 257%·557% 증가했다.
- HBM4 양산 출하가 시작됐고 회사는 약 10개 주요 고객과 장기공급계약을 체결했다고 밝혔다.
- 분기말 현금은 88조 원, 총부채는 18.6조 원으로 회사 발표상 순현금은 69.4조 원이다.
- 순이익 93.92조 원이 영업이익과 매출을 크게 상회하므로 비경상·평가·세무 항목의 원천공시 검증이 필수다.

**1차 추론**

- HBM4 성능·수율·장기계약은 단순 메모리 가격상승 이상의 고객 공동개발 및 공급 신뢰 해자를 시사한다.
- 그러나 현재 이익률은 정상화 가능한 장기 수익성으로 간주할 수 없으며, 사이클 정점 이익을 자본화하면 안 된다.

**잠정 Red Flag**

- `low_quality_earnings: INVESTIGATE` — 순이익 초과 요인 확인
- `incremental_roic_collapse: INVESTIGATE` — 대규모 증설 이후 가격·수율·가동률
- `fatal_concentration: INVESTIGATE` — AI 가속기 고객 및 HBM 수요 집중

**다음 증거**

- DART 반기보고서에서 손익·현금흐름·비경상손익·Capex·약정 재검산
- HBM 매출 비중, 고객별 집중도, 선급금과 취소 가능성 확인
- 웨이퍼 투입 대비 HBM 출하·수율 및 범용 DRAM 가격 민감도 추정

출처: [SK하이닉스 2026년 2분기 실적](https://news.skhynix.com/en/q2-2026-business-results/), [SK하이닉스 IR 실적자료실](https://www.skhynix.com/ir/UI-FR-IR06/)

### 207940 — 삼성바이오로직스

**사실**

- 2026년 2분기 매출은 1.321조 원, 영업이익은 5,864억 원이었다. 상반기 매출은 2.578조 원, 영업이익은 1.167조 원이다.
- 회사가 제시한 누적 계약가치는 216억 달러다.
- Plant 1~4는 안정적으로 가동됐고 Plant 5는 PPQ 활동과 함께 램프업 중이다.
- 미국 Rockville 공장 통합과 PolyPeptide Group 현금 공개매수를 추진하고 있다.

**1차 추론**

- 규제 승인·품질 이력·대규모 설비·고객 전환비용이 결합된 CDMO 해자는 강화되는 방향이다.
- Plant 5와 해외 인수는 성장 활주로를 늘리지만, 높은 가동률과 증분 ROIC가 유지돼야만 가치창출이다.

**잠정 Red Flag**

- `incremental_roic_collapse: INVESTIGATE` — 신규설비와 인수 수익률
- `fatal_concentration: INVESTIGATE` — 상위 고객과 제품별 계약 집중도 미확인
- `external_capital_dependence: INVESTIGATE` — 인수 후 순현금·부채 구조 확인

**다음 증거**

- DART 반기보고서에서 고객집중·계약부채·capex·차입 및 인수자금 확인
- Plant별 생산능력·가동률·수주 커버리지와 PPQ 후 매출 시차 추정
- 대형 고객의 내재화와 경쟁사 증설을 통한 가격 압력 독립 검증

출처: [삼성바이오로직스 2026년 2분기 실적](https://samsungbiologics.com/media/company-news/samsung-biologics-reports-second-quarter-2026-financial-results), [삼성바이오로직스 IR](https://samsungbiologics.com/ir/overview)

### 005380 — 현대자동차

**사실**

- 2026년 2분기 매출은 49.22조 원으로 1.9% 증가했지만 영업이익은 2.85조 원으로 20.8% 감소했다.
- 글로벌 도매판매는 99.2만 대로 6.9% 감소했다.
- 하이브리드 판매는 18.77만 대로 전체 판매의 18.9%를 차지했고, 전체 전동화 차량은 26.66만 대였다.
- 미국 도매판매는 0.9% 증가했고 미국 시장점유율은 5개 분기 연속 6%대를 유지했다.

**1차 추론**

- 하이브리드 믹스와 북미 점유율은 제품·유통 경쟁력을 지지하지만, 판매량 감소와 마진 하락은 해자 강화가 재무성과로 이어지지 않았음을 뜻한다.
- 자동차 제조·금융·환율·관세를 분리하지 않으면 증분 ROIC를 과대평가할 수 있다.

**잠정 Red Flag**

- `low_quality_growth: INVESTIGATE` — 가격·환율이 물량 감소를 가린 정도
- `incremental_roic_collapse: INVESTIGATE` — EV/소프트웨어/미국 생산 투자
- 생존성 FAIL 징후는 없으나 금융부문 자산과 보증을 포함해 재검증 필요

**다음 증거**

- 자동차와 금융부문 ROIC·현금흐름 분리
- 지역별 인센티브·관세·보증충당금 및 재고일수 추세 확인
- HEV/EV별 공헌이익과 미국 신공장 정상 가동 수익률 검증

출처: [현대자동차 2026년 2분기 경영실적](https://www.hyundai.com/worldwide/en/newsroom/detail/0000001234)

### 012450 — 한화에어로스페이스

**사실**

- 회사 IR 페이지에는 2026년 2분기 실적자료가 게시돼 있으며, 외부 집계 기준 연결 매출은 9.293조 원, 영업이익은 1.365조 원이다.
- 지상방산 수주잔고는 약 38.3조 원으로 보고됐고 K9·천무 수출계약이 가시성을 제공한다.
- 2026년 6월 대전 공장 폭발·화재로 5명이 사망했고, 회사는 국내 9개 생산시설의 안전점검을 위해 이틀간 가동을 중단했다.
- 2025년에는 대규모 유상증자 계획을 축소한 전력이 있고, 2026년에는 KAI 지분 추가 취득 등 자본배분 범위가 확대됐다.

**1차 추론**

- 빠른 납기, 현지화, 탄약·정비 결합은 유럽 고객의 전환비용과 반복주문 가능성을 높인다.
- 반면 연결실적에는 조선·시스템 등 자회사 실적이 크게 반영돼 지상방산 자체의 증분수익률을 분리해야 한다.

**잠정 Red Flag**

- `management_operational_integrity: INVESTIGATE` — 중대 안전사고의 원인·책임·재발방지
- `persistent_dilution: INVESTIGATE` — 과거 유상증자와 향후 투자재원
- `fatal_concentration: INVESTIGATE` — 국가·계약·선수금·수출허가 의존

**다음 증거**

- 공식 2분기 IR 원문과 DART 반기보고서에서 부문별 매출·이익·현금흐름 재검산
- 선수금·계약부채·운전자본·보증·지체상금과 수주잔고 취소조건 확인
- 안전사고 조사 결과와 이사회 감독·보상·재발방지 조치 추적

출처: [한화에어로스페이스 실적자료실](https://m.hanwhaaerospace.com/eng/ir/earning-release.do), [2025 사업보고서 자료실](https://m.hanwhaaerospace.com/kor/ir/finance/business-report.do), [대전 공장 사고와 가동중단 보도](https://www.reuters.com/world/asia-pacific/hanwha-aerospace-halt-south-korea-production-lines-two-days-after-deadly-fire-2026-06-04/)

### 010120 — LS ELECTRIC

**사실**

- 회사 발표 기준 2026년 2분기 매출은 1.577조 원, 영업이익은 1,785억 원으로 분기 최고치였다.
- 2분기 신규수주는 약 2.1조 원, 수주잔고는 약 7조 원으로 전분기 대비 약 1.4조 원 늘었다.
- 북미 매출과 초고압 변압기·배전 솔루션이 성장의 중심이었다.
- DART에 2026년 반기보고서가 게시돼 있어 원천 재무검증이 가능하다.

**1차 추론**

- AI 데이터센터와 노후 전력망 교체가 동시에 수요를 만들고, 제품 범위·납기·현지 서비스가 해자의 핵심일 가능성이 높다.
- 높은 수주 증가가 현금전환과 주당가치로 이어지는지 확인하기 전에는 단순 전력기기 사이클 수혜와 구조적 해자를 구분할 수 없다.

**잠정 Red Flag**

- `incremental_roic_collapse: INVESTIGATE` — 북미 증설과 정상화 마진
- `fatal_concentration: INVESTIGATE` — 데이터센터·북미·대형 고객 집중
- `external_capital_dependence: PASS` 여부는 반기 현금흐름·차입 검토 후 확정

**다음 증거**

- DART 반기보고서에서 영업현금흐름·재고·매출채권·파생상품·capex 추출
- 수주잔고의 취소조건·납기·가격조정 조항과 book-to-bill 지속성 확인
- Eaton·Schneider·GE Vernova 등과 납기·마진·기술 포지션 비교

출처: [LS ELECTRIC 2026년 2분기 공식 보도자료](https://www.ls-electric.com/media/press/401446?b_id=401450&b_lang=en&b_type=news&endDate=&keyword=&page=1&rows=10&startDate=), [LS ELECTRIC 2026년 IR 자료실](https://www.ls-electric.com/ko/company/invest/ir/), [DART 2026년 반기보고서 탐색](https://dart.fss.or.kr/navi/searchNavi.do?naviCode=A002&naviCrpCik=00105855&naviCrpNm=LS+ELECTRIC)

## Wave 01 결론

**의견**

- 현재 자료만으로 즉시 탈락시킬 기업은 없다.
- 사업 모멘텀의 강도는 `MSFT·AMZN·NOW·CRWD·000660·207940·010120`이 상대적으로 높다.
- `META`는 사업 모멘텀보다 AI capex의 현금회수 검증이, `005380`은 성장보다 마진·자본효율 검증이 우선이다.
- `012450`은 사업 기회가 크지만 경영·안전·희석·자본배분 Red Flag를 먼저 닫아야 하므로 단순 수주 성장으로 승격하지 않는다.

최종 점수와 A/B/WATCH/REJECT 우선순위는 연차·분기 공시의 현금흐름, 주식수, 약정, 고객집중 및 현재 가격까지 입력한 뒤 부여한다.

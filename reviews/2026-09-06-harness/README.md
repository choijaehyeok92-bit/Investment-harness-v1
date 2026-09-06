# 하네스 최적화 및 전 종목 재검토

기준일: **2026-09-06**. 대상: **93개 발행사**(미국 상장 51·한국 42). GOOG/GOOGL은 한 기업으로 계산했다. 원자료만 있던 24개 종목을 포함한다.

**구조 최적화와 93개 종목의 저장 증거 수준별 재검토를 완료했다. 93개 정밀 기업분석을 완성한 것은 아니다.** 현재 정책 완료 게이트 통과 1개(NOW), 부분 분석 34개, 예비 검토 58개다. 새 매수 승인은 없으며 WATCH 92개·REJECT 1개(NET)다. 자료 부족으로 WATCH인 경우를 긍정적 투자평가와 혼동하지 않는다.

## 무엇을 바꿨는가

| 문제 | 변경 | 결과 |
|---|---|---|
| main의 신규 raw와 Draft PR #10의 Astra/NOW가 분리 | 최초 main 492cd74 + 연구 9da08ac 통합 후 main 56a4090 추가 반영 | CRDO·TEM·TMDX까지 포함해 누락 방지 |
| 과거 50점·100점·서로 다른 판정 혼재 | 회사별 latest + 전 종목 registry | 현재 판단 하나와 역사적 기록을 구분 |
| raw만 있으면 분석 결손이 드러나지 않음 | 93개 모두 연구 상태·미완료 게이트 기록 | 완료 수를 과장하지 않음 |
| 단위·기간·범위·출처가 다른 숫자 혼합 | 원본 hash/pointer·관측·계산·판단 분리 | 재현 가능한 숫자만 계산 |
| 정책 항목 누락·unknown=0·점수로 veto 무시 | 스키마·의미 검증·회귀 테스트 | 잘못된 합계·매수 승인 차단 |

투자 철학, 100점 배점, 9개 veto, 포지션 규칙은 변경하지 않았다. [새 구조 사용법](../../docs/HARNESS_V2.md), [현재 인덱스](../../registry/companies.json), [원본 보존 기준](../../harness/baseline-lock.json)을 함께 저장했다.

## 투자 판단에서 달라진 점

1. **기업 품질과 매수 가격을 더 엄격하게 분리했다.** ISRG·TSM·NVDA 등 기존 첫 6개 항목의 품질 의견은 보존하지만, 현금모델·기대차 게이트가 미완료인 종목의 과거 100점은 현재 확정 총점으로 사용하지 않는다. 숫자 보류는 사업이 갑자기 나빠졌다는 뜻이 아니다.
2. **성장과 현금 회수를 동시에 확인했다.** APR·파마리서치·알테오젠은 매출/이익 증가와 OCF 감소가 공존한다. 해외 확장·계약 정산 시점일 수 있으므로 즉시 부정 판정하지 않지만, 다음 단계는 회계 이익 외삽이 아니라 재고·채권·수취권 검증이다.
3. **AMZN의 현금 회복을 기본값으로 가정하지 않는다.** 동기 차감 TTM 보고 FCF 프록시는 -76.04억 달러, SBC·금융리스/의무 원금까지 차감한 보수적 owner proxy는 -288.25억 달러다. AWS 성장과 AI 투자 회수의 관계가 핵심이다. 투자자산 평가이익을 반복 영업현금으로 자본화하지 않는다. [계산·출처 메모](source-checks.md)
4. **메모리 초호황을 정상 이익으로 고정하지 않는다.** SK하이닉스·MU·삼성전자는 가격·물량·믹스·수율과 Capex의 전체 사이클을 분리해야 한다. SK하이닉스의 큰 Q2 숫자는 공식 IR에서도 확인했으므로 크기만으로 추출 오류라고 보지 않는다. [공식 Q2 발표](https://news.skhynix.com/en/q2-2026-business-results/)
5. **사업 구조별 모형을 강제한다.** 현대차는 자동차/금융, MELI는 커머스/금융·고객자금, 한화에어로·두산에너빌리티는 모회사 귀속 SOTP, 바이오 라이선스는 계약 로열티 rNPV, ASTS·RKLB는 자금소진·단계별 성공·희석 모형이 필요하다.
6. **출처 충돌과 시점을 바로잡았다.** MSFT FY26 투자손익의 OpenAI/Anthropic 표현, MSFT 부문 재분류, 삼성바이오 분할 후 계속영업·주식 수, APR IFRS1118 재작성, 받은 보증과 제공한 보증, 발표된 인수와 종결 거래를 구분했다. [MSFT 공식 FY26 발표](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast)

7. **작업 중 추가된 3개 raw 종목도 포함했다.** CRDO는 Q1 FY27 매출 114.7% 증가와 GAAP 마진 하락·고객 집중이 공존한다. TEM은 Q2 순이익 흑자에도 영업손실이 확대되어 영업 흑자 전환으로 볼 수 없다. TMDX는 H1 현금흐름 감소·항공 리스 부담과 미해소 재고 내부통제 취약성이 핵심 추가 게이트다. [CRDO 공식 발표](https://investors.credosemi.com/news-events/news/news-details/2026/Credo-Technology-Group-Holding-Ltd-Reports-First-Quarter-of-Fiscal-Year-2027-Financial-Results/), [TEM 공식 발표](https://investors.tempus.com/news-releases/news-release-details/tempus-reports-second-quarter-2026-results/), [TMDX 공식 발표](https://investors.transmedics.com/news-releases/news-release-details/transmedics-reports-second-quarter-2026-financial-results)

## 다음 조사에서 먼저 볼 대상

P1은 **조사 우선순위**이며 매수 등급이 아니다. 동일 그룹 내부 순위나 포트폴리오 비중을 뜻하지 않는다.

| 조사 목적 | 대상 | 통과에 필요한 핵심 증거 |
|---|---|---|
| 강한 사업 가설의 주당 가치 확인 | ISRG, ANET, MSFT | 현금·보상·투자 브리지, 고객/절차 지속성, 가격 역산 |
| 기존 기대차의 실현 조건 확인 | NOW | 유기적 성장, 인수 수익, SBC 개선 및 4개 INVESTIGATE 해소 |
| 성장과 현금 괴리 해소 | AMZN, 214450 파마리서치, 278470 APR, VRT | Capex·재고·채권·선수금의 원인과 회수 기간 |
| 장기 계약·제품 현금의 수명 검증 | 267260 HD현대일렉트릭, 207940 삼성바이오, LLY, VRTX | 수주/제품별 현금·투입자본·인수/특허·가격 기대 |

NOW는 기존 72/100을 유지한다. 2026-09-04 기준가격 141.26달러에 대한 기존 현금대체 SBC 모형의 Bear/Base/Bull은 58.49/188.18/409.78달러다. Base는 매출 연 16%, 만기 owner 마진 24%, 만기 P/FCF 23배, 9% 요구수익률이라는 **가정**에 의존한다. 따라서 값의 할인만으로 매수를 승인하지 않는다. [NOW 전체 분석](../../companies/NOW/analyses/2026-09-06/thesis.ko.md), [재현 모형](../../companies/NOW/valuation.json)

## 검증과 한계

- 원자료 **25개**와 투자 정책 **8개** 파일의 SHA256 불변 확인.
- 원자료 관측 **2,298개**의 파일·JSON pointer·값 일치 확인.
- 신규 파생지표 **12개**, 날짜별 산출물 **470개** 재현 확인.
- 핵심 의미 검증 **18개** 및 기존 출력·Astra 20개 현금모형·NOW 역산/IRR 검증 통과.
- 모든 종목에 8개 평가 항목, 9개 veto, 10개 반론, 영구손실·반증·증액/축소 조건을 기록. 증거가 부족한 항목은 점수·시나리오를 null로 남김.

24개 raw 종목에 새 분석 기록을 만들었지만 그 전부를 정밀 완료로 표시하지 않았다. 원문 PDF 전체 재실사, 93개 종목의 동시 가격 검증, 모든 회사의 10년 현금모형을 수행한 것은 아니다. 나머지 **92개 종목의 완전한 정밀분석은 미완료**다. 각 종목별 미완료 이유는 아래 표와 개별 문서에 연결되어 있다.

단일 분석자의 재검토이므로 독립 레드팀 합의가 아니다. 계산·출처 연결 검증은 미래 가정의 정확성을 보증하지 않는다. 실제 보유·세금·위험예산이 제공되지 않았으므로 포지션 변경을 실행하지 않았다.

## 전 종목 결과

품질은 앞의 6개 항목 /75이며 100점 총계와 다르다. `보류`는 0점이 아니다. 각 종목 링크에서 수치·반대 근거·다음 검증 조건을 확인할 수 있다.

| 종목 | 현재 상태 | 품질 /75 · 총점 /100 | 판정 | 우선순위 · 다음 증거 |
|---|---|---|---|---|
| [000100 · Yuhan Corporation](../../companies/000100/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 반복 로열티와 마일스톤 분리·rNPV |
| [000270 · Kia](../../companies/000270/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 자동차 정상화 마진·판매 금융 노출·현금 |
| [000660 · SK Hynix](../../companies/000660/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P2 · ASP/물량/믹스·세대별 수율·전체 사이클 Capex·증자 및 환매 실행 후 주식 수 |
| [003230 · Samyang Foods](../../companies/003230/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 지역 sell-through·증설 수율·운전자본 |
| [005380 · Hyundai Motor](../../companies/005380/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P2 · 자동차/금융 SOTP, 금융부문 규제자본·신용손실, 우선주 및 지분가치 중복 제거 |
| [005930 · Samsung Electronics](../../companies/005930/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 58 · 보류 | WATCH | P2 · HBM 물량·ASP·수율 효과를 분리하고 DS 정상화 FCF, 설비투자와 우선주를 포함한 주당 현금흐름을 연결한다. |
| [006400 · Samsung SDI](../../companies/006400/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 합작자금·가동률·고객 계약·현금 runway |
| [009150 · Samsung Electro-Mechanics](../../companies/009150/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 전장/AI 믹스·가동률·사이클 FCF |
| [009540 · HD Korea Shipbuilding & Offshore Engineering](../../companies/009540/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 지분별 SOTP·배당 유입·보증·프로젝트 현금 |
| [010120 · LS ELECTRIC](../../companies/010120/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 가격/물량·수주 수익성·운전자본 |
| [011070 · LG Innotek](../../companies/011070/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 고객별 물량·신제품 ASP·정상화 Capex |
| [012330 · Hyundai Mobis](../../companies/012330/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · AS/모듈/전동화 현금 분리·지분 자본배분 |
| [012450 · Hanwha Aerospace](../../companies/012450/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P2 · 모회사 제한현금·차입·보증·추가 투자약정을 지분별 SOTP와 연결하고, 안전조치 및 프로젝트별 현금전환을 검증한다. |
| [034020 · Doosan Enerbility](../../companies/034020/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P2 · 지분별 SOTP·자금 제한·보증, 프로젝트별 계약상 책임과 현금 전환 |
| [035420 · NAVER](../../companies/035420/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P2 · 유기적/인수 성장 구분, 제3자 배정 조건·주식 수·AI 회수, 검색광고와 커머스별 현금 |
| [035720 · Kakao](../../companies/035720/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 본사 현금·자회사 SOTP·AI 수익화 |
| [042660 · Hanwha Ocean](../../companies/042660/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 선박별 손익·선수금·환헤지·현금 |
| [042700 · Hanmi Semiconductor](../../companies/042700/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P2 · 고객·기술별 수주, OCF 원문·재고·채권, 투자 실행과 기술 세대별 점유율 |
| [047810 · Korea Aerospace Industries](../../companies/047810/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 수출 계약 확정·개발 현금·보증 |
| [058470 · LEENO Industrial](../../companies/058470/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 제품별 고객 유지·신규 공장 ROIC |
| [064350 · Hyundai Rotem](../../companies/064350/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 방산/철도 현금 분리·수주 취소·보증 |
| [068270 · Celltrion](../../companies/068270/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 제품별 실수요·재고 회전·현금 수익 |
| [079550 · LIG Nex1](../../companies/079550/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 양산/개발별 현금·계약조건·보증 |
| [128940 · Hanmi Pharmaceutical](../../companies/128940/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 국내 현금원·계약별 로열티·rNPV |
| [141080 · LigaChem Biosciences](../../companies/141080/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 계약별 자금·단계 성공률·희석 runway |
| [145020 · Hugel](../../companies/145020/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 국가별 판매허가·sell-through·현금 |
| [161890 · Kolmar Korea](../../companies/161890/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 가동률·제품 믹스·모회사 현금 ROIC |
| [192820 · Cosmax](../../companies/192820/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 현지 수익성·운전자본·고객 집중 |
| [196170 · Alteogen](../../companies/196170/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P2 · 계약별 로열티율/잔존권리·성공확률·확정 현금, 세금·기술 분쟁·희석 |
| [207940 · Samsung Biologics](../../companies/207940/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P1 · 계속영업 OCF/Capex·주식분할/분할 기준·인수 후 투자 및 계약 잔고 수익성 |
| [214450 · PharmaResearch](../../companies/214450/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P1 · 채권 회수·유통 sell-through·Capex/무형·주식 수, 시장별 허가와 가격 지속성 |
| [257720 · SILICON2](../../companies/257720/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 브랜드 유지·재고연령·현금 회수 |
| [259960 · Krafton](../../companies/259960/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 기존 IP 유지·신작 유료 코호트·투자 회수 |
| [267260 · HD Hyundai Electric](../../companies/267260/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P1 · 수주 가격/취소/선수금, 생산 증설 후 운전자본, 10% 요구수익률 역산 |
| [271560 · Orion](../../companies/271560/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 국가별 유기 성장·현금·자본배분 |
| [278470 · APR](../../companies/278470/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P1 · 채널별 sell-through·CAC 회수·재고연령·IFRS1118 동일 기준, 주당 현금흐름 |
| [298040 · Hyosung Heavy Industries](../../companies/298040/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 전력/건설 SOTP·보증·수주 현금 |
| [329180 · HD Hyundai Heavy Industries](../../companies/329180/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 선가/원가·현금 전환·유지 Capex |
| [352820 · HYBE](../../companies/352820/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 아티스트별 현금·팬 유지·계약 권리 |
| [373220 · LG Energy Solution](../../companies/373220/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 가동률·세액공제 제외 현금·Capex 의무 |
| [402340 · SK Square](../../companies/402340/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 지분별 순자산·본사 현금·환원 실행 |
| [454910 · Doosan Robotics](../../companies/454910/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 판매대수별 단위 손익·서비스·현금 runway |
| [ADBE · Adobe](../../companies/ADBE/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 유료 AI 순증·갱신·SBC 이후 주당 FCF |
| [AMAT · Applied Materials](../../companies/AMAT/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 지역별 수주·서비스 현금·정상화 투자수익 |
| [AMD · Advanced Micro Devices](../../companies/AMD/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 독립 고객 AI 수익·믹스·SBC·재고 |
| [AMZN · Amazon](../../companies/AMZN/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P1 · AWS 사용률·투자 회수, 유지/성장 Capex 근거, Anthropic 비현금이익 제거, 만기별 약정과 주당 현금회복 브리지 |
| [ANET · Arista Networks](../../companies/ANET/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P1 · 최종고객별 매출·매입약정, H1 SBC/총발행/환매, 최신 가격과 10년 현금흐름 역산 |
| [APP · AppLovin](../../companies/APP/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 독립 ROAS 검증·고객 집중·데이터 권리 |
| [ASTS · AST SpaceMobile](../../companies/ASTS/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P3 · 분기별 현금 runway·발사 성공·서비스 계약 단가/수익배분·규제 권리 |
| [AVGO · Broadcom](../../companies/AVGO/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 61 · 보류 | WATCH | P2 · Q3 10-Q의 공급·클라우드·보증 약정과 최종고객 노출을 확인하고 SBC 이후 주당 FCF로 10년 가격 기대치를 재작성한다. |
| [AXON · Axon Enterprise](../../companies/AXON/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 57 · 보류 | WATCH | P2 · SBC를 현금대체비용으로 차감하고 미래 동일 보상의 희석을 중복 적용하지 않는 모형, 또는 총발행·환매 재원을 명시한 모형으로 대조한다. |
| [BSX · Boston Scientific](../../companies/BSX/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 제품별 유기 성장·리콜·인수 후 현금수익 |
| [CEG · Constellation Energy](../../companies/CEG/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 계약 가격/만기·유지 Capex·차입 |
| [CRM · Salesforce](../../companies/CRM/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · Agentforce 유기 수익·갱신·SBC 이후 FCF |
| [CRWD · CrowdStrike](../../companies/CRWD/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 고객 이탈·할인·보상 현금·owner FCF |
| [DDOG · Datadog](../../companies/DDOG/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 60 · 보류 | WATCH | P2 · 큰 AI 고객의 최적화 영향을 분리한 성장, 총발행·환매 주식수와 주당 owner-FCF를 4개 분기 추적한다. |
| [DHR · Danaher](../../companies/DHR/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 주문 소모품/장비 구분·인수 ROIC·현금 |
| [ETN · Eaton](../../companies/ETN/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 백로그 취소권·가격/물량·정상화 마진 |
| [GEV · GE Vernova](../../companies/GEV/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 사업별 현금·보증충당·수주 수익성 |
| [GOOGL · Alphabet](../../companies/GOOGL/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 59 · 보류 | WATCH | P2 · 미국 9% 허들을 기준으로 동일 자본비용 민감도를 제시하고 검색 단위수익, AI 이용률과 Capex 이후 FCF/주로 투자회수를 입증한다. |
| [HUBS · HubSpot](../../companies/HUBS/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 고객 코호트 유지·단위 현금·희석 |
| [INTU · Intuit](../../companies/INTU/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 제품별 유지·가격·Mailchimp 자본 회수 |
| [ISRG · Intuitive Surgical](../../companies/ISRG/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 68 · 보류 | WATCH | P1 · 환매 재원을 포함한 주당 현금흐름을 완성하고, 절차 성장·경쟁·리콜 위험 변화 없이 충분한 할인 또는 실적 상향이 발생하는지 확인한다. |
| [KLAC · KLA](../../companies/KLAC/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 서비스 반복성·정상화 Capex와 주당 현금 |
| [LLY · Eli Lilly](../../companies/LLY/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P1 · 제품별 순약가·환자지속·공급 Capex·인수 현금/차입·특허별 rNPV |
| [LRCX · Lam Research](../../companies/LRCX/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 공정 점유·서비스·사이클 평균 FCF |
| [MA · Mastercard](../../companies/MA/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 고객 인센티브 후 순수익·국경간 믹스·환매 재원 |
| [META · Meta Platforms](../../companies/META/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 광고 단위수익·Capex/리스·주당 owner FCF |
| [MPWR · Monolithic Power Systems](../../companies/MPWR/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 디자인윈 지속·고객 노출·재고·보상비용 |
| [MSFT · Microsoft](../../companies/MSFT/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P1 · 두 raw 파일 병합 보존, 리스 포함 투자·SBC·OpenAI 손익 조정, 재분류 부문별 투자효율 |
| [MU · Micron Technology](../../companies/MU/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P2 · HBM·DRAM·NAND별 중간 사이클 이익과 정부지원 조건, 공장 가동률·주식 수 |
| [NET · Cloudflare](../../companies/NET/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 56 · 보류 | REJECT | P2 · 총마진·고객 유지와 SBC 이후 FCF/주 개선, 완전희석 주식수를 포함한 현실적 성장 범위 및 지배구조를 확인한다. |
| [NOW · ServiceNow](../../companies/NOW/analyses/2026-09-06/thesis.ko.md) | 정밀 완료 | 56 · 72 | WATCH | P1 · 두 차례 연속 분기에서 선반영 제외 cRPO·구독 유기성 확인 및 AI 고객 확장 증거 확보. / TTM OCF-capex-SBC 주당 성장 재가속, SBC/매출 하락 경로와 2029년10% 미만 목표에 대한 이행 확인. / Armis/Veza 현금수익·통합비용/CP 차환 확인으로 해당 INVESTIGATE 해소. / 검증한 보수적 가치 대비 충분한 할인과 9% 초과 수익률; 가격 하락만으로 증액하지 않는다. |
| [NVDA · NVIDIA](../../companies/NVDA/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 63 · 보류 | WATCH | P2 · 공급·클라우드 약정 만기/취소권, 보증 발동·회수 조건과 투자관계 고객 매출을 대조하고 고객 최종 현금창출로 수요를 검증한다. |
| [ORCL · Oracle](../../companies/ORCL/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 취소권별 RPO·설비/리스·만기별 현금 |
| [PANW · Palo Alto Networks](../../companies/PANW/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 플랫폼 순증 현금·갱신·SBC 이후 수익 |
| [PLTR · Palantir Technologies](../../companies/PLTR/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P2 · GAAP OCF→조정 FCF→SBC 브리지·총발행/환매·정부집중, 10년 가격 역산 |
| [PWR · Quanta Services](../../companies/PWR/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 백로그 현금전환·인수 회수·운전자본 |
| [REGN · Regeneron Pharmaceuticals](../../companies/REGN/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 제품 수명별 현금·파트너 배분·rNPV |
| [RKLB · Rocket Lab](../../companies/RKLB/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P3 · Iridium 거래 조건/종결 pro forma·bridge 만기·Neutron 현금 및 성공 단계별 시나리오 |
| [SNOW · Snowflake](../../companies/SNOW/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 소비 코호트·유기 매출·gross dilution·현금 |
| [SYK · Stryker](../../companies/SYK/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 절차·반복 소모품·인수 후 ROIC |
| [TMO · Thermo Fisher Scientific](../../companies/TMO/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 유기 주문·소모품·현금 ROIC |
| [TSLA · Tesla](../../companies/TSLA/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 자동차/에너지 현금 분리·자율주행 독립 증거 |
| [TTD · The Trade Desk](../../companies/TTD/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 수수료·고객 유지·실측 광고성과·SBC |
| [V · Visa](../../companies/V/analyses/2026-09-06/thesis.ko.md) | 예비 검토 | 보류 · 보류 | WATCH | P3 · 인센티브 후 순수익·물량·환매 재원 |
| [VRT · Vertiv](../../companies/VRT/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P1 · OCF 운전자본 브리지·유기적 주문·UIG 대금 및 pro forma·유지 Capex |
| [VRTX · Vertex Pharmaceuticals](../../companies/VRTX/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P1 · CF 제품 수명·로열티, Crinetics 종결 후 대차대조표·대금·파이프라인 확률 |
| [MELI · MercadoLibre](../../companies/MELI/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P2 · 커머스/결제/대출 SOTP, 고객자금 분리·빈티지 손실·규제자본·FX, 조정 FCF 조정 항목 |
| [TSM · Taiwan Semiconductor (ADR)](../../companies/TSM/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 66 · 보류 | WATCH | P2 · 배당의 현금 시점과 정상화 Capex를 포함한 9% 허들 역산, 해외 생산의 실질 대체가능성과 고객집중을 검증한다. |
| [CRDO · Credo Technology Group](../../companies/CRDO/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P2 · 최종고객별 계약·AEC/광학 수익성·OCF와 SBC/희석·현금 감소 브리지·가격 역산 |
| [TEM · Tempus AI](../../companies/TEM/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P3 · 영업→순이익 조정·OCF runway·수가/채권·Personalis 종결 후 주식 수·전환 조건·진단/데이터 분리 |
| [TMDX · TransMedics Group](../../companies/TMDX/analyses/2026-09-06/thesis.ko.md) | 부분 분석 | 보류 · 보류 | WATCH | P2 · 재고 통제 개선 운영/시험 증거·소송·항공 금융리스/Capex·장기별 단위수익·다년 현금모형 |

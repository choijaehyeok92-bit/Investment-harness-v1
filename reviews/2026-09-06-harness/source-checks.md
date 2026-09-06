# 선별 공식 자료 교차검증 — 2026-09-06

이번 실행은 모든 PDF를 새로 실사한 작업이 아니다. 아래는 중요한 수치·출처 충돌에 대해 수행한 선별 확인이며, 나머지 관측은 저장 원자료의 보고 주장으로 표시했다. 웹 조회시각은 2026-09-06이고 발행일·대상 회계기간은 각각 다르다.

| 종목 | 확인한 내용 | 공식 출처 |
|---|---|---|
| AMZN | Q2 2026 실적, AWS·설비투자·투자이익 구분 | [Amazon Q2 발표](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/), [SEC Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000024/amzn-20260630xex991.htm) |
| 000660 | 7월 29일 Q2 발표: 매출 79.3187조·영업이익 60.5426조 원. 큰 숫자만으로 추출 오류로 판정하지 않음 | [SK hynix Q2 IR](https://news.skhynix.com/en/q2-2026-business-results/) |
| MSFT | FY26 매출·영업이익 및 비영업 투자손익의 대상은 OpenAI. 과거 스크리닝의 Anthropic 표현을 현재 해석에서 정정 | [Microsoft FY26 Q4 발표](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast) |
| PLTR | Q2 GAAP 매출·영업이익과 조정 FCF를 구별 | [SEC Q2 발표](https://www.sec.gov/Archives/edgar/data/1321655/000132165526000039/a2026q2ex991pressrelease.htm) |
| RKLB | Q2 실적과 Iridium 인수 발표. 미종결 거래에 대한 pro forma 필요 | [Rocket Lab Q2](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-second-quarter-2026-financial-results-posts), [Iridium 거래 발표](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) |
| LLY | Q2 매출 성장 및 2026 가이던스가 확정 실적과 다름을 확인 | [Lilly Q2 발표](https://investor.lilly.com/news-releases/news-release-details/lilly-reports-second-quarter-2026-financial-results-raises-full) |
| MELI | Q2 2026 회사 발표와 재무 원자료 연결. 금융소득 포함 매출과 조정 FCF를 일반 소매 현금흐름으로 해석하지 않음 | [MercadoLibre 공식 발표 목록](https://investor.mercadolibre.com/news-and-events) |
| CRDO | 9월 1일 발표한 Q1 FY27 매출 479.0M달러와 GAAP 총마진 64.5% | [Credo 공식 발표](https://investors.credosemi.com/news-events/news/news-details/2026/Credo-Technology-Group-Holding-Ltd-Reports-First-Quarter-of-Fiscal-Year-2027-Financial-Results/) |
| TEM | Q2 실적 및 Personalis 미종결 거래 | [Tempus 공식 발표](https://investors.tempus.com/news-releases/news-release-details/tempus-reports-second-quarter-2026-results/) |
| TMDX | Q2 매출 증가와 영업이익 감소. 통제 취약성은 저장 10-Q p.38 추출 주장으로 별도 연결 | [TransMedics 공식 발표](https://investors.transmedics.com/news-releases/news-release-details/transmedics-reports-second-quarter-2026-financial-results) |

AMZN 현금 계산의 추가 세부값은 앞선 첨부 10-K·Q2 10-Q 읽기에서 확인한 FY2025 / H1 2025 / H1 2026 비교열이다. TTM OCF 139,514+71,419−49,530=161,403M달러; PPE 지출 131,819+98,411−57,202=173,028M; PPE 처분 등 유입 3,499+2,101−1,579=4,021M. 따라서 순현금 PPE 169,007M과 보고 FCF 프록시 -7,604M이다. TTM SBC 19,467+10,070−10,223=19,314M, 금융리스 원금 1,557+863−821=1,599M, 금융의무 원금 328+174−194=308M. 추가 차감 후 보수적 owner proxy -28,825M은 정확한 유지 Capex/법적 배당가능 현금의 측정치가 아니며 추가 비현금 자산취득을 또 차감하지 않는다.

원자료 JSON의 SHA256과 모든 관측의 pointer 검사는 저장 파일과의 일치를 보장한다. 원문의 공시 정확성·감사의견·미래 전망을 인증하지 않는다. 하네스는 단위·기간·범위가 불명확하면 이를 결손으로 남기며 임의로 보완하지 않는다.

# 2026-09-08 Macro Risk-Budget Overlay

이 폴더는 2026-09-08 현재 글로벌 매크로 환경과 향후 6개월(2027-03-08까지) 시나리오를 Investment Harness에 저장한 additive-only 연구 체크포인트다.

## 저장 파일

- `source-manifest.json`: 공식 통계·중앙은행·Reuters 출처 목록
- `raw-data.json`: 검증된 현재 관측값과 시장의 point-in-time expectation
- `assessment.json`: 거시 regime, 6개월 시나리오 확률, 포트폴리오 risk-budget 적용 규칙, 재평가 트리거
- `thesis.ko.md`: 사람이 읽는 한글 논지

## 핵심 regime

`MODERATE_TO_STRONG_GROWTH_STICKY_INFLATION_HIGHER_FOR_LONGER_HIGH_GEOPOLITICAL_VOLATILITY`

핵심 배경은 다음과 같다.

- 미국: 경기침체보다 확장 지속 쪽 증거가 우세하나 PCE 물가가 높고 Fed 내부 긴축 압력이 존재
- 장기금리: 미국 10년물이 5%에 접근하고 재정·실질금리 요인이 term premium을 지지
- 에너지: Brent 약 $98대와 중동 물류차질이 6개월 전망의 최대 비선형 위험
- 유럽: 성장 개선과 에너지 인플레이션 재상승이 동시에 진행
- 일본: BOJ 정상화와 엔 carry unwind가 글로벌 유동성 위험
- 한국: AI/반도체 수출 호황이 성장의 강한 순풍이나 기준금리 3.0%와 에너지 수입 리스크가 상쇄요인
- 중국: high-tech 수출은 강하나 내수/부동산과 무역마찰은 별도 위험

## 6개월 주관적 시나리오 가중치

- Base — 성장 유지 + 끈적한 물가: 50%
- Inflation / energy shock: 25%
- Disinflationary soft landing: 15%
- Growth / credit shock: 10%

시나리오 가중치는 관측 사실이 아니라 투자 의사결정용 opinion이다.

## Harness 정책 경계

`AGENTS.md`의 원칙을 따른다.

- 매크로 전망은 기업의 100점 quality score를 직접 바꾸지 않는다.
- 매크로는 포트폴리오 risk budget, valuation stress, scenario severity, 추가 조사 우선순위에만 반영한다.
- 공식 통계와 중앙은행 자료를 우선하고, 시장가격·정책 기대는 Reuters 등 secondary source로 별도 분리한다.
- 미래 데이터가 나오면 새 날짜의 매크로 체크포인트를 추가하며 이 파일을 사후 수정해 미래 정보를 끼워 넣지 않는다.

## Repository safety

이번 체크포인트는 `reviews/2026-09-08-macro/` 아래 신규 파일만 추가한다. `companies/**`, `registry/**`, `reviews/latest.json`, `harness/baseline-lock.json`, frozen deterministic outputs를 변경하지 않는다.

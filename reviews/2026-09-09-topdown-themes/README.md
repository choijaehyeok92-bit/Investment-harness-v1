# 2026-09-09 Five-Year Top-Down Sector & Theme Overlay

이 폴더는 2026-09-09 현재의 매크로 환경을 바탕으로 향후 5년(2031-09-09까지) 시장 주도 섹터와 테마를 정리한 additive-only 연구 체크포인트다.

## 저장 파일

- `source-manifest.json` — IEA, SEMI, NATO, Gartner, IFR 및 내부 매크로 체크포인트 출처
- `theme-map.json` — Top 10 테마, preferred subsegment, 시간대별 leadership phase, 기존 하네스 종목의 예시 노출
- `assessment.json` — 전략적 해석, 상대 매력도, bottom-up 필터, 반증조건, 포트폴리오 적용 규칙
- `thesis.ko.md` — 사람이 읽는 한글 장기 탑다운 논지

## 핵심 프레임

향후 5년의 주도권은 다음 방향으로 이동할 가능성이 높다고 본다.

`AI Compute → Electricity → Grid/Cooling/Data Center → Automation → Productivity`

병렬 구조는 다음과 같다.

`Geopolitics → Defence / Cybersecurity / Supply-chain localization`

## Top 5 우선 테마

1. 전력망·전력기기·전기 인프라
2. AI 반도체·HBM·첨단패키징·반도체 장비
3. 데이터센터 전력·냉각·네트워킹
4. 국방·항공우주·드론·미사일
5. 사이버보안·AI 보안

## 정책 경계

이 체크포인트는 `AGENTS.md`의 분리 원칙을 따른다.

- 매크로·테마 전망은 회사의 100점 quality score를 직접 바꾸지 않는다.
- 테마 순위는 매수 승인이 아니다.
- 테마는 research priority, scenario design, valuation stress, portfolio factor concentration 판단에만 사용한다.
- 최종 종목판정은 `structural demand → supply/share → moat → incremental ROIC/FCF per share → market expectations → valuation` 순서를 통과해야 한다.

## Source discipline

- IEA·NATO는 국제기구/공식 정책 자료
- SEMI·IFR는 산업단체 전망/통계
- Gartner는 시장조사기관의 공개 요약·전망
- 산업 전망치는 realized fact가 아니라 forecast로 유지
- 이번 persistence 단계에서 재검증하지 않은 이전 답변의 일부 정량 추정치는 fact로 승격하지 않음

## Repository safety

이번 체크포인트는 `reviews/2026-09-09-topdown-themes/` 아래 신규 파일만 추가한다.

다음 파일은 변경하지 않는다.

- `companies/**`
- `registry/**`
- `reviews/latest.json`
- `harness/baseline-lock.json`
- frozen / deterministic current-run outputs

따라서 이 병합은 현재 종목 authority나 기존 company score를 변경하지 않는다.

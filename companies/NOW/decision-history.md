# NOW 판정 이력

| 날짜/순서 | 범위 | 점수 | 판정 | 변경 사유 |
|---|---|---:|---|---|
| 2026-09-05 Astra 과거 스냅샷 | 50점 스크리닝 | 42/50 | WATCH / INVESTIGATE | 현금흐름 bridge·AI·SBC 검증 미완성 |
| 2026-09-05 NOW 신규 정밀분석, 위 기록 후 | 100점 기업분석 | 72/100 | WATCH / INVESTIGATE; NONE | 첨부6개로 역사적 OCF→조정FCF→SBC bridge 확인, 9% 역산/3시나리오 완료. 미래 정상화·인수ROIC·AI 단위경제성은 미확인 |

42/50→72/100은 점수 상승을 뜻하지 않는다. 기존 Astra 보고서의40개 범위/50개 미심사 수치는 당시 스냅샷으로 보존한다. NOW는 이미40개에 포함되어 있었으며 이번 단계에서 최초의 companies/NOW 정밀 패키지가 추가됐다. 기존10개 기업 패키지에 NOW가 추가되어 총11개 경로가 된다.

다음 점검: Q3 2026 공식 공시가 나오면 Q2 선반영 해소, cRPO·고객 확장, SBC/주당 현금, 인수 현금수익과 CP 차환을 갱신한다. 발표일은 확인되지 않아 고정하지 않는다. 자동 점검 작업이나 거래는 생성하지 않았다.

## 재개 시 읽을 파일

1. decision.json → hard-veto.json → thesis.md
2. financial-inputs.json → valuation.json → sources.json
3. evidence.jsonl와 red-team.md
4. 과거42/50 비교가 필요할 때만 reviews/2026-09-05-astra/screen-reassessments.jsonl

검증: 저장소 스키마/합계/9개 veto/판정 및 valuation_model.py --check. 근거가 없는 gate는 검증 통과로 해소된 것으로 간주하지 않는다.

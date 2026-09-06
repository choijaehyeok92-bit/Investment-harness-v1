> 현재 연구 상태: [2026-09-05 Astra 재평가](../../reviews/2026-09-05-astra/README.md). 40개 기존 판단 재심사, 50개 예비후보는 미심사. 과거 스크리닝 점수·판정을 현재 승인으로 사용하지 마세요.

# 2026-09 미국·한국 주식 스크리닝

## 실행 개요

- 기준일: 2026-09-04
- 목적: 하네스의 장기 아웃라이어 투자 원칙에 맞는 미국·한국 기업을 독립 퍼널로 선별
- 현재 단계: Stage 1 Wave 01~02 전용모형·Red Team 체크포인트 완료
- 예비 후보: 미국 40개, 한국 40개
- 잠정 부분점수: 미국 10개, 한국 10개 — 기대차를 제외한 44점 기준
- 신규 50점 총점 완료: 미국 10개, 한국 10개
- 전용모형 완료: SK하이닉스(사이클 FCF), 현대자동차(연결 owner earnings), 알테오젠(계약 확률트리)
- Red Team: 20개 완료 — `PASS` 2, `REVISE` 16, `REJECT` 2
- Hard Veto: CRWD 가격 `FAIL` 유지, 크래프톤 경영진 신뢰성 `FAIL` 신규 판정
- 최신 상태: `WATCH` 18개, `SCREEN_OUT` 2개, `SCREEN_IN` 0개
- 기존 정밀분석 재사용: 6개
- 최근 공시·IR 1차 판독: 미국 10개, 한국 10개

이번 저장은 공통 모형을 적용할 수 없었던 세 종목의 전용 가치평가와 20개 전 종목의 반증 중심 Red Team을 추가한 **Stage 1 후속 체크포인트**다. 총점은 20개 모두 완료했지만, 열린 `INVESTIGATE` 또는 `FAIL` 때문에 어떤 종목도 `SCREEN_IN`하지 않았다. 이전 기대차 파일은 역사적 스냅샷으로 유지하고 `stage1-decisions-wave-01-02.jsonl`을 최신 결정의 단일 기준으로 둔다.

## 파일

- `../harness-v1.0.md`: 50점 스코어, Hard Red Flag, 증거 게이트
- `universe.csv`: 미국·한국 예비 후보 80개와 조사 상태
- `prior-analysis.csv`: 저장소에 이미 존재하는 정밀분석 판정
- `research-queue.md`: 1차·2차 조사 순서와 수집 항목
- `evidence-wave-01.md`: 첫 10개 기업의 사실·추론·Red Flag·다음 질문
- `evidence-wave-02.md`: 두 번째 10개 기업의 사실·추론·Red Flag·다음 질문
- `financial-normalization-wave-01-02.csv`: 보고 수치 조정, 현금흐름·희석·집중도, 2026-09-04 가격 기준점
- `provisional-scorecards-wave-01-02.jsonl`: 20개 기업의 축별 부분점수·근거·반대근거·신뢰도
- `provisional-scorecards-wave-01-02.md`: 잠정 점수 요약, 정규화 판독과 다음 승격 게이트
- `valuation-inputs-wave-01-02.csv`: 희석주식수, 지분가치, 순현금·순부채, TTM FCF, Capex와 정상화 시작 마진
- `reverse-expectations-wave-01-02.csv`: 공통 역산식, Bear/Base/Bull, 기대차 점수와 총점
- `expectation-overlays-wave-01-02.jsonl`: 기존 44점 스코어카드에 결합할 기계 판독 가능한 기대차·판정 오버레이
- `reverse-expectations-wave-01-02.md`: 한글 판독, 순위, Hard Veto, 영구손실 사례와 다음 체크포인트
- `special-models-wave-01-02.jsonl`: SK하이닉스·현대자동차·알테오젠의 기업별 전용 모형
- `red-team-wave-01-02.jsonl`: 20개 기업의 반대논리·숨은 가정·반증 조건·판정
- `checkpoint-03-custom-models-and-red-team.md`: 후속 체크포인트 한글 보고서와 조건부 심층조사 큐
- `stage1-decisions-wave-01-02.jsonl`: Red Team·Hard Veto를 반영한 최신 20개 판정 객체
- `stage1-tracker.csv`: 기업별 증거 게이트와 조사 상태
- `progress.json`: 기계 판독 가능한 진행 상태

## 운영 원칙

- 미국과 한국의 후보 수·순위를 서로 섞지 않는다.
- 낮은 PER, 높은 단기 성장률, 최근 주가 하락/상승만으로 통과 또는 탈락시키지 않는다.
- 자료 부족은 `UNREVIEWED` 또는 `EVIDENCE_INSUFFICIENT`로 두며, 전용 모형의 미공개 입력은 추정 범위와 낮은 신뢰도로 표시한다.
- 기존 정밀분석의 결론은 `CARRIED_FORWARD`로 표시하며 신규 50점 스크리닝과 혼합하지 않는다.
- 44점 부분점수는 사업 증거의 상대 강도일 뿐 기대수익률 순위가 아니다. 최신 우선순위 구간은 총점을 확정한 20개에 적용하되 Hard Veto가 항상 선순위다.
- NAVER는 NVIDIA 대상 720만 주 제3자 배정을 포함한 최소 프로포마 주식수를 사용한다.
- 미국은 9%, 한국은 10% 요구수익률로 현재 가격의 5년·10년 기대를 역산한다. 숫자는 목표주가가 아니라 가격이 요구하는 성장·마진·기간의 스트레스 테스트다.
- `INVESTIGATE`는 A/B 점수와 무관하게 승격을 막고, `FAIL`은 `SCREEN_OUT`을 강제한다.
- Red Team의 `PASS`는 투자논리가 1차 공격을 견뎠다는 뜻일 뿐 매수 또는 `SCREEN_IN`이 아니다.
- NVDA의 `decision.json`에는 서로 다른 두 판정이 한 파일에 병합된 데이터 충돌이 있어, 재사용 전에 정합성 복구가 필요하다.

## 완료 조건

Stage 1은 각 시장의 모든 후보에 대해 최소한 사업 구조, 구조적 성장, 해자 방향, 재투자 구조, 생존성 및 명백한 Red Flag를 점검하면 완료된다. Wave 01~02의 다음 단계는 미국 `NOW·AMZN·MSFT·LLY·VRTX`, 한국 `NAVER·현대자동차·삼성바이오로직스·APR·알테오젠`을 조건부 심층조사 큐로 두고 열린 `INVESTIGATE`를 우선 반증하는 것이다. 이는 승격 확정이 아니며 시장별 최대 5개 제한을 지킨다.

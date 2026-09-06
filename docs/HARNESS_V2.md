# 증거·판정 분리 하네스 — 구현 v2

투자 철학과 100점 배점, 9개 Hard Veto, 포지션 규칙은 변경하지 않았다. v2는 데이터 저장·출처 연결·완료 상태·검증 방법의 버전이다.

## 현재 판단을 읽는 방법

`reviews/latest.json` → `registry/companies.json` → `companies/<ticker>/latest.json` → 날짜별 `assessment.json`을 따른다. 루트의 이전 `scorecard.json`, `decision.json`, `thesis.md`와 스크리닝 50점은 역사적 기록이다. 폴더 이름이나 파일 수정시각으로 최신 판단을 추정하지 않는다. GOOG는 GOOGL과 같은 발행사의 별칭이며 미국 상장 MELI·TSM의 현지 위험은 별도 보존한다.

```bash
python -m harness.current GOOG
python -m harness.current AMZN
python -m harness.current --list
```

## 데이터 계층

| 계층 | 저장 위치 | 의미 |
|---|---|---|
| 원자료 | `companies/<ticker>/raw-data/` | 추출 당시의 주장. 수정·자동 보정 금지 |
| 출처 목록 | `reviews/<run>/source-manifest.json` | 파일 SHA256·유형·원문 검증 여부 |
| 관측값 | `companies/<ticker>/analyses/<date>/observations.json` | 원파일·JSON pointer·기간·단위·위치·불확실성 |
| 계산치 | 같은 폴더의 `derived-metrics.json` | 입력 관측 ID·범위·비교 가능성·산식 |
| 판단 | 같은 폴더의 `assessment.json` | 8개 항목·9개 veto·가치평가·10개 반론·반증·행동 조건 |
| 한글 논지 | 같은 폴더의 `thesis.ko.md` | 사람이 읽는 판단과 한계 |
| 최신 인덱스 | `latest.json` 및 회사 registry | 종목마다 현재 판단 하나만 지정 |

원본 JSON은 구조가 서로 다르다. 어댑터는 명시된 `value`와 중첩 재무 숫자를 손실 없이 연결하지만, `h1_2026` 같은 키 이름에서 기간을 사실로 만들어 넣지 않는다. 단위·기간·원문 위치가 없는 관측은 결손 플래그를 보존한다. 한 `value`가 복합 객체이면 전체 객체를 보존하며 임의로 통화를 나누지 않는다. LLY·삼성바이오 같은 중첩 구조는 추가 수동 매핑 없이 자동 가치계산에 투입하지 않는다.

## 연구 상태와 투자 판정

| 상태 | 완료한 일 | 아직 주장하지 않는 것 |
|---|---|---|
| PRELIMINARY_REVIEW | 종목별 가설·반증·필요 증거 재정의 | 정량실사·내재가치·100점 |
| PARTIAL_ANALYSIS | 저장 원자료/기존 분석을 재검토 | 열려 있는 점수·정규화·역산 게이트 통과 |
| FULL_ANALYSIS | 정책의 필수 산출물·완료 게이트 충족 | Hard Veto 해소 또는 매수 승인 |

점수 `null`은 0점도, 과거 점수도 아니다. 첫 6개가 모두 평가 가능할 때만 75점 품질 합계를 표시한다. 100점 총계는 8개 점수가 모두 있어야 한다. 50점 스크리닝을 두 배로 만들지 않는다. 과거 100점과 현재 보류 상태를 나란히 보존한다. 자료 결손 때문에 회사에 FAIL을 부여하지 않으며 INVESTIGATE 사유를 명시한다.

## 계산의 필수 구분

- 실적 기간·통화·연결 범위·계속영업/재작성 기준을 맞춘다. 현재 growth 어댑터는 명시된 H1 전년 비교만 허용한다.
- 분기를 곱해서 TTM을 만들지 않는다. TTM은 연간+당해 누계−전년 동기 누계로 연결한다.
- `OCF-PPE` 진단은 owner FCF 전체가 아니다. 무형자산·리스 원금·SBC·운전자본의 한계를 기록한다.
- Capex 음수 표기는 원문 그대로 보존한다. 분석 계층에서 출금 부호를 명시적으로 정규화하지 않으면 계산을 차단한다.
- FCFE에는 이자가 남고 기업가치 순부채 브리지를 다시 더하지 않는다. FCFF에는 세후 이자·순부채·비지배지분을 일관되게 처리한다.
- SBC를 현금대체비용으로 차감하는 모형과 주식발행·환매 모형을 구분한다. 같은 보상을 비용·희석으로 중복 차감하지 않고, 환매에 현금이 들지 않는다고 가정하지 않는다.
- 현대차 금융사업·MELI 고객자금, 모회사/자회사 지분, ADR/우선주, 분할 후 주식 수를 별도 처리한다.
- 높은 일회성 마진·투자자산 이익·선수금 증가·미종결 인수·계획 보증을 정상화 현금 실적으로 승격하지 않는다.

## 작업 순서와 검증

사업 품질 → 9개 veto → 시장 기대 역산 → Bear/Base/Bull → 10개 반론 → 포지션/행동 조건 순서다. 같은 분석자가 레드팀을 수행했다면 독립 검토나 다수 합의로 표현하지 않는다. 실제 포트폴리오 정보가 없으면 위험예산·포지션을 만들지 않는다.

```bash
python -m pip install jsonschema
python -m unittest discover -s tests -v
python -m harness.validate
python -m harness.build --check
python scripts/validate_outputs.py
python scripts/validate_reassessment.py
python companies/NOW/valuation_model.py --check
```

`harness/build.py`와 `research.py`는 **2026-09-06의 동결된 재평가를 재현**한다. 라이브 데이터 수집기나 미래 분기 자동 분석기가 아니다. `--emit`은 파일별 결과를 stdout JSON으로만 내보내며 승인된 패치 작업에서 저장한다. 재현 검사와 원자료 pointer 검사는 계산·일관성을 검증하며 분석 가정의 진실을 증명하지 않는다.

다음 분기에는 새 원자료를 추가하고 새로운 날짜의 연구 입력과 산출물을 만든다. 이전 실행을 덮어쓰지 않는다. 새 실행의 전 종목 범위·baseline lock·검증을 완료한 후 latest 인덱스를 함께 갱신한다. 일부만 갱신하면 각 기업 latest의 실제 날짜를 보존한다. 연간 재분석은 이전 논지 복사가 아닌 원점 재검토를 수행한다.

## 이번 구조 감사에서 해결한 문제

1. 최초 main의 21개 원자료 종목과 Draft PR #10의 Astra/NOW 결과가 분리되어 있었다. main `492cd74`와 연구 `9da08ac`를 통합한 뒤, `56a4090`에 추가된 CRDO·TEM·TMDX도 포함해 원자료 종목은 24개, 전체는 93개가 되었다.
2. NOW의 42/50·72/100, NVDA의 상충 판정, 한화에어로의 점수 충돌이 최신 선택 규칙 없이 혼재했다. 단일 인덱스와 점수 척도를 분리했다.
3. 원자료만 존재하면 검증기에서 사실상 연구 상태가 드러나지 않았다. 93개 전수 registry와 완료 상태를 추가했다.
4. 기간·단위·문서 위치가 약한 숫자를 즉시 가치모델에 넣을 수 있었다. 원본 hash/pointer, 명시적 계산 범위와 차단 규칙을 추가했다.
5. 최신 자료 파일 하나가 과거 파일 전체를 대체할 위험이 있었다. MSFT의 두 raw 파일을 모두 보존하고 재분류 범위만 해석했다.

미해결: 92개 종목은 최종 정밀분석 게이트가 열려 있다. 새 구조와 전수 증거 검토 완료를 93개 완전한 투자 실사 완료로 표현하지 않는다.

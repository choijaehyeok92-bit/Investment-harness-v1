# 파괴적 혁신 축과 5분류 — 설계와 사용법

이 문서는 두 개의 추가 계층을 설명한다.

1. `policy/disruption-axis.yaml` — 파괴적 혁신을 평가하는 20점 축
2. `policy/archetype-classification.yaml` — 평가 후 5분류

투자 철학, 8개 항목 100점, 9개 Hard Veto, 포지션 규칙은 바꾸지 않았다.

## 1. 왜 100점 안에 넣지 않았는가

100점 배점은 사업 품질과 가격에 반영된 기대를 측정한다. 강한 기존 사업자와 초기 형태의
파괴자를 구분하지는 못한다. 두 유형은 요구하는 증거, 허용 가능한 밸류에이션, 적정 포지션
크기가 서로 다르다. 그래서 별도 축이 필요하다.

100점 안에 9번째 항목을 넣으려면 기존 8개 배점을 줄여야 한다. 그 경우:

- `policy/scorecard.yaml`은 `harness/baseline-lock.json`의 SHA로 고정되어 있고,
- `schemas/assessment-v2.schema.json`은 항목 수를 정확히 8개로 제한하며,
- 기존 93개 종목의 점수가 소급해서 다시 쓰이게 된다.

따라서 혁신 축은 **100점 밖의 20점 축**으로 두고, 별도 파일에 저장하고, 별도로 보고한다.

### 혁신 축이 할 수 있는 것과 없는 것

| 허용 | 금지 |
|---|---|
| 5분류의 원형(archetype) 결정 | 8개 항목 점수 변경 |
| 문샷형의 밸류에이션 용인폭 결정 | 100점·75점 합계 변경 |
| 포지션 상한과 매수 속도 결정 | 9개 Hard Veto 완화·유예 |
| 추적할 핵심 KPI 결정 | 매수 승인 |

서열은 `Hard Veto > Score > Archetype`이다.

## 2. 20점 축의 5개 차원

각 차원 0~4점. 모르면 `null`이며 0점이 아니다. 하나라도 `null`이면 등급은 `UNSCORED`다.

| 차원 | 핵심 질문 |
|---|---|
| `non_consumption_and_new_market_creation` | 기존에 아예 살 수 없던 수요를 만들었는가, 남의 몫을 가져온 것인가 |
| `incumbent_business_model_conflict` | 기존 강자가 제대로 대응하려면 자기 수익구조를 깨야 하는가 |
| `cost_or_performance_curve` | 단위원가 하락 또는 성능 상승이 반복 측정되는 곡선인가 |
| `s_curve_position_and_adoption_evidence` | 실제 유상 채택이 어디까지 관측되는가 |
| `platform_optionality_and_second_curve` | 지금의 자산이 두 번째 수익 곡선을 실제로 열고 있는가 |

등급: `FOUNDATIONAL` 17-20 · `STRONG` 13-16 · `EMERGING` 9-12 · `INCREMENTAL` 4-8 ·
`NONE` 0-3 · `UNSCORED`.

### 과장 방지 규칙

- TAM 크기, 주가 강세, "제2의 엔비디아" 비교는 점수 근거가 아니다.
- 수주잔고·수주·파이프라인·MOU·제휴 건수는 그 자체로 채택 증거가 아니다. 유상 상용 채택만 채택이다.
- 다기간 측정 없는 원가곡선은 2점을 넘지 못한다.
- 출시 제품도 부착 증거도 없는 옵션가치는 1점을 넘지 못한다.
- 보조금·규제 창구에 의존하는 채택은 그것이 끝났을 때를 반드시 기술한다.
- 등급을 낮출 관측(반증)을 최소 3개 적는다.

## 3. 5분류

| 분류 | 정의 | 밸류에이션 허용 | 포지션 상한 |
|---|---|---|---|
| `COMPOUNDER` 컴파운더 | 재투자가 장기간 주당 경제가치를 복리로 키우는 기업 | base 대비 -10%까지만 초과 허용 | EXCEPTIONAL_WINNER |
| `MOONSHOT` 문샷형 | 테슬라·팔란티어·엔비디아·구글·아마존의 초기 형태. 파괴적이고 채택은 아직 확대 중 | FOUNDATIONAL은 base의 2.5배, STRONG은 1.67배까지 | STARTER |
| `EMERGING_OUTLIER` 이머징 아웃라이어 | 아웃라이어 성격이 이미 강하고 가격은 여전히 base 전후 | base 대비 -15% 이내 | HIGH_CONVICTION |
| `EXPECTATION_GAP` 기대차형 | 성장성은 적당하지만 가격이 충분히 내려와 시장 기대가 틀렸을 가능성이 큰 기업 | gap 35% 이상 필수 | NORMAL |
| `NOT_QUALIFIED` 비적격형 | 잔여 분류. 게이트 미달 또는 증거 부족 | 해당 없음 | NONE |

`expectation_gap_ratio = base_value_per_share / current_price - 1`. 양수면 base가 현재가보다
위에 있다는 뜻이다. 이 값은 FACT가 아니라 base 시나리오에 딸린 ESTIMATE다.

### 우선순위

`COMPOUNDER` → `MOONSHOT` → `EMERGING_OUTLIER` → `EXPECTATION_GAP` → `NOT_QUALIFIED`.

첫 번째로 모든 게이트를 통과한 분류가 배정된다. 입증된 복리 경제성이 혁신 서사보다 앞서고,
아직 입증되지 않은 파괴자는 이머징 아웃라이어가 아니라 문샷으로 작게 사이징한다. 문샷이
채택과 재투자 수익률을 입증하면 재분류를 통해 상위 분류로 올라간다(자동 승격은 없다).

### 비적격형의 사유 코드

`HARD_VETO_FAIL` · `INSUFFICIENT_EVIDENCE` · `QUALITY_GATES_NOT_MET` ·
`PRICED_BEYOND_BASE` · `PRICED_BEYOND_MOONSHOT_TOLERANCE` ·
`MISPRICING_MECHANISM_NOT_ESTABLISHED` · `SURVIVABILITY_GATE_NOT_MET`.

`INSUFFICIENT_EVIDENCE`는 연구 상태에 대한 진술이지 기업에 대한 부정 판정이 아니다.
`REJECT` 라벨과 같지 않다. 밸류에이션 게이트만 놓친 경우 해당 분류는 `quality_gates_met`에
남아 관찰 목록에서 이유를 잃지 않는다.

### 기대차형의 필수 조건

가격이 내렸다는 사실은 근거가 아니다. **시장이 왜 틀렸는지의 메커니즘**과 그 메커니즘의
반증을 적어야 한다. 허용 예: 일시적 비용·믹스 항목을 구조적인 것으로 외삽, 연결 보고에
가려진 사업부 경제성, 종료 시점이 명시된 강제 매도·지수 흐름, 실제 범위가 가격이 함의하는
것보다 훨씬 좁은 규제·소송 부담. 기각 예: "많이 빠졌다", "PER이 과거 평균보다 낮다",
"내 매수가보다 싸다", "센티먼트가 나쁘다".

기대차형은 gap이 재산정된 base 대비 닫히면 축소가 정당하다. 이때 기록은 "주가가 올라서"가
아니라 "가치 대비 gap 소멸"이어야 하며, 축소 전에 재언더라이팅을 먼저 한다.

## 4. 결정 라벨과의 관계

분류는 결정 라벨이 아니다. 라벨(`REJECT`…`EXIT`)은 무엇을 할지, 분류는 그 기업이 어떤
성격의 베팅인지를 말한다. 둘 다 기록하며 서로를 대체하지 않는다. 분류가 매수를 승인하지도
않는다. `research_state`가 `FULL_ANALYSIS`가 아니면 분류는 잠정(provisional)이고 포지션
상한은 `NONE`이다. Hard Veto가 `PASS`가 아니어도 상한은 `NONE`이다.

## 5. 사용법

```bash
python -m unittest tests.test_archetype -v
python -m harness.archetype              # 저장된 archetype.json 전수 재계산 검증
python scripts/validate_outputs.py       # 스키마 + 분류 일관성 + 포지션 상한 검사
```

```python
from harness.archetype import build_inputs, classify

inputs = build_inputs(assessment, disruption,
                      current_price=180.0, base_value_per_share=110.0,
                      permanent_loss_case_sized=True)
result = classify(inputs)   # archetype, gate_results, position_ceiling
```

분류는 결정론적이다. 같은 입력은 항상 같은 분류를 낸다. 저장된 `archetype.json`이
분류기와 다르면 `scripts/validate_outputs.py`가 실패한다. 분석자가 손으로 분류를 바꾸는
경로는 없다. 게이트를 바꾸려면 정책 파일과 `harness/archetype.py`를 함께 고치고 테스트를
갱신해야 한다.

## 6. 예시 (가상 종목)

STRONG 등급(16점), base 대비 약 1.64배 가격, 런웨이 31개월인 기업의 분류 결과:

```text
disruption_dimensions  4 / 4 / 3 / 3 / 2  = 16  → tier STRONG
expectation_gap_ratio  110 / 180 - 1      = -0.389
archetype              MOONSHOT
position_ceiling       STARTER
quality_gates_met      EMERGING_OUTLIER, EXPECTATION_GAP  (가격 게이트만 미달)
COMPOUNDER 실패 게이트  business_quality_75>=52, moat_trajectory>=11,
                       incremental_roic_and_fcf_per_share>=11, ...
```

같은 기업의 가격이 base의 3배였다면 결과는 `NOT_QUALIFIED` /
`PRICED_BEYOND_MOONSHOT_TOLERANCE`다. 고밸류에이션 용인은 무한하지 않다.

## 7. 한계

- 게이트의 임계값은 정책적 선택이다. 근거는 기존 배점 체계와의 정합성이며, 통계적으로
  최적화된 값이 아니다. 바꾸려면 정책·코드·테스트를 함께 바꾸고 변경 이유를 남긴다.
- `expectation_gap_ratio`는 base 시나리오의 품질을 그대로 물려받는다. base가 부실하면
  분류도 부실하다.
- 혁신 축은 사후에 확인 가능한 사실이 아니라 현재 관측 가능한 증거의 요약이다. 등급이
  높다고 성공 확률이 높다는 뜻이 아니며, 오히려 문샷형의 포지션 상한이 가장 낮다.
- 기존 93개 종목에는 아직 `disruption.json`과 `archetype.json`이 없다. 새 계층은 다음
  실행부터 채운다. 과거 판단을 소급해 분류하지 않는다.

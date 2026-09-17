# Agent: Archetype Classifier

## Objective

Place the company in exactly one of the five archetypes in
`policy/archetype-classification.yaml`, after scoring, Hard Veto, valuation, the
disruption axis and the red team have all been completed.

| Archetype | 한글 | Position ceiling |
|---|---|---|
| `COMPOUNDER` | 컴파운더 | EXCEPTIONAL_WINNER |
| `MOONSHOT` | 문샷형 | STARTER |
| `EMERGING_OUTLIER` | 이머징 아웃라이어 | HIGH_CONVICTION |
| `EXPECTATION_GAP` | 기대차형 | NORMAL |
| `NOT_QUALIFIED` | 비적격형 | NONE |

An archetype is not a decision label. It states what kind of bet the company is; the
decision label in `AGENTS.md` states what to do.

## Procedure

1. Collect the classifier inputs: Hard Veto status, research state, the eight category
   scores and their confidence, `business_quality_75`, the disruption dimensions and
   tier, current price and the base-case value per share.
2. Compute `expectation_gap_ratio = base_value_per_share / current_price - 1`.
3. Run `harness.archetype.classify`. Do not hand-assign an archetype: the gates are
   deterministic, and a stored archetype that disagrees with the classifier fails
   `python scripts/validate_outputs.py`.
4. Write `companies/<TICKER>/archetype.json` against `schemas/archetype.schema.json`,
   including the full `gate_results` and at least one entry in `what_would_change_it`.
5. Pass the position ceiling to the Portfolio Monitor. The ceiling and the
   `policy/position-sizing.yaml` band are both binding; the lower one applies.

```python
from harness.archetype import build_inputs, classify
inputs = build_inputs(assessment, disruption, current_price=..., base_value_per_share=...,
                      permanent_loss_case_sized=True)
result = classify(inputs)
```

## Rules

- A Hard Veto FAIL forces `NOT_QUALIFIED` with reason `HARD_VETO_FAIL`, whatever the score.
- Missing inputs produce `NOT_QUALIFIED` with reason `INSUFFICIENT_EVIDENCE`. Report this
  as a statement about the research, not as a rejection of the company.
- An archetype is provisional until `research_state` is `FULL_ANALYSIS`, and a provisional
  archetype carries position ceiling `NONE`.
- A Hard Veto status other than `PASS` also carries ceiling `NONE`.
- When only the valuation gate failed, record the archetype in `quality_gates_met` so the
  watchlist keeps why the company was close.
- `MOONSHOT` tolerates a price above base only within the tier bound (2.5x base for
  `FOUNDATIONAL`, 1.67x for `STRONG`), and never when
  `price_requires_unrealistic_bull_case` is FAIL.
- `EXPECTATION_GAP` requires a stated mispricing mechanism and a falsifier for it. "The
  price fell" is not a mechanism.
- Never change an archetype because of price alone. Re-underwrite value first, then
  reclassify, and log the change in `decision-history.md`.

## Deliverables

- `companies/<TICKER>/archetype.json`
- the archetype, its gate results and the implied position ceiling
- the evidence that would move the company to a different archetype

# Operating Workflow

## A. New-stock research

```text
Universe
  ↓
Screener
  ↓
SCREEN_IN / WATCH / SCREEN_OUT
  ↓
Deep Analyst
  ↓
Disruption Analyst  (20-point axis, outside the 100 points)
  ↓
Hard Veto
  ↓
Valuation / Reverse Expectations
  ↓
Red Team
  ↓
Archetype Classifier
  ↓
COMPOUNDER / MOONSHOT / EMERGING_OUTLIER / EXPECTATION_GAP / NOT_QUALIFIED
  ↓
Portfolio Monitor
  ↓
Decision + Evidence Ledger
```

The archetype sets the position ceiling. The ceiling and the `policy/position-sizing.yaml`
band are both binding; the lower one applies.

## B. File creation order

For `TICKER`:

1. create `companies/TICKER/`
2. create `thesis.md`
3. create `scorecard.json`
4. create `disruption.json`
5. create `hard-veto.json`
6. create `valuation.json`
7. create `red-team.md`
8. create `archetype.json` (derived with `harness.archetype.classify`, never hand-assigned)
9. create or append `evidence.jsonl`
10. create `decision.json`
11. append `decision-history.md`
12. run `python scripts/validate_outputs.py`

## C. Annual anti-anchoring procedure

The annual re-underwrite should be completed from current primary evidence before reading the prior-year conclusion. After the new thesis is finished, compare it against the previous thesis and log differences. Re-score the disruption axis and re-run the classification from the new evidence before reading the prior archetype.

## C2. Reclassification

Re-run the classification at every quarterly review and always at the annual re-underwrite.
An archetype change requires business evidence and a `decision-history.md` entry. Price
movement alone never changes an archetype; re-underwrite the base case first, then
reclassify against the new value.

## D. Branching suggestion

For material research updates:

- `research/TICKER-YYYY-MM`
- validate outputs
- review diff
- merge only after all schema and policy checks pass

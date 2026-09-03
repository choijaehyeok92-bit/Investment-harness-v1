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
Hard Veto
  ↓
Valuation / Reverse Expectations
  ↓
Red Team
  ↓
Portfolio Monitor
  ↓
Decision + Evidence Ledger
```

## B. File creation order

For `TICKER`:

1. create `companies/TICKER/`
2. create `thesis.md`
3. create `scorecard.json`
4. create `hard-veto.json`
5. create `valuation.json`
6. create `red-team.md`
7. create or append `evidence.jsonl`
8. create `decision.json`
9. append `decision-history.md`
10. run `python scripts/validate_outputs.py`

## C. Annual anti-anchoring procedure

The annual re-underwrite should be completed from current primary evidence before reading the prior-year conclusion. After the new thesis is finished, compare it against the previous thesis and log differences.

## D. Branching suggestion

For material research updates:

- `research/TICKER-YYYY-MM`
- validate outputs
- review diff
- merge only after all schema and policy checks pass

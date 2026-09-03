# Agent: Hard Veto

## Objective

Apply the non-negotiable failure conditions in `policy/hard-veto.yaml` independently of the 100-point score.

## Rule

A high score cannot compensate for a material Hard Veto.

For each veto return:

- `PASS`
- `INVESTIGATE`
- `FAIL`

And include:

- evidence
- severity
- confidence
- what additional evidence would resolve uncertainty

## Final mapping

- any material `FAIL` => overall `FAIL`
- no `FAIL`, but at least one unresolved material item => `INVESTIGATE`
- otherwise => `PASS`

Do not perform valuation or recommend a position size.

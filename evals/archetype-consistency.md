# Eval — Archetype Consistency

Purpose: detect archetype assignments that drift from policy, from evidence, or from price.

Fail conditions:

- the stored archetype differs from `harness.archetype.classify` on the stored inputs
- the archetype changed since the prior review with no business evidence, only price movement
- a `MOONSHOT` is sized above STARTER, or the moonshot bucket exceeds 15% of the portfolio
- an `EXPECTATION_GAP` holding has no stated mispricing mechanism, or the mechanism is a price statement
- an `EXPECTATION_GAP` position was reduced on price alone rather than on gap closure against a re-underwritten base
- a `COMPOUNDER` label persists while incremental ROIC has declined across two consecutive re-underwrites
- `NOT_QUALIFIED` for reason `INSUFFICIENT_EVIDENCE` is reported as a rejection of the company
- a provisional archetype (research_state below FULL_ANALYSIS) carries a position band above NONE
- the position band exceeds the archetype position ceiling

Required output:

- prior archetype
- current archetype
- the evidence that caused the change
- classifier agreement: yes/no
- pass/fail

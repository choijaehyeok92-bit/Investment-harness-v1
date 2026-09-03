# Eval — Score Stability

Purpose: detect excessive score drift when the evidence set has not materially changed.

Fail conditions:

- total score changes by >10 points without new material evidence
- category score changes by >3 points without explicit explanation
- confidence increases when evidence quality did not improve

Required output:

- old score
- new score
- new evidence
- justified change
- pass/fail

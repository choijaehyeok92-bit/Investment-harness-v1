# Eval — Disruption Evidence Discipline

Purpose: detect a disruption tier that rests on narrative rather than falsifiable adoption evidence.

Fail conditions:

- a dimension scores 3 or 4 with no FACT-labeled evidence
- `s_curve_position_and_adoption_evidence` scores above 1 on backlog, bookings, pipeline, MOUs or partnership counts alone
- `cost_or_performance_curve` scores above 2 without a multi-period measured series
- `platform_optionality_and_second_curve` scores above 1 with no shipped product and no attach evidence
- TAM size, share-price strength or a "next NVIDIA" comparison appears as scoring evidence
- fewer than three falsifiers, or falsifiers that no realistic observation could satisfy
- a dimension is unknown but the tier is asserted anyway instead of `UNSCORED`
- a scorecard category moved in the same revision with no evidence other than the disruption story

Required output:

- dimension
- score
- the single strongest piece of evidence, with its claim type
- whether that evidence is falsifiable
- pass/fail

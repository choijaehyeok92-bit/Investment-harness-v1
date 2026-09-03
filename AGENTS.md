# AGENTS.md — Investment Harness v1.0

## Mission

Find listed companies where the market materially underestimates the scale and/or duration of long-term economic-value growth, provided that competitive advantage is strengthening, reinvestment economics are attractive, and successful outcomes offer materially greater upside than permanent-loss downside.

## Authority hierarchy

When instructions conflict, follow this order:

1. `policy/investment-philosophy.md`
2. `policy/hard-veto.yaml`
3. `policy/scorecard.yaml`
4. `policy/source-policy.yaml`
5. role-specific instructions under `agents/`
6. task-specific user instructions

Do not silently override higher-order policy.

## Mandatory distinctions

Always separate:

- Fact
- Estimate
- Inference
- Opinion

Always separate:

- Company quality
- Market expectations
- Valuation
- Portfolio risk budget

Never allow macro views to directly change the 100-point company score.

## Default workflow

For a new stock:

1. Run `agents/screener.md`.
2. If candidate survives, run `agents/deep-analyst.md`.
3. Apply `policy/hard-veto.yaml`.
4. Run `agents/valuation.md`.
5. Run `agents/red-team.md`.
6. Produce final status through `agents/portfolio-monitor.md`.
7. Persist outputs under `companies/<TICKER>/`.

For an existing holding:

1. Load the latest thesis, scorecard, valuation, evidence ledger and decision.
2. Add only new evidence.
3. Re-evaluate only the components affected by new evidence unless it is the annual re-underwrite.
4. Never average down solely because price declined.
5. Never trim solely because price rose.

## Completion gate

A stock analysis is incomplete unless it contains:

- all eight scorecard categories
- score evidence and counter-evidence
- confidence for every category
- Hard Veto status
- market-implied expectations
- Bear/Base/Bull scenarios
- explicit permanent-loss case
- explicit thesis falsifiers
- position increase evidence
- sell evidence
- source-quality notes

## Output discipline

Use machine-readable JSON where a schema exists.
Use Markdown for narrative thesis and decision history.
Do not invent unavailable data.
If a required metric cannot be established, mark it `unknown` and reduce confidence.

## Decision labels

Allowed final labels:

- `REJECT`
- `WATCH`
- `STARTER`
- `NORMAL`
- `HIGH_CONVICTION`
- `CORE_WINNER`
- `EXCEPTIONAL_WINNER`
- `HOLD`
- `REDUCE`
- `EXIT`

No other label should be used without updating policy first.

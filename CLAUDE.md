@AGENTS.md
@policy/investment-philosophy.md

# Claude Code Adapter — Investment Harness v1.1

## Purpose

Use the repository's existing investment policy as the single source of truth. Claude-specific files are adapters only; they must not duplicate or redefine the investment philosophy.

## Operating rules

- `Hard Veto > Score` at all times.
- Separate FACT, ESTIMATE, INFERENCE, and OPINION.
- Separate company quality, market expectations, valuation, and portfolio risk budget.
- Macro may change purchase pacing or risk budget, never the 100-point company score.
- Never add solely because price declined. Never trim solely because price rose.
- Reverse-engineer market expectations before giving a valuation conclusion.
- Missing evidence lowers confidence; never invent precision.
- For full stock analysis, delegate to the specialist agents rather than collapsing the workflow into one general analysis.

## Canonical state

- Company state: `companies/<TICKER>/`
- Portfolio state: `portfolio/`
- Screening state: `screening/`
- Policy: `policy/`
- Output schemas: `schemas/`

Do not create a parallel Claude-only company database or copy policy files into `.claude/`.

## Recommended entrypoints

- `/analyze-stock TICKER` — full underwriting pipeline
- `/screen-stock TICKER` — lightweight candidate screen
- `/quarterly-review TICKER` — evidence-only quarterly update
- `/annual-reunderwrite TICKER` — clean-slate annual re-underwrite

For an orchestrated session, run `claude --agent investment-pm` from the repository root.

## Validation

Before a research package is considered complete, run:

`python scripts/validate_outputs.py`

The project Stop hook also runs this validator automatically.

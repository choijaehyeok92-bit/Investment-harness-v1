> 현재 연구 상태: [2026-09-05 Astra 재평가](reviews/2026-09-05-astra/README.md). 40개 기존 판단 재심사, 50개 예비후보는 미심사. 과거 스크리닝 점수·판정을 현재 승인으로 사용하지 마세요.

# Investment Harness v1.1 — Codex + Claude Code

A repository-native harness for long-horizon, expectation-gap, outlier-oriented equity research and screening.

## Core idea

This harness is built around seven durable alpha sources:

- Time horizon
- Duration mispricing
- Moat trajectory
- Reinvestment economics
- Expectation gap
- Power-law outcomes
- Behavioral discipline

The system separates company selection from portfolio risk pacing. Macro conditions may adjust risk budget and buying pace, but must not directly alter the company quality score.

## Pipeline

1. `screener` — narrow the universe and identify candidates worth deeper work.
2. `deep-analyst` — assess business quality, structural growth, moat trajectory, reinvestment and management.
3. `valuation` — reverse-engineer market expectations and build Bear/Base/Bull scenarios.
4. `hard-veto` — apply non-negotiable rejection/investigation gates.
5. `red-team` — attack the thesis, surface falsifiers, and challenge key assumptions.
6. `portfolio-monitor` — assign status/position band and maintain the evidence ledger over time.

## Decision rule

High score is necessary but not sufficient.

`Hard Veto > Score`

A stock must also have a meaningful expectation gap and favorable asymmetry. Position size should increase with evidence, not merely with analyst conviction or price declines.

## Repository layout

- `AGENTS.md` — top-level operating contract for AI agents
- `policy/` — immutable strategy and decision rules
- `agents/` — role contracts for each agent
- `schemas/` — machine-readable output schemas
- `templates/` — one-page investment record and monitoring templates
- `evals/` — quality-control checks for the harness itself
- `companies/<TICKER>/` — per-company research state
- `portfolio/` — portfolio-level state and macro overlay
- `screening/` — candidate and rejection outputs
- `scripts/validate_outputs.py` — basic schema and consistency checks

## Recommended company folder

```text
companies/MSFT/
├── thesis.md
├── scorecard.json
├── evidence.jsonl
├── valuation.json
├── decision.json
└── decision-history.md
```

## Important operating rule

Never overwrite prior decisions without logging the change. The purpose of the repository is not only to make decisions, but to preserve what was believed at the time and why.

## Claude Code support

This version adds a Claude adapter without duplicating the strategy core:

- `CLAUDE.md` imports the common agent contract and investment philosophy.
- `.claude/agents/` defines specialist Claude Code subagents.
- `.claude/skills/` provides `/analyze-stock`, `/screen-stock`, `/quarterly-review`, and `/annual-reunderwrite`.
- `.claude/settings.json` protects policy/schema/harness infrastructure and registers a Stop validation hook.
- `docs/CLAUDE_SETUP.md` contains setup and verification steps.

Recommended Claude Code entrypoint: `claude --agent investment-pm`.

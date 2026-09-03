# Claude Code Setup

## Requirements

- Claude Code installed and authenticated
- Python 3
- `pip install -r requirements.txt`

This adapter uses current Claude Code project features: `CLAUDE.md`, project subagents under `.claude/agents/`, project skills under `.claude/skills/`, project settings/permissions, and hooks.

## Start

From the repository root:

```bash
claude --agent investment-pm
```

Or start normal Claude Code:

```bash
claude
```

Then use one of the project skills:

```text
/analyze-stock MSFT
/screen-stock CRWD
/quarterly-review NVDA
/annual-reunderwrite GOOGL
```

## Verify adapter discovery

Inside Claude Code:

```text
/memory
/agents
/skills
/hooks
/permissions
/status
/doctor
```

Expected:
- `CLAUDE.md` is loaded and imports `AGENTS.md` and the investment philosophy.
- seven project subagents are visible.
- four project skills are visible.
- the Stop validation hook is active.
- edits to policy/schema/eval/agent/config files are denied.

## Architecture

The Claude layer is an adapter only:

```text
Investment Harness Core
├── policy/
├── schemas/
├── agents/          # model-neutral role contracts
├── companies/
├── portfolio/
└── screening/

Claude Adapter
├── CLAUDE.md
└── .claude/
    ├── agents/
    ├── skills/
    ├── hooks/
    └── settings.json
```

Do not copy policy or company state into `.claude/`.

## Permissions

The shared project settings intentionally protect Harness infrastructure from agent edits. Normal research state under `companies/`, `portfolio/`, and `screening/` remains writable subject to Claude Code's normal permission prompts.

The project disables `bypassPermissions` mode to reduce the chance of accidentally bypassing these safeguards.

## MCP / financial-data connectors

No MCP server is hard-coded in v1.1 because MCP server names and authentication are environment-specific. Add your financial-data or filing MCP server to Claude Code separately, then either:

1. expose it to the whole session, or
2. add the configured server name under `mcpServers:` in selected `.claude/agents/*.md` files.

Keep credentials outside the repository.

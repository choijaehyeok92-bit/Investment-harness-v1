#!/usr/bin/env python3
"""Minimal repository validation for investment-harness outputs."""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Missing dependency: jsonschema. Install with: pip install jsonschema")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"

MAPPINGS = {
    "scorecard.json": "scorecard.schema.json",
    "valuation.json": "valuation.schema.json",
    "decision.json": "decision.schema.json",
    "hard-veto.json": "hard-veto.schema.json",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_file(data_path: Path, schema_path: Path) -> list[str]:
    errors = []
    schema = load_json(schema_path)
    data = load_json(data_path)
    validator = jsonschema.Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
        errors.append(f"{data_path}: {err.message}")
    return errors


def main() -> int:
    errors: list[str] = []
    companies = ROOT / "companies"
    if not companies.is_dir():
        print("No companies/ directory yet - nothing to validate.")
        return 0
    for company_dir in companies.iterdir():
        if not company_dir.is_dir():
            continue
        for filename, schema_filename in MAPPINGS.items():
            data_path = company_dir / filename
            if data_path.exists():
                errors.extend(validate_file(data_path, SCHEMAS / schema_filename))

        scorecard_path = company_dir / "scorecard.json"
        decision_path = company_dir / "decision.json"
        if scorecard_path.exists():
            scorecard = load_json(scorecard_path)
            total = sum(v["score"] for v in scorecard.get("categories", {}).values())
            if abs(total - scorecard.get("total_score", -999)) > 1e-9:
                errors.append(f"{scorecard_path}: total_score does not equal category sum")
        if decision_path.exists():
            decision = load_json(decision_path)
            if decision.get("hard_veto_status") == "FAIL" and decision.get("label") not in {"REJECT", "EXIT"}:
                errors.append(f"{decision_path}: Hard Veto FAIL must resolve to REJECT or EXIT")

    if errors:
        print("VALIDATION FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

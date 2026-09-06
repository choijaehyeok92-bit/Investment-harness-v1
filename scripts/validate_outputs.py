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
    try:
        data = load_json(data_path)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        return [f"{data_path}: invalid JSON: {exc}"]
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
    category_maxima = {
        "structural_change_and_leadership": 15, "customer_value_and_product": 10,
        "moat_trajectory": 15, "incremental_roic_and_fcf_per_share": 15,
        "management_and_capital_allocation": 10, "financial_survivability": 10,
        "expectation_gap_and_valuation": 15, "power_law_and_asymmetry": 10,
    }
    veto_ids = {
        "management_or_accounting_integrity", "external_capital_dependence", "persistent_dilution",
        "low_quality_growth", "incremental_roic_collapse", "moat_shrinkage",
        "price_requires_unrealistic_bull_case", "fatal_concentration", "permanent_loss_probability",
    }
    for company_dir in sorted(companies.iterdir()):
        if not company_dir.is_dir():
            continue
        for filename, schema_filename in MAPPINGS.items():
            data_path = company_dir / filename
            if data_path.exists():
                errors.extend(validate_file(data_path, SCHEMAS / schema_filename))

        scorecard_path = company_dir / "scorecard.json"
        decision_path = company_dir / "decision.json"
        if scorecard_path.exists():
            try:
                scorecard = load_json(scorecard_path)
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            if set(scorecard.get("categories", {})) != set(category_maxima):
                errors.append(f"{scorecard_path}: must contain exactly the eight policy categories")
            for name, value in scorecard.get("categories", {}).items():
                if value.get("max_score") != category_maxima.get(name) or value.get("score", -1) > value.get("max_score", 0):
                    errors.append(f"{scorecard_path}: invalid category maximum/score for {name}")
            total = sum(v["score"] for v in scorecard.get("categories", {}).values())
            if abs(total - scorecard.get("total_score", -999)) > 1e-9:
                errors.append(f"{scorecard_path}: total_score does not equal category sum")
        if decision_path.exists():
            try:
                decision = load_json(decision_path)
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            if decision.get("hard_veto_status") == "FAIL" and decision.get("label") not in {"REJECT", "EXIT"}:
                errors.append(f"{decision_path}: Hard Veto FAIL must resolve to REJECT or EXIT")
            veto_path = company_dir / "hard-veto.json"
            if veto_path.exists():
                try:
                    report = load_json(veto_path)
                    flags = report.get("vetoes", [])
                    if len(flags) != 9 or {v["id"] for v in flags} != veto_ids:
                        errors.append(f"{veto_path}: must contain exactly the nine policy veto IDs")
                    expected = "FAIL" if any(v["status"] == "FAIL" for v in flags) else "INVESTIGATE" if any(v["status"] == "INVESTIGATE" for v in flags) else "PASS"
                    if report["overall_status"] != expected or decision["hard_veto_status"] != expected:
                        errors.append(f"{veto_path}: veto aggregate and decision status disagree")
                except (json.JSONDecodeError, UnicodeDecodeError):
                    pass  # Reported by validate_file above.

        ledger = company_dir / "evidence.jsonl"
        if ledger.exists():
            for lineno, line in enumerate(ledger.read_text(encoding="utf-8").splitlines(), 1):
                if not line.strip():
                    continue
                try:
                    json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(f"{ledger}:{lineno}: invalid JSONL: {exc}")

    if errors:
        print("VALIDATION FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

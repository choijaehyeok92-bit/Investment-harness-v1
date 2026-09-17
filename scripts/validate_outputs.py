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
sys.path.insert(0, str(ROOT))

from harness.archetype import (  # noqa: E402  (path is set above)
    SCORECARD_CATEGORIES, check_document, disruption_tier, disruption_total,
)

MAPPINGS = {
    "scorecard.json": "scorecard.schema.json",
    "valuation.json": "valuation.schema.json",
    "decision.json": "decision.schema.json",
    "hard-veto.json": "hard-veto.schema.json",
    "disruption.json": "disruption.schema.json",
    "archetype.json": "archetype.schema.json",
}

# policy/position-sizing.yaml bands, weakest first. The archetype ceiling in
# policy/archetype-classification.yaml and the sizing band are both binding.
POSITION_BANDS = ["NONE", "STARTER", "NORMAL", "HIGH_CONVICTION", "CORE_WINNER", "EXCEPTIONAL_WINNER"]


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

        disruption_path = company_dir / "disruption.json"
        archetype_path = company_dir / "archetype.json"
        disruption = None
        if disruption_path.exists():
            try:
                disruption = load_json(disruption_path)
            except (json.JSONDecodeError, UnicodeDecodeError):
                disruption = None
        if disruption is not None:
            dimension_scores = {name: item.get("score") for name, item in disruption.get("dimensions", {}).items()}
            try:
                expected_total = disruption_total(dimension_scores)
                expected_tier = disruption_tier(dimension_scores)
            except ValueError as exc:
                errors.append(f"{disruption_path}: {exc}")
            else:
                if disruption.get("total") != expected_total:
                    errors.append(f"{disruption_path}: total must equal the five dimension scores, or null when any is unknown")
                if disruption.get("tier") != expected_tier:
                    errors.append(f"{disruption_path}: tier does not match policy/disruption-axis.yaml bands")

        if archetype_path.exists():
            try:
                archetype = load_json(archetype_path)
            except (json.JSONDecodeError, UnicodeDecodeError):
                archetype = None
            if archetype is not None and "inputs" in archetype:
                errors.extend(f"{archetype_path}: {message}" for message in check_document(archetype))
                inputs = archetype["inputs"]
                if scorecard_path.exists():
                    try:
                        stored = {name: item.get("score") for name, item in load_json(scorecard_path).get("categories", {}).items()}
                    except (json.JSONDecodeError, UnicodeDecodeError):
                        stored = None
                    if stored and any(inputs["category_scores"].get(name) != stored.get(name) for name in SCORECARD_CATEGORIES):
                        errors.append(f"{archetype_path}: inputs.category_scores disagree with scorecard.json")
                if disruption is not None:
                    if inputs.get("disruption_total") != disruption.get("total") or inputs.get("disruption_tier") != disruption.get("tier"):
                        errors.append(f"{archetype_path}: disruption inputs disagree with disruption.json")
                if decision_path.exists():
                    try:
                        decision = load_json(decision_path)
                    except (json.JSONDecodeError, UnicodeDecodeError):
                        decision = None
                    if decision is not None:
                        if inputs.get("hard_veto_status") != decision.get("hard_veto_status"):
                            errors.append(f"{archetype_path}: hard_veto_status disagrees with decision.json")
                        ceiling = archetype.get("position_ceiling", "NONE")
                        band = decision.get("position_band", "NONE")
                        if POSITION_BANDS.index(band) > POSITION_BANDS.index(ceiling):
                            errors.append(f"{decision_path}: position_band {band} exceeds the {archetype['archetype']} ceiling {ceiling}")

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

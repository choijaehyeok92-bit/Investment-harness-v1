#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python -m unittest discover -s tests -v
python -m harness.validate
python -m harness.build --check
python -m harness.deep_report --check
python scripts/validate_outputs.py
python scripts/validate_reassessment.py
python companies/NOW/valuation_model.py --check

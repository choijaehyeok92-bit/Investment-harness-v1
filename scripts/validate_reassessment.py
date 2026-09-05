#!/usr/bin/env python3
"""Structural/regression tests, not certification of investment conclusions."""
import json
from pathlib import Path
from reassessment_models import audit, company_audit, self_test

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "reviews/2026-09-05-astra"


def records(name):
    return [json.loads(line) for line in (R / name).read_text().splitlines() if line.strip()]


def main():
    inventory = json.loads((R / "coverage.json").read_text())
    companies = records("company-reassessments.jsonl")
    screens = records("screen-reassessments.jsonl")
    qualitative = records("qualitative-reassessments.jsonl")
    assert len(inventory) == len({r["ticker"] for r in inventory}) == 90
    active = {r["ticker"] for r in companies + screens + qualitative}
    assert len(active) == 40
    assert len(companies) == 10 and len(screens) == 20 and len(qualitative) == 12
    assert sum(r["review_status"] == "UNREVIEWED_PRELIMINARY_ONLY" for r in inventory) == 50
    assert sum(r["total_score"] is not None for r in companies) == 9
    assert {r["ticker"] for r in screens if r["total_score"] is None} == {"000660", "005380", "012450", "196170"}
    for row in companies + screens:
        components = row.get("categories", row.get("scores"))
        assert len(components) == (8 if row in companies else 7)
        values = [c["score"] for c in components.values()]
        if None in values:
            assert row["total_score"] is None and row["score_status"] == "EVIDENCE_INSUFFICIENT"
        else:
            assert row["total_score"] == sum(values)
        for c in components.values():
            assert c["score"] is None or 0 <= c["score"] <= c["max_score"]
            assert 0 <= c["confidence"] <= 1
            assert c["evidence"] and c["counter_evidence"] and c["missing_data"]
    for row in companies:
        decision = json.loads((ROOT / "companies" / row["ticker"] / "decision.json").read_text())
        assert decision["label"] == row["decision"] and decision["position_band"] == "NONE"
        assert decision["hard_veto_status"] == row["hard_veto_status"]
        if row["total_score"] is not None:
            score = json.loads((ROOT / "companies" / row["ticker"] / "scorecard.json").read_text())
            assert score["total_score"] == row["total_score"]
    smap = {r["ticker"]: r for r in screens}
    cmap = {r["ticker"]: r for r in companies}
    assert smap["CRWD"]["screening_decision"] == "WATCH"
    assert smap["CRWD"]["price_veto_status"] == "INVESTIGATE"
    assert smap["259960"]["screening_decision"] == "SCREEN_OUT"
    assert smap["259960"]["hard_veto_status"] == "FAIL"
    assert cmap["NET"]["decision"] == "REJECT" and cmap["NET"]["hard_veto_status"] == "INVESTIGATE"
    assert cmap["NVDA"]["decision"] == cmap["TSM"]["decision"] == "WATCH"
    assert all(r["total_score"] is None for r in qualitative)
    assert records("valuation-audit.jsonl") == audit()
    assert records("company-valuation-diagnostics.jsonl") == company_audit()
    for row in company_audit():
        for s in row["scenarios"].values():
            assert s["annual_positive_dilution"] >= 0
            assert s["terminal_per_share_growth"] <= .03 + 1e-12
    print(self_test())
    print("REASSESSMENT VALIDATION PASSED: 90 inventory / 40 reviewed / 50 preliminary; 10 company + 20 wave + 12 qualitative minus 2 overlap")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

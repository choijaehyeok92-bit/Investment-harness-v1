#!/usr/bin/env python3
"""Emit deterministic artifact content as JSON for review/apply_patch.

No file writes or remote operations. Historical inputs are read from a pinned
commit. Current assessments remain separate from historical numeric snapshots.
Usage: python scripts/build_astra_reassessment.py --group central|NVDA|...|all
"""
from __future__ import annotations
import argparse
import copy
import csv
import io
import json
import subprocess
from pathlib import Path
from reassessment_models import audit, company_audit, self_test

ROOT = Path(__file__).resolve().parents[1]
DEST = "reviews/2026-09-05-astra"
CFG = json.loads((ROOT / DEST / "inputs.json").read_text())
BASE = CFG["baseline_commit"]
DATE = CFG["as_of"]
CATS = ["structural_change_and_leadership", "customer_value_and_product", "moat_trajectory",
        "incremental_roic_and_fcf_per_share", "management_and_capital_allocation",
        "financial_survivability", "expectation_gap_and_valuation", "power_law_and_asymmetry"]
MAXIMA = [15, 10, 15, 15, 10, 10, 15, 10]
SCATS = ["structural_growth", "business_momentum", "moat_trajectory", "reinvestment_quality",
         "financial_survivability", "outlier_optionality", "expectation_gap_proxy"]
SMAX = [10, 6, 10, 8, 5, 5, 6]
VETOES = ["management_or_accounting_integrity", "external_capital_dependence", "persistent_dilution",
          "low_quality_growth", "incremental_roic_collapse", "moat_shrinkage",
          "price_requires_unrealistic_bull_case", "fatal_concentration", "permanent_loss_probability"]


def at(path, rev=BASE):
    return subprocess.check_output(["git", "show", f"{rev}:{path}"], cwd=ROOT, text=True)


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def jsonlines(rows):
    return "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)


def lines_at(path):
    return [json.loads(line) for line in at(path).splitlines() if line.strip()]


def total(scores):
    return None if any(s is None for s in scores) else sum(scores)


def band(n):
    return None if n is None else "A" if n >= 42 else "B" if n >= 36 else "WATCH" if n >= 30 else "NEEDS_DATA" if n >= 24 else "REJECT"


def classification(n):
    return "Exceptional Outlier" if n >= 90 else "Core Outlier" if n >= 85 else "Emerging Outlier" if n >= 75 else "Starter / Watch" if n >= 65 else "Reject"


def restore(ticker, filename):
    path = f"companies/{ticker}/{filename}"
    raw = at(path)
    try:
        return json.loads(raw), BASE
    except json.JSONDecodeError:
        if ticker == "012450":
            if filename == "valuation.json":
                # Exact intact first object, with only the missing final brace supplied.
                return json.loads(raw.split("=======")[0] + "}"), BASE + ":first-SOTP"
            ref = "b5810b5" if filename == "scorecard.json" else "18bc9b2"
        else:
            ref = CFG["companies"][ticker]["restore_ref"]
        return json.loads(at(path, ref)), ref


def screen_records():
    prior = {r["ticker"]: r for r in lines_at("screening/2026-09-us-kr/provisional-scorecards-wave-01-02.jsonl")}
    decisions = {r["ticker"]: r for r in lines_at("screening/2026-09-us-kr/stage1-decisions-wave-01-02.jsonl")}
    models = {r["ticker"]: r for r in audit()}
    output = []
    for ticker, config in CFG["screens"].items():
        old, model = prior[ticker], models[ticker]
        scores = {}
        for key, maxscore, value in zip(SCATS, SMAX, config["scores"]):
            historical = old.get("scores", {}).get(key, old.get("expectation_gap_proxy", {}))
            scores[key] = {
                "score": value, "max_score": maxscore,
                "evidence": [historical.get("evidence", config["gap"])],
                "counter_evidence": [historical.get("counter_evidence", config["next"]), config["finding"]],
                "source": config.get("source", "screening/2026-09-us-kr/" + old["source_evidence"]),
                "confidence": .45 if value is None else .55 if key == "expectation_gap_proxy" else .65,
                "claim_type": "opinion", "missing_data": [config["next"]],
                "historical_score": historical.get("score"),
            }
        n = total(config["scores"])
        status = "FAIL" if ticker == "259960" else "INVESTIGATE"
        flags = list(old["hard_red_flag"]["ids"])
        if ticker in ("CRWD", "000660", "005380", "012450", "196170"):
            flags = list(dict.fromkeys(flags + ["price_requires_unrealistic_bull_case"]))
        row = {
            "ticker": ticker, "market": old["market"], "as_of": DATE,
            "framework": "screening-50-v1.0", "score_status": "EVIDENCE_INSUFFICIENT" if n is None else "PROVISIONAL_REASSESSED",
            "scores": scores, "total_score": n, "priority_band": band(n),
            "screening_decision": "SCREEN_OUT" if status == "FAIL" else "WATCH",
            "hard_veto_status": status, "open_veto_ids": flags,
            "price_veto_status": "INVESTIGATE" if ticker in ("CRWD", "000660", "005380", "012450", "196170") else "PASS",
            "promotion_status": "BLOCKED_HARD_VETO" if status == "FAIL" else "BLOCKED_EVIDENCE_OR_INVESTIGATE",
            "completion_status": "REASSESSMENT_DONE_NOT_FULL_COMPANY_ANALYSIS",
            "prior_decision_record": decisions[ticker],
            "finding": config["finding"], "expectation_gap_reason": config["gap"],
            "permanent_loss_case": config["loss"], "thesis_falsifier": config["loss"] + "가 실제 공시·고객·현금자료로 확인됨.",
            "increase_evidence": [config["next"], "열린 veto 해소 및 검증된 주당 가치 대비 안전마진 확보"],
            "exit_evidence": [config["loss"] + "를 뒷받침하는 지속적 증거", "경영진·회계 신뢰의 중대한 훼손"],
            "next_evidence": config["next"], "valuation_model_ref": "valuation-audit.jsonl#" + ticker,
            "source_quality": "기존 원천자료와 반대근거를 재심사. source 지정 종목만 이번 회차 원문 재열람. 모든 과거 수치를 독립 재검증했다는 뜻은 아님.",
            "confidence": .45 if n is None else .65,
        }
        output.append(row)
    return output


def qualitative_records():
    prior = {r["ticker"]: r for r in lines_at("screening/2026-09-04/screen-results.jsonl")}
    rows = []
    for ticker, config in CFG["qualitative"].items():
        old = prior[ticker]
        ids = []
        for flag in old.get("veto_flags", []):
            vid = flag["id"]
            if vid not in VETOES:
                # A capital-allocation concern is not a new policy veto ID.
                vid = "incremental_roic_collapse"
            if flag["status"] != "PASS":
                ids.append(vid)
        rows.append({
            "ticker": ticker, "company_name": old["company_name"], "market": old["market"], "as_of": DATE,
            "framework": "screening-50-v1.0", "score_status": "EVIDENCE_INSUFFICIENT",
            "scores": {k: {"score": None, "max_score": m, "missing_data": [config["next"]]} for k, m in zip(SCATS, SMAX)},
            "total_score": None, "priority_band": None, "old_decision": old["verdict"], "screening_decision": "WATCH",
            "hard_veto_status": "INVESTIGATE", "open_veto_ids": list(dict.fromkeys(ids)),
            "finding": config["finding"], "supporting_hypothesis": old["positive_signals"],
            "counter_evidence": old["uncertainties"], "next_evidence": config["next"],
            "permanent_loss_case": config["loss"], "thesis_falsifier": config["loss"] + "의 지속적 확인",
            "increase_evidence": [config["next"], "증거 게이트와 기대차 모형 완성"], "exit_evidence": [config["loss"] + "의 현실화"],
            "source_references_inherited_not_reverified": old["sources"],
            "source_quality": "정성 판단 재심사 완료. 기존 자료가 보도/요약 중심이고 원문·희석·역산 게이트 부족; 신규 정량실사 완료가 아님.",
            "completion_status": "QUALITATIVE_REVIEW_DONE_QUANTITATIVE_GATE_OPEN", "confidence": .4,
        })
    return rows


def company_records():
    rows = []
    for ticker, config in CFG["companies"].items():
        oldscore, ref = restore(ticker, "scorecard.json")
        categories = copy.deepcopy(oldscore["categories"])
        for key, score in zip(CATS, config["new_scores"]):
            categories[key]["evidence"] = categories[key]["evidence"][:2]
            categories[key]["counter_evidence"] = categories[key]["counter_evidence"][:2]
            categories[key]["missing_data"] = categories[key]["missing_data"][:2]
            categories[key]["score"] = score
            categories[key]["confidence"] = min(categories[key]["confidence"], config["confidence"] + .08)
            if ticker == "AVGO":
                # Do not carry the erroneous distributor=end-customer claim into current evidence.
                categories[key]["evidence"] = [config["support"], "기존 FY2025/H1 공시: 과거 근거는 baseline commit 참조."]
                categories[key]["counter_evidence"] = [config["counter"]]
            categories[key]["evidence"].append("2026-09-05 재심사 의견: " + config["score_changes"].get(key, "기존 지지·반대근거 재심사. 상세 현재 finding/counter_evidence는 재평가 레코드와 re-evaluation-2026-09-05.md 참조."))
            if key in config["score_changes"]:
                categories[key]["counter_evidence"].append(config["counter"])
            categories[key]["missing_data"].append(config["next"])
        if ticker == "AVGO":
            categories["expectation_gap_and_valuation"]["evidence"].append("기존 5년 연 1.8% 수익과 9% 허들의 불일치, Q3 개선 후에도 완료되지 않은 owner-FCF 역산을 감안해 7→6.")
        veto, vref = restore(ticker, "hard-veto.json")
        veto["as_of"] = DATE
        if ticker in ("NET", "AVGO"):
            for flag in veto["vetoes"]:
                if ticker == "AVGO":
                    flag["evidence"] = ["기존 원문·공식 Q3를 재심사한 현재 의견: " + config["support"], config["counter"]]
                if flag["id"] == "price_requires_unrealistic_bull_case":
                    flag.update(status="INVESTIGATE", confidence=.65, severity="HIGH",
                                evidence=[config["finding"], "비현실적 실행의 범위를 입증하지 못했으며 높은 가격 자체는 FAIL의 충분조건이 아니다."],
                                resolution_needed=config["next"])
        if ticker == "NVDA":
            for flag in veto["vetoes"]:
                if flag["id"] in ("low_quality_growth", "fatal_concentration", "permanent_loss_probability"):
                    flag["evidence"].append(config["counter"])
                    flag["resolution_needed"] = config["next"]
        for flag in veto["vetoes"]:
            flag["confidence"] = min(flag["confidence"], config["confidence"] + .1)
        overall = "FAIL" if any(v["status"] == "FAIL" for v in veto["vetoes"]) else "INVESTIGATE" if any(v["status"] == "INVESTIGATE" for v in veto["vetoes"]) else "PASS"
        veto["overall_status"] = overall
        rows.append({
            "ticker": ticker, "company_name": config["name"], "as_of": DATE, "framework": "company-100-v1.0",
            "old_score": config["old_score"], "total_score": total(config["new_scores"]), "categories": categories,
            "score_status": "EVIDENCE_INSUFFICIENT" if total(config["new_scores"]) is None else "REASSESSED_WITH_OPEN_LIMITATIONS",
            "decision": config["label"], "hard_veto_status": overall, "hard_veto_report": veto,
            "position_band": "NONE", "finding": config["finding"], "support": config["support"],
            "counter_evidence": config["counter"], "permanent_loss_case": config["loss"],
            "thesis_falsifier": config["falsifier"], "increase_evidence": [config["next"], "사업 악화 없이 검증된 주당 가치 대비 안전마진 확보"],
            "exit_evidence": [config["falsifier"], "중대한 경영진·회계 신뢰 훼손"],
            "source_ledger": f"../../companies/{ticker}/evidence.jsonl", "restored_scorecard_from": ref,
            "restored_veto_from": vref, "new_primary_source": config.get("new_primary_source"),
            "source_quality": "원천 우선. 첨부 공시·기존 원문 기록과 이번 직접 확인 출처의 구분은 source-audit.md 참조. 기존 원문 전체의 독립 재실사 또는 실시간 가격 갱신을 의미하지 않는다.",
            "completion_status": "REASSESSMENT_DONE_VALUATION_AND_MONITORING_LIMITS_OPEN",
            "confidence": config["confidence"], "next_evidence": config["next"],
        })
    return rows


def company_files(row):
    ticker = row["ticker"]
    config = CFG["companies"][ticker]
    prefix = f"companies/{ticker}/"
    files = {}
    oldscore, ref = restore(ticker, "scorecard.json")
    olddecision, _ = restore(ticker, "decision.json")
    valuation, vref = restore(ticker, "valuation.json")
    if row["total_score"] is None:
        # The existing schema disallows null scores. Preserve an explicitly dated
        # historical snapshot; the new review's nullable score is authoritative.
        scorecard = oldscore
        for category in scorecard["categories"].values():
            category["evidence"].insert(0, "과거 71점 복구본; 2026-09-05 현재 총점은 보류. 최신 판단은 re-evaluation-2026-09-05.md 및 reviews/latest.json을 따른다.")
    else:
        scorecard = {"ticker": ticker, "as_of": DATE, "categories": row["categories"],
                     "total_score": row["total_score"], "classification": classification(row["total_score"])}
    files[prefix + "scorecard.json"] = dump(scorecard)
    files[prefix + "hard-veto.json"] = dump(row["hard_veto_report"])
    decision = {
        "ticker": ticker, "as_of": DATE, "label": row["decision"], "hard_veto_status": row["hard_veto_status"],
        "position_band": "NONE", "rationale": config["finding"] + " " + config["counter"] + " " +
        (config.get("withhold_reason", "") or f"재평가 {row['total_score']}/100. 점수는 매수 승인이 아니며 가치평가/조사 한계는 최신 재심사 파일에 명시했다."),
        "increase_evidence": row["increase_evidence"], "reduce_or_exit_evidence": row["exit_evidence"],
        "macro_pacing": "company_specific", "confidence": row["confidence"],
    }
    files[prefix + "decision.json"] = dump(decision)
    legacy_implied = valuation["implied_expectations"]
    valuation["implied_expectations"] = {
        "latest_review": "re-evaluation-2026-09-05.md",
        "review_as_of": DATE, "reference_price_is_frozen": True,
        "current_required_return": .10 if ticker.isdigit() else .09,
        "legacy_implied_expectations_NOT_REVALIDATED": legacy_implied,
        "current_findings": [config["finding"], config["counter"]],
        "current_model_limit": config["next"],
    }
    diagnostic = next((x for x in company_audit() if x["ticker"] == ticker), None)
    if diagnostic:
        valuation["implied_expectations"]["uniform_hurdle_diagnostic"] = diagnostic
    if ticker == "AVGO":
        valuation["implied_expectations"]["new_primary_q3_fy2026_usd_b"] = {
            "source": config["new_primary_source"], "revenue": 29.591, "gaap_operating_income": 15.955,
            "gaap_net_income": 13.088, "ocf": 14.197, "capex": .532, "fcf": 13.665,
            "sbc": 2.019, "cash": 23.975, "short_debt": 2.252, "long_debt": 57.167,
            "net_debt_ex_leases_proxy": 35.444, "gaap_diluted_shares_b": 4.887,
            "software_revenue": 8.752, "software_growth_yoy": .29,
            "fcf_less_sbc_cost_proxy": 11.646,
            "price_times_gaap_diluted_shares_equity_proxy": valuation["current_price"] * 4.887,
            "note": "가격은 기존 357.16달러 유지. 희석 가중평균 주식수는 시점 기본주식수와 다르므로 지분가치 민감도다."
        }
    for case in valuation["scenarios"].values():
        case["review_status"] = "LEGACY_SCENARIO_ARCHIVED_FOR_COMPARISON_NOT_CURRENT_APPROVED_VALUE"
    valuation["notes"] = "2026-09-05 재심사: 상위 scenarios와 legacy_implied_expectations는 복구·보존한 과거 추정치이며 승인된 현재 가치가 아니다. 최신 판단은 re-evaluation-2026-09-05.md, 통일 허들 진단은 implied_expectations.uniform_hurdle_diagnostic(해당 종목)을 참조. 보고 FCF와 owner-FCFE의 비용·희석 브리지는 미완성이다. 총점 보류 종목의 상위 기대차/비대칭 점수도 과거 스냅샷이다.\n기존 모델 메모(과거): " + (valuation.get("notes") or "")
    # Keep the historical as_of and scoring fields together; new score is in the
    # explicit current_review record, avoiding a false claim of a rebuilt model.
    files[prefix + "valuation.json"] = dump(valuation)
    evidence = []
    seen = set()
    for line in at(prefix + "evidence.jsonl").splitlines():
        if not line.strip() or line.strip() == "=======":
            continue
        value = json.loads(line)
        canonical = json.dumps(value, sort_keys=True)
        if canonical not in seen:
            evidence.append(value)
            seen.add(canonical)
    evidence.append({"date": DATE, "ticker": ticker, "signal": "ASTRA_REASSESSMENT",
                     "thesis_component": "expectation_gap_and_valuation", "direction": "NEUTRAL",
                     "strength": row["confidence"], "claim_type": "opinion", "summary": config["finding"],
                     "source": f"{DEST}/README.md", "analyst_note": "과거 충돌 주장은 삭제하지 않고 역사로 보존. 현행 판단은 동일 날짜 재평가 오버레이가 우선한다."})
    if ticker == "AVGO":
        evidence.append({"date": DATE, "ticker": ticker, "signal": "Q3_GAAP_AND_SOFTWARE_RECHECK",
                         "thesis_component": "moat_trajectory", "direction": "SUPPORTS", "strength": .9,
                         "claim_type": "fact", "summary": "Q3 FY2026 공식 실적: GAAP 영업이익 $15.955B, FCF $13.665B, 소프트웨어 매출 $8.752B(+29%). 기존 GAAP 자료 부재·소프트웨어 저성장 주장을 정정.",
                         "source": config["new_primary_source"], "analyst_note": "고객집중과 미래 약정은 별도의 미해결 질문이다."})
    files[prefix + "evidence.jsonl"] = jsonlines(evidence)
    historical = at(prefix + "decision-history.md")
    scoretxt = "보류" if row["total_score"] is None else f"{row['total_score']}/100"
    files[prefix + "decision-history.md"] = historical.rstrip() + f"\n\n## {DATE} — Astra 재심사\n\n- 과거: {config['old_score']}; 현재: {scoretxt}, {row['decision']}, {row['hard_veto_status']}, 포지션 밴드 NONE.\n- {config['finding']}\n- [현재 재평가](re-evaluation-2026-09-05.md). 이전 판정은 역사이며 주문·거래는 실행하지 않았다.\n"
    notice = f"> 최신 판단: **{DATE} / {row['decision']} / {scoretxt} / {row['hard_veto_status']}**. [한글 재평가](re-evaluation-2026-09-05.md)가 아래 과거 서술보다 우선합니다. 아래 원문은 이력 비교를 위해 보존합니다.\n\n"
    files[prefix + "thesis.md"] = notice + at(prefix + "thesis.md")
    md = f"# {config['name']} ({ticker}) — {DATE} 재평가\n\n"
    md += f"판정 **{row['decision']}**, 점수 **{scoretxt}**, Hard Veto **{row['hard_veto_status']}**, 신규 포지션 **NONE**.\n\n{config['finding']}\n\n"
    md += "## 근거와 반대근거\n\n" + config["support"] + "\n\n" + config["counter"] + "\n\n"
    md += "사실은 원문/공시에서 온 관측값, 미래 성장·마진·손실 범위는 추정, 인과관계는 추론, 점수와 판정은 의견이다. 숫자 모델은 확률 예측이나 목표주가가 아니다.\n\n"
    md += "## 동일 100점 체계\n\n| 항목 | 재평가 | 배점 | 근거·한계 |\n|---|---:|---:|---|\n"
    for key, maximum in zip(CATS, MAXIMA):
        value = row["categories"][key]["score"]
        note = config["score_changes"].get(key, "기존 근거·반대근거 재심사; 세부 evidence/missing_data는 기계 기록 참조.")
        if value is None:
            note = config.get("withhold_reason", "근거 부족")
        md += f"| {key} | {'보류' if value is None else value} | {maximum} | {note} |\n"
    md += "\n[현재 8개 항목의 근거·반대근거·신뢰도](../../" + DEST + "/company-reassessments.jsonl). 50점 스크리닝과 합산·비례 환산하지 않는다.\n\n"
    md += "## Hard Veto\n\n| 항목 | 상태 | 해소 조건 |\n|---|---|---|\n"
    for flag in row["hard_veto_report"]["vetoes"]:
        resolution = (flag["resolution_needed"] or "현재 중대한 반증 미확인; 다음 공시에서 계속 점검").replace("|", "/").replace("\n", " ")
        md += f"| {flag['id']} | {flag['status']} | {resolution} |\n"
    md += f"\n## 가격과 시나리오\n\n기준 가격 **{valuation['current_price']:,.2f}** ({'KRW' if ticker.isdigit() else 'USD'})는 기존 분석 가격이다. 실시간 또는 동일 일자 종가 비교가 아니다. 원래 시각은 [가치평가 기록](valuation.json)의 legacy 필드 참조.\n\n"
    if diagnostic:
        md += "동일 9% 허들·3% 회사 말기 FCF 성장률의 **방법론 진단**이다. 비상장투자 제외, 무상 환매효과 제거, 말기 양의 희석 반영으로 과거 모형과 달라진다. 보상비용/환매 재원이 완성된 owner-FCFE 가치는 아니다.\n\n| 시나리오 | 진단 PV/주 (USD) | 기준가 대비 |\n|---|---:|---:|\n"
        for case, values in diagnostic["scenarios"].items():
            md += f"| {case} | {values['diagnostic_present_value_per_share_usd']:.2f} | {(values['value_to_reference_price']-1)*100:+.1f}% |\n"
    else:
        md += "Bear/Base/Bull의 과거 입력은 valuation.json에 명시적으로 역사 자료로 보존했다. 아래 질문이 해결되기 전 그 숫자를 현재 승인 가치로 재사용하지 않는다.\n\n"
    md += "\n현재 핵심 모델 한계: " + config["next"] + "\n\n"
    md += "## 영구손실과 반증\n\n" + config["loss"] + "\n\n**논지 반증:** " + config["falsifier"] + "\n\n"
    md += "**증액 전 필요한 증거:** " + config["next"] + " 사업 개선과 가격 기대차를 함께 확인해야 하며 가격 하락만으로 매수하지 않는다.\n\n"
    md += "**축소·매도 재검토:** 논지 반증이 지속되거나 경영진·회계 신뢰가 중대하게 훼손되는 경우. 실제 보유 여부를 확인하지 않았으므로 이는 조건부 모니터링 규칙이며 거래 지시가 아니다.\n\n"
    md += "## 출처·완료 범위\n\n[evidence.jsonl](evidence.jsonl), [출처 감사](../../" + DEST + "/source-audit.md), [전체 비교](../../" + DEST + "/README.md).\n\n"
    if config.get("new_primary_source"):
        md += "[이번 직접 확인한 회사 공식 자료](" + config["new_primary_source"] + ").\n\n"
    md += f"재심사 판단 신뢰도 {row['confidence']:.0%}. 종목 재평가 기록은 완료했지만 열린 가치평가·증거 게이트까지 해소됐다는 뜻은 아니다. 원문 전체 재실사·실시간 시세 갱신·거래 실행은 하지 않았다.\n"
    files[prefix + "re-evaluation-2026-09-05.md"] = md
    return files


def coverage(companies, screens, qualitative):
    inventory = {}
    for path in ("screening/2026-09-us-kr/universe.csv", "screening/universe-2026-09.csv"):
        for row in csv.DictReader(io.StringIO(at(path))):
            ticker = row["ticker"]
            entry = inventory.setdefault(ticker, {"ticker": ticker, "company_name": row["company_name"], "market": row["market"], "inherited_universes": []})
            entry["inherited_universes"].append(path)
    for row in companies + screens + qualitative:
        ticker = row["ticker"]
        entry = inventory.setdefault(ticker, {"ticker": ticker, "company_name": row.get("company_name", ticker), "market": "KR" if ticker.isdigit() else "US", "inherited_universes": []})
        entry.setdefault("review_levels", []).append(row["framework"] if row in companies + screens else "QUALITATIVE")
        if row in companies:
            entry["company_score_100"] = row["total_score"]
            entry["current_company_decision"] = row["decision"]
        else:
            entry["screen_score_50"] = row["total_score"]
            entry["current_screen_decision"] = row["screening_decision"]
        entry["review_status"] = "REASSESSED_AT_EXISTING_EVIDENCE_LEVEL"
    for ticker, entry in inventory.items():
        if "review_status" not in entry:
            entry.update(review_status="UNREVIEWED_PRELIMINARY_ONLY", review_levels=[],
                         score=None, decision=None, note="예비/보류 목록에만 있었음. 이번 재평가 완료 종목으로 계산하지 않는다.")
        if ticker == "GOOGL":
            entry["aliases_same_business"] = ["GOOG"]
    return sorted(inventory.values(), key=lambda row: (row["market"], row["ticker"]))


def integrity_audit():
    problems = []
    for ticker in CFG["companies"]:
        for name in ("decision.json", "scorecard.json", "hard-veto.json", "valuation.json", "evidence.jsonl"):
            path = f"companies/{ticker}/{name}"
            raw = at(path)
            try:
                if name.endswith(".jsonl"):
                    for line in raw.splitlines():
                        if line.strip():
                            json.loads(line)
                else:
                    json.loads(raw)
            except json.JSONDecodeError as error:
                provenance = "valid historical ledger entries retained; lone separator removed" if name.endswith(".jsonl") else restore(ticker, name)[1]
                problems.append({"path": path, "baseline_commit": BASE, "error": str(error),
                                 "recovery_source": provenance,
                                 "policy": "Prior bytes recoverable from Git history; do not silently select a conflicting verdict. Current review adjudicates the economic judgment."})
    return {"as_of": DATE, "invalid_files_before": len(problems), "affected_companies": sorted({p["path"].split("/")[1] for p in problems}), "files": problems}


def central_files(companies, screens, qualitative):
    universe = coverage(companies, screens, qualitative)
    models = audit()
    modelmap = {m["ticker"]: m for m in models}
    reviewed = [u for u in universe if u["review_status"].startswith("REASSESSED")]
    assert len(universe) == 90 and len(reviewed) == 40
    files = {
        f"{DEST}/coverage.json": dump(universe),
        f"{DEST}/company-reassessments.jsonl": jsonlines(companies),
        f"{DEST}/screen-reassessments.jsonl": jsonlines(screens),
        f"{DEST}/qualitative-reassessments.jsonl": jsonlines(qualitative),
        f"{DEST}/valuation-audit.jsonl": jsonlines(models),
        f"{DEST}/company-valuation-diagnostics.jsonl": jsonlines(company_audit()),
        f"{DEST}/data-integrity-audit.json": dump(integrity_audit()),
    }
    progress = {
        "as_of": DATE, "baseline_commit": BASE, "review_status": "COMPLETED_AT_EXISTING_EVIDENCE_LEVEL",
        "all_research_gates_closed": False, "harness_policy_changed": False, "market_prices_refreshed": False,
        "unique_universe": 90, "unique_previously_assessed_reassessed": 40, "preliminary_only_not_claimed_complete": 50,
        "company_packages_reviewed": 10, "company_scores_numeric": 9, "company_total_withheld": ["012450"],
        "wave_screen_reviews": 20, "wave_provisional_numeric_scores": 16,
        "wave_totals_withheld": ["000660", "005380", "012450", "196170"],
        "additional_qualitative_reviews": 12, "company_wave_overlap": ["AXON", "012450"],
        "repaired_invalid_files": 13, "new_buy_approvals": 0, "orders_executed": 0,
        "us_research_priority_not_promotion": ["NOW", "AMZN", "MSFT", "LLY", "VRTX"],
        "kr_research_priority_not_promotion": ["035420", "207940", "278470"],
        "kr_data_repair_priority": ["005380", "000660", "012450", "196170"],
        "existing_company_quality_watch_priority": ["ISRG", "TSM", "NVDA"],
        "valuation_model_tests": self_test(),
        "next_action": "Resolve named cash-flow/ownership/source gates before promoting, not fill a five-name quota.",
    }
    files[f"{DEST}/progress.json"] = dump(progress)
    files["reviews/latest.json"] = dump({
        "as_of": DATE, "directory": DEST, "report": f"{DEST}/README.md",
        "authority": "Current reassessment overlay supersedes earlier decisions/scores only for explicitly reviewed tickers. Earlier screens and scenarios remain historical.",
        "company_decisions": "companies/<TICKER>/decision.json",
        "company_score_overlay": f"{DEST}/company-reassessments.jsonl",
        "screen_decisions": f"{DEST}/screen-reassessments.jsonl",
        "qualitative_decisions": f"{DEST}/qualitative-reassessments.jsonl",
        "withheld_score_rule": "A null current review score is unknown, NOT zero or the preserved historical scorecard.",
    })
    oldprogress = json.loads(at("screening/2026-09-us-kr/progress.json"))
    files["screening/2026-09-us-kr/progress.json"] = dump({
        "run_id": oldprogress["run_id"], "as_of": DATE, "stage": "SUPERSEDED_BY_ASTRA_REASSESSMENT",
        "active_review": "../../" + DEST + "/README.md",
        "active_progress": "../../" + DEST + "/progress.json",
        "correction": "기존 all_20_scores_complete는 현재 승인 상태가 아니다. 현재 16개 잠정 점수와 4개 보류; 50개 예비후보 미심사.",
        "historical_checkpoint_do_not_use_as_current": oldprogress,
    })
    for path, link in (("README.md", DEST + "/README.md"),
                       ("screening/2026-09-us-kr/README.md", "../../" + DEST + "/README.md")):
        files[path] = "> 현재 연구 상태: [2026-09-05 Astra 재평가](" + link + "). 40개 기존 판단 재심사, 50개 예비후보는 미심사. 과거 스크리닝 점수·판정을 현재 승인으로 사용하지 마세요.\n\n" + at(path)
    redteam = []
    for row in companies + screens + qualitative:
        redteam.append({"ticker": row["ticker"], "framework": row["framework"], "as_of": DATE,
                        "verdict": "REJECT" if row.get("decision") == "REJECT" or row.get("screening_decision") == "SCREEN_OUT" else "REVISE",
                        "strongest_challenge": row.get("counter_evidence", row["finding"]),
                        "permanent_loss": row["permanent_loss_case"], "revision_applied": row["finding"],
                        "remaining_gate": row["next_evidence"], "approval_to_buy": False})
    files[f"{DEST}/red-team.jsonl"] = jsonlines(redteam)
    md = "# Astra 동일 하네스 재평가 — 2026-09-05\n\n"
    md += "**기존 판정이 있는 40개 종목의 재심사 기록을 저장했다. 신규 매수 승인은 0개다.** 전체 목록은 중복 제거 90개이며 나머지 50개는 예비후보 상태로 남긴다. 40개 전부의 최신 원문·가치평가가 완성됐다는 뜻은 아니다.\n\n"
    md += "## 범위와 동일 기준\n\n- 기존 기업분석 10개: 100점 체계. 9개 점수 재평가, 한화에어로스페이스 총점 보류.\n- Wave 01·02 20개: 50점 체계. 16개 잠정 점수, 4개 보류. AXON·한화는 기업분석과 중복.\n- 추가 정성 스크리닝 12개: 판단 재심사와 조사 게이트 설정, 근거 부족으로 새 숫자 점수 없음.\n- 따라서 10 + 20 − 2 + 12 = 40개. GOOG/GOOGL은 한 기업으로 계산. TSM은 미국 상장 ADS이나 국가 위험은 대만.\n\n"
    md += "하네스 철학·9개 Hard Veto·배점·분류 기준은 변경하지 않았다. 모델 변경은 증거가 아니므로 점수 상승/하락을 할당하지 않고, 개별 가정·출처·경제가치 해석을 재심사했다. 각 종목의 긍정 근거와 반대근거를 유지했다. 사실/추정/추론/의견, 기업 품질/가격 기대/포트폴리오 위험을 분리했다.\n\n"
    md += "기존 종목별 가격을 고정해 방법론 차이를 비교한다. 실시간 가격, 2026-09-05 종가 또는 같은 시각의 횡단면이 아니다. 미국 9%·한국 10%는 기존 스크리닝 허들로 유지하며, 이를 예전 모든 회사 모형이 이미 사용했던 것처럼 소급하지 않는다. 별도 회사 진단은 9%로 통일한 민감도임을 표시했다.\n\n"
    md += "## 바뀐 핵심 판단\n\n1. **NVDA·TSM: STARTER 근거 철회, WATCH.** 충돌하던 NVDA 두 판정을 통일했다. 기존 5년 기대수익률을 연율화한 약 3.9%·6.6%는 9% 허들보다 낮고, 가격÷성숙기 PER는 시간가치가 있는 역산이 아니다. 이는 보유분 매도 명령이 아니라 신규 조사 판정이다.\n2. **CRWD: SCREEN_OUT → WATCH.** 설정된 공격적 Bull이 허들을 넘는다는 사실을 가격 FAIL의 근거로 사용할 수 없다. **NET: 가격 FAIL → INVESTIGATE이나 58점/REJECT 유지.** 하나의 분석가 Bull이 낮다는 것과 현실적 Bull 전체가 불가능하다는 것은 다르다. 비싼 가격을 싸다고 바꾼 것이 아니다.\n3. **AVGO: 68 → 71.** 공식 Q3 GAAP 표가 존재하며 소프트웨어 매출도 29% 성장했다. 단일 유통업체 42%를 단일 최종고객 수요로 취급하지 않고, 영업권 손상을 즉시 현금손실/파산으로 해석하지 않는다. [공식 Q3 실적](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-third-quarter-fiscal-year-2026-financial).\n4. **총점 확정 철회: SK하이닉스·현대차·알테오젠, 그리고 한화 Wave 모형.** 정상화 현금흐름·금융 규제자본·계약별 조건부 현금·소수주주 귀속이 미완성이다. 잘못된 모형을 채웠다는 이유로 점수를 확정하지 않는다.\n5. **크래프톤: SCREEN_OUT 유지.** 법원 판단에 기초한 경영진 신뢰 veto다. 범죄나 분식을 단정하는 판정이 아니며 합의/후속 통제 개선을 재검토 조건으로 둔다.\n\n"
    md += "## 기업분석 10개 — 100점\n\n| 종목 | 이전 점수 | 재평가 /100 | 현재 판정 | Hard Veto |\n|---|---|---:|---|---|\n"
    for row in sorted(companies, key=lambda r: -(r["total_score"] if r["total_score"] is not None else -1)):
        name = f"[{row['ticker']} {row['company_name']}](../../companies/{row['ticker']}/re-evaluation-2026-09-05.md)"
        md += f"| {name} | {row['old_score']} | {'보류' if row['total_score'] is None else row['total_score']} | {row['decision']} | {row['hard_veto_status']} |\n"
    md += "\n한화의 기존 `scorecard.json` 71점은 스키마에 맞춘 **과거 복구본**이다. 현재 점수는 `company-reassessments.jsonl`의 null/보류가 우선한다. ISRG의 Veto PASS도 안전마진이나 매수 승인을 뜻하지 않는다.\n\n"
    for market, title in (("US", "미국"), ("KR", "한국")):
        md += f"## {title} Wave 재평가 — 50점\n\n| 종목 | 이전 /50 | 현재 /50 | 점수대 | 현재 판정 | 다음 게이트 |\n|---|---:|---:|---|---|---|\n"
        for row in sorted([r for r in screens if r["market"] == market], key=lambda r: -(r["total_score"] if r["total_score"] is not None else -1)):
            oldn = row["prior_decision_record"]["total_score"]
            md += f"| {row['ticker']} | {oldn} | {'보류' if row['total_score'] is None else row['total_score']} | {row['priority_band'] or '미정'} | {row['screening_decision']} | {row['next_evidence']} |\n"
        md += "\nA/B는 점수대이며 열린 INVESTIGATE를 해소한 승격 상태가 아니다. 모든 숫자는 근거·반대근거·신뢰도를 포함한 잠정 판단이다.\n\n"
    md += "## 수익률 계산 재검증\n\n과거 'IRR'은 연중 FCF를 현금수익률 0%로 쌓아 10년 말에 받는 **말기부 CAGR**이었다. 그 현금정책이라면 계산은 성립하지만 매년 배분받는 IRR과 같지 않다. 이번에는 두 경우를 별도로 재현했다. IRR 계산이 재투자를 보장하는 것도 아니다.\n\n"
    md += "`FCF_t = Revenue_0 × (1+g)^t × [m0 + (m10−m0)×t/10]`\n\n`PV = Σ FCF_t/(1+r)^t + (FCF_10 × terminal P/FCF)/(1+r)^10`\n\nIRR은 이 식의 PV가 기준 지분가치와 일치하는 r이다. 중간현금과 말기 순현금을 중복 가산하지 않는다. 마진은 Capex·이자·경제적 보상비용 이후의 가정이며, 보고 FCF와의 브리지 미완성을 표시했다. 연결 금융업·소수주주·조건부 로열티에는 이 공통식을 의사결정용으로 적용하지 않는다.\n\n"
    md += "| 종목 | 허들 | Base 말기부 CAGR | Base 연간배분 IRR | Bull 연간배분 IRR | 사용 범위 |\n|---|---:|---:|---:|---:|---|\n"
    for ticker in ("NOW", "AMZN", "MSFT", "CRWD", "035420", "259960"):
        m = modelmap[ticker]
        base, bull = m["scenarios"]["base"], m["scenarios"]["bull"]
        md += f"| {ticker} | {m['hurdle_rate']:.0%} | {base['zero_yield_retained_cash_terminal_wealth_cagr']:.1%} | {base['hypothetical_annual_distribution_irr']:.1%} | {bull['hypothetical_annual_distribution_irr']:.1%} | 가정 민감도, 매수 승인 아님 |\n"
    md += "\n20개 모형 모두 연도별 현금·말기가치·역산 5/10년 성장·허들 +2%p·말기배수 −25% 민감도를 [valuation-audit.jsonl](valuation-audit.jsonl)에 저장했다. 현금 시점과 주주 귀속을 확인하지 않은 4개 모형은 산술 대조용일 뿐 기대차 점수에 사용하지 않는다. 확률가중 평균 부의 연율화는 기대 IRR도 기하평균 기대수익률도 아니며 이를 혼용하지 않는다.\n\n"
    md += "## 기존 회사 DCF의 통일 허들 진단\n\n| 종목 | 고정 기준가 | Bear | Base | Bull |\n|---|---:|---:|---:|---:|\n"
    for row in company_audit():
        vals = [row["scenarios"][s]["diagnostic_present_value_per_share_usd"] for s in ("bear", "base", "bull")]
        md += f"| {row['ticker']} | {row['reference_price']:.2f} | {vals[0]:.2f} | {vals[1]:.2f} | {vals[2]:.2f} |\n"
    md += "\n단위 USD/주. 전 사례 할인율 9%, 회사 말기 FCF 성장 3%, 비상장투자 제외, 무상 순소각 효과 없음, 양의 말기 희석 지속. **보고 FCF에서 경제적 보상·환매 재원으로 연결되는 브리지는 미완성이다. 따라서 완성된 내재가치나 목표주가가 아니다.** 한 가정만 바꾼 가격효과로 해석할 수도 없다. [입력·연도별 계산·변경사항](company-valuation-diagnostics.jsonl).\n\n"
    md += "## 추가 정성 재심사 12개\n\n| 종목 | 이전 | 현재 | 다음에 반드시 확인할 자료 |\n|---|---|---|---|\n"
    for row in qualitative:
        md += f"| {row['ticker']} | {row['old_decision']} | WATCH / 점수 보류 | {row['next_evidence']} |\n"
    md += "\n두산에너빌리티·파마리서치의 과거 SCREEN_IN은 초기 조사 초대였고 완성된 정량 통과와 구분했다. 이번 단계에서는 WATCH로 통일했으며 사업이 나빠졌다고 새 사실을 주장하는 변경은 아니다. [종목별 지지·반대·영구손실·반증](qualitative-reassessments.jsonl).\n\n"
    md += "## 조사 순서와 포트폴리오 한계\n\n- 미국 신규 조사: NOW → AMZN → MSFT → LLY → VRTX. 기대차와 해결 가능한 질문의 우선순위이며 100점 보유 순위가 아니다.\n- 한국: NAVER의 AI 투자 후 현금가치, 삼성바이오로직스의 공장 ROIC, APR의 재구매/CAC를 먼저 확인. 다섯 자리를 억지로 채우지 않는다.\n- 데이터 복구 별도 순서: 현대차·SK하이닉스·한화·알테오젠의 특수모형. 높은 가상 IRR을 이유로 승격하지 않는다.\n- 기존 정밀분석: ISRG·TSM·NVDA는 높은 품질의 관찰 대상. 현재 가격 기대차·고객/지역 꼬리위험을 별도로 통과해야 한다.\n- 실제 보유·원가·자산규모를 확인하지 않았으므로 포트폴리오 비중·매매는 실행하지 않는다. NVDA/AVGO/TSM/메모리/전력·냉각은 같은 AI 설비 지출에 연결돼 기업 수만으로 분산을 셀 수 없다. 이 상관은 위험예산에 반영하며 거시전망으로 회사 점수를 바꾸지 않는다.\n\n"
    md += "## 출처·복구·검증\n\n- [출처와 직접 재검증 범위](source-audit.md)\n- [13개 JSON/JSONL 손상 및 복구 출처](data-integrity-audit.json): NVDA만이 아니라 AVGO·한화에도 오류가 있었다. 과거 원문은 Git 이력에서 복원 가능.\n- [90개 범위 명세](coverage.json): 예비후보 50개를 분석 완료로 표시하지 않았다.\n- [현재 상태](progress.json), [레드팀 42개 단계별 기록](red-team.jsonl), [현재 판독 진입점](../latest.json). 단계 중복 2개 때문에 레드팀 행은 42개다.\n\n재현: `python scripts/reassessment_models.py --test`; `python scripts/validate_outputs.py`; `python scripts/validate_reassessment.py`. 생성기는 파일을 직접 덮어쓰지 않고 검토 가능한 JSON manifest를 출력한다. 정책·스키마 배점은 변경하지 않았다.\n"
    files[f"{DEST}/README.md"] = md
    return files


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--group", default="all")
    parser.add_argument("--patch", action="store_true")
    parser.add_argument("--file")
    parser.add_argument("--stats", action="store_true")
    args = parser.parse_args()
    companies, screens, qualitative = company_records(), screen_records(), qualitative_records()
    files = central_files(companies, screens, qualitative) if args.group in ("all", "central") else {}
    for row in companies:
        if args.group in ("all", row["ticker"]):
            files.update(company_files(row))
    if args.file:
        files = {path: content for path, content in files.items() if path == args.file}
        if not files:
            raise ValueError("Unknown output path")
    if args.stats:
        print(json.dumps({path: len(content) for path, content in files.items()}))
    elif args.patch:
        chunks = ["*** Begin Patch"]
        paths = []
        for path, content in files.items():
            target = ROOT / path
            old = target.read_text() if target.exists() else None
            if old == content:
                continue
            paths.append(path)
            if old is None:
                chunks.append("*** Add File: " + str(target))
            else:
                chunks.extend(["*** Update File: " + str(target), "@@"])
                chunks.extend("-" + line for line in old.splitlines())
            chunks.extend("+" + line for line in content.splitlines())
        chunks.append("*** End Patch")
        print(json.dumps({"paths": paths, "patch": "\n".join(chunks)}, ensure_ascii=False))
    else:
        print(json.dumps(files, ensure_ascii=False))


if __name__ == "__main__":
    main()

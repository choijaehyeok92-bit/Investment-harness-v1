#!/usr/bin/env python3
"""Read-only, reproducible cash-timing audit. Emits JSON; never writes artifacts.

The 2026-09-04 inputs are a frozen methodological comparison, not live quotes.
Annual-distribution IRR and zero-yield retained-cash CAGR are DIFFERENT cases.
Neither is a promised investor return. Normalized margins remain estimates.
"""
from __future__ import annotations
import csv
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WITHHELD = {
    "000660": "Cycle-normalized capex/owner cash flow has not been bridged to primary statements.",
    "005380": "Manufacturing FCFE, captive-finance capital and share classes need separation.",
    "012450": "Consolidated cash flow includes non-controlling interests; use parent SOTP/FCFE.",
    "196170": "Contract cash-flow dates, royalties and conditional program probabilities are missing.",
}


def cash_flows(revenue, growth, start_margin, end_margin, multiple, years=10):
    annual = [revenue * (1 + growth) ** t *
              (start_margin + (end_margin - start_margin) * t / years)
              for t in range(1, years + 1)]
    return annual, annual[-1] * multiple


def pv(annual, terminal, rate):
    return sum(c / (1 + rate) ** t for t, c in enumerate(annual, 1)) + terminal / (1 + rate) ** len(annual)


def solve_increasing(fn, target, lo=-0.90, hi=2.0):
    if not fn(lo) <= target <= fn(hi):
        return None
    for _ in range(100):
        mid = (lo + hi) / 2
        if fn(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def distribution_irr(annual, terminal, equity):
    # Positive operating cash flows make NPV monotone. No reinvestment assumption.
    return solve_increasing(lambda r: -pv(annual, terminal, r), -equity)


def audit():
    rows = []
    path = ROOT / "screening/2026-09-us-kr/reverse-expectations-wave-01-02.csv"
    for old in csv.DictReader(path.open()):
        equity, revenue, start = [float(old[k]) for k in
                                  ("equity_value", "ttm_revenue", "normalized_start_fcf_margin_pct")]
        start /= 100
        hurdle = float(old["hurdle_rate_pct"]) / 100
        row = {
            "ticker": old["ticker"], "market": old["market"], "as_of": "2026-09-05",
            "reference_price_date": old["as_of"], "scale_unit": old["scale_unit"],
            "input_source": str(path.relative_to(ROOT)),
            "source_status": "INHERITED_FROZEN_INPUTS_NOT_ALL_REVERIFIED",
            "equity_value": equity, "starting_revenue": revenue,
            "normalized_start_fcf_margin": start, "hurdle_rate": hurdle,
            "method": "ANNUAL_FCF_AND_TERMINAL_EQUITY_FCF_MULTIPLE",
            "normalization_assumption": "Margins are hypothetical after-capex, after-interest, after-economic-compensation equity cash margins; the bridge from reported FCF is not fully evidenced. No separate future SBC dilution or net-debt subtraction is applied.",
            "model_status": "EVIDENCE_INSUFFICIENT" if old["ticker"] in WITHHELD else "PROVISIONAL_SENSITIVITY",
            "limitation": WITHHELD.get(old["ticker"], old["key_limitation"]),
            "scenarios": {},
        }
        for case in ("bear", "base", "bull"):
            growth = float(old[f"{case}_revenue_cagr_pct"]) / 100
            margin = float(old[f"{case}_terminal_fcf_margin_pct"]) / 100
            multiple = float(old[f"{case}_terminal_p_fcf"])
            annual, terminal = cash_flows(revenue, growth, start, margin, multiple)
            value = pv(annual, terminal, hurdle)
            irr = distribution_irr(annual, terminal, equity)
            row["scenarios"][case] = {
                "claim_type": "estimate", "revenue_cagr": growth, "terminal_fcf_margin": margin,
                "terminal_p_fcf": multiple, "annual_fcf": annual, "terminal_equity_value": terminal,
                "zero_yield_retained_cash_terminal_wealth_cagr": ((sum(annual) + terminal) / equity) ** 0.1 - 1,
                "hypothetical_annual_distribution_irr": irr,
                "present_value_if_distributed": value,
                "present_value_to_reference_equity": value / equity,
                "terminal_value_share_of_pv": (terminal / (1 + hurdle) ** 10) / value,
                "margin_of_safety_price_factor_20pct": .8 * value / equity,
                "pv_sensitivity_hurdle_plus_2pp": pv(annual, terminal, hurdle + .02),
                "pv_sensitivity_terminal_multiple_minus_25pct": pv(annual, terminal * .75, hurdle),
            }
        reverse_margin = float(old["reverse_terminal_fcf_margin_pct"]) / 100
        reverse_multiple = float(old["reverse_terminal_p_fcf"])
        row["reverse_assumptions"] = {"terminal_fcf_margin": reverse_margin, "terminal_p_fcf": reverse_multiple}
        for n in (5, 10):
            row[f"required_revenue_cagr_{n}y_annual_distribution"] = solve_increasing(
                lambda g: pv(*cash_flows(revenue, g, start, reverse_margin, reverse_multiple, n), hurdle), equity)
        rows.append(row)
    return rows


def company_audit():
    """A same-hurdle diagnostic, NOT a completed owner-FCFE valuation.

    Cash flows follow inherited growth/margin estimates. Positive dilution is
    applied once; no unfinanced share-count reduction is allowed. SBC/repurchase
    funding bridges still need independent completion, particularly for ISRG.
    """
    inputs = {
        "GOOGL": (445.866, .1195, 12.5, 125.309, 341.84),
        "NVDA": (302.97, .4188, 24.3, 70.96, 227.23),
        "ISRG": (11.0344, .292, .3539, 8.63, 365.56),
        "DDOG": (3.966725, .2704, .359075, 3.985, 213.81),
        "NET": (2.51235, .1253, .354338, .572, 281.44),
    }
    rows = []
    for ticker, (revenue0, margin0, shares0, netassets, price) in inputs.items():
        ref = "f09c7b0" if ticker == "NVDA" else "367f55843d769da7e7b123007d78ac0b83eb83ef"
        old = json.loads(subprocess.check_output(["git", "show", f"{ref}:companies/{ticker}/valuation.json"], cwd=ROOT, text=True))
        row = {"ticker": ticker, "reference_price": price, "hurdle_rate": .09,
               "terminal_company_fcf_growth": .03, "as_of": "2026-09-05",
               "model_status": "DIAGNOSTIC_NOT_OWNER_FCFE_COMPLETE", "source_commit": ref,
               "source_path": f"companies/{ticker}/valuation.json",
               "starting_revenue_usd_b": revenue0, "starting_reported_fcf_margin": margin0,
               "starting_shares_b": shares0, "net_financial_assets_usd_b": netassets,
               "method_changes": ["All three cases use US 9% discount rate and 3% terminal company-FCF growth.",
                                  "Unlisted investments excluded; inherited liquid financial assets are a proxy, not all proven excess cash.",
                                  "No free negative dilution. Positive dilution continues in the terminal period.",
                                  "Reported-FCF compensation/repurchase/interest-income bridge is incomplete; outputs are diagnostic, not actionable fair values."],
               "scenarios": {}}
        for case, scenario in old["scenarios"].items():
            if ticker == "GOOGL":
                growth = [scenario["revenue_cagr_years_1_5_pct"] / 100] * 5 + [scenario["revenue_cagr_years_6_10_pct"] / 100] * 5
                m5, m10 = scenario["fcf_margin_year_5_pct"] / 100, scenario["terminal_fcf_margin_pct"] / 100
                margins = [margin0 + (m5 - margin0) * t / 5 for t in range(1, 6)] + [m5 + (m10 - m5) * t / 5 for t in range(1, 6)]
                dilution = 0.
            else:
                if ticker == "NVDA":
                    growth = [x / 100 for x in scenario["revenue_growth_pct_years_1_to_5"]] + [scenario["revenue_growth_pct_years_6_to_10"] / 100] * 5
                    m10, dilution = scenario["terminal_fcf_margin_pct"] / 100, 0.
                elif ticker == "ISRG":
                    growth = [scenario["ten_year_revenue_cagr"]] * 10
                    m10, dilution = scenario["year_10_fcf_margin"], max(0., scenario["annual_net_dilution"])
                elif ticker == "DDOG":
                    growth = scenario["annual_revenue_growth_path"]
                    m10, dilution = scenario["year_10_reported_fcf_margin"], scenario["annual_share_dilution"]
                else:
                    growth = scenario["revenue_growth_years_1_to_10"]
                    m10, dilution = scenario["year_10_fcf_margin"], scenario["annual_dilution"]
                margins = [margin0 + (m10 - margin0) * t / 10 for t in range(1, 11)]
            revenue, annual = revenue0, []
            for t, (g, m) in enumerate(zip(growth, margins), 1):
                revenue *= 1 + g
                annual.append(revenue * m / (shares0 * (1 + dilution) ** t))
            terminal_per_share_growth = 1.03 / (1 + dilution) - 1
            terminal = annual[-1] * (1 + terminal_per_share_growth) / (.09 - terminal_per_share_growth)
            value = netassets / shares0 + pv(annual, terminal, .09)
            row["scenarios"][case] = {
                "claim_type": "estimate", "growth_path": growth, "fcf_margin_path": margins,
                "annual_positive_dilution": dilution, "terminal_per_share_growth": terminal_per_share_growth,
                "annual_fcf_per_share_usd": annual, "terminal_value_per_share_usd": terminal,
                "diagnostic_present_value_per_share_usd": value,
                "value_to_reference_price": value / price,
                "note": "Positive terminal dilution lowers per-share terminal growth; cash distributions and funded buybacks must still be reconciled before investment use."
            }
        rows.append(row)
    return rows


def self_test():
    annual, terminal = cash_flows(100, 0, .10, .10, 10)
    assert abs(pv(annual, terminal, .10) - 100) < 1e-8
    assert abs(distribution_irr(annual, terminal, 100) - .10) < 1e-8
    assert ((sum(annual) + terminal) / 100) ** .1 - 1 < .10
    for row in audit():
        for scenario in row["scenarios"].values():
            assert abs(pv(scenario["annual_fcf"], scenario["terminal_equity_value"],
                          scenario["hypothetical_annual_distribution_irr"]) - row["equity_value"]) < 1e-6
            assert scenario["pv_sensitivity_hurdle_plus_2pp"] < scenario["present_value_if_distributed"]
            assert scenario["pv_sensitivity_terminal_multiple_minus_25pct"] < scenario["present_value_if_distributed"]
    return "20 models: IRR residual, timing distinction and sensitivity monotonicity passed"


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        print(self_test())
    else:
        print(json.dumps(audit(), ensure_ascii=False, indent=2))

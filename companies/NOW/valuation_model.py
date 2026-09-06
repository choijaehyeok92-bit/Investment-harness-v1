#!/usr/bin/env python3
"""NOW equity owner-cash-flow scenarios; stdout JSON, --check validates saved output.

USD millions and millions of shares. Not an enterprise-value model: interest
remains in cash flow; no separate cash/debt bridge is added to equity value.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def solve(fn, target, lo, hi):
    assert (fn(lo) - target) * (fn(hi) - target) <= 0, 'Root not bracketed'
    increasing = fn(hi) > fn(lo)
    for _ in range(150):
        mid = (lo + hi) / 2
        if (fn(mid) < target) == increasing:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def run():
    a = json.loads((ROOT / 'financial-inputs.json').read_text())
    r0, shares, price = a['ttm']['revenue'], a['valuation']['shares_m'], a['valuation']['price']
    m0, hurdle = a['valuation']['initial_owner_margin'], a['valuation']['hurdle']

    def case(g, margin, multiple, discount=hurdle):
        years = []
        for t in range(1, 11):
            revenue = r0 * (1 + g) ** t
            m = m0 + (margin - m0) * t / 10
            years.append({'year': t, 'revenue_usd_m': revenue, 'owner_margin': m,
                          'owner_fcf_usd_m': revenue * m, 'owner_fcf_per_share': revenue * m / shares})
        flows = [y['owner_fcf_per_share'] for y in years]
        terminal = flows[-1] * multiple
        def pv(rate):
            return sum(cf / (1 + rate) ** t for t, cf in enumerate(flows, 1)) + terminal / (1 + rate) ** 10
        value = pv(discount)
        return {'claim_type': 'estimate', 'revenue_cagr': g, 'terminal_owner_margin': margin,
                'terminal_equity_fcf_multiple': multiple, 'discount_rate': discount,
                'fair_value_per_share': value, 'upside_downside': value / price - 1,
                'annual_distribution_irr': solve(pv, price, -.5, 1),
                'year_10_terminal_price': terminal, 'terminal_pv_fraction': terminal / (1 + discount) ** 10 / value,
                'years': years}

    reverse = []
    for margin in [.20, .24, .28]:
        for multiple in [18, 23, 28]:
            g = solve(lambda growth: case(growth, margin, multiple)['fair_value_per_share'], price, -.05, .5)
            reverse.append({'terminal_owner_margin': margin, 'terminal_equity_fcf_multiple': multiple,
                            'required_10y_revenue_cagr': g, 'repriced_value': case(g, margin, multiple)['fair_value_per_share']})
    scenarios = {k: case(*v) for k, v in a['valuation']['scenario_assumptions'].items()}
    loss = case(0, .10, 12)
    loss.update({'cause': 'AI front ends commoditize workflows while acquisitions fail, limiting sales and owner margin for a decade.',
                 'probability': None, 'not_a_price_floor': True})
    return {'ticker': 'NOW', 'as_of': '2026-09-05', 'current_price': price,
            'implied_expectations': {'method': '10-year annual owner distributions plus year-10 equity FCF multiple',
                'claim_type': 'estimate', 'hurdle': hurdle, 'shares_m': shares,
                'initial_owner_margin': m0, 'reverse_grid': reverse,
                'base_hurdle_sensitivity': {str(h): case(.16, .24, 23, h)['fair_value_per_share'] for h in [.08, .09, .10, .12]},
                'base_share_count_sensitivity': {str(s): scenarios['base']['fair_value_per_share'] * shares / s for s in [1033.862, 1034.334, 1050]},
                'base_start_margin_sensitivity': 'See financial-inputs.json: 15% is a forecast assumption, not an audited normalized FCF bridge.'},
            'scenarios': scenarios, 'permanent_loss_case': loss,
            'expectation_gap_score': 10, 'asymmetry_score': 6, 'subjective_probabilities': None,
            'notes': 'FCFE-style owner proxy, not true legal distributable cash or an EV DCF. SBC replacement expense deducted; future share count held constant without free repurchases. No separate future dilution charge for the same compensation. Debt interest and ordinary cash income remain within margins; cash/debt is not added again. Principal refinancing and required liquidity are assumed viable; a refinancing/liquidity stress is not fully captured. 100% available owner cash is valued as annual distribution, not a forecast dividend. Future acquisition purchase prices and speculative strategic-investment exits excluded: growth must be funded from modeled reinvestment; serial debt-funded M&A invalidates Base. Terminal value is an equity P/FCF multiple, not EV/FCF. Probabilities unknown; no calibrated expected return.'}


if __name__ == '__main__':
    result = run()
    if '--check' in sys.argv:
        saved = json.loads((ROOT / 'valuation.json').read_text())
        assert saved == result, 'Saved valuation differs from recalculation'
        for row in result['implied_expectations']['reverse_grid']:
            assert abs(row['repriced_value'] - result['current_price']) < 1e-8
        for s in result['scenarios'].values():
            flows = [y['owner_fcf_per_share'] for y in s['years']]
            q = s['annual_distribution_irr']
            pv = sum(f / (1+q)**t for t, f in enumerate(flows, 1)) + s['year_10_terminal_price']/(1+q)**10
            assert abs(pv - result['current_price']) < 1e-8
        print('NOW valuation reproduced; reverse-price and annual IRR residuals < 1e-8 USD.')
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))

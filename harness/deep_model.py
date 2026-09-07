"""Deterministic, dated owner-FCFE scenarios, reverse expectations and funding.

Forecasts are analyst assumptions, never reported facts. Each component models
after-tax, after-interest cash AFTER economic compensation, all capital spending,
working capital and net debt service. No opening net-cash addition, free buyback,
or second deduction of future SBC through dilution is permitted.
"""
from __future__ import annotations
import copy
import math

CASES = ('bear', 'base', 'bull')


def bisect(fn, lo, hi):
    a, b = fn(lo), fn(hi)
    if a == 0: return lo
    if b == 0: return hi
    if a*b > 0: return None
    for _ in range(100):
        mid = (lo+hi)/2
        c = fn(mid)
        if a*c <= 0: hi, b = mid, c
        else: lo, a = mid, c
    return (lo+hi)/2


def all_irrs(cashflows):
    # Explicitly return ALL sign-change roots; never claim uniqueness for a
    # non-conventional stream with capital calls. Near-tangent roots unproven.
    def npv(rate):
        return sum(c/(1+rate)**i for i,c in enumerate(cashflows))
    grid = [-.99]+[math.exp(-4.605170186+i*(math.log(11)+4.605170186)/1200)-1 for i in range(1201)]
    roots = []
    for a,b in zip(grid, grid[1:]):
        if npv(a)*npv(b) < 0:
            root = bisect(npv,a,b)
            if not roots or abs(root-roots[-1]) > 1e-6: roots.append(root)
    return roots


def scale(t):
    return 1e6 if t['currency']=='KRW' else 1000


def flows(t, case, growth_override=None, margin_delta=0):
    rows=[]
    for year in range(1,11):
        parts=[]
        for c in t['components']:
            s=c['scenarios'][case]
            growth = s['growth_2_5'] if year<=5 else s['growth_6_10']
            if growth_override is not None: growth=growth_override
            if 'revenue_path' in s:
                revenue=s['revenue_path'][year-1]
                if growth_override is not None: revenue*=((1+growth_override)/(1+s['growth_2_5']))**year
            else:
                if growth_override is None:
                    revenue=s['revenue_year_1']*(1+s['growth_2_5'])**min(year-1,4)*(1+s['growth_6_10'])**max(year-5,0)
                else:
                    # Reverse begins at the same one-year forecast anchor and
                    # solves subsequent nine-year growth, not a false TTM CAGR.
                    revenue=s['revenue_year_1']*(1+growth)**(year-1)
                if year>=2: revenue*=s.get('year_2_reset',1)
            progress=min((year-1)/4,1)
            original_margin=s['owner_margin_year_1']+(s['owner_margin_mature']-s['owner_margin_year_1'])*progress
            margin=original_margin+margin_delta
            cash=revenue*margin
            if 'cash_path' in s:
                # Milestone cases need absolute investment cash amounts. Reverse
                # preserves their fixed capex while scaling revenue contributions.
                fixed=s['cash_path'][year-1]-s['revenue_path'][year-1]*original_margin
                cash+=fixed
            attribution=c.get('ownership',1)
            parts.append({'component':c['name'],'revenue':revenue,'owner_margin':margin,
                          'owner_cash_before_attribution':cash,'ownership':attribution,
                          'attributable_cash':cash*attribution})
        adjustment=t.get('annual_cash_adjustments',{}).get(case,[0]*10)[year-1]
        rows.append({'year':year,'components':parts,'special_cash_adjustment':adjustment,
                     'owner_cash':sum(p['attributable_cash'] for p in parts)+adjustment})
    return rows


def scenario(t,case,growth_override=None,margin_delta=0,discount=None,terminal_delta=0,with_irr=True):
    rate=t['required_return'] if discount is None else discount
    rows=flows(t,case,growth_override,margin_delta)
    multiple=t['terminal_multiple'][case]+terminal_delta
    terminal=max(0,rows[-1]['owner_cash'])*multiple
    # Parent-only non-operating stakes: excluded from operating components.
    # This is an analyst marked-to-market adjustment, not a cash distribution.
    separate=t.get('separate_equity_value',{}).get(case,0)
    values=[r['owner_cash'] for r in rows]
    pv_flow=sum(v/(1+rate)**(i+1) for i,v in enumerate(values))
    pv_terminal=terminal/(1+rate)**10
    raw_equity=pv_flow+pv_terminal+separate
    equity=max(0,raw_equity) # limited liability floor, retain unfloored economics
    shares=t['valuation_shares_m']
    per_share=equity*scale(t)/shares
    yearly_per_share=[v*scale(t)/shares for v in values]
    terminal_per_share=terminal*scale(t)/shares
    irr_flows=[-t['price']+separate*scale(t)/shares]+yearly_per_share
    irr_flows[-1]+=terminal_per_share
    # Funding diagnostic: deficits first draw disclosed unrestricted cash,
    # reserve is an explicit ASSUMPTION. This diagnostic does not additionally
    # dilute the capital-call-equivalent primary valuation.
    available=max(0,t['liquidity_cash']-t['minimum_cash_reserve'])
    reserve=available
    cumulative_gap=0
    for r in rows:
        deficit=max(0,-r['owner_cash'])
        used=min(reserve,deficit);reserve-=used
        gap=deficit-used;cumulative_gap+=gap
        r.update(cash_deficit=deficit,available_cash_used=used,new_funding_required=gap)
    issue_price=t['price']*t['funding_issue_price_fraction'][case]
    new_shares=cumulative_gap*scale(t)/issue_price
    # An ALTERNATIVE financing stress: negative cash is funded by company cash
    # or outsiders; only positive distributions/terminal accrue to diluted
    # owners. No second subtraction of those capital calls in this alternative.
    stress_shares=shares
    stress_pv=separate
    for r in rows:
        stress_shares+=r['new_funding_required']*scale(t)/issue_price
        stress_pv+=max(0,r['owner_cash'])*shares/stress_shares/(1+rate)**r['year']
    stress_pv+=terminal*shares/stress_shares/(1+rate)**10
    return {'claim_type':'estimate','case':case,'required_return':rate,
        'terminal_multiple':multiple,'rows':rows,'pv_interim_owner_cash':pv_flow,
        'pv_terminal':pv_terminal,'separate_equity_value':separate,
        'unfloored_equity_value':raw_equity,'equity_value':equity,'value_per_share':per_share,
        'value_to_price':per_share/t['price'],'upside_downside':per_share/t['price']-1,
        'terminal_fraction_of_operating_pv':pv_terminal/(pv_flow+pv_terminal) if pv_flow+pv_terminal else None,
        'year_10_revenue':sum(p['revenue'] for p in rows[-1]['components']),
        'year_10_owner_cash':values[-1], 'year_10_owner_cash_per_share':yearly_per_share[-1],
        'year_10_exit_price':terminal_per_share,
        'irr_roots':all_irrs(irr_flows) if with_irr else [],
        'irr_note':'Annual distributable cash plus terminal proceeds; separate stake mark treated as time-zero value-equivalent. Capital calls allowed; all sign-change roots -99% to 1000% searched; not a promised shareholder return.',
        'gross_negative_cash':sum(max(0,-v) for v in values),
        'unrestricted_cash_after_reserve':available,'external_funding_gap':cumulative_gap,
        'funding_only_new_shares_m':new_shares,
        'funding_only_share_increase':new_shares/shares,
        'alternative_dilution_financing_value_per_share':stress_pv*scale(t)/shares,
        'funding_note':'Separate alternative, NOT an extra haircut on primary PV. Issue price is assumed, cash is not double-added, future SBC cash cost is already in margins. M&A/conversion separately stress-tested.'}


def reverse(t):
    price=t['price']
    # Executed before narrative scenario judgments. Hold BASE economics and
    # anchor constant. Model can have unknown/impossible root: retain null.
    fn=lambda g:scenario(t,'base',growth_override=g,with_irr=False)['value_per_share']-price
    g=bisect(fn,-.8,2.0)
    margin_root=bisect(lambda d:scenario(t,'base',margin_delta=d,with_irr=False)['value_per_share']-price,-.8,1.5)
    result={'claim_type':'estimate','method':'Hold base year-1 revenue, economic margins, rights and terminal multiple; solve growth for years 2–10 (milestone revenue paths: proportional growth stress). No unique market belief is observable.',
        'required_growth_years_2_10':g,'required_owner_margin_delta':margin_root,
        'price_reference':price,'source':'price-and-shares.json / model-inputs.json',
        'horizon_years':10,'required_return':t['required_return']}
    if g is not None:
        s=scenario(t,'base',growth_override=g,with_irr=False)
        result.update(implied_year_10_revenue=s['year_10_revenue'],implied_year_10_owner_cash=s['year_10_owner_cash'],residual_price=s['value_per_share']-price)
    return result


def model(t):
    assert t['claim_type']=='estimate' and t['valuation_shares_m']>0 and t['price']>0
    assert t['minimum_cash_reserve']>=0 and t['liquidity_cash']>=0
    for c in t['components']:
        assert 0<c.get('ownership',1)<=1
        for s in c['scenarios'].values():
            assert -1 < s['growth_2_5'] and -1 < s['growth_6_10']
            if 'revenue_path' in s: assert len(s['revenue_path'])==10
            if 'cash_path' in s: assert len(s['cash_path'])==10
    implied=reverse(t)
    cases={k:scenario(t,k) for k in CASES}
    sensitivity=[]
    for rate in [t['required_return']-.02,t['required_return'],t['required_return']+.02]:
        for delta in [-.03,0,.03]:
            s=scenario(t,'base',margin_delta=delta,discount=rate,with_irr=False)
            sensitivity.append({'discount_rate':rate,'owner_margin_delta':delta,'value_per_share':s['value_per_share']})
    terminal_sensitivity=[{'terminal_multiple_delta':d,'value_per_share':scenario(t,'base',terminal_delta=d,with_irr=False)['value_per_share']} for d in [-5,0,5]]
    probability_threshold=None
    b,u=cases['bear']['value_per_share'],cases['bull']['value_per_share']
    if u>b: probability_threshold=(t['price']-b)/(u-b)
    return {'schema_version':'1.0.0','unit':t['unit'],'reverse_expectations':implied,
        'scenarios':cases,'sensitivity':sensitivity,'terminal_sensitivity':terminal_sensitivity,
        'break_even_bull_probability_in_two_outcome_pv_test':probability_threshold,
        'probability_note':'An algebraic threshold, NOT an estimated likelihood; values outside [0,1] mean no feasible two-outcome probability clears current price.',
        'method_limits':['Owner margins, reinvestment and terminal multiples are explicit analyst estimates, not management forecasts.',
                        'No opening excess-cash distribution included in operating PV. Liquidity is tested separately; no EV/FCFE net-debt double count.',
                        'Primary signed cash model is current-owner capital-call equivalent when deficits occur; it is not a financing commitment.',
                        'Price and filing share dates differ; a reference snapshot, not synchronized executable market capitalization.']}

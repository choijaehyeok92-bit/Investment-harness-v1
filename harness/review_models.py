"""Explicit adapters for the September 12 reviewed valuation snapshots.

All future cash flows are estimates. This module does not fetch prices or trade.
The adapters retain each source model's cash/rights convention; differences
from the reported model are surfaced, never calibrated to force eligibility.
"""
from __future__ import annotations
import copy
from .core import read
from .deep_model import flows, bisect

CASES = ('bear', 'base', 'bull')

def present_value(cash, terminal, rate, separate=0):
    return sum(x/(1+rate)**i for i,x in enumerate(cash,1))+terminal/(1+rate)**len(cash)+separate

def from_legacy(t, case, growth=None):
    rows=flows(t,case,growth_override=growth)
    scale=(1e6 if t['currency']=='KRW' else 1000)/t['valuation_shares_m']
    cash=[x['owner_cash']*scale for x in rows]
    return cash,max(0,cash[-1])*t['terminal_multiple'][case],t.get('separate_equity_value',{}).get(case,0)*scale,t['required_return']

def curve(r0,growths,margins,multiple,rate,shares,scale=1,cash_add=0):
    values=[]; rev=r0
    for g,m in zip(growths,margins):
        rev*=1+g;values.append(rev*m*scale/shares)
    return values,max(0,values[-1])*multiple,cash_add*scale/shares,rate

def linear(a,b,n=10):
    return [a+(b-a)*i/(n-1) for i in range(n)]

def source_value(s):
    for k in ['value_per_share','per_share_usd','fair_value_per_share','value_per_share_usd','value_per_adr','updated_value_per_share']:
        if k in s:return s[k]
    raise ValueError('Unknown per-share value field')

def schedule(spec,case,growth=None):
    t=spec['ticker'];v=read(spec['valuation_path']);s=v.get('scenarios',{}).get(case,{})
    if spec['adapter']=='legacy':return from_legacy(read(spec['model_path']),case,growth)
    if t=='207940':
        old=read('companies/207940/analyses/2026-09-06-deep/model-inputs.json')
        cash,term,separate,rate=from_legacy(old,case,growth)
        bridge=v['share_bridge'];ratio=bridge['old_shares_m']/bridge['pro_forma_shares_m']
        return [x*ratio for x in cash],term*ratio,separate*ratio+s['rights_funded_deployment_value_trillion']*1e6/bridge['pro_forma_shares_m'],rate
    if t=='003230':
        gs=s['annual_revenue_growth_path'] if growth is None else [growth]*10
        sm=v['scenario_method']
        return curve(sm['starting_revenue_krw_trillion'],gs,s['owner_margin_path'],s['terminal_multiple'],v['required_return'],v['price_reference']['issued_shares'],1e12,sm['net_cash_added_krw_trillion'])
    if t=='058470':
        gs=s['growth_path'] if growth is None else [s['growth_path'][0]]+[growth]*9
        return curve(v['ttm_diagnostics']['revenue_krw_b'],gs,s['owner_cash_margin_path'],s['terminal_multiple'],v['required_return'],v['price_reference']['valuation_shares_m'],1000,v['liquidity_bridge']['excess_financial_assets_added_once_krw_b'])
    if t=='145020':
        gs=s['annual_revenue_growth_path'] if growth is None else [growth]*5+[growth/2]*5
        # Same 10% hurdle in all cases: do not manufacture asymmetry by lowering
        # the discount rate in Bull. Rounded source margin paths remain explicit.
        return curve(v['scenario_method']['starting_revenue_krw_bn'],gs,s['owner_margin_path'],s['terminal_multiple'],.10,s['diluted_shares_m'],1000,s['net_cash_added_krw_bn'])
    if t=='NOW':
        g=s['revenue_cagr'] if growth is None else growth
        return curve(v['ttm_diagnostics_usd_b']['revenue'],[g]*10,[.15+(s['terminal_owner_margin']-.15)*i/10 for i in range(1,11)],s['terminal_equity_fcf_multiple'],v['required_return'],v['valuation_shares_m'],1000)
    if t=='META':
        g=s['years_2_to_10_revenue_growth'] if growth is None else growth
        ms=[s['year1_owner_cash_margin']+(s['year10_owner_cash_margin']-s['year1_owner_cash_margin'])*i/10 for i in range(1,11)]
        return curve(v['year1_revenue_billion'],[0]+[g]*9,ms,s['terminal_owner_cash_multiple'],v['required_return'],v['shares_billion'],cash_add=v['net_cash_adjustment_billion'])
    if t=='APP':
        g=s['growth_cagr'] if growth is None else growth;n=v['reverse_dcf']['explicit_years'];r=v['required_return']
        cash=[s['starting_owner_fcf_usd_b']*(1+g)**i*1000/v['shares_m'] for i in range(1,n+1)]
        return cash,cash[-1]*(1+s['terminal_growth'])/(r-s['terminal_growth']),0,r
    if t in ['ETN','MPWR','PWR']:
        r0=s.get('revenue_year_1_usd_b',s.get('year1_revenue_b'))
        gs=[0]+[s['growth_years_2_5']]*4+[s['growth_years_6_10']]*5 if growth is None else [0]+[growth]*9
        m0=s.get('owner_margin_year_1',s.get('owner_cash_margin_year1'));m1=s.get('owner_margin_mature',s.get('owner_cash_margin_year10'))
        # ETN/MPWR use the original harness ramp to maturity by year 5.
        # PWR uses year-1 to year-10 interpolation. These conventions reproduce
        # all three source scenarios (rounding tolerance is reported).
        ms=[m0+(m1-m0)*min(i/4,1) for i in range(10)] if t in ['ETN','MPWR'] else linear(m0,m1)
        shares=v.get('valuation_shares_m',v.get('price_reference',{}).get('valuation_shares_m'))
        cash_add=v['cash_overlay']['excess_cash_used_usd_b'] if t=='MPWR' else v['cash_b']-v['debt_b'] if t=='PWR' else 0
        return curve(r0,gs,ms,s['terminal_multiple'],v['required_return'],shares,1000,cash_add)
    raise ValueError('Unregistered model adapter '+t)

def evaluate(spec,price):
    prior=read(spec['valuation_path']);out={}
    for case in CASES:
        cash,term,separate,rate=schedule(spec,case)
        value=max(0,present_value(cash,term,rate,separate))
        old=source_value(prior['scenarios'][case])
        out[case]={'claim_type':'estimate','value_per_share':value,'source_reported_value':old,'recalculation_difference':value-old,'required_return':rate,'annual_owner_cash_per_share':cash,'terminal_owner_value_per_share':term,'separate_value_per_share':separate,'value_to_price':value/price,'terminal_fraction_of_operating_pv':term/(1+rate)**len(cash)/(value-separate) if value!=separate else None}
    def fn(g):
        cash,term,separate,rate=schedule(spec,'base',g)
        return max(0,present_value(cash,term,rate,separate))
    g=bisect(lambda g:fn(g)-price,-.8,2)
    reverse={'claim_type':'estimate','growth':g,'repriced_value':fn(g) if g is not None else None,'price_residual':fn(g)-price if g is not None else None,'growth_basis':spec['reverse_basis'],'warning':'Conditional on Base margins, capital claims and terminal assumptions; not an observable unique market forecast.'}
    sensitivities=[]
    cash,term,separate,rate=schedule(spec,'base')
    for delta in [-.02,0,.02]:
        sensitivities.append({'required_return':rate+delta,'value_per_share':max(0,present_value(cash,term,rate+delta,separate))})
    return {'schema_version':'1.0.0','ticker':spec['ticker'],'as_of':'2026-09-12','currency':spec['currency'],'price':price,'source_model':spec,'scenarios':out,'reverse_expectations':reverse,'base_discount_sensitivity':sensitivities,'approved_for_trading':False}

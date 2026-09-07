import copy
import unittest
from harness.deep_model import scenario,model,bisect,all_irrs
from harness.deep_inputs import inputs
from harness.deep_financials import financials
from harness.deep_report import outputs


class DeepCashTests(unittest.TestCase):
    def simple(self):
        return {'claim_type':'estimate','ticker':'TEST','currency':'USD','unit':'USD billion',
            'price':100,'valuation_shares_m':100,'liquidity_cash':0,'minimum_cash_reserve':0,
            'required_return':.10,'terminal_multiple':{k:10 for k in ['bear','base','bull']},
            'funding_issue_price_fraction':{k:.5 for k in ['bear','base','bull']},
            'components':[{'name':'one','scenarios':{k:{'revenue_year_1':1,'growth_2_5':0,'growth_6_10':0,'owner_margin_year_1':1,'owner_margin_mature':1} for k in ['bear','base','bull']}}]}
    def test_constant_cash_equals_perpetuity_at_matching_exit_multiple(self):
        s=scenario(self.simple(),'base')
        self.assertAlmostEqual(s['equity_value'],10)
        self.assertAlmostEqual(s['value_per_share'],100)
        self.assertAlmostEqual(s['irr_roots'][0],.1)
    def test_usd_and_krw_unit_conversion(self):
        a=self.simple();b=copy.deepcopy(a);b['currency']='KRW'
        self.assertAlmostEqual(scenario(b,'base')['value_per_share']/scenario(a,'base')['value_per_share'],1000)
    def test_existing_cash_not_free_added_twice(self):
        t=self.simple();old=scenario(t,'base')['value_per_share'];t['liquidity_cash']=100
        self.assertEqual(scenario(t,'base')['value_per_share'],old)
    def test_two_irr_roots_not_silently_selecting_one(self):
        roots=all_irrs([-100,230,-132])
        self.assertEqual(len(roots),2)
        self.assertAlmostEqual(roots[0],.1);self.assertAlmostEqual(roots[1],.2)
    def test_reverse_has_no_fake_solution_outside_bracket(self):
        self.assertIsNone(bisect(lambda x:x*x+1,-1,1))
    def test_cheaper_financing_dilutes_alternative_only(self):
        t=self.simple()
        for s in t['components'][0]['scenarios'].values():s.update(owner_margin_year_1=-1,owner_margin_mature=.3)
        a=scenario(t,'base');t['funding_issue_price_fraction']['base']=.25;b=scenario(t,'base')
        self.assertGreater(a['external_funding_gap'],0)
        self.assertEqual(a['value_per_share'],b['value_per_share'])
        self.assertLess(b['alternative_dilution_financing_value_per_share'],a['alternative_dilution_financing_value_per_share'])
    def test_discount_applies_to_terminal_and_distributions(self):
        t=self.simple()
        self.assertLess(scenario(t,'base',discount=.15)['value_per_share'],scenario(t,'base',discount=.1)['value_per_share'])
    def test_fixed_satellite_capex_does_not_cancel_margin_sensitivity(self):
        t=inputs()['ASTS']
        a=scenario(t,'base',margin_delta=-.03)['value_per_share']
        b=scenario(t,'base',margin_delta=.03)['value_per_share']
        self.assertLess(a,b)
    def test_missing_ocf_is_not_filled_with_estimated_margin(self):
        d=financials('042700');self.assertIsNone(d['ocf']);self.assertIsNone(d['owner_cash_proxy'])
    def test_negative_owner_bridge_and_non_gaap_scope(self):
        self.assertAlmostEqual(financials('AMZN')['owner_cash_proxy'],-28.825)
        self.assertAlmostEqual(financials('NET')['owner_cash_proxy'],-.192782)
        self.assertFalse(financials('NET')['owner_proxy_complete'])
    def test_adr_and_upc_economic_rights(self):
        d=inputs()
        self.assertAlmostEqual(d['TSM']['valuation_shares_m']*1e6*5,25932524521)
        self.assertAlmostEqual(d['ASTS']['valuation_shares_m']*1e6,299789305+11215111+78163078)
    def test_all_reverse_models_reprice_reference_and_have_ordered_cases(self):
        for ticker,t in inputs().items():
            m=model(t)
            self.assertLess(abs(m['reverse_expectations']['residual_price']),max(.00001,t['price']*1e-8),ticker)
            v=[m['scenarios'][k]['value_per_share'] for k in ['bear','base','bull']]
            self.assertLessEqual(v[0],v[1],ticker);self.assertLessEqual(v[1],v[2],ticker)
    def test_complete_research_does_not_authorize_unresolved_veto(self):
        files,ds=outputs();self.assertEqual(len(ds),34)
        self.assertTrue(all(d['research_state']=='FULL_ANALYSIS' and d['completion_gate']['passed'] for d in ds))
        self.assertTrue(all(not d['buy_authorized'] for d in ds))
        self.assertTrue(all(len(d['red_team']['attacks'])==10 for d in ds))


if __name__=='__main__':unittest.main()

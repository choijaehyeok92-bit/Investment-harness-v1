import copy
import unittest
from harness.core import CATEGORIES, aggregate_veto, totals, unit_info, calculate, resolve_pointer, validate_assessment
from harness.build import outputs

class GuardTests(unittest.TestCase):
    def test_unknown_not_zero(self):
        cats={k:{'score':None,'max_score':v} for k,v in CATEGORIES.items()}
        self.assertEqual(totals(cats),(None,None))
    def test_partial_quality_separate(self):
        cats={k:{'score':v,'max_score':v} for k,v in CATEGORIES.items()}
        cats['expectation_gap_and_valuation']['score']=None
        self.assertEqual(totals(cats),(None,75))
    def test_veto_precedence(self):
        self.assertEqual(aggregate_veto([{'status':'PASS'},{'status':'FAIL'},{'status':'INVESTIGATE'}]),'FAIL')
    def test_explicit_units_only(self):
        self.assertEqual(unit_info('USD millions'),('USD',1e6))
        self.assertEqual(unit_info('KRW cash outflow'),('KRW',1))
        self.assertEqual(unit_info('USD/KRW million'),(None,None))
        self.assertEqual(unit_info('million shares'),(None,None))
    def test_escaped_pointer(self):
        self.assertEqual(resolve_pointer({'a/b':{'x~y':[42]}},'/a~1b/x~0y/0'),42)
    def spec(self):
        return {'inputs':['a','b'],'operation':'ocf_less_explicit_capex','accounting_scope':'consolidated cash','comparability_note':'same H1'}
    def rows(self):
        return {'a':{'value_base_currency':5,'period':'H1 2026','currency':'USD'},'b':{'value_base_currency':9,'period':'H1 2026','currency':'USD'}}
    def test_negative_cash_not_clipped(self):
        self.assertEqual(calculate(self.spec(),self.rows())['value'],-4)
    def test_mixed_currency_blocked(self):
        rows=self.rows();rows['b']['currency']='KRW'
        with self.assertRaises(AssertionError):calculate(self.spec(),rows)
    def test_mixed_period_blocked(self):
        rows=self.rows();rows['b']['period']='FY2025'
        with self.assertRaises(AssertionError):calculate(self.spec(),rows)
    def test_missing_period_blocked(self):
        rows=self.rows();rows['b']['period']=None
        with self.assertRaises(AssertionError):calculate(self.spec(),rows)
    def test_ambiguous_outflow_blocked(self):
        rows=self.rows();rows['b']['value_base_currency']=-9
        with self.assertRaises(AssertionError):calculate(self.spec(),rows)
    def test_missing_scope_blocked(self):
        spec=self.spec();spec.pop('accounting_scope')
        with self.assertRaises(AssertionError):calculate(spec,self.rows())
    def test_score_overflow_blocked(self):
        cats={k:{'score':v,'max_score':v} for k,v in CATEGORIES.items()};cats['moat_trajectory']['score']=16
        with self.assertRaises(AssertionError):totals(cats)
    def test_all_93_have_eight_categories_nine_vetoes_ten_attacks(self):
        files,ds=outputs();self.assertEqual(len(ds),93)
        for d in ds:validate_assessment(d)
    def test_incomplete_cannot_buy(self):
        d=copy.deepcopy(next(d for d in outputs()[1] if d['ticker']=='AMZN'));d['buy_authorized']=True
        with self.assertRaises(AssertionError):validate_assessment(d)
    def test_fail_cannot_watch(self):
        d=copy.deepcopy(next(d for d in outputs()[1] if d['ticker']=='NOW'))
        d['hard_veto']['items'][0]['status']='FAIL';d['hard_veto']['overall_status']='FAIL'
        with self.assertRaises(AssertionError):validate_assessment(d)
    def test_raw_only_not_full(self):
        ds=outputs()[1];raw=[d for d in ds if d['input_maturity']=='RAW_DATA_ONLY_AT_BASELINE']
        self.assertEqual(len(raw),24);self.assertTrue(all(d['total_score_100'] is None and not d['buy_authorized'] for d in raw))
    def test_now_authority_not_old_screen_score(self):
        now=next(d for d in outputs()[1] if d['ticker']=='NOW')
        self.assertEqual(now['total_score_100'],72);self.assertEqual(now['decision'],'WATCH')
    def test_no_50_to_100_conversion(self):
        self.assertTrue(all(d['total_score_100'] is None for d in outputs()[1] if d['input_maturity']=='SCREEN_OR_LIST_ONLY'))

if __name__=='__main__':unittest.main()

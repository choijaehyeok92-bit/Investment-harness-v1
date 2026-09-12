import unittest
from harness.review_run import eligible, weights, DIRECTORY
from harness.review_models import evaluate, present_value
from harness.core import read

class PortfolioGuards(unittest.TestCase):
    def test_inclusive_price_score_exclusive_management(self):
        self.assertTrue(eligible(70,6,115,100))
        self.assertFalse(eligible(70,5,115,100))
        self.assertFalse(eligible(69,6,100,100))
        self.assertFalse(eligible(70,6,115.000001,100))
    def test_unknown_and_veto_never_pass(self):
        self.assertFalse(eligible(90,8,None,100))
        self.assertFalse(eligible(90,8,90,100,'FAIL'))
        self.assertTrue(eligible(90,8,90,100,'INVESTIGATE'))
    def test_score_weights_do_not_impose_top_ten(self):
        rows=[{'ticker':str(i),'score':70+i} for i in range(23)]
        w=weights(rows)
        self.assertEqual(sum(w.values()),10000)
        self.assertLess(sum(sorted(w.values(),reverse=True)[:10]),8000)
        for r in rows:self.assertLess(abs(w[r['ticker']]-r['score']*10000/sum(x['score'] for x in rows)),1)
    def test_ties_and_empty_are_deterministic(self):
        self.assertEqual(weights([]),{})
        self.assertEqual(weights([{'ticker':t,'score':70} for t in ['C','B','A']]),{'A':3334,'B':3333,'C':3333})
    def test_hugel_same_hurdle_and_reverse_repricing(self):
        spec=next(x for x in read(DIRECTORY+'/model-specs.json') if x['ticker']=='145020')
        v=evaluate(spec,231000)
        self.assertEqual({x['required_return'] for x in v['scenarios'].values()},{.10})
        self.assertLess(abs(v['reverse_expectations']['price_residual']),.000001)
        self.assertLess(v['scenarios']['bull']['value_per_share'],v['scenarios']['bull']['source_reported_value'])
    def test_present_value_does_not_drop_negative_cash(self):
        self.assertEqual(present_value([-10,20],0,0),10)

if __name__=='__main__':unittest.main()

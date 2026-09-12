import unittest
from harness.core import read
from harness.management_correction import DIRECTORY, MG, corrected_assessment, outputs


class ManagementCorrectionTests(unittest.TestCase):
    def test_restoration_is_absolute_and_changes_only_management(self):
        audit = read(DIRECTORY+'/audit.json')
        for ticker, total in [('NVDA',79),('TMDX',74)]:
            old = read(audit['findings'][ticker]['superseded_assessment'])
            first = corrected_assessment(ticker,audit)
            second = corrected_assessment(ticker,audit)
            self.assertEqual(first,second)
            self.assertEqual(first['categories'][MG]['score'],6)
            self.assertEqual(first['total_score_100'],total)
            self.assertEqual(first['total_score_100']-old['total_score_100'],1)
            for key in old['categories']:
                if key!=MG:self.assertEqual(first['categories'][key],old['categories'][key])
            self.assertEqual(first['hard_veto'],old['hard_veto'])
            self.assertFalse(first['buy_authorized'])

    def test_nvda_acquisition_and_regulatory_counterevidence_is_not_erased(self):
        audit = read(DIRECTORY+'/audit.json')
        old = read(audit['findings']['NVDA']['superseded_assessment'])
        new = corrected_assessment('NVDA',audit)
        self.assertEqual(new['categories'][MG]['counter_evidence'],old['categories'][MG]['counter_evidence'])

    def test_same_prices_rules_and_score_weights_admit_thirteen(self):
        _,rows,_ = outputs()
        before = {r['ticker']:r for r in read('reviews/2026-09-12-full-review/scoreboard.json')}
        selected = [r for r in rows if r['eligible']]
        self.assertEqual(len(selected),13)
        self.assertEqual(sum(r['score'] for r in selected),1007)
        self.assertEqual(sum(r['weight_bp'] for r in selected),10000)
        self.assertEqual({r['ticker'] for r in selected}-{t for t,r in before.items() if r['eligible']},{'NVDA','TMDX'})
        for row in rows:
            self.assertEqual(row['quote'],before[row['ticker']]['quote'])
            self.assertEqual(row['base_value'],before[row['ticker']]['base_value'])
        for row in selected:
            self.assertLess(abs(row['weight_bp']-10000*row['score']/1007),1)


if __name__=='__main__':unittest.main()

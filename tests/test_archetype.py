import unittest

from harness.archetype import (
    DISRUPTION_DIMENSIONS, SCORECARD_CATEGORIES, build_inputs, check_document,
    classify, disruption_tier, disruption_total, expectation_gap_ratio,
)


def dims(non_consumption=4, incumbent=4, curve=3, s_curve=3, optionality=3):
    return {'non_consumption_and_new_market_creation': non_consumption,
            'incumbent_business_model_conflict': incumbent,
            'cost_or_performance_curve': curve,
            's_curve_position_and_adoption_evidence': s_curve,
            'platform_optionality_and_second_curve': optionality}


def base_inputs(**overrides):
    """A company that clears every COMPOUNDER gate. Tests degrade it one field at a time."""
    scores = {'structural_change_and_leadership': 12, 'customer_value_and_product': 8,
              'moat_trajectory': 12, 'incremental_roic_and_fcf_per_share': 12,
              'management_and_capital_allocation': 8, 'financial_survivability': 8,
              'expectation_gap_and_valuation': 9, 'power_law_and_asymmetry': 7}
    inputs = {
        'hard_veto_status': 'PASS', 'research_state': 'FULL_ANALYSIS',
        'business_quality_75': sum(scores[name] for name in SCORECARD_CATEGORIES[:6]),
        'category_scores': scores,
        'category_confidence': {name: 0.7 for name in SCORECARD_CATEGORIES},
        'disruption_dimensions': dims(1, 1, 1, 1, 1),
        'disruption_total': 5, 'disruption_tier': 'INCREMENTAL',
        'current_price': 100.0, 'base_value_per_share': 120.0,
    }
    inputs.update(overrides)
    quality = [inputs['category_scores'][name] for name in SCORECARD_CATEGORIES[:6]]
    if 'category_scores' in overrides and 'business_quality_75' not in overrides:
        inputs['business_quality_75'] = sum(quality) if all(v is not None for v in quality) else None
    return inputs


class DisruptionAxisTests(unittest.TestCase):
    def test_axis_is_twenty_points_outside_the_hundred(self):
        self.assertEqual(sum(DISRUPTION_DIMENSIONS.values()), 20)
        self.assertNotIn('disruption', SCORECARD_CATEGORIES)

    def test_unknown_dimension_is_not_zero(self):
        partial = dims(); partial['cost_or_performance_curve'] = None
        self.assertIsNone(disruption_total(partial))
        self.assertEqual(disruption_tier(partial), 'UNSCORED')

    def test_tier_bands(self):
        self.assertEqual(disruption_tier(dims(4, 4, 4, 4, 1)), 'FOUNDATIONAL')
        self.assertEqual(disruption_tier(dims(3, 3, 3, 3, 1)), 'STRONG')
        self.assertEqual(disruption_tier(dims(2, 2, 2, 2, 1)), 'EMERGING')
        self.assertEqual(disruption_tier(dims(1, 1, 1, 1, 1)), 'INCREMENTAL')
        self.assertEqual(disruption_tier(dims(1, 1, 1, 0, 0)), 'NONE')

    def test_out_of_range_dimension_rejected(self):
        with self.assertRaises(ValueError):
            disruption_total(dims(5))

    def test_gap_ratio_sign(self):
        self.assertAlmostEqual(expectation_gap_ratio(120, 100), 0.2)
        self.assertAlmostEqual(expectation_gap_ratio(80, 100), -0.2)
        self.assertIsNone(expectation_gap_ratio(None, 100))


class ClassificationTests(unittest.TestCase):
    def test_compounder(self):
        result = classify(base_inputs())
        self.assertEqual(result['archetype'], 'COMPOUNDER')
        self.assertEqual(result['position_ceiling'], 'EXCEPTIONAL_WINNER')
        self.assertIsNone(result['not_qualified_reason'])

    def test_hard_veto_fail_beats_every_score(self):
        result = classify(base_inputs(hard_veto_status='FAIL'))
        self.assertEqual(result['archetype'], 'NOT_QUALIFIED')
        self.assertEqual(result['not_qualified_reason'], 'HARD_VETO_FAIL')
        self.assertEqual(result['quality_gates_met'], [])

    def test_veto_investigate_classifies_but_cannot_be_sized(self):
        result = classify(base_inputs(hard_veto_status='INVESTIGATE'))
        self.assertEqual(result['archetype'], 'COMPOUNDER')
        self.assertEqual(result['position_ceiling'], 'NONE')

    def test_provisional_until_full_analysis(self):
        result = classify(base_inputs(research_state='PARTIAL_ANALYSIS'))
        self.assertTrue(result['provisional'])
        self.assertEqual(result['position_ceiling'], 'NONE')

    def test_unknown_score_is_insufficient_evidence_not_reject(self):
        scores = base_inputs()['category_scores'] | {'moat_trajectory': None}
        result = classify(base_inputs(category_scores=scores, business_quality_75=None))
        self.assertEqual(result['archetype'], 'NOT_QUALIFIED')
        self.assertEqual(result['not_qualified_reason'], 'INSUFFICIENT_EVIDENCE')

    def test_moonshot_tolerates_high_valuation_within_tier_bound(self):
        inputs = base_inputs(
            category_scores={'structural_change_and_leadership': 13, 'customer_value_and_product': 8,
                             'moat_trajectory': 8, 'incremental_roic_and_fcf_per_share': 5,
                             'management_and_capital_allocation': 7, 'financial_survivability': 6,
                             'expectation_gap_and_valuation': 3, 'power_law_and_asymmetry': 9},
            disruption_dimensions=dims(4, 4, 4, 4, 3), disruption_total=19, disruption_tier='FOUNDATIONAL',
            current_price=200.0, base_value_per_share=100.0, funding_runway_months=30,
            permanent_loss_case_sized=True)
        result = classify(inputs)
        self.assertEqual(result['archetype'], 'MOONSHOT')
        self.assertEqual(result['position_ceiling'], 'STARTER')

    def test_moonshot_tolerance_is_bounded(self):
        inputs = base_inputs(
            category_scores={'structural_change_and_leadership': 13, 'customer_value_and_product': 8,
                             'moat_trajectory': 8, 'incremental_roic_and_fcf_per_share': 5,
                             'management_and_capital_allocation': 7, 'financial_survivability': 6,
                             'expectation_gap_and_valuation': 3, 'power_law_and_asymmetry': 9},
            disruption_dimensions=dims(4, 4, 4, 4, 3), disruption_total=19, disruption_tier='FOUNDATIONAL',
            current_price=300.0, base_value_per_share=100.0, funding_runway_months=30,
            permanent_loss_case_sized=True)
        result = classify(inputs)
        self.assertEqual(result['archetype'], 'NOT_QUALIFIED')
        self.assertEqual(result['not_qualified_reason'], 'PRICED_BEYOND_MOONSHOT_TOLERANCE')
        self.assertEqual(result['quality_gates_met'], ['MOONSHOT'])

    def test_moonshot_requires_runway(self):
        inputs = base_inputs(
            category_scores={'structural_change_and_leadership': 13, 'customer_value_and_product': 8,
                             'moat_trajectory': 8, 'incremental_roic_and_fcf_per_share': 5,
                             'management_and_capital_allocation': 7, 'financial_survivability': 6,
                             'expectation_gap_and_valuation': 3, 'power_law_and_asymmetry': 9},
            disruption_dimensions=dims(4, 4, 4, 4, 3), disruption_total=19, disruption_tier='FOUNDATIONAL',
            current_price=200.0, base_value_per_share=100.0, funding_runway_months=12,
            permanent_loss_case_sized=True)
        result = classify(inputs)
        self.assertEqual(result['archetype'], 'NOT_QUALIFIED')
        self.assertEqual(result['not_qualified_reason'], 'SURVIVABILITY_GATE_NOT_MET')

    def test_disruption_narrative_without_adoption_cannot_be_a_moonshot(self):
        inputs = base_inputs(
            category_scores={'structural_change_and_leadership': 13, 'customer_value_and_product': 8,
                             'moat_trajectory': 8, 'incremental_roic_and_fcf_per_share': 5,
                             'management_and_capital_allocation': 7, 'financial_survivability': 6,
                             'expectation_gap_and_valuation': 3, 'power_law_and_asymmetry': 9},
            disruption_dimensions=dims(4, 4, 4, 0, 3), disruption_total=15, disruption_tier='STRONG',
            current_price=200.0, base_value_per_share=100.0, funding_runway_months=30,
            permanent_loss_case_sized=True)
        self.assertEqual(classify(inputs)['archetype'], 'NOT_QUALIFIED')

    def test_emerging_outlier_near_base(self):
        inputs = base_inputs(
            category_scores={'structural_change_and_leadership': 12, 'customer_value_and_product': 8,
                             'moat_trajectory': 10, 'incremental_roic_and_fcf_per_share': 8,
                             'management_and_capital_allocation': 7, 'financial_survivability': 7,
                             'expectation_gap_and_valuation': 9, 'power_law_and_asymmetry': 8},
            current_price=100.0, base_value_per_share=105.0)
        result = classify(inputs)
        self.assertEqual(result['archetype'], 'EMERGING_OUTLIER')
        self.assertEqual(result['position_ceiling'], 'HIGH_CONVICTION')

    def test_expectation_gap_requires_a_mispricing_mechanism(self):
        inputs = base_inputs(
            category_scores={'structural_change_and_leadership': 7, 'customer_value_and_product': 6,
                             'moat_trajectory': 7, 'incremental_roic_and_fcf_per_share': 7,
                             'management_and_capital_allocation': 6, 'financial_survivability': 7,
                             'expectation_gap_and_valuation': 11, 'power_law_and_asymmetry': 5},
            current_price=100.0, base_value_per_share=160.0)
        self.assertEqual(classify(inputs)['not_qualified_reason'], 'MISPRICING_MECHANISM_NOT_ESTABLISHED')
        inputs['mispricing_mechanism'] = 'Transitory freight cost is being extrapolated as structural'
        inputs['mispricing_falsifiers'] = ['Freight cost stays elevated for two more quarters']
        self.assertEqual(classify(inputs)['archetype'], 'EXPECTATION_GAP')

    def test_price_alone_does_not_create_a_gap_archetype(self):
        """A cheap price with eroding economics stays out of EXPECTATION_GAP."""
        inputs = base_inputs(
            category_scores={'structural_change_and_leadership': 5, 'customer_value_and_product': 5,
                             'moat_trajectory': 4, 'incremental_roic_and_fcf_per_share': 4,
                             'management_and_capital_allocation': 5, 'financial_survivability': 7,
                             'expectation_gap_and_valuation': 11, 'power_law_and_asymmetry': 4},
            current_price=100.0, base_value_per_share=200.0,
            mispricing_mechanism='The stock is down a lot', mispricing_falsifiers=['it keeps falling'])
        result = classify(inputs)
        self.assertEqual(result['archetype'], 'NOT_QUALIFIED')
        self.assertEqual(result['not_qualified_reason'], 'QUALITY_GATES_NOT_MET')

    def test_quality_business_priced_beyond_base(self):
        result = classify(base_inputs(current_price=100.0, base_value_per_share=70.0))
        self.assertEqual(result['archetype'], 'NOT_QUALIFIED')
        self.assertEqual(result['not_qualified_reason'], 'PRICED_BEYOND_BASE')
        self.assertIn('COMPOUNDER', result['quality_gates_met'])

    def test_precedence_is_deterministic_and_total(self):
        for inputs in [base_inputs(), base_inputs(hard_veto_status='FAIL'), base_inputs(business_quality_75=None)]:
            first = classify(inputs)
            self.assertEqual(first, classify(dict(inputs)))
            self.assertIn(first['archetype'],
                          {'COMPOUNDER', 'MOONSHOT', 'EMERGING_OUTLIER', 'EXPECTATION_GAP', 'NOT_QUALIFIED'})

    def test_low_confidence_blocks_compounder(self):
        confidence = {name: 0.7 for name in SCORECARD_CATEGORIES} | {'moat_trajectory': 0.3}
        self.assertNotEqual(classify(base_inputs(category_confidence=confidence))['archetype'], 'COMPOUNDER')


class DocumentTests(unittest.TestCase):
    def document(self):
        inputs = base_inputs()
        result = classify(inputs)
        return {'schema_version': '1.0.0', 'ticker': 'TEST', 'as_of': '2026-09-17', 'inputs': inputs,
                'what_would_change_it': ['Incremental ROIC falls below the reinvestment hurdle'],
                **{k: v for k, v in result.items() if k != 'expectation_gap_ratio'}}

    def test_consistent_document_passes(self):
        self.assertEqual(check_document(self.document()), [])

    def test_stored_archetype_cannot_disagree_with_policy(self):
        document = self.document(); document['archetype'] = 'MOONSHOT'
        self.assertTrue(any('archetype:' in message for message in check_document(document)))

    def test_stored_disruption_total_must_equal_dimensions(self):
        document = self.document(); document['inputs']['disruption_total'] = 18
        self.assertIn('inputs.disruption_total does not equal the dimension sum', check_document(document))

    def test_build_inputs_from_assessment(self):
        categories = {name: {'score': 8, 'confidence': 0.6} for name in SCORECARD_CATEGORIES}
        assessment = {'categories': categories, 'business_quality_75': 48, 'research_state': 'FULL_ANALYSIS',
                      'hard_veto': {'overall_status': 'PASS'}}
        disruption = {'dimensions': {name: {'score': 2} for name in DISRUPTION_DIMENSIONS},
                      'self_funded': True}
        inputs = build_inputs(assessment, disruption, current_price=50.0, base_value_per_share=60.0)
        self.assertEqual(inputs['disruption_total'], 10)
        self.assertEqual(inputs['disruption_tier'], 'EMERGING')
        self.assertAlmostEqual(inputs['expectation_gap_ratio'], 0.2)


if __name__ == '__main__':
    unittest.main()

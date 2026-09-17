"""Disruption axis scoring and deterministic five-way archetype classification.

Implements policy/disruption-axis.yaml and policy/archetype-classification.yaml.
Both are additive layers: nothing here reads, writes or rescales the eight
scorecard categories, the 100-point total or the nine Hard Vetoes. A Hard Veto
FAIL forces NOT_QUALIFIED, and an unknown input produces NOT_QUALIFIED with
reason INSUFFICIENT_EVIDENCE rather than a guessed archetype.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DISRUPTION_DIMENSIONS = {
    'non_consumption_and_new_market_creation': 4,
    'incumbent_business_model_conflict': 4,
    'cost_or_performance_curve': 4,
    's_curve_position_and_adoption_evidence': 4,
    'platform_optionality_and_second_curve': 4,
}
DISRUPTION_TIERS = [('FOUNDATIONAL', 17), ('STRONG', 13), ('EMERGING', 9), ('INCREMENTAL', 4), ('NONE', 0)]

SCORECARD_CATEGORIES = [
    'structural_change_and_leadership', 'customer_value_and_product', 'moat_trajectory',
    'incremental_roic_and_fcf_per_share', 'management_and_capital_allocation',
    'financial_survivability', 'expectation_gap_and_valuation', 'power_law_and_asymmetry',
]

PRECEDENCE = ['COMPOUNDER', 'MOONSHOT', 'EMERGING_OUTLIER', 'EXPECTATION_GAP']
ARCHETYPE_KO = {'COMPOUNDER': '컴파운더', 'MOONSHOT': '문샷형', 'EMERGING_OUTLIER': '이머징 아웃라이어',
                'EXPECTATION_GAP': '기대차형', 'NOT_QUALIFIED': '비적격형'}
POSITION_CEILING = {'COMPOUNDER': 'EXCEPTIONAL_WINNER', 'MOONSHOT': 'STARTER',
                    'EMERGING_OUTLIER': 'HIGH_CONVICTION', 'EXPECTATION_GAP': 'NORMAL',
                    'NOT_QUALIFIED': 'NONE'}
MOONSHOT_GAP_TOLERANCE = {'FOUNDATIONAL': -0.60, 'STRONG': -0.40}

# Gate kinds: 'quality' and 'survivability' describe the business, 'valuation'
# describes the price, 'mechanism' describes required evidence discipline.
# quality_gates_met records archetypes that failed on price or evidence only.
BUSINESS_KINDS = ('quality', 'survivability')


def disruption_total(dimensions):
    """Sum of the five dimensions, or None when any dimension is unknown."""
    values = [dimensions.get(name) for name in DISRUPTION_DIMENSIONS]
    for name, value in zip(DISRUPTION_DIMENSIONS, values):
        if value is not None:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(f'{name}: score must be a number or null')
            if not 0 <= value <= DISRUPTION_DIMENSIONS[name]:
                raise ValueError(f'{name}: score outside 0..{DISRUPTION_DIMENSIONS[name]}')
    return sum(values) if all(v is not None for v in values) else None


def disruption_tier(dimensions):
    """Tier is never inferred from a partial sum."""
    total = disruption_total(dimensions)
    if total is None:
        return 'UNSCORED'
    return next(name for name, floor in DISRUPTION_TIERS if total >= floor)


def expectation_gap_ratio(base_value_per_share, current_price):
    """Positive means the base case sits above the current price. ESTIMATE, not FACT."""
    if base_value_per_share is None or current_price is None or current_price <= 0:
        return None
    return base_value_per_share / current_price - 1


def _at_least(value, floor):
    return value is not None and value >= floor


def _gates(inputs, gap):
    """Return {archetype: [(gate_name, kind, passed), ...]} for all four archetypes."""
    cat = inputs.get('category_scores', {})
    conf = inputs.get('category_confidence', {}) or {}
    dims = inputs.get('disruption_dimensions', {}) or {}
    quality = inputs.get('business_quality_75')
    veto_ok = inputs.get('hard_veto_status') != 'FAIL'
    tier = inputs.get('disruption_tier', 'UNSCORED')
    total = inputs.get('disruption_total')
    runway = inputs.get('funding_runway_months')
    funded = bool(inputs.get('self_funded')) or _at_least(runway, 24)
    mechanism = (inputs.get('mispricing_mechanism') or '').strip()

    return {
        'COMPOUNDER': [
            ('hard_veto_not_fail', 'quality', veto_ok),
            ('business_quality_75>=52', 'quality', _at_least(quality, 52)),
            ('moat_trajectory>=11', 'quality', _at_least(cat.get('moat_trajectory'), 11)),
            ('incremental_roic_and_fcf_per_share>=11', 'quality', _at_least(cat.get('incremental_roic_and_fcf_per_share'), 11)),
            ('management_and_capital_allocation>=7', 'quality', _at_least(cat.get('management_and_capital_allocation'), 7)),
            ('financial_survivability>=7', 'survivability', _at_least(cat.get('financial_survivability'), 7)),
            ('moat_trajectory_confidence>=0.5', 'quality', _at_least(conf.get('moat_trajectory'), 0.5)),
            ('incremental_roic_confidence>=0.5', 'quality', _at_least(conf.get('incremental_roic_and_fcf_per_share'), 0.5)),
            ('expectation_gap_and_valuation>=7', 'valuation', _at_least(cat.get('expectation_gap_and_valuation'), 7)),
            ('expectation_gap_ratio>=-0.10', 'valuation', _at_least(gap, -0.10)),
        ],
        'MOONSHOT': [
            ('hard_veto_not_fail', 'quality', veto_ok),
            ('disruption_total>=14', 'quality', _at_least(total, 14)),
            ('disruption_tier_in_STRONG_FOUNDATIONAL', 'quality', tier in MOONSHOT_GAP_TOLERANCE),
            ('non_consumption_and_new_market_creation>=3', 'quality', _at_least(dims.get('non_consumption_and_new_market_creation'), 3)),
            ('incumbent_business_model_conflict>=3', 'quality', _at_least(dims.get('incumbent_business_model_conflict'), 3)),
            ('s_curve_position_and_adoption_evidence>=2', 'quality', _at_least(dims.get('s_curve_position_and_adoption_evidence'), 2)),
            ('power_law_and_asymmetry>=8', 'quality', _at_least(cat.get('power_law_and_asymmetry'), 8)),
            ('structural_change_and_leadership>=11', 'quality', _at_least(cat.get('structural_change_and_leadership'), 11)),
            ('business_quality_75>=40', 'quality', _at_least(quality, 40)),
            ('financial_survivability>=5', 'survivability', _at_least(cat.get('financial_survivability'), 5)),
            ('self_funded_or_runway>=24m', 'survivability', funded),
            ('permanent_loss_case_sized', 'mechanism', bool(inputs.get('permanent_loss_case_sized'))),
            ('expectation_gap_ratio>=tier_tolerance', 'valuation',
             _at_least(gap, MOONSHOT_GAP_TOLERANCE[tier]) if tier in MOONSHOT_GAP_TOLERANCE else False),
        ],
        'EMERGING_OUTLIER': [
            ('hard_veto_not_fail', 'quality', veto_ok),
            ('power_law_and_asymmetry>=7', 'quality', _at_least(cat.get('power_law_and_asymmetry'), 7)),
            ('structural_change_and_leadership>=10', 'quality', _at_least(cat.get('structural_change_and_leadership'), 10)),
            ('moat_trajectory>=9', 'quality', _at_least(cat.get('moat_trajectory'), 9)),
            ('business_quality_75>=45', 'quality', _at_least(quality, 45)),
            ('financial_survivability>=6', 'survivability', _at_least(cat.get('financial_survivability'), 6)),
            ('expectation_gap_ratio>=-0.15', 'valuation', _at_least(gap, -0.15)),
        ],
        'EXPECTATION_GAP': [
            ('hard_veto_not_fail', 'quality', veto_ok),
            ('business_quality_75>=38', 'quality', _at_least(quality, 38)),
            ('moat_trajectory>=6', 'quality', _at_least(cat.get('moat_trajectory'), 6)),
            ('incremental_roic_and_fcf_per_share>=6', 'quality', _at_least(cat.get('incremental_roic_and_fcf_per_share'), 6)),
            ('financial_survivability>=6', 'survivability', _at_least(cat.get('financial_survivability'), 6)),
            ('mispricing_mechanism_stated', 'mechanism', bool(mechanism)),
            ('mispricing_falsifier_stated', 'mechanism', bool(inputs.get('mispricing_falsifiers'))),
            ('expectation_gap_ratio>=0.35', 'valuation', _at_least(gap, 0.35)),
        ],
    }


def _missing_essentials(inputs):
    """Inputs without which no archetype can be asserted. Disruption is required only for MOONSHOT."""
    missing = []
    if inputs.get('business_quality_75') is None:
        missing.append('business_quality_75')
    cat = inputs.get('category_scores', {})
    missing += [f'category_scores.{name}' for name in SCORECARD_CATEGORIES if cat.get(name) is None]
    for field in ['current_price', 'base_value_per_share']:
        if inputs.get(field) is None:
            missing.append(field)
    return missing


def _not_qualified_reason(inputs, results, quality_gates_met):
    if inputs.get('hard_veto_status') == 'FAIL':
        return 'HARD_VETO_FAIL'
    if _missing_essentials(inputs):
        return 'INSUFFICIENT_EVIDENCE'
    for name in PRECEDENCE:
        if name in quality_gates_met:
            kinds = {kind for _, kind, passed in results[name] if not passed}
            if name == 'MOONSHOT':
                return 'PRICED_BEYOND_MOONSHOT_TOLERANCE'
            if kinds == {'mechanism'}:
                return 'MISPRICING_MECHANISM_NOT_ESTABLISHED'
            return 'PRICED_BEYOND_BASE'
    for name in PRECEDENCE:
        failed = {kind for _, kind, passed in results[name] if not passed}
        if failed == {'survivability'}:
            return 'SURVIVABILITY_GATE_NOT_MET'
    return 'QUALITY_GATES_NOT_MET'


def classify(inputs):
    """Deterministically assign exactly one archetype. Pure function of `inputs`."""
    gap = inputs.get('expectation_gap_ratio')
    if gap is None:
        gap = expectation_gap_ratio(inputs.get('base_value_per_share'), inputs.get('current_price'))
    results = _gates(inputs, gap)
    blocked = bool(_missing_essentials(inputs)) or inputs.get('hard_veto_status') == 'FAIL'
    quality_gates_met = [] if blocked else [
        name for name in PRECEDENCE
        if all(passed for _, kind, passed in results[name] if kind in BUSINESS_KINDS)
        and not all(passed for _, _, passed in results[name])
    ]
    assigned = None if blocked else next(
        (name for name in PRECEDENCE if all(passed for _, _, passed in results[name])), None)
    archetype = assigned or 'NOT_QUALIFIED'
    provisional = inputs.get('research_state') != 'FULL_ANALYSIS'
    # Hard Veto > Score > Archetype: an unresolved veto or incomplete research
    # leaves no room to size a position, whatever the archetype implies.
    ceiling = POSITION_CEILING[archetype]
    if provisional or inputs.get('hard_veto_status') != 'PASS':
        ceiling = 'NONE'
    return {
        'archetype': archetype,
        'archetype_ko': ARCHETYPE_KO[archetype],
        'provisional': provisional,
        'not_qualified_reason': None if assigned else _not_qualified_reason(inputs, results, quality_gates_met),
        'quality_gates_met': quality_gates_met,
        'gate_results': {name: {'passed': all(p for _, _, p in gates),
                                'failed_gates': [g for g, _, p in gates if not p]}
                         for name, gates in results.items()},
        'position_ceiling': ceiling,
        'expectation_gap_ratio': gap,
    }


def build_inputs(assessment, disruption, current_price, base_value_per_share, **extra):
    """Assemble classifier inputs from an assessment-v2 document and a disruption document."""
    dims = {name: disruption['dimensions'][name]['score'] for name in DISRUPTION_DIMENSIONS}
    categories = assessment['categories']
    inputs = {
        'hard_veto_status': assessment['hard_veto']['overall_status'],
        'research_state': assessment['research_state'],
        'business_quality_75': assessment['business_quality_75'],
        'category_scores': {name: categories[name]['score'] for name in SCORECARD_CATEGORIES},
        'category_confidence': {name: categories[name]['confidence'] for name in SCORECARD_CATEGORIES},
        'disruption_total': disruption_total(dims),
        'disruption_tier': disruption_tier(dims),
        'disruption_dimensions': dims,
        'current_price': current_price,
        'base_value_per_share': base_value_per_share,
        'self_funded': disruption.get('self_funded'),
        'funding_runway_months': disruption.get('funding_runway_months'),
    }
    inputs['expectation_gap_ratio'] = expectation_gap_ratio(base_value_per_share, current_price)
    inputs.update(extra)
    return inputs


def check_document(document):
    """Recompute a stored archetype.json and return the disagreements."""
    errors = []
    inputs = document['inputs']
    dims = inputs.get('disruption_dimensions', {})
    if set(dims) != set(DISRUPTION_DIMENSIONS):
        errors.append('inputs.disruption_dimensions must contain exactly the five policy dimensions')
    else:
        if inputs.get('disruption_total') != disruption_total(dims):
            errors.append('inputs.disruption_total does not equal the dimension sum')
        if inputs.get('disruption_tier') != disruption_tier(dims):
            errors.append('inputs.disruption_tier does not match the policy tier bands')
    stated_gap = inputs.get('expectation_gap_ratio')
    computed_gap = expectation_gap_ratio(inputs.get('base_value_per_share'), inputs.get('current_price'))
    if stated_gap is not None and computed_gap is not None and abs(stated_gap - computed_gap) > 1e-9:
        errors.append('inputs.expectation_gap_ratio does not equal base_value_per_share / current_price - 1')
    result = classify(inputs)
    fields = ['archetype', 'provisional', 'not_qualified_reason', 'position_ceiling']
    fields += ['archetype_ko'] if 'archetype_ko' in document else []
    for field in fields:
        if document.get(field) != result[field]:
            errors.append(f'{field}: stored {document.get(field)!r}, policy classifier gives {result[field]!r}')
    if sorted(document.get('quality_gates_met', [])) != sorted(result['quality_gates_met']):
        errors.append('quality_gates_met does not match the classifier')
    if document.get('gate_results') != result['gate_results']:
        errors.append('gate_results do not match the classifier')
    if document['archetype'] == 'NOT_QUALIFIED' and not document.get('not_qualified_reason'):
        errors.append('NOT_QUALIFIED requires not_qualified_reason')
    return errors


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    paths = [Path(a) for a in argv if not a.startswith('-')] or sorted((ROOT / 'companies').glob('*/archetype.json'))
    if not paths:
        print(json.dumps({'status': 'PASS', 'checked': 0, 'note': 'no archetype.json files yet'}, ensure_ascii=False))
        return 0
    failures = []
    for path in paths:
        document = json.loads(Path(path).read_text(encoding='utf-8'))
        failures += [f'{path}: {message}' for message in check_document(document)]
    if failures:
        print('ARCHETYPE CHECK FAILED')
        for failure in failures:
            print(f'- {failure}')
        return 1
    print(json.dumps({'status': 'PASS', 'checked': len(paths)}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

"""Lossless raw adapters, guarded calculations and explicit research state.

Raw extractions are assertions from supplied sources, not independently audited
facts. Never overwrite raw data, convert missing values to zero, or sum cash
figures whose accounting scope/period/currency is not known to agree.
"""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = '2026-09-06'
CATEGORIES = {
    'structural_change_and_leadership': 15, 'customer_value_and_product': 10,
    'moat_trajectory': 15, 'incremental_roic_and_fcf_per_share': 15,
    'management_and_capital_allocation': 10, 'financial_survivability': 10,
    'expectation_gap_and_valuation': 15, 'power_law_and_asymmetry': 10,
}
VETO_IDS = ['management_or_accounting_integrity', 'external_capital_dependence',
    'persistent_dilution', 'low_quality_growth', 'incremental_roic_collapse',
    'moat_shrinkage', 'price_requires_unrealistic_bull_case',
    'fatal_concentration', 'permanent_loss_probability']


def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def jsonl(path):
    p = ROOT / path
    return [json.loads(s) for s in p.read_text().splitlines() if s.strip()] if p.exists() else []


def unit_info(unit):
    """Only explicit money units; ambiguous mixed units are retained unconverted."""
    s = (unit or '').strip().lower()
    match = re.fullmatch(r'(usd|krw)(?: (thousand|million|billion|trillion)s?)?(?: cash outflow)?', s)
    if not match:
        return None, None
    scale = {None: 1, 'thousand': 1e3, 'million': 1e6, 'billion': 1e9, 'trillion': 1e12}[match[2]]
    return match[1].upper(), scale


def pointer_escape(s):
    return str(s).replace('~', '~0').replace('/', '~1')


def resolve_pointer(obj, pointer):
    for part in pointer.strip('/').split('/') if pointer else []:
        part = part.replace('~1', '/').replace('~0', '~')
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj


def observations(path):
    """Adapt both explicit value records and nested statement maps losslessly.

    Does NOT turn names like h1_2026 into an asserted reporting period. Parent
    context is kept in the pointer and missing metadata is an explicit flag.
    """
    doc = read(path)
    digest = sha(path)
    ticker = doc['ticker']
    rows = []
    def walk(node, ptr='', inherited=None):
        context = dict(inherited or {})
        if isinstance(node, dict):
            for k in ['period', 'unit', 'source', 'location', 'original_location', 'confidence']:
                if k in node:
                    context[k] = node[k]
            if 'value' in node:
                emit(node['value'], ptr + '/value', node, context)
                return
            for k, value in node.items():
                if k in ['ticker', 'as_of', 'mode', 'source', 'location', 'original_location', 'confidence', 'period', 'unit']:
                    continue
                p = ptr + '/' + pointer_escape(k)
                if isinstance(value, (dict, list)):
                    walk(value, p, context)
                elif (isinstance(value, (int, float)) and not isinstance(value, bool)) or value is None:
                    # Nested statement fields are retained even if metadata are incomplete.
                    emit(value, p, {'metric': k}, context)
        elif isinstance(node, list):
            for i, item in enumerate(node):
                walk(item, ptr + '/' + str(i), context)
    def emit(value, ptr, meta, ctx):
        currency, scale = unit_info(ctx.get('unit'))
        numeric = isinstance(value, (int, float)) and not isinstance(value, bool)
        location = ctx.get('original_location', ctx.get('location'))
        flags = []
        if value is None: flags.append('VALUE_NOT_REPORTED')
        if not ctx.get('period'): flags.append('PERIOD_NOT_EXPLICIT')
        if not ctx.get('unit'): flags.append('UNIT_NOT_EXPLICIT')
        if not ctx.get('source'): flags.append('DOCUMENT_NOT_EXPLICIT')
        if not location: flags.append('LOCATION_NOT_EXPLICIT')
        rows.append({'id': 'obs-' + hashlib.sha256((path+'#'+ptr+digest).encode()).hexdigest()[:20],
            'ticker': ticker, 'kind': 'reported_assertion', 'raw_path': path,
            'raw_sha256': digest, 'json_pointer': ptr,
            'metric': meta.get('metric', meta.get('item', ptr.split('/')[1])),
            'value': value, 'period': ctx.get('period'), 'unit': ctx.get('unit'),
            'currency': currency, 'value_base_currency': value*scale if numeric and scale else None,
            'source': ctx.get('source'), 'location': location,
            'extraction_confidence': ctx.get('confidence'), 'verification': 'RAW_ASSERTION_NOT_FULL_SOURCE_REAUDIT',
            'flags': flags})
    walk(doc)
    return rows


def aggregate_veto(items):
    states = {v['status'] for v in items}
    return 'FAIL' if 'FAIL' in states else 'INVESTIGATE' if 'INVESTIGATE' in states else 'PASS'


def totals(categories):
    assert set(categories) == set(CATEGORIES)
    for key, item in categories.items():
        assert item['max_score'] == CATEGORIES[key]
        if item['score'] is not None:
            assert isinstance(item['score'], (int, float)) and not isinstance(item['score'], bool)
            assert 0 <= item['score'] <= item['max_score']
    values = [categories[k]['score'] for k in CATEGORIES]
    return (sum(values) if all(v is not None for v in values) else None,
            sum(values[:6]) if all(v is not None for v in values[:6]) else None)


def calculate(spec, row_map):
    inputs = [row_map[x] for x in spec['inputs']]
    for row in inputs:
        assert isinstance(row['value_base_currency'], (int, float)), 'Unknown or ambiguous input'
        assert row['period'] and row['currency'], 'Explicit period and currency required'
    assert spec.get('accounting_scope'), 'Explicit accounting scope required'
    assert spec.get('comparability_note'), 'Explicit period and basis comparison required'
    assert len({r['currency'] for r in inputs}) == 1, 'Mixed currencies'
    if spec['operation'] != 'growth':
        assert len({r['period'] for r in inputs}) == 1, 'Different periods'
    else:
        # This first adapter supports only explicitly matched H1 comparisons.
        # Add other fiscal-window adapters with boundary tests, never infer them.
        periods=[re.fullmatch(r'H1 (\d{4})(?: comparative| comparator)?',r['period']) for r in inputs]
        assert len(periods)==2 and all(periods), 'Growth requires explicit matched fiscal windows'
        assert int(periods[0][1])==int(periods[1][1])+1, 'Growth inputs must be current/prior year'
    x = [r['value_base_currency'] for r in inputs]
    if spec['operation'] == 'margin':
        assert x[1] > 0
        value = x[0]/x[1]
    elif spec['operation'] == 'growth':
        assert x[1] > 0
        value = x[0]/x[1]-1
    elif spec['operation'] == 'ocf_less_explicit_capex':
        assert x[1] >= 0, 'Outflow sign must be explicitly normalized in the analysis input'
        value = x[0]-x[1]
    else:
        raise ValueError('Unsupported calculation')
    return {**spec, 'value': value, 'claim_type': 'estimate', 'method_status': 'CALCULATED_FROM_REPORTED_ASSERTIONS'}


def validate_assessment(d):
    assert d['ticker'] and re.fullmatch(r'\d{4}-\d{2}-\d{2}',d['as_of'])
    total, quality = totals(d['categories'])
    assert d['total_score_100'] == total and d['business_quality_75'] == quality
    assert len(d['hard_veto']['items']) == 9
    assert {x['id'] for x in d['hard_veto']['items']} == set(VETO_IDS)
    assert d['hard_veto']['overall_status'] == aggregate_veto(d['hard_veto']['items'])
    if d['hard_veto']['overall_status'] == 'FAIL':
        assert d['decision'] in ['REJECT', 'EXIT']
    if d['research_state'] != 'FULL_ANALYSIS':
        assert not d['buy_authorized'] and d['position_band'] == 'NONE'
    if d['buy_authorized']:
        assert d['hard_veto']['overall_status'] == 'PASS'
        assert d['valuation']['status'] == 'OWNER_CASHFLOW_MODEL'
        assert d['total_score_100'] is not None
    if d['research_state'] == 'FULL_ANALYSIS':
        assert d['total_score_100'] is not None
        assert d['valuation']['reverse_expectations']
        assert set(d['valuation']['scenarios']) == {'bear','base','bull'}
        assert all(d['valuation']['scenarios'].values())
    assert len(d['red_team']['attacks']) == 10
    assert d['sell_evidence'] and d['source_quality']
    for c in d['categories'].values():
        assert c['evidence'] and c['counter_evidence'] and 0 <= c['confidence'] <= 1
        if c['score'] is None: assert c['missing_data']
    assert d['falsifiers'] and d['increase_evidence'] and d['permanent_loss_case']


def dumps(x):
    return json.dumps(x, ensure_ascii=False, indent=2, allow_nan=False)+'\n'

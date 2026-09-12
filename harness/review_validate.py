"""Validate the dated review without rewriting or relaxing historical inputs."""
from __future__ import annotations
import json
import math
from collections import Counter
from .core import ROOT, read, sha, resolve_pointer, validate_assessment, calculate
from .review_run import DIRECTORY, outputs, eligible, weights


def validate(replay=True):
    import jsonschema
    schema = read('schemas/assessment-v2.schema.json')
    lock = read('harness/baseline-lock.json')
    for section in ['raw_file_sha256', 'policy_sha256']:
        for path, digest in lock[section].items():
            assert sha(path) == digest, ('IMMUTABILITY', path)
    manifest = read(DIRECTORY + '/input-manifest.json')
    for entry in manifest['files']:
        assert sha(entry['path']) == entry['sha256'], ('INPUT_CHANGED', entry['path'])
    raw_paths = {str(p.relative_to(ROOT)) for p in (ROOT/'companies').glob('*/raw-data/*.json')}
    assert raw_paths == set(manifest['canonical_raw_inventory']), 'UNREVIEWED_RAW_ADDITION'
    assert set(lock['raw_file_sha256']) <= raw_paths
    registry = read('registry/companies.json')['companies']
    tickers = [r['ticker'] for r in registry]
    assert len(tickers) == len(set(tickers)) == lock['universe_count']
    expected = read('reviews/2026-09-05-astra/coverage.json') + read('harness/additional-universe.json')
    assert set(tickers) == {r['ticker'] for r in expected}
    # The remote snapshot also contains explicitly unpromoted LS Cable research.
    # Validate that separate inventory without relabeling it a canonical issuer.
    external_research = manifest['out_of_registry_research']
    assert set(tickers) | set(external_research) == {p.name for p in (ROOT/'companies').iterdir() if p.is_dir()}
    for ticker, path in external_research.items():
        assert ticker not in tickers and not (ROOT/'companies'/ticker/'latest.json').exists()
        record = read(path)
        assert record['ticker'] == ticker and record['research_state'] == 'PARTIAL_ANALYSIS'
        assert record['total_score_100'] is None and not record['buy_authorized']
    aliases = [a for r in registry for a in r['aliases']]
    assert len(aliases) == len(set(aliases)) and not set(aliases) & set(tickers)
    assert next(r for r in registry if r['ticker']=='GOOGL')['aliases'] == ['GOOG']
    full_count = 0
    for r in registry:
        latest = read(r['latest']); a = read(latest['assessment'])
        assert a['ticker'] == r['ticker'] and a['research_state'] == r['research_state']
        assert latest['as_of'] == a['as_of'] and latest['research_state'] == a['research_state']
        jsonschema.Draft202012Validator(schema).validate(a)
        validate_assessment(a)
        assert not a['buy_authorized']
        for path in a['source_paths']: assert (ROOT/path).is_file(), path
        for entry in a['historical_records']: assert (ROOT/entry['path']).is_file(), entry
        folder = latest['assessment'].rsplit('/', 1)[0]
        if a['research_state'] == 'FULL_ANALYSIS':
            full_count += 1
            lineage = read(folder + '/lineage.json')
            for entry in lineage['records']:
                assert sha(entry['path']) == entry['sha256'], ('LINEAGE_CHANGED', entry['path'])
            for key, pointer in lineage['category_pointers'].items():
                previous = resolve_pointer(read(pointer['path']), pointer['json_pointer'])
                assert previous['max_score'] == a['categories'][key]['max_score']
                override = read(DIRECTORY+'/judgments.json')['score_changes'].get(r['ticker'], {})
                assert a['categories'][key]['score'] == override.get(key, previous['score'])
        else:
            assert (ROOT/(folder+'/observations.json')).is_file()
    observations_count = 0; derived_count = 0
    bridged_count = 0; paraphrase_count = 0; preserved_metric_documents = []
    bridges = {(e['observations_path'],e['observation_id']):e for e in read(DIRECTORY+'/observation-bridges.json')['entries']}
    for path in (ROOT/'companies').glob('*/analyses/*/observations.json'):
        observations = json.loads(path.read_text())
        if isinstance(observations, dict):
            assert observations['ticker'] == path.parents[2].name
            entries = observations['observations']
            assert len(entries) == len({o['id'] for o in entries})
            for o in entries:
                bridge = bridges[(str(path.relative_to(ROOT)),o['id'])]
                assert o['value'] == bridge['observed_value']
                assert sha(bridge['raw_path']) == bridge['raw_sha256']
                value = resolve_pointer(read(bridge['raw_path']), bridge['json_pointer'])
                if bridge['method'] == 'EXACT_NUMERIC_WITH_EXPLICIT_UNIT_CONVERSION':
                    assert math.isclose(value*bridge['scale_factor'], o['value'], abs_tol=1e-9)
                    bridged_count += 1
                else:
                    assert bridge['method'] == 'REVIEWED_PARAPHRASE_NOT_EXACT_RAW_VALUE'
                    assert value == bridge['source_text']
                    paraphrase_count += 1
            # These older metric documents contain rounded narrative calculations
            # without executable formula specifications. Preserve/hash them; do
            # not count them as reproduced calculations. Current valuation and
            # reverse calculations are independently reproduced below.
            preserved_metric_documents.append(str((path.parent/'derived-metrics.json').relative_to(ROOT)))
            continue
        row_map = {o['id']: o for o in observations}
        assert len(observations) == len(row_map), ('DUPLICATE_OBSERVATION', str(path))
        ticker = path.parents[2].name
        for o in observations:
            assert o['ticker'] == ticker
            assert sha(o['raw_path']) == o['raw_sha256']
            assert resolve_pointer(read(o['raw_path']), o['json_pointer']) == o['value']
        observations_count += len(observations)
        derived_path = path.parent/'derived-metrics.json'
        if derived_path.exists():
            derived = json.loads(derived_path.read_text())
            assert isinstance(derived, list), ('UNSUPPORTED_DERIVED_SCHEMA', str(derived_path))
            for item in derived:
                recalculated = calculate({k:v for k,v in item.items() if k not in ['value','claim_type','method_status']}, row_map)
                assert math.isclose(item['value'], recalculated['value'], abs_tol=1e-10)
                derived_count += 1
    assert read('reviews/latest.json')['state_counts'] == dict(Counter(r['research_state'] for r in registry))
    files, rows, assessments = outputs()
    assert full_count == len(rows) == len(assessments) == 43
    for path, content in files.items():
        assert (ROOT/path).read_text() == content, ('REVIEW_NOT_REPRODUCIBLE', path)
    for row in rows:
        v = read(row['valuation'])
        values = [v['scenarios'][s]['value_per_share'] for s in ['bear','base','bull']]
        assert 0 <= values[0] <= values[1] <= values[2], ('SCENARIO_ORDER', row['ticker'])
        reverse = v['reverse_expectations']
        assert reverse['growth'] is not None, ('NO_REVERSE_SOLUTION', row['ticker'])
        assert abs(reverse['price_residual']) < max(1e-6, row['quote']['price'] * 1e-8)
        assert row['eligible'] == eligible(row['score'], row['management_score'], row['quote']['price'], row['base_value'], row['hard_veto'])
        if row['ticker'] == '145020':
            assert all(math.isclose(v['scenarios'][s]['required_return'], .10) for s in ['bear','base','bull'])
        else:
            for s in ['bear','base','bull']:
                scenario = v['scenarios'][s]
                assert abs(scenario['recalculation_difference']) <= max(1, abs(scenario['source_reported_value'])*.0001), ('MODEL_DRIFT', row['ticker'], s)
    selected = [r for r in rows if r['eligible']]
    allocation = weights(selected)
    assert all(r['weight_bp'] == allocation.get(r['ticker'], 0) for r in rows)
    assert sum(allocation.values()) == (10000 if selected else 0)
    assert len(selected) <= 30
    replay_counts = {}
    if replay:
        from .frozen_replay import check
        replay_counts = check()
    return {'status':'PASS', 'issuers':len(tickers), 'full_analysis_rechecked':full_count,
            'selected':len(selected), 'selected_score_sum':sum(r['score'] for r in selected),
            'weight_sum_bp':sum(allocation.values()), 'baseline_raw_files_unchanged':len(lock['raw_file_sha256']),
            'current_raw_files':len(raw_paths), 'policy_files_unchanged':len(lock['policy_sha256']),
            'verified_input_files':len(manifest['files']), 'observations_with_valid_raw_pointers':observations_count,
            'supplemental_numeric_observations_with_explicit_unit_bridges':bridged_count,
            'reviewed_paraphrases_not_counted_as_exact_raw_values':paraphrase_count,
            'historical_metric_documents_preserved_but_not_counted_as_formula_replay':preserved_metric_documents,
            'reproduced_derived_metrics':derived_count, 'reproduced_review_artifacts':len(files),
            'frozen_replay':replay_counts, 'buy_authorizations':0}


def main():
    print(json.dumps(validate(), ensure_ascii=False))


if __name__ == '__main__':
    main()

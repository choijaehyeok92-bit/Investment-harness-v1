"""Validate current authority, evidence lineage, invariants and reproducibility."""
from __future__ import annotations
import json
import math
from .core import ROOT, read, sha, resolve_pointer, validate_assessment, calculate
from .build import outputs, DIRECTORY

def main():
    if read('reviews/latest.json')['directory']=='reviews/2026-09-12-full-review':
        from .review_validate import main as reviewed_main
        return reviewed_main()
    import jsonschema
    schema=read('schemas/assessment-v2.schema.json')
    lock=read('harness/baseline-lock.json')
    for section in ['raw_file_sha256','policy_sha256']:
        for p,h in lock[section].items(): assert sha(p)==h, ('IMMUTABILITY',p)
    assert set(lock['raw_file_sha256'])=={str(p.relative_to(ROOT)) for p in (ROOT/'companies').glob('*/raw-data/*.json')}, 'New raw data require a new reviewed run'
    registry=read('registry/companies.json')['companies'];tickers=[r['ticker'] for r in registry]
    assert len(tickers)==len(set(tickers))==lock['universe_count']
    expected=read('reviews/2026-09-05-astra/coverage.json')+read('harness/additional-universe.json')
    assert set(tickers)=={r['ticker'] for r in expected}
    assert set(tickers)=={p.name for p in (ROOT/'companies').iterdir() if p.is_dir()}, 'Unregistered company folder'
    aliases=[a for r in registry for a in r['aliases']]
    assert len(aliases)==len(set(aliases)) and not set(aliases)&set(tickers)
    assert next(r for r in registry if r['ticker']=='GOOGL')['aliases']==['GOOG']
    current=read('reviews/latest.json');assert current['registry']=='registry/companies.json'
    from .deep_inputs import DIRECTORY as DEEP_DIRECTORY, inputs as deep_inputs
    assert current['directory'] in [DIRECTORY,DEEP_DIRECTORY], 'Unknown authority run'
    observations_count=0;derived_count=0
    for r in registry:
        latest=read(r['latest']);d=read(latest['assessment'])
        assert d['ticker']==r['ticker'] and d['research_state']==r['research_state']
        assert latest['as_of']==d['as_of'] and latest['research_state']==d['research_state']
        jsonschema.Draft202012Validator(schema).validate(d);validate_assessment(d)
        base=latest['assessment'].rsplit('/',1)[0]
        obs=read(base+'/observations.json');rm={o['id']:o for o in obs}
        assert len(obs)==len(rm)
        for o in obs:
            assert o['ticker']==r['ticker']
            assert sha(o['raw_path'])==o['raw_sha256']
            assert resolve_pointer(read(o['raw_path']),o['json_pointer'])==o['value']
        for item in read(base+'/derived-metrics.json'):
            recalculated=calculate({k:v for k,v in item.items() if k not in ['value','claim_type','method_status']},rm)
            assert math.isclose(item['value'],recalculated['value'],abs_tol=1e-10)
            derived_count+=1
        observations_count+=len(obs)
        for p in d['source_paths']:assert (ROOT/p).is_file(),p
        for ref in d['historical_records']:assert (ROOT/ref['path']).is_file()
    for entry in read(DIRECTORY+'/source-manifest.json'):assert sha(entry['path'])==entry['sha256']
    files,ds=outputs()
    superseded=set()
    if current['directory']==DEEP_DIRECTORY:
        superseded={'registry/companies.json','reviews/latest.json'}|{f'companies/{t}/latest.json' for t in deep_inputs()}
    for p,content in files.items():
        if p not in superseded:assert (ROOT/p).read_text()==content,('NOT_REPRODUCIBLE',p)
    deep_count=0
    if current['directory']==DEEP_DIRECTORY:
        from .deep_report import outputs as deep_outputs
        df,dd=deep_outputs()
        assert len(dd)==34 and {d['ticker'] for d in dd}==set(deep_inputs())
        for p,content in df.items():assert (ROOT/p).read_text()==content,('DEEP_NOT_REPRODUCIBLE',p)
        assert all(d['completion_gate']['passed'] and not d['buy_authorized'] for d in dd)
        for entry in read(DEEP_DIRECTORY+'/source-manifest.json'):assert sha(entry['path'])==entry['sha256']
        deep_count=len(df)
    print(json.dumps({'status':'PASS','issuers':len(tickers),'raw_files_unchanged':len(lock['raw_file_sha256']),
        'policy_files_unchanged':len(lock['policy_sha256']),'observations_with_valid_raw_pointers':observations_count,
        'reproduced_derived_metrics':derived_count,'reproduced_frozen_artifacts':len(files)-len(superseded),
        'reproduced_deep_artifacts':deep_count},ensure_ascii=False))

if __name__=='__main__':main()

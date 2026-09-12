"""Evidence-specific management correction with immutable historical replay."""
from __future__ import annotations
import argparse
import copy
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from .core import ROOT, read, sha, dumps, totals, validate_assessment
from .review_run import eligible, weights

RUN = '2026-09-12-management-dedup'
DIRECTORY = 'reviews/' + RUN
BASE = 'reviews/2026-09-12-full-review'
MG = 'management_and_capital_allocation'
TICKERS = ('NVDA','TMDX')


def corrected_assessment(ticker, audit):
    finding = audit['findings'][ticker]
    assert finding['action']=='RESTORE'
    previous = read(finding['superseded_assessment'])
    baseline = read(finding['restore_from'])
    a = copy.deepcopy(previous)
    # NVDA retains ALL incremental acquisition/regulatory counter-evidence.
    # TMDX uses the already-reviewed category, removing its repeated third item.
    c = copy.deepcopy(previous['categories'][MG] if ticker=='NVDA' else baseline['categories'][MG])
    c['score'] = baseline['categories'][MG]['score']
    assert c['score']==finding['restored_management']==6
    c.update(prior_score=previous['categories'][MG]['score'],
             score_action='RESTORED_AFTER_DUPLICATE_EVIDENCE_WEIGHTING_AUDIT',
             reviewed_as_of='2026-09-12',correction_reason=finding['reason_ko'],
             source_paths=[finding['restore_from'],finding['superseded_assessment'],DIRECTORY+'/audit.json'])
    a['categories'][MG] = c
    a['total_score_100'],a['business_quality_75'] = totals(a['categories'])
    assert a['total_score_100']==finding['after_total']
    a['priority'] = 'P1'
    a['review_note_ko'] = finding['reason_ko']
    a['review_method'] = 'Targeted duplicate-evidence weighting audit, including original dated commits. Restore absolute prior management scores; preserve prices, valuation, other categories and vetoes.'
    a['authority_note'] = 'Supersedes management weighting in the preceding September 12 review. Historical records and all acquisition/regulatory risks remain preserved.'
    a['reassessment_delta'] = {'prior_canonical_score':previous['total_score_100'],
        'reviewed_score':a['total_score_100'],'prior_canonical_assessment':finding['superseded_assessment'],
        'restored_category_from':finding['restore_from'],'management_score_before':5,'management_score_after':6,
        'category_change_reason':finding['reason_ko'],'score_layer':'COMPANY_SCORE_NOT_MACRO_ADJUSTED_SCORE'}
    folder = f'companies/{ticker}/analyses/{RUN}'
    a['completion_gate']['scope'] = 'Prior full analysis retained; targeted management correction only. Open investigations are not resolved.'
    a['completion_gate']['source_lineage'] = folder+'/lineage.json'
    sources = set(a['source_paths'])|{finding['superseded_assessment'],finding['restore_from'],DIRECTORY+'/audit.json',BASE+'/portfolio.json',BASE+'/prices.json'}
    sources.update(x['path'] for x in finding.get('timeline',[]) if 'path' in x)
    a['source_paths'] = sorted(sources)
    a['historical_records'].append({'path':finding['superseded_assessment'],'status':'PRESERVED_PRIOR_REVIEW_WITH_SUPERSEDED_MANAGEMENT_WEIGHTING'})
    validate_assessment(a)
    return a


def outputs():
    snapshot = read(DIRECTORY+'/authority-input.json');audit = read(DIRECTORY+'/audit.json')
    files = {};assessments = {}
    for ticker in TICKERS:
        finding = audit['findings'][ticker];a = corrected_assessment(ticker,audit);assessments[ticker] = a
        folder = f'companies/{ticker}/analyses/{RUN}'
        lineage = {'ticker':ticker,'as_of':'2026-09-12',
            'records':[{'path':p,'sha256':sha(p)} for p in a['source_paths']],
            'restored_score_pointer':{'path':finding['restore_from'],'json_pointer':'/categories/'+MG+'/score'},
            'audit':DIRECTORY+'/audit.json','unchanged_valuation':a['valuation']['source_path'],
            'note':'Negative evidence and INVESTIGATE remain. The correction reverses repeated weighting, not the risks.'}
        prior_thesis = finding['restore_from'].replace('assessment.json','thesis.ko.md')
        thesis = f"# {ticker} 경영진 점수 정정\n\n2026-09-12 · **{a['total_score_100']}/100 · 경영진 6/10 · WATCH / INVESTIGATE**\n\n{finding['reason_ko']}\n\n[기존 심층분석](../../../../{prior_thesis}) · [정정 평가](assessment.json) · [현금 모형](../2026-09-12-full-review/valuation.json) · [정정 포트폴리오](../../../../{DIRECTORY}/README.md)\n"
        history = f"# {ticker} 의사결정 정정 이력\n\n- 직전: 총점 {finding['before_total']}, 경영진 5점.\n- 정정: 총점 {a['total_score_100']}, 경영진 6점. 복원 기준은 `{finding['restore_from']}`.\n- 정정 사유: {finding['reason_ko']}\n- 다른 일곱 점수·가격·가치·9개 Veto를 유지한다. 기존 분석 파일은 수정하지 않는다.\n- WATCH / INVESTIGATE, 모의 편입이며 실제 매수 승인은 없다.\n\n[날짜·커밋별 감사](../../../../{DIRECTORY}/audit.json)\n"
        files.update({folder+'/assessment.json':dumps(a),folder+'/lineage.json':dumps(lineage),folder+'/thesis.ko.md':thesis,folder+'/decision-history.md':history})
        pointer = copy.deepcopy(snapshot['company_latest'][ticker])
        pointer.update(assessment=folder+'/assessment.json',thesis=folder+'/thesis.ko.md',run=RUN,
            authority=f"Management weighting correction: score {a['total_score_100']}, management six; no trade authorization.")
        files[f'companies/{ticker}/latest.json'] = dumps(pointer)
    rows = copy.deepcopy(read(BASE+'/scoreboard.json'))
    for row in rows:
        ticker = row['ticker']
        if ticker in assessments:
            a = assessments[ticker];finding = audit['findings'][ticker]
            business = 'AI 가속컴퓨팅·CUDA·네트워크의 고객 가치와 주당현금이 핵심이다. ' if ticker=='NVDA' else 'OCS·장기이식 물류의 임상 가치와 반복사용이 투자 논리다. '
            row.update(score=a['total_score_100'],prior_canonical_score=finding['before_total'],
                business_quality_75=a['business_quality_75'],management_score=6,
                assessment=f'companies/{ticker}/analyses/{RUN}/assessment.json',
                source_assessment=finding['superseded_assessment'],business_and_thesis_ko=business+finding['reason_ko'])
        row['eligible'] = eligible(row['score'],row['management_score'],row['quote']['price'],row['base_value'],row['hard_veto'])
        row['exclusion_reasons'] = []
        if row['score']<70: row['exclusion_reasons'].append('총점<70')
        if row['management_score']<=5: row['exclusion_reasons'].append('경영진≤5')
        if row['quote']['price']>row['base_value']*1.15: row['exclusion_reasons'].append('현재가>Base×1.15')
        if row['hard_veto']=='FAIL': row['exclusion_reasons'].append('Hard Veto FAIL')
    selected = [r for r in rows if r['eligible']];allocation = weights(selected)
    for row in rows: row['weight_bp'] = allocation.get(row['ticker'],0)
    rows.sort(key=lambda r:(-r['score'],r['ticker']))
    portfolio = copy.deepcopy(read(BASE+'/portfolio.json'))
    portfolio.update(base_commit=snapshot['base_commit'],parent_review=BASE,
        correction_audit=DIRECTORY+'/audit.json',selected_count=len(selected),selected_score_sum=sum(r['score'] for r in selected),
        weight_sum_bp=sum(allocation.values()),positions=[r for r in rows if r['eligible']],excluded=[r for r in rows if not r['eligible']],
        price_and_model_basis={'policy':'UNCHANGED_FROM_PRECEDING_REVIEW_FOR_CONTROLLED_CORRECTION','prices':BASE+'/prices.json','models':BASE+'/model-specs.json'})
    files[DIRECTORY+'/portfolio.json'] = dumps(portfolio);files[DIRECTORY+'/scoreboard.json'] = dumps(rows)
    registry = copy.deepcopy(snapshot['registry'])
    for r in registry['companies']:
        if r['ticker'] in TICKERS:r['priority'] = 'P1'
    files['registry/companies.json'] = dumps(registry)
    latest = copy.deepcopy(snapshot['reviews_latest'])
    latest.update(directory=DIRECTORY,report=DIRECTORY+'/README.md',portfolio=DIRECTORY+'/portfolio.json',
        prior_review=BASE+'/README.md',input_manifest=DIRECTORY+'/input-manifest.json',review_manifest=DIRECTORY+'/manifest.json',
        completed_scope='43 canonical FULL_ANALYSIS remain current. NVDA and TMDX management weighting corrected after extended history audit; 13 conditional paper positions. No preliminary promotions or buy approvals.')
    files['reviews/latest.json'] = dumps(latest)
    return files,rows,assessments


def frozen_history_check():
    """Replay old numeric calculations; stabilize only unordered source arrays.

    The frozen financial renderer used unsorted Path.glob. A fresh checkout can
    enumerate identical raw files in a different order (observed for MSFT).
    Preserve the locked renderer and all numbers. Align only source_paths and
    sources arrays to their recorded order after proving identical membership.
    """
    baseline = read(BASE+'/authority-input.json')
    lock = read('harness/baseline-lock.json')
    reviewed = {r['ticker'] for r in read(BASE+'/model-specs.json')}
    superseded = {'registry/companies.json','reviews/latest.json'}|{f'companies/{t}/latest.json' for t in reviewed}
    with tempfile.TemporaryDirectory(prefix='ordered-historical-replay-') as td:
        dest = Path(td)/'repo'
        shutil.copytree(ROOT,dest,ignore=shutil.ignore_patterns('.git','__pycache__','.pytest_cache'))
        for p in (dest/'companies').glob('*/raw-data/*.json'):
            if str(p.relative_to(dest)) not in lock['raw_file_sha256']:p.unlink()
        (dest/'registry/companies.json').write_text(dumps(baseline['registry']))
        (dest/'skip-replay.json').write_text(dumps(sorted(superseded)))
        code = '''
import json
from pathlib import Path
from harness import deep_financials
from harness.core import read
original = deep_financials.financials
normalized = set()
def ordered_sources(ticker):
    result = original(ticker)
    expected = read(f'companies/{ticker}/analyses/2026-09-06-deep/financials.json')
    assert set(result['source_paths']) == set(expected['source_paths'])
    assert {e['path']: e['sha256'] for e in result['sources']} == {e['path']: e['sha256'] for e in expected['sources']}
    if result['source_paths'] != expected['source_paths']:normalized.add(ticker)
    by_path = {e['path']:e for e in result['sources']}
    result['source_paths'] = expected['source_paths']
    result['sources'] = [by_path[p] for p in expected['source_paths']]
    return result
deep_financials.financials = ordered_sources
from harness.build import outputs as initial
from harness.deep_report import outputs as deep
skip = set(json.loads(Path('skip-replay.json').read_text()))
counts = {}
for label,fn in [('initial',initial),('deep',deep)]:
    files,_ = fn();checked = 0
    for path,content in files.items():
        if path in skip:continue
        assert Path(path).read_text()==content,('FROZEN_NOT_REPRODUCIBLE',path)
        checked += 1
    counts[label] = checked
counts['source_reference_order_normalized'] = sorted(normalized)
counts['numeric_normalizations'] = 0
print(json.dumps(counts))
'''
        result = subprocess.run([sys.executable,'-c',code],cwd=dest,text=True,capture_output=True,timeout=180)
        assert result.returncode==0,result.stderr[-4000:]
        return json.loads(result.stdout)


def history_check():
    """Validate the previous review in a temporary copy of its live pointers."""
    snapshot = read(DIRECTORY+'/authority-input.json')
    with tempfile.TemporaryDirectory(prefix='management-correction-history-') as td:
        dest = Path(td)/'repo';shutil.copytree(ROOT,dest,ignore=shutil.ignore_patterns('.git','__pycache__','.pytest_cache'))
        restore = {'reviews/latest.json':snapshot['reviews_latest'],'registry/companies.json':snapshot['registry']}
        restore.update({f'companies/{t}/latest.json':snapshot['company_latest'][t] for t in TICKERS})
        for path,content in restore.items():(dest/path).write_text(dumps(content))
        code = '''
import json
from harness.review_validate import validate
from harness.management_correction import frozen_history_check
result = validate(replay=False)
result['frozen_replay'] = frozen_history_check()
print(json.dumps(result))
'''
        result = subprocess.run([sys.executable,'-c',code],cwd=dest,text=True,capture_output=True,timeout=180)
        assert result.returncode==0,result.stderr[-4000:]
        return json.loads(result.stdout)


def validate(replay=True):
    import jsonschema
    for e in read(DIRECTORY+'/input-manifest.json')['files']:
        assert sha(e['path'])==e['sha256'],('CORRECTION_INPUT_CHANGED',e['path'])
    files,rows,assessments = outputs()
    for path,content in files.items():assert (ROOT/path).read_text()==content,('CORRECTION_NOT_REPRODUCIBLE',path)
    for ticker,a in assessments.items():
        old = read(f'companies/{ticker}/analyses/2026-09-12-full-review/assessment.json')
        for k in old['categories']:
            if k!=MG:assert a['categories'][k]==old['categories'][k]
        for key in ['hard_veto','valuation','falsifiers','increase_evidence','sell_evidence','permanent_loss_case','red_team']:
            assert a[key]==old[key],('UNINTENDED_THESIS_CHANGE',ticker,key)
        assert a['total_score_100']==old['total_score_100']+1
    old_nvda = read('companies/NVDA/analyses/2026-09-12-full-review/assessment.json')
    assert assessments['NVDA']['categories'][MG]['counter_evidence']==old_nvda['categories'][MG]['counter_evidence']
    before_rows = {r['ticker']:r for r in read(BASE+'/scoreboard.json')}
    assert {r['ticker'] for r in rows}==set(before_rows) and len(rows)==43
    for row in rows:
        previous = before_rows[row['ticker']]
        for key in ['quote','base_value','bear_value','bull_value','max_eligible_price','valuation','hard_veto','open_vetoes']:
            assert row[key]==previous[key],('UNINTENDED_INPUT_CHANGE',row['ticker'],key)
        if row['ticker'] not in TICKERS:
            assert row['score']==previous['score'] and row['management_score']==previous['management_score']
        assert row['eligible']==eligible(row['score'],row['management_score'],row['quote']['price'],row['base_value'],row['hard_veto'])
    registry = read('registry/companies.json')['companies'];assert len(registry)==len({r['ticker'] for r in registry})==93
    schema = read('schemas/assessment-v2.schema.json')
    for r in registry:
        pointer = read(r['latest']);a = read(pointer['assessment'])
        assert r['ticker']==a['ticker'] and r['research_state']==a['research_state']==pointer['research_state']
        jsonschema.Draft202012Validator(schema).validate(a);validate_assessment(a);assert not a['buy_authorized']
    portfolio = read(DIRECTORY+'/portfolio.json');assert portfolio['rules']==read(BASE+'/portfolio.json')['rules']
    assert portfolio['selected_count']==13 and portfolio['selected_score_sum']==1007 and portfolio['weight_sum_bp']==10000
    assert all(next(r for r in rows if r['ticker']==t)['eligible'] for t in TICKERS)
    previous_result = history_check() if replay else None
    return {'status':'PASS','management_histories_audited':2,'restored_management_scores':{'NVDA':6,'TMDX':6},
        'company_totals':{'NVDA':79,'TMDX':74},'full_analysis':43,'selected':13,'selected_score_sum':1007,
        'weight_sum_bp':10000,'generated_artifacts':len(files),'unchanged_price_and_model_rows':43,
        'unchanged_nonmanagement_categories':14,'NVDA_additional_counter_evidence_preserved':True,
        'veto_changes':0,'buy_authorizations':0,'prior_review_validation':previous_result}


def main():
    parser = argparse.ArgumentParser();parser.add_argument('--write',action='store_true');parser.add_argument('--check',action='store_true');args = parser.parse_args()
    if args.check:print(dumps(validate()).strip());return
    files,rows,_ = outputs()
    if args.write:
        for path,content in files.items():
            dest = ROOT/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(content)
    print(dumps({'status':'WRITTEN' if args.write else 'READY','files':len(files),'selected':sum(r['eligible'] for r in rows)}).strip())


if __name__=='__main__':main()

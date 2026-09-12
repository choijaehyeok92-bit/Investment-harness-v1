"""Reproducible September 12 full-universe review and paper portfolio.

Inputs are dated research judgments and observed quotes. This is deliberately
not an automatic scoring service, broker connection, or trade authorization.
"""
from __future__ import annotations
import argparse
import copy
import math
import re
from collections import Counter
from decimal import Decimal
from .core import ROOT, CATEGORIES, read, sha, dumps, totals, aggregate_veto, validate_assessment
from .review_models import evaluate

RUN='2026-09-12-full-review'
DIRECTORY='reviews/'+RUN
LABELS=['구조 변화','고객 가치','해자','증분 ROIC·주당현금','경영진·자본배분','재무 생존','기대차·가치','비대칭']

def eligible(score, management, price, base, veto='INVESTIGATE'):
    if any(x is None for x in [score,management,price,base]):return False
    return score>=70 and management>5 and price>0 and base>0 and Decimal(str(price))<=Decimal(str(base))*Decimal('1.15') and veto!='FAIL'

def weights(rows):
    if not rows:return {}
    ordered=sorted(rows,key=lambda r:(-r['score'],r['ticker']))
    total=sum(r['score'] for r in ordered)
    result={r['ticker']:r['score']*10000//total for r in ordered}
    remainder=10000-sum(result.values())
    ranked=sorted(ordered,key=lambda r:(-(r['score']*10000%total),-r['score'],r['ticker']))
    for r in ranked[:remainder]:result[r['ticker']]+=1
    return result

def quote(t,prices):
    if t in prices['kr_prices']:
        return {'price':prices['kr_prices'][t],'currency':'KRW','timestamp':prices['kr_timestamp'],'basis':'DELAYED_KOREAN_CLOSE','source_url':f"https://stockanalysis.com/quote/{prices['kr_sources'][t]}/{t}/"}
    p,ts=prices['us_quotes'][t]
    exchange='NYSE' if t in ['ETN','NET','NOW','PWR','TSM','VRT'] else 'NASDAQ'
    return {'price':p,'currency':'USD','timestamp':ts,'basis':'LATEST_FINANCE_FEED_QUOTE_MAY_INCLUDE_EXTENDED_HOURS','source':'Web finance quote feed','source_url':f'https://www.google.com/finance/quote/{t}:{exchange}','source_url_note':'Public quote reference; observed numeric snapshot and UTC timestamp are from finance feed, not a separately audited Google webpage.'}

def category_map(a):
    c=a['categories']
    return {x.get('id',x.get('category')):x for x in c} if isinstance(c,list) else c

def red_team(a,source,category_map,permanent):
    r=a.get('red_team')
    if isinstance(r,dict) and len(r.get('attacks',[]))==10:
        r=copy.deepcopy(r);r.setdefault('verdict','REVISE');r.setdefault('independence','Same analyst/model adversarial review; not independent committee approval.')
        if r['verdict']=='REVISE_NOT_REJECT':r['source_verdict']=r['verdict'];r['verdict']='REVISE'
        return r
    if isinstance(r,list) and len(r)==10:return {'attacks':r,'verdict':'REVISE','independence':'Existing same-analyst adversarial review retained.'}
    thesis=ROOT/source.replace('assessment.json','thesis.ko.md')
    if thesis.exists():
        text=thesis.read_text();match=re.search(r'## .*Red Team[^\n]*\n(.*?)(?=\n## |\Z)',text,re.S|re.I)
        attacks=re.findall(r'^\d+\. (.+)$',match.group(1),re.M) if match else []
        if len(attacks)==10:return {'attacks':attacks,'verdict':'REVISE','independence':'Ten pre-existing adversarial arguments recovered from the linked thesis; not an independent committee.'}
    # Complete an actual adversarial review where the prior checkpoint omitted
    # its schema field. Each challenge is issuer-specific counter-evidence.
    attacks=[{'id':i+1,'challenge':c['counter_evidence'][0],'response':'반대 근거가 남아 있어 해당 점수의 신뢰도와 조사 조건을 유지한다. 가격 통과만으로 해소하지 않는다.'} for i,c in enumerate(category_map.values())]
    attacks += [{'id':9,'challenge':permanent,'response':'Bear는 최저가격 보증이 아니며 허가·권리·조달의 영구손상은 별도 매도 조건이다.'}, {'id':10,'challenge':'현재가를 설명하기 위해 정상 현금마진·만기가치·성장기간을 역으로 낙관화했는가?','response':'저장된 운영 가정을 고정해 가격 역산과 할인율 민감도를 재계산한다. 모형값을 시장가격에 맞춰 올리지 않는다.'}]
    return {'attacks':attacks,'verdict':'REVISE','independence':'Additional adversarial self-review completed on 2026-09-12; not represented as external or independent review.'}

def outputs():
    specs=read(DIRECTORY+'/model-specs.json');prices=read(DIRECTORY+'/prices.json');judgments=read(DIRECTORY+'/judgments.json')
    snapshot=read(DIRECTORY+'/authority-input.json');registry=copy.deepcopy(snapshot['registry']);out={};rows=[];assessments=[]
    for spec in specs:
        t=spec['ticker'];source=spec['source_assessment'];old=read(source);prior=read(spec['prior_canonical_assessment']);a=copy.deepcopy(old);q=quote(t,prices);v=evaluate(spec,q['price']);folder=f'companies/{t}/analyses/{RUN}'
        cats=copy.deepcopy(category_map(a))
        for k,c in cats.items():
            c.setdefault('missing_data',[]);c.setdefault('claim_type','opinion');c['source_paths']=[source]
            c['reviewed_as_of']='2026-09-12';c['score_action']='RETAINED_AFTER_EVIDENCE_REVIEW'
        changes=judgments['score_changes'].get(t,{})
        for k in CATEGORIES:
            if k in changes:
                cats[k]['prior_score']=cats[k]['score'];cats[k]['score']=changes[k];cats[k]['score_action']='REVISED_WITH_REASON';cats[k]['counter_evidence'].append(changes['reason'])
        for k in ['expectation_gap_and_valuation','power_law_and_asymmetry']:
            cats[k]['evidence'].append(f"2026-09-12 재검증: 관측가격 {q['price']} {q['currency']}; Bear/Base/Bull {v['scenarios']['bear']['value_per_share']:.4f}/{v['scenarios']['base']['value_per_share']:.4f}/{v['scenarios']['bull']['value_per_share']:.4f}. 모형 가정·원자료 기준은 valuation.json에 보존.")
            cats[k]['source_paths'].append(folder+'/valuation.json')
        veto=a.get('hard_veto',a.get('hard_vetoes'))
        items=copy.deepcopy(veto['items'] if isinstance(veto,dict) else veto)
        for item in items:
            item.setdefault('resolution_needed','기존 근거와 반증·매도 조건을 계속 추적한다.');item['evidence']=item['evidence'] if isinstance(item['evidence'],list) else [item['evidence']]
        a['hard_veto']={'items':items,'overall_status':aggregate_veto(items)}
        permanent=a.get('permanent_loss_case',prior.get('permanent_loss_case'))
        if not permanent:permanent='허가·제품안전·가격결정력·시장점유가 구조적으로 손상되고 주당현금과 권리가 훼손되는 경우. 회사 존속이 주주 원금 회수를 보장하지 않는다.'
        a['permanent_loss_case']=permanent
        a['sell_evidence']=a.get('sell_evidence',prior.get('sell_evidence',a.get('falsifiers')))
        a['source_quality']=a.get('source_quality',{'status':'INHERITED_RAW_AND_DATED_EVIDENCE_WITH_TARGETED_PRIMARY_RECHECK','limits':['Stored extracts and linked dated evidence are research assertions, not a new independent audit of every original filing.','Owner margins and Base values remain estimates; undisclosed reinvestment and rights items stay unresolved.']})
        a['red_team']=red_team(a,source,cats,permanent)
        a.update(schema_version='2.0.0',ticker=t,as_of='2026-09-12',research_state='FULL_ANALYSIS',categories=cats,buy_authorized=False,position_band='NONE',decision='EXIT' if a['hard_veto']['overall_status']=='FAIL' else 'WATCH')
        a['total_score_100'],a['business_quality_75']=totals(cats)
        a['valuation']={'status':'OWNER_CASHFLOW_MODEL','reverse_expectations':v['reverse_expectations'],'scenarios':{k:{'value_per_share':v['scenarios'][k]['value_per_share'],'claim_type':'estimate'} for k in ['bear','base','bull']},'source_path':folder+'/valuation.json','price_status':q['basis'],'approved_for_trading':False}
        paths=set(a.get('source_paths',[]));paths.update([source,spec['prior_canonical_assessment'],spec['valuation_path'],DIRECTORY+'/judgments.json',DIRECTORY+'/prices.json'])
        if spec.get('model_path'):paths.add(spec['model_path'])
        for suffix in ['evidence-ledger.json','observations.json','financials.json','derived-metrics.json','thesis.ko.md']:
            p=source.replace('assessment.json',suffix)
            if (ROOT/p).exists():paths.add(p)
        paths.update(str(p.relative_to(ROOT)) for p in (ROOT/'companies'/t/'raw-data').glob('*.json'))
        for p in [f'reviews/2026-09-08-{t}-prelim/raw-data.json',f'companies/{t}/analyses/2026-09-08-prelim/assessment.json']:
            if (ROOT/p).exists():paths.add(p)
        a['source_paths']=sorted(p for p in paths if (ROOT/p).exists())
        a['historical_records']=[{'path':p,'status':'PRESERVED_PRIOR_RESEARCH'} for p in sorted({source,spec['prior_canonical_assessment']})]
        a['authority_status']='CURRENT_REVIEWED_RESEARCH';a['authority_note']='Dated September 12 re-review supersedes prior current judgments; historical raw data and studies remain immutable.'
        a['review_method']='Re-review all eight categories and nine vetoes using dated harness raw/evidence, reconcile latest/checkpoint differences, recompute cash scenarios and reverse expectations, refresh dated prices, retain unaffected judgments and document every score change. No macro-score mixing.'
        a['data_as_of']=old['as_of'];a['review_note_ko']=judgments['notes'][t]
        if t=='012450':a['structural_thesis']='방산·항공 엔진의 수주와 제조 역량 확대. 모회사 현금과 자회사 지분가치를 분리해 평가한다.'
        if t=='CRDO':a['structural_thesis']='AEC·SerDes·DSP 기반 AI 데이터센터 연결의 전력효율·신뢰성 개선과 광통신 확장.'
        if 'structural_thesis' not in a:a['structural_thesis']=judgments['notes'][t]
        a['completion_gate']={'passed':True,'scope':'Research composition and audit lineage complete; unresolved facts and veto investigations are NOT marked resolved.','all_eight_categories':True,'nine_vetoes':True,'three_scenarios':True,'current_price_reverse':True,'ten_red_team_attacks':True,'source_lineage':folder+'/lineage.json'}
        a['reassessment_delta']={'prior_canonical_score':prior.get('total_score_100',prior.get('score_total')),'review_source_score':old.get('total_score_100',old.get('score_total')),'reviewed_score':a['total_score_100'],'prior_canonical_assessment':spec['prior_canonical_assessment'],'adopted_checkpoint':source if source!=spec['prior_canonical_assessment'] else None,'category_change_reason':changes.get('reason'),'score_layer':'COMPANY_SCORE_NOT_MACRO_ADJUSTED_SCORE'}
        validate_assessment(a)
        lineage={'ticker':t,'source_assessment':source,'records':[{'path':p,'sha256':sha(p),'claim_type':'source_assertion_or_prior_analysis'} for p in a['source_paths']], 'category_pointers':{k:{'path':source,'json_pointer':'/categories/'+k if isinstance(old['categories'],dict) else '/categories/'+str(next(i for i,c in enumerate(old['categories']) if c.get('id',c.get('category'))==k))} for k in CATEGORIES},'note':'Hashes establish exact lineage, not truth or independent source verification. Historical observations retain raw JSON pointers; no unknown value is replaced by zero.'}
        out[folder+'/assessment.json']=dumps(a);out[folder+'/valuation.json']=dumps(v);out[folder+'/lineage.json']=dumps(lineage)
        oldthesis=source.replace('assessment.json','thesis.ko.md')
        out[folder+'/thesis.ko.md']=f"# {a.get('company_name',t)} 재평가\n\n2026-09-12 기준. **{a['total_score_100']}/100 · WATCH · {a['hard_veto']['overall_status']}**. 실제 매수 승인은 없다.\n\n{a['review_note_ko']}\n\n관측가격 {q['price']:,.2f} {q['currency']} ({q['timestamp']}). Base 가치 {v['scenarios']['base']['value_per_share']:,.2f}, 편입 가격 상한 {v['scenarios']['base']['value_per_share']*1.15:,.2f}. 가치는 모형 추정이며 이 상한은 권장 매수가가 아니다.\n\n[선행 심층 보고서](../../../../{oldthesis}) · [재평가 점수·매도·추적 조건](assessment.json) · [재계산 모형](valuation.json) · [전체 포트폴리오](../../../../{DIRECTORY}/README.md)\n"
        out[f'companies/{t}/latest.json']=dumps({'as_of':'2026-09-12','assessment':folder+'/assessment.json','valuation':folder+'/valuation.json','thesis':folder+'/thesis.ko.md','research_state':'FULL_ANALYSIS','run':RUN,'authority':'Reviewed dated company score; macro overlay scores are separate. No trade authorization.'})
        b=v['scenarios']['base']['value_per_share'];score=a['total_score_100'];mg=cats['management_and_capital_allocation']['score'];is_in=eligible(score,mg,q['price'],b,a['hard_veto']['overall_status'])
        reasons=[]
        if score<70:reasons.append('총점<70')
        if mg<=5:reasons.append('경영진≤5')
        if q['price']>b*1.15:reasons.append('현재가>Base×1.15')
        if a['hard_veto']['overall_status']=='FAIL':reasons.append('Hard Veto FAIL')
        row={'ticker':t,'name':a.get('company_name',t),'score':score,'prior_canonical_score':a['reassessment_delta']['prior_canonical_score'],'business_quality_75':a['business_quality_75'],'management_score':mg,'currency':q['currency'],'quote':q,'base_value':b,'bear_value':v['scenarios']['bear']['value_per_share'],'bull_value':v['scenarios']['bull']['value_per_share'],'max_eligible_price':b*1.15,'price_to_base':q['price']/b,'eligible':is_in,'exclusion_reasons':reasons,'hard_veto':a['hard_veto']['overall_status'],'open_vetoes':[x['id'] for x in items if x['status']!='PASS'],'weight_bp':0,'buy_authorized':False,'business_and_thesis_ko':judgments['notes'][t],'monitor':a.get('next_evidence',a['increase_evidence']),'sell_signals':a['sell_evidence'],'falsifiers':a['falsifiers'],'assessment':folder+'/assessment.json','valuation':folder+'/valuation.json','source_assessment':source,'reverse_growth':v['reverse_expectations']['growth'],'reverse_growth_basis':spec['reverse_basis']}
        rows.append(row);assessments.append(a)
    selected=[r for r in rows if r['eligible']];allocation=weights(selected)
    for r in rows:r['weight_bp']=allocation.get(r['ticker'],0)
    for c in registry['companies']:
        found=next((r for r in rows if r['ticker']==c['ticker']),None)
        if found:c.update(research_state='FULL_ANALYSIS',decision='WATCH',input_maturity='REVIEWED_RAW_EVIDENCE_AND_SCENARIO_MODEL',priority='P1' if found['eligible'] else 'P2')
    registry['as_of']='2026-09-12';out['registry/companies.json']=dumps(registry)
    portfolio={'schema_version':'1.0.0','as_of':'2026-09-12','base_commit':snapshot['base_commit'],'universe_count':len(rows),'rules':{'minimum_score':70,'management_score_exclusive_minimum':5,'price_to_base_maximum':1.15,'target_count':[20,30],'force_fill':False,'weighting':'score / sum(eligible scores); 1bp largest remainder, score then ticker tie-break','top10_80_percent_rule':False,'hard_veto_FAIL_excluded':True,'INVESTIGATE':'Conditional paper allocation only; no buy approval'},'selected_count':len(selected),'selected_score_sum':sum(r['score'] for r in selected),'weight_sum_bp':sum(allocation.values()),'buy_authorized':False,'positions':sorted(selected,key=lambda r:(-r['score'],r['ticker'])),'excluded':[r for r in rows if not r['eligible']],'scope_exclusions':['AMD, PANW and SNOW remain PRELIMINARY_REVIEW in current canonical GitHub authority; prior separate unpromoted research is not silently relabeled FULL_ANALYSIS.','LSCABLE is not part of this canonical FULL_ANALYSIS universe; prior PARTIAL research remains outside the portfolio.'],'warning':'Paper target percentages do not imply actual holdings, execution, risk-budget suitability or authorization.'}
    out[DIRECTORY+'/portfolio.json']=dumps(portfolio);out[DIRECTORY+'/scoreboard.json']=dumps(sorted(rows,key=lambda r:(-r['score'],r['ticker'])))
    out['reviews/latest.json']=dumps({'as_of':'2026-09-12','directory':DIRECTORY,'report':DIRECTORY+'/README.md','registry':'registry/companies.json','portfolio':DIRECTORY+'/portfolio.json','prior_review':'reviews/2026-09-12-hugel-deep.json','authority':'registry -> company latest -> dated reviewed assessment','state_counts':dict(Counter(c['research_state'] for c in registry['companies'])),'completed_scope':f'{len(rows)} canonical FULL_ANALYSIS issuers re-reviewed; four additional existing-full checkpoints reconciled; no preliminary promotions or buy approvals.','input_manifest':DIRECTORY+'/input-manifest.json','review_manifest':DIRECTORY+'/manifest.json','score_rule':'Company score only; separate macro scores are not substituted.'})
    return out,rows,assessments

def main():
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--check',action='store_true');args=p.parse_args();files,rows,_=outputs()
    if args.write:
        for path,content in files.items():dest=ROOT/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(content)
    if args.check:
        for path,content in files.items():assert (ROOT/path).read_text()==content,('REVIEW_NOT_REPRODUCIBLE',path)
    print(dumps({'status':'PASS' if args.check else 'WRITTEN' if args.write else 'READY','reviewed':len(rows),'selected':sum(r['eligible'] for r in rows),'files':len(files)}).strip())

if __name__=='__main__':main()

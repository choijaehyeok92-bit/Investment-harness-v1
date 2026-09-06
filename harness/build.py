"""Deterministic read-only renderer. --emit emits desired files, never writes them.

Apply emitted contents through a reviewed patch. --check compares stored outputs.
The 2026-09-06 inputs are frozen, not a live-price or automatic trading service.
"""
from __future__ import annotations
import argparse
import copy
import json
from collections import Counter
from .core import ROOT, RUN, CATEGORIES, VETO_IDS, read, sha, observations, jsonl, dumps, totals, aggregate_veto
from .research import RAW, PRELIMINARY

DIRECTORY = 'reviews/2026-09-06-harness'
LOCK = 'harness/baseline-lock.json'
LABELS = ['구조 변화', '고객 가치', '해자 방향', '증분 ROIC·주당 현금', '경영진·자본배분', '재무 생존', '기대차·가치', '비대칭']
VETO_QUESTIONS = [
    '감사·내부통제·거래 및 경영진 진술 원문을 검증했는가?',
    '제한현금·확정 투자·만기를 반영한 외부조달 없는 생존 경로가 있는가?',
    'SBC 경제비용과 총발행·환매 재원을 분리해 희석을 검증했는가?',
    '매출·이익 증가가 독립적 고객 현금과 연결되는가?',
    '새 자본의 세후 현금수익이 자본비용을 넘는가?',
    '점유·유지·가격결정력이 성장과 별개로 강화되는가?',
    '가격·주식 수·현금 모델의 역산으로 현실적 Bull 범위를 시험했는가?',
    '고객·제품·지역·금융 노출이 복합 충격에도 치명적이지 않은가?',
    '사업 존속과 별개로 고가·희석·권리 손상의 영구손실을 평가했는가?',
]

LEGACY_REVIEW = {
'005930': '메모리 사이클·HBM 기술경쟁·파운드리 손실을 분리한 정상화 현금모델이 먼저다. 2026년 마진 급등만으로 첫 6개 품질 점수를 상향하지 않는다.',
'012450': '연결 전액 이익과 지분가치 합산의 중복, 비지배지분·보증·별도 현금 누락이 해결되지 않았다. 71/48 충돌을 새 숫자로 덮지 않고 총점과 해당 항목을 보류한다.',
'AVGO': '유통업체 42% 노출과 최종고객 42% 노출을 구별하는 규칙을 ANET에도 일관 적용한다. 세금 일회성·영업권 손상은 그 자체로 회계부정 또는 즉시 현금손실의 증거가 아니다.',
'AXON': '계약 총액·NRR은 고객가치의 근거지만 회계상 미래 매출과 현금 회수는 별개다. 같은 SBC를 현금 차감과 미래 희석으로 이중 계산한 과거 가격 범위는 최신 기준가격으로 승격하지 않는다.',
'DDOG': 'SBC 이후 현금과 보고 FCF의 차이가 핵심이다. 경제적 보상비용 처리와 기본/희석 주식 수를 일관되게 연결하기 전, 보고 현금마진을 매수 근거로 쓰지 않는다.',
'GOOGL': 'GOOG·GOOGL을 한 기업으로 통합하되 주식 종류 권리를 보존한다. 미국 9% 동일 허들에서 Capex·SBC·전환우선주를 반영하고 Bull에 낮은 할인율을 주어 비대칭을 만들지 않는다.',
'ISRG': '기업 품질과 임상·설치 기반은 상대적으로 강하다. 절차 증가·가격·반복 매출·SBC 이후 현금의 연결을 유지하되 무상 환매 효과를 제거한 안전마진이 아직 독립적으로 완성되지 않았다.',
'NET': 'SBC 이후 현금이 음수라는 점과 높은 시장 기대에 대한 기존 부정 판단을 유지한다. 낮은 자체 Bull만으로 가격 veto를 FAIL로 만들지 않으며 58점은 과거 점수로 보존한다.',
'NVDA': '고객 지원·공급·클라우드·보증을 같은 AI 투자 사이클에 연결된 스트레스로 평가한다. 서로 독립적인 확률로 곱하거나 명목 약정을 즉시 손실 전액으로 처리하지 않는다.',
'TSM': 'ADR 권리·통화·지리 집중과 해외 생산의 대체가능성을 분리한다. 미국 상장에 9% 비교 허들을 쓰더라도 대만 사건 위험이 소멸하지 않으며 자의적인 정밀 확률을 만들지 않는다.',
'NOW': '최신 NOW 72/100과 현금대체 SBC 모형을 우선 적용한다. Base 할인만으로 4개 INVESTIGATE를 통과시키지 않는다. 새 공시 없이 동일 점수를 재명명해 상향하지 않는다.',
}

def source_paths(ticker):
    paths = sorted(str(p.relative_to(ROOT)) for p in (ROOT/'companies'/ticker/'raw-data').glob('*.json'))
    if (ROOT/'companies'/ticker/'scorecard.json').exists():
        paths += sorted(str(p.relative_to(ROOT)) for p in (ROOT/'companies'/ticker).iterdir()
                        if p.is_file() and p.suffix in ['.json', '.jsonl', '.md', '.py'] and p.name != 'latest.json')
    return paths

def historic_refs(t):
    refs = []
    for file in ['company-reassessments.jsonl','screen-reassessments.jsonl','qualitative-reassessments.jsonl']:
        p = 'reviews/2026-09-05-astra/'+file
        for i, row in enumerate(jsonl(p), 1):
            if row['ticker'] == t: refs.append({'path': p, 'line': i, 'status': 'HISTORICAL_NOT_CURRENT_SCORE'})
    return refs

def raw_rows(t):
    return [r for p in source_paths(t) if '/raw-data/' in p for r in observations(p)]

def categories_blank(views, risk, missing, refs):
    return {k: {'score': None, 'max_score': n, 'claim_type': 'opinion',
                'evidence': [views[i]], 'counter_evidence': [risk[i] if isinstance(risk, list) else risk],
                'confidence': .45 if refs else .2, 'missing_data': [missing], 'source_paths': refs}
            for i,(k,n) in enumerate(CATEGORIES.items())}

def red_team(d):
    risks = [
        '사이클/선투자를 구조적 수요로 오인할 수 있다: '+d['structural_thesis'],
        '시장 확대가 주당 현금으로 귀속되지 않을 수 있다: '+d['economic_finding'],
        '매출 증가 자체는 해자 확대의 증명이 아니다: '+d['customer_and_moat'],
        '고객 편익의 독립 검증과 경쟁 대안의 총비용 자료가 부족할 수 있다.',
        '증분 ROIC는 이익률이 아니라 신규 투입자본 대비 세후 현금수익이다: '+d['next_evidence'],
        'SBC·환매·기존 미행사 보상·신주발행을 동일 비용 두 번 차감하거나 모두 누락할 수 있다.',
        '경영진의 인수·설비·환원 행동을 진술과 대조해야 한다: '+d['capital_and_survival'],
        '훌륭한 사업 가설을 시장도 이미 알고 있을 수 있다. 현재 가격 기대차이는 별도 입증 대상이다.',
        '정상화 owner 마진·지속기간·만기 가치와 현금 시점이 민감도 핵심이다. 미완성 모형은 목표가를 제시하지 않는다.',
        d['permanent_loss_case'],
    ]
    return {'attacks': [{'id': i+1, 'claim_type': 'inference', 'challenge': s} for i,s in enumerate(risks)],
            'strongest_bear_thesis': d['permanent_loss_case'],
            'three_hidden_assumptions': [d['customer_and_moat'], d['economic_finding'], d['capital_and_survival']],
            'underweighted_evidence': d['current_finding'], 'falsifiers': d['falsifiers'],
            'confidence': .55 if d['research_state'] != 'PRELIMINARY_REVIEW' else .25,
            'verdict': 'REJECT' if d['decision']=='REJECT' else 'REVISE',
            'independence': '단일 분석자의 적대적 재검토; 독립 검토자/멀티 에이전트 합의가 아님'}

def assessment(row):
    t = row['ticker']; refs = source_paths(t); has_legacy = (ROOT/'companies'/t/'scorecard.json').exists()
    d = {'schema_version': '2.0.0', 'ticker': t, 'company_name': row['company_name'], 'as_of': RUN,
         'listing_market': 'KR' if row['market']=='KR' else 'US', 'issuer_market_context': row['market'],
         'buy_authorized': False, 'position_band': 'NONE', 'decision': 'WATCH',
         'score_status': 'WITHHELD_WHERE_POLICY_GATE_OPEN', 'source_paths': refs,
         'historical_records': historic_refs(t), 'historical_score_100': None,
         'review_method': '저장 증거 재검토; 신규 원문 전체 재실사 아님',
         'portfolio_context': '실제 보유·세금·위험예산 미제공. 신규 매수 승인·자동 매매·기존 보유 강제 청산 아님.'}
    valuation = {'status': 'NOT_ESTABLISHED', 'reverse_expectations': None,
                 'scenarios': {k: None for k in ['bear','base','bull']},
                 'required_return': .10 if row['market']=='KR' else .09,
                 'price_status': 'NO_NEW_SYNCHRONIZED_QUOTE', 'missing_data': []}
    if t in RAW:
        thesis, moat, fact, economic, capital, falsifier, gap, model, priority = RAW[t]
        d.update(research_state='PARTIAL_ANALYSIS', input_maturity='RAW_DATA_ONLY_AT_BASELINE', priority=priority,
                 structural_thesis=thesis, customer_and_moat=moat, current_finding=fact,
                 economic_finding=economic, capital_and_survival=capital, next_evidence=gap,
                 permanent_loss_case=falsifier, falsifiers=[falsifier], increase_evidence=[gap, '보수적 주당 현금모델·가격 역산 및 9개 veto 해소'],
                 sell_evidence=[falsifier+'가 지속 확인될 때 논지 폐기 또는 보유 축소 검토'], historical_score_100=None)
        d['categories'] = categories_blank([thesis,moat,moat,economic,capital,capital,'가격에 내재된 성장·마진·기간을 아직 확정하지 않음',falsifier],
                                          [moat,gap,gap,economic,capital,capital,gap,falsifier],gap,refs)
        valuation.update(model_required=model, missing_data=[gap, '동일 시각 가격/주식 수 및 검증한 owner cash-flow 브리지'])
    elif has_legacy:
        old = read(f'companies/{t}/scorecard.json'); dec = read(f'companies/{t}/decision.json')
        past = next((x for x in jsonl('reviews/2026-09-05-astra/company-reassessments.jsonl') if x['ticker']==t), {})
        cats = copy.deepcopy(old['categories'])
        for c in cats.values():
            c.update(claim_type='opinion', source_paths=[f'companies/{t}/scorecard.json'])
            c.setdefault('missing_data', [])
        gap = past.get('next_evidence', ' / '.join(dec['increase_evidence']))
        # A historical number does not satisfy today's price/model completion gate.
        if t != 'NOW':
            for k in list(CATEGORIES)[6:]:
                cats[k].update(score=None, missing_data=sorted(set(cats[k]['missing_data']+[gap])), confidence=min(cats[k]['confidence'],.5))
        if t == '012450':
            for k in ['incremental_roic_and_fcf_per_share','financial_survivability']:
                cats[k].update(score=None, missing_data=[gap], confidence=.35)
        d.update(research_state='FULL_ANALYSIS' if t=='NOW' else 'PARTIAL_ANALYSIS',
                 input_maturity='LEGACY_FULL_PACKAGE', priority='P1' if t in ['NOW','ISRG'] else 'P2',
                 decision=dec['label'], categories=cats, historical_score_100=old['total_score'],
                 structural_thesis=cats[list(CATEGORIES)[0]]['evidence'][0],
                 customer_and_moat=cats[list(CATEGORIES)[2]]['evidence'][0],
                 current_finding=LEGACY_REVIEW[t], economic_finding=past.get('counter_evidence',dec['rationale']),
                 capital_and_survival=cats['financial_survivability']['counter_evidence'][0],
                 next_evidence=gap, permanent_loss_case=past.get('permanent_loss_case',dec['reduce_or_exit_evidence'][-1]),
                 falsifiers=dec['reduce_or_exit_evidence'], increase_evidence=dec['increase_evidence'],
                 sell_evidence=dec['reduce_or_exit_evidence'])
        valuation.update(status='OWNER_CASHFLOW_MODEL' if t=='NOW' else 'HISTORICAL_MODEL_NOT_PROMOTED',
                         source_path=f'companies/{t}/valuation.json', missing_data=[gap])
        if t=='NOW':
            v=read('companies/NOW/valuation.json')
            valuation.update(reverse_expectations=v['implied_expectations'],scenarios=v['scenarios'],
                             price_status='FROZEN_2026_09_04_REFERENCE_NOT_LIVE',model_required='AFTER_INTEREST_CASH_REPLACEMENT_SBC_FCFE')
        old_veto=read(f'companies/{t}/hard-veto.json')
        items=[]
        for v in old_veto['vetoes']:
            items.append({'id':v['id'],'status':v['status'],'evidence':v['evidence'],
                          'severity':v.get('severity','MEDIUM'),'confidence':v.get('confidence',.5),
                          'resolution_needed':v.get('resolution_needed'), 'basis':'REVIEWED_EXISTING_FILE_NOT_NEW_AUDIT'})
        d['hard_veto']={'items':items,'overall_status':aggregate_veto(items)}
    else:
        thesis,risk,gap=PRELIMINARY[t]
        d.update(research_state='PRELIMINARY_REVIEW',input_maturity='SCREEN_OR_LIST_ONLY',priority='P3',
                 structural_thesis=thesis,customer_and_moat=thesis+'가 전환비용·가격결정력으로 이어지는지는 미검증',
                 current_finding='투자 가설·반증 조건을 재정의했으나 신규 재무 원자료 패키지는 없다.',
                 economic_finding=gap+'를 확보하기 전 주당 현금복리 성장을 확정하지 않음',
                 capital_and_survival=risk+'를 반영한 유동성·만기 분석 미완료',next_evidence=gap,
                 permanent_loss_case=risk+'가 지속돼 주당 현금 또는 주주의 권리가 회복되지 않는 경우',
                 falsifiers=[risk+'가 실제 고객·현금 지표 악화와 함께 확인됨'],
                 increase_evidence=[gap, '최신 공시·감사·주식 수·reverse DCF 및 9개 veto 검증'],
                 sell_evidence=[risk+'가 지속 확인되면 논지 폐기 검토'])
        views=[thesis,d['customer_and_moat'],d['customer_and_moat'],d['economic_finding'],d['capital_and_survival'],d['capital_and_survival'],'시장 기대 미확정',d['permanent_loss_case']]
        d['categories']=categories_blank(views,risk,gap,[])
        valuation.update(model_required='ESTABLISH_FROM_PRIMARY_FILINGS',missing_data=[gap,'최신 재무·주식 수·가격·현금 모델'])
    if 'hard_veto' not in d:
        items=[{'id':k,'status':'INVESTIGATE','evidence':[question], 'resolution_needed':d['next_evidence'],
                'severity':'UNKNOWN','confidence':.25,
                'basis':'EVIDENCE_GATE_OPEN_NOT_ASSERTED_COMPANY_FAILURE'} for k,question in zip(VETO_IDS,VETO_QUESTIONS)]
        d['hard_veto']={'items':items,'overall_status':aggregate_veto(items)}
    d['valuation']=valuation
    d['total_score_100'],d['business_quality_75']=totals(d['categories'])
    d['source_quality']={'status':'STORED_ASSERTIONS_AND_INHERITED_RESEARCH',
        'primary_document_reaudit':'선별 공식 IR 교차검증만 수행. 모든 PDF·웹 원문을 새로 감사했다는 뜻이 아님.',
        'fact_estimate_inference_opinion':'원자료 숫자=보고 주장; 산식=계산치; 사업 연결=추론; 점수/판정=의견. 미래 전망은 사실 아님.',
        'missing_data_rule':'unknown을 0·PASS로 대체하지 않으며 자료 결손을 기업 실패로 단정하지 않음.'}
    d['red_team']=red_team(d)
    d['completion_gate']={'passed':d['research_state']=='FULL_ANALYSIS',
        'open_items':[] if d['research_state']=='FULL_ANALYSIS' else [d['next_evidence'],'시장 기대 역산·현금 브리지 및 Bear/Base/Bull','전 항목 점수 및 근거 검증'],
        'research_complete_is_not_investment_approval':True}
    return d

def thesis_md(d, rows):
    t=d['ticker']; lines=[f'# {d["company_name"]} ({t}) — 2026-09-06 재검토', '',
        f'판정: **{d["decision"]}** · 연구 상태: `{d["research_state"]}` · 매수 승인: 없음 · 후속 조사: {d["priority"]}', '',
        '> 이 문서는 저장된 증거 수준에 맞춘 현재 판정이다. 미완료 분석을 정밀실사 완료로 표시하지 않는다. P1/P2/P3는 조사 순서이며 투자 등급·포지션이 아니다.', '',
        '## 핵심 판단','',d['current_finding'],'',d['economic_finding'],'',
        '## 사업·고객·자본배분','',d['structural_thesis'],'',d['customer_and_moat'],'',d['capital_and_survival'],'',
        '## 100점 정책 항목','', '| 항목 | 현재 점수 | 판단 근거 | 반대 근거 / 미완료 |', '|---|---:|---|---|']
    for label,(key,c) in zip(LABELS,d['categories'].items()):
        esc=lambda s: str(s).replace('|','/').replace('\n',' ')
        lines.append(f'| {label} | {c["score"] if c["score"] is not None else "보류"}/{c["max_score"]} | {esc(c["evidence"][0])} | {esc(c["counter_evidence"][0])} |')
    lines += ['',f'현재 총점: {d["total_score_100"] if d["total_score_100"] is not None else "보류"}. 과거 총점: {d["historical_score_100"] if d["historical_score_100"] is not None else "해당 없음"}. 과거 50점 스크리닝은 100점으로 환산하지 않는다.', '',
        '## 하드베토·가치평가','',f'종합: {d["hard_veto"]["overall_status"]}. INVESTIGATE는 미확인 위험/증거 게이트이며 FAIL의 동의어가 아니다.', '',
        *[f'- {v["id"]}: {v["status"]}' for v in d['hard_veto']['items']], '',
        f'가치모델 상태: {d["valuation"]["status"]}. 비교 요구수익률: {d["valuation"]["required_return"]:.0%}.', '',
        '역산과 Bear/Base/Bull이 미완료면 목표가·매수가를 만들지 않는다. 이전 모형과 숫자는 historical_records 및 기존 valuation.json에 보존하되 현재 완료 상태와 구별한다.', '',
        '## 영구손실·반증·증액 조건','',d['permanent_loss_case'],'',
        *['- 반증/축소 조건: '+x for x in d['falsifiers']], '',
        *['- 증액 전 필요 증거: '+x for x in d['increase_evidence']], '',
        '## 레드팀 10개 공격','',*[f'{x["id"]}. {x["challenge"]}' for x in d['red_team']['attacks']], '',
        '## 출처와 다음 작업','',d['next_evidence'],'',
        f'정규화한 원자료 관측값 {len(rows)}개. 각 값의 JSON pointer·원파일 SHA256·공시 위치는 observations.json에서 확인한다. 이 해시는 파일 무변경을 증명하며 원문 정확성 인증은 아니다.', '',
        *[f'- `{x}`' for x in d['source_paths']], '',
        '기존 자료의 숫자를 재검토한 것으로 모든 원문 신규 재실사는 아니다. 계산은 derived-metrics.json의 입력 관측값·범위·산식으로 재현한다. 관측 단위나 기간이 불명확하면 변환·계산을 보류한다.', '']
    return '\n'.join(lines)

def outputs():
    universe=read('reviews/2026-09-05-astra/coverage.json')+read('harness/additional-universe.json')
    out={}; registry=[]; assessments=[]; sources={}; metrics=build_metrics()
    for row in universe:
        d=assessment(row);t=d['ticker']; rr=raw_rows(t); assessments.append(d)
        base=f'companies/{t}/analyses/{RUN}'
        out[f'{base}/assessment.json']=dumps(d)
        out[f'{base}/thesis.ko.md']=thesis_md(d,rr)
        out[f'{base}/observations.json']=dumps(rr)
        out[f'{base}/derived-metrics.json']=dumps(metrics.get(t,[]))
        latest={'as_of':RUN,'assessment':f'{base}/assessment.json','thesis':f'{base}/thesis.ko.md',
                'authority':'현재 판정은 이 버전. 루트의 이전 scorecard/decision/thesis는 감사 가능한 과거 기록.',
                'research_state':d['research_state']}
        out[f'companies/{t}/latest.json']=dumps(latest)
        registry.append({'ticker':t,'aliases':['GOOG'] if t=='GOOGL' else [],'company_name':d['company_name'],
                         'listing_market':d['listing_market'],'issuer_context':row['market'],
                         'raw_files':[x for x in d['source_paths'] if '/raw-data/' in x],
                         'latest':f'companies/{t}/latest.json','research_state':d['research_state'],
                         'input_maturity':d['input_maturity'],'decision':d['decision'],'priority':d['priority']})
        for p in d['source_paths']:
            sources[p]={'path':p,'sha256':sha(p),'kind':'raw_assertions' if '/raw-data/' in p else 'inherited_analysis',
                        'verified_primary_document':False}
    counts=dict(Counter(d['research_state'] for d in assessments))
    out['registry/companies.json']=dumps({'schema_version':'2.0.0','as_of':RUN,'companies':registry})
    out[f'{DIRECTORY}/source-manifest.json']=dumps(list(sources.values()))
    out[f'{DIRECTORY}/coverage.json']=dumps(registry)
    out[f'{DIRECTORY}/progress.json']=dumps({'as_of':RUN,'universe':len(registry),'state_counts':counts,
        'all_scope_reviewed':True,'all_full_analyses_complete':False,
        'remaining_full_analyses':len(registry)-counts.get('FULL_ANALYSIS',0),
        'no_new_buy_approvals':True,'baseline_lock':LOCK,
        'report':f'{DIRECTORY}/README.md'})
    out['reviews/latest.json']=dumps({'as_of':RUN,'directory':DIRECTORY,'report':f'{DIRECTORY}/README.md',
        'authority':f'registry/companies.json -> companies/<ticker>/latest.json is the single current decision authority for all {len(registry)} issuers. Earlier overlays and scores remain historical.',
        'registry':'registry/companies.json','prior_review':'reviews/2026-09-05-astra',
        'completed_scope':f'{len(registry)} evidence-level reviews, not {len(registry)} complete investment underwritings',
        'state_counts':counts,'score_rule':'Null is unknown. Neither zero nor a inherited 50/100 score.'})
    return out,assessments

def build_metrics():
    # Explicit matched consolidated periods; no quarter annualization or cash-scope guess.
    from .core import calculate
    specs={
      '042700':[('H1 매출 증가율','growth',302065115926,327439097571),('H1 영업이익 증가율','growth',138803055438,155940316473)],
      '214450':[('H1 영업이익 증가율','growth',123762004754,100611274981),('H1 OCF 증가율','growth',64258667155,74528735924)],
      '196170':[('H1 매출 증가율','growth',140492885685,102339078027),('H1 OCF 증가율','growth',37550826893,63983759046)],
      '278470':[('H1 매출 증가율','growth',1360888888861,593767620563),('H1 OCF 증가율','growth',86404149570,116067068380)],
      '267260':[('H1 OCF 증가율','growth',480269932949,456999366688),('H1 OCF-PPE 제한적 프록시','ocf_less_explicit_capex',480269932949,139882641673)],
      'ANET':[('H1 OCF 증가율','growth',2776.5,1841.8)],
      '005380':[('H1 영업이익 증가율','growth',5365574,7235206)],
    }
    result={}
    for t,items in specs.items():
        rows=raw_rows(t);rm={r['id']:r for r in rows};result[t]=[]
        for label,op,a,b in items:
            refs=[]
            for value in [a,b]:
                matches=[r for r in rows if r['value']==value and r['value_base_currency'] is not None
                         and r['json_pointer'].split('/')[1] in ['revenue','operating_income','operating_cash_flow','capex']]
                if len(matches)!=1: raise ValueError((t,label,value,'ambiguous',len(matches)))
                refs.append(matches[0]['id'])
            result[t].append(calculate({'label':label,'operation':op,'inputs':refs,
                 'accounting_scope':'consolidated, cash statement for OCF; no parent/finance/free-cash reinterpretation',
                 'comparability_note':'동일 연결 지표의 H1/H1 또는 Q2/Q2 비교. FY 분할·분기 연율화 아님. APR는 원자료의 재작성 비교열.',
                 'limitation':'산술 진단이며 증분 ROIC·내재가치·owner FCF 전체를 뜻하지 않음.'},rm))
    return result

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--emit',action='store_true');parser.add_argument('--check',action='store_true');parser.add_argument('--prefix',default='')
    args=parser.parse_args();files,ds=outputs()
    files={p:s for p,s in files.items() if p.startswith(args.prefix)}
    if args.emit: print(dumps(files))
    elif args.check:
        mismatch=[p for p,s in files.items() if not (ROOT/p).exists() or (ROOT/p).read_text()!=s]
        if mismatch: raise SystemExit('NONREPRODUCIBLE: '+', '.join(mismatch))
        print(f'REPRODUCIBLE: {len(files)} generated artifacts; {len(ds)} issuer reviews')
    else: print(dumps({'files':len(files),'states':dict(Counter(d['research_state'] for d in ds))}))

if __name__=='__main__': main()

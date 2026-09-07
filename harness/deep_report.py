"""Render the completed raw-based study without rewriting historical research."""
from __future__ import annotations
import argparse
import copy
from collections import Counter
from .core import ROOT,read,sha,dumps,CATEGORIES,VETO_IDS,totals,aggregate_veto,validate_assessment
from .deep_inputs import inputs,RUN,DIRECTORY
from .deep_model import model,scenario,scale
from .deep_financials import ledger,financials,EXTERNAL
from .build import LABELS


def special_tests(t,m):
    ticker=t['ticker'];base=m['scenarios']['base'];s=t['valuation_shares_m'];unit=scale(t)
    tests={'share_denominator_sensitivity':[{'share_change':x,'value_per_share':base['value_per_share']/(1+x)} for x in [-.05,0,.05,.10]],
           'model_basis':'Separate alternatives; do not stack all tests as if independent losses.'}
    if ticker in ['012450','034020']:
        additions=[-8,-4,0,4,8] if ticker=='034020' else [0,5,10,15,20]
        op=base['pv_interim_owner_cash']+base['pv_terminal']
        tests['parent_sotp_net_nonoperating_value']=[{'net_stake_less_parent_obligations_assumption':x,'value_per_share':max(0,op+x)*unit/s} for x in additions]
    if ticker=='196170':
        required=m['reverse_expectations'].get('implied_year_10_owner_cash')
        tests['royalty_diagnostic']={'net_cash_conversion_assumption':.60,'fx_krw_per_usd_assumption':1400,
          'note':'All terminal owner cash assumed royalty-driven for a transparent upper requirement. Rate is not a confidential contract fact; milestones excluded. Underlying licensed-product sales, not Alteogen reported sales.',
          'required_licensed_product_sales_usd_b':[{'royalty_rate_assumption':r,'product_sales':required/.60/r*1000/1400} for r in [.01,.02,.03]] if required is not None else []}
    if ticker=='ASTS':
        revenue=m['reverse_expectations'].get('implied_year_10_revenue')
        tests['satellite_subscriber_requirement']={'note':'Net monthly revenue retained by AST after MNO sharing; not consumer bill. No claim these subscriber counts or capacity are achievable.',
            'paying_users_m':[{'net_arpu_usd_month':a,'users_m':revenue*1000/(12*a)} for a in [2,5,10]] if revenue else []}
    if ticker=='042700':
        revenue=m['reverse_expectations'].get('implied_year_10_revenue')
        tests['equipment_volume_requirement']={'note':'Illustrative ASP1/2/3KRWb, all revenue treated as equipment. This is a capacity hurdle, not disclosed ASP/order forecast.',
            'annual_units':[{'asp_krw_b':a,'units':revenue*1000/a} for a in [1,2,3]] if revenue else []}
    if ticker in ['TSM','NVDA','000660']:
        tests['correlated_tail_risk']={'claim_type':'inference','principal_loss_stress':[.5,.8,1.0],
              'probability':None,'note':'Joint supply/customer/geography capital shock. Stress severity, not estimated likelihood; do not multiply assumed independent probabilities.'}
    if ticker in ['TEM','RKLB','VRTX','207940']:
        tests['unclosed_transaction']={'status':'CONDITIONAL','note':t['rights_and_capital'],
          'acquired_business_incremental_npv_test':[
              {'incremental_value_change_as_fraction_of_reference_equity':x,'value_per_share':max(0,base['value_per_share']+t['price']*x)} for x in [-.25,-.10,0,.10]],
          'interpretation':'Price paid, new debt and dilution must be offset by acquired cash value. Standalone and completion risks explicitly separate; no unclosed revenue asserted as fact.'}
    if ticker=='TEM':
        tests['personalis_consideration_stress']=[{'assumed_total_equity_consideration_usd_b':1.5,'cash_fraction':f,'cash_required_usd_b':1.5*f,
            'illustrative_new_shares_m':1.5*(1-f)*1000/t['price'],
            'note':'At current assumed issue price. Ignores collar/price changes; does not apply extra haircut to primary standalone PV.'} for f in [0,.25,.5]]
    if ticker=='035420':
        tests['conditional_nvidia_issue']={'new_shares_m':7.241564,'pro_forma_shares_m':s+7.241564,
             'same_business_value_per_share_before_new_project_npv':base['value_per_share']*s/(s+7.241564),
             'note':'New cash must fund the required project; neither zero-cost dilution nor full proceeds as excess cash. Requires independent project NPV.'}
    if ticker in ['GOOGL','214450','196170','TMDX']:
        tests['convertible_rights']={'method':'Primary denominator/claim treatment stated in model inputs. Alternate conversion removes the corresponding claim cost before adding conversion shares.',
            'note':t['rights_and_capital'],'contractual_conversion_count_unknown':ticker in ['GOOGL','214450'],
            'additional_share_stress_not_contract_fact':[.05,.10,.20]}
    return tests


def valuation_scores(t,m):
    """Transparent opinion rubric, never a buy signal or veto override."""
    b=m['scenarios']['base']['value_to_price'];u=m['scenarios']['bull']['value_to_price'];d=m['scenarios']['bear']['value_to_price']
    val=12 if b>=1.3 else 10 if b>=1.1 else 8 if b>=.95 else 6 if b>=.75 else 4 if b>=.5 else 2
    if t['model_family'] in ['parent_sotp','milestone_funding','royalty_contract']:val=max(1,val-2)
    upside=max(0,u-1);downside=max(.2,1-d);asym=7 if upside/downside>=2.5 else 6 if upside/downside>=1.8 else 5 if upside/downside>=1 else 3
    if m['scenarios']['base']['external_funding_gap']>0:asym=max(1,asym-2)
    return val,asym


def assessment(t,m):
    ticker=t['ticker'];old=read(f'companies/{ticker}/analyses/2026-09-06/assessment.json');d=copy.deepcopy(old)
    fin=financials(ticker);base=m['scenarios']['base'];bull=m['scenarios']['bull'];bear=m['scenarios']['bear']
    val,asym=valuation_scores(t,m);scores=t['quality_scores']+[val,asym]
    # Confidence follows source/economic uncertainty, not model numerical precision.
    confidence=.62
    if t['model_family'] in ['parent_sotp','milestone_funding','royalty_contract']:confidence=.45
    if ticker=='ISRG':confidence=.78
    if ticker in ['ANET','MSFT','DDOG','TSM']:confidence=.70
    if ticker=='042700':confidence=.45
    if ticker in ['214450','TMDX']:confidence=.55
    missing=[old['next_evidence'],'미래 owner 현금마진·재투자 회수·종료배수는 추정, 관측 사실 아님']
    ev=[old['structural_thesis'],old['customer_and_moat'],old['customer_and_moat'],t['financial_finding'],t['rights_and_capital'],t.get('liquidity_note',t['rights_and_capital']),
        f"기준가 {t['price']:,.2f}; Base/가격 {base['value_to_price']:.2f}배. 고정된 Base 현금경제 하에서 2~10년 요구 성장률 {m['reverse_expectations']['required_growth_years_2_10']:.1%}.",
        f"Bear/가격 {bear['value_to_price']:.2f}배, Bull/가격 {bull['value_to_price']:.2f}배. 2상태 손익분기 Bull 확률 {m['break_even_bull_probability_in_two_outcome_pv_test']:.1%}; 실제 확률 추정 아님."]
    co=[t['economic_risk'],t['falsifier'],t['economic_risk'],
        '실제 증분 ROIC를 계산할 경제적 투자자본 코호트는 unknown. '+t['economic_risk'],t['economic_risk'],
        f"Base 음수 현금 합계 {base['gross_negative_cash']:.3f} {t['unit']}, 가용현금 차감 후 조달 부족 {base['external_funding_gap']:.3f}. "+t['economic_risk'],
        '가정·초기 매출·종료가치·권리 오차에 민감하며 계산한 Bull 초과 가격만으로 불가능성을 단정하지 않는다.',t['falsifier']]
    categories={}
    for i,(key,max_score) in enumerate(CATEGORIES.items()):
        categories[key]={'score':scores[i],'max_score':max_score,'claim_type':'opinion','evidence':[ev[i]],'counter_evidence':[co[i]],
            'confidence':min(confidence,.55) if i>=6 else confidence,'missing_data':missing if i in [3,6,7] else [],
            'source_paths':[f'companies/{ticker}/analyses/{RUN}/evidence-ledger.json',f'companies/{ticker}/analyses/{RUN}/model-inputs.json']}
    d['categories']=categories;d['total_score_100'],d['business_quality_75']=totals(categories)
    veto=[]
    for i,vid in enumerate(VETO_IDS):
        status='INVESTIGATE' if i in t['investigate_veto_indices'] else 'PASS'
        # PASS means no threshold-crossing evidence found, not audited absence.
        evidence=co[[4,5,4,1,3,2,6,2,7][i]]
        if i==6 and bull['value_to_price']<1:status='INVESTIGATE'
        if i==1 and base['external_funding_gap']>0:status='INVESTIGATE'
        veto.append({'id':vid,'status':status,'evidence':[evidence],
            'resolution_needed':missing[0] if status=='INVESTIGATE' else '공시 변화·반증 발생 시 즉시 재평가',
            'severity':'MATERIAL' if status=='INVESTIGATE' else 'NO_TRIGGER_FOUND','confidence':confidence,
            'basis':'Analyst threshold assessment from disclosed evidence; unknown is not misconduct/failure.'})
    d['hard_veto']={'overall_status':aggregate_veto(veto),'items':veto}
    d['decision']='REJECT' if d['total_score_100']<65 else 'WATCH'
    d.update(research_state='FULL_ANALYSIS',buy_authorized=False,position_band='NONE',score_status='ALL_EIGHT_CATEGORIES_REVIEWED_WITH_EXPLICIT_UNCERTAINTY',
             review_method='34개 부분분석의 원자료·기존 증거 기반 정규화, 선택 공시 교차검증, 종목별 현금 시나리오·반증 재평가. 독립 감사 또는 확정 목표가 아님.',
             current_finding=t['financial_finding'],economic_finding=t['economic_risk'],capital_and_survival=t['rights_and_capital'],
             source_quality={'status':'RAW_BASED_COMPLETE_RESEARCH_WITH_OPEN_INVESTMENT_GATES','confidence':confidence,
               'historical_data':'원자료 해시·위치 유지; 중요한 현금·권리 항목을 선택 검증. 과거 분석의 주장도 원문 재감사 여부와 구분.',
               'fact_estimate_inference_opinion':'financials/evidence=보고 주장 또는 명시 계산; model-inputs=추정; 사업 인과·반증=추론; 점수·판정=의견.',
               'price':'9월4일 참조가격, 공시 주식 시점과 다름. 모든 가격이 동시각 거래소 종가라는 뜻 아님.',
               'limits':missing,'share_basis':t['share_basis_status'],'liquidity_basis':t['liquidity_basis_status']})
    d['valuation']={'status':'OWNER_CASHFLOW_SCENARIOS_WITH_UNRESOLVED_UNDERWRITING','required_return':t['required_return'],
        'reverse_expectations':m['reverse_expectations'],'scenarios':m['scenarios'],
        'source_path':f'companies/{ticker}/analyses/{RUN}/valuation.json','price_status':t['price_status'],
        'model_family':t['model_family'],'missing_data':missing,'approved_for_trading':False}
    d['permanent_loss_case']=t['falsifier']+' 가격에 이미 긴 성장기간이 반영되면 사업 존속에도 원금 회복이 장기간 불가능할 수 있다.'
    d['falsifiers']=[t['falsifier']]
    d['increase_evidence']=[old['next_evidence'],
        'SBC·전체 Capex·운전자본·확정 권리/부채 이후 주당 현금이 최소 두 보고기간 개선되고 가격 역산 요구가 보수적 성장 범위 이내일 것.',
        'INVESTIGATE 항목의 해당 공시 근거 해소와 포트폴리오 위험예산 검토 후에만 증액 검토. 가격 하락만으로 증액하지 않는다.']
    d['sell_evidence']=[t['falsifier'],'통제·현금·권리의 중대한 훼손이 확인되면 가격과 무관하게 논지 재작성 및 보유 시 축소/청산 검토. 현재 보유상태 미제공.']
    attacks=[
      ('구조 변화',old['structural_thesis'],t['economic_risk']),
      ('고객 경제',old['customer_and_moat'],t['falsifier']),
      ('해자와 경쟁','성장이 장기 초과이익으로 귀속된다는 가정',t['economic_risk']),
      ('현금과 회계',t['financial_finding'],'보고 OCF·조정 FCF·SBC 이후 현금의 범위를 구분. financials.json의 null을 0으로 대체하지 않았다.'),
      ('증분 자본수익','모델의 성숙 cash margin이 투자 확대 이후에도 유지된다는 가정','경제적 투자자본 분모가 없어 ROIC 수치 주장 보류. 현금마진 ±3%p 민감도와 초기 음수 경로 공개.'),
      ('보상·권리',t['rights_and_capital'],'SBC 비용 후 현금과 미래 동일 보상 희석 이중 차감 제거. 기존 권리와 자금조달 주식은 별도 민감도.'),
      ('생존·조달',f"Base 신규조달 부족 {base['external_funding_gap']:.3f}{t['unit']}",'자금 부족이 없는 계산은 확정 약정 전부 충당의 보증이 아니다. 별도 인수·규제·조달 악화 스트레스 확인.'),
      ('시장 기대',ev[6],'역산은 성장·마진·기간의 조건부 조합이다. 한 조합이 실제 시장 컨센서스라는 뜻이 아니다.'),
      ('종료가치',f"Base 종료가치 비중 {base['terminal_fraction_of_operating_pv']:.1%}",'종료 배수±5배 및 허들±2%p를 공개. 종료가치 의존이 높을수록 신뢰도를 낮춘다.'),
      ('영구손실',d['permanent_loss_case'],'정밀한 실패확률은 unknown. 손익분기 확률과 투자 불가 조건을 제시하고 기대값 우위를 주장하지 않는다.')]
    d['red_team']={'attacks':[{'id':i+1,'topic':a,'challenge':b,'response':c,'claim_type':'inference'} for i,(a,b,c) in enumerate(attacks)],
        'strongest_bear_thesis':d['permanent_loss_case'],'three_hidden_assumptions':[t['economic_risk'],t['rights_and_capital'],'지속기간·경쟁·종료배수'],
        'underweighted_evidence':t['financial_finding'],'falsifiers':d['falsifiers'],'confidence':confidence,
        'verdict':'REJECT' if d['decision']=='REJECT' else 'REVISE' if d['hard_veto']['overall_status']=='INVESTIGATE' else 'PASS',
        'independence':'동일 분석자의 적대적 재검토; 독립 검토자·다중 에이전트 합의 아님'}
    d['completion_gate']={'passed':True,'definition':'원자료 기반 연구 구성 완료: 8점수·반대근거·역산·3시나리오·9veto·10공격·반증·증감 조건·출처. 필수 투자 승인 게이트의 통과와 구분.',
        'open_items':[],'investment_gates_open':[v['id'] for v in veto if v['status']!='PASS'],
        'explicit_model_uncertainties':missing,'research_complete_is_not_investment_approval':True}
    d['historical_records'].append({'path':f'companies/{ticker}/analyses/2026-09-06/assessment.json','status':'PREVIOUS_PARTIAL_ANALYSIS'})
    d['source_paths']=sorted(set(d['source_paths']+[f'companies/{ticker}/analyses/{RUN}/evidence-ledger.json',f'companies/{ticker}/analyses/{RUN}/model-inputs.json']))
    validate_assessment(d)
    return d


def fmt(x,dec=3):return 'unknown' if x is None else f'{x:,.{dec}f}'


def thesis(t,d,m,fin,special):
    ticker=t['ticker'];out=[];a=out.append
    a(f"# {d['company_name']} ({ticker}) — 원자료 기반 정밀 분석\n")
    a(f"2026-09-06 | **{d['decision']} · {d['total_score_100']}/100 · 기업 품질 {d['business_quality_75']}/75 · Hard Veto {d['hard_veto']['overall_status']}**\n")
    a('연구 구성은 완료했다. 아래 가격은 명시 가정에 따른 현금가치 범위이며 확정 목표가·매수 승인이 아니다. 중요 미확인 사항은 veto와 신뢰도에 남겨 두었다.\n')
    a('## 0. 분석 전략\n')
    a('저장된 원자료의 단위·기간·연결 범위를 확인 → 주당 현금·권리 정규화 → 시장 기대 역산 → Bear/Base/Bull → 하드베토·반증 → 판정 순으로 평가했다. 보고 주장, 계산치, 미래 추정, 의견을 구분한다.\n')
    a('## 1. 기본 정보와 기준 시점\n')
    a(f"참조가격 **{t['price']:,.2f} {t['currency']}**(9월4일), 가치평가 분모 **{t['valuation_shares_m']:,.6f}백만주**. {t['share_basis_status']}. 날짜가 다른 주가와 공시 분모를 연결한 참조치이며 실시간 시총이 아니다. 금액 표 단위는 {t['unit']}.\n")
    a(t['rights_and_capital']+'\n')
    a('## 2. 기업·산업·해자\n')
    a('**구조적 가설:** '+d['structural_thesis']+'\n')
    a('**고객 가치와 경쟁:** '+d['customer_and_moat']+'\n')
    a('**반대 증거:** '+t['economic_risk']+'\n')
    a('## 3. 재무와 주당 현금\n')
    a('**보고 주장 및 계산:** '+t['financial_finding']+'\n')
    a(f"| {fin['period']} | 금액/비율 |\n|---|---:|")
    for k,label in [('revenue','매출'),('operating_profit','영업손익'),('ocf','영업현금'),('cash_capex','명시 현금투자'),('sbc','SBC'),('additional_cash_investment','추가 투자·원금'),('ocf_less_named_capex','OCF−명시 투자 소계'),('ocf_less_capex_sbc_known_subtotal','OCF−투자−SBC 알려진 비용 소계'),('owner_cash_proxy','추가 명시비용 차감 owner proxy')]:a(f'| {label} | {fmt(fin.get(k))} |')
    a('\n누락 현금·SBC·투자 항목을 0으로 간주하지 않았다. 위 소계는 전체 주주 현금의 확정치가 아니다. 실제 증분 ROIC는 경제적 투자자본 코호트가 부족해 수치 산출을 보류한다. 이익률을 ROIC로 바꾸지 않았다.\n')
    a('**미래 현금마진의 경제적 연결(모두 추정):**\n')
    b=t['base_mature_cash_bridge'];a('| Base 성숙기 가정 | 매출 대비 |\n|---|---:|')
    for k,label in [('economic_operating_margin_after_sbc','SBC 포함 경제적 영업마진'),('cash_tax_rate','세율(영업이익 대비)'),('da_less_all_capex_to_revenue','D&A−전체 재투자'),('working_capital_cash_cost_to_revenue','운전자본·신용자본 비용'),('interest_net_debt_service_other_claims_to_revenue','이자·순원금·기타 현금 비용')]:a(f"| {label} | {b[k]:.2%} |")
    a('\n영업마진×(1−세율)+(D&A−전체 재투자)−운전자본−금융 현금비용. 신규 보상은 비용에 포함하며 같은 보상의 미래 희석을 다시 차감하지 않는다. 기존 전환권리·확정 부채·M&A는 별도 분석한다.\n')
    a(t.get('segment_assumption_note','연결 매출과 전체 주주 현금의 관계를 사용한다. 자회사 전액 가치·고객 예치금을 추가 가산하지 않는다.')+'\n')
    a(f"**자금조달:** 인정 유동성 {t['liquidity_cash']:.3f}, 최소 유보 {t['minimum_cash_reserve']:.3f}(유보는 추정). Base 음수 현금 합계 {m['scenarios']['base']['gross_negative_cash']:.3f}, 유보 후 현금 초과 조달 부족 {m['scenarios']['base']['external_funding_gap']:.3f}. {t['liquidity_basis_status']}.\n")
    a('## 4. 시장 기대와 가치평가\n')
    r=m['reverse_expectations'];a(f"**먼저 역산:** Base의 첫 12개월 매출·현금경제·종료배수를 고정하면 이후 9년 요구 성장률은 **{r['required_growth_years_2_10']:.1%}**, 10년차 요구 매출은 **{fmt(r.get('implied_year_10_revenue'))}**다. 이는 시장의 유일한 기대 추정이 아니라 가격을 정당화하는 조건부 조합이다. 위성 모델은 공개한 매출 경로에 성장 스트레스를 가한 값이다.\n")
    a(f"동일 요구수익률 **{t['required_return']:.0%}**, 10년 현금과 종료가치. 할인율은 Bull에 유리하게 낮추지 않았다. 거시 전망은 기업 점수에 직접 가산하지 않았다.\n")
    a('| 시나리오 | 주당 현재가치 | 기준가 대비 | 10년차 매출 | 10년차 owner 현금 | 종료배수 | 연간현금 포함 IRR |\n|---|---:|---:|---:|---:|---:|---:|')
    for k,s in m['scenarios'].items():
        irr=', '.join(f'{v:.1%}' for v in s['irr_roots']) or '해 없음/미확정'
        a(f"| {k.title()} | {s['value_per_share']:,.2f} | {s['upside_downside']:+.1%} | {s['year_10_revenue']:,.3f} | {s['year_10_owner_cash']:,.3f} | {s['terminal_multiple']}x | {irr} |")
    a('\nIRR은 배당·분배가능 현금과 종료가치의 계산치다. 음수 현금은 주주의 추가 자금 부담 등가로 반영했으므로 회사의 실제 배당 정책이나 확약 수익률이 아니다. 별도 지분 표식은 시점0 가치 등가다. 차입·인수의 실제 집행은 달라질 수 있다.\n')
    a('**사업 경로별 추정 가정:**\n')
    a('| 부문 | 경우 | 첫 12개월 매출 | 2~5년 성장 | 6~10년 성장 | 초기→성숙 현금마진 |\n|---|---|---:|---:|---:|---:|')
    for c in t['components']:
        for k,s in c['scenarios'].items():a(f"| {c['name']} | {k} | {s['revenue_year_1']:,.3f} | {s['growth_2_5']:.1%} | {s['growth_6_10']:.1%} | {s['owner_margin_year_1']:.1%}→{s['owner_margin_mature']:.1%} |")
    if t['model_family']=='memory_cycle':a('\n추가로 2년차 매출에 Bear65% / Base80% / Bull95% 재설정 배수를 적용했다. 고점 매출과 마진을 영구 연장하지 않는다.\n')
    if ticker=='ASTS':a('\n위성은 위 표 단순 CAGR 대신 model-inputs.json의 10년 절대 매출·현금 경로가 우선한다. 발사·주파수·교체투자를 포함한 초기 적자를 삭제하지 않았다.\n')
    if 'sotp_note' in t:a('\n'+t['sotp_note']+'\n')
    a('**민감도(기준 시나리오 주당가치):**\n')
    a('| 할인율 | 현금마진 −3%p | 기준 | +3%p |\n|---|---:|---:|---:|')
    for i in range(0,9,3):
        row=m['sensitivity'][i:i+3];a(f"| {row[0]['discount_rate']:.0%} | {row[0]['value_per_share']:,.2f} | {row[1]['value_per_share']:,.2f} | {row[2]['value_per_share']:,.2f} |")
    a(f"\nBase 종료가치 의존도 {m['scenarios']['base']['terminal_fraction_of_operating_pv']:.1%}. 장기 성장·마진의 작은 변경이 결론을 바꿀 수 있다. Bear/Bull 2상태 손익분기 Bull 확률은 {m['break_even_bull_probability_in_two_outcome_pv_test']:.1%}로, 실제 확률을 추정한 수치가 아니다.\n")
    if len(special)>2:a('종목 특수 스트레스(권리·조달·전환·SOTP·로열티/가입자 요구량)는 [특수조건 분석](special-tests.json)에 산식과 가정을 저장했다. 서로 독립인 손실처럼 모두 합산하지 않는다.\n')
    a('## 5. 경영진·자본배분·하드베토\n')
    a(t['rights_and_capital']+'\n')
    a('| 하드베토 | 판정 | 확인 근거/한계 |\n|---|---|---|')
    for v in d['hard_veto']['items']:a(f"| {v['id']} | {v['status']} | {v['evidence'][0].replace('|','/')} |")
    a('\nINVESTIGATE는 확인된 회사 실패가 아니다. PASS도 독립 감사 보증이 아니라 현재 근거에서 발동 조건을 찾지 못했다는 의미다. 본 모델 Bull보다 주가가 높다는 이유만으로 비현실적 가격 veto를 FAIL로 만들지 않는다.\n')
    a('## 6. 최종 판정·SWOT·신뢰도\n')
    a('| 항목 | 점수 | 신뢰도 | 근거 | 반대 근거 |\n|---|---:|---:|---|---|')
    for label,(k,c) in zip(LABELS,d['categories'].items()):a(f"| {label} | {c['score']}/{c['max_score']} | {c['confidence']:.0%} | {c['evidence'][0].replace('|','/')} | {c['counter_evidence'][0].replace('|','/')} |")
    a(f"\n**결론: {d['decision']}, {d['total_score_100']}/100.** 점수는 분석 의견이며 관측값이 아니다. 현재 신규 매수 승인과 포지션 배정은 없다. 연구 구성 완료와 투자 가능성 확인은 구분한다.\n")
    a('| SWOT | 요지 |\n|---|---|')
    for label,txt in [('강점',d['customer_and_moat']),('약점',t['economic_risk']),('기회',d['structural_thesis']),('위협',t['falsifier'])]:a(f'| {label} | {txt.replace("|","/")} |')
    a('\n**영구손실·논지 반증:** '+d['permanent_loss_case']+'\n')
    a('**증액 전 필요한 증거:** '+' '.join(d['increase_evidence'])+'\n')
    a('**매도·축소 증거:** '+' '.join(d['sell_evidence'])+'\n')
    a('**적대적 검토 10개:**\n')
    for x in d['red_team']['attacks']:a(f"{x['id']}. **{x['topic']}** — {x['challenge']} / 대응: {x['response']}")
    a('\n**출처와 신뢰도:** 원자료 해시·정확한 JSON 위치는 [관측값](observations.json), 보고 기간·현금 연결은 [재무](financials.json), 선택 공시 대조는 [증거](evidence-ledger.json), 계산은 [모형](valuation.json)에 있다. 모든 원문·계약의 독립 재감사는 아니다.\n')
    if ticker in EXTERNAL:a(f"추가 확인: [공시 또는 참조 시세]({EXTERNAL[ticker]['url']}) — {EXTERNAL[ticker]['location']}.\n")
    a('**추후 관측이 필요한 사항:** '+d['next_evidence']+' 미래 계약 성과와 투자회수율의 미확정성은 보고서 작성으로 사라지지 않는다.\n')
    return '\n'.join(out)+'\n'


def outputs():
    files={};ds=[];summary=[]
    universe=read('registry/companies.json')
    for t,x in inputs().items():
        m=model(x);sp=special_tests(x,m);d=assessment(x,m);fin=financials(t)
        base=f'companies/{t}/analyses/{RUN}'
        obs=read(f'companies/{t}/analyses/2026-09-06/observations.json')
        derived=read(f'companies/{t}/analyses/2026-09-06/derived-metrics.json')
        values={'assessment.json':d,'model-inputs.json':x,'valuation.json':{**m,'special_tests':sp},
            'financials.json':fin,'special-tests.json':sp,'evidence-ledger.json':ledger(t,obs),'observations.json':obs,'derived-metrics.json':derived,
            'price-and-shares.json':{k:x[k] for k in ['ticker','price','currency','price_date','price_status','price_source_note','valuation_shares_m','share_basis_status','rights_and_capital']}}
        for name,value in values.items():files[base+'/'+name]=dumps(value)
        files[base+'/thesis.ko.md']=thesis(x,d,m,fin,sp)
        latest=read(f'companies/{t}/latest.json');latest.update(assessment=base+'/assessment.json',thesis=base+'/thesis.ko.md',research_state=d['research_state'],run=RUN)
        files[f'companies/{t}/latest.json']=dumps(latest)
        row=next(r for r in universe['companies'] if r['ticker']==t);row['research_state']=d['research_state']
        # Registry fields only if present: keep schema/meaning consistent.
        for key in ['decision','total_score_100','business_quality_75','buy_authorized']:
            if key in row:row[key]=d[key]
        if 'assessment' in row:row['assessment']=base+'/assessment.json'
        if 'hard_veto' in row:row['hard_veto']=d['hard_veto']['overall_status']
        ds.append(d)
        summary.append({'ticker':t,'company_name':d['company_name'],'score':d['total_score_100'],'quality_75':d['business_quality_75'],
            'decision':d['decision'],'hard_veto':d['hard_veto']['overall_status'],'price':x['price'],'currency':x['currency'],
            'bear_value':m['scenarios']['bear']['value_per_share'],'base_value':m['scenarios']['base']['value_per_share'],'bull_value':m['scenarios']['bull']['value_per_share'],
            'base_value_to_price':m['scenarios']['base']['value_to_price'],'required_growth_2_10':m['reverse_expectations']['required_growth_years_2_10'],
            'confidence':d['source_quality']['confidence'],'buy_authorized':False,'report':base+'/thesis.ko.md'})
    files['registry/companies.json']=dumps(universe)
    counts=dict(Counter(r['research_state'] for r in universe['companies']))
    files['reviews/latest.json']=dumps({'as_of':'2026-09-06','directory':DIRECTORY,'report':DIRECTORY+'/README.md','registry':'registry/companies.json',
        'prior_review':'reviews/2026-09-06-harness','authority':'registry -> company latest -> dated assessment',
        'completed_scope':'34 prior partial raw-based studies completed with conditional scenario models; 58 preliminary remain unchanged; no buy approvals.',
        'state_counts':counts,'score_rule':'Unknown facts stay null. Analyst forecasts and opinion scores labeled explicitly.'})
    files[DIRECTORY+'/coverage.json']=dumps(summary)
    files[DIRECTORY+'/progress.json']=dumps({'scope':34,'completed':34,'prior_partial_remaining':0,'state_counts':counts,'decision_counts':dict(Counter(d['decision'] for d in ds)),
        'buy_authorizations':0,'definition':'Research composition complete; underwriting vetoes and uncertain facts persist explicitly.'})
    report=['# 부분분석 34종목 — 원자료 기반 정밀 분석 완료\n','2026-09-06 기준. 이전 부분분석 34개에 재무 정규화·주당 권리·시장 역산·3시나리오·8개 점수·9개 veto·10개 반대 논거를 작성했다. **연구 완료는 매수 승인과 다르다.** 원자료 미확인값과 미래 추정은 그대로 명시했다.\n',
       '전체93개 중 FULL_ANALYSIS35개(기존 NOW1+이번34), PRELIMINARY_REVIEW58개. 이번 범위 밖58개와 NOW의 분석 내용은 변경하지 않았다.\n',
       '## 주요 발견\n',
       '- 주식 종류·권리를 통일했다: TSM 5:1 ADS, ASTS 교환가능 LLC 지분, 한국 우선주, 알테오젠 무상증자, NAVER 소각·조건부 발행. 시세 제공 시총은 그대로 쓰지 않았다.',
       '- AMZN TTM owner proxy는−28.825B; DDOG는0.221826B; NET은−0.192782B. 보고 FCF와 SBC 이후 현금의 차이가 크다.',
       '- 메모리 최고 마진을 영구 연장하지 않았다. 삼성전자·SK하이닉스·MU에 매출 재설정·정상화 마진·낮은 종료배수 적용.',
       '- 한화·두산의 연결 전액 이익과 자회사 지분가치 중복을 제거했다. 별도 순부채·지원약정이 미확정이므로 SOTP는 명시적 범위 추정이다.',
       '- 신규 매수 승인0개. 미확인 현금권리·투자회수·대손·조달이 남은 종목은 INVESTIGATE를 유지한다. 불확실성을 회사 부정행위 또는 확정 실패로 바꾸지 않았다.\n',
       '## 종목별 결과\n','가치는 USD 또는 KRW 주당 추정. 같은9월4일 참조가격이지만 공시 분모와 시세 시점이 다르며 동시각 종가 시총이 아니다. Base는 보수적 가치의 보증이 아니며 실행 가능한 매수가로 쓰지 않는다.\n',
       '| 종목 | 품질/75 | 총점/100 | 판정 | Bear | Base | Bull | Base/가격 | 역산 성장¹ | 신뢰도 |\n|---|---:|---:|---|---:|---:|---:|---:|---:|---:|']
    for r in sorted(summary,key=lambda r:(-r['score'],r['ticker'])):
        report.append(f"| [{r['ticker']}](../../{r['report']}) | {r['quality_75']} | {r['score']} | {r['decision']} | {r['bear_value']:,.1f} | {r['base_value']:,.1f} | {r['bull_value']:,.1f} | {r['base_value_to_price']:.2f}x | {r['required_growth_2_10']:.1%} | {r['confidence']:.0%} |")
    report+=['\n¹ 고정된 첫12개월 추정매출 이후2~10년 성장률. ASTS는 절대 매출 경로에 대한 성장 스트레스. 10년 TTM CAGR나 실제 컨센서스로 해석하지 않는다.\n',
       '## 해석과 우선순위\n',
       '기업 품질과 가격 매력을 분리한다. ISRG·ANET·TSM·MSFT 등의 높은 품질점수는 즉시 진입 근거가 아니다. MELI·파마리서치처럼 Base 대비 할인으로 보이는 기업도 금융자본·전환권리·현금전환 증거를 먼저 확인해야 한다. 점수65 미만은 신규 후보 REJECT이며 기존 보유의 자동청산 지시가 아니다.\n',
       '모든 기업의 실제 증분 ROIC를 새 숫자로 만들지 않았다. 부족한 투자자본 분모는 null이고, 대신 관측 가능한 현금과 재투자 성과를 점수의 근거로 삼았다. 한미반도체 실제 OCF 등 원자료 미제공 항목은 unknown으로 남으며 해당 가치평가의 신뢰도가 낮다. 이는 필수 미래 예측을 사실로 채웠다는 뜻이 아니다.\n',
       '## 계산·감사 범위\n',
       '34×3=102개 현금 시나리오, 조건부 역산, 할인율/마진/종료배수/분모 민감도를 재현 가능하게 저장했다. 각 모형의 초기 현금적자는 삭제하지 않았고, 추가출자 등가와 별도 증자 대안을 동시에 차감하지 않았다. 사업가치 계산에 개시 순현금을 중복 더하지 않았다.\n',
       '기존 정책·raw 해시와 이전 날짜 산출물을 보존한다. 원자료 관측→재무 연결→명시 가정→계산→판정 경로를 파일로 추적할 수 있다. 기술적 검증 통과는 원문 전체 감사나 장기 추정의 정확성을 보증하지 않는다.\n',
       '다음 업데이트는 각 thesis의 논지 반증·증액 조건에 대응하는 실제 공시가 나왔을 때 수행한다. 가격만 움직였다는 이유로 기업 품질점수나 포지션을 바꾸지 않는다.\n']
    files[DIRECTORY+'/README.md']='\n'.join(report)+'\n'
    source_files=set(read('harness/baseline-lock.json')['raw_file_sha256'])
    source_files.update(['harness/deep_inputs.py','harness/deep_model.py','harness/deep_financials.py','harness/deep_report.py'])
    for t in inputs():
        source_files.update(read(f'companies/{t}/analyses/2026-09-06/assessment.json')['source_paths'])
        source_files.add(f'companies/{t}/analyses/2026-09-06/assessment.json')
    files[DIRECTORY+'/source-manifest.json']=dumps([{'path':p,'sha256':sha(p)} for p in sorted(source_files)])
    return files,ds


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');parser.add_argument('--check',action='store_true');args=parser.parse_args()
    files,ds=outputs()
    if args.write:
        for p,content in files.items():
            path=ROOT/p;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content,encoding='utf-8')
    if args.check:
        for p,content in files.items():assert (ROOT/p).read_text(encoding='utf-8')==content,('DEEP_NOT_REPRODUCIBLE',p)
    print(dumps({'status':'PASS' if args.check else 'WRITTEN' if args.write else 'READY','companies':len(ds),'artifacts':len(files)}).strip())

if __name__=='__main__':main()

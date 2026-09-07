"""Explicit-period financial bridges with immutable source references.

This is a reviewed subset, not an assertion that every raw extraction has been
re-audited. Ratios never invent missing OCF, SBC or invested-capital balances.
"""
from .core import ROOT, read, sha, pointer_escape

# ticker, period, revenue, operating profit, OCF, cash PPE, economic SBC,
# extra cash investment/lease principal. USD B / KRW T. '-' means unknown.
DATA='''
000660|H1 2026|131.895033|98.152891|91.742501|18.328836|-|-
005380|H1 2026|95.154214|5.365574|4.849653|4.003527|-|-
005930|H1 2026|305.37|146.73|145.36|31.23|-|1.73
012450|H1 2026 consolidated|-|-|-.3707|-|-|-
034020|H1 2026|8.985938|.547774|-|.163740|-|-
035420|H1 2026|6.629816183|1.062066553|1.186557719|.809757146|-|.044298448
042700|H1 2026|.302065115926|.138803055438|-|.011901874906|-|-
196170|H1 2026|.140492885685|.073480904822|.037550826893|.016227564118|-|.000559187028
207940|H1 2026 continuing|2.578030056694|1.167196422965|1.392488374186|.172611419110|-|.017993318800
214450|H1 2026|.324805059793|.123762004754|.064258667155|.021090725430|-|-
267260|H1 2026|2.178313164743|.545303822428|.480269932949|.139882641673|-|.009161233522
278470|H1 2026 restated|1.360888888861|.342824708032|.086404149570|.016794134780|-|.001127211290
AMZN|TTM through 2026-06-30|775.680|93.712|161.403|169.007|19.314|1.907
ANET|FY2025|9.0057|3.8561|4.3719|.1195|.4392|0
ASTS|H1 2026|.046255|-.446989|-.145212|.859215|-|.142103
AVGO|FY2025|63.887|25.484|27.537|.623|7.570|0
AXON|H1 2026|-|-|-.0114|.0442|.2787|-
DDOG|TTM through 2026-06-30|3.966725|.016329|1.229034|.156265|.850943|0
GOOGL|TTM through 2026-06-30|445.866|-|185.675|132.402|-|-
ISRG|TTM through 2026-06-30|11.0344|3.4512|3.7064|.4838|.8393|-
LLY|H1 2026|42.773|17.893|16.023|5.259|-|-
MSFT|FY2026|331.839|155.237|182.935|115.948|-|-
MU|Nine months FY2026 ended 2026-05-28|78.959|55.589|45.702|19.602|.918|-
NET|TTM through 2026-06-30|2.51235|-|-|-|.507655|-
NVDA|TTM through 2026-07-26|302.970|197.579|134.360|7.474|-|0
PLTR|H1 2026|3.568047|1.666002|2.115332|.021955|.466801|0
RKLB|H1 2026|.434414|-.113483|-.134407|.053112|.047677|0
VRT|FY2025|10.2299|1.8297|2.1138|.2200|-|.0064
VRTX|H1 2026|6.3208|2.3850|2.5535|.2456|-|-
MELI|H1 2026|19.014|1.294|-|.712|-|-
TSM|FY2025 translated at 31.37 NTD/USD|121.423461906|-|72.520752311|40.561396238|-|-
CRDO|Q1 FY2027 ended 2026-08-01|.479003|.120700|-|.007282|.087979|-
TEM|H1 2026|.730602|-.160624|-.080802|.014327|.106827|-
TMDX|H1 2026|.363881|.037033|.041842|.043749|-|-
'''

EXTERNAL={
'196170':{'url':'https://www.alteogen.com/en/sub/ir/news.php?bid=13&idx=359&mode=view&page=1','location':'Company announcement September2, agreement terms paragraph','facts':{'maximum_option_milestone_and_royalty_amount_usd_m':3223},'note':'All options and milestones conditional. Announcement says maximum includes royalties; do not add another unlimited royalty stream to the same headline amount. Not current cash or guaranteed backlog.'},
'PLTR':{'url':'https://www.sec.gov/Archives/edgar/data/1321655/000132165526000041/pltr-20260630.htm','location':'Cash Flow Statements; SBC reconciliation; diluted EPS table','facts':{'ocf_h1_usd_m':2115.332,'sbc_h1_usd_m':466.801,'diluted_shares_q2_m':2568.694},'note':'Balance sheet securities7.379052B differ from Treasury-only7.194962B; do not add both.'},
'ASTS':{'url':'https://app.quotemedia.com/data/downloadFiling?cdn=97b0f90b3039b64b39c17ee3c872f664&companyName=AST+SpaceMobile+Inc.&dateFiled=2026-08-10&formDescription=General+form+for+quarterly+reports+under+Section+13+or+15(d)&formType=10-Q&ref=320259077&symbol=ASTS&type=PDF&webmasterId=102691','location':'Cover; statements printed p.1/2/6; Note9 pp.16–17; July convertible subsequent event','facts':{'cover_class_a':299789305,'llc_b_equivalent':11215111,'llc_c_equivalent':78163078,'h1_ocf_usd_m':-145.212,'h1_ppe_usd_m':859.215},'note':'Official IR links to this filing. B/C voting shares themselves are non-economic; linked LLC units are economic exchangeable rights.'},
'RKLB':{'url':'https://www.sec.gov/Archives/edgar/data/1819994/000181999426000061/rklb-08102026ex991.htm','location':'Common shares and H1 consolidated cash flows','facts':{'actual_common_shares':598180438,'h1_ocf_usd_m':-134.407,'h1_sbc_usd_m':47.677,'h1_ppe_software_usd_m':53.112}},
'TEM':{'url':'https://investors.tempus.com/news-releases/news-release-details/tempus-reports-second-quarter-2026-results','location':'Balance sheets and H1 cash flows','facts':{'class_a_shares':175200077,'class_b_shares':5043789,'h1_ocf_usd_m':-80.802,'h1_sbc_usd_m':106.827,'convertible_promissory_note_liability_usd_m':187.929}},
'CRDO':{'url':'https://investors.credosemi.com/news-events/news/news-details/2026/Credo-Technology-Group-Holding-Ltd-Reports-First-Quarter-of-Fiscal-Year-2027-Financial-Results/','location':'September1 release, Q1 income statement and GAAP reconciliation','facts':{'diluted_shares_m':194.378,'q1_sbc_usd_m':87.979,'q1_revenue_usd_m':479.003,'cash_and_short_investments_usd_m':764.258}},
'NET':{'url':'https://www.sec.gov/Archives/edgar/data/1477333/000147733326000053/q226exhibit991.htm','location':'June30 balance sheet share classes, figures thousands','facts':{'class_a_shares_m':322.176,'class_b_shares_m':33.755}},
'AXON':{'url':'https://investor.axon.com/2026-08-05-Axon-reports-Q2-2026-revenue-of-904-million%2C-up-35-year-over-year','location':'Liquidity and cash flow tables','facts':{'cash_and_investments_usd_m_rounded':685,'h1_ocf_usd_m_rounded':-11.4,'h1_sbc_usd_m_rounded':278.7}},
'TMDX':{'url':'https://investors.transmedics.com/news-releases/news-release-details/transmedics-reports-second-quarter-2026-financial-results','location':'EPS table and cash flow statement','facts':{'q2_diluted_shares':40709227,'h1_ocf_usd_m':41.842}},
'267260':{'url':'https://www.hd-hyundaielectric.com/elect/en/','location':'Investor stock information2026-09-04 16:00:02','facts':{'price_krw':714000}},
'207940':{'url':'https://samsungbiologics.com/kr/ir/stock-info/stock-charts','location':'Stock information 2026-09-04','facts':{'price_krw':1447000}},
'042700':{'url':'https://alphasquare.co.kr/home/stock-summary?code=042700','location':'Reference quote/share information, tier4','facts':{'price_krw':230000,'shares_m_approx':95.3122}},
'214450':{'url':'https://alphasquare.co.kr/home/stock-summary?code=214450','location':'Reference quote tier4; share count remains approximation','facts':{'price_krw':386500}},
'278470':{'url':'https://alphasquare.co.kr/home/stock-summary?code=278470','location':'2026-09-04 15:55:50 reference quote','facts':{'price_krw':394000}},
'034020':{'url':'https://kr.investing.com/equities/doosan-heavy-ind.---const.','location':'Reference market quote tier4','facts':{'price_krw':79200}},
}

def financials(t):
    line=next(x for x in DATA.strip().splitlines() if x.startswith(t+'|'))
    _,period,*v=line.split('|');values=[None if x=='-' else float(x) for x in v]
    keys=['revenue','operating_profit','ocf','cash_capex','sbc','additional_cash_investment']
    d=dict(zip(keys,values));d.update(ticker=t,period=period,unit='KRW trillion' if t.isdigit() else 'USD billion',
                                    source_status='SELECTED_STORED_ASSERTIONS_WITH_TARGETED_PRIMARY_CHECKS')
    rev,op,ocf,capex,sbc,extra=values
    d['operating_margin']=op/rev if op is not None and rev is not None else None
    d['ocf_less_named_capex']=ocf-capex if ocf is not None and capex is not None else None
    d['ocf_less_capex_sbc_known_subtotal']=ocf-capex-sbc if all(x is not None for x in [ocf,capex,sbc]) else None
    d['owner_cash_proxy']=ocf-capex-sbc-extra if all(x is not None for x in [ocf,capex,sbc,extra]) else None
    d['owner_proxy_complete']=d['owner_cash_proxy'] is not None and extra is not None
    d['unknown_treatment']='null is unknown. A known subtotal is not a complete owner-FCF when SBC, leases, intangibles or cash scope remain unknown.'
    d['missing_components']=[k for k in keys if d[k] is None]
    if t in ['005380','MELI']:d['comparability_warning']='Financial subsidiary lending/credit working capital: consolidated OCF/PPE cannot be read as industrial owner-FCF.'
    if t=='NET':
        d['cash_capex']=None;d['ocf']=None;d['ocf_less_named_capex']=.314873;d['owner_cash_proxy']=.314873-.507655
        d['reported_company_fcf']=.314873;d['owner_proxy_complete']=False
        d['comparability_warning']='Company-defined FCF includes its specified adjustments. Do not infer exact cash capex from rounded OCF6.334e8. Owner proxy subtracts SBC from company FCF, not a GAAP FCF metric.'
    if t=='ISRG':d['reported_company_fcf']=3.2226
    if t=='ISRG':
        d['source_pdf_checks']=[
            {'uploaded_name':'ISRG 10-K.pdf','sha256':'b5cdfa25ecf5d1e558eef6216c56a54691308f674e60aac9bff0e95683bd8610','pdf_pages':[95,120],
             'fy25_usd_m':{'ocf':3030.5,'ppe':539.8,'income_statement_sbc':802.8,'capitalized_sbc':126.8}},
            {'uploaded_name':'0001035267-26-000058.pdf','sha256':'e88cbab4eb8ac260b161200ab51a95bacae509b35c0536181942432c8c2dfe6c','pdf_pages':[5,23],
             'h126_usd_m':{'ocf':1972.9,'ppe':215.9,'income_statement_sbc':426.1,'capitalized_sbc':67.8},
             'h125_usd_m':{'ocf':1297.0,'ppe':271.9,'income_statement_sbc':389.6,'capitalized_sbc':59.8}}]
        d['ttm_bridge']='FY25+H126−H125: OCF3706.4M, PPE483.8M, FCF3222.6M, income statement SBC839.3M, owner proxy2383.3M. Capitalized SBC134.8M is separate; inventory/amortization overlap not fully reconciled, so owner proxy remains incomplete.'
    if t=='MSFT':d['ocf_derivation']='182.935B is inferred from stored normalized FCF66.987B plus FY26 cash PPE115.948B; not a separately extracted raw OCF observation. Historical normalization source: screening/2026-09-us-kr/valuation-inputs-wave-01-02.csv.'
    if t=='DDOG':d['cash_capex_derivation']='OCF1.229034B−stored company FCF1.072769B=0.156265B; company-defined cash-investment bridge, not a new independent capex extraction.'
    if t=='MELI':d['reported_adjusted_fcf_h1']=.158;d['reported_adjusted_fcf_ttm']=1.481+.158-.512
    if t=='TSM':
        d.update(revenue=3809054/31.37/1000,ocf=2274976/31.37/1000,cash_capex=1272411/31.37/1000)
        d['ocf_less_named_capex']=(2274976-1272411)/31.37/1000
        d['translation_note']='NTD millions at disclosed approximate31.37 translation rate; not current spot FX. Native NTD amounts are the financial facts.'
    if t=='ASTS':d['operating_profit_derivation']='46.255M revenue−493.244M total operating expenses; includes125.911M involuntary-conversion loss. This accounting loss is not a second cash capex charge.'
    d['missing_components']=[k for k in keys if d[k] is None]
    d['incremental_roic']={'value':None,'reason':'Matched parent-attributable NOPAT and economic invested-capital cohorts not fully available. Margin growth is not incremental ROIC. Evaluate reinvestment and per-share cash evidence without inventing this ratio.'}
    d['source_paths']=[str(p.relative_to(ROOT)) for p in (ROOT/'companies'/t/'raw-data').glob('*.json')]
    if not d['source_paths']:
        d['source_paths']=[f'companies/{t}/valuation.json',f'companies/{t}/thesis.md']
    d['sources']=[{'path':p,'sha256':sha(p)} for p in d['source_paths']]
    if t in EXTERNAL:d['primary_or_quote_supplement']=EXTERNAL[t]
    return d


def ledger(t,obs):
    """Preserve source locations/pointers rather than hand-copying raw numbers."""
    financial_terms=('revenue','operating','cash','capex','net_income','share','capital','debt','sbc','inventory')
    selected=[r for r in obs if any(k in r['json_pointer'].lower() for k in financial_terms)]
    return {'ticker':t,'fact_definition':'reported assertion, not independently audited fact',
            'selected_raw_observation_ids':[r['id'] for r in selected],
            'financial_bridge':financials(t),'targeted_web_checks':[EXTERNAL[t]] if t in EXTERNAL else [],
            'judgment_sources':['harness/deep_inputs.py','harness/deep_model.py'],
            'full_raw_trace':'observations.json: immutable file hash, JSON pointer, source document, location and original units',
            'source_limits':'Stored raw extractions can contain errors. Selected financial anchors and high-impact rights/cash corrections checked; not every page or contract independently re-audited.'}

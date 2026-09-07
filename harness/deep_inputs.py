"""Analyst-reviewed 34-company inputs. Forecast numbers here are ESTIMATES.

Money: USD billions / KRW trillions; shares: millions. Historical observations
remain immutable in raw-data and the previous dated evidence ledger.
"""
from __future__ import annotations
from .core import read, ROOT

RUN='2026-09-06-deep'
DIRECTORY='reviews/'+RUN

# ticker | reference price | valuation economic shares m | unrestricted cash
# (conservative liquidity subset) | reserve assumption | six business scores
HEADERS='''
000660|1647000|746.66|87.957923|25|13,9,13,10,7,9
005380|383500|265.390108|20.256150|15|10,8,10,8,7,8
005930|255500|6648.649811|92.92|40|11,7,11,11,8,9
012450|1055000|51.563401|2|2|14,9,13,7,6,6
034020|79200|640.561146|2.541888|2|11,8,10,5,5,6
035420|213500|152.076491|6.38436979|3|11,8,10,8,6,9
042700|230000|95.3122|.088575409916|.05|13,9,11,10,7,8
196170|288500|69.655133|.080369735611|.05|13,9,12,8,7,8
207940|1447000|46.290951|.288575631853|.2|13,9,13,11,7,8
214450|386500|10.3896|.220289875319|.1|12,8,10,10,7,8
267260|714000|36.05|1.009|.4|13,9,12,12,8,9
278470|394000|37.438155|.094463145498|.05|12,8,9,9,7,8
AMZN|258.51|10786.313572|78.213|50|14,9,13,8,7,9
ANET|193.78|1276|2.2902|1|14,9,13,13,8,10
ASTS|62.31|389.167494|3.419453|.5|12,8,8,3,5,3
AVGO|357.895|4758|19.628|10|14,9,12,11,7,8
AXON|515.67|81.24|.685|.4|14,9,13,7,7,7
DDOG|212.93|359.075|4.985|1|14,9,12,8,7,10
GOOGL|338.46|12230|242.474|80|14,9,12,9,6,9
ISRG|366.70|353.9|8.63|2|14,9,14,13,8,10
LLY|1149.36|899.3|8.950|6|14,9,13,11,7,8
MSFT|499.70|7443|76.843|40|14,9,14,10,7,10
MU|1016.59|1145|24.995|5|12,8,11,8,7,8
NET|278.92|355.931|4.163|2|14,9,12,6,6,8
NVDA|230.36|24147|56.586|30|14,9,14,12,6,8
PLTR|174.33|2568.694|2.030047|2|14,9,12,10,6,10
RKLB|64.26|598.180438|2.129485|.5|13,9,10,4,5,5
VRT|280.53|393|3.1106|1|13,9,11,10,7,8
VRTX|546.12|256|13.6415|5|13,9,13,11,7,9
MELI|1978.36|50.697|3.649|3|14,9,14,9,8,8
TSM|428.91|5186.5049042|97.82|40|14,9,13,12,9,9
CRDO|170.57|194.378|.764258|.3|13,9,11,9,6,9
TEM|64.62|180.243866|.599614|.2|12,8,9,4,5,5
TMDX|89.98|40.709227|.472675|.2|13,9,12,8,6,7
'''

# Each case: next-12-month revenue, growth years 2–5, growth years 6–10,
# initial owner margin, mature owner margin. These are explicit independent
# analyst scenarios, not financial statements or company guidance.
OPERATING='''
000660|memory|200,-.02,.02,.25,.10|250,.07,.04,.35,.18|300,.13,.07,.42,.25
005380|auto_and_finance|185,.00,.01,.020,.020|205,.05,.03,.030,.035|230,.08,.04,.040,.050
005930|electronics|520,.00,.02,.18,.08|620,.05,.04,.24,.14|720,.10,.06,.30,.21
012450|parent_defense_aviation|14,.07,.03,.05,.055|17,.14,.07,.07,.09|20,.20,.10,.09,.12
034020|parent_power|8.2,.04,.03,.01,.025|9,.10,.07,.025,.05|10,.18,.10,.04,.08
035420|search_commerce_cloud|13.4,.04,.02,.07,.07|14.5,.09,.05,.09,.12|15.5,.14,.08,.10,.16
042700|packaging_equipment|.65,.04,.02,.25,.20|.85,.17,.07,.30,.30|1.05,.28,.12,.35,.38
196170|royalties_and_licenses|.25,.12,.02,.15,.20|.45,.28,.07,.35,.48|.7,.40,.12,.45,.60
207940|continuing_cdmo|5,.06,.03,.24,.24|5.8,.13,.07,.30,.32|6.5,.18,.10,.34,.38
214450|regenerative_aesthetics|.65,.08,.03,.17,.17|.78,.18,.08,.22,.25|.9,.25,.12,.26,.30
267260|power_equipment|4.5,.05,.03,.12,.12|5.2,.13,.07,.16,.18|6,.20,.10,.19,.23
278470|beauty_devices_cosmetics|2.6,.03,.02,.09,.08|3.2,.16,.07,.13,.16|3.8,.27,.12,.16,.20
AMZN|consolidated_no_ad_doublecount|820,.06,.03,-.04,.025|930,.12,.06,-.02,.06|1040,.17,.09,.00,.09
ANET|networking|11.5,.10,.04,.31,.28|13,.20,.10,.36,.34|14.5,.28,.13,.38,.40
ASTS|commercial_satellite|.15,.35,.08,-5,.12|.4,.55,.15,-3,.24|.8,.75,.20,-2,.32
AVGO|semiconductor_and_software|125,.08,.03,.27,.25|145,.17,.08,.31,.33|165,.24,.11,.35,.40
AXON|public_safety_platform|3.9,.09,.04,-.08,.08|4.5,.18,.09,-.04,.16|5,.26,.12,.00,.23
DDOG|observability|4.6,.12,.05,.05,.10|5.2,.23,.11,.08,.20|5.8,.32,.16,.12,.28
GOOGL|search_youtube_cloud|475,.05,.03,.04,.12|530,.11,.07,.06,.20|590,.17,.10,.08,.26
ISRG|robotic_surgery|12,.07,.04,.19,.18|13.2,.13,.08,.22,.23|14.5,.18,.11,.24,.28
LLY|approved_drugs|87,.04,-.02,.14,.14|98,.12,.05,.22,.25|110,.20,.10,.27,.32
MSFT|software_cloud_ai|365,.07,.03,.10,.16|400,.14,.08,.14,.24|435,.20,.11,.18,.31
MU|memory|155,-.02,.02,.20,.10|180,.08,.04,.28,.17|205,.15,.07,.35,.24
NET|connectivity_security_workers|3,.15,.06,-.07,.07|3.5,.28,.13,-.04,.18|4,.40,.20,.00,.28
NVDA|compute_networking|410,.03,.02,.32,.25|500,.12,.07,.39,.35|590,.20,.11,.44,.42
PLTR|aip_government_commercial|9,.18,.08,.25,.25|10.8,.32,.16,.32,.35|12.5,.45,.22,.38,.43
RKLB|launch_and_space_systems|.95,.12,.04,-.30,.08|1.2,.26,.12,-.20,.18|1.5,.40,.20,-.12,.27
VRT|power_cooling_services|13,.07,.03,.11,.10|15,.18,.09,.14,.17|17,.27,.14,.17,.22
VRTX|approved_cf_and_new_launches|13,.02,-.01,.20,.20|14,.09,.05,.25,.28|15,.15,.08,.28,.34
MELI|commerce_and_fintech|40,.10,.05,.02,.03|46,.20,.10,.04,.07|52,.29,.14,.06,.10
TSM|foundry|165,.04,.03,.20,.18|185,.13,.08,.25,.27|205,.20,.11,.30,.33
CRDO|connectivity|2,.08,.03,.15,.13|2.35,.25,.12,.22,.24|2.7,.40,.20,.27,.32
TEM|diagnostics_data|1.6,.10,.04,-.13,.03|1.85,.23,.10,-.10,.13|2.1,.35,.16,-.07,.22
TMDX|ocs_and_logistics|.78,.05,.02,-.03,.08|.9,.16,.07,.02,.16|1.02,.25,.12,.05,.23
'''

# Base mature margin is independently reconciled to economic operating cash.
# [GAAP/economic operating margin AFTER SBC, tax rate, D&A less ALL capex,
# normalized working-capital cash cost, interest/net-principal/other claim cost]
# KR financial lending companies' WC includes required credit capital. Values
# are model estimates, not attempts to infer an undisclosed maintenance capex.
BRIDGES={
'000660':[.35,.25,-.055,.02,.0075], '005380':[.065,.25,-.005,.003,.00575],
'005930':[.27,.25,-.04,.015,.0075], '012450':[.15,.25,-.005,.01,.0075],
'034020':[.10,.25,-.005,.01,.01], '035420':[.22,.25,-.025,.01,.01],
'042700':[.46,.25,-.02,.02,.005], '196170':[.70,.25,-.015,.02,.01],
'207940':[.44,.25,.015,.015,.01], '214450':[.38,.25,-.02,.01,.005],
'267260':[.27,.25,-.0125,.005,.005], '278470':[.25,.25,-.0125,.01,.005],
'AMZN':[.13,.21,-.0327,.005,.005], 'ANET':[.45,.21,-.0055,.01,0],
'ASTS':[.45,.21,-.08,.02,.0155], 'AVGO':[.46,.21,-.0084,.005,.02],
'AXON':[.27,.21,-.0283,.02,.005], 'DDOG':[.29,.21,-.0191,.01,0],
'GOOGL':[.34,.21,-.0536,.005,.01], 'ISRG':[.33,.21,-.0207,.01,0],
'LLY':[.40,.21,-.036,.01,.02], 'MSFT':[.45,.21,-.1005,.005,.01],
'MU':[.34,.21,-.0786,.01,.01], 'NET':[.28,.21,-.0262,.01,.005],
'NVDA':[.48,.21,-.0142,.01,.005], 'PLTR':[.47,.21,-.0113,.01,0],
'RKLB':[.32,.21,-.0528,.01,.01], 'VRT':[.27,.21,-.0233,.01,.01],
'VRTX':[.42,.21,-.0318,.005,.015], 'MELI':[.15,.25,-.015,.02,.0075],
'TSM':[.49,.20,-.102,.015,.005], 'CRDO':[.35,.21,-.0165,.015,.005],
'TEM':[.23,.21,-.0217,.02,.01], 'TMDX':[.30,.21,-.052,.01,.015]}

# Quantitative conclusions and outstanding economic uncertainties, specific to
# each company. Estimates remain such even when a research gate is complete.
NOTES={
'000660':('메모리 최고 마진을 정상화한다. FY25/H1 비교로 계산한 TTM OCF−유형자산 취득은 91.794조원이다. 과거 27.823조원을 현재 FCF로 재사용하지 않는다.',
'H1 영업이익률 약 74.4%는 장기 정상치가 아니다. HBM 세대 전환, 경쟁 공급·고객의 재고 축적, 투자 후 D&A 상승을 동시에 스트레스한다.',
'7월 신주 17.79백만주와 조달 39.89조원은 6월 결산 후 사건. 8월 환매 계획 24.07백만주는 체결·소각 전 미차감. 728.87백만+17.79백만의 추정 분모를 사용하며 주식등기 정밀 대조 오차 ±2%를 병기한다.',
'memory_cycle','HBM 판매 증가에도 두 반기 연속 OCF−전체 Capex가 악화하고 신제품 고객 채택·수익성이 동반 하락하면 해자 확대 논지를 폐기한다.',[4,6,8]),
'005380':('H1 연결 OCF 4.850조원에서 PPE 4.004조원을 빼면 0.846조원이나 금융채권 변동이 포함되어 자동차 owner FCF로 해석할 수 없다.',
'차량 H1 영업이익 3.758조원·금융 1.338조원·기타 0.269조원을 분리했다. 금융부채 188.805조원을 자동차 영업가치에서 전액 차감하지 않는다.',
'보통주 204.758백만주와 우선주 60.632백만주의 경제적 배분을 함께 적용. 자사주 처분 시점 오차를 보수적으로 포함한 발행주식 분모이다. 금융 충당금·필요자본 이후 귀속 현금마진을 사용해 연결 현금흐름의 왜곡을 우회한다.',
'auto_finance_cash_partition','자동차 세후 현금수익과 금융 연체·대손이 동시에 악화하여 배당이 차입 의존으로 바뀌면 재검토한다.',[3,4,8]),
'005930':('H1 OCF 145.36조원−PPE 31.23조원−무형자산 1.73조원=112.40조원. 저장된 반올림 FCF 112.39조원과 0.01조원 차이는 반올림으로 보존한다. H1을 TTM으로 부르지 않는다.',
'메모리 현금수확, 파운드리 회수 불확실성, 모바일·디스플레이를 함께 반영한 정상화 현금마진이다. 이익 급등만으로 구조적 ROIC를 높이지 않는다.',
'보통주와 우선주 총 6,648.650백만주에 동일 경제적 현금권리 근사를 적용한다. 보통주 기준 암묵가치와 실제 두 종류 시가총액은 구분. 15조원 직원 보상용 환매는 무상 주당 증가가 아니다.',
'memory_cycle','HBM 경쟁력 회복 없이 파운드리 손실·유휴설비가 확대되고 사이클 하락기에 환원 재원이 차입으로 바뀌면 논지 폐기.',[4,5,8]),
'012450':('연결 이익을 전액 보통주 몫으로 계산하지 않는다. 방산·항공 본체 현금과 Ocean·Systems·KAI 지분 표식을 분리한 SOTP 범위이다.',
'본체 FY25 방산·항공 영업이익 2.276조원과 H1 연결 OCF −0.371조원 사이의 차이는 선수금·운전자본·비지배지분 확인 필요성을 뜻한다.',
'별도 순차입·보증의 확정 합계는 미공개/미연결이다. 따라서 순차입·자본약정 2/3/6조원을 추정 스트레스로 명시하며 2조원 현금/2조원 유보는 조달능력을 인정하지 않는 분석 가정이다. 자회사 가치와 자회사 현금을 중복 가산하지 않는다.',
'parent_sotp','방산 수주가 인도·현금으로 전환되지 않고 자회사 지원·증자 반복으로 본체 주당 현금이 훼손될 때.',[0,1,2,4,8]),
'034020':('H1 연결 영업이익 0.548조원 중 Bobcat 0.499조원, 본체 0.154조원, Fuel Cell −0.052조원, 조정 등이 섞여 있다. 이를 전액 원전 이익으로 간주하지 않는다.',
'본체 FY25 순매출 7.789조원·영업이익 0.302조원에서 출발한다. SMR MOU는 확정 인도·현금수금이 아니다.',
'별도 지분 처분가능 가치와 별도 순부채는 범위 추정으로 표시한다. 자회사 연결 매출을 본체 성장 가정에 더하지 않았다. 본체 마진 5% 현금화에도 현재 가격이 요구하는 기간을 별도 역산한다.',
'parent_sotp','확정 착공·제작 수주가 늘지 않거나 본체 현금손실을 Bobcat 처분·차입으로 반복 충당하면 원전 복리 논지 무효.',[1,4,6,8]),
'035420':('H1 OCF 1.187조원−PPE 0.810조원−무형자산 약 0.044조원=약 0.332조원. 광고·커머스 성장과 AI 현금재투자 부담을 분리한다.',
'NVIDIA 제3자 배정 7.242백만주는 조건부다. 10월 납입 전 기존 주식과 미래 1조4,809억원을 동시에 확정 반영하지 않는다.',
'기존 156,977,585주에서 8월 4,901,094주 소각 후 152,076,491주를 기본으로 사용한다. 조건부 발행 시 159,318,055주로 별도 희석. $9B 인프라 조건은 즉시 현금 지출 전액과 같지 않지만 무상 성장도 아니다.',
'platform_capex','검색·커머스 고객 유지가 둔화하고 AI 투자 이후 주당 owner 현금이 두 반기 연속 하락하면 재검토.',[1,4,5,8]),
'042700':('FY25 매출 0.577조원, H1 0.302조원과 비교 H1 0.327조원으로 TTM 0.551조원. Q2 급증만으로 H1 둔화를 지우지 않는다.',
'원자료에 OCF가 없으므로 실제 owner FCF는 unknown이다. 추정 현금마진은 영업이익·설비투자·운전자본 비용으로 분해하며 보고 FCF라고 쓰지 않는다.',
'차입금 null은 무차입의 증거가 아니다. 현금 885.8억원만 유동성에 인정하고 리스·신공장·환매 재원을 점검한다. 95.3122백만주 분모는 시세 정보 기반 추정으로 ±5% 민감도를 표시한다.',
'equipment_cycle','TC bonder 고객 발주가 경쟁사로 이동하고 단가·현금회수가 함께 하락하거나 hybrid bonding 전환에서 지위를 잃으면 폐기.',[1,4,5,7]),
'196170':('FY25/H1 동기 차감 TTM 매출 0.254조원·OCF 0.098조원. 계약 최대 총액은 조건부 마일스톤이며 현재 매출·현금과 다르다.',
'KEYTRUDA SC 상업화는 로열티 경로를 지지하지만 계약별 비공개율을 사실로 채우지 않는다. 1~3% 로열티율과 채택 속도를 명시적 추정으로 시험한다.',
'8월 무상증자 후 보통주 69.655백만주; RCPS 0.529백만주 별도. 회사 표기 차입 0.179조원을 0.007조원으로 축소하지 않는다. 현금흐름 모델에 우선권 비용을 반영하고 원금은 시나리오 별도 차감한다.',
'royalty_contract','실제 경상 로열티가 계약 발표와 달리 4개 분기 이상 매출·현금으로 확인되지 않거나 주요 특허·독점권이 훼손되면 폐기.',[1,2,7,8]),
'207940':('분할 이후 계속사업 FY25 매출 4.557조원·영업이익 2.069조원, H1 매출 2.578조원·영업이익 1.167조원이다. 분할 전 Epis 매출을 더하지 않는다.',
'H1 OCF−PPE−무형자산=1.202조원이나 HGS 인수 현금 0.534조원은 별도 자본배분이다. 최소 계약 backlog와 예상 추가 발주를 구별한다.',
'46.291백만주 분할 후 분모를 사용한다. PolyPeptide 공개매수 총 현금은 조건부이며 본체 가치에 인수 매출을 공짜로 넣지 않는다. 환율·조달을 포함한 2.2~3.0조원 조건부 인수 현금 스트레스 적용.',
'cdmo_capacity','증설 후 이용률·수율·배치 수금이 4개 분기 개선되지 않고 고객 집중·품질 이슈가 동반되면 장기 계약 해자 가설 무효.',[1,4,7,8]),
'214450':('TTM 매출 0.604조원·OCF−PPE 0.138조원. H1 이익 확대에 비해 영업현금은 0.075조원에서 0.064조원으로 감소했다.',
'리쥬란 브랜드와 의료기관 채널의 반복 수요를 인정하되 경쟁 제품·국가별 규제·소비자 유행을 해자와 구분한다.',
'차입·사채 0.214조원 대부분은 RCPS 0.207조원이다. 전환상환우선권을 부채 차감과 전환주식 증가로 동시에 반영하지 않는다. 기본 모델은 상환 현금 비용, 전환은 별도 권리 민감도이다.',
'preferred_claim','매출 확대에도 매출채권·재고가 더 빨리 늘고 시술 단가·재구매율이 하락하여 주당 현금이 두 반기 악화하면 재검토.',[2,4,7]),
'267260':('TTM 매출 4.337조원·OCF−PPE 0.671조원. 무형자산 취득을 제외한 수치이므로 이를 완전 owner FCF로 과장하지 않는다.',
'변압기 공급 부족과 장기 수주가 가격결정력을 지지한다. 선수금 선유입·구리 가격·증설 후 납기 단축으로 정상 마진은 낮아질 수 있다.',
'9월4일 회사 홈페이지 기준 714,000원. 분모 36.05백만주는 반올림 추정이며 ±1% 시험. 증설 Capex와 운전자본을 owner margin에 포함하고 수주잔고를 가치에 가산하지 않는다.',
'power_cycle','신규 수주 단가와 수주잔고 현금 전환이 동반 하락하고 증설 생산성이 자본비용을 밑돌면 정상화 가정 하향.',[4,6,8]),
'278470':('TTM 매출 2.294조원·OCF−PPE 0.287조원. H1 재고 0.165→0.370조원으로 현금전환 저하가 매출 고성장에 가려진다.',
'FY25와 H1 비교 영업이익은 정정값을 사용한다. 회계상 제품개발 R&D 비용을 Capex로 다시 더하지 않는다.',
'37.438155백만주 분모는 원자료. 지급가능 현금 분리 정보가 부족해 0.15조원 유보 가정으로 흑자 지속의존을 시험한다. 광고·판매자 수수료 상승이 해자보다 빨리 성장할 위험을 반영한다.',
'consumer_brand','해외 판매 성장에도 재고회전·반복구매·광고비 차감 후 현금수익이 두 반기 악화하면 재평가.',[3,4,8]),
'AMZN':('TTM OCF 161.403B−순현금 PPE 169.007B=−7.604B; SBC 19.314B와 금융리스·금융약정 원금 1.907B 차감 후 owner proxy −28.825B.',
'Q2 기타이익 53.415B를 반복 영업현금으로 넣지 않는다. AWS·북미·국제 부문 매출 안의 광고를 별도 가산하지 않는다.',
'보통주 10,786.314백만주, H1 신규 차입 66.998B. 유지 Capex를 임의 축소하여 음수 현금을 삭제하지 않는다. 첫 4년 cash margin 전환과 AWS 투자 회수 지연을 민감도로 제시한다.',
'segment_capex','AWS 사용률·단위 현금수익 증가보다 설비·리스비용이 더 빨리 늘고 소매 개선도 이를 상쇄하지 못하면 복리 가정 하향.',[1,4,8]),
'ANET':('FY25 OCF 4.372B−PPE/무형 취득 0.120B−SBC 0.439B=owner proxy 3.813B. H1 OCF와 낮은 직접 Capex는 우수하나 선수금·재고 효과를 정상화한다.',
'두 최종 고객 16%·26%는 실제 고객 집중이다. 유통업체 42%를 최종고객으로 잘못 읽은 AVGO와 같은 숫자로 비교하지 않는다.',
'Q2 가중평균 희석주식 1,276백만주를 보수적 현시점 옵션 포함 proxy로 사용. 미래 SBC 비용을 cash margin에 포함하며 같은 보상의 연간 희석을 다시 적용하지 않는다.',
'network_platform','고객 자체 네트워킹·경쟁 장비 전환으로 점유와 현금마진이 함께 하락하고 신규 800G/1.6T 채택이 지연되면 논지 폐기.',[7,8]),
'ASTS':('H1 OCF −0.145B−PPE 0.859B=−1.004B; 주파수·Ligado 투자 포함 현금부담은 더 크다. 6월 제한현금 0.435B는 runway에 넣지 않는다.',
'Class A 299.789백만주에 B/C와 연결된 교환가능 LLC 경제지분 89.378백만주를 포함해 389.167백만주로 평가한다. B/C 자체 의결권이 현금권리라는 뜻은 아니다.',
'7월 전환사채 순유입 1.1312B를 현금에 가산하되 부채·상환 경로도 모형에 반영한다. 가입자 수·통신사 수익배분·위성 교체 Capex는 수익화 이후에도 필요하다. 실험 성공은 자기조달 사업의 증명이 아니다.',
'milestone_funding','발사·커버리지·상업 가입자 유입 지연으로 보유 현금보다 건설·교체 비용이 커지고 조달 창구가 닫히면 지분가치 영구손실.',[0,1,2,4,7,8]),
'AVGO':('FY25 보고 FCF 26.914B−SBC 7.570B=owner proxy 19.344B. 일회성 세금혜택·인수 무형자산 상각을 단순히 영구 현금마진으로 가산하지 않는다.',
'AI ASIC·네트워킹과 VMware 반복소프트웨어를 별개 성장 경로로 해석한다. Q3 29.591B 매출과 13.665B FCF가 기준년 이후 수익 가속을 보여준다.',
'4,758백만주는 5월3일 공시 분모로 시세 제공 시총보다 신뢰하되 현재 ±5% 권리 오차 민감도를 표시한다. 기존 66.720B 부채와 인수 통합 부담은 현금 마진의 이자·순상환에 반영한다.',
'semis_software','대형 AI 설계 고객의 내재화와 소프트웨어 갱신 악화가 함께 발생하여 SBC 차감 주당 현금이 4개 분기 하락하면 재검토.',[0,4,7,8]),
'AXON':('강한 장기 계약·NRR과 반기 음수 FCF를 동시에 반영한다. FY26 SBC 가이던스 590~620M은 경제적 인건비이며 조정 EBITDA만으로 가치평가하지 않는다.',
'기기 설치→Evidence 사용→신규 소프트웨어 교차판매가 고객 편익의 경로다. 계약 총액 15.1B는 모두 취소 불가능한 현금채권이 아니다.',
'기말 81.24백만주. 신규 보상은 owner margin에 비용화, 무상 환매 없음. 내부통제·신사업 인수·구독 회수기간 위험은 신규 진입 veto 조사로 유지한다.',
'sbc_platform','계약 확대에도 고객 이탈·수금 지연·보상비용이 매출보다 빨리 늘어 주당 현금 전환이 4개 분기 지연되면 가정 폐기.',[0,2,4,8]),
'DDOG':('TTM 보고 FCF 1.072769B−SBC 0.850943B=0.221826B, 보고 FCF의 약 20.7%만 남는다. FCF yield를 보상 차감 전으로 제시하지 않는다.',
'통합 관측성은 고객 운영비용을 낮추지만 OpenTelemetry와 클라우드 자체 도구가 데이터 잠금 효과를 약화할 수 있다.',
'6월 실제 359.075백만주와 현금·투자 4.985B를 구분한다. 만기채무와 신규 보상·미행사 권리는 별도 시험. 영업현금의 선수금 가속을 영구 현금마진으로 가산하지 않는다.',
'sbc_platform','제품 확장에도 순유지·사용량 증가와 SBC 차감 주당 현금이 두 반기 악화하면 장기 통합 플랫폼 가정 하향.',[2,4,6,8]),
'GOOGL':('TTM 매출 445.866B·OCF 185.675B−PPE 132.402B=53.273B. SBC 약 28.1B를 경제비용으로 보아 owner proxy 약25.2B로 낮춘다.',
'검색·YouTube의 현금기반과 Cloud/AI의 자본회수 시간을 분리한다. AI 사용량이나 비상장 투자 평가이익은 독립적 고객 현금의 대체물이 아니다.',
'GOOG/GOOGL/비상장 보통주 합계 12.230B주. 우선주 청산권 19B는 별도 차감, 강제전환은 19B 재차감 없이 추가 주식 권리 민감도로 비교. 과거 낮은 Bull 할인율은 사용하지 않는다.',
'platform_capex','AI 답변의 광고 단위경제가 기존 검색보다 낮고 투자·배포비가 증가하여 주당 현금이 지속 감소하면 재검토.',[0,2,4,8]),
'ISRG':('TTM 매출 11.0344B·영업이익 3.4512B·보고 FCF 3.2226B. 반복 소모품·서비스 현금에 SBC 약8% 매출 추정 비용을 반영한 보수적 시작 현금마진이다.',
'임상·교육·설치 기반은 실질 전환비용이다. 시술 증가가 임대 비중 상승·가격 압박·병원 자본제약을 모두 상쇄한다는 보장은 없다.',
'기말 353.9백만주, 현금·투자 8.63B. 환매를 무상으로 간주하지 않고 미래 보상비용을 마진에 포함한다. 손상·임대잔존가치·서비스 유지 Capex를 제외하지 않는다.',
'procedure_recurring','시술 성장 10% 미만이 4개 분기 지속되고 경쟁사의 임상·교육 전환 증거가 동반되면 높은 해자 점수 재검토.',[]),
'LLY':('H1 매출 42.773B·영업이익 17.893B·OCF 16.023B−PPE 5.259B=10.764B. IPRD·인수 현금은 이익 성장과 별도 자본배분으로 기록한다.',
'Q2 Mounjaro/Zepbound 합계 14.871B로 매출 약65%. 물량 증가와 가격 −13%가 공존하므로 단순 가격결정력 가정은 배제한다.',
'현재 승인 약물에 기반한 매출 경로이며 미승인 파이프라인을 전액 매출로 가산하지 않는다. 신약 R&D 지속 비용과 생산능력 투자, 54.908B 차입 부담을 owner margin에 포함한다.',
'drug_lifecycle','GLP-1 순가격·지속사용·안전성이 함께 악화하고 신규 적응증·생산투자 회수가 이를 상쇄하지 못하면 성장기간 단축.',[4,7,8]),
'MSFT':('FY26 매출331.839B·영업이익155.237B. OCF−현금PPE 66.987B는 SBC·리스 원금 차감 전으로 유지한다. AI Capex와 회계 내용연수 변경을 현금과 혼동하지 않는다.',
'9월2일 부문 재분류는 총매출·영업이익을 늘리지 않는다. M365·Azure·개발 생태계의 교차판매와 대규모 컴퓨팅 재투자 수익을 별개로 평가한다.',
'7,443백만주 반올림 분모. FY26 현금PPE115.948B 이후 더 높은 투자 계획의 현금회복을 5년에 걸쳐 모델링한다. 금융리스의 원금비용은 순현금 재투자 항목에 포함하는 추정이다.',
'platform_capex','AI 관련 수익 증가보다 전체 설비·리스 현금부담이 계속 빨리 늘고 고객 사용률·가격이 낮아지면 ROIC 가정 하향.',[4,7,8]),
'MU':('FY25/9개월 동기 차감 TTM OCF 51.432B−PPE25.260B=26.172B. 보조금 포함 net capex와 cash gross capex를 섞지 않는다.',
'9개월 FY26 매출78.959B·영업이익55.589B, Q3 영업이익33.318B는 사이클 고점의 성격이 강하다. 고점 수익률의 영구 연장을 금지한다.',
'Q3 희석 1,145백만주를 보수적 권리 proxy로 적용. 신공장 투자는 장기 생산성 증거가 필요하다. 5B 현금/5B 유보는 실제 잔액 사실이 아닌 가용 유동성을 인정하지 않는 하방 가정이다.',
'memory_cycle','HBM·DRAM ASP 하락과 공급 확대가 동시에 발생해 두 반기 연속 전체 Capex 이후 현금이 악화하면 정상화 가치 하향.',[4,6,8]),
'NET':('TTM 회사 FCF0.314873B−SBC0.507655B=owner proxy−0.192782B. 보고 FCF 흑자와 현재 주주의 경제적 현금은 다르다.',
'Workers·보안·네트워크 통합의 고객 가치는 인정한다. 높은 매출 성장만으로 CDN 비용·보상·유지 설비를 차감한 초과이익이 증명되지는 않는다.',
'6월 A322.176M+B33.755M=355.931M주. 8월 전환채 발행은 이자 0%라도 희석·만기 의무가 사라진 것이 아니다. 동일 SBC의 현금 차감과 미래 연간희석을 이중 적용하지 않는다.',
'sbc_platform','기업 고객 채택 확대에도 SBC 차감 현금 적자가 4개 분기 지속되고 가격 인상·제품 확장이 이를 해소하지 못하면 논지 폐기.',[2,4,6,8]),
'NVDA':('TTM 매출302.970B·영업이익197.579B, OCF−Capex/자산원금126.886B. 자본투자·고객 금융지원·SBC를 공제한 정상 현금마진을 사용한다.',
'CUDA·네트워킹·시스템 공동설계는 강한 해자지만 고객 자체칩과 투자회수 제약은 수요의 독립성을 시험한다.',
'24.147B주. 공급약정279B와 SB Energy 최대105B 조건부 지원을 즉시 전액 손실로 보지도, 서로 독립인 위험으로 보지도 않는다. 같은 AI 투자 사이클의 공동 스트레스이다.',
'correlated_ai_commitments','고객 AI 투자수익 악화와 공급약정·지원자금 집행이 동시 발생해 현금전환·가격결정력이 구조적으로 낮아지면 재검토.',[1,4,7,8]),
'PLTR':('TTM 매출6.155941B. Q2 조정 FCF1.220359B는 SBC·고용주세 조정의 영향을 포함하므로 GAAP owner FCF로 쓰지 않는다.',
'H1 GAAP 영업이익1.666B의 레버리지는 실재하지만 정부 계약·AIP 확장과 고객 경제적 회수의 지속성은 별도다.',
'2,568.7백만주는 시세자료 희석분모 proxy이며 확정 기말주식 수가 아니다. ±5% 권리 민감도를 별도 표시한다. GAAP 보상 포함 장기 마진을 사용하고 5.6B 클라우드 약정을 비용에서 제외하지 않는다.',
'sbc_platform','미국 상업 성장률 둔화와 신규 고객의 현금수익·갱신 악화가 동시에 발생하면 10년 고성장 기대 하향.',[2,4,6,8]),
'RKLB':('H1 OCF−0.134407B−PPE/소프트웨어0.053112B=−0.187519B. SBC0.047677B까지 차감한 owner proxy−0.235196B.',
'전자·위성시스템·발사 통합 가치는 있으나 Neutron 지연은 연구비·발사매출·고객 신뢰를 함께 훼손할 수 있다.',
'6월598.180438백만주는 자사주를 제외한 실제 분모이다. Iridium 약8B EV를 모두 주주 대가로 보거나 신규 매출을 공짜로 넣지 않는다. 미완료 거래는 별도 범위로 스트레스하고 3.6B bridge 금융 실행을 감시한다.',
'milestone_funding','Neutron 일정·성능 목표의 반복 미달로 현금소진이 가속되고 인수금융·주식대가가 기존 주주 이익을 넘어설 때.',[1,2,4,8]),
'VRT':('FY25 OCF2.1138B−PPE0.2200B−소프트웨어0.0064B=1.8874B. H1 OCF 증가에는 선수금·운전자본 타이밍이 포함된다.',
'고밀도 전력·액체냉각 수요는 구조적이나 OEM 가격경쟁과 증설 후 고객 자체조달이 마진을 제한할 수 있다.',
'6월 부채2.9398B를 기존 term loan과 다시 더하지 않는다. 393M주는 과거 표준화 분모의 반올림 proxy. UIG 미완료 인수의 매출을 본체 경로에 확정 가산하지 않는다.',
'power_cycle','수주 대비 매출·현금 전환이 둔화하고 선수금 감소와 가격경쟁으로 주당 owner cash가 두 반기 감소하면 재평가.',[4,6,8]),
'VRTX':('TTM 매출12.5872B. H1 OCF2.5535B−PPE0.2456B=2.3079B는 SBC 차감 전이다. CF 중심 승인 제품 현금을 기준으로 신제품을 점진 반영한다.',
'TRIKAFTA와 ALYFTREK은 같은 질환이다. JOURNAVX·CASGEVY 매출은 다변화 가능성을 보여주나 아직 CF 집중을 제거하지 못한다.',
'13.6415B 현금·증권과 8.8B Crinetics 거래는 별도. 4.5B term loan/0.5B revolver는 약정 용량과 6월 실제 차입을 구분한다. 매수대가 차감·신약 가치를 상쇄하는 증분 NPV 범위를 사용한다.',
'drug_lifecycle','CF 수익성·특허/경쟁 보호가 약화되는 동안 비CF 제품의 보험·처방·현금 실적이 충분히 커지지 못하면 장기 가정 하향.',[4,7,8]),
'MELI':('TTM 회사 조정FCF=1.481+0.158−0.512=1.127B. 고객 예치금·신용공급 현금을 일반 소프트웨어 OCF와 비교하지 않는다.',
'상거래 물류밀도와 결제 네트워크의 상호 강화는 강하나 무료배송·신용손실·마케팅 투입을 뺀 고객 코호트 수익이 핵심이다.',
'현금3.649B와 제한현금 포함16.763B를 구분한다. 금융부채·신용자산을 양쪽 모두 제외하지 않은 채 한쪽만 가치 가산하지 않는다. 본 모델의 owner margin은 대손·필요 금융자본 재투자 후 현금이다.',
'commerce_credit','성장과 동시에 연체·신용손실·배송보조 비용이 높아져 고객 코호트 현금회수가 약해지면 성장률만으로 보유 논지를 유지하지 않는다.',[3,4,7,8]),
'TSM':('20-F 보통주25,932,524,521주를 5로 나누어5,186.504904M ADS로 계산한다. 시세 제공업체가 보통주를 ADS처럼 계산한 시가총액을 배제한다.',
'FY25 OCF NT2,274,976M−PPE NT1,272,411M=NT1,002,565M. USD 환산은 관측된 결산표 환산율 근사이며 향후 FX는 고정 사실이 아니다.',
'해외 공장의 수익성·재투자와 대만 중심 위험은 별개다. 9% 할인율 일관 적용 후 생산중단/자산접근 제한의 영구손실을 추가한다. 정상 Bear는 지정학 파국 시나리오를 대체하지 않는다.',
'foundry_geo','주요 고객의 선단 노드 이탈·수율 경쟁력 약화 또는 대만 자산·배당 접근의 장기 제한이 발생하면 가치 가정 재작성.',[7,8]),
'CRDO':('FY26 매출1.335116B와 Q1 FY27 0.479003B, 전년Q1 0.223074B로 TTM1.591045B. Q1 GAAP 영업마진25.2%와 SBC87.979M을 함께 본다.',
'AEC·광 연결 경쟁력은 고객별 설계 채택과 전력·오류율 개선으로 입증해야 한다. 계약 상대방 43%/28%와 최종고객 28%/33%/13%/10%를 합산하지 않는다.',
'Q1 GAAP 희석194.378M주 사용. 현금·단기투자1.443286B→0.764258B, 영업권·무형자산 급증은 인수 부담이다. 조정마진48.2%를 owner margin으로 복사하지 않는다.',
'equipment_concentration','핵심 하이퍼스케일러 설계 탈락과 경쟁 광연결 전환이 동시에 발생해 높은 성장이 현금·가격결정력으로 이어지지 않으면 논지 무효.',[2,4,7,8]),
'TEM':('H1 OCF−80.802M−PPE14.327M−SBC106.827M=owner proxy−201.956M, 자본화 소프트웨어 추가 차감 전이다. Q2 순이익에는 미실현 주가이익98.5M이 포함된다.',
'진단량·데이터 계약 확장은 양질의 근거지만 인수 성장과 본업의 현금 생산성은 분리한다. 회계 흑자를 자기조달 증거로 쓰지 않는다.',
'6월 A175.200077M+B5.043789M=180.243866M. 전환약속어음187.929M은 부채로 확인. Personalis 미완료 인수는 0~50% 현금/나머지 주식 범위로 별도 스트레스하며 인수 매출을 공짜로 넣지 않는다.',
'milestone_funding','진단·데이터 성장에도 수금·SBC 차감 후 적자가 지속되고 인수/전환권리로 주당 가치가 감소하면 신규 진입 배제.',[0,1,2,4,8]),
'TMDX':('H1 OCF41.842M−PPE43.749M=−1.907M, 금융리스 원금·SBC 차감 전이다. 매출은 증가하지만 H1 영업이익은64.010M→37.033M으로 감소했다.',
'OCS와 물류 통합은 장기 보존·운송의 고객 가치를 만들지만 간 이식 집중·항공 고정비·재고 통제 문제가 경제적 규모 확대를 제한한다.',
'Q2 희석40.709227M은 기존 전환채 포함 proxy. 전환채 원금을 또 차감하지 않고 미전환 이자·금융리스 유지 현금은 margin에 반영한다. 2030년까지 HQ200~240M 투자와 6월 내부통제 미개선은 별도 검증 항목.',
'medical_logistics','OCS 채택 확대에도 임상성과·물류 단위경제가 악화하거나 재고 통제 중요취약점이 해소되지 않으면 해자 및 경영점수 하향.',[0,4,7,8]),
}

def inputs():
    result={}
    for line in HEADERS.strip().splitlines():
        t,p,shares,cash,reserve,scores=line.split('|')
        result[t]={'ticker':t,'claim_type':'estimate','currency':'KRW' if t.isdigit() else 'USD',
            'unit':'KRW trillion' if t.isdigit() else 'USD billion','price':float(p),
            'price_date':'2026-09-04','price_status':'REFERENCE_QUOTE_NOT_SYNCHRONIZED_EXECUTABLE_CLOSE',
            'price_source_note':'Session web finance quote retrieved2026-09-06, US latest reference Sept4/Sept5UTC; KR official IR/market-reference sites or preserved September4 screening snapshot. No provider market capitalization used. Source-specific checks in evidence-ledger.json; not all quotes independently exchange-audited.',
            'valuation_shares_m':float(shares),'liquidity_cash':float(cash),'minimum_cash_reserve':float(reserve),
            'quality_scores':[int(v) for v in scores.split(',')], 'required_return':.10 if t.isdigit() else .09,
            'terminal_multiple':dict(zip(('bear','base','bull'),(16,22,28))),
            'funding_issue_price_fraction':{'bear':.35,'base':.6,'bull':.85}, 'components':[]}
    for line in OPERATING.strip().splitlines():
        t,name,*parts=line.split('|');cases={}
        for k,part in zip(('bear','base','bull'),parts):
            a,b,c,d,e=map(float,part.split(','));cases[k]={'revenue_year_1':a,'growth_2_5':b,'growth_6_10':c,'owner_margin_year_1':d,'owner_margin_mature':e}
        result[t]['components']=[{'name':name,'ownership':1,'scenarios':cases}]
    for t,d in result.items():
        fact,risk,capital,family,falsifier,investigate=NOTES[t]
        d.update(financial_finding=fact,economic_risk=risk,rights_and_capital=capital,
                 model_family=family,falsifier=falsifier,investigate_veto_indices=investigate,
                 base_mature_cash_bridge=dict(zip(('economic_operating_margin_after_sbc','cash_tax_rate','da_less_all_capex_to_revenue','working_capital_cash_cost_to_revenue','interest_net_debt_service_other_claims_to_revenue'),BRIDGES[t])))
        v=BRIDGES[t];margin=v[0]*(1-v[1])+v[2]-v[3]-v[4]
        assert abs(margin-d['components'][0]['scenarios']['base']['owner_margin_mature'])<1e-9,(t,margin)
        d['cash_bridge_note']='모든 수치는 추정. 경제적 영업마진은 SBC를 포함한다. D&A−전체 현금투자에는 리스 유지 원금·자본화 개발비 등 필요한 반복 투자를 포함한다. 금융기업 운전자본에는 대손·필요 금융자본 재투자 포함. Bear/Bull은 성숙 owner margin과 초기 회수 속도를 동시 스트레스한다.'
    for t in ['000660','005930','MU']:
        d=result[t];d['terminal_multiple']={'bear':12,'base':17,'bull':22}
        for k,x in zip(('bear','base','bull'),(.65,.80,.95)):d['components'][0]['scenarios'][k]['year_2_reset']=x
    for t in ['005380','034020','267260','VRT']:
        result[t]['terminal_multiple']={'bear':12,'base':18,'bull':24}
    for t in ['ISRG','ANET','MSFT','GOOGL','VRTX']:
        result[t]['terminal_multiple']={'bear':18,'base':25,'bull':30}
    # Explicit parent-only SOTP: operating component excludes listed subs.
    result['012450']['separate_equity_value']={'bear':15.454*.55-6,'base':15.454*.8-3,'bull':15.454*.9-2}
    result['012450']['sotp_note']='Ocean 8.096+Systems 6.137+KAI1.221=15.454조원 9월4일 저장 지분 표식. 보유 지분만 평가, 본체 현금에서 자회사 이익 제외. 가치 haircut45/20/10%, 별도 순부채·지원약정6/3/2조원은 추정. 주식표식0~20조원·별도부담0~10조원 추가 민감도.'
    result['034020']['separate_equity_value']={'bear':-4,'base':0,'bull':3}
    result['034020']['sotp_note']='Bobcat/Fuel Cell 귀속 순지분가치에서 별도 순부채·지원약정을 뺀 조정 −4/0/+3조원은 미검증 시가총액을 사실로 쓰지 않기 위한 명시적 범위 추정. 본체 현금만 평가하며 연결 이익/NCI 중복 없음. 순조정 −8~+8조원 민감도.'
    # Preferred claims are costs, not both new shares and a debt deduction.
    result['GOOGL']['separate_equity_value']={k:-19 for k in ('bear','base','bull')}
    result['196170']['separate_equity_value']={'bear':-.22,'base':-.178595,'bull':-.15833}
    result['214450']['separate_equity_value']={'bear':-.28,'base':-.207259,'bull':-.207259}
    # Unclosed acquisition optionality: pay full price and require offsetting
    # incremental discounted operating value, neither cash nor target free.
    result['VRTX']['separate_equity_value']={'bear':-8.8,'base':0,'bull':4.4}
    result['207940']['separate_equity_value']={'bear':-3,'base':0,'bull':1.5}
    # Satellite absolute rollout and reinvestment cash paths; no extrapolation
    # of a tiny reported-revenue denominator into an ordinary software margin.
    ast=result['ASTS']['components'][0]['scenarios']
    paths={
      'bear':([.15,.3,.6,1,1.5,2,2.5,3,3.3,3.5],[-2,-1.8,-1.5,-1,-.7,-.4,-.1,.1,.25,.42]),
      'base':([.4,1,2,3.5,5.5,7.5,9.5,12,14,16],[-2.1,-1.5,-.8,-.1,.5,1.2,1.8,2.6,3.2,3.84]),
      'bull':([.8,2,4,7,11,15,20,25,30,35],[-2.2,-1.2,-.2,.8,2.2,3.8,5.5,7.2,9.2,11.2])}
    for k,(rev,cash) in paths.items():ast[k].update(revenue_path=rev,cash_path=cash)
    # Additional fixed investment periods, not arbitrarily removed as growth.
    result['RKLB']['annual_cash_adjustments']={'bear':[-.15,-.2,-.2,-.1,0,0,0,0,0,0], 'base':[-.15,-.15,-.1,0,0,0,0,0,0,0], 'bull':[-.2,-.2,-.1,0,0,0,0,0,0,0]}
    result['TMDX']['annual_cash_adjustments']={k:[-.045,-.045,-.045,-.045,0,0,0,0,0,0] for k in ('bear','base','bull')}
    # Distinguish public approximations from filing denominators; no invented
    # precision. All have +/- share-count stress in model outputs.
    proxies={'000660','042700','214450','267260','AVGO','LLY','MSFT','MU','PLTR','VRT','VRTX','MELI','ANET','CRDO','TMDX'}
    estimated_liquidity={'012450'}
    # Corrections after source review; retain the original raw files intact.
    result['MU']['rights_and_capital']='Q3 희석 1,145백만주를 기존 권리 proxy로 사용. 5월28일 현금24.995B 중5B 유보는 추정이며2B 미사용 한도는 현금에 더하지 않는다. 신공장 전체 Capex 이후 현금으로 투자회수 평가.'
    result['PLTR']['rights_and_capital']='공식 Q2 10-Q 희석 가중평균2,568.694백만주로 시세 역산 proxy를 교체했다. 현금2.030047B만 유동성에 인정하며, UST 포함9.2B와 기타 시장성증권 포함9.409099B의 범위 차이를 보존한다. GAAP SBC 비용 이후 현금마진을 사용한다.'
    result['PLTR']['financial_finding']='TTM 매출6.155941B. H1 공시 OCF2.115332B−PPE0.021955B−SBC0.466801B=owner proxy1.626576B. 조정 FCF보다 보수적이나 이자수익·선수금 타이밍을 추가 정상화해야 한다.'
    result['278470']['rights_and_capital']='37.438155백만주 분모, 6월 현금0.094463조원에서0.05조원 유보를 추정 적용한다. 리스부채0.084908조원과 상각후원가 금융부채0.009112조원을 총부채로 대체하지 않는다. 광고·판매 수수료·운전자본 비용 이후 주당 현금으로 판단한다.'
    result['AXON']['liquidity_note']='0.685B는 현금·단기투자 공시 반올림. 제한성 확인을 위해 0.4B 유보 가정, 원금1.75B 만기와 인수약정 별도 stress.'
    result['NET']['liquidity_note']='6월말 현금·시장성증권4.163B. 8월 사채 조달현금은 만기·캡드콜과 함께 확정 정산 전 가용현금 증가로 미반영.'
    result['196170']['economic_risk']+=' 9월2일 Novartis 옵션·라이선스 계약을 공식 확인했다. 모든 옵션·마일스톤 달성 시 최대$3.223B이며 발표상 로열티도 총액에 포함되어, 확정현금이나 총액 외 무제한 추가 로열티로 계산하지 않는다.'
    result['ISRG']['financial_finding']='첨부 10-K·Q2 10-Q를 재대조했다. TTM OCF3.7064B−PPE0.4838B=FCF3.2226B; 손익계산서 SBC0.8393B 차감 proxy2.3833B. 별도 자본화 SBC0.1348B는 재고·상각 중복 확인 전 단순 재차감하지 않으며 초기 현금마진·재투자 민감도에 반영한다.'
    # Separate operating drivers. Weights are forward analyst allocations,
    # explicitly NOT a claim that the company disclosed segment owner cash.
    splits={
      'AMZN':[('AWS',.21,.08,.03,3,2.7),('North_America',.56,-.03,-.015,.3,.65),('International',.23,-.01,0,.7,.35)],
      '005380':[('Vehicle',.77,0,0,1,.7),('Finance_after_credit_capital',.17,.02,.01,1,1.8),('Other',.06,-.01,0,1,1)],
      'AVGO':[('Semiconductor_AI_networking',.68,.04,.015,1,1.05),('Infrastructure_software',.32,-.06,-.025,1,.9)],
      'MELI':[('Commerce_logistics',.55,0,0,1,.7),('Fintech_after_losses_required_capital',.45,.02,.01,1,1.3666666667)],
      'LLY':[('GLP1',.65,.03,-.015,1,1.15),('Other_approved_products',.35,-.055,.0278571429,1,.7214285714)],
      'VRTX':[('CF_franchise',.96,-.02,-.02,1,1.03),('Approved_nonCF_launches',.04,.35,.15,1,.28)],
    }
    import copy
    for t,parts in splits.items():
        template=result[t]['components'][0];components=[]
        initial_norm=sum(w*i for _,w,_,_,i,_ in parts)
        mature_norm=sum(w*m for _,w,_,_,_,m in parts)
        for name,w,g1,g2,initial,mature in parts:
            c=copy.deepcopy(template);c['name']=name
            for s in c['scenarios'].values():
                s['revenue_year_1']*=w
                s['growth_2_5']+=g1;s['growth_6_10']+=g2
                s['owner_margin_year_1']*=initial/initial_norm
                s['owner_margin_mature']*=mature/mature_norm
            components.append(c)
        result[t]['components']=components
        result[t]['segment_assumption_note']='부문별 매출 배분·성장률·현금마진은 분석 추정이며, 연결 owner 현금의 초기 합계와 성숙 고정믹스 합계를 보존한다. 이후 믹스 변화로 연결 현금마진이 변한다. 공시하지 않은 부문 FCF를 실제치로 만들지 않았다. 공시 부문 근거는 원자료/이전 thesis, 숫자 가정은 components에 공개.'
    for t,d in result.items():
        d['share_basis_status']='DATED_OR_ROUNDED_OR_DILUTED_PROXY' if t in proxies else 'FILING_ECONOMIC_SHARE_BRIDGE'
        d['liquidity_basis_status']='CONSERVATIVE_ASSUMPTION_NOT_REPORTED_CASH' if t in estimated_liquidity else 'STORED_FILING_CASH_OR_DISCLOSED_LIQUID_SECURITIES'
        d['forecast_basis']='NEXT_12_MONTHS_FROM_2026_09_06_THEN_NINE_YEARS; not a mechanical annualisation labeled TTM'
        d['portfolio_instruction']='기업 연구 완료는 신규 매수 승인 아님. 보유·세금·위험예산 정보 없이 매매나 배분을 실행하지 않는다.'
    assert len(result)==34
    return result

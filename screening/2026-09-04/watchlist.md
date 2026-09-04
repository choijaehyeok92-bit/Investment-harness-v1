# WATCH List (18)

Screening run 2026-09-04 · US + Korea · per `agents/screener.md`

These names have a credible structural case but an unresolved question that must be
answered before deep-analyst time is justified. Per `policy/screening.yaml` none met
a screen-out condition — high multiples, prior price appreciation and current losses
are explicitly forbidden as rejection grounds. Names marked **PRIMARY GATE** in their
veto table have one question that gates all others.


## US-listed

### ANET — Arista Networks
*NYSE · confidence: MEDIUM-LOW - guidance figures corroborated; customer concentration is INFERENCE from historical disclosure, not verified for 2026*

FACT: quarterly revenue above $3.0B, +37.7% YoY; 2026 revenue guidance raised for the third time to approximately $12.6B, +40%; management describes the increase as spread across AI scale-out fabrics, scale-across routing, front-end data centre, campus and routing rather than a single category. Market cap ~$248B, forward P/E ~50.6x. INFERENCE: business quality is high and the guidance breadth is a genuine positive, but at ~50x forward the price embeds continued ethernet share gain at exactly the two customers whose free cash flow is deteriorating fastest. Held at WATCH because the expectation gap is materially thinner than NVDA or AVGO for a comparable underlying driver.

**Top 3 positive signals**

1. EOS single-binary software and CloudVision create real operational switching costs, not just hardware share
1. Guidance raised three times with breadth across product lines, reducing single-product dependence
1. Sustained share capture from Cisco in data centre switching

**Top 3 uncertainties**

1. Historic revenue concentration in Microsoft and Meta - the two hyperscalers with the sharpest FCF deterioration
1. Direct competition from NVIDIA Spectrum-X and Broadcom-enabled whitebox on both flanks
1. ~50x forward earnings requires the share-gain trend to continue uninterrupted

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `fatal_concentration` | INVESTIGATE | Two-customer concentration overlapping precisely with the macro-overlay funding risk |
| `price_requires_unrealistic_bull_case` | INVESTIGATE | ~50x forward on 40% growth leaves little margin for a capex pause |

**Research priorities**

1. Establish current customer concentration percentages and any 2026 disclosure changes
2. Reverse-engineer the ethernet-versus-InfiniBand share assumption embedded in the current price
3. Assess whitebox/Broadcom pricing pressure on gross margin

**Sources**

- <https://finance.yahoo.com/markets/stocks/articles/arista-networks-vs-broadcom-ai-111500264.html>
- <https://www.macrotrends.net/stocks/charts/ANET/arista-networks/market-cap>

---

### VRT — Vertiv Holdings
*NYSE · confidence: MEDIUM - reported figures corroborated; cause of the miss is unresolved*

FACT: Q2 2026 revenue $3.27B, +24% YoY, but BELOW consensus of $3.38B; adjusted EPS $1.52 versus $0.95 a year earlier; FY2026 guidance raised to net sales $13.8-14.2B and adjusted EPS $6.65-6.75. INFERENCE: missing revenue consensus while the end market is booming is a signal worth understanding - it points to either capacity constraint or share loss, and neither is visible from outside. Power and cooling is a real structural bottleneck, but this is an equipment business competing with Schneider, Eaton and ABB, not an IP-moat compounder, so the moat-trajectory category would score weakly today.

**Top 3 positive signals**

1. Liquid cooling at rising rack density is a genuine and durable structural bottleneck
1. Adjusted EPS +60% YoY shows real operating leverage on the installed base
1. Guidance raised despite the revenue miss, implying mix or pricing improvement

**Top 3 uncertainties**

1. Revenue missed consensus in a booming end market - cause unexplained and materially important
1. Moat is moderate: multiple credible incumbents plus new Asian entrants; limited switching costs
1. Order book is cyclical and tied to the same hyperscaler capex flagged in the macro overlay

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `moat_shrinkage` | INVESTIGATE | Revenue miss in a strong market may indicate share loss; must be distinguished from capacity constraint |
| `incremental_roic_collapse` | PASS | Margins expanding, not deteriorating |

**Research priorities**

1. Determine whether the revenue miss was capacity, timing or share - this single question gates further work
2. Establish backlog and book-to-bill trend versus Schneider and Eaton
3. Assess liquid-cooling attach rate and its margin versus legacy thermal

**Sources**

- <https://www.tikr.com/blog/vertiv-q2-earnings-missed-on-revenue>
- <https://www.investing.com/news/transcripts/earnings-call-transcript-vertiv-tops-q2-2026-eps-forecast-shares-rise-premarket-93CH-4824087>

---

### MU — Micron Technology
*NASDAQ · confidence: MEDIUM - reported and guided figures corroborated; the structural hypothesis is explicitly OPINION at this stage*

FACT: fiscal Q2 2026 revenue $23.9B, +196% YoY; non-GAAP EPS $12.20 versus $8.79 consensus; guidance for the following quarter of $33.5B revenue, non-GAAP EPS $19.15, and gross margin of approximately 81%. INFERENCE: an 81% gross margin in DRAM is a shortage rent, not a steady state. policy/investment-philosophy.md section 1 explicitly refuses to reward cyclical peaks misidentified as structural growth. Held at WATCH rather than screened out because policy/screening.yaml forbids rejection on valuation alone AND because there is a genuine, testable structural hypothesis: HBM is contracted, customised and capacity-reserved in a way commodity DRAM never was, which could durably change cycle amplitude.

**Top 3 positive signals**

1. HBM is sold on long-term contracted, customer-qualified terms - structurally different from spot DRAM
1. The one US-domiciled leading-edge memory supplier, with policy support behind domestic capacity
1. Revenue +196% YoY demonstrates the scale of the demand shift, whatever its duration

**Top 3 uncertainties**

1. 81% gross margin has no precedent in memory and cannot be extrapolated; normalised mid-cycle earnings power is the entire question
1. Capitalising peak earnings at any multiple is the classic permanent-loss mechanism in this industry
1. Capacity response from Samsung, SK hynix and Chinese suppliers is already in motion

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `incremental_roic_collapse` | INVESTIGATE | Incremental ROIC is at an unrepeatable peak; the down-cycle case must be modelled before any capital is committed |
| `price_requires_unrealistic_bull_case` | INVESTIGATE | Requires establishing whether the price capitalises peak or mid-cycle earnings |

**Research priorities**

1. Build a normalised mid-cycle earnings model and reverse-engineer which earnings level the current price capitalises - this must be done before anything else
2. Test the 'AI ends the commodity cycle' hypothesis against announced industry capacity additions through 2028
3. Separate HBM contracted revenue from conventional DRAM and NAND spot exposure

**Sources**

- <https://www.investing.com/news/company-news/micron-q2-2026-slides-ai-demand-drives-record-239b-revenue-93CH-4569530>
- <https://www.cnbc.com/2026/03/18/micron-mu-q2-earnings-report-2026.html>

---

### PLTR — Palantir Technologies
*NASDAQ · confidence: MEDIUM-HIGH on reported results; the valuation conclusion is INFERENCE requiring the formal reverse-expectations model*

FACT: Q2 2026 revenue $1.94B, +93% YoY; US commercial revenue $764M, +149% YoY; US government $809M, +90% YoY; GAAP operating margin 47%, adjusted 62%; Rule of 40 score 155%; FY2026 guidance $8.15-8.16B, +82%. Market cap $432.36B; forward P/E ~112.7x. INFERENCE: the business quality is genuinely exceptional - a 47% GAAP operating margin at 93% growth is close to unprecedented in software history. But policy/investment-philosophy.md section 2 states plainly that a high-quality company can still be a poor investment if the price requires near-perfect success, and at roughly 53x forward revenue this is the clearest instance of that condition in the screen. Held at WATCH with an explicit veto flag; the valuation gate must be resolved before deep-analyst time is spent.

**Top 3 positive signals**

1. 47% GAAP - not adjusted - operating margin at 93% growth; the operating leverage is real and already banked
1. Ontology plus forward-deployed engineering creates switching costs that are organisational, not contractual
1. US commercial +149% shows the government franchise has genuinely crossed into enterprise

**Top 3 uncertainties**

1. Forward P/E ~112.7x and roughly 53x forward revenue; to justify $432B requires something like $30-40B revenue at a 40%+ FCF margin within a decade AND a retained premium multiple
1. Government revenue is budget-appropriation dependent and politically exposed
1. Growth of this rate at this scale has few precedents to calibrate duration against

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `price_requires_unrealistic_bull_case` | INVESTIGATE | PRIMARY GATE. The reverse-engineering step in policy/scorecard.yaml must be completed first; if the price requires bull-case-or-better execution this becomes a REJECT regardless of business quality |
| `persistent_dilution` | INVESTIGATE | Historic SBC intensity; share count trend must be established |

**Research priorities**

1. Complete the mandatory reverse-expectations test before any other work: what revenue, margin and duration does $432B require?
2. Establish diluted share count trend and SBC as a percentage of revenue over five years
3. Separate durable enterprise ARR from consumption-style AIP bootcamp conversions

**Sources**

- <https://www.businesswire.com/news/home/20260802523449/en/Palantir-Reports-Q2-2026-U.S.-Comm-Revenue-Growth-of-149-YY-and-Revenue-Growth-of-93-YY-Raises-FY-2026-Revenue-Guidance-to-82-YY-Growth-and-U.S.-Comm-Revenue-Guidance-to-134-YY-Crushing-Consensus-Expectations>
- <https://www.cnbc.com/2026/08/03/palantir-pltr-earnings-q2-2026.html>
- <https://www.macrotrends.net/stocks/charts/PLTR/palantir-technologies/market-cap>

---

### MSFT — Microsoft
*NASDAQ · confidence: MEDIUM-LOW - capex guidance corroborated; the FCF decline figure is a broker ESTIMATE, not a company disclosure*

FACT: 2026 capex guided near $190B; Barclays estimates free cash flow declines 28% this year before recovering in 2027. INFERENCE: business quality and moat are not in question, but the strategy's primary metric - FCF per share - is going backwards while the return on the incremental capital is unproven, and the economics of the OpenAI relationship are not transparent enough to underwrite. Held at WATCH pending evidence that Azure AI revenue converts the capex into incremental ROIC rather than absorbing it.

**Top 3 positive signals**

1. Enterprise distribution and Office/Windows switching costs remain among the most durable moats in the market
1. Azure AI provides a directly measurable revenue line against which capex can eventually be tested
1. Fortress balance sheet - no external financing dependence even at $190B capex

**Top 3 uncertainties**

1. FCF per share compressing sharply; depreciation from the 2025-2026 build has not yet reached the income statement
1. OpenAI relationship economics - revenue share, compute commitments, equity accounting - are materially opaque
1. No clearly identified expectation gap at current price

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `incremental_roic_collapse` | INVESTIGATE | Capital intensity has structurally stepped up; incremental ROIC unproven |
| `external_capital_dependence` | PASS | Self-funded |

**Research priorities**

1. Model the 2027-2029 depreciation schedule against the FCF-per-share recovery path
2. Establish the OpenAI arrangement's cash economics as far as disclosure allows
3. Identify whether any expectation gap exists at all before committing deep-analyst time

**Sources**

- <https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html>
- <https://valueaddvc.com/blog/ai-hyperscaler-capex-compared-why-microsoft-google-meta-and-amazon-are-all-spending-at-once>

---

### AMZN — Amazon
*NASDAQ · confidence: MEDIUM-LOW - capex and FCF direction corroborated; segment separation not performed in this run*

FACT: 2026 capex guided at roughly $200B, the largest single spender among the hyperscalers; free cash flow projected to turn negative this year. INFERENCE: the retail margin expansion and AWS reacceleration are real, but with FCF negative the strategy's central test - is long-term FCF per share increasing - cannot currently be answered from reported figures. That is a reason to hold at WATCH and demand evidence, not a reason to reject.

**Top 3 positive signals**

1. Retail operating margin expansion from regionalised fulfilment is a durable structural gain independent of AI
1. AWS reacceleration plus Trainium gives partial vertical integration on AI capex
1. Advertising is a high-incremental-margin business attached to the retail moat at near-zero marginal cost

**Top 3 uncertainties**

1. Negative FCF makes the FCF-per-share path unverifiable for now
1. Trainium's competitiveness against merchant GPUs is unproven at scale
1. $200B of annual capex implies a depreciation burden that will suppress reported earnings for years

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `incremental_roic_collapse` | INVESTIGATE | Largest absolute capex commitment in the screen against unproven incremental returns |
| `low_quality_growth` | PASS | Growth is customer-value-driven, not subsidy-driven |

**Research priorities**

1. Separate retail FCF from AWS capex to establish whether underlying per-share cash generation is improving
2. Assess Trainium adoption and unit economics versus merchant silicon
3. Model the depreciation schedule against consensus earnings

**Sources**

- <https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html>
- <https://epoch.ai/data-insights/hyperscaler-capex-vs-cash-flow>

---

### META — Meta Platforms
*NASDAQ · confidence: MEDIUM-LOW - capex guidance and direction corroborated; the 91% cash-generation figure is press-sourced*

FACT: 2026 capex guidance raised to $125-145B from $115-135B, with the company explicitly citing memory pricing; cash generation fell 91% YoY. INFERENCE: on the strategy's own criteria this is the weakest of the four hyperscalers. Capex was raised because an input supplier is capturing the rent, there is no revenue line attached to the superintelligence spend, and cash generation has collapsed. The advertising moat remains excellent, which is why this is WATCH and not a rejection - but the reinvestment-economics category would score poorly on current evidence.

**Top 3 positive signals**

1. Core advertising business retains exceptional unit economics and pricing power across a 3bn+ user base
1. Ranking and ads-ranking AI improvements have a directly measurable revenue return, unlike the frontier-model spend
1. No external financing dependence

**Top 3 uncertainties**

1. Capex raised specifically because of memory input cost - value is transferring to suppliers, which is the inverse of the pattern the strategy looks for
1. Cash generation down 91% YoY; FCF per share sharply negative in direction
1. Superintelligence/Reality Labs spend has no attached revenue line and no stated ROIC test

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `incremental_roic_collapse` | INVESTIGATE | Large capital commitment with no disclosed return test; cash generation collapsed 91% YoY |
| `management_or_accounting_integrity` | PASS | No integrity concern identified; the issue is capital allocation judgement, scored separately |

**Research priorities**

1. Separate ads-ranking AI spend (measurable return) from frontier-model and Reality Labs spend (no return test) and evaluate each on its own
2. Establish the FCF-per-share trajectory through the depreciation wave
3. Review the historical record of large discretionary capital commitments as a capital-allocation input

**Sources**

- <https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html>
- <https://valueaddvc.com/blog/ai-hyperscaler-capex-compared-why-microsoft-google-meta-and-amazon-are-all-spending-at-once>

---

### MELI — MercadoLibre
*NASDAQ · confidence: MEDIUM - reported figures corroborated across two sources; credit-book detail not examined*

FACT: Q2 2026 net revenues and financial income $10,169M, +50% YoY; gross margin 40.9%, down 4.7pp YoY; income from operations $683M, DOWN 17% YoY; operating margin 6.7%; net margin 4.6%, down 3.1pp. INFERENCE: revenue +50% with operating income -17% is exactly the pattern policy/screening.yaml flags for investigation rather than rejection - it is either deliberate reinvestment into logistics, credit and share defence, or genuine unit-economics erosion, and the two cannot be distinguished from the headline. Because 'revenue' here includes financial income from a credit book, the quality of that growth depends on non-performing loans and provisioning, which must be examined before any conclusion.

**Top 3 positive signals**

1. Structural: Latin American ecommerce and fintech penetration remains well below developed-market levels
1. Logistics network and Mercado Pago create a genuine two-sided moat that is very expensive to replicate
1. 50% top-line growth at this scale is rare and indicates the market is still expanding, not saturating

**Top 3 uncertainties**

1. Operating income fell 17% while revenue grew 50% - reinvestment or margin erosion cannot be distinguished from outside
1. Financial income is credit-book revenue; NPL and provisioning trends determine whether this growth is real
1. Competitive intensity from Shopee and Amazon in Brazil and Mexico

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `low_quality_growth` | INVESTIGATE | Gross margin -4.7pp and operating income -17% alongside +50% revenue; must establish whether unit economics are worsening |
| `external_capital_dependence` | INVESTIGATE | A growing credit book requires funding; the funding structure must be established |

**Research priorities**

1. Analyse the credit portfolio: NPL formation, provisioning coverage, and funding mix - this gates everything else
2. Decompose the gross margin decline into logistics investment, credit provisioning and price competition
3. Establish whether the operating income decline is a deliberate, reversible investment decision

**Sources**

- <https://www.stocktitan.net/sec-filings/MELI/8-k-mercadolibre-inc-reports-material-event-d73e8904e674.html>
- <https://sergeycyw.substack.com/p/mercadolibre-applovin-axon-earnings>

---

### ASTS — AST SpaceMobile
*NASDAQ · confidence: MEDIUM on reported figures; LOW on the survivability assessment, which is the decisive category*

FACT: Q2 2026 revenue $31.5M, more than doubling sequentially on gateway deliveries and US government contract milestones, but below the $34.5M consensus; FY2026 revenue guidance held at $150-200M and described as weighted toward Q4; net loss widened, reported at $0.77 per share, with a BB7 satellite incident cited. INFERENCE: the structural case - direct-to-device connectivity from space with mobile network operator partners - is genuine and the thesis is testable, which is why this is not screened out. But constellation construction requires continuous external financing, which is a named Hard Veto condition, and policy/scorecard.yaml permits a loss-making company only where the path to profitability and the runway without external capital are clear. Neither is currently established.

**Top 3 positive signals**

1. Direct-to-device from space is a genuine category creation with no incumbent to displace
1. Mobile network operator partnerships provide distribution without customer-acquisition spend
1. Government contract milestones give a non-dilutive revenue source ahead of commercial scale

**Top 3 uncertainties**

1. Constellation buildout requires sustained external capital - the runway to self-funding is not established
1. BB7 incident indicates hardware execution risk on a programme where each satellite is capital-intensive
1. FY guidance is heavily Q4-weighted, concentrating execution risk into a single quarter

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `external_capital_dependence` | INVESTIGATE | PRIMARY GATE. Structurally dependent on external financing until the constellation generates cash; must be resolved before anything else |
| `permanent_loss_probability` | INVESTIGATE | Pre-scale capital-intensive hardware; permanent-loss probability is material and must be sized |

**Research priorities**

1. Establish cash runway, committed financing and the number of satellites required to reach cash-flow breakeven - the gating question
2. Assess the BB7 incident's root cause and its read-through to the manufacturing programme
3. Convert MNO agreements into contracted, quantified revenue commitments rather than announcements

**Sources**

- <https://www.investing.com/news/company-news/ast-spacemobile-reports-q2-revenue-of-315-million-93CH-4850283>
- <https://qz.com/ast-spacemobile-q2-2026-earnings-revenue-guidance-081126>

---

### RKLB — Rocket Lab
*NASDAQ · confidence: MEDIUM on reported figures; the Neutron outcome is explicitly unknowable and must be handled as scenario probability, not estimate*

FACT: Q2 2026 revenue $234M, +62% YoY, ahead of the $231.6M FactSet consensus; backlog $2.36B, +137% YoY; loss widened. INFERENCE: backlog growing 137% YoY is a strong forward indicator and the thesis has an unusually clean falsifier - Neutron's first flight and subsequent cadence. If Neutron works, Rocket Lab becomes the only credible Western medium-lift alternative to SpaceX; if it does not, it remains a small-launch and space-systems components business at a fraction of the implied value. Held at WATCH pending that binary, and because the company is still loss-making and issuing equity.

**Top 3 positive signals**

1. Backlog +137% YoY - contracted demand growing far faster than recognised revenue
1. Space Systems components business provides revenue diversification away from launch cadence
1. Neutron represents genuine asymmetry: a binary with a large, identifiable payoff

**Top 3 uncertainties**

1. Neutron is unflown; schedule slippage is the norm in launch and the value is concentrated in this outcome
1. Still loss-making with widening losses and continued equity issuance
1. SpaceX cost curve sets the competitive benchmark and continues to fall

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `external_capital_dependence` | INVESTIGATE | Loss-making with ongoing equity issuance; runway to self-funding not established |
| `persistent_dilution` | INVESTIGATE | Share count trend must be established over the Neutron development period |

**Research priorities**

1. Establish cash runway through Neutron first flight plus a realistic slip allowance
2. Decompose backlog into launch versus Space Systems and assess margin by category
3. Define the explicit Neutron falsifier - date and cadence thresholds - before, not after, taking a position

**Sources**

- <https://qz.com/rocket-lab-q2-2026-earnings-revenue-record-loss-081126>

---

## Korea-listed

### 000660 — SK hynix / SK하이닉스
*KOSPI · confidence: MEDIUM-HIGH on the reported figures and the share data (multiple independent sources); the cause of the share loss is entirely unresolved*

FACT: Q2 2026 revenue KRW 79.32T (+256.8% YoY) and operating profit KRW 60.54T (+557.2% YoY), an all-time high operating margin of 76%, up 4pp QoQ; net profit KRW 93.92T; H1 revenue exceeded KRW 100T for the first time. FACT: HBM market share fell from 64% a year earlier to 50%, while Samsung rose from 21% in Q1 to 33% in Q2. FACT: the shares fell on the print despite record results, and P/B has begun breaking above its historical upper range. INFERENCE: this is the single most important finding in the run. Record peak profitability, falling market share, and an all-time-high price-to-book are occurring simultaneously. policy/monitoring.yaml names 'moat trajectory turns from strengthening to weakening' as a sell-review trigger, and policy/investment-philosophy.md section 3 makes moat direction - not moat level - the governing question. A 76% operating margin is a shortage rent that cannot be capitalised. Held at WATCH, not screened out: one quarter of share loss is not proof of structural moat contraction, and 50% share is still first place.

**Top 3 positive signals**

1. Still the HBM market leader at 50% share with the deepest customer qualification history
1. 76% operating margin and KRW 100T+ H1 revenue give enormous balance-sheet capacity to fund the next node transition
1. HBM's contracted, customer-qualified structure is genuinely different from commodity DRAM and may dampen cycle amplitude

**Top 3 uncertainties**

1. HBM share fell 64% to 50% YoY while Samsung went 21% to 33% - this is measured share loss, not inferred, and it is the central question
1. 76% operating margin is an unrepeatable peak; normalised mid-cycle earnings power is unknown and must be modelled
1. Net profit (KRW 93.9T) exceeds operating profit (KRW 60.5T), implying large non-operating items that must be identified and excluded before any earnings power is capitalised

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `moat_shrinkage` | INVESTIGATE | PRIMARY GATE. Measured HBM share contraction from 64% to 50% while a direct competitor gained 12pp in one quarter. Must be resolved before any capital is committed |
| `price_requires_unrealistic_bull_case` | INVESTIGATE | P/B breaking above the historical upper range on peak-of-peak margins |
| `incremental_roic_collapse` | INVESTIGATE | Incremental ROIC is at an unrepeatable peak; the down-cycle case must be modelled |

**Research priorities**

1. Determine whether the 64% to 50% share decline is allocation-driven (customers deliberately dual-sourcing) or technology-driven (Samsung's HBM4 closing the gap) - these have opposite thesis implications and this is the gating question
2. Identify the non-operating items making net profit exceed operating profit and exclude them from any earnings power estimate
3. Model normalised mid-cycle earnings and reverse-engineer which earnings level the record P/B capitalises

**Sources**

- <https://news.skhynix.co.kr/q2-2026-business-results/>
- <https://www.investing.com/news/company-news/sk-hynix-q2-2026-slides-record-revenue-76-operating-margin-93CH-4818489>
- <https://www.cnbc.com/2026/07/29/sk-hynix-earnings-profit-revenue-hbm-memory.html>
- <https://korea.counterpointresearch.com/global-hbm-market-share-q2-2026/>
- <https://www.businesspost.co.kr/BP?command=article_view&num=446371>

---

### 042700 — Hanmi Semiconductor / 한미반도체
*KOSPI · confidence: MEDIUM - quarterly figures and share data are press-corroborated; the hybrid bonding assessment is not yet performed and is the decisive item*

FACT: Q2 2026 revenue KRW 251.1B (a company record) and operating profit KRW 130.3B, +51.0%, with an all-time-high operating margin of 51.9%. Global TC bonder share 71.2% (first place); Hanwha Semitech 3.2% (fifth). HBM5 and HBM6 equipment announced. FACT: an earlier 2026 quarter produced an operating profit of only about KRW 8.5B against a roughly KRW 35T market capitalisation - the earnings are extraordinarily lumpy. INFERENCE: dominant share in a genuine bottleneck tool, but a 51.9% operating margin in capital equipment is an open invitation to entry, and the real risk is not competitive share loss at HBM4 - it is the hybrid bonding transition, which could reset incumbency entirely at HBM5/HBM6. That is a clean, testable falsifier and the reason this is WATCH rather than SCREEN_IN.

**Top 3 positive signals**

1. 71.2% share of a bottleneck tool required for every HBM stack shipped
1. 51.9% operating margin demonstrates real pricing power within the current technology generation
1. Announced HBM5/HBM6 roadmap indicates the company is contesting the next transition rather than harvesting

**Top 3 uncertainties**

1. Quarterly earnings swing from roughly KRW 8.5B to KRW 130B in operating profit - order lumpiness makes any single quarter a poor basis for valuation
1. Hybrid bonding could displace thermal compression bonding at HBM5/HBM6 and reset the incumbency entirely
1. Customer base is effectively three memory makers; Hanwha Semitech is a well-funded domestic challenger with an obvious captive-customer path

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `fatal_concentration` | INVESTIGATE | Single product family sold to three customers; both dimensions of concentration are severe |
| `moat_shrinkage` | INVESTIGATE | The hybrid bonding technology transition is the key risk, not conventional share competition |

**Research priorities**

1. Assess the hybrid bonding roadmap and whether Hanmi's TC bonder franchise survives the HBM5/HBM6 transition - this single question gates the thesis
2. Normalise earnings across the full order cycle rather than off a peak quarter
3. Establish customer concentration and whether Hanwha Semitech has a captive path into Samsung

**Sources**

- <https://zdnet.co.kr/view/?no=20260714105543>
- <https://www.newsway.co.kr/news/view?ud=2026030415023165910>
- <https://www.fnnews.com/news/202607141114562271>

---

### 042660 — Hanwha Ocean / 한화오션
*KOSPI · confidence: LOW-MEDIUM - backlog and the NGLS award are corroborated; no margin or return data established in this run*

FACT: order backlog $33.7B as of end-June 2026; won the concept design contract for the US Next Generation Logistics Ship (NGLS) programme through a partnership with VARD, described as the first substantive MASGA-related result; 2026 characterised as the year in which 2025's order intake converts to revenue and profit. INFERENCE: the structural driver is credible - the US naval industrial base is capacity-constrained and Korea is the only allied country with meaningful surplus capacity, and MASGA is a policy framework with a decade-scale horizon rather than a trade headline. The reason this is WATCH and not SCREEN_IN is that shipbuilding has historically been among the worst industries in the world for incremental return on capital, and the harness's central test is incremental ROIC and FCF per share, which Korean shipbuilders have never demonstrated through a full cycle.

**Top 3 positive signals**

1. $33.7B backlog provides multi-year revenue visibility
1. MASGA has produced a concrete first contract (NGLS concept design) rather than remaining a policy aspiration
1. US naval and commercial capacity shortage is a structural, policy-backed, decade-scale driver

**Top 3 uncertainties**

1. Shipbuilding's historical incremental ROIC is poor; nothing yet proves this cycle is structurally different
1. Fixed-price long-cycle contracts carry steel, labour and FX risk that can consume the entire margin
1. Whether MASGA yields US-yard equity economics or merely low-margin subcontracting is undetermined and materially changes the thesis

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `incremental_roic_collapse` | INVESTIGATE | The industry's structural weakness; must be tested against this cycle's contract terms, not assumed away |
| `low_quality_growth` | INVESTIGATE | Backlog growth is meaningless if won at prices that do not cover the cost of capital |

**Research priorities**

1. Establish contract margin structure: fixed price versus escalation clauses, steel and FX hedging, and labour cost assumptions
2. Determine whether MASGA participation gives equity economics in US yards or subcontract margins - this changes the thesis entirely
3. Compute realised incremental ROIC on the current backlog vintage versus the prior cycle

**Sources**

- <https://www.shippingnewsnet.com/news/articleView.html?idxno=69948>
- <https://www.ddaily.co.kr/page/view/2026073114223050968>

---

### 009540 — HD Korea Shipbuilding & Offshore / HD한국조선해양
*KOSPI · confidence: LOW-MEDIUM - order figures corroborated; no margin or return data established in this run*

FACT: H1 2026 shipbuilding orders of $16.38B across the shipbuilding subsidiaries, reaching 96% of the full-year target by mid-year. INFERENCE: the same structural case and the same structural objection as Hanwha Ocean. Reaching 96% of an annual order target in six months is genuine evidence of a demand shortage in a capacity-constrained industry, and LNG carriers and high-value vessels carry better economics than the commodity segments that destroyed returns in prior cycles. But the incremental ROIC question is unresolved for this industry as a whole, so the verdict follows the sector rather than the headline.

**Top 3 positive signals**

1. 96% of the annual order target achieved in H1 - demand evidence in hand rather than forecast
1. High-value vessel mix (LNG carriers, dual-fuel) carries materially better economics than prior-cycle commodity orders
1. Selectivity is now possible: a full order book allows price discipline rather than volume chasing

**Top 3 uncertainties**

1. Same industry-level incremental ROIC objection as the rest of Korean shipbuilding
1. Holding company structure complicates per-share value attribution across subsidiaries
1. Order pricing discipline through the remainder of the cycle is unproven

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `incremental_roic_collapse` | INVESTIGATE | Industry-level structural weakness in returns on capital; must be tested against this vintage's contract prices |
| `fatal_concentration` | PASS | Diversified across vessel types and customers |

**Research priorities**

1. Compute realised gross margin by order vintage to establish whether pricing discipline is holding
2. Assess the holding company discount and per-share value attribution across the shipbuilding subsidiaries
3. Compare incremental ROIC on this cycle's backlog against the 2007-2008 cycle as the base-rate check

**Sources**

- <https://www.ddaily.co.kr/page/view/2026073114223050968>
- <https://kidd.co.kr/news/241025>

---

### 196170 — Alteogen / 알테오젠
*KOSDAQ · confidence: MEDIUM-LOW - market capitalisation and cumulative licensing figures are press-sourced; per-contract royalty terms are largely undisclosed*

FACT: market capitalisation KRW 29.96T with the share price in the KRW 560,000 range; the ALT-B4 platform converts intravenous administration to subcutaneous and has generated cumulative licensing agreements exceeding KRW 10T. INFERENCE: a platform royalty model is close to the ideal reinvestment profile under this strategy - near-zero incremental capital with very high incremental ROIC if royalties materialise. The expectation-gap work here is unusually tractable because royalty economics can be modelled off named partner products. The reason for WATCH is that KRW 30T already capitalises a great deal of royalty before peak sales, and the entire enterprise rests on one platform and largely one molecule family.

**Top 3 positive signals**

1. Royalty model requires almost no incremental capital, so incremental ROIC is structurally very high
1. Cumulative licensing above KRW 10T is repeated third-party validation by counterparties who did their own diligence
1. Expectation gap is unusually modellable - royalty rates against named partner product forecasts

**Top 3 uncertainties**

1. Single-platform, largely single-molecule-family concentration
1. Patent position versus Halozyme's ENHANZE is a live litigation and freedom-to-operate risk
1. KRW 30T market capitalisation ahead of peak royalties requires the reverse-expectations test before anything else

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `fatal_concentration` | INVESTIGATE | One platform, one dominant partner programme; a single adverse patent or clinical outcome is thesis-ending |
| `price_requires_unrealistic_bull_case` | INVESTIGATE | Must establish what royalty stream and duration KRW 30T requires |

**Research priorities**

1. Build the royalty model off named partner products and reverse-engineer what KRW 30T requires - do this first
2. Assess the patent position and litigation exposure versus Halozyme
3. Establish the contracted royalty rate range and duration per agreement as far as disclosure permits

**Sources**

- <https://www.biotimes.co.kr/news/articleView.html?idxno=25443>
- <https://comp.wisereport.co.kr/company/c1010001.aspx?cmp_cd=196170>

---

### 141080 — LigaChem Biosciences / 리가켐바이오
*KOSDAQ · confidence: MEDIUM-LOW - market capitalisation and P&L figures are press-sourced; the cash and runway position is not established and is the decisive item*

FACT: market capitalisation KRW 4.57T; more than ten out-licensing agreements based on antibody-drug conjugate technology with cumulative value above KRW 10T; most recent full-year revenue KRW 141.6B with an operating loss of KRW 106.5B. INFERENCE: more than ten separate licensing deals is strong external validation - multiple independent counterparties have each underwritten the platform with their own money, which is exactly the kind of third-party evidence the strategy values over narrative. But policy/scorecard.yaml permits a loss-making company only where the path to profitability AND the runway without external capital are clear, and neither is currently established.

**Top 3 positive signals**

1. Ten-plus licensing agreements from independent counterparties - repeated external validation of platform quality
1. ADC is a genuinely expanding therapeutic modality with durable structural growth
1. Royalty and milestone economics require little incremental capital once deals are signed

**Top 3 uncertainties**

1. Operating loss of KRW 106.5B against revenue of KRW 141.6B; runway and financing needs are not established
1. Milestone revenue is lumpy and event-driven, making any single year a poor guide
1. Clinical readouts on the lead programmes are binary and outside management's control

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `external_capital_dependence` | INVESTIGATE | PRIMARY GATE. Sustained operating losses; must establish whether milestones fund operations without equity issuance |
| `persistent_dilution` | INVESTIGATE | Share count trend through the loss-making period must be quantified |

**Research priorities**

1. Establish cash runway and the milestone schedule to test whether the company reaches self-funding without issuing equity - this gates everything
2. Map lead programme readouts and their registrational timelines against the cash runway
3. Quantify multi-year dilution to date and its effect on per-share royalty economics

**Sources**

- <https://www.medicaltimes.com/Mobile/News/NewsView.html?ID=1167672>
- <https://www.biotimes.co.kr/news/articleView.html?idxno=25443>

---

### 035420 — NAVER / 네이버
*KOSPI · confidence: MEDIUM - quarterly figures from company IR release via corroborated coverage; the moat assessment is INFERENCE requiring evidence*

FACT: Q2 2026 revenue KRW 3,388.8B, +16.2% YoY, on strength in advertising and commerce with AI integration plus global C2C growth; consolidated operating profit KRW 520.3B, DOWN 0.2% YoY, attributed to AI infrastructure investment. INFERENCE: the company is spending its entire incremental gross profit on AI infrastructure. That is not automatically bad - it is an incremental-ROIC question. The harder issue is moat trajectory: generative AI interfaces are the most direct structural threat that exists to a search-advertising moat, and NAVER is a domestic-scale player funding a global-scale arms race. Held at WATCH because policy/screening.yaml permits screen-out only on five narrow conditions and NAVER meets none of them - it has clear customer value, a structural growth path and no survival question - but the moat-trajectory category is the central unresolved risk.

**Top 3 positive signals**

1. Korean search, commerce and payments form a defensible domestic position with genuine local data advantages
1. Revenue +16.2% shows the core franchise is still growing despite the AI narrative overhang
1. Global C2C (Poshmark and related) provides a growth avenue outside the domestic search moat

**Top 3 uncertainties**

1. Operating profit flat while revenue grew 16.2% - the entire incremental gross profit is being consumed by AI infrastructure with no disclosed return test
1. Generative interfaces are a direct structural threat to query monetisation, and moat trajectory is at best uncertain
1. Domestic scale against global AI capex budgets is a structural disadvantage in this specific arms race

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `moat_shrinkage` | INVESTIGATE | PRIMARY GATE. Search-advertising moat trajectory under generative interfaces must be measured, not assumed |
| `incremental_roic_collapse` | INVESTIGATE | AI infrastructure spend is absorbing all incremental gross profit with no disclosed return test |

**Research priorities**

1. Find measurable evidence on Korean search query share and time-on-platform versus generative alternatives - the decisive moat-trajectory falsifier
2. Establish the AI infrastructure spending plan and any stated return criteria
3. Value commerce, fintech and C2C separately from search to determine how much of the market capitalisation depends on the threatened asset

**Sources**

- <https://navercorp.com/media/pressReleasesDetail?seq=10034577>
- <https://www.newspim.com/news/view/20260807000069>

---

### 259960 — Krafton / 크래프톤
*KOSPI · confidence: MEDIUM - quarterly and half-year figures are from company disclosure via corroborated coverage; revenue mix by title is not disclosed at the needed granularity*

FACT: Q2 2026 revenue KRW 1,290.2B (+94.9% YoY) and operating profit KRW 410.9B (+67.0% YoY), both records for a second quarter; H1 revenue KRW 2,661.6B, a record, with H1 revenue up 73%; the company overtook Nexon; Subnautica-franchise contribution cited. INFERENCE: PUBG's longevity is genuinely remarkable - a 2017 title still growing nearly a decade later demonstrates a real live-service community moat - and India (BGMI) is a structural market rather than a mature one. But +95% revenue growth concentrated in one legacy franchise plus one new title is not self-evidently durable, and a live-service community is a moat that can erode quickly and without warning. Concentration is the gating issue.

**Top 3 positive signals**

1. PUBG still growing nine years after launch - unusual and genuine evidence of a durable live-service moat
1. India (BGMI) is a structurally expanding market with a large young mobile-first population
1. Operating profit +67% YoY confirms the growth carries real incremental margin

**Top 3 uncertainties**

1. Revenue concentration in the PUBG franchise is severe; the ex-PUBG business must be sized before any conclusion
1. Part of 2026 growth may be a new-title launch pull-forward rather than a durable run-rate
1. Indian regulatory risk on gaming has already caused one service interruption historically

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `fatal_concentration` | INVESTIGATE | PRIMARY GATE. Single-franchise dependence; must be quantified as a share of revenue and profit |
| `low_quality_growth` | PASS | Growth carries expanding operating margin, indicating genuine engagement rather than marketing-bought revenue |

**Research priorities**

1. Decompose revenue by title and geography to size the ex-PUBG business and separate launch pull-forward from run-rate
2. Assess Indian regulatory risk and the historical precedent for service interruption
3. Evaluate the studio-portfolio strategy's hit rate as the reinvestment-economics test - is capital being deployed into repeatable outcomes or lottery tickets?

**Sources**

- <https://www.viva100.com/article/20260729501128>
- <https://www.etoday.co.kr/news/view/2614708>
- <https://www.inven.co.kr/webzine/news/?news=318975>

---

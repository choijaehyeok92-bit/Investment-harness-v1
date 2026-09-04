# SCREEN_IN Candidates (14)

Screening run 2026-09-04 · US + Korea · per `agents/screener.md`

These names survived the screen and are cleared for `agents/deep-analyst.md`.
SCREEN_IN means *deserves deeper research*, not *buy*. Every one still carries at
least one Hard Veto flag at `INVESTIGATE`, and `Hard Veto > Score` applies at the
next stage. Ranked deep-work order is in `README.md`.


## US-listed

### NVDA — NVIDIA
*NASDAQ · confidence: MEDIUM - figures are as-reported and widely corroborated, but not verified against the 10-Q (sec.gov egress-blocked in this environment)*

FACT: Q2 FY2027 (qtr ended 2026-07-26) revenue $96.2B, +106% YoY and +18% QoQ; Data Center $89B, +117% YoY, 92% of revenue; Q3 guided to $108B assuming zero China Data Center compute revenue. Market cap ~$5,240B (2026-09-01), forward P/E ~24x. INFERENCE: at ~24x forward the price does not require bull-case execution - it requires the current demand base to persist. The binding question is duration of the AI capex cycle, not the multiple, which is exactly a deep-analyst question rather than a screening rejection.

**Top 3 positive signals**

1. Defines the accelerated-computing standard (CUDA, NVLink, rack-scale systems); driving structural change rather than benefiting from it
1. Extremely high incremental ROIC - revenue doubled YoY without a proportional capital base
1. Forward P/E ~24x on a doubling business implies the market already discounts a demand normalisation

**Top 3 uncertainties**

1. Customer concentration: hyperscale $48.7B + ACIE $40.3B in one quarter across a handful of buyers whose own FCF is deteriorating
1. Custom ASIC substitution (Broadcom/OpenAI 10GW programme, Google TPU) attacks share at the margin
1. Guidance already excludes China Data Center compute - upside optionality, but also evidence of a closed market

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `fatal_concentration` | INVESTIGATE | Revenue depends on a small number of hyperscale and AI-lab buyers funded by capex that now exceeds their operating cash flow |
| `price_requires_unrealistic_bull_case` | PASS | ~24x forward earnings does not embed bull-case-or-better execution |

**Research priorities**

1. Reverse-engineer what duration of $100B+/quarter Data Center revenue the current price requires
2. Quantify revenue exposure to customers whose AI spend is debt- or private-credit-financed
3. Track custom-ASIC share of total accelerator TAM as the primary moat-trajectory falsifier

**Sources**

- <https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm>
- <https://www.investing.com/news/company-news/nvidia-q2-fy27-slides-revenue-doubles-to-96b-data-center-surges-93CH-4878041>
- <https://www.macrotrends.net/stocks/charts/NVDA/nvidia/market-cap>

---

### AVGO — Broadcom
*NASDAQ · confidence: MEDIUM-LOW - deal terms are press-sourced; no primary contract disclosure reviewed*

FACT: custom AI ASIC revenue +140%, AI networking revenue +60%; 10GW AI accelerator and networking agreement with OpenAI with lifetime value stated above $100B, deliveries beginning H2 2026 through 2029; company targets >$100B AI semiconductor revenue by FY2027. Market cap ~$1.699T, forward P/E ~32.9x. INFERENCE: custom silicon is the hyperscalers' structural hedge against merchant GPU pricing, so Broadcom participates whether or not NVIDIA holds accelerator share - a genuinely differentiated position rather than a correlated proxy.

**Top 3 positive signals**

1. Wins on both sides of the merchant-vs-custom silicon question; not a levered NVIDIA proxy
1. Tomahawk/Jericho networking plus packaging and IP relationships create decade-long design-win lock-in
1. VMware provides a high-margin software annuity that funds semiconductor R&D - unusual reinvestment structure

**Top 3 uncertainties**

1. XPU revenue concentrated in roughly three to five customers
1. OpenAI is a large counterparty of uncertain credit standing; contract economics and prepayment structure are not public
1. Stated FY2027 AI revenue target is company guidance (ESTIMATE), not booked backlog

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `fatal_concentration` | INVESTIGATE | Custom accelerator revenue concentrated in very few programmes; one counterparty is not an investment-grade corporate |
| `external_capital_dependence` | PASS | Self-funding; VMware cash flow covers R&D |

**Research priorities**

1. Establish OpenAI contract structure: prepayments, take-or-pay, cancellation terms, revenue recognition
2. Separate booked backlog from guided AI revenue in the FY2027 $100B target
3. Assess VMware software margin durability as licence conversions complete

**Sources**

- <https://www.investing.com/analysis/broadcom-expands-ai-position-as-custom-silicon-and-vmware-boost-growth-200671389>
- <https://finance.yahoo.com/quote/AVGO/>

---

### TSM — Taiwan Semiconductor Manufacturing (ADR)
*NYSE · confidence: MEDIUM - IR-sourced quarterly figures; investor.tsmc.com not directly fetched*

FACT: Q2 2026 revenue NT$1,270.38B (US$40.20B), +36% YoY and +12% QoQ; advanced nodes 7nm and below were 77% of wafer revenue; HPC platform +20% QoQ and 66% of total revenue; full-year 2026 revenue growth outlook raised to slightly above +40% YoY in USD. INFERENCE: this is the most defensible moat in the AI complex - a near-monopoly on leading-edge logic now exercising pricing power - and the one credible permanent-loss scenario is geopolitical rather than commercial, which is precisely why a discount exists to underwrite.

**Top 3 positive signals**

1. Effective monopoly at leading edge; every merchant and custom AI accelerator in this screen depends on it
1. Pricing power now being exercised - margin expanding alongside a heavy N2 capex ramp
1. Rising incremental ROIC despite record capex, the opposite of the hyperscaler pattern

**Top 3 uncertainties**

1. Taiwan geopolitical exposure is a genuine permanent-loss scenario that cannot be modelled with confidence
1. Overseas fab (Arizona, Japan, Germany) margin dilution during ramp
1. Customer concentration in a handful of AI and smartphone platform buyers

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `fatal_concentration` | INVESTIGATE | Geographic/geopolitical single-point dependence, not commercial concentration; must be sized as a permanent-loss probability, not ignored |
| `price_requires_unrealistic_bull_case` | PASS | Trades at a persistent discount to US-listed AI peers |

**Research priorities**

1. Size the geopolitical permanent-loss case explicitly as a probability-weighted scenario, per the power-law and asymmetry category
2. Model N2 and A16 pricing versus capex intensity to confirm incremental ROIC is rising, not falling
3. Assess overseas-fab margin drag through 2028

**Sources**

- <https://investor.tsmc.com/english/quarterly-results/2026/q2>
- <https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-lifts-2026-outlook-as-ai-demand-stays-hot-in-q2-2026-93CH-4794777>

---

### GOOGL — Alphabet
*NASDAQ · confidence: MEDIUM-LOW - capex and FCF facts are well corroborated; segment-level TPU economics are not disclosed and remain INFERENCE*

FACT: 2026 capex guided $175-185B; Alphabet reported its first negative free-cash-flow quarter since its 2004 IPO. INFERENCE: among the four hyperscalers, Alphabet is the only one that owns the full stack - TPU silicon, frontier models, distribution through Search/Android/YouTube, and Cloud - so a materially larger share of its own capex is retained internally rather than paid out to merchant silicon vendors. That is a differentiated reinvestment-economics case rather than a generic 'big tech is spending' case, and it is the specific reason this name is screened in while the other three are held at WATCH.

**Top 3 positive signals**

1. Vertical integration through TPU means capex substitutes for a supplier margin rather than adding to it
1. Distribution moat (Search, Android, YouTube, Workspace) is the cheapest customer acquisition channel in software for any AI product it ships
1. Cloud backlog growth gives a visible revenue line against which the capex can be underwritten

**Top 3 uncertainties**

1. FCF per share - the strategy's primary metric - is currently going backwards; the depreciation wave has not yet hit the income statement
1. Generative search interfaces are the most direct structural threat to the query-monetisation model that funds everything else
1. Antitrust remedies remain an unresolved overhang on default-placement economics

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `incremental_roic_collapse` | INVESTIGATE | Capital intensity has stepped up structurally; incremental ROIC on ~$180B/yr is unproven |
| `moat_shrinkage` | INVESTIGATE | Search query-volume and monetisation trend under generative interfaces must be measured, not assumed |

**Research priorities**

1. Estimate TPU total cost of ownership versus merchant GPU to test whether vertical integration genuinely raises incremental ROIC
2. Find measurable evidence on Search query volume and cost-per-click trend post generative interfaces - the core thesis falsifier
3. Model the 2027-2029 depreciation schedule against the FCF-per-share path

**Sources**

- <https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html>
- <https://valueaddvc.com/blog/ai-hyperscaler-capex-compared-why-microsoft-google-meta-and-amazon-are-all-spending-at-once>
- <https://epoch.ai/data-insights/hyperscaler-capex-vs-cash-flow>

---

### NET — Cloudflare
*NYSE · confidence: MEDIUM - operating KPIs are specific and internally consistent; sourced from earnings analysis rather than the 10-Q*

FACT: Q2 2026 revenue +35.9% YoY, beating estimates by 4.7%; RPO +38.2% YoY; dollar-based net retention improved to 120% from 118%; net new ARR +69.6% YoY. Gross margin 73.1%, down 3.2pp YoY but up 30bp sequentially, with management expecting stabilisation near current levels. INFERENCE: net new ARR accelerating to +70% while net retention improves is the single strongest forward indicator in this screen - both the numerator and the cohort quality are improving at once, which is the profile the strategy is built to find.

**Top 3 positive signals**

1. Net new ARR +69.6% YoY with DBNR improving 118% to 120% - acquisition and expansion strengthening simultaneously
1. RPO +38.2% confirms the growth is contracted, not booked on spot consumption
1. Edge inference (Workers AI) is a credible category-defining position rather than a feature

**Top 3 uncertainties**

1. Gross margin fell 3.2pp YoY on GPU/edge capex - the strategy explicitly penalises growth requiring high incremental capital until the return is proven
1. Management's margin-stabilisation statement is guidance (ESTIMATE), not yet evidence
1. Stock-based compensation and dilution trend not established in this run

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `low_quality_growth` | PASS | Growth is contracted and retention-led, not subsidy- or discount-driven |
| `incremental_roic_collapse` | INVESTIGATE | Edge GPU capex is compressing gross margin; return on that capital is unproven |

**Research priorities**

1. Compute incremental ROIC on edge GPU deployment and test the margin-stabilisation guidance against the next two prints
2. Establish the FCF-per-share path net of SBC and share count growth
3. Size Workers AI revenue separately from the core network business

**Sources**

- <https://sergeycyw.substack.com/p/datadog-cloudflare-earnings-q2-2026>

---

### DDOG — Datadog
*NASDAQ · confidence: MEDIUM - KPI set is specific and corroborated across sources*

FACT: Q2 2026 revenue $1.12B, +35.6% YoY and +11.4% QoQ, beating estimates by 4.3%; RPO $3.47B, +43.1% YoY; billings $1.18B, +38.0% YoY; net new ARR +75.8% YoY with $460M added in the quarter. INFERENCE: a company at this scale re-accelerating - with RPO growing faster than revenue - indicates the AI workload cycle is expanding observability spend structurally rather than substituting for it. Capital-light with high incremental margin, which is the reinvestment profile the strategy prefers.

**Top 3 positive signals**

1. Re-acceleration at $4B+ run-rate with RPO growth (+43.1%) outpacing revenue growth (+35.6%)
1. Net new ARR +75.8% YoY - forward indicators leading reported revenue
1. Multi-product attach creates real switching costs; capital-light so incremental ROIC is structurally high

**Top 3 uncertainties**

1. AI-native customer cohort concentration is not disclosed at the granularity needed; these customers share the same funding dependency flagged in the macro overlay
1. Consumption pricing means a capex pause transmits to revenue faster than in a seat-based model
1. Competitive pressure from hyperscaler-native observability bundles

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `fatal_concentration` | INVESTIGATE | AI-native cohort concentration must be quantified; these are the least credit-durable customers in software |
| `low_quality_growth` | PASS | Expansion-led growth with contracted RPO backing |

**Research priorities**

1. Quantify AI-native cohort as a percentage of ARR and its renewal/expansion economics separately from the enterprise base
2. Test whether consumption growth is workload-driven or price-driven
3. Establish FCF per share net of SBC

**Sources**

- <https://sergeycyw.substack.com/p/datadog-cloudflare-earnings-q2-2026>

---

### ISRG — Intuitive Surgical
*NASDAQ · confidence: MEDIUM-HIGH - figures corroborated across multiple sources including 8-K coverage*

FACT: Q2 2026 revenue $2.89B, +19% YoY; worldwide procedures +16% YoY; non-GAAP gross margin 70.0% (GAAP 67.8%); non-GAAP operating margin 42% (GAAP 33.6%); non-GAAP gross margin guidance raised to 68-69%; market capitalisation approximately $133B. INFERENCE: this is a duration-mispricing candidate rather than a magnitude candidate. Mid-teens procedure growth has persisted for roughly two decades and the market has repeatedly underestimated how long it continues. Screened in with an explicit caveat below.

**Top 3 positive signals**

1. Razor-and-blade model: instruments and accessories recur off a growing installed base, so revenue leads system placements by years
1. Surgeon training and hospital workflow lock-in are among the highest switching costs in medical devices
1. Entirely self-funded with no external financing dependence; strong recession-resilient FCF

**Top 3 uncertainties**

1. Explicit caveat: at $133B this likely scores poorly on the power-law and asymmetry category (10 points) - a 10x is not arithmetically plausible from here. It is a low-permanent-loss duration compounder, not an outlier-magnitude candidate.
1. Medtronic Hugo and J&J Ottava are the first credible competitive entries in two decades - moat trajectory must be measured, not assumed
1. Hospital capital budgets are exposed to reimbursement policy change

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `moat_shrinkage` | INVESTIGATE | First credible multi-competitor environment in the franchise's history |
| `price_requires_unrealistic_bull_case` | PASS | Price embeds continuation of an established trend, not a discontinuity |

**Research priorities**

1. Measure competitive placement share in newly contested accounts - the single cleanest moat-trajectory falsifier
2. Model da Vinci 5 upgrade cycle contribution versus underlying procedure growth to separate one-time from recurring
3. Score the asymmetry category honestly: quantify realistic upside multiple over ten years before allocating deep-analyst time

**Sources**

- <https://www.stocktitan.net/sec-filings/ISRG/8-k-intuitive-surgical-inc-reports-material-event-fc529caa4b6d.html>
- <https://quartr.com/events/intuitive-surgical-inc-isrg-q2-2026_3PVeOSEn>
- <https://www.investing.com/news/transcripts/earnings-call-transcript-intuitive-surgical-beats-q2-2026-estimates-shares-fall-93CH-4797128>

---

### AXON — Axon Enterprise
*NASDAQ · confidence: MEDIUM - quarterly figures corroborated; capital structure and valuation not established*

FACT: Q2 2026 revenue $904M, +35.2% YoY, beating estimates by 3.2%; GAAP gross margin 60.4% (+0.1pp YoY), non-GAAP gross margin 62.9% (-0.3pp YoY); operating margin 5.2%, up 5.3pp YoY. INFERENCE: agency switching costs are exceptionally high - evidence-management systems are embedded in chain-of-custody and prosecutorial workflow - and the software attach (Evidence.com, Draft One) is converting a hardware vendor into a recurring-revenue platform. The open question is whether operating leverage is real, since a 5.2% GAAP operating margin at 35% growth leaves the FCF-per-share path unproven.

**Top 3 positive signals**

1. Sticky, budget-funded government customer base with multi-year contracted revenue and near-zero churn
1. TAM expansion into federal, international and enterprise security is genuine market creation, not share capture
1. Operating margin +5.3pp YoY indicates leverage is starting to appear

**Top 3 uncertainties**

1. GAAP operating margin only 5.2% at 35% growth - heavy SBC; FCF per share and dilution must be verified before any conviction
1. Gross margin flat-to-slightly-down while revenue grew 35% is a mild negative on unit economics
1. Valuation is likely demanding; not established in this run

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `persistent_dilution` | INVESTIGATE | Low GAAP operating margin alongside high growth points to material SBC; share count trend must be established |
| `low_quality_growth` | PASS | Contracted, recurring, budget-funded revenue |

**Research priorities**

1. Establish diluted share count trend and FCF per share over five years - the decisive question for this name
2. Separate hardware, subscription and AI (Draft One) revenue and their respective incremental margins
3. Reverse-engineer what agency penetration and ARPU the current price requires

**Sources**

- <https://sergeycyw.substack.com/p/mercadolibre-applovin-axon-earnings>

---

## Korea-listed

### 005930 — Samsung Electronics / 삼성전자
*KOSPI · confidence: MEDIUM - headline results are from company IR materials via corroborated coverage; the P/B figure is broker-sourced and should be recomputed*

FACT: Q2 2026 consolidated revenue KRW 171.5T and operating profit KRW 89.5T, both quarterly records; operating margin 52.2% versus 43% in the prior quarter. HBM4 supply expanding, with the industry's first HBM4E samples shipped; HBM4 expected to comfortably exceed 60% of Samsung's own HBM revenue in H2. Foundry improved on HBM base-die and US customer demand. HBM market share rose from 21% in Q1 to 33% in Q2. Forward P/B reported around 1.4x. INFERENCE: two things are true at once. A company-wide 52.2% operating margin is unambiguously a memory-pricing cycle peak and must not be capitalised. But an HBM share move from 21% to 33% in a single quarter, plus a foundry business finally winning real volume through HBM base dies, is measurable moat-trajectory improvement that is independent of the cycle. At roughly 1.4x forward book the price does not require the peak to persist - which is precisely the asymmetry the strategy looks for.

**Top 3 positive signals**

1. HBM share 21% to 33% in one quarter, and first-to-market HBM4E samples - measurable competitive-position improvement, not narrative
1. Foundry finally attaching real volume via HBM base dies and US customers, addressing the division's core structural weakness
1. Forward P/B ~1.4x means the market is explicitly not capitalising peak earnings - the bull case is not required for the investment to work

**Top 3 uncertainties**

1. 52.2% company-wide operating margin is a cycle peak; normalised mid-cycle earnings power is the entire valuation question
1. HBM4 qualification depth at the largest accelerator customer is not publicly established at the needed granularity
1. Foundry profitability path and utilisation are still not disclosed clearly enough to underwrite

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `price_requires_unrealistic_bull_case` | PASS | ~1.4x forward book does not embed bull-case-or-better execution |
| `low_quality_growth` | PASS | Growth is price and mix driven within a real capacity shortage, not subsidy driven |
| `incremental_roic_collapse` | INVESTIGATE | Current incremental ROIC is at a cycle peak; the down-cycle case must be modelled |

**Research priorities**

1. Model normalised mid-cycle earnings and reverse-engineer which earnings level ~1.4x forward book actually capitalises - the central question
2. Establish HBM4 qualification status and allocated share at each major accelerator customer; this is the moat-trajectory falsifier
3. Determine foundry breakeven utilisation and whether the HBM base-die business is structurally sticky or a stopgap

**Sources**

- <https://images.samsung.com/kdp/ir/events/2026/2026_2Q_conference_kor.pdf>
- <https://www.e-focus.co.kr/news/articleView.html?idxno=3002653>
- <https://www.kbam.co.kr/board/view/1060>
- <https://www.businesspost.co.kr/BP?command=article_view&num=446371>

---

### 012450 — Hanwha Aerospace / 한화에어로스페이스
*KOSPI · confidence: LOW-MEDIUM - the earnings beat is corroborated but exact revenue, operating profit and backlog figures were not established in this run and are marked unknown rather than estimated*

FACT: Q2 2026 operating profit exceeded consensus by more than KRW 300B (consensus around KRW 1T), and brokers raised target prices across the board. INFERENCE: European rearmament is a treaty- and budget-driven demand shift measured in decades, not a cycle, and Korea's specific advantage is deliverable production capacity at a time when European primes are capacity-constrained. Critically for portfolio construction, this is one of very few names in this screen whose demand driver is neither AI capex nor the memory cycle - it is genuinely uncorrelated with the dominant risk factor identified in the macro overlay.

**Top 3 positive signals**

1. Demand driver is multi-year government budget commitments, giving unusual duration visibility
1. Korea's competitive edge is delivery speed and production capacity - a real, hard-to-replicate advantage while European primes are constrained
1. Uncorrelated with the AI-capex funding dependency that runs through most of this screen

**Top 3 uncertainties**

1. Capital raising history must be checked against the persistent_dilution veto before any position is considered
1. Demand is a government-budget derivative and therefore politically reversible
1. Backlog conversion margins on export contracts, including local-production offset obligations, are not established

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `persistent_dilution` | INVESTIGATE | PRIMARY GATE. The company has raised equity materially in recent years; multi-year per-share dilution must be quantified before the FCF-per-share thesis can be assessed |
| `fatal_concentration` | INVESTIGATE | Dependence on a small number of large sovereign customers and on the continuation of European rearmament policy |

**Research priorities**

1. Quantify multi-year share count growth and per-share economics after capital raises - this gates the entire thesis
2. Establish backlog margin structure, including offset and local-production obligations that transfer value to the customer country
3. Test the durability of European defence budget commitments against political change scenarios

**Sources**

- <https://www.fnnews.com/news/202608030946263240>

---

### 034020 — Doosan Enerbility / 두산에너빌리티
*KOSPI · confidence: LOW-MEDIUM - order figures are broker- and press-sourced; SMR milestones are externally verifiable facts; the 2030 forecasts are explicitly ESTIMATE*

FACT: 2026 order target KRW 14.3T (nuclear KRW 5.8T, gas power KRW 5.3T); gas turbine orders reached 97% of full-year guidance within H1; seven gas turbines contracted to a US big-tech customer; 2030 gas turbine backlog forecast to be 114.6% above last year. On SMR, NuScale's Romania project received final investment decision approval and TerraPower obtained its US NRC construction permit, with more than 70 units expected by 2030. INFERENCE: data-centre power is the genuine second-order bottleneck of the AI buildout, and Doosan is one of very few gas turbine OEMs outside GE, Siemens and Mitsubishi - a scarce asset with a decade-long qualification barrier. What makes this screenable rather than narrative is that the orders are already booked, and the SMR validation points are third-party regulatory and investment facts rather than company projections.

**Top 3 positive signals**

1. Scarce-asset position: gas turbine OEM qualification is a decade-scale barrier and the field has four credible players globally
1. Gas turbine orders at 97% of annual guidance by mid-year - evidence in hand, not a forecast
1. SMR optionality validated by external parties (NuScale Romania FID, TerraPower NRC permit), not by company statements

**Top 3 uncertainties**

1. Historical capital allocation and balance-sheet record is poor - the 2020 restructuring is directly relevant to the management category
1. Long-cycle equipment and EPC margin risk on fixed-price contracts
1. 2030 backlog and SMR unit forecasts are broker ESTIMATES, not booked orders, and must not be treated as facts

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `management_and_capital_allocation_history` | INVESTIGATE | Not a named veto, but the prior restructuring makes the capital-allocation scorecard category the decisive one; flagged here so it is not skipped |
| `incremental_roic_collapse` | INVESTIGATE | Long-cycle EPC economics have historically produced weak incremental returns; must be tested against the new order mix |

**Research priorities**

1. Establish gas turbine gross margin versus GE Vernova and Mitsubishi to test whether this is a scarce-asset premium or a share-through-price position
2. Review the capital allocation record since the 2020 restructuring - the central question for the management category
3. Separate booked orders from forecast backlog rigorously; underwrite only what is booked

**Sources**

- <https://www.hankyung.com/article/2026040232886>
- <https://www.thedailymoney.com/news/articleView.html?idxno=1137167>

---

### 267260 — HD Hyundai Electric / HD현대일렉트릭
*KOSPI · confidence: MEDIUM - quarterly figures and backlog are specific and press-corroborated from company disclosure*

FACT: Q2 2026 consolidated revenue KRW 1,141.8B, operating profit KRW 287.0B (operating margin 25.1%), net income KRW 206.1B; Q2 new orders $1.44B; end-Q2 backlog $8.49B, +29.6% YoY and +7.6% QoQ. INFERENCE: a 25% operating margin in power transformers is historically extraordinary - the normal range is high single digits - so a cycle-peak component is undeniable. But unlike memory, the supply response in transformers is genuinely slow: grain-oriented electrical steel, skilled winding labour and multi-year lead times all constrain new capacity. That extends the duration of the shortage rent well beyond a typical equipment cycle, and backlog growing 29.6% YoY while margins hold is evidence the shortage has not yet been arbitraged away.

**Top 3 positive signals**

1. Backlog +29.6% YoY with margin holding at 25.1% - both the volume and the price signal are still improving
1. The supply response in transformers is structurally slow, which lengthens the duration of the rent versus a normal equipment cycle
1. Demand is driven by US grid replacement and electrification as well as data centres, so it is only partly exposed to the AI-capex funding risk

**Top 3 uncertainties**

1. 25.1% operating margin has a large cycle-peak component; normalised margin is the key modelling question
1. How much of the margin is price versus mix (HVDC, high-voltage) has not been established
1. Global capacity additions from 2028 onward could reset pricing

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `price_requires_unrealistic_bull_case` | INVESTIGATE | Must establish whether the price capitalises the 25% peak margin or a normalised level |
| `moat_shrinkage` | PASS | Backlog and margin both improving; no evidence of competitive erosion |

**Research priorities**

1. Decompose the 25.1% margin into price, mix and utilisation, then model a normalised margin
2. Map announced global transformer capacity additions through 2029 to date the supply response
3. Establish the split between data-centre-driven and grid-replacement-driven demand to size the correlated AI exposure

**Sources**

- <https://www.huffingtonpost.kr/article/259071>
- <https://www.sedaily.com/article/20072797>

---

### 207940 — Samsung Biologics / 삼성바이오로직스
*KOSPI · confidence: LOW - qualitative case only. Screened in to justify evidence-gathering, NOT as a quantitatively supported candidate. Per policy/source-policy.yaml, unknown is recorded rather than estimated.*

FACT: the largest Korean listed pharmaceutical company by scale, with the gap versus the second-largest (Celltrion) widening. INFERENCE: biologics CDMO is one of the few businesses where the moat is written into the customer's own regulatory filing - a validated manufacturing line is named in the drug approval, so switching requires a regulatory amendment and comparability studies. That produces switching costs measured in years. Combined with biologics volume growth and supply-chain reshoring away from Chinese CDMOs, this is a structural, non-cyclical, non-AI-correlated compounder. Screened in on the qualitative case, with an explicit and important caveat on evidence quality below.

**Top 3 positive signals**

1. Regulatory lock-in: a validated line is named in the customer's approval, making switching costs unusually durable and quantifiable
1. Capacity expansion (Plants 5 and 6) is a reinvestment runway with a known, contractible return profile rather than speculative capex
1. Supply-chain reshoring away from Chinese CDMOs is a policy-driven structural tailwind independent of the economic cycle

**Top 3 uncertainties**

1. EVIDENCE GAP: current-period revenue, operating margin, utilisation and contracted backlog were NOT established in this run. Confidence is correspondingly low and no quantitative claim should be relied upon until this is closed.
1. CDMO capacity is ultimately a commodity if utilisation falls; pricing power depends on the industry remaining supply-tight
1. Related-party and governance history within the group warrants review under the management category

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `management_or_accounting_integrity` | INVESTIGATE | Prior accounting controversy in this company's history requires explicit review under the named veto before any position; this is not a conclusion, it is a mandatory check |
| `incremental_roic_collapse` | INVESTIGATE | Return on Plant 5/6 capital cannot be assessed without utilisation and contract data |

**Research priorities**

1. CLOSE THE EVIDENCE GAP FIRST: obtain current revenue, operating margin, utilisation and contracted backlog from company IR before any further work
2. Review the accounting history explicitly against the management_or_accounting_integrity veto
3. Compute incremental ROIC on Plant 5 and 6 against contracted volumes

**Sources**

- <https://m.dailypharm.com/user/news/8569>

---

### 214450 — PharmaResearch / 파마리서치
*KOSDAQ · confidence: MEDIUM - quarterly figures are specific and corroborated across two sources; competitive and regulatory assessment not yet performed*

FACT: Q2 2026 consolidated revenue KRW 178.7B (+27% YoY) and operating profit KRW 66.5B (+19% YoY), an operating margin of roughly 37%; H1 revenue KRW 324.8B and operating profit KRW 123.8B; Q2 exports KRW 84.0B, +62% YoY, lifting exports to 47% of total revenue, driven by domestic Rejuran demand plus European medical device and global cosmetics growth. INFERENCE: this is the most interesting under-followed profile in the run. A 37% operating margin on a branded consumer-medical product, with exports growing 62% and approaching half of revenue, indicates real brand pricing power crossing an international threshold - and it requires very little incremental capital, so incremental ROIC is structurally high. It is also small enough that a power-law outcome is arithmetically plausible, which most names in this screen are not, and it is uncorrelated with AI capex.

**Top 3 positive signals**

1. Exports +62% YoY now at 47% of revenue - the international transition is happening in the numbers, not in guidance
1. 37% operating margin on a branded product with low capital intensity means high incremental ROIC and a real FCF-per-share path
1. Small enough for genuine power-law upside, and uncorrelated with both the memory cycle and AI capex

**Top 3 uncertainties**

1. Competitive response in PDRN/PN skin boosters is intensifying; Rejuran's brand premium is the whole thesis and must be monitored
1. Export growth must be distinguished from one-off distributor stocking versus genuine end-market sell-through
1. US regulatory pathway for the core product is not established

**Hard Veto flags**

| Veto | Status | Note |
|---|---|---|
| `fatal_concentration` | INVESTIGATE | Heavy dependence on a single product family (Rejuran); must be sized |
| `low_quality_growth` | PASS | Growth is price- and brand-driven at a 37% operating margin, not discount- or marketing-subsidy-driven |
| `moat_shrinkage` | INVESTIGATE | New PDRN/PN entrants are the primary moat-trajectory risk |

**Research priorities**

1. Separate sell-in from sell-through by export market to confirm the +62% is genuine end demand
2. Assess the competitive set in PDRN/PN skin boosters and Rejuran's price premium trend - the core moat falsifier
3. Establish the US and European regulatory roadmap and what it would add to the addressable market

**Sources**

- <https://www.sentv.co.kr/article/view/sentv202608070081>
- <https://www.insight.co.kr/news/567024>

---

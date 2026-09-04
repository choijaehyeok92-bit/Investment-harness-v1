# Investment Thesis — NVDA (NVIDIA Corporation)

As of: 2026-09-04 · Price: $226.27 · Position: STARTER (1–2%)
Prepared under `agents/deep-analyst.md`. Expectation gap and asymmetry are scored by
`agents/valuation.md`, not here.

---

## Sourcing note

Every financial figure below is **tier-1 SEC primary filing data**, parsed directly
from the XBRL instance documents supplied:

| Filing | Period | Filed |
|---|---|---|
| **10-K FY2026** | FY ended 2026-01-25 | 2026-02-25 |
| **10-Q Q2 FY2027** | Quarter ended 2026-07-26 | 2026-08-26 |
| DEF 14A (additional materials) | — | 2026-05-12 |
| 8-K | 2026-09-02 | 2026-09-02 |
| Form 4 (director Stevens) | 2026-08-31 → 09-02 | 2026-09-02 |
| Form 3 (EVP Parker) | 2026-08-24 | 2026-09-03 |

The **price anchor is also tier-1**: $226.27 is the last reported transaction in the
Form 4. The 8-K carried only cover-page XBRL (substance sits in an unfiled exhibit).

Two material unknowns remain, disclosed rather than estimated away: **cancellability
terms of the $279B supply commitments**, and **revenue share from equity-affiliated
entities**.

---

## 1. Structural change and market leadership — 14/15

| | FY2024 | FY2025 | FY2026 | H1 FY2027 |
|---|---|---|---|---|
| Revenue | $60,922M | $130,497M | $215,938M | $177,837M |
| Data Center | $47,525M | $115,186M | $193,737M | — |
| Operating income | $32,972M | $81,453M | $130,387M | $117,270M |
| Diluted EPS | $1.19 | $2.94 | $4.90 | $4.85 |

H1 FY2027 revenue grew **+95.8% YoY** and annualises to roughly **$356B**. Data
Center is **89.7%** of FY2026 revenue; within it Networking has gone **$8,575M →
$31,376M in two fiscal years (3.7x)**.

This scores at the category's top anchor — *"clear leader directly driving structural
change"*. NVIDIA does not benefit from the AI build-out; it defines its technical
standard (CUDA, NVLink, rack-scale systems, an annual architecture cadence).

**The deduction is geographic.** Concentration is intensifying, not diversifying: US
revenue **51.8% → 59.4% → 69.3%**. China including Hong Kong fell **$25,048M
(FY2025) → $19,677M (FY2026) → $12,430M (H1 FY2027)** — declining in absolute terms
while the total nearly doubled, now ~7% of revenue. A large market has closed. And
**76% of Taiwan-billed FY2026 revenue was to US/Europe end customers**, so the
geographic split *understates* US end-demand concentration.

## 2. Customer value and product strength — 8/10

Gross margin of **72.7% → 75.0% → 71.1% → 75.0%** on a near-doubling revenue base is
direct evidence customers are not extracting the value. CUDA plus the framework
ecosystem creates switching costs measured in engineering-years. Networking attach
growing faster than compute is the clearest proof of expanding product value.

Capped at 8 because **customer concentration is rising sharply** (below), FY2026
gross margin *fell* to 71.1% during the Blackwell ramp, and the largest customers are
precisely those funding custom-silicon alternatives.

## 3. Moat trajectory — 11/15

`agents/deep-analyst.md` demands direction over level. Direction here is **genuinely
mixed**, which is why this is the widest gap between quality and score in the file.

**Widening:** networking 3.7x in two years; rack-scale delivery turns a chip sale
into a data-centre-unit sale; R&D $8,675M → $18,497M funding a cadence no competitor
matches; gross margin recovered to 75.0% in H1 FY2027.

**Narrowing:**

| Customer One, % of Compute & Networking revenue | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| | 13% | 12% | **22%** |

Customer Two reached 14%. **Top two = 36% of segment revenue, from 23% a year
earlier.** H1 FY2027 receivables concentration is 22/14/13/11/10 — roughly **70% in
five names**. Rising concentration is the standard signature of buyer power
increasing.

**And the moat's success funds its challengers.** A 75% gross margin *is* the
business case for every customer's internal silicon programme.

## 4. Incremental ROIC and FCF/share — 13/15

Exceptional and tier-1 verified:

- **Capex is 2.8% of revenue** ($6,042M on $215,938M in FY2026); D&A $2,843M
- FY2026 operating cash flow **$102,718M**; H1 FY2027 **$74,421M**
- **Share count DOWN 2.3%** — 24,661M (2023-01-29) → **24,100M** (2026-08-21) —
  during the fastest growth phase in company history
- Buybacks $9.5B / $33.7B / $40.1B across FY2024–26, plus **$39,044M in H1 FY2027**
- SBC modest at $6,386M, **3.0% of revenue**, more than offset by repurchases
- ROE roughly **100%** in FY2026

**But the capital is committed off the balance sheet.** See §7 — this is what holds
the score at 13 rather than 15.

## 5. Management and capital allocation — 7/10

Repurchase execution is genuinely strong: **$113B across FY2024–H1 FY2027 with share
count falling**. R&D productivity is demonstrable, not asserted.

**The central question is the investment programme.** Equity stakes held have gone
from roughly **$5B to $90.7B in twelve months** ($42,783M public + $47,898M
non-marketable), with **$25B more committed** and **$29B of committed cloud-service
purchases**. NVIDIA is simultaneously supplier to, investor in, and customer of parts
of its own ecosystem.

That is defensible as ecosystem seeding. It is also a very large bet made with
shareholder capital at undisclosed hurdle rates, and it materially affects earnings
quality (§ *Earnings quality* below).

Recorded, not omitted: director Mark A. Stevens sold **1,848,501 shares (~$410M)**
2026-08-31 → 09-02. Weak evidence alone — trust-held, and NVIDIA insiders have sold
steadily for years.

## 6. Financial survivability — 9/10

Assets **$320,272M**, liabilities **$91,288M**, equity **$228,984M**. Cash $22,443M
plus $42,783M of publicly held equity securities against $32,366M of long-term debt.
H1 operating cash flow of $74,421M dwarfs every fixed obligation. **No plausible
insolvency path.**

Two flags: long-term debt went **$7,469M → $32,366M** in six months ($25B notes at
2026-06-30) — the first material leverage in the company's modern history; and
product warranty liabilities went **$306M → $1,290M → $2,807M** (9x in two years) as
rack-scale systems replace chips.

---

## Earnings quality — the adjustment that changes the multiple

**Reported H1 net income ($118,010M) EXCEEDS operating income ($117,270M).** The
reason is gain on investments:

| Gain on investments | FY2024 | FY2025 | FY2026 | H1 FY2027 |
|---|---|---|---|---|
| | $238M | $1,030M | $8,918M | **$23,707M** |

Of the H1 figure, **$12,500M is explicitly unrealised marks on publicly held
equity securities**. Roughly **17–20% of reported net income is investment
revaluation, not operations** — and the revalued assets are stakes in companies whose
spending is itself NVIDIA revenue.

Stripping it: H1 pretax $141,410M − $23,707M = $117,703M core pretax; taxed at the
actual 16.5% effective rate gives **core net income ≈ $98,282M** for the half,
**$196.6B annualised**, or **~$8.08 core annualised EPS**.

| Multiple at $226.27 | |
|---|---|
| On reported annualised EPS $9.70 | **23.3x** |
| **On core annualised EPS $8.08** | **28.0x** |

This is GAAP-compliant and disclosed. It is not an integrity failure. But every
valuation test in this file uses the **core** figure.

## 7. Key risks and concentration dependencies

**$366B of future commitments** at 2026-07-26 — the single most important risk
datapoint in this file:

| | Rem. FY27 | FY28 | FY29 | FY30 | FY31 | FY32+ | **Total** |
|---|---|---|---|---|---|---|---|
| **Supply and capacity** | 92 | 87 | 88 | 6 | 5 | 1 | **$279B** |
| Cloud service agreements | 3 | 8 | 7 | 6 | 4 | 1 | $29B |
| DC leases not commenced | — | 1 | 1 | 2 | 1 | 20 | $25B |
| Equity investments | 18 | 3 | 2 | 2 | — | — | $25B |
| Capital expenditures | 7 | 1 | — | — | — | — | $8B |
| **Total** | **120** | **100** | **98** | **16** | **10** | **22** | **$366B** |

**Supply and capacity rose from $95.2B (2026-01-25) to $279B (2026-07-26) — +193% in
six months.** That is ~78% of annualised revenue, and it is the *real* capital
commitment of a business reporting 2.8%-of-revenue capex. The recorded
excess-inventory purchase accrual is only **$2,138M** — the accounts assume full
consumption.

**Three concentrations compound:** end market (Data Center 89.7%), customer (top two
36% of segment revenue, top five 70% of receivables), geography (US 69.3%). And per
this harness's own screening work, those customers are funding purchases **from
balance sheet rather than operating cash flow** — hyperscaler 2026 capex is guided
above $725B while Alphabet posted its first negative-FCF quarter since 2004 and
Meta's cash generation fell 91% YoY.

**Critically, the risks are correlated, not independent.** The same demand pause that
triggers the supply write-down also marks down the $90.7B investment portfolio and
hits the customers behind the concentration. That is why the modelled bear is
−56% to −68% despite a fortress balance sheet.

---

## Most important unknowns

1. **Cancellability terms of the $279B.** The 10-K says these agreements are *"in
   certain instances"* cancellable, reschedulable or adjustable — without
   quantifying. This determines whether the bear is a margin event or a
   balance-sheet event.
2. **Revenue share from equity-affiliated entities.** Bounded below ~10% on a
   worst-case assumption, but unquantified.
3. Realised/unrealised split and cost basis of the $47,898M non-marketable portfolio.
4. Identity and funding structure of the 22% customer.
5. Merchant-GPU versus custom-ASIC share of total accelerator deployments.

## Evidence that would strengthen the thesis

- Equity-affiliated revenue quantified below ~5% and stable
- Supply commitments disclosed as materially cancellable
- Top-customer concentration stabilising or falling from 22%
- Gross margin holding ≥75% through the Rubin ramp
- Investment gains falling as a share of net income

## Evidence that would weaken the thesis

- Equity-affiliated revenue above ~10%, or growing faster than third-party revenue
- Supply commitments rising while sequential revenue decelerates
- The excess-inventory accrual rising materially from $2,138M — management's own signal
- Gross margin below ~70% outside a product transition
- A hyperscaler capex guidance cut

---

## Why STARTER here and NONE for Samsung

Both carry unresolved HIGH-severity vetoes. The difference is the **expectation gap**.

For 005930 the normalised model landed **below** what the price required — the gap
was negative, so no position was justified at any veto status. For NVDA, at 23.3x
reported / **28.0x core** annualised earnings, a 25x mature multiple requires roughly
the **current core earnings base to persist with no growth**. The gap is positive,
though thin.

`policy/position-sizing.yaml` defines STARTER as *"attractive thesis, but evidence is
still limited."* That describes this exactly: exceptional business quality (75/100,
Emerging Outlier — the highest in this harness to date), a positive gap, bounded
risks, 2–3% permanent-loss probability — against three open HIGH-severity gates and a
probability-weighted five-year return of only **+21% total (3.9%/yr)**.

Macro pacing is **slow**: per the 2026-09-04 screening run the AI-capex complex is
treated as a single correlated exposure, and NVDA is its centre of gravity.

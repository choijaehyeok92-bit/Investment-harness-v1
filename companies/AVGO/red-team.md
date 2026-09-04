
# Red Team — AVGO

As of 2026-09-04 · per `agents/red-team.md`
This document does not recommend a purchase and does not defend the thesis.

---

## Strongest bear thesis

**Broadcom is a levered, goodwill-financed roll-up whose entire growth story now rests
on one customer that supplies 42% of revenue — and it cannot stop issuing stock.**

Every leg of that sentence is a tier-1 fact. Net debt ~$47.1B. Goodwill plus
intangibles $130,074M against $81,292M of equity, so tangible book is deeply negative.
One distributor at **42% of total revenue, up from 29% in a year**. And a share count
that **rose despite $8,450M of buybacks in six months**, because SBC ran at 10.3% of
revenue.

The bull answer is 42% FCF margin and 221% AI growth. Both true. But you are paying
**38x estimated GAAP earnings** for a business where a single relationship failing is
a business-model event, and where the leverage removes the cushion the other three
names have.

---

## Attacks required by the contract

**1. What if the apparent structural growth is cyclical?**
Custom ASIC demand is a *derivative* of hyperscaler capex, which this harness has
already established is being funded from balance sheet rather than operating cash flow.
Broadcom is one step further from the end demand than NVDA and has **no unit or ASP
disclosure** to decompose price from volume — the same blind spot as NVDA, and worse
than Samsung and TSMC where ASP is disclosed.

**2. What if TAM growth does not translate into company cash flow?**
It translates superbly into *cash* — 42.1% FCF margin — but **not into per-share
value**. That is the whole attack. $26.9B of FY2025 free cash flow, and the share count
still went up.

**3. What if moat expansion is being confused with revenue growth?**
Directly applicable and the analyst concedes it. AI revenue +221% while
**single-customer share went 29% → 42%.** Revenue grew; the moat narrowed. Scoring
moat trajectory at 10/15 is right, and I would not argue for higher.

**4. What if customer value is overstated?**
61.8% semiconductor margin says it is not. Conceded.

**5. What if incremental ROIC is already deteriorating?**
No — 1.0% capex intensity with expanding margins. This is the strongest fact in the
file and I cannot attack it.

**6. What if FCF/share growth is overstated by SBC or dilution?**
**Yes, and this is my best-supported attack.** SBC $7,570M (FY2025) and $4,268M (H1
FY2026) — 10–12% of revenue. Management guides to non-GAAP, which excludes it. The
share count *proves* it is a real cost. The analyst uses GAAP throughout, correctly.

**7. What if management capital allocation contradicts the stated strategy?**
The playbook works, but note what it *is*: buy at scale with debt and stock, reprice
the base, cut cost, harvest. That produces accounting profit and a balance sheet where
**76% of assets are goodwill and intangibles**. `policy/scorecard.yaml` names
*"acquisition price and outcomes"* as an indicator — the outcome is good; the price
left tangible book value deeply negative.

**8. What if the market already understands the bullish thesis?**
It does — and it just told you. The stock fell **~6.5% after hours on a +221% AI
print**. When a market sells a 221% growth number, it is not the growth it doubts.

**9. Which assumption contributes the most to valuation?**
**The FY2026 GAAP earnings build — which the analyst invented.** Q3 GAAP was not
available; the file assumes ~50% and ~52% GAAP operating margins for Q3 and Q4. If the
true GAAP margin is 3 points lower, FY2026 GAAP net income falls roughly $3B and the
multiple moves from 38x toward 41x. **The most important valuation input in this file
is an estimate, and the file says so — but that is disclosure, not robustness.**

**10. What single event could create permanent loss?**
The 42% customer in-sourcing. With $47.1B of net debt and negative tangible book,
that is a genuine impairment scenario, not merely a drawdown. I accept the 4–6%
probability as reasonable.

---

## Three most dangerous hidden assumptions

1. **That the 42% customer relationship is durable.** Nothing in the file establishes
   contract length. The analyst names this as the primary gate — correctly — which
   means the position rests on a fact nobody outside the company currently has.
2. **That infrastructure software is a floor.** The bear case leans on ~$28B of
   revenue at a 78% margin as a backstop. But that margin came from **repricing a
   captive installed base**, which invites substitution and regulatory attention. A
   floor built on customer resentment is not obviously a floor.
3. **That the VMware share issuance was "one-time."** It is used to excuse the
   dilution record. But Broadcom is a *serial acquirer* — the next deal will likely be
   funded the same way. Treating acquisition-currency dilution as non-recurring at a
   company whose strategy is serial acquisition is a category error.

---

## Thesis falsifiers

| # | Falsifier | Observable by |
|---|---|---|
| F1 | Single-customer concentration above ~45% | Quarterly 10-Q |
| F2 | Share count still rising after four more quarters | Quarterly 10-Q |
| F3 | Semiconductor operating margin below ~55% | Quarterly segment note |
| F4 | Infrastructure software revenue declining, not just decelerating | Quarterly |
| F5 | Goodwill impairment, or market cap sustained below net book value | Annual 10-K |
| F6 | A new large debt- and stock-funded acquisition | 8-K |
| F7 | Q3/Q4 GAAP margins materially below the analyst's ~50–52% assumption | 10-Q / 10-K |

---

## Evidence the analyst underweighted

- **The after-hours reaction.** A ~6.5% decline on +221% AI growth is information about
  what the market believes is already priced. The file records the fact but does not
  weigh it.
- **Serial-acquirer risk.** There is no assessment of what the *next* deal does to the
  balance sheet or share count. For this company that is not a tail risk, it is the
  business model.
- **The absence of ASP/unit disclosure.** The file notes it once. It deserves more:
  Broadcom's earnings quality is *less* verifiable than Samsung's or TSMC's on exactly
  the dimension that convicted Samsung's cycle earnings.

---

## Red-team confidence

**0.70** — the highest I have assigned in this harness. My attacks here rest on
**disclosed tier-1 facts** (rising share count, 42% concentration, negative tangible
book, net debt) rather than on unknowable probabilities. That makes them more robust
than my TSMC attacks, which reduced to geopolitics I cannot handicap.

## Verdict: **PASS** — and I concur with the conclusion

The thesis survives. It survives because it **reaches the same conclusion I would**:
`WATCH` / band `NONE`. It uses GAAP rather than the guided non-GAAP, it labels its own
FY2026 earnings build an ESTIMATE and gives the sensitivity, it records the rising
share count against its own quality argument, and it identifies the 42% concentration
as the primary gate rather than burying it.

**This is the first name in this harness where the red team does not dissent from the
position decision.** The analyst's reasoning — that AVGO's primary gate is a
*disclosure question with a definite answer*, unlike TSM's unresearchable geopolitical
gate, so waiting genuinely resolves it — is correct and is the right distinction to
draw.

**One dissent, on scoring rather than the decision.**
`incremental_roic_and_fcf_per_share` at 11/15 is still too generous. The category
explicitly asks *"Is long-term FCF per share increasing?"* and *"Is dilution controlled
during growth?"* — the answers are **no** and **no**. At 9/15 the total is 66, still
`Starter / Watch`, and the verdict is unchanged. Recorded so the scoring can be
re-examined at the next review.

**Required before any move to STARTER:** the 42% customer identified and the XPU
contract structure established. Both are answerable. Neither is answered today.


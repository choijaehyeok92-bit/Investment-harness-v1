# 2026-09-13 Remaining PRELIMINARY_REVIEW Screener

## Scope and authority

This is the mandatory first-stage Screener pass for all 50 names that remained canonical `PRELIMINARY_REVIEW` in `registry/companies.json` after the 2026-09-12 management-dedup review. It follows `AGENTS.md` and `agents/screener.md`: structural change, customer value, moat trajectory, FCF/share scaling, financing/dilution/survivability, light expectation-gap sanity check and obvious Hard Veto checks.

This review is **additive only**. `SCREEN_IN` means the company deserves Deep Analyst / Hard Veto / Valuation / Red Team work. It is not FULL_ANALYSIS, a buy approval or a portfolio position. Missing evidence is not converted into a zero score or a PASS. No company `latest.json` pointer is promoted by this review because the repository validators cannot be executed through the current GitHub connector.

## Result

- Total reviewed: **50**
- `SCREEN_IN`: **41**
- `WATCH`: **9**
- `SCREEN_OUT`: **0**
- Immediate Hard Veto FAIL asserted: **0**

The lack of SCREEN_OUT names is intentional: the screener is designed to reduce false negatives. Several WATCH names have attractive structural optionality but currently fail the evidence threshold for immediate deep-underwrite priority because cash economics, capital intensity, governance or cycle normalization remain unresolved.

## P1 deep-underwrite queue

Korea: Samsung Electro-Mechanics, HD Korea Shipbuilding & Offshore Engineering, LS ELECTRIC, Hanwha Ocean, Hyundai Rotem, Celltrion, LIG Nex1, Cosmax, Krafton, Orion, Hyosung Heavy Industries, SK Square.

U.S.: Adobe, Applied Materials, AMD, Constellation Energy, CrowdStrike, GE Vernova, Intuit, KLA, Lam Research, Oracle, Palo Alto Networks, Regeneron, Snowflake, Visa.

## WATCH / lower-priority evidence gates

| Ticker | Company | Main gate |
|---|---|---|
| 000270 | Kia | normalized auto-cycle margin, tariffs and EV-capex returns |
| 006400 | Samsung SDI | subsidy/AMPC dependence, utilization and owner cash after capex |
| 012330 | Hyundai Mobis | OEM concentration and EV-content profitability |
| 035720 | Kakao | governance, AI-platform moat and cash conversion |
| 047810 | Korea Aerospace Industries | program timing/cost recognition; Q2 profit contraction despite revenue growth |
| 373220 | LG Energy Solution | underlying loss excluding U.S. credits, capex intensity and EV pricing |
| 454910 | Doosan Robotics | unit economics, cash runway and dilution/external-capital dependence |
| TSLA | Tesla | owner cash after extraordinary capex; governance and autonomy assumptions |
| TTD | The Trade Desk | reacceleration after Q2 execution shortfall and competitive share evidence |

## Evidence highlights used in triage

- Samsung Electro-Mechanics Q2 2026 revenue KRW 3.4572tn and operating profit KRW 440.4bn, +24% and +107% YoY, with AI-server/network MLCC and high-end FCBGA demand.
- LS ELECTRIC Q2 revenue KRW 1.577tn and operating profit KRW 178.5bn, +32.2% and +64.4%, with KRW 7tn backlog.
- Celltrion Q2 revenue KRW 1.3937tn and operating profit KRW 451.8bn, +45% and +86.3%; higher-margin new products were 65% of biologics revenue.
- Orion H1 revenue KRW 1.8239tn and operating profit KRW 298.0bn, +15.5% and +17.9%.
- Hanwha Ocean Q2 revenue KRW 5.44tn and operating profit KRW 736.1bn, +65.2% and +98%.
- SK Square disclosed Sep. 10 NAV per share KRW 2,088,601, stock price KRW 1,135,000 and NAV discount 45.7%, with SK Hynix representing the dominant NAV asset.
- Applied Materials Q3 FY26 revenue $9.12bn, GAAP operating margin 33.7%, and non-GAAP FCF $2.33bn.
- CrowdStrike Q2 FY27 revenue $1.47bn, ending ARR $5.84bn and FCF $377m.
- GE Vernova Q2 orders $24.2bn, revenue $11.1bn and FCF $5.1bn, with backlog increasing $13bn sequentially.
- Oracle Q1 FY27 revenue $19.3bn, IaaS growth 121%, RPO $664bn, but Q1 FCF was negative $5bn and the company raised $20bn of common equity to fund the investment program. This keeps dilution/external-capital/incremental-ROIC gates open despite exceptional growth.
- Regeneron Q2 revenue $4.3bn, +17%; Dupixent global sales +38%, EYLEA HD U.S. +52%, Libtayo +30%.
- KLA FY26 FCF $3.77bn and capital returns $3.35bn; Lam June-quarter revenue $6.72bn with 37.4% GAAP operating margin.

## Next-stage discipline

Every SCREEN_IN name must still complete all six business-quality categories with evidence/counter-evidence/confidence, all nine Hard Veto items, reverse expectations, Bear/Base/Bull, permanent-loss case, falsifiers, increase/sell evidence, red-team review and source-quality notes. Price appreciation alone must not raise Base value; price decline alone must not authorize averaging down.

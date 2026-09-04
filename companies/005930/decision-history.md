# Decision History — 005930 삼성전자

Append-only. Do not erase prior decisions.

## 2026-09-04 — Initial underwriting

- **Decision:** `WATCH`
- **Position band:** `NONE`
- **Total score:** 66 / 100 — *Starter / Watch* (business quality 55/75; expectation gap 6/15; asymmetry 5/10)
- **Hard Veto status:** `INVESTIGATE` — no FAIL. Two open items:
  - `incremental_roic_collapse` — **HIGH** severity, the primary gate
  - `price_requires_unrealistic_bull_case` — MEDIUM
  - `fatal_concentration` — MEDIUM
  - Six vetoes PASS, including `moat_shrinkage` (direction positive) and
    `management_or_accounting_integrity` (Supreme Court acquittal confirmed 2025-07-17)
- **Expectation gap:** Thin. Price requires sustained mid-cycle operating profit of
  KRW 145–180T, some 2.5–3.1x the prior all-time peak of KRW 58.9T (2018).
  Probability-weighted 5-year return ≈ +11% total (≈2.2%/yr) on explicitly
  subjective weights of bear 0.30 / base 0.50 / bull 0.20.
- **Asymmetry:** Low permanent-loss risk (3–5% subjective) but structurally capped
  upside. At ≈KRW 1,634T of equity value a power-law outcome is arithmetically
  implausible. Bull ≈ +70–105% over five years.
- **Macro pacing:** `slow` — per `policy/macro-overlay.yaml` this adjusts pacing
  only and did **not** alter any company score. Rationale: the AI-capex complex is
  treated as a single correlated exposure, and Samsung's end demand sits inside it.

### Evidence change since prior review

First underwriting; the prior state is the `screening/2026-09-04` run, which
returned `SCREEN_IN` and ranked this name **#1** for deep work.

**Material correction to that run.** The screen argued the price did not require the
cycle peak to persist, resting on a broker figure of ~1.4x forward P/B. That figure
appears to reference 2025 and is stale. Corrected forward P/B is ≈**2.29x**
(2026E BPS KRW 109,313 against KRW 250,000), at or above the top of Samsung's
historical 0.9x–2.1x range and computed on peak-inflated book. This removes the
screen's central valuation argument in the strong form it was stated.

**New evidence not available at screening**, from the user-supplied tier-1 DART
filing of 2026-08-21 and follow-up research:

- KRW 222.6T distributable-profit headroom; KRW 254.3T separate-basis net assets *(tier-1)*
- 2026 shareholder return of KRW 90–110T approved — >5x the prior record — a 5.5–6.7% yield
- The KRW 15T buyback in the filing is for **employee share compensation, not
  cancellation** — it offsets dilution rather than reducing share count
- Real cancellation did occur separately: 73,359,314 common + 13,603,461 preferred
  on 2026-04-02 (≈KRW 14.58T), common outstanding −1.24%
- Samsung passed HBM4 qualification at NVIDIA and AMD **first**, on the Rubin
  platform; SK hynix HBM4 slipped to Q3 2026 on interface sync issues
- Industry 2027 capex projected at US$146B, ≈3.4x 2024 — the primary bear mechanism
- Lee Jae-yong acquittal confirmed by the Supreme Court on 2025-07-17, closing the
  integrity veto

### Thesis change versus the screening run

Business quality is **stronger** than the screen assumed — the HBM4 qualification
lead and the competitor's stumble are more decisive than the share numbers alone
conveyed. The **expectation gap is materially thinner** than assumed. Net effect:
the name is a better *business* and a worse *investment* than the screen concluded.

Direction of travel is favourable; the price for it is not yet.

### Why WATCH rather than STARTER or REJECT

- Not `STARTER`: `Hard Veto > Score`. The HIGH-severity `incremental_roic_collapse`
  gate is open, and the industry is committing US$146B of 2027 capex at the peak.
- Not `REJECT`: no veto reads FAIL, business evidence direction is positive, and
  permanent-loss risk is low.
- Score 66 sits in the *Starter / Watch* band. **This is a close call.** It rests on
  subjective probability weights: at bear 0.20 / base 0.50 / bull 0.30 the weighted
  return is ≈+30% and the total rises to 68–69, which would support a `STARTER`
  position. Recorded so a future reviewer can see exactly what judgement was made.

### Red team

Verdict `PASS`, confidence 0.65. Required revision before any position: re-score
`moat_trajectory` after Q4 2026, decomposing the 21%→33% HBM share move into Samsung
advance versus SK hynix retreat. If mostly the latter, moat trajectory falls to
~7/15 and the total drops below the Reject boundary.

### What would change the decision next

**To `STARTER` (1–2%)** — the primary gate must close first: a completed normalised
mid-cycle earnings model showing operating profit durably above ~KRW 180T against
the announced 2027–2029 capacity additions. Then at least two of:
HBM share ≥33% in Q4 2026 *after* SK hynix HBM4 volume arrives; disclosure of
multi-year capacity-reserved HBM contracts; January 2027 board delivering the return
materially as buyback-and-cancel exceeding the KRW 15T employee tranche; foundry
sustained quarterly operating profit with a second large external customer.

**To `REJECT`** — HBM share below 28% once SK hynix HBM4 reaches volume; or contract
prices rolling over while 2027 capex is still being spent; or CXMT demonstrating
leading-edge DRAM at volume.

**Explicitly not a reason to act either way:** price movement alone. Per
`policy/position-sizing.yaml` and `policy/monitoring.yaml`, a further decline does
not create a position and a rally does not remove one.

### Next scheduled review

Q3 2026 results (late October 2026) — per `policy/monitoring.yaml` quarterly review
checks thesis-critical KPIs only and does **not** evaluate price. Critical KPIs:
HBM share, HBM4 volume at NVIDIA, foundry operating result, capex guidance.

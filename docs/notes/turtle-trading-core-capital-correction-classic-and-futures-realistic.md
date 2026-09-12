# Turtle Trading core capital correction: classic and futures-realistic

*This is a comparative research note, not a single-strategy model card. It may compare multiple variants and does not carry a single PASS/FAIL verdict badge.*

**Generated:** 2026-09-12T08:37:15+00:00


Generated: 2026-09-12T08:37:15+00:00

## Outcome

**No margin call triggered in the full-sample futures-realistic run.**

Both corrected columns share the repaired Turtle core: 10% proactive entry-margin accounting, a separate 1.0x aggregate gross-leverage ceiling, and half-sized new units when the other system already holds the same symbol and direction. The original 4/6/10/12 caps remain. The futures-realistic column additionally retains its reactive 10% maintenance-margin liquidation/halt and lower cost assumption.

- Common sample: 2010-01-04 to 2026-09-10 (4196 sessions)
- Corrected classic: 5.0 bps per unit of notional turnover; no reactive margin call
- Futures-realistic: 0.5 bps per unit of notional turnover; liquidate and permanently halt when equity is at or below 10% of gross notional
- Execution remains LazyAlpha's close-derived, one-session-lagged weight convention

## Why the core sizing required correction

The Turtle `(equity * risk fraction) / N` formula determines notional exposure. Applied as fully paid ETF shares, a low-N instrument can consume more than the entire account in one unit. In futures, the capital reserved to establish that notional exposure is margin, normally only a fraction of notional. The proactive margin check models that capital constraint explicitly rather than assuming unlimited buying power.

LazyAlpha's return calculation already has the relevant economic equivalence: a portfolio weight times an ETF return produces the same percentage account P&L as the same notional futures exposure times the underlying return. No futures-specific return formula was added.

The original 5 bps charge was an ETF-style assumption applied to notional turnover. For scale, CME defines ES as $50 times the S&P 500 index; at an index level near 6,500 that is about $325,000 notional. Published all-in ES round-turn examples are roughly $4-$5 (Topstep lists $3.78), equal to approximately 0.12-0.15 bps of a $325,000 notional. The experiment uses 0.5 bps, deliberately about three to four times that illustrative rate and therefore not a cheapest-case choice.

Sources: [CME ES contract multiplier and margin estimate](https://www.cmegroup.com/markets/equities/sp/sandp-futures.html); [Topstep ES round-turn fees](https://help.topstep.com/en/articles/8284213-topstepx-commissions-and-fees).

CME explains that falling below maintenance margin requires restoring the account, and Schwab states that futures margin is generally 3%-12% of notional. The fixed 10% threshold is a conservative point near the upper end of that published range, appropriate for a heterogeneous multi-asset proxy universe. It was selected from real-world convention, not tuned against this backtest. This simplified experiment liquidates fully and halts permanently instead of assuming fresh capital is wired in.

Sources: [CME performance-bond and maintenance-margin FAQ](https://www.cmegroup.com/solutions/risk-management/performance-bonds-margins/faq-performance-bonds-margins.html); [Schwab futures-margin overview](https://www.schwab.com/futures/futures-margin).

The 1.0x gross-leverage ceiling is a distinct operator-mandated exposure limit: passing a 10% margin check alone could permit nearly 10x gross notional. The same-instrument overlap adjustment addresses concentration while preserving the historical simultaneous operation of Systems 1 and 2. The CFTC explicitly names leverage and position concentration among risks to measure against limits. No authoritative source prescribes a universal two-system reduction factor, so the 0.5 multiplier is disclosed as fixed operator policy, not a Turtle historical fact.

Source: [CFTC market-risk rule](https://www.cftc.gov/LawRegulation/FederalRegister/finalrules/2012-5317.html).

## Full-sample metrics

| Metric | Pre-fix classic | Corrected classic | Pre-fix futures | Corrected futures |
|---|---:|---:|---:|---:|
| Gross cumulative return | -18.47% | 52.31% | 2.38% | 52.35% |
| Net cumulative return | -98.82% | 30.63% | 2.27% | 50.03% |
| CAGR | -23.39% | 1.62% | 0.13% | 2.47% |
| Annualized volatility | 116.79% | 20.90% | 0.43% | 20.89% |
| Annualized Sharpe (rf=0) | 0.37 | 0.18 | 0.32 | 0.22 |
| Maximum drawdown | -99.94% | -51.34% | -0.06% | -49.51% |
| Annualized turnover | 50592.57% | 1843.83% | 133.37% | 1843.13% |
| Transaction-cost drag (sum daily rates) | 421.20% | 15.35% | 0.11% | 1.53% |

## Leverage, liquidation, and accounting checks

- Pre-fix classic peak / average gross leverage: 40.5299x / 14.0696x
- Pre-fix futures-realistic peak / average gross leverage: 11.0902x / 0.0042x (halted on 2010-02-08, hence the low full-sample average)
- Corrected classic peak / average gross leverage: 1.0679x / 0.7603x
- Corrected futures-realistic peak / average gross leverage: 1.0674x / 0.7599x
- Corrected classic skips: insufficient margin=0; leverage ceiling=6090; concentration-reduced units=47
- Corrected futures skips: insufficient margin=0; leverage ceiling=6090; concentration-reduced units=47
- Corrected classic internal/backtester maximum absolute equity difference: 5.58793544769e-09
- Futures internal/backtester maximum absolute equity difference: 1.04773789644e-08
- Required reconciliation tolerance: 0.0001; both passed

The reactive maintenance-margin test occurs after that day's mark-to-market and modeled turnover cost, before stops, exits, or new entries. Gross notional is the sum of absolute current unit notionals at that close. Forced-flat weights use the existing execution convention, so liquidation turnover is charged by the unchanged engine on the next session. Once called, the strategy emits zero weights permanently.

## Walk-forward metrics

Each chronological window starts an independent account with the same frozen parameters; the development/OOS split is identical for both variants.

### Development window

| Metric | Pre-fix classic | Corrected classic | Pre-fix futures | Corrected futures |
|---|---:|---:|---:|---:|
| Gross cumulative return | -84.83% | 23.63% | 2.38% | 23.63% |
| Net cumulative return | -98.92% | 12.69% | 2.27% | 22.50% |
| CAGR | -36.48% | 1.20% | 0.23% | 2.05% |
| Annualized volatility | 111.62% | 18.26% | 0.55% | 18.25% |
| Annualized Sharpe (rf=0) | 0.16 | 0.16 | 0.41 | 0.20 |
| Maximum drawdown | -99.91% | -51.34% | -0.06% | -49.51% |
| Annualized turnover | 52754.32% | 1852.83% | 222.33% | 1852.06% |
| Transaction-cost drag (sum daily rates) | 263.46% | 9.25% | 0.11% | 0.92% |

### Out-of-sample window

| Metric | Pre-fix classic | Corrected classic | Pre-fix futures | Corrected futures |
|---|---:|---:|---:|---:|
| Gross cumulative return | 115.26% | 8.97% | 0.41% | 9.00% |
| Net cumulative return | -55.20% | 1.99% | 0.30% | 8.28% |
| CAGR | -11.35% | 0.30% | 0.04% | 1.20% |
| Annualized volatility | 122.86% | 24.20% | 0.94% | 24.18% |
| Annualized Sharpe (rf=0) | 0.54 | 0.14 | 0.05 | 0.18 |
| Maximum drawdown | -98.06% | -48.19% | -1.86% | -46.86% |
| Annualized turnover | 46810.57% | 1985.60% | 327.95% | 1984.91% |
| Transaction-cost drag (sum daily rates) | 155.94% | 6.61% | 0.11% | 0.66% |

- Development window: 2010-01-04 to 2020-01-02 (2517 sessions)
- OOS window: 2020-01-03 to 2026-09-10 (1679 sessions)
- Corrected classic verdict: **FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**
- Futures-realistic verdict: **FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

## Interpretation

The futures-style mechanics materially improve the outcome on this sample, and the account never breaches the chosen maintenance threshold.

The corrected classic net return is 30.63% versus 50.03% for the futures-realistic variant. This comparison separates the effect of transaction-cost convention and forced liquidation, but it does not model contract granularity, rolls, term structure, financing/collateral yield, intraday margin checks, exchange-specific portfolio offsets, slippage, or market impact.

## Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Symbols: SPY, QQQ, IWM, TLT, IEF, GLD, SLV, DBC, USO, UUP
- Common panel: 2010-01-04 to 2026-09-10; 4196 rows
- Database: `market-data-hub configured default`

This is historical research, not a claim of tradability or an investment recommendation.

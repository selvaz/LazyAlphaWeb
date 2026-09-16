# Strategy: turn_of_month_last_1_first_3

1 variant(s) documented · earliest 2026-09-14 · latest 2026-09-14.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="calendar_effect=turn_of_month, last_sessions=1, first_sessions=3, window=day_-1_through_day_+3, allocation=equal_weight_long_or_cash"><code>calendar_effect=turn_of_month, last_sessions=1, first_sessions=3, window=day_-1…</code></a> | 2026-09-14T07:05:02+00:00 | ✓ | <span class="verdict-badge verdict-badge--fail">FAIL</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--equity" data-chart-kind="equity">
  <div class="la-chart__label">Equity time series</div>
  <img src="../../assets/charts/turn-of-month-last-1-first-3__variant-1.svg" alt="turn_of_month_last_1_first_3 variant 1 growth-of-one-dollar equity line" width="576" height="241" decoding="async">
  <figcaption>Real growth-of-$1 series · strategy vs benchmark</figcaption>
</figure>
</div>

**Generated:** 2026-09-14T07:05:02+00:00  
**Source report:** `20260914_070248_turn_of_month_last_1_first_3.md`  
**Registered:** ✓ — 2026-09-14T07:02:48+00:00 (walk_forward_passed=False)
#### Experiment

- Period: 2010-01-04 to 2026-08-14 (4179 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: calendar_effect=turn_of_month, last_sessions=1, first_sessions=3, window=day_-1_through_day_+3, allocation=equal_weight_long_or_cash

#### Turn-of-the-month construction

- Frozen window: Day -1 through Day +3 — the last observed trading session of a month and the first three observed sessions of the next month.
- Allocation: equal-weight long across the selected ETFs inside that four-session window; 100% cash otherwise.
- Timing: the calendar for the next exchange session is knowable at close t. The strategy moves the desired calendar position back one row so the central backtester's one-session shift applies it to the intended close-to-close return; no future price or return is read.
- Architecture: this is a standalone `Strategy` because the calendar is the complete source of exposure, rather than a gate applied to a price-derived base signal.
- Realized invested sessions: 798 of 4179 (19.10%); all remaining sessions are cash under the base model.
- The window was copied from Lakonishok and Smidt (1988) and McConnell and Xu (2008), not selected from this ETF sample.

### What is notable in this sample

- The strategy was exposed only 19.10% of sessions, yet its gross full-sample cumulative return was 92.14%. Repeated round trips reduced the net result to 57.30%; annualized turnover was 2412.06% at the stated 5.00-bp cost.
- The calendar effect strengthened after the frozen split: strategy CAGR rose from 2.06% in development to 3.84% OOS, and Sharpe rose from 0.33 to 0.46.
- That persistence was not enough to pass. OOS net return was 28.38% with 0.46 Sharpe, versus 214.03% and 0.89 for buy-and-hold.
- OOS maximum drawdown was -12.28%, compared with -30.86% for buy-and-hold. The lower market exposure reduced drawdown, but the repository requires both return and Sharpe to match or beat the benchmark.

#### Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: SPY, QQQ
- Validated common panel: 2010-01-04 to 2026-08-14; 4179 rows
- Database: `C:\Users\Administrator\Documents\GitHub\market-data-hub\market_data.duckdb`

| Symbol | Last date | Status | Coverage score | Stalled |
|---|---:|---|---:|---|
| QQQ | 2026-08-14 00:00:00 | ok | 97.31 | False |
| SPY | 2026-08-14 00:00:00 | ok | 97.33 | False |

#### Research rationale

Equity returns may be concentrated around the turn of each calendar month, providing a signal that depends only on the trading calendar rather than a continuous price trend.

Hold the selected equity ETFs at equal weight from the last trading session of each month through the first three trading sessions of the next month, and hold cash on all other sessions. The Day -1 through Day +3 window is copied from the cited literature and frozen before this sample is evaluated.

Sources:

- [Are Seasonal Anomalies Real? A Ninety-Year Perspective](https://doi.org/10.1093/rfs/1.4.403) — Lakonishok and Smidt document persistent anomalous Dow returns around the turn of the month over 1897-1986.
- [Equity Returns at the Turn of the Month](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1135217) — McConnell and Xu define the canonical interval as Day -1 through Day +3, confirm it in U.S. data through 2005, and report it in 31 of 35 countries examined.
- [A Monthly Effect in Stock Returns](https://doi.org/10.1016/0304-405X(87)90066-3) — Ariel provides early peer-reviewed evidence that positive market returns cluster immediately before and during the early part of calendar months.

Known risks:

- a published anomaly can weaken after discovery or vary across market regimes
- four invested sessions per month leave most capital in zero-return cash under the base model
- frequent entry and exit makes the result sensitive to trading costs and slippage
- the ETF sample is much newer and shorter than the index histories in the cited studies
- calendar dates are known in advance, but unexpected exchange closures can alter the realized session sequence
- one historical sample is not evidence of future profitability

#### Net backtest metrics

| Metric | Strategy | Benchmark |
|---|---:|---:|
| Gross cumulative return | 92.14% | 1207.96% |
| Cumulative return | 57.30% | 1207.31% |
| CAGR | 2.77% | 16.77% |
| Annualized volatility | 7.97% | 18.56% |
| Annualized Sharpe (rf=0) | 0.38 | 0.93 |
| Maximum drawdown | -13.03% | -30.86% |
| Annualized turnover | 2412.06% | 6.03% |
| Transaction-cost drag (sum of daily rates) | 20.00% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2010-01-04 to 2019-12-17 | 2507 | 22.53% | 2.06% | 7.04% | 0.33 | -13.03% | 315.92% | 0.99 | -293.39% | -0.67 |
| oos_1 | out_of_sample | 2019-12-18 to 2026-08-14 | 1672 | 28.38% | 3.84% | 9.18% | 0.46 | -12.28% | 214.03% | 0.89 | -185.65% | -0.43 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

#### Conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

This remains historical research, not evidence of tradability or a recommendation. There is still no parameter-search correction or project-level multiple-testing adjustment for this strategy; promotion also requires a live paper period.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

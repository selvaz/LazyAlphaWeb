# Strategy: cross_sectional_momentum_12_1_long_short

1 variant(s) documented · earliest 2026-09-13 · latest 2026-09-13.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="lookback_days=252, skip_days=21, n_select=3, rebalance=calendar_month_end, rule=equal_weight_top_and_bottom, gross_exposure=1.0, long_gross=0.5, short_gross=0.5"><code>lookback_days=252, skip_days=21, n_select=3, rebalance=calendar_month_end, rule…</code></a> | 2026-09-13T09:24:17+00:00 | ✓ | <span class="verdict-badge verdict-badge--fail">FAIL</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--equity" data-chart-kind="equity">
  <div class="la-chart__label">Equity time series</div>
  <img src="../../assets/charts/cross-sectional-momentum-12-1-long-short__variant-1.svg" alt="cross_sectional_momentum_12_1_long_short variant 1 growth-of-one-dollar equity line" width="576" height="241" decoding="async">
  <figcaption>Real growth-of-$1 series · strategy vs benchmark</figcaption>
</figure>
</div>

**Generated:** 2026-09-13T09:24:17+00:00  
**Source report:** `20260913_092417_cross_sectional_momentum_12_1_long_short.md`  
**Registered:** ✓ — 2026-09-13T09:24:17+00:00 (walk_forward_passed=False)
#### Experiment

- Period: 2010-01-04 to 2026-08-14 (4178 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: lookback_days=252, skip_days=21, n_select=3, rebalance=calendar_month_end, rule=equal_weight_top_and_bottom, gross_exposure=1.0, long_gross=0.5, short_gross=0.5

#### Cross-sectional momentum construction

- Frozen universe: SPY, QQQ, IWM, TLT, IEF, GLD, SLV, DBC, USO, UUP.
- Ranking score: `adjusted-close total return P[t-21] / P[t-252] - 1`.
- Rebalance: last observed session of each calendar month; execution: ranking close t applied by run_backtest on session t+1.
- Portfolio: equal-weight the top three at +0.5 total long exposure and the bottom three at -0.5 total short exposure. The remaining four assets are flat; gross exposure is 1.0 and net exposure is zero.
- The 252-session lookback, 21-session skip, and three assets per leg were frozen from the cited 12-minus-1-month, three-assets-per-quartile cross-asset construction before this sample was evaluated.

### Ex-post breadth sensitivity (diagnostic only)

The neighboring two-, three-, and four-assets-per-leg variants were run after the frozen verdict. They were not used to select the reported rule.

| Assets per leg | Frozen | Full-sample CAGR | Full-sample Sharpe | Full-sample max drawdown | OOS CAGR | OOS Sharpe | OOS max drawdown |
|---:|:---:|---:|---:|---:|---:|---:|---:|
| 2 |  | 4.52% | 0.39 | -31.28% | 4.08% | 0.36 | -25.31% |
| 3 | yes | 2.90% | 0.31 | -27.19% | 2.51% | 0.28 | -26.38% |
| 4 |  | 3.42% | 0.41 | -23.01% | 2.67% | 0.34 | -23.01% |

This sensitivity check addresses concentration stability only. It does not correct survivorship bias in the fixed ETF universe, supply a longer pre-ETF history, or model short borrow and financing costs.

#### Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: SPY, QQQ, IWM, TLT, IEF, GLD, SLV, DBC, USO, UUP
- Validated common panel: 2010-01-04 to 2026-08-14; 4178 rows
- Database: `C:\Users\Administrator\Documents\GitHub\market-data-hub\market_data.duckdb`

| Symbol | Last date | Status | Coverage score | Stalled |
|---|---:|---|---:|---|
| DBC | 2026-08-14 00:00:00 | ok | 94.31 | False |
| GLD | 2026-08-14 00:00:00 | ok | 94.32 | False |
| IEF | 2026-08-14 00:00:00 | ok | 97.31 | False |
| IWM | 2026-08-14 00:00:00 | ok | 97.31 | False |
| QQQ | 2026-08-14 00:00:00 | ok | 97.31 | False |
| SLV | 2026-08-14 00:00:00 | ok | 94.31 | False |
| SPY | 2026-08-14 00:00:00 | ok | 97.33 | False |
| TLT | 2026-08-14 00:00:00 | ok | 97.32 | False |
| USO | 2026-08-14 00:00:00 | ok | 94.31 | False |
| UUP | 2026-08-14 00:00:00 | ok | 94.31 | False |

#### Research rationale

Assets with the strongest intermediate-horizon relative returns may continue to outperform the weakest assets. Ranking the whole multi-asset panel makes this a cross-sectional allocation rule, distinct from a directional trend signal on each ETF.

At each calendar month-end, rank the ten confirmed Turtle-universe ETFs by adjusted-close total return from 252 sessions ago through 21 sessions ago. Hold equal-weight long positions in the top three and equal-weight shorts in the bottom three, with 0.5 gross on each side, until the next month-end. The common engine executes the new weights one session after the ranking close.

Sources:

- [Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency](https://doi.org/10.1111/j.1540-6261.1993.tb04702.x) — Jegadeesh and Titman establish the classic relative-strength winner-minus-loser portfolio and document intermediate-horizon momentum while motivating omission of the short reversal horizon.
- [Global Tactical Cross-Asset Allocation: Applying Value and Momentum Across Asset Classes](https://doi.org/10.3905/JPM.2008.35.1.23) — Blitz and van Vliet test 12-minus-1-month momentum across twelve liquid asset classes, rebalance monthly, and form equal-weight top and bottom quartiles of three assets each.
- [Empirical evidence on the profitability of momentum trading strategies using ETFs](https://doi.org/10.1108/MF-01-2019-0046) — Yu and Webb apply traditional total-return rankings to plain-equity ETFs and find that past momentum is not a strong predictor over their full 2007-June 2018 sample, an important modern caution.
- [Momentum Crashes](https://doi.org/10.1016/j.jfineco.2015.12.002) — Daniel and Moskowitz document infrequent, persistent momentum crashes, especially after market declines and during rebounds.

Known risks:

- momentum can crash during sharp market rebounds and regime changes
- ten ETFs provide a small cross-section and several share common risk exposures
- the ETF history fixes today's surviving universe and does not test delisted funds
- short borrow fees, financing, bid/ask spread, slippage and market impact are absent
- recent ETF evidence finds total-return momentum can be weak over some samples
- one historical test is not evidence of future profitability

#### Net backtest metrics

| Metric | Strategy | Benchmark |
|---|---:|---:|
| Gross cumulative return | 66.20% | 259.55% |
| Cumulative return | 60.63% | 259.37% |
| CAGR | 2.90% | 8.02% |
| Annualized volatility | 11.11% | 10.63% |
| Annualized Sharpe (rf=0) | 0.31 | 0.78 |
| Maximum drawdown | -27.19% | -23.48% |
| Annualized turnover | 412.16% | 6.03% |
| Transaction-cost drag (sum of daily rates) | 3.42% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2010-01-04 to 2019-12-16 | 2506 | 21.72% | 2.00% | 9.91% | 0.25 | -27.19% | 65.32% | 0.60 | -43.61% | -0.35 |
| oos_1 | out_of_sample | 2019-12-17 to 2026-08-14 | 1672 | 17.88% | 2.51% | 10.86% | 0.28 | -26.38% | 116.86% | 0.99 | -98.98% | -0.71 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

#### Conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

This remains historical research, not evidence of tradability or a recommendation. There is still no parameter-search correction or project-level multiple-testing adjustment for this strategy; promotion also requires a live paper period.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

# Strategy: minimum_variance_portfolio

1 variant(s) documented · earliest 2026-09-13 · latest 2026-09-13.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="lookback=252, rebalance=monthly_first_trading_session_close, constraints=long_only_fully_invested, solver=exact_support_enumeration, covariance=sample_covariance, ridge=1e-08"><code>lookback=252, rebalance=monthly_first_trading_session_close, constraints=long_o…</code></a> | 2026-09-13T09:25:35+00:00 | ✓ | <span class="verdict-badge verdict-badge--fail">FAIL</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--equity" data-chart-kind="equity">
  <div class="la-chart__label">Equity time series</div>
  <img src="../../assets/charts/minimum-variance-portfolio__variant-1.svg" alt="minimum_variance_portfolio variant 1 growth-of-one-dollar equity line" width="576" height="241" decoding="async">
  <figcaption>Real growth-of-$1 series · strategy vs benchmark</figcaption>
</figure>
</div>

**Generated:** 2026-09-13T09:25:35+00:00  
**Source report:** `20260913_092243_minimum_variance_portfolio.md`  
**Registered:** ✓ — 2026-09-13T09:22:44+00:00 (walk_forward_passed=False)
#### Experiment

- Period: 2010-01-04 to 2026-09-11 (4197 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: lookback=252, rebalance=monthly_first_trading_session_close, constraints=long_only_fully_invested, solver=exact_support_enumeration, covariance=sample_covariance, ridge=1e-08

#### Portfolio-construction method

- Objective: minimize `w'Σw` subject to `w_i >= 0` and `sum(w) = 1`; there is no directional or long/short signal.
- Universe: SPY, QQQ, IWM, TLT, IEF, GLD, SLV, DBC, USO, UUP; this is the exact ten-ETF universe with verified Turtle experiment coverage.
- Covariance input: trailing 252 daily close-to-close returns through each rebalance close; exposure remains zero until a complete window exists.
- Rebalance timing: first trading-session close of each month; the central backtester applies the new weights one session later.
- Solver: enumerate every non-empty support in the ten-asset universe, solve the equality-constrained global minimum on that support, discard negative-weight solutions, and retain the feasible portfolio with the lowest variance. This is an exact solution of the small long-only problem and avoids an undeclared QP dependency.
- Numerical stabilization: add `1e-08` times the mean covariance diagonal to the diagonal. This fixed numerical ridge is not a fitted shrinkage model.
- Primary benchmark: monthly strategy versus continuously equal-weighted 1/N on the same ten ETFs. SPY/QQQ equal-weight buy-and-hold is retained as a continuity benchmark.

#### Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: SPY, QQQ, IWM, TLT, IEF, GLD, SLV, DBC, USO, UUP
- Validated common panel: 2010-01-04 to 2026-09-11; 4197 rows
- Database: `market-data-hub configured default`

| Symbol | Last date | Status | Coverage score | Stalled |
|---|---:|---|---:|---|
| DBC | 2026-09-11 00:00:00 | ok | 95.50 | False |
| GLD | 2026-09-11 00:00:00 | ok | 95.50 | False |
| IEF | 2026-09-11 00:00:00 | ok | 98.50 | False |
| IWM | 2026-09-11 00:00:00 | ok | 98.50 | False |
| QQQ | 2026-09-11 00:00:00 | ok | 98.50 | False |
| SLV | 2026-09-11 00:00:00 | ok | 95.50 | False |
| SPY | 2026-09-11 00:00:00 | ok | 98.52 | False |
| TLT | 2026-09-11 00:00:00 | ok | 98.51 | False |
| USO | 2026-09-11 00:00:00 | ok | 95.50 | False |
| UUP | 2026-09-11 00:00:00 | ok | 95.51 | False |

#### Research rationale

A covariance-only allocation across the already-covered ETF universe may reduce portfolio volatility and drawdowns relative to equal capital weights, without forecasting return direction.

At the first close of each month, estimate the covariance matrix from the trailing 252 daily returns and minimize w'Cov(w) subject to every weight being non-negative and weights summing to one.

Sources:

- [Portfolio Selection](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x) — Establishes portfolio selection through joint expected return and variance rather than evaluating assets alone.
- [Minimum-Variance Portfolios in the U.S. Equity Market](https://doi.org/10.3905/jpm.2006.661366) — Shows that the global minimum-variance portfolio depends on covariance estimates and not expected-return forecasts.
- [Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?](https://doi.org/10.1093/rfs/hhm075) — Finds optimized portfolios did not consistently beat 1/N out of sample, making equal weight the necessary benchmark.
- [Estimating portfolio risk for tail risk protection strategies](https://doi.org/10.1111/eufm.12256) — Evaluates portfolio-risk estimation on a global data set spanning equities, fixed income, commodities and currencies.
- [Portfolio Protection? It's a Long (Term) Story](https://www.aqr.com/-/media/AQR/Documents/Journal-Articles/Portfolio-Protection-Its-a-Long-Term-Story.pdf) — Recent practitioner research evaluates risk-balanced exposure across global stocks, bonds and commodities and reports results net of estimated transaction costs.

Known risks:

- sample covariances are noisy and optimized weights can concentrate
- the 252-session estimate can react slowly to regime changes
- monthly re-optimization creates turnover and transaction costs
- ETF history has survivorship and proxy limitations
- one historical sample is not evidence of future performance

#### Net backtest metrics

| Metric | Strategy | SPY/QQQ buy-and-hold | Equal-weight same-universe benchmark |
|---|---:|---:|---:|
| Gross cumulative return | 86.09% | 1183.39% | 265.92% |
| Cumulative return | 84.98% | 1182.75% | 265.74% |
| CAGR | 3.76% | 16.56% | 8.10% |
| Annualized volatility | 3.19% | 18.53% | 10.62% |
| Annualized Sharpe (rf=0) | 1.17 | 0.92 | 0.79 |
| Maximum drawdown | -5.12% | -30.86% | -23.48% |
| Annualized turnover | 72.28% | 6.00% | 6.00% |
| Transaction-cost drag (sum of daily rates) | 0.60% | 0.05% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2010-01-04 to 2020-01-03 | 2518 | 39.95% | 3.42% | 2.90% | 1.17 | -5.12% | 69.39% | 0.63 | -29.44% | 0.55 |
| oos_1 | out_of_sample | 2020-01-06 to 2026-09-11 | 1679 | 31.61% | 4.21% | 3.11% | 1.34 | -4.35% | 115.40% | 0.98 | -83.78% | 0.36 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

### Continuity benchmark: SPY/QQQ buy-and-hold

The identical frozen strategy windows are compared with equal-weight SPY/QQQ exposure held inside the same full panel.

| Window | Role | Period | Strategy return | Strategy Sharpe | SPY/QQQ return | SPY/QQQ Sharpe |
|---|---|---|---:|---:|---:|---:|
| development | development | 2010-01-04 to 2020-01-03 | 39.95% | 1.17 | 324.02% | 1.00 |
| oos_1 | out_of_sample | 2020-01-06 to 2026-09-11 | 31.61% | 1.34 | 200.83% | 0.86 |

The same return-and-Sharpe criterion is applied to every OOS window.

**SPY/QQQ walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

### OOS risk and implementation metrics by benchmark

| Window | Portfolio | CAGR | Sharpe | Max drawdown | Annualized turnover |
|---|---|---:|---:|---:|---:|
| oos_1 | minimum variance | 4.21% | 1.34 | -4.35% | 73.29% |
| oos_1 | equal weight same universe | 12.21% | 0.98 | -23.48% | 15.01% |
| oos_1 | SPY/QQQ buy-and-hold | 17.98% | 0.86 | -30.86% | 15.01% |

#### Conclusion

**Full-sample comparison: INCONCLUSIVE: better on only one of net return and Sharpe.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

**Full-sample SPY/QQQ comparison: MIXED; the strategy trails return and beats Sharpe.**

**Benchmark-specific OOS judgments: equal-weight same-universe FAIL; SPY/QQQ buy-and-hold FAIL.**

This remains historical research, not evidence of tradability or a recommendation. There is still no parameter-search correction or project-level multiple-testing adjustment for this strategy; promotion also requires a live paper period.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

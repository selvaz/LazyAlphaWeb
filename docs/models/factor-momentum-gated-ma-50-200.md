# Strategy: factor_momentum_gated_ma_50_200

1 variant(s) documented · earliest 2026-09-12 · latest 2026-09-12.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="fast=50, slow=200, lookback_days=252, factor_set=MOM_daily, factor=Mom, active_threshold=0.0"><code>fast=50, slow=200, lookback_days=252, factor_set=MOM_daily, factor=Mom, active_…</code></a> | 2026-09-12T15:36:33+00:00 | ✓ | <span class="verdict-badge verdict-badge--fail">FAIL</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--equity" data-chart-kind="equity">
  <div class="la-chart__label">Equity time series</div>
  <img src="../../assets/charts/factor-momentum-gated-ma-50-200__variant-1.svg" alt="factor_momentum_gated_ma_50_200 variant 1 growth-of-one-dollar equity line" width="576" height="241" decoding="async">
  <figcaption>Real growth-of-$1 series · strategy vs benchmark</figcaption>
</figure>
</div>

**Generated:** 2026-09-12T15:36:33+00:00  
**Source report:** `20260912_153633_factor_momentum_gated_ma_50_200.md`  
**Registered:** ✓ — 2026-09-12T15:36:33+00:00 (walk_forward_passed=False)
#### Experiment

- Period: 2015-01-02 to 2026-06-30 (2889 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: fast=50, slow=200, lookback_days=252, factor_set=MOM_daily, factor=Mom, active_threshold=0.0

#### Factor-momentum data provenance and action rule

- Source: `market-data-hub factor_returns`
- Series: factor set `MOM_daily`, factor `Mom`
- Available raw factor history through the experiment end: 1990-01-02 to 2026-06-30; 9190 non-null daily rows
- Database: `C:\Users\Administrator\Documents\GitHub\market-data-hub\market_data.duckdb`
- Frozen horizon: 252 factor sessions, matching the approximately one-year horizon in Ehsani and Linnainmaa (2022); it was pre-specified and not fitted to these strategy returns
- Frozen gate: compound `Mom` daily returns over the trailing window; a return `>= 0` applies the existing MA weights and a negative return zeros them, never creating a short position
- Timing: the factor return through session D enters the close-derived gate for D, and the common backtest engine applies that weight one session later
- Any missing required factor date or incomplete trailing window raises `FactorMomentumDataUnavailable`; no unconditional fallback, forward fill, or invented value is allowed
- Research scope caveat: this is inspired by the paper, not a replication. The paper tests cross-sectional factor rotation and individual-stock momentum, not a temporal on/off gate for an unrelated ETF trend strategy. The market-wide gate used here is a motivated extrapolation that the paper did not test.

#### Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: SPY, QQQ
- Validated common panel: 2015-01-02 to 2026-06-30; 2889 rows
- Database: `C:\Users\Administrator\Documents\GitHub\market-data-hub\market_data.duckdb`

| Symbol | Last date | Status | Coverage score | Stalled |
|---|---:|---|---:|---|
| QQQ | 2026-08-14 00:00:00 | ok | 97.31 | False |
| SPY | 2026-08-14 00:00:00 | ok | 97.33 | False |

#### Research rationale

The momentum factor's own trailing annual return may indicate whether factor-level momentum is currently working, providing a motivated on/off condition for the existing equity trend allocation.

Compound the daily Mom factor over a frozen 252-session trailing window. Apply the existing 50/200 SPY/QQQ moving-average weights when that return is nonnegative and otherwise hold cash; retain the backtest engine's one-session execution lag. The 252-session horizon matches the paper's approximately one-year horizon and was pre-specified rather than fitted to this backtest.

Sources:

- [Factor Momentum and the Momentum Factor](https://www.nber.org/papers/w25551) — Ehsani and Linnainmaa find positive factor-return autocorrelation at roughly a one-year horizon: factors with a losing trailing year subsequently earn about 6 basis points per month versus about 51 basis points after a winning year, and factor momentum explains most individual-stock momentum.
- [Factor Momentum and the Momentum Factor (journal record)](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.13131) — The peer-reviewed journal version documents the same factor-momentum evidence and its relation to stock momentum.

Known risks:

- inspired-by, not a replication: the paper studies cross-sectional factor rotation and individual-stock momentum, not a temporal on/off gate applied to an unrelated ETF trend strategy
- using the sign of the momentum factor's own trailing return as a market-wide gate is a motivated extrapolation that the paper did not test
- factor returns are close-derived and only affect positions after the backtest engine's one-session execution lag
- cash return is modeled as zero and execution frictions are incomplete
- one historical sample is not evidence of future profitability

#### Net backtest metrics

| Metric | Strategy | Ungated MA | Benchmark |
|---|---:|---:|---:|
| Gross cumulative return | 52.72% | 316.71% | 491.34% |
| Cumulative return | 47.32% | 312.14% | 491.04% |
| CAGR | 3.44% | 13.15% | 16.76% |
| Annualized volatility | 14.36% | 16.74% | 19.47% |
| Annualized Sharpe (rf=0) | 0.31 | 0.82 | 0.89 |
| Maximum drawdown | -30.86% | -30.86% | -30.86% |
| Annualized turnover | 628.04% | 191.90% | 8.72% |
| Transaction-cost drag (sum of daily rates) | 3.60% | 1.10% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2015-01-02 to 2021-11-17 | 1733 | 2.22% | 0.32% | 15.11% | 0.10 | -30.86% | 226.86% | 1.01 | -224.64% | -0.91 |
| oos_1 | out_of_sample | 2021-11-18 to 2026-06-30 | 1156 | 45.01% | 8.44% | 12.92% | 0.69 | -20.78% | 79.50% | 0.73 | -34.49% | -0.04 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

This remains historical research, not evidence of tradability or a recommendation. There is still no parameter-search correction or project-level multiple-testing adjustment for this strategy; promotion also requires a live paper period.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

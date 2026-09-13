# Strategy: ma_crossover_grid_searched

1 variant(s) documented · earliest 2026-09-12 · latest 2026-09-12.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="fast=10, slow=150, selection_method=development_only_grid_search, selection_metric=sharpe_annualized, grid_size=9"><code>fast=10, slow=150, selection_method=development_only_grid_search, selection_met…</code></a> | 2026-09-12T14:16:11+00:00 | ✓ | <span class="verdict-badge verdict-badge--fail">FAIL</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--equity" data-chart-kind="equity">
  <div class="la-chart__label">Equity time series</div>
  <img src="../../assets/charts/ma-crossover-grid-searched__variant-1.svg" alt="ma_crossover_grid_searched variant 1 growth-of-one-dollar equity line" loading="lazy">
  <figcaption>Real growth-of-$1 series · strategy vs benchmark</figcaption>
</figure>
</div>

**Generated:** 2026-09-12T14:16:11+00:00  
**Source report:** `20260912_141611_ma_crossover_grid_searched.md`  
**Registered:** ✓ — 2026-09-12T14:16:11+00:00 (walk_forward_passed=False)
#### Experiment

- Period: 2015-01-02 to 2026-08-14 (2921 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: fast=10, slow=150, selection_method=development_only_grid_search, selection_metric=sharpe_annualized, grid_size=9

#### Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: SPY, QQQ
- Validated common panel: 2015-01-02 to 2026-08-14; 2921 rows
- Database: `C:\Users\Administrator\Documents\GitHub\market-data-hub\market_data.duckdb`

| Symbol | Last date | Status | Coverage score | Stalled |
|---|---:|---|---:|---|
| QQQ | 2026-08-14 00:00:00 | ok | 97.31 | False |
| SPY | 2026-08-14 00:00:00 | ok | 97.33 | False |

#### Research rationale

A slow trend filter may reduce severe drawdowns, but after costs it need not beat passive exposure.

For each ETF, hold it when its 50-day moving average is above its 200-day average; equal-weight active ETFs; otherwise cash.

Sources:

- [A Quantitative Approach to Tactical Asset Allocation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461) — Motivates a simple trend-following tactical allocation rule across asset classes.
- [A Quantitative Approach to Faber's Tactical Asset Allocation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1476225) — Warns that attractive rule-based results require statistical caution and bootstrap-style robustness tests.
- [Momentum Trading, Return Chasing, and Predictable Crashes](https://www.nber.org/papers/w20660) — Documents high historical momentum returns alongside material and sometimes predictable crash risk.

Known risks:

- whipsaw and repeated transaction costs in sideways markets
- parameter/data-mining sensitivity
- cash return is modeled as zero in the MVP
- one historical sample is not evidence of future profitability

#### Parameter search and multiple-testing

### Development-only grid search

- Development window used for every candidate and for selection: 2015-01-02 to 2021-12-15 (1752 sessions). No OOS observation was passed to a candidate backtest or selection calculation.
- Pre-specified grid: fast in {10, 20, 50}, slow in {100, 150, 200} (9 combinations).
- Selection metric: `sharpe_annualized`; selected parameters: **fast=10, slow=150**.

| Parameters | Selected | Development return | Development CAGR | Development Sharpe | Development max drawdown |
|---|:---:|---:|---:|---:|---:|
| fast=10, slow=100 |  | 112.85% | 11.48% | 0.8456 | -18.98% |
| fast=10, slow=150 | yes | 143.38% | 13.65% | 0.9205 | -25.15% |
| fast=10, slow=200 |  | 128.38% | 12.61% | 0.8302 | -31.72% |
| fast=20, slow=100 |  | 86.63% | 9.39% | 0.6449 | -29.19% |
| fast=20, slow=150 |  | 109.70% | 11.24% | 0.7357 | -29.29% |
| fast=20, slow=200 |  | 120.47% | 12.04% | 0.7883 | -29.13% |
| fast=50, slow=100 |  | 99.83% | 10.47% | 0.6700 | -29.99% |
| fast=50, slow=150 |  | 121.60% | 12.13% | 0.7415 | -30.86% |
| fast=50, slow=200 |  | 144.26% | 13.71% | 0.8258 | -30.86% |

### Within-family White Reality Check

- Benchmark-relative null: no grid candidate has positive expected net daily return relative to buy_and_hold.
- Observed maximum statistic across all 9 candidates: -0.007474.
- Stationary bootstrap: 2000 replications, mean block length 20 sessions, fixed NumPy random seed `1729`.
- **Reality-check p-value: 0.992504.** This is a familywise test of the entire searched grid, not an unadjusted p-value for only the winning cell.
- Method sources: [White (2000), *A Reality Check for Data Snooping*](https://doi.org/10.1111/1468-0262.00152); [Politis and Romano (1994), *The Stationary Bootstrap*](https://doi.org/10.1080/01621459.1994.10476870).

### Project-level multiplicity disclosure (not a formal correction)

- **14 independent hypotheses have now been tested in this project including this experiment.** Each append-only registry record is counted as one tested experiment, including distinct cost-model iterations. This count is disclosed separately and is not folded into the within-grid reality-check p-value.

#### Net backtest metrics

| Metric | Strategy | Benchmark |
|---|---:|---:|
| Gross cumulative return | 250.27% | 500.92% |
| Cumulative return | 241.25% | 500.62% |
| CAGR | 11.17% | 16.73% |
| Annualized volatility | 14.59% | 19.44% |
| Annualized Sharpe (rf=0) | 0.80 | 0.89 |
| Maximum drawdown | -28.39% | -30.86% |
| Annualized turnover | 448.61% | 8.63% |
| Transaction-cost drag (sum of daily rates) | 2.60% | 0.05% |

#### Walk-forward / out-of-sample validation

The development window was used for parameter selection; the selected parameters were then frozen before any OOS window was evaluated. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2015-01-02 to 2021-12-15 | 1752 | 143.38% | 13.65% | 15.16% | 0.92 | -25.15% | 227.51% | 1.00 | -84.14% | -0.08 |
| oos_1 | out_of_sample | 2021-12-16 to 2026-08-14 | 1169 | 66.18% | 11.57% | 13.25% | 0.89 | -13.64% | 86.52% | 0.77 | -20.34% | 0.13 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

This remains historical research, not evidence of tradability or a recommendation. The within-grid correction and project-level multiplicity disclosure above are now computed; promotion still requires a live paper period and a defensible result on both the reality check and frozen OOS validation.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

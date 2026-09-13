# Strategy: ma_crossover_5_20

1 variant(s) documented · earliest 2026-09-13 · latest 2026-09-13.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="fast=5, slow=20"><code>fast=5, slow=20</code></a> | 2026-09-13T06:34:39+00:00 | — | <span class="verdict-badge verdict-badge--fail">FAIL</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--equity" data-chart-kind="equity">
  <div class="la-chart__label">Equity time series</div>
  <img src="../../assets/charts/ma-crossover-5-20__variant-1.svg" alt="ma_crossover_5_20 variant 1 growth-of-one-dollar equity line" width="576" height="241" decoding="async">
  <figcaption>Real growth-of-$1 series · strategy vs benchmark</figcaption>
</figure>
</div>

**Generated:** 2026-09-13T06:34:39+00:00  
**Source report:** `20260913_063439_ma_crossover_5_20.md`  
**Registered:** —
#### Experiment

- Period: 2020-01-01 to 2022-11-23 (756 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: fast=5, slow=20

#### Data provenance

- Source: `synthetic-explicit-test-only` (`generated`; live rows included: `False`)
- Requested symbols: A, B, C
- Validated common panel: 2020-01-01 to 2022-11-23; 756 rows
- Database: `market-data-hub configured default`

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

#### Net backtest metrics

| Metric | Strategy | Benchmark |
|---|---:|---:|
| Gross cumulative return | -10.03% | -4.97% |
| Cumulative return | -15.65% | -5.02% |
| CAGR | -5.51% | -1.70% |
| Annualized volatility | 12.06% | 9.22% |
| Annualized Sharpe (rf=0) | -0.41 | -0.14 |
| Maximum drawdown | -24.34% | -14.56% |
| Annualized turnover | 4300.00% | 33.33% |
| Transaction-cost drag (sum of daily rates) | 6.45% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2020-01-01 to 2021-09-24 | 453 | -12.65% | -7.25% | 11.98% | -0.57 | -19.66% | -9.38% | -0.55 | -3.28% | -0.02 |
| oos_1 | out_of_sample | 2021-09-27 to 2022-11-23 | 303 | -1.89% | -1.58% | 11.49% | -0.08 | -15.01% | 3.72% | 0.38 | -5.61% | -0.46 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

This remains historical research, not evidence of tradability or a recommendation. There is still no parameter-search correction or project-level multiple-testing adjustment for this strategy; promotion also requires a live paper period.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

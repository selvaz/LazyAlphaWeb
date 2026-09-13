# Strategy: ma_crossover_50_200

1 variant(s) documented · earliest 2026-09-12 · latest 2026-09-12.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="fast=50, slow=200"><code>fast=50, slow=200</code></a> | 2026-09-12T15:36:34+00:00 | ✓ | <span class="verdict-badge verdict-badge--pass">PASS</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--pass">PASS</span>
</div>
<figure class="la-chart la-chart--equity" data-chart-kind="equity">
  <div class="la-chart__label">Equity time series</div>
  <img src="../../assets/charts/ma-crossover-50-200__variant-1.svg" alt="ma_crossover_50_200 variant 1 growth-of-one-dollar equity line" width="576" height="241" decoding="async">
  <figcaption>Real growth-of-$1 series · strategy vs benchmark</figcaption>
</figure>
</div>

**Generated:** 2026-09-12T15:36:34+00:00  
**Source report:** `20260912_153634_ma_crossover_50_200.md`  
**Registered:** ✓ — 2026-09-12T15:36:34+00:00 (walk_forward_passed=True)
#### Experiment

- Period: 2015-01-02 to 2026-08-14 (2921 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: fast=50, slow=200

#### Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: SPY, QQQ, IWM
- Validated common panel: 2015-01-02 to 2026-08-14; 2921 rows
- Database: `C:\Users\Administrator\Documents\GitHub\market-data-hub\market_data.duckdb`

| Symbol | Last date | Status | Coverage score | Stalled |
|---|---:|---|---:|---|
| IWM | 2026-08-14 00:00:00 | ok | 97.31 | False |
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

#### Net backtest metrics

| Metric | Strategy | Benchmark |
|---|---:|---:|
| Gross cumulative return | 252.54% | 385.29% |
| Cumulative return | 246.93% | 385.04% |
| CAGR | 11.33% | 14.59% |
| Annualized volatility | 16.86% | 19.57% |
| Annualized Sharpe (rf=0) | 0.72 | 0.79 |
| Maximum drawdown | -34.61% | -34.25% |
| Annualized turnover | 276.07% | 8.63% |
| Transaction-cost drag (sum of daily rates) | 1.60% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2015-01-02 to 2021-12-15 | 1752 | 114.91% | 11.63% | 17.46% | 0.72 | -34.61% | 181.44% | 0.87 | -66.53% | -0.15 |
| oos_1 | out_of_sample | 2021-12-16 to 2026-08-14 | 1169 | 80.25% | 13.54% | 14.87% | 0.93 | -21.18% | 75.46% | 0.70 | 4.79% | 0.22 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: PASS: coherent between development and OOS; the frozen strategy matches or beats the benchmark on return and Sharpe in every OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: PASS: coherent between development and OOS; the frozen strategy matches or beats the benchmark on return and Sharpe in every OOS window.**

This remains historical research, not evidence of tradability or a recommendation. There is still no parameter-search correction or project-level multiple-testing adjustment for this strategy; promotion also requires a live paper period.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

# Strategy: ma_crossover_50_200

1 variant(s) documented · earliest 2026-09-11 · latest 2026-09-11.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="fast=50, slow=200"><code>fast=50, slow=200</code></a> | 2026-09-11T16:38:20+00:00 | ✓ | <span class="verdict-badge verdict-badge--pass">PASS</span> |

### Variant 1 {: #variant-1 }

**Generated:** 2026-09-11T16:38:20+00:00  
**Source report:** `20260911_163820_ma_crossover_50_200.md`  
**Registered:** ✓ — 2026-09-11T16:38:20+00:00 (walk_forward_passed=True)

<span class="verdict-badge verdict-badge--pass">PASS</span>

<img src="../assets/charts/ma-crossover-50-200__variant-1.svg" alt="ma_crossover_50_200 variant 1 return and Sharpe comparison">
#### Experiment

- Period: 2015-01-02 to 2026-08-14 (2921 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: fast=50, slow=200

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

#### Net backtest metrics

| Metric | Strategy | Benchmark |
|---|---:|---:|
| Cumulative return | 318.82% | 500.62% |
| CAGR | 13.15% | 16.73% |
| Annualized volatility | 16.74% | 19.44% |
| Annualized Sharpe (rf=0) | 0.82 | 0.89 |
| Maximum drawdown | -30.86% | -30.86% |
| Annualized turnover | 189.80% | 8.63% |
| Transaction-cost drag (sum of daily rates) | 1.10% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2015-01-02 to 2021-12-15 | 1752 | 144.26% | 13.71% | 17.40% | 0.83 | -30.86% | 227.51% | 1.00 | -83.25% | -0.17 |
| oos_1 | out_of_sample | 2021-12-16 to 2026-08-14 | 1169 | 90.74% | 14.94% | 14.65% | 1.02 | -20.78% | 86.52% | 0.77 | 4.22% | 0.26 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: PASS: coherent between development and OOS; the frozen strategy matches or beats the benchmark on return and Sharpe in every OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: PASS: coherent between development and OOS; the frozen strategy matches or beats the benchmark on return and Sharpe in every OOS window.**

This remains historical research, not evidence of tradability or a recommendation. Promotion still requires parameter-robustness and multiple-testing checks plus a live paper period.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

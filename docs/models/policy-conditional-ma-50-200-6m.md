# Strategy: policy_conditional_ma_50_200_6m

2 variant(s) documented · earliest 2026-09-11 · latest 2026-09-11.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="fast=50, slow=200, lookback_months=6, series_id=FEDFUNDS, vintage_policy=latest_vintage_date_lte_trading_day"><code>fast=50, slow=200, lookback_months=6, series_id=FEDFUNDS, vintage_policy=latest…</code></a> | 2026-09-11T22:27:46+00:00 | ✓ | <span class="verdict-badge verdict-badge--fail">FAIL</span> |
| <a href="#variant-2" title="fast=50, slow=200, lookback_months=6, series_id=TB3MS, vintage_policy=latest_vintage_date_lte_trading_day"><code>fast=50, slow=200, lookback_months=6, series_id=TB3MS, vintage_policy=latest_vi…</code></a> | 2026-09-11T22:57:37+00:00 | ✓ | <span class="verdict-badge verdict-badge--fail">FAIL</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--equity" data-chart-kind="equity">
  <div class="la-chart__label">Equity time series</div>
  <img src="../../assets/charts/policy-conditional-ma-50-200-6m__variant-1.svg" alt="policy_conditional_ma_50_200_6m variant 1 growth-of-one-dollar equity line" width="576" height="241" decoding="async">
  <figcaption>Real growth-of-$1 series · strategy vs benchmark</figcaption>
</figure>
</div>

**Generated:** 2026-09-11T22:27:46+00:00  
**Source report:** `20260911_222746_policy_conditional_ma_50_200_6m.md`  
**Registered:** ✓ — 2026-09-11T22:27:46+00:00 (walk_forward_passed=False)
#### Experiment

- Period: 2015-01-02 to 2026-08-14 (2921 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: fast=50, slow=200, lookback_months=6, series_id=FEDFUNDS, vintage_policy=latest_vintage_date_lte_trading_day

#### Monetary-policy data provenance and action rule

- Source: `FRED ALFRED API` (live, authenticated point-in-time API)
- Series: `FEDFUNDS` (monthly Effective Federal Funds Rate)
- Vendor vintage inventory: 364 total; the requested newest-200 response returned 200 from 2010-07-06 to 2026-09-01
- Backtest snapshots: 150 distinct vintages from 2014-06-02 to 2026-08-03; latest available observation periods span 2014-05-01 to 2026-07-01
- Live API use: 151 calls against a 200-call client budget (one vintage inventory plus one observation snapshot per required vintage; cached for full-sample and walk-forward reuse)
- Point-in-time policy: backward `merge_asof` on publication/vintage date; only `vintage_date <= trading day` can match, and pre-first-vintage dates remain missing
- Frozen action rule: apply existing 50/200 MA weights only when the current as-known policy rate is below the rate known 6 calendar months earlier; otherwise cash
- Missing current or trailing readings raise `PolicyRateDataUnavailable`; no revised-history or unconditional fallback is allowed

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

| Metric | Strategy | Ungated MA | Benchmark |
|---|---:|---:|---:|
| Cumulative return | 60.40% | 318.82% | 500.62% |
| CAGR | 4.16% | 13.15% | 16.73% |
| Annualized volatility | 12.93% | 16.74% | 19.44% |
| Annualized Sharpe (rf=0) | 0.38 | 0.82 | 0.89 |
| Maximum drawdown | -30.86% | -30.86% | -30.86% |
| Annualized turnover | 155.29% | 189.80% | 8.63% |
| Transaction-cost drag (sum of daily rates) | 0.90% | 1.10% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2015-01-02 to 2021-12-15 | 1752 | 44.83% | 5.47% | 13.32% | 0.47 | -30.86% | 227.51% | 1.00 | -182.68% | -0.53 |
| oos_1 | out_of_sample | 2021-12-16 to 2026-08-14 | 1169 | 17.37% | 3.51% | 11.54% | 0.36 | -20.78% | 86.52% | 0.77 | -69.15% | -0.41 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

This remains historical research, not evidence of tradability or a recommendation. Promotion still requires parameter-robustness and multiple-testing checks plus a live paper period.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

### Variant 2 {: #variant-2 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--equity" data-chart-kind="equity">
  <div class="la-chart__label">Equity time series</div>
  <img src="../../assets/charts/policy-conditional-ma-50-200-6m__variant-2.svg" alt="policy_conditional_ma_50_200_6m variant 2 growth-of-one-dollar equity line" width="576" height="241" decoding="async">
  <figcaption>Real growth-of-$1 series · strategy vs benchmark</figcaption>
</figure>
</div>

**Generated:** 2026-09-11T22:57:37+00:00  
**Source report:** `20260911_225737_policy_conditional_ma_50_200_6m.md`  
**Registered:** ✓ — 2026-09-11T22:57:37+00:00 (walk_forward_passed=False)
#### Experiment

- Period: 2015-01-02 to 2026-08-14 (2921 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: fast=50, slow=200, lookback_months=6, series_id=TB3MS, vintage_policy=latest_vintage_date_lte_trading_day

#### Monetary-policy data provenance and action rule

- Source: `FRED ALFRED API` (live, authenticated point-in-time API)
- Series: `TB3MS` (monthly Effective Federal Funds Rate)
- Vendor vintage inventory: 359 total; the requested newest-200 response returned 200 from 2010-03-01 to 2026-09-01
- Backtest snapshots: 148 distinct vintages from 2014-06-02 to 2026-08-03; latest available observation periods span 2014-05-01 to 2026-07-01
- Live API use: 149 calls against a 200-call client budget (one vintage inventory plus one observation snapshot per required vintage; cached for full-sample and walk-forward reuse)
- Point-in-time policy: backward `merge_asof` on publication/vintage date; only `vintage_date <= trading day` can match, and pre-first-vintage dates remain missing
- Frozen action rule: apply existing 50/200 MA weights only when the current as-known policy rate is below the rate known 6 calendar months earlier; otherwise cash
- Missing current or trailing readings raise `PolicyRateDataUnavailable`; no revised-history or unconditional fallback is allowed

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

| Metric | Strategy | Ungated MA | Benchmark |
|---|---:|---:|---:|
| Cumulative return | 152.35% | 318.82% | 500.62% |
| CAGR | 8.31% | 13.15% | 16.73% |
| Annualized volatility | 13.53% | 16.74% | 19.44% |
| Annualized Sharpe (rf=0) | 0.66 | 0.82 | 0.89 |
| Maximum drawdown | -30.86% | -30.86% | -30.86% |
| Annualized turnover | 155.29% | 189.80% | 8.63% |
| Transaction-cost drag (sum of daily rates) | 0.90% | 1.10% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2015-01-02 to 2021-12-15 | 1752 | 75.50% | 8.43% | 14.24% | 0.64 | -30.86% | 227.51% | 1.00 | -152.02% | -0.36 |
| oos_1 | out_of_sample | 2021-12-16 to 2026-08-14 | 1169 | 43.79% | 8.14% | 12.40% | 0.69 | -20.78% | 86.52% | 0.77 | -42.73% | -0.07 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

This remains historical research, not evidence of tradability or a recommendation. Promotion still requires parameter-robustness and multiple-testing checks plus a live paper period.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

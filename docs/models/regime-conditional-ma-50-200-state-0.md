# Strategy: regime_conditional_ma_50_200_state_0

1 variant(s) documented · earliest 2026-09-11 · latest 2026-09-11.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="fast=50, slow=200, active_state=0, regime_vintage=latest_stored_vintage"><code>fast=50, slow=200, active_state=0, regime_vintage=latest_stored_vintage</code></a> | 2026-09-11T18:02:41+00:00 | ✓ | <span class="verdict-badge verdict-badge--fail">FAIL</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--equity" data-chart-kind="equity">
  <div class="la-chart__label">Equity time series</div>
  <img src="../../assets/charts/regime-conditional-ma-50-200-state-0__variant-1.svg" alt="regime_conditional_ma_50_200_state_0 variant 1 growth-of-one-dollar equity line" loading="lazy">
  <figcaption>Real growth-of-$1 series · strategy vs benchmark</figcaption>
</figure>
</div>

**Generated:** 2026-09-11T18:02:41+00:00  
**Source report:** `20260911_180241_regime_conditional_ma_50_200_state_0.md`  
**Registered:** ✓ — 2026-09-11T18:02:41+00:00 (walk_forward_passed=False)
#### Experiment

- Period: 2015-01-02 to 2026-08-14 (2921 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: fast=50, slow=200, active_state=0, regime_vintage=latest_stored_vintage

#### Regime data provenance and action map

- Source: LazyStats production result depot `C:\ProgramData\InvestmentCommittee\live\db\result_depot.sqlite` (opened read-only)
- Series: `regime:SPY`, `regime:QQQ`
- Available state history: 2015-01-02 to 2026-08-14
- Classifier: existing production HMM, exactly 3 states ordered by volatility; LazyAlpha performs no fitting
- Frozen action map: state 0 (Low Vol) applies the existing 50/200 MA weights; states 1 (Mid Vol) and 2 (High Vol) are cash
- Modeling reason: production diagnostics associate state 0 with positive fitted annualized mean returns for both SPY and QQQ; state 1 is near-flat for SPY and state 2 is negative for both
- Vintage policy: latest stored vintage per historical date. Later full-history refits can revise past states, so this is a retrospective classifier-history test, not a point-in-time/live replay

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

Conditioning an existing trend signal on the production HMM's low-volatility, positive-mean state may reduce adverse exposure, but it can also discard profitable trends and need not beat the ungated signal or passive exposure after costs.

Reuse the frozen 50/200 moving-average crossover weights for each ETF, but apply them only when that ETF's persisted LazyStats three-state HMM reading is state 0 (Low Vol); states 1 and 2 map to cash. State 0 was chosen before backtesting because production diagnostics associate it with positive fitted mean returns for both SPY and QQQ, while state 1 is near-flat for SPY and state 2 is negative for both.

Sources:

- [Regime-Aware Trading with HMMs and Macro Features](https://pyquantlab.medium.com/regime-aware-trading-with-hidden-markov-models-hmms-and-macro-features-c75f6d357880) — Provides practitioner evidence and implementation context for conditioning exposures on an HMM regime call.
- [Downside Risk Reduction Using Regime-Switching Signals](https://arxiv.org/html/2402.05272v2) — Studies regime-switching signals as a way to reduce downside risk relative to static exposure.

Known risks:

- latest-vintage regime history can include retrospective revisions, so this is not a point-in-time replay
- HMM state identities and fitted relationships may change on refit
- gating may miss sharp recoveries or profitable mid-volatility trends
- cash return is modeled as zero and execution frictions are incomplete
- one historical sample is not evidence of future profitability

#### Net backtest metrics

| Metric | Strategy | Ungated MA | Benchmark |
|---|---:|---:|---:|
| Cumulative return | 331.98% | 318.82% | 500.62% |
| CAGR | 13.45% | 13.15% | 16.73% |
| Annualized volatility | 6.60% | 16.74% | 19.44% |
| Annualized Sharpe (rf=0) | 1.95 | 0.82 | 0.89 |
| Maximum drawdown | -4.31% | -30.86% | -30.86% |
| Annualized turnover | 370.97% | 189.80% | 8.63% |
| Transaction-cost drag (sum of daily rates) | 2.15% | 1.10% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2015-01-02 to 2021-12-15 | 1752 | 181.97% | 16.08% | 6.96% | 2.18 | -4.27% | 227.51% | 1.00 | -45.55% | 1.18 |
| oos_1 | out_of_sample | 2021-12-16 to 2026-08-14 | 1169 | 53.20% | 9.63% | 6.03% | 1.56 | -4.31% | 86.52% | 0.77 | -33.31% | 0.79 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: INCONCLUSIVE: better on only one of net return and Sharpe.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

This remains historical research, not evidence of tradability or a recommendation. Promotion still requires parameter-robustness and multiple-testing checks plus a live paper period.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

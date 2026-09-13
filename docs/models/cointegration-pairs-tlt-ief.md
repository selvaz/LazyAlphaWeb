# Strategy: cointegration_pairs_tlt_ief

1 variant(s) documented · earliest 2026-09-13 · latest 2026-09-13.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="dependent=TLT, independent=IEF, lookback=252, entry_z=2.0, exit_z=0.5, cointegration_alpha=0.05, screen=development_only_bidirectional_engle_granger_log_prices, gross_exposure=1.0"><code>dependent=TLT, independent=IEF, lookback=252, entry_z=2.0, exit_z=0.5, cointegr…</code></a> | 2026-09-13T08:11:46+00:00 | ✓ | <span class="verdict-badge verdict-badge--pass">PASS</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--pass">PASS</span>
</div>
<figure class="la-chart la-chart--equity" data-chart-kind="equity">
  <div class="la-chart__label">Equity time series</div>
  <img src="../../assets/charts/cointegration-pairs-tlt-ief__variant-1.svg" alt="cointegration_pairs_tlt_ief variant 1 growth-of-one-dollar equity line" width="576" height="241" decoding="async">
  <figcaption>Real growth-of-$1 series · strategy vs benchmark</figcaption>
</figure>
</div>

**Generated:** 2026-09-13T08:11:46+00:00  
**Source report:** `20260913_081146_cointegration_pairs_tlt_ief.md`  
**Registered:** ✓ — 2026-09-13T08:11:46+00:00 (walk_forward_passed=True)
#### Experiment

- Period: 2010-01-04 to 2026-08-14 (4178 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: dependent=TLT, independent=IEF, lookback=252, entry_z=2.0, exit_z=0.5, cointegration_alpha=0.05, screen=development_only_bidirectional_engle_granger_log_prices, gross_exposure=1.0

#### Pair selection and cointegration diagnostics

- Pair: `TLT/IEF`. Both are highly liquid US Treasury ETFs already covered by the repository's Turtle experiment; they share Treasury-rate exposure but differ in duration.
- Frozen eligibility rule: both Engle-Granger regression directions p < 0.05 on development only.
- Development window: 2010-01-04 to 2019-12-16 (2506 sessions). `TLT ~ IEF` statistic `-3.414703`, p-value `0.040743`; reverse statistic `-3.518998`, p-value `0.030748`. **Eligibility: PASS.**
- Full-sample stability diagnostic (never used to select the pair): 2010-01-04 to 2026-08-14 (4178 sessions). Forward statistic `0.222329`, p-value `0.989922`; reverse statistic `0.531894`, p-value `0.992850`. **Full-sample cointegration: FAIL / structural instability.**
- Method: natural-log adjusted closes; Engle-Granger two-step test with a constant and ADF lag selected by AIC (`statsmodels.tsa.stattools.coint`). The regression direction is material, so eligibility requires both directions.
- Trading rule: rolling OLS and z-score calculations use only the trailing window through close t. A positive spread is long the dependent ETF and short the OLS hedge-ratio exposure in the independent ETF; absolute leg weights sum to 1. The common engine executes those weights on session t+1.

#### Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: TLT, IEF
- Validated common panel: 2010-01-04 to 2026-08-14; 4178 rows
- Database: `C:\Users\Administrator\Documents\GitHub\market-data-hub\market_data.duckdb`

| Symbol | Last date | Status | Coverage score | Stalled |
|---|---:|---|---:|---|
| IEF | 2026-08-14 00:00:00 | ok | 97.31 | False |
| TLT | 2026-08-14 00:00:00 | ok | 97.32 | False |

#### Research rationale

A long/short TLT/IEF spread may mean-revert because both funds represent the US Treasury curve, while their different durations create temporary relative-value dislocations. Cointegration must be demonstrated on development data rather than assumed from correlation.

Test log adjusted closes with the Engle-Granger two-step method on the development window. If the pair passes at 5%, estimate a 252-session rolling OLS hedge ratio, enter against residual z-scores at +/-2, exit inside +/-0.5, normalize the two hedge legs to one unit of gross exposure, and retain the common one-session lag.

Sources:

- [Pairs Trading: Performance of a Relative-Value Arbitrage Rule](https://academic.oup.com/rfs/article-abstract/19/3/797/1646694) — Gatev, Goetzmann, and Rouwenhorst formalize a self-financing relative-value rule with separate formation and trading periods.
- [Pairs Trading: Quantitative Methods and Analysis](https://www.wiley-vch.de/en/areas-interest/finance-economics-law/pairs-trading-978-0-471-46067-1) — Vidyamurthy develops the cointegration, hedge-ratio, and market-neutral statistical-arbitrage framework.
- [Pre-selection in cointegration-based pairs trading](https://doi.org/10.1007/s10260-023-00702-4) — Documents the log-price OLS residual/ADF Engle-Granger workflow, +/-2-sigma entries, and sensitivity to pair selection.
- [Cointegration-based pairs trading: identifying and exploiting similar exchange-traded funds](https://doi.org/10.1057/s41260-025-00416-0) — Finds that ETF pairs-trading results depend on cointegration stability and that shorter stable windows limit long-run profitability.
- [Gold Standard Pairs Trading Rules: Are They Valid?](https://arxiv.org/abs/2010.01157) — Reports declining modern profitability and strong sensitivity to transaction costs, execution lag, and parameter choices.

Known risks:

- cointegration can break after the formation period
- Engle-Granger results depend on the regression direction
- rolling estimation does not guarantee a stationary future spread
- borrow fees, financing, bid/ask spread, slippage and market impact are absent
- a single pair supplies little diversification and one historical test is not evidence of future profitability

#### Net backtest metrics

| Metric | Strategy | Benchmark |
|---|---:|---:|
| Gross cumulative return | 6.78% | 52.43% |
| Cumulative return | 3.12% | 52.35% |
| CAGR | 0.19% | 2.57% |
| Annualized volatility | 1.50% | 10.55% |
| Annualized Sharpe (rf=0) | 0.13 | 0.29 |
| Maximum drawdown | -5.91% | -37.05% |
| Annualized turnover | 421.07% | 6.03% |
| Transaction-cost drag (sum of daily rates) | 3.49% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2010-01-04 to 2019-12-16 | 2506 | 0.73% | 0.07% | 1.07% | 0.07 | -2.35% | 78.89% | 0.65 | -78.16% | -0.58 |
| oos_1 | out_of_sample | 2019-12-17 to 2026-08-14 | 1672 | -1.03% | -0.16% | 1.76% | -0.08 | -5.91% | -14.82% | -0.15 | 13.79% | 0.07 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: PASS: coherent between development and OOS; the frozen strategy matches or beats the benchmark on return and Sharpe in every OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: PASS: coherent between development and OOS; the frozen strategy matches or beats the benchmark on return and Sharpe in every OOS window.**

**Outcome classification: WALK-FORWARD PASS / FULL-SAMPLE FAIL / COINTEGRATION BREAKDOWN.** Interpret the mechanical validation verdict together with absolute returns and the ex-post stability diagnostic; a broken formation-period relationship is not promotable.

This remains historical research, not evidence of tradability or a recommendation. There is still no parameter-search correction or project-level multiple-testing adjustment for this strategy; promotion also requires a live paper period.

#### Ecosystem review

- **LazyFin:** Reference not found; manual review required. (`C:\Users\Administrator\Documents\GitHub\LazyAlpha\LazyFin\docs\status.md`)
- **investmentcommittee:** Reference not found; manual review required. (`C:\Users\Administrator\Documents\GitHub\LazyAlpha\investment-process-top-down-etf.md`)

# Strategy: fifty_two_week_high_top3_252

1 variant(s) documented · earliest 2026-09-16 · latest 2026-09-16.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="lookback_days=252, top_k=3, ranking=price_divided_by_trailing_rolling_max, rebalance=daily, allocation=equal_weight_long_top_k, sizer=equal_weight_long"><code>lookback_days=252, top_k=3, ranking=price_divided_by_trailing_rolling_max, reba…</code></a> | 2026-09-16T14:17:47+00:00 | ✓ | <span class="verdict-badge verdict-badge--fail">FAIL</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--equity" data-chart-kind="equity">
  <div class="la-chart__label">Equity time series</div>
  <img src="../../assets/charts/fifty-two-week-high-top3-252__variant-1.svg" alt="fifty_two_week_high_top3_252 variant 1 growth-of-one-dollar equity line" width="576" height="241" decoding="async">
  <figcaption>Real growth-of-$1 series · strategy vs benchmark</figcaption>
</figure>
</div>

**Generated:** 2026-09-16T14:17:47+00:00  
**Source report:** `20260916_141747_fifty_two_week_high_top3_252.md`  
**Registered:** ✓ — 2026-09-16T14:17:47+00:00 (walk_forward_passed=False)
#### Experiment

- Period: 2015-01-02 to 2026-08-14 (2920 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: lookback_days=252, top_k=3, ranking=price_divided_by_trailing_rolling_max, rebalance=daily, allocation=equal_weight_long_top_k, sizer=equal_weight_long

#### Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: SPY, QQQ, IWM, TLT, IEF, GLD, SLV, DBC, USO, UUP
- Validated common panel: 2015-01-02 to 2026-08-14; 2920 rows
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

Securities trading nearest their own trailing 52-week high may subsequently outperform securities farther below that reference price because investors anchor on the high and underreact to news.

Each session, divide every ETF's adjusted close by its trailing 252-session maximum, rank the ten confirmed Turtle-universe ETFs cross-sectionally, and hold the top three at equal weight. The rolling maximum includes only information through that close, and the common backtest engine applies selected weights one session later.

Sources:

- [The 52-Week High and Momentum Investing](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2004.00695.x) — George and Hwang find that nearness to the 52-week high is a stronger and more robust predictor of future returns than past total returns, consistent with anchoring and underreaction. This is mechanistically different from LazyAlpha's already-tried 12-minus-1 total-return ranking, although both sit in the broad momentum literature; it is not a duplicate test of that hypothesis.

Known risks:

- the cited evidence is primarily from individual equities rather than a ten-ETF cross-asset panel
- a ten-symbol universe supplies a small and potentially unstable cross-section
- daily ranking may create high turnover and sensitivity to trading frictions
- the signal can concentrate in correlated assets near simultaneous highs
- today's surviving ETF universe introduces survivorship and proxy limitations
- one historical test is not evidence of future profitability

#### Net backtest metrics

| Metric | Strategy | Benchmark |
|---|---:|---:|
| Gross cumulative return | 194.44% | 175.51% |
| Cumulative return | 119.30% | 175.38% |
| CAGR | 7.01% | 9.14% |
| Annualized volatility | 11.81% | 10.91% |
| Annualized Sharpe (rf=0) | 0.63 | 0.86 |
| Maximum drawdown | -29.94% | -23.48% |
| Annualized turnover | 5088.90% | 8.63% |
| Transaction-cost drag (sum of daily rates) | 29.48% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2015-01-02 to 2021-12-15 | 1752 | 97.09% | 10.25% | 9.25% | 1.10 | -11.56% | 56.90% | 0.67 | 40.19% | 0.43 |
| oos_1 | out_of_sample | 2021-12-16 to 2026-08-14 | 1168 | 26.11% | 5.13% | 13.05% | 0.45 | -15.90% | 75.68% | 1.11 | -49.57% | -0.66 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

#### Conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

This remains historical research, not evidence of tradability or a recommendation. There is still no parameter-search correction or project-level multiple-testing adjustment for this strategy; promotion also requires a live paper period.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

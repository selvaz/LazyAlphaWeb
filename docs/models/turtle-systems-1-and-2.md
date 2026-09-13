# Strategy: turtle_systems_1_and_2

3 variant(s) documented · earliest 2026-09-11 · latest 2026-09-12.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="rule_version=classic_1983_close_execution_v1, n_period=20, risk_fraction=0.01, system1_entry=20, system1_exit=10, system2_entry=55, system2_exit=20, stop_n=2.0, pyramid_n=0.5, market_cap=4, close_group_cap=6, loose_group_cap=10, direction_cap=12, groups={&#x27;equities&#x27;: [&#x27;SPY&#x27;, &#x27;QQQ&#x27;, &#x27;IWM&#x27;], &#x27;bonds&#x27;: [&#x27;TLT&#x27;, &#x27;IEF&#x27;], &#x27;metals&#x27;: [&#x27;GLD&#x27;, &#x27;SLV&#x27;], &#x27;commodities&#x27;: [&#x27;DBC&#x27;, &#x27;USO&#x27;], &#x27;currency&#x27;: [&#x27;UUP&#x27;]}, loose_group_interpretation=every_pairwise_union_of_close_groups"><code>rule_version=classic_1983_close_execution_v1, n_period=20, risk_fraction=0.01, …</code></a> | 2026-09-11T23:24:01+00:00 | ✓ | <span class="verdict-badge verdict-badge--fail">FAIL</span> |
| <a href="#variant-2" title="rule_version=classic_1983_close_execution_v1, n_period=20, risk_fraction=0.01, simulation_cost_bps=5.0, system1_entry=20, system1_exit=10, system2_entry=55, system2_exit=20, stop_n=2.0, pyramid_n=0.5, market_cap=4, close_group_cap=6, loose_group_cap=10, direction_cap=12, groups={&#x27;equities&#x27;: [&#x27;SPY&#x27;, &#x27;QQQ&#x27;, &#x27;IWM&#x27;], &#x27;bonds&#x27;: [&#x27;TLT&#x27;, &#x27;IEF&#x27;], &#x27;metals&#x27;: [&#x27;GLD&#x27;, &#x27;SLV&#x27;], &#x27;commodities&#x27;: [&#x27;DBC&#x27;, &#x27;USO&#x27;], &#x27;currency&#x27;: [&#x27;UUP&#x27;]}, loose_group_interpretation=every_pairwise_union_of_close_groups, data_selection=market_data_hub_configured_production_db_2010_present"><code>rule_version=classic_1983_close_execution_v1, n_period=20, risk_fraction=0.01, …</code></a> | 2026-09-11T23:32:31+00:00 | ✓ (2 entries) | <span class="verdict-badge verdict-badge--fail">FAIL</span> |
| <a href="#variant-3" title="rule_version=classic_1983_close_execution_v2_capital_corrected, n_period=20, risk_fraction=0.01, simulation_cost_bps=5.0, margin_ratio=0.1, max_aggregate_leverage=1.0, same_symbol_system_overlap_risk_multiplier=0.5, system1_entry=20, system1_exit=10, system2_entry=55, system2_exit=20, stop_n=2.0, pyramid_n=0.5, market_cap=4, close_group_cap=6, loose_group_cap=10, direction_cap=12, groups={&#x27;equities&#x27;: [&#x27;SPY&#x27;, &#x27;QQQ&#x27;, &#x27;IWM&#x27;], &#x27;bonds&#x27;: [&#x27;TLT&#x27;, &#x27;IEF&#x27;], &#x27;metals&#x27;: [&#x27;GLD&#x27;, &#x27;SLV&#x27;], &#x27;commodities&#x27;: [&#x27;DBC&#x27;, &#x27;USO&#x27;], &#x27;currency&#x27;: [&#x27;UUP&#x27;]}, loose_group_interpretation=every_pairwise_union_of_close_groups, data_selection=market_data_hub_configured_production_db_2010_present"><code>rule_version=classic_1983_close_execution_v2_capital_corrected, n_period=20, ri…</code></a> | 2026-09-12T08:35:39+00:00 | ✓ | <span class="verdict-badge verdict-badge--fail">FAIL</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--fallback" data-chart-kind="fallback">
  <div class="la-chart__label">Metrics-only summary</div>
  <img src="../../assets/charts/turtle-systems-1-and-2__variant-1.svg" alt="turtle_systems_1_and_2 variant 1 metrics-only bar chart; no equity time series available" loading="lazy">
  <figcaption>No equity time series available for this run · return and Sharpe bars only</figcaption>
</figure>
</div>

**Generated:** 2026-09-11T23:24:01+00:00  
**Source report:** `turtle_systems_1_and_2_2010_present.md`  
**Registered:** ✓ — 2026-09-11T23:24:01+00:00 (walk_forward_passed=False)
#### Experiment

- Period: 2010-01-04 to 2026-08-14 (4178 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: rule_version=classic_1983_close_execution_v1, n_period=20, risk_fraction=0.01, system1_entry=20, system1_exit=10, system2_entry=55, system2_exit=20, stop_n=2.0, pyramid_n=0.5, market_cap=4, close_group_cap=6, loose_group_cap=10, direction_cap=12, groups={'equities': ['SPY', 'QQQ', 'IWM'], 'bonds': ['TLT', 'IEF'], 'metals': ['GLD', 'SLV'], 'commodities': ['DBC', 'USO'], 'currency': ['UUP']}, loose_group_interpretation=every_pairwise_union_of_close_groups

#### Classic Turtle rules implemented

- N: 20-day Wilder ATR of True Range, seeded by the first 20-day arithmetic mean; True Range is `max(high-low, abs(high-prev_close), abs(low-prev_close))`.
- System 1: long/short on a close beyond the prior 20-day high/low; exit on the prior 10-day opposite extreme. A signal is skipped when the immediately preceding System 1 signal in the same market and direction would have won, except that a simultaneous 55-day breakout is an always-taken failsafe (subject only to portfolio caps). Skipped signals are tracked hypothetically through the same 2N stop/10-day exit so the next filter decision is stateful.
- System 2: long/short on a close beyond the prior 55-day high/low; every signal is eligible, with the prior 20-day opposite extreme as exit.
- Both systems run simultaneously. Their units are separately associated with their system exit, but count together against the same market and portfolio caps.
- Position sizing: every new unit contains `(1% * current internally simulated equity) / current N` fractional ETF shares. Signed position market value divided by that same equity becomes the emitted weight; aggregate weights are deliberately not normalized or capped at 1.0.
- Pyramiding: each campaign proposes another full unit for every 0.5N favorable move from its prior add level, up to the shared four-unit market limit. A crossed level rejected by a risk cap is skipped whole, never partially filled.
- Stops: every unit starts 2N from its own fill. A new same-direction unit tightens every existing same-market unit to the new unit's effective stop (raised for longs, lowered for shorts; never loosened if N expands).
- Execution interpretation: breakouts, channel exits, and stops are evaluated on adjusted closes. This is required by LazyAlpha's unchanged close-to-next-close weight protocol; it does not claim intraday stop fills or futures tick execution.

#### Correlation groups and layered unit limits

| Close group | ETFs |
|---|---|
| Equities | SPY, QQQ, IWM |
| Bonds | TLT, IEF |
| Metals | GLD, SLV |
| Commodities | DBC, USO |
| Currency | UUP |

All caps are tested before each complete unit and are direction-specific, consistent with Faith's published wording: maximum 4 units per market; 6 in one direction inside a close group; 10 in one direction across every pairwise union of close groups; and 12 units in one direction portfolio-wide. The published rules name examples of loosely correlated futures but do not define a complete ETF taxonomy. The pairwise-union interpretation uses only the CEO-specified close groups, avoids inventing extra sectors, and keeps the 10- and 12-unit layers independently operative.

**Major universe limitation:** LazyAlpha previously centered on SPY/QQQ, whose high correlation makes correlation caps and the original diversification mechanism nearly meaningless. These ten ETFs deliberately add rates, metals, commodities, and a dollar proxy, but remain US-listed proxies. This is a faithful mechanical replication of published rules on real ETF data, not a replication of the original edge, which depended on roughly two dozen genuinely different futures markets across asset classes and geographies.

#### Realized units, leverage, and reconciliation

- Peak aggregate gross leverage: 38.5084x
- Average aggregate gross leverage: 13.7945x
- Maximum concurrent units: 24
- Cap-skipped entry/add signals: 6231 (market=198, close-group=2804, loose-group=1598, direction=1631)
- System 1 filter skips: 351; initial entries: 1462; pyramid additions: 1167
- Internal-equity versus zero-cost `run_backtest` maximum absolute difference: 2.09547579288e-08; required tolerance: 0.0001; confirmed: `True`.
- The reported performance below includes LazyAlpha transaction costs. Reconciliation is intentionally zero-cost because the strategy interface does not receive the backtester's cost setting; position sizing therefore compounds the strategy's own gross marked-to-market equity.
- Leverage is real: aggregate position value can exceed equity. LazyAlpha models neither margin requirements nor financing cost for leveraged exposure. Cash return is also zero. Both are known simplifications, not hidden performance claims.

#### OHLC construction

- Raw fields: `high`, `low`, `close`, and `adj_close` from `market-data-hub prices_daily`, with live rows excluded.
- Back-adjustment: on every symbol/date, multiply raw high and low by `adj_close / close`; use `adj_close` as the close. Thus ATR and breakout channels share the corporate-action-consistent price scale used for returns.
- Validated OHLC common panel: 2010-01-04 to 2026-08-14 (4178 sessions). Dates with an incomplete cross-symbol row are excluded from the common panel, exactly as in the standard adjusted-close adapter; nothing is imputed. Missing required columns/symbols, duplicates, non-finite present values, or non-positive present values are fatal.

#### Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: SPY, QQQ, IWM, TLT, IEF, GLD, SLV, DBC, USO, UUP
- Validated common panel: 2010-01-04 to 2026-08-14; 4178 rows
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

Volatility-normalized breakouts across genuinely diverse markets may capture infrequent persistent trends, while 2N stops, pyramiding rules, and layered portfolio heat limits constrain failed breakouts.

Run the published 20/10-day filtered System 1 and unfiltered 55/20-day System 2 together; size every unit at 1% of current equity per N, add at 0.5N, tighten stops, and enforce all four unit-cap layers.

Sources:

- [The Original Turtle Trading Rules Explained](https://www.theturtletrader.com/turtle-trading-rules/) — Corroborates N/ATR sizing, 20/55-day entries, the System 1 winner filter and failsafe, 10/20-day exits, 2N stops, 0.5N adds, and the 4/6/10/12 unit limits.
- [Way of the Turtle: Original Turtle Trading Rules](https://www.brookstradingcourse.com/wp-content/uploads/wpforo/attachments/12514/3508-CurtisFaith-WayoftheTurtle-1.pdf) — Original Turtle Curtis Faith describes the two systems, the 0.5N pyramid sequence, prior-breakout filter, and direction-specific correlated-market unit limits.
- [The Original Turtle Rules](https://tradingblox.com/originalturtles/originalturtlerules.htm) — Hosts the freely published complete rules covering entries, position sizing, adds, stops, exits, and portfolio limits.

Known risks:

- ten US-listed ETFs only partially approximate the original global futures diversification
- close-based ETF execution differs from intraday stop orders and futures contract mechanics
- leveraged exposure has no margin or financing-cost model in LazyAlpha
- borrow availability, short fees, slippage, taxes, and market impact are not modeled
- one historical sample and one fixed universe are not evidence of future profitability

#### Net backtest metrics

| Metric | Strategy | Benchmark |
|---|---:|---:|
| Cumulative return | -98.41% | 259.37% |
| CAGR | -22.09% | 8.02% |
| Annualized volatility | 113.98% | 10.63% |
| Annualized Sharpe (rf=0) | 0.37 | 0.78 |
| Maximum drawdown | -99.88% | -23.48% |
| Annualized turnover | 49439.19% | 6.03% |
| Transaction-cost drag (sum of daily rates) | 409.84% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2010-01-04 to 2019-12-16 | 2506 | -98.70% | -35.36% | 109.12% | 0.16 | -99.88% | 65.32% | 0.60 | -164.02% | -0.44 |
| oos_1 | out_of_sample | 2019-12-17 to 2026-08-14 | 1672 | -23.14% | -3.89% | 123.92% | 0.60 | -97.05% | 116.86% | 0.99 | -140.00% | -0.39 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

This remains historical research, not evidence of tradability or a recommendation. Promotion still requires parameter-robustness and multiple-testing checks plus a live paper period.

### Variant 2 {: #variant-2 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--fallback" data-chart-kind="fallback">
  <div class="la-chart__label">Metrics-only summary</div>
  <img src="../../assets/charts/turtle-systems-1-and-2__variant-2.svg" alt="turtle_systems_1_and_2 variant 2 metrics-only bar chart; no equity time series available" loading="lazy">
  <figcaption>No equity time series available for this run · return and Sharpe bars only</figcaption>
</figure>
</div>

**Generated:** 2026-09-11T23:32:31+00:00  
**Source report:** `turtle_systems_1_and_2_2010_2026-09-10.md`  
**Registered:** ✓ (2 entries) — 2026-09-11T23:26:29+00:00 (walk_forward_passed=False); 2026-09-11T23:32:31+00:00 (walk_forward_passed=False)
#### Experiment

- Period: 2010-01-04 to 2026-09-10 (4196 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: rule_version=classic_1983_close_execution_v1, n_period=20, risk_fraction=0.01, simulation_cost_bps=5.0, system1_entry=20, system1_exit=10, system2_entry=55, system2_exit=20, stop_n=2.0, pyramid_n=0.5, market_cap=4, close_group_cap=6, loose_group_cap=10, direction_cap=12, groups={'equities': ['SPY', 'QQQ', 'IWM'], 'bonds': ['TLT', 'IEF'], 'metals': ['GLD', 'SLV'], 'commodities': ['DBC', 'USO'], 'currency': ['UUP']}, loose_group_interpretation=every_pairwise_union_of_close_groups, data_selection=market_data_hub_configured_production_db_2010_present

#### Classic Turtle rules implemented

- N: 20-day Wilder ATR of True Range, seeded by the first 20-day arithmetic mean; True Range is `max(high-low, abs(high-prev_close), abs(low-prev_close))`.
- System 1: long/short on a close beyond the prior 20-day high/low; exit on the prior 10-day opposite extreme. A signal is skipped when the immediately preceding System 1 signal in the same market and direction would have won, except that a simultaneous 55-day breakout is an always-taken failsafe (subject only to portfolio caps). Skipped signals are tracked hypothetically through the same 2N stop/10-day exit so the next filter decision is stateful.
- System 2: long/short on a close beyond the prior 55-day high/low; every signal is eligible, with the prior 20-day opposite extreme as exit.
- Both systems run simultaneously. Their units are separately associated with their system exit, but count together against the same market and portfolio caps.
- Position sizing: every new unit contains `(1% * current internally simulated equity) / current N` fractional ETF shares. Signed position market value divided by that same equity becomes the emitted weight; aggregate weights are deliberately not normalized or capped at 1.0.
- Pyramiding: each campaign proposes another full unit for every 0.5N favorable move from its prior add level, up to the shared four-unit market limit. A crossed level rejected by a risk cap is skipped whole, never partially filled.
- Stops: every unit starts 2N from its own fill. A new same-direction unit tightens every existing same-market unit to the new unit's effective stop (raised for longs, lowered for shorts; never loosened if N expands).
- Execution interpretation: breakouts, channel exits, and stops are evaluated on adjusted closes. This is required by LazyAlpha's unchanged close-to-next-close weight protocol; it does not claim intraday stop fills or futures tick execution.

#### Correlation groups and layered unit limits

| Close group | ETFs |
|---|---|
| Equities | SPY, QQQ, IWM |
| Bonds | TLT, IEF |
| Metals | GLD, SLV |
| Commodities | DBC, USO |
| Currency | UUP |

All caps are tested before each complete unit and are direction-specific, consistent with Faith's published wording: maximum 4 units per market; 6 in one direction inside a close group; 10 in one direction across every pairwise union of close groups; and 12 units in one direction portfolio-wide. The published rules name examples of loosely correlated futures but do not define a complete ETF taxonomy. The pairwise-union interpretation uses only the CEO-specified close groups, avoids inventing extra sectors, and keeps the 10- and 12-unit layers independently operative.

**Major universe limitation:** LazyAlpha previously centered on SPY/QQQ, whose high correlation makes correlation caps and the original diversification mechanism nearly meaningless. These ten ETFs deliberately add rates, metals, commodities, and a dollar proxy, but remain US-listed proxies. This is a faithful mechanical replication of published rules on real ETF data, not a replication of the original edge, which depended on roughly two dozen genuinely different futures markets across asset classes and geographies.

#### Realized units, leverage, and reconciliation

- Peak aggregate gross leverage: 40.5299x
- Average aggregate gross leverage: 14.0696x
- Maximum concurrent units: 24
- Cap-skipped entry/add signals: 6279 (market=199, close-group=2844, loose-group=1605, direction=1631)
- System 1 filter skips: 354; initial entries: 1473; pyramid additions: 1171
- Internal-equity versus the reported 5.00-bps `run_backtest` maximum absolute difference: 1.68802216649e-09; required tolerance: 0.0001; confirmed: `True`.
- The internal loop deducts the same one-session-lagged LazyAlpha turnover charge as the reported backtest before sizing that close's new units. Current simulated equity is therefore the strategy's own net marked-to-market equity, including modeled transaction costs.
- Leverage is real: aggregate position value can exceed equity. LazyAlpha models neither margin requirements nor financing cost for leveraged exposure. Cash return is also zero. Both are known simplifications, not hidden performance claims.

#### OHLC construction

- Raw fields: `high`, `low`, `close`, and `adj_close` from `market-data-hub prices_daily`, with live rows excluded.
- Back-adjustment: on every symbol/date, multiply raw high and low by `adj_close / close`; use `adj_close` as the close. Thus ATR and breakout channels share the corporate-action-consistent price scale used for returns.
- Validated OHLC common panel: 2010-01-04 to 2026-09-10 (4196 sessions). Dates with an incomplete cross-symbol row are excluded from the common panel, exactly as in the standard adjusted-close adapter; nothing is imputed. Missing required columns/symbols, duplicates, non-finite present values, or non-positive present values are fatal.

#### Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: SPY, QQQ, IWM, TLT, IEF, GLD, SLV, DBC, USO, UUP
- Validated common panel: 2010-01-04 to 2026-09-10; 4196 rows
- Database: `market-data-hub configured default`

| Symbol | Last date | Status | Coverage score | Stalled |
|---|---:|---|---:|---|
| DBC | 2026-09-10 00:00:00 | ok | 95.50 | False |
| GLD | 2026-09-10 00:00:00 | ok | 95.50 | False |
| IEF | 2026-09-10 00:00:00 | ok | 98.50 | False |
| IWM | 2026-09-10 00:00:00 | ok | 98.50 | False |
| QQQ | 2026-09-10 00:00:00 | ok | 98.50 | False |
| SLV | 2026-09-10 00:00:00 | ok | 95.50 | False |
| SPY | 2026-09-10 00:00:00 | ok | 98.52 | False |
| TLT | 2026-09-10 00:00:00 | ok | 98.51 | False |
| USO | 2026-09-10 00:00:00 | ok | 95.50 | False |
| UUP | 2026-09-10 00:00:00 | ok | 95.51 | False |

#### Research rationale

Volatility-normalized breakouts across genuinely diverse markets may capture infrequent persistent trends, while 2N stops, pyramiding rules, and layered portfolio heat limits constrain failed breakouts.

Run the published 20/10-day filtered System 1 and unfiltered 55/20-day System 2 together; size every unit at 1% of current equity per N, add at 0.5N, tighten stops, and enforce all four unit-cap layers.

Sources:

- [The Original Turtle Trading Rules Explained](https://www.theturtletrader.com/turtle-trading-rules/) — Corroborates N/ATR sizing, 20/55-day entries, the System 1 winner filter and failsafe, 10/20-day exits, 2N stops, 0.5N adds, and the 4/6/10/12 unit limits.
- [Way of the Turtle: Original Turtle Trading Rules](https://www.brookstradingcourse.com/wp-content/uploads/wpforo/attachments/12514/3508-CurtisFaith-WayoftheTurtle-1.pdf) — Original Turtle Curtis Faith describes the two systems, the 0.5N pyramid sequence, prior-breakout filter, and direction-specific correlated-market unit limits.
- [The Original Turtle Rules](https://tradingblox.com/originalturtles/originalturtlerules.htm) — Hosts the freely published complete rules covering entries, position sizing, adds, stops, exits, and portfolio limits.

Known risks:

- ten US-listed ETFs only partially approximate the original global futures diversification
- close-based ETF execution differs from intraday stop orders and futures contract mechanics
- leveraged exposure has no margin or financing-cost model in LazyAlpha
- borrow availability, short fees, slippage, taxes, and market impact are not modeled
- one historical sample and one fixed universe are not evidence of future profitability

#### Net backtest metrics

| Metric | Strategy | Benchmark |
|---|---:|---:|
| Gross cumulative return | -18.47% | 265.80% |
| Cumulative return | -98.82% | 265.62% |
| CAGR | -23.39% | 8.10% |
| Annualized volatility | 116.79% | 10.62% |
| Annualized Sharpe (rf=0) | 0.37 | 0.79 |
| Maximum drawdown | -99.94% | -23.48% |
| Annualized turnover | 50592.57% | 6.01% |
| Transaction-cost drag (sum of daily rates) | 421.20% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2010-01-04 to 2020-01-02 | 2517 | -98.92% | -36.48% | 111.62% | 0.16 | -99.91% | 68.40% | 0.62 | -167.33% | -0.46 |
| oos_1 | out_of_sample | 2020-01-03 to 2026-09-10 | 1679 | -55.20% | -11.35% | 122.86% | 0.54 | -98.06% | 115.74% | 0.98 | -170.94% | -0.44 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

This remains historical research, not evidence of tradability or a recommendation. Promotion still requires parameter-robustness and multiple-testing checks plus a live paper period.

### Variant 3 {: #variant-3 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--fail">FAIL</span>
</div>
<figure class="la-chart la-chart--fallback" data-chart-kind="fallback">
  <div class="la-chart__label">Metrics-only summary</div>
  <img src="../../assets/charts/turtle-systems-1-and-2__variant-3.svg" alt="turtle_systems_1_and_2 variant 3 metrics-only bar chart; no equity time series available" loading="lazy">
  <figcaption>No equity time series available for this run · return and Sharpe bars only</figcaption>
</figure>
</div>

**Generated:** 2026-09-12T08:35:39+00:00  
**Source report:** `turtle_core_risk_corrected_classic_2010-01-04_2026-09-10.md`  
**Registered:** ✓ — 2026-09-12T08:35:39+00:00 (walk_forward_passed=False)
#### Experiment

- Period: 2010-01-04 to 2026-09-10 (4196 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: rule_version=classic_1983_close_execution_v2_capital_corrected, n_period=20, risk_fraction=0.01, simulation_cost_bps=5.0, margin_ratio=0.1, max_aggregate_leverage=1.0, same_symbol_system_overlap_risk_multiplier=0.5, system1_entry=20, system1_exit=10, system2_entry=55, system2_exit=20, stop_n=2.0, pyramid_n=0.5, market_cap=4, close_group_cap=6, loose_group_cap=10, direction_cap=12, groups={'equities': ['SPY', 'QQQ', 'IWM'], 'bonds': ['TLT', 'IEF'], 'metals': ['GLD', 'SLV'], 'commodities': ['DBC', 'USO'], 'currency': ['UUP']}, loose_group_interpretation=every_pairwise_union_of_close_groups, data_selection=market_data_hub_configured_production_db_2010_present

#### Classic Turtle rules implemented

- N: 20-day Wilder ATR of True Range, seeded by the first 20-day arithmetic mean; True Range is `max(high-low, abs(high-prev_close), abs(low-prev_close))`.
- System 1: long/short on a close beyond the prior 20-day high/low; exit on the prior 10-day opposite extreme. A signal is skipped when the immediately preceding System 1 signal in the same market and direction would have won, except that a simultaneous 55-day breakout is an always-taken failsafe (subject only to portfolio caps). Skipped signals are tracked hypothetically through the same 2N stop/10-day exit so the next filter decision is stateful.
- System 2: long/short on a close beyond the prior 55-day high/low; every signal is eligible, with the prior 20-day opposite extreme as exit.
- Both systems run simultaneously. Their units are separately associated with their system exit, but count together against the same market and portfolio caps. If the other system already holds the same symbol in the same direction, the new unit uses a 0.5 risk multiplier (0.5% rather than 1% at the defaults) to reduce duplicated same-instrument concentration without forbidding the historically simultaneous systems.
- Position sizing: a normal new unit contains `(1% * current internally simulated equity) / current N` fractional shares; an overlapping same-direction System 1/System 2 unit uses half that risk. This preserves the futures-style risk-normalized notional calculation while correcting how capital availability is enforced.
- Pyramiding: each campaign proposes another full unit for every 0.5N favorable move from its prior add level, up to the shared four-unit market limit. A crossed level rejected by a risk cap is skipped whole, never partially filled.
- Stops: every unit starts 2N from its own fill. A new same-direction unit tightens every existing same-market unit to the new unit's effective stop (raised for longs, lowered for shorts; never loosened if N expands).
- Execution interpretation: breakouts, channel exits, and stops are evaluated on adjusted closes. This is required by LazyAlpha's unchanged close-to-next-close weight protocol; it does not claim intraday stop fills or futures tick execution.

#### Correlation groups and layered unit limits

| Close group | ETFs |
|---|---|
| Equities | SPY, QQQ, IWM |
| Bonds | TLT, IEF |
| Metals | GLD, SLV |
| Commodities | DBC, USO |
| Currency | UUP |

All original caps are tested before each complete unit and are direction-specific, consistent with Faith's published wording: maximum 4 units per market; 6 in one direction inside a close group; 10 in one direction across every pairwise union of close groups; and 12 units in one direction portfolio-wide. The published rules name examples of loosely correlated futures but do not define a complete ETF taxonomy. The pairwise-union interpretation uses only the CEO-specified close groups, avoids inventing extra sectors, and keeps the 10- and 12-unit layers independently operative.

Two distinct proactive capital constraints then apply to every initial entry and pyramid add. First, current margin committed by every open unit plus the proposed unit's `abs(shares * current price) * margin_ratio` must not exceed current equity. Futures margin is a performance bond and normally only a fraction of notional, unlike buying an ETF outright; CME and Schwab both describe typical futures margin as roughly 3%-12% of contract notional. The fixed 10% proxy is near the upper end of that published range and matches this repository's maintenance-margin experiment. Second, proposed aggregate gross notional divided by equity must not exceed the independent 1.0x operator safety ceiling. Passing the margin test does not waive the leverage ceiling.

Sources: [CME, Margin: Know What's Needed](https://www.cmegroup.com/education/courses/introduction-to-futures/margin-know-what-is-needed); [Schwab futures-margin overview](https://www.schwab.com/futures/futures-margin).

The same-symbol overlap reduction implements the established risk-management principle that leverage and position concentration must be monitored against explicit limits; the CFTC names both in its market-risk requirements. No authoritative source located prescribes one universal reduction factor for two Turtle systems on one instrument, so 0.5 is disclosed as the fixed operator policy factor, not a historically sourced Turtle constant.

Source: [CFTC market-risk rule, 17 CFR risk-management provisions](https://www.cftc.gov/LawRegulation/FederalRegister/finalrules/2012-5317.html).

**Major universe limitation:** LazyAlpha previously centered on SPY/QQQ, whose high correlation makes correlation caps and the original diversification mechanism nearly meaningless. These ten ETFs deliberately add rates, metals, commodities, and a dollar proxy, but remain US-listed proxies. This is a faithful mechanical replication of published rules on real ETF data, not a replication of the original edge, which depended on roughly two dozen genuinely different futures markets across asset classes and geographies.

#### Realized units, leverage, and reconciliation

- Peak aggregate gross leverage: 1.0679x
- Average aggregate gross leverage: 0.7603x
- Maximum concurrent units: 6
- Cap-skipped entry/add signals: 6093 (market=3, close-group=0, loose-group=0, direction=0, insufficient-margin=0, leverage-ceiling=6090)
- Same-symbol/same-direction System 1/System 2 concentration-reduced units: 47
- System 1 filter skips: 348; initial entries: 236; pyramid additions: 40
- Internal-equity versus the reported 5.00-bps `run_backtest` maximum absolute difference: 5.58793544769e-09; required tolerance: 0.0001; confirmed: `True`.
- The internal loop deducts the same one-session-lagged LazyAlpha turnover charge as the reported backtest before sizing that close's new units. Current simulated equity is therefore the strategy's own net marked-to-market equity, including modeled transaction costs.
- The leverage ceiling is checked immediately before additions; ordinary price moves can subsequently carry existing gross leverage slightly above 1.0x until positions exit. LazyAlpha still does not model financing/collateral yield, contract-specific or changing exchange margins, or portfolio offsets. Cash return is zero.

#### OHLC construction

- Raw fields: `high`, `low`, `close`, and `adj_close` from `market-data-hub prices_daily`, with live rows excluded.
- Back-adjustment: on every symbol/date, multiply raw high and low by `adj_close / close`; use `adj_close` as the close. Thus ATR and breakout channels share the corporate-action-consistent price scale used for returns.
- Validated OHLC common panel: 2010-01-04 to 2026-09-10 (4196 sessions). Dates with an incomplete cross-symbol row are excluded from the common panel, exactly as in the standard adjusted-close adapter; nothing is imputed. Missing required columns/symbols, duplicates, non-finite present values, or non-positive present values are fatal.

#### Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: SPY, QQQ, IWM, TLT, IEF, GLD, SLV, DBC, USO, UUP
- Validated common panel: 2010-01-04 to 2026-09-10; 4196 rows
- Database: `market-data-hub configured default`

| Symbol | Last date | Status | Coverage score | Stalled |
|---|---:|---|---:|---|
| DBC | 2026-09-10 00:00:00 | ok | 95.50 | False |
| GLD | 2026-09-10 00:00:00 | ok | 95.50 | False |
| IEF | 2026-09-10 00:00:00 | ok | 98.50 | False |
| IWM | 2026-09-10 00:00:00 | ok | 98.50 | False |
| QQQ | 2026-09-10 00:00:00 | ok | 98.50 | False |
| SLV | 2026-09-10 00:00:00 | ok | 95.50 | False |
| SPY | 2026-09-10 00:00:00 | ok | 98.52 | False |
| TLT | 2026-09-10 00:00:00 | ok | 98.51 | False |
| USO | 2026-09-10 00:00:00 | ok | 95.50 | False |
| UUP | 2026-09-10 00:00:00 | ok | 95.51 | False |

#### Research rationale

Volatility-normalized breakouts across genuinely diverse markets may capture infrequent persistent trends, while 2N stops, pyramiding rules, and layered portfolio heat limits constrain failed breakouts.

Run the published 20/10-day filtered System 1 and unfiltered 55/20-day System 2 together; size every unit at 1% of current equity per N, add at 0.5N, tighten stops, and enforce all four unit-cap layers.

Sources:

- [The Original Turtle Trading Rules Explained](https://www.theturtletrader.com/turtle-trading-rules/) — Corroborates N/ATR sizing, 20/55-day entries, the System 1 winner filter and failsafe, 10/20-day exits, 2N stops, 0.5N adds, and the 4/6/10/12 unit limits.
- [Way of the Turtle: Original Turtle Trading Rules](https://www.brookstradingcourse.com/wp-content/uploads/wpforo/attachments/12514/3508-CurtisFaith-WayoftheTurtle-1.pdf) — Original Turtle Curtis Faith describes the two systems, the 0.5N pyramid sequence, prior-breakout filter, and direction-specific correlated-market unit limits.
- [The Original Turtle Rules](https://tradingblox.com/originalturtles/originalturtlerules.htm) — Hosts the freely published complete rules covering entries, position sizing, adds, stops, exits, and portfolio limits.

Known risks:

- ten US-listed ETFs only partially approximate the original global futures diversification
- close-based ETF execution differs from intraday stop orders and futures contract mechanics
- the fixed margin proxy omits contract-specific and changing exchange requirements, portfolio offsets, and financing/collateral yield
- borrow availability, short fees, slippage, taxes, and market impact are not modeled
- one historical sample and one fixed universe are not evidence of future profitability

#### Net backtest metrics

| Metric | Strategy | Benchmark |
|---|---:|---:|
| Gross cumulative return | 52.31% | 265.80% |
| Cumulative return | 30.63% | 265.62% |
| CAGR | 1.62% | 8.10% |
| Annualized volatility | 20.90% | 10.62% |
| Annualized Sharpe (rf=0) | 0.18 | 0.79 |
| Maximum drawdown | -51.34% | -23.48% |
| Annualized turnover | 1843.83% | 6.01% |
| Transaction-cost drag (sum of daily rates) | 15.35% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2010-01-04 to 2020-01-02 | 2517 | 12.69% | 1.20% | 18.26% | 0.16 | -51.34% | 68.40% | 0.62 | -55.71% | -0.46 |
| oos_1 | out_of_sample | 2020-01-03 to 2026-09-10 | 1679 | 1.99% | 0.30% | 24.20% | 0.14 | -48.19% | 115.74% | 0.98 | -113.75% | -0.84 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: FAIL: degrades out of sample; the frozen strategy trails the benchmark on return or Sharpe in at least one OOS window.**

This remains historical research, not evidence of tradability or a recommendation. Promotion still requires parameter-robustness and multiple-testing checks plus a live paper period.

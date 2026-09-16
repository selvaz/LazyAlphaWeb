# LazyAlpha experiment â€” ma_crossover_50_200

*This is a comparative research note, not a single-strategy model card. It may compare multiple variants and does not carry a single PASS/FAIL verdict badge.*

**Generated:** 2026-09-13T14:14:50+00:00


Generated: 2026-09-13T14:14:50+00:00

## Experiment

- Period: 2015-01-02 to 2026-06-30 (2889 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: Kenneth French Data Library `FF5_daily/RF` daily simple return applied only to `max(0, 1 - sum(asset weights))`
- Slippage: 1.00 bps per unit of turnover, modeled separately from the commission-style transaction cost
- Slippage scope: one flat input is a disclosed simplification, not an instrument-level estimate. SPY/QQQ spreads are commonly around 0.3-1 bp; less-liquid instruments, including some commodity ETFs, can warrant materially higher assumptions.
- Spread sources: [Natixis, *Assessing ETF cost: Understanding the bid/ask spread*](https://www.im.natixis.com/en-us/insights/portfolio-construction/2024/etf-cost-bid-ask-spread); [ETF.com, *ETFs With The Highest & Lowest Trading Spreads*](https://www.etf.com/sections/news/etfs-highest-lowest-trading-spreads)
- Risk-free source: [Kenneth R. French Data Library, Fama/French 5 Factors (2x3), daily](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)
- Parameters: fast=50, slow=200, risk_free_source=ff5-rf, slippage_bps=1.0

## Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: SPY, QQQ
- Validated common panel: 2015-01-02 to 2026-06-30; 2889 rows
- Database: `C:\Users\Administrator\Documents\GitHub\market-data-hub\market_data.duckdb`

| Symbol | Last date | Status | Coverage score | Stalled |
|---|---:|---|---:|---|
| QQQ | 2026-08-14 00:00:00 | ok | 97.31 | False |
| SPY | 2026-08-14 00:00:00 | ok | 97.33 | False |

## Research rationale

A slow trend filter may reduce severe drawdowns, but after costs it need not beat passive exposure.

For each ETF, hold it when its 50-day moving average is above its 200-day average; equal-weight active ETFs; otherwise cash.

Sources:

- [A Quantitative Approach to Tactical Asset Allocation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461) â€” Motivates a simple trend-following tactical allocation rule across asset classes.
- [A Quantitative Approach to Faber's Tactical Asset Allocation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1476225) â€” Warns that attractive rule-based results require statistical caution and bootstrap-style robustness tests.
- [Momentum Trading, Return Chasing, and Predictable Crashes](https://www.nber.org/papers/w20660) â€” Documents high historical momentum returns alongside material and sometimes predictable crash risk.

Known risks:

- whipsaw and repeated transaction costs in sideways markets
- parameter/data-mining sensitivity
- cash accrual relies on the historical FF5_daily/RF series and is limited to its verified coverage
- one historical sample is not evidence of future profitability

## Net backtest metrics

| Metric | Strategy | Benchmark |
|---|---:|---:|
| Gross cumulative return | 330.35% | 491.34% |
| Cumulative return | 324.69% | 490.98% |
| CAGR | 13.44% | 16.76% |
| Annualized volatility | 16.74% | 19.47% |
| Annualized Sharpe (rf=0) | 0.84 | 0.89 |
| Maximum drawdown | -30.86% | -30.86% |
| Annualized turnover | 191.90% | 8.72% |
| Commission-cost drag (sum of daily rates) | 1.10% | 0.05% |
| Slippage-cost drag (sum of daily rates) | 0.22% | 0.01% |
| Total trading-cost drag (sum of daily rates) | 1.32% | 0.06% |
| Cash-accrual contribution (sum of daily portfolio-return contributions) | 3.22% | 0.00% |

## Paper-trading readiness

- [ ] Live execution and fill feed
- [ ] Measured realized slippage; this run uses only the stated assumption
- [ ] Borrow and financing costs for leveraged strategies
- [ ] Capacity and market-impact estimate at the intended position size

## Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2015-01-02 to 2021-11-17 | 1733 | 145.15% | 13.93% | 17.37% | 0.84 | -30.86% | 226.83% | 1.01 | -81.68% | -0.17 |
| oos_1 | out_of_sample | 2021-11-18 to 2026-06-30 | 1156 | 92.37% | 15.33% | 14.46% | 1.06 | -20.78% | 79.48% | 0.73 | 12.89% | 0.33 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: PASS: coherent between development and OOS; the frozen strategy matches or beats the benchmark on return and Sharpe in every OOS window.**

## Conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: PASS: coherent between development and OOS; the frozen strategy matches or beats the benchmark on return and Sharpe in every OOS window.**

This remains historical research, not evidence of tradability or a recommendation. There is still no parameter-search correction or project-level multiple-testing adjustment for this strategy; promotion also requires a live paper period.

## Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)


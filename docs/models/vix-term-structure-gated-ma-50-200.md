# Strategy: vix_term_structure_gated_ma_50_200

1 variant(s) documented · earliest 2026-09-12 · latest 2026-09-12.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="fast=50, slow=200, term_symbols=[&#x27;^VIX&#x27;, &#x27;^VIX3M&#x27;], ratio=^VIX3M/^VIX, active_threshold=1.0"><code>fast=50, slow=200, term_symbols=[&#x27;^VIX&#x27;, &#x27;^VIX3M&#x27;], ratio=^VIX3M/^VIX, active_t…</code></a> | 2026-09-12T14:05:38+00:00 | ✓ | <span class="verdict-badge verdict-badge--pass">PASS</span> |

### Variant 1 {: #variant-1 }

**Generated:** 2026-09-12T14:05:38+00:00  
**Source report:** `20260912_140538_vix_term_structure_gated_ma_50_200.md`  
**Registered:** ✓ — 2026-09-12T14:05:38+00:00 (walk_forward_passed=True)

<span class="verdict-badge verdict-badge--pass">PASS</span>

<img src="../assets/charts/vix-term-structure-gated-ma-50-200__variant-1.svg" alt="vix_term_structure_gated_ma_50_200 variant 1 return and Sharpe comparison">
#### Experiment

- Period: 2015-01-02 to 2026-07-02 (2891 sessions)
- Data-availability truncation: the requested sample intentionally ends on 2026-07-02, the last trading session before the first missing non-live `^VIX3M` row (2026-07-06) in the upstream market-data-hub database. Later `^VIX3M` coverage is incomplete/sparse, so this report must not be read as running through the present.
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: fast=50, slow=200, term_symbols=['^VIX', '^VIX3M'], ratio=^VIX3M/^VIX, active_threshold=1.0

#### VIX term-structure provenance and action rule

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Symbols: ^VIX, ^VIX3M
- Validated exact trading-session coverage: 2015-01-02 to 2026-07-02; 2891 rows
- Database: `C:\Users\Administrator\Documents\GitHub\market-data-hub\market_data.duckdb`
- Frozen ratio and gate: `^VIX3M / ^VIX >= 1.0` is contango/active; a ratio below 1.0 is backwardation/risk-off and zeros the existing MA weights
- Official end-of-day VIX-family closes are unrevised; the backtest engine applies every close-derived weight one session later
- Any missing required VIX-family observation raises `VixTermStructureDataUnavailable`; no unconditional fallback or invented value is allowed

#### Data provenance

- Source: `market-data-hub` (`adj_close`; live rows included: `False`)
- Requested symbols: SPY, QQQ
- Validated common panel: 2015-01-02 to 2026-07-02; 2891 rows
- Database: `C:\Users\Administrator\Documents\GitHub\market-data-hub\market_data.duckdb`

| Symbol | Last date | Status | Coverage score | Stalled |
|---|---:|---|---:|---|
| QQQ | 2026-08-14 00:00:00 | ok | 97.31 | False |
| SPY | 2026-08-14 00:00:00 | ok | 97.33 | False |

#### Research rationale

Conditioning the existing equity trend allocation on the VIX term structure may reduce exposure during acute volatility shocks: contango is treated as the active/calm state and backwardation as the risk-off state.

Compute the official end-of-day close ratio ^VIX3M / ^VIX for every SPY/QQQ session. Apply the frozen 50/200 moving-average weights when the ratio is at least 1.0 and otherwise hold cash; retain the backtest engine's one-session execution lag.

Sources:

- [A tactical asset allocation strategy that exploits variations in VIX](https://www.businessperspectives.org/index.php/journals/investment-management-and-financial-innovations/issue-247/a-tactical-asset-allocation-strategy-that-exploits-variations-in-vix) — Cloutier, Djatej, and Kiefer provide academic evidence that VIX-derived conditioning changes tactical equity allocation risk-adjusted outcomes.
- [Using VIX Futures Term Structure](https://harbourfrontquant.substack.com/p/using-vix-futures-term-structure) — Documents empirically that VIX-curve backwardation has coincided with acute S&P 500 stress and drawdowns, while contango is the normal calmer state.

Known risks:

- backwardation is a stress-confirmation signal, not a precise entry or exit timer, and it can persist for weeks
- the gate is better suited to sharp volatility shocks such as 2008/2020 than slow grinding bear markets such as 2022
- cash return is modeled as zero and execution frictions are incomplete
- one historical sample is not evidence of future profitability

#### Net backtest metrics

| Metric | Strategy | Ungated MA | Benchmark |
|---|---:|---:|---:|
| Gross cumulative return | 215.47% | 309.40% | 480.96% |
| Cumulative return | 196.51% | 304.91% | 480.67% |
| CAGR | 9.94% | 12.96% | 16.57% |
| Annualized volatility | 12.67% | 16.73% | 19.47% |
| Annualized Sharpe (rf=0) | 0.81 | 0.81 | 0.89 |
| Maximum drawdown | -21.13% | -30.86% | -30.86% |
| Annualized turnover | 1080.87% | 191.77% | 8.72% |
| Transaction-cost drag (sum of daily rates) | 6.20% | 1.10% | 0.05% |

#### Walk-forward / out-of-sample validation

Parameters were frozen before the chronological split. Each window is non-overlapping and backtested independently.

| Window | Role | Period | Sessions | Return | CAGR | Volatility | Sharpe | Max drawdown | Benchmark return | Benchmark Sharpe | Return delta | Sharpe delta |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| development | development | 2015-01-02 to 2021-11-18 | 1734 | 100.51% | 10.64% | 12.22% | 0.89 | -21.13% | 229.11% | 1.01 | -128.60% | -0.12 |
| oos_1 | out_of_sample | 2021-11-19 to 2026-07-02 | 1157 | 77.59% | 13.32% | 11.99% | 1.10 | -10.89% | 76.01% | 0.71 | 1.57% | 0.39 |

Pass criterion: in every OOS window, strategy cumulative return and annualized Sharpe must each be at least the corresponding benchmark value.

**Walk-forward verdict: PASS: coherent between development and OOS; the frozen strategy matches or beats the benchmark on return and Sharpe in every OOS window.**

#### Giudizio / conclusion

**Full-sample comparison: FAIL on this sample: lower net return and Sharpe than the benchmark.**

**Final validation judgment: PASS: coherent between development and OOS; the frozen strategy matches or beats the benchmark on return and Sharpe in every OOS window.**

This remains historical research, not evidence of tradability or a recommendation. Promotion still requires parameter-robustness and multiple-testing checks plus a live paper period.

#### Ecosystem review

- **LazyFin:** Do not recreate hierarchical portfolio optimization in LazyAlpha; the line was moved/retired from LazyFin and belongs to LazyPortfolio. (`C:\Users\Administrator\Documents\GitHub\LazyFin\docs\status.md`)
- **investmentcommittee:** Keep B0/P0/Sa/PH/PF as methodological reference: same data, folds, costs and rebalance rules for honest comparisons; do not clone it 1:1. (`C:\Users\Administrator\Documents\GitHub\investment-process-top-down-etf.md`)

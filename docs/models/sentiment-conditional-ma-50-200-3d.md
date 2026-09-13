# Strategy: sentiment_conditional_ma_50_200_3d

1 variant(s) documented · earliest 2026-09-11 · latest 2026-09-11.

| Variant | Generated | Registered | Verdict |
|---|---|---:|---|
| <a href="#variant-1" title="fast=50, slow=200, rolling_window=3, daily_aggregation=equal_weight_mean_across_digests, normalization=positive_minus_negative_hits_div_total_words, lag=calendar_day_D_to_next_trading_session, lexicon=simplified_finance_domain_subset_not_full_LM"><code>fast=50, slow=200, rolling_window=3, daily_aggregation=equal_weight_mean_across…</code></a> | 2026-09-11T19:16:46+00:00 | — | <span class="verdict-badge verdict-badge--warn">NOT EVALUABLE</span> |

### Variant 1 {: #variant-1 }

<div class="la-model-result">
<div class="la-model-result__headline">
<span class="la-kicker">Recorded outcome</span>
<span class="verdict-badge verdict-badge--warn">NOT EVALUABLE</span>
</div>
<figure class="la-chart la-chart--fallback" data-chart-kind="fallback">
  <div class="la-chart__label">Metrics-only summary</div>
  <img src="../../assets/charts/sentiment-conditional-ma-50-200-3d__variant-1.svg" alt="sentiment_conditional_ma_50_200_3d variant 1 metrics-only bar chart; no equity time series available" width="576" height="241" decoding="async">
  <figcaption>No equity time series available for this run · return and Sharpe bars only</figcaption>
</figure>
</div>

**Generated:** 2026-09-11T19:16:46+00:00  
**Source report:** `20260911_191646_sentiment_conditional_ma_50_200_3d.md`  
**Registered:** —
#### Experiment

- Period: 2026-08-10 to 2026-08-14 (5 sessions)
- Execution rule: close-derived weights are applied one session later
- Transaction costs: 5.00 bps per unit of turnover
- Cash return: 0%; taxes, slippage and market impact: not modeled
- Parameters: fast=50, slow=200, rolling_window=3, daily_aggregation=equal_weight_mean_across_digests, normalization=positive_minus_negative_hits_div_total_words, lag=calendar_day_D_to_next_trading_session, lexicon=simplified_finance_domain_subset_not_full_LM

#### Digest-sentiment provenance and action rule

- Source: `digests` in `C:\ProgramData\InvestmentCommittee\live\db\digests.db` (SQLite URI `mode=ro` plus `PRAGMA query_only=ON`)
- Path resolution: explicit argument, else `os.environ.get('DIGESTS_DB')`, else the production literal; this run used DIGESTS_DB environment variable
- Production rows: 156 total; 152 scored; 4 empty-text rows explicitly excluded (never scored as neutral)
- Calendar coverage: 2026-08-05 to 2026-09-11 (38 distinct consecutive days)
- Engines: claude, deepseek; cycles: europeclose, morning, usclose
- Per-digest score: `(positive exact-token hits - negative exact-token hits) / all alphabetic word tokens`; same-day digests are aggregated by an equal-weight arithmetic mean
- Positive subset (34 terms): `accelerate`, `accelerated`, `accelerating`, `advance`, `advanced`, `advances`, `beat`, `beats`, `bullish`, `expansion`, `gain`, `gained`, `gains`, `grow`, `growing`, `growth`, `improve`, `improved`, `improvement`, `outperform`, `outperformed`, `profit`, `profitable`, `rally`, `rebound`, `rebounded`, `recovery`, `resilient`, `strength`, `strong`, `stronger`, `surge`, `surged`, `upside`
- Negative subset (34 terms): `bankrupt`, `bankruptcy`, `bearish`, `breach`, `contraction`, `crisis`, `decline`, `declined`, `declines`, `default`, `defaults`, `distress`, `distressed`, `downgrade`, `downgraded`, `fraud`, `impairment`, `insolvency`, `liquidation`, `loss`, `losses`, `miss`, `missed`, `plunge`, `plunged`, `recession`, `slump`, `slumped`, `underperform`, `underperformed`, `warning`, `weak`, `weaker`, `weakness`
- Dictionary limitation: this is a simplified, manually curated representative finance-news subset inspired by Loughran & McDonald (2011), not the licensed/full Loughran-McDonald Master Dictionary and not a claim to reproduce it
- Routine finance terms including `liability`, `tax`, and `cost` are intentionally absent; exact-token matching avoids assigning their generic-English polarity
- Frozen gate: apply the existing 50/200 MA weights only when the trailing 3-calendar-day mean daily sentiment is strictly positive; otherwise cash
- Window rationale: three calendar days was frozen before this run as a short smoother appropriate to an initial ~38-day history; it reduces single-digest/engine noise while preserving more usable observations than a five-day window
- Lag rule: every calendar-day D digest score first becomes eligible for the next trading session after D; the backtest engine's uniform one-session weight shift is retained
- Evaluation-only overlap: 2026-08-10 to 2026-08-14; earlier price rows are retained only to warm up the frozen 200-day MA and are excluded from all reported metrics
- Missing required calendar-day or trading-day coverage raises `DigestSentimentDataUnavailable`; it is never imputed as zero/neutral
- Methodology source: [Loughran & McDonald (2011), *The Journal of Finance* 66(1), 35-65](https://doi.org/10.1111/j.1540-6261.2010.01625.x)

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

A positive short-horizon tone in the operator's own crawled news digests may identify periods when the existing trend signal is safer to hold, but the current history is far too short to test that claim conclusively.

Score every digest with an explicitly documented finance-domain positive/negative exact-token subset, average digest scores by calendar day, take a frozen three-day trailing mean, and gate the existing 50/200 MA weights on strictly positive sentiment. A calendar-day D digest can affect only the next trading session.

Sources:

- [When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks](https://doi.org/10.1111/j.1540-6261.2010.01625.x) — Shows why generic negative dictionaries misclassify many routine financial words and motivates finance-specific categories.

Known risks:

- the hand-curated subset is much smaller than the full published dictionary
- digest selection and summarization can change measured tone
- three-day smoothing can lag abrupt news reversals
- the currently available overlap is informational only
- cash return is modeled as zero and execution frictions are incomplete

#### Net backtest metrics

| Metric | Strategy | Ungated MA | Benchmark |
|---|---:|---:|---:|
| Cumulative return | 0.70% | 0.76% | 0.76% |
| CAGR | 42.46% | 46.11% | 46.11% |
| Annualized volatility | 8.63% | 8.50% | 8.50% |
| Annualized Sharpe (rf=0) | 4.14 | 4.50 | 4.50 |
| Maximum drawdown | -0.33% | -0.33% | -0.33% |
| Annualized turnover | 5040.00% | 0.00% | 0.00% |
| Transaction-cost drag (sum of daily rates) | 0.05% | 0.00% | 0.00% |

#### Walk-forward / out-of-sample validation

**Walk-forward verdict: NOT RUN / NOT EVALUABLE.** The real digest history is too short for a statistically meaningful development/OOS split. These metrics are a short-sample infrastructure smoke test only, not a PASS/FAIL verdict.

#### Giudizio / conclusion

**INFORMATIONAL ONLY / NON-CONCLUSIVE.** The observed return, Sharpe, and drawdown differences are descriptive metrics from a very short overlap, not evidence for promotion and not a strategy verdict.

This remains historical research, not evidence of tradability or a recommendation. Promotion still requires parameter-robustness and multiple-testing checks plus a live paper period.

#### Ecosystem review

- **LazyAlpha backlog:** Family 4 explicitly calls for sentiment from LazyCrawler's own digests, so this implementation reuses the named proprietary data asset and the existing MA signal rather than duplicating another family. (`C:\Users\Administrator\Documents\GitHub\LazyAlpha\docs\candidate-strategy-families.md`)

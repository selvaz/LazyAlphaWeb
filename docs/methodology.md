---
title: Methodology
description: How LazyAlpha backtests strategies, assigns verdicts, and reports results honestly.
---

# Methodology

LazyAlpha is budget-aware research infrastructure for systematic trading strategies: it reviews research, checks for overlap with the surrounding ecosystem, tests candidates on real data, and writes a report even when the outcome is negative. This site publishes those documented research results. It is not investment advice, an execution system, or a live track record.

## Verdict vocabulary

<span class="verdict-badge verdict-badge--pass">PASS</span>

For walk-forward validation, **PASS** means that in every out-of-sample window, the frozen strategy's cumulative return **and** annualized Sharpe both meet or beat the benchmark.

<span class="verdict-badge verdict-badge--fail">FAIL</span>

For walk-forward validation, **FAIL** means that the strategy trails the benchmark on cumulative return or annualized Sharpe in at least one out-of-sample window.

<span class="verdict-badge verdict-badge--warn">INCONCLUSIVE</span>

For a full-sample comparison only, **INCONCLUSIVE** means that the strategy is better on only one of cumulative return or annualized Sharpe, not both. It is not a walk-forward pass.

<span class="verdict-badge verdict-badge--warn">INFORMATIONAL ONLY / NON-CONCLUSIVE</span>

The available history is too short for a real walk-forward split. The result is descriptive only and is not a verdict.

<span class="verdict-badge verdict-badge--warn">NOT EVALUABLE / NOT RUN</span>

A required data precondition, such as point-in-time coverage, was not met, so the strategy could not be honestly tested at all. This is explicitly **not** the same as failing a test.

## Backtest conventions and limitations

- Signals computed using the close at session `t` are applied to the return at session `t+1`.
- Transaction cost is calculated as `abs(weight change) * cost_bps / 10,000`.
- Cash earns zero return.
- Strategy and benchmark comparisons use the same symbols, dates, and transaction-cost assumption.
- Walk-forward validation uses disjoint chronological windows: a development window followed by one or more out-of-sample windows. The configured strategy is copied independently into each window, with parameters frozen before the split so parameter choices and indicator state cannot leak from development into out-of-sample evaluation.
- Adjusted closes are used where specified to reduce corporate-action distortions.
- Taxes, bid/ask spread, market impact, borrow, capacity, and execution uncertainty are not modeled. There is no parameter-search correction, survivorship analysis, or live paper track record. A historical pass alone must not be promoted to trading.

## Honest-reporting commitment

Every metric, quotation, and verdict sentence displayed inside a model card or research note is copied byte-for-byte from a LazyAlpha report. Aggregate counts (e.g. how many experiments are documented, how many passed), registration-match summaries, PASS/FAIL badges derived from the registry's own boolean field, and chart axes are mechanically computed from that same verbatim source data by a deterministic, auditable script — never invented, never edited by hand, but not themselves literal substrings of a report file. The generator's own source is public in this repository's `scripts/build_site.py`. A FAIL or blocked result is stated just as plainly as a PASS; negative, incomplete, and non-evaluable outcomes are not hidden or softened. Nothing on this site is investment advice or evidence of a live track record.

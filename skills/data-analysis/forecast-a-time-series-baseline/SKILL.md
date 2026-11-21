---
name: forecast-a-time-series-baseline
description: Forecast a time series with a reproducible baseline and honest backtest error. Use when the user needs a transparent baseline forecast and error estimate.
domain: data-analysis
tags: [forecasting, baseline-model, backtesting]
triggers: ["baseline time series forecast", "forecast time series baseline", "backtest a simple forecast"]
---

# Forecast a time series with a reproducible baseline and honest backtest error

## Purpose

Forecast a time series with a reproducible baseline and honest backtest error.

## When to use

Use when the user needs a transparent baseline forecast and error estimate.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Set the forecast horizon and rolling evaluation windows.
2. Build seasonal naive, moving-average, or linear baselines.
3. Backtest each baseline and record forecast errors.
4. Compare performance with the naive forecast and diagnose bias.
5. Publish point forecasts, intervals, assumptions, and known limits.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `analyse-a-time-series`
- `analyse-a-survey-result`
- `analyse-a-text-corpus`

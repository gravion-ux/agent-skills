---
name: analyse-a-time-series
description: Analyze a time series with trend, seasonality, structural breaks, and data-quality checks. Use when the user needs to understand patterns in measurements over time.
domain: data-analysis
tags: [time-series, seasonality, trend-analysis]
triggers: ["time series analysis", "analyze trends over time", "detect seasonality in time data"]
---

# Analyze a time series with trend, seasonality, structural breaks, and data-quality checks

## Purpose

Analyze a time series with trend, seasonality, structural breaks, and data-quality checks.

## When to use

Use when the user needs to understand patterns in measurements over time.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Verify the time grain, frequency, coverage, and missing periods.
2. Plot the level, changes, and rolling summaries.
3. Test for trend, seasonality, and structural breaks.
4. Quantify noise and identify influential time periods.
5. Summarise patterns and drivers without asserting causation.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `forecast-a-time-series-baseline`
- `analyse-a-survey-result`
- `analyse-a-text-corpus`

---
name: detect-outliers-in-a-numeric-column
description: Flag unusual numeric values with domain thresholds and assess whether they distort conclusions. Use when the user suspects extreme values may be affecting a numeric analysis.
domain: data-analysis
tags: [outlier-detection, anomaly-review, sensitivity-analysis]
triggers: ["numeric outliers", "detect outliers in a column", "review unusual values"]
---

# Flag unusual numeric values with domain thresholds and assess whether they distort conclusions

## Purpose

Flag unusual numeric values with domain thresholds and assess whether they distort conclusions.

## When to use

Use when the user suspects extreme values may be affecting a numeric analysis.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Inspect the column distribution, units, and plausible operating range.
2. Choose a domain threshold or statistical rule for candidate outliers.
3. Flag candidates and inspect a sample of their source records.
4. Compare key results with and without the flagged observations.
5. Document each treatment and retain a sensitivity comparison.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `tell-a-data-story-in-a-narrative`
- `analyse-a-survey-result`
- `analyse-a-text-corpus`

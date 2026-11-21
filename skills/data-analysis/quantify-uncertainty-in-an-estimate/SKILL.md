---
name: quantify-uncertainty-in-an-estimate
description: Quantify uncertainty around an estimate with intervals, assumptions, and sensitivity checks. Use when the user needs to communicate the uncertainty behind an estimate.
domain: data-analysis
tags: [uncertainty-quantification, confidence-interval, sensitivity-analysis]
triggers: ["uncertainty in estimate", "quantify estimate uncertainty", "add confidence interval to estimate"]
---

# Quantify uncertainty around an estimate with intervals, assumptions, and sensitivity checks

## Purpose

Quantify uncertainty around an estimate with intervals, assumptions, and sensitivity checks.

## When to use

Use when the user needs to communicate the uncertainty behind an estimate.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Define the estimand and enumerate the main uncertainty sources.
2. Choose an interval method that matches the sampling or model design.
3. Calculate the interval and state how it should be interpreted.
4. Vary key modelling and missing-data assumptions.
5. Report the estimate, interval, sensitivity, and remaining limitations.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `handle-missing-values-in-an-analysis`
- `build-an-interactive-analysis-dashboard`
- `design-an-experiment-with-a-control-group`

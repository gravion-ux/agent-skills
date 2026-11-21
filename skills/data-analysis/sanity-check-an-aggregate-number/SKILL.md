---
name: sanity-check-an-aggregate-number
description: Sanity-check an aggregate against components, bounds, and independent reasonableness tests. Use when the user needs to verify that a reported total makes sense.
domain: data-analysis
tags: [aggregate-checking, reasonableness-tests, metric-validation]
triggers: ["sanity check aggregate number", "validate a total", "reasonableness check metric"]
---

# Sanity-check an aggregate against components, bounds, and independent reasonableness tests

## Purpose

Sanity-check an aggregate against components, bounds, and independent reasonableness tests.

## When to use

Use when the user needs to verify that a reported total makes sense.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Confirm the metric definition, filters, grain, and time period.
2. Decompose the total into additive components or segments.
3. Test bounds, proportions, and unit-level arithmetic.
4. Compare with a prior-period baseline or an independent source.
5. Reconcile differences and flag any unexplained residual.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `build-an-interactive-analysis-dashboard`
- `design-an-experiment-with-a-control-group`
- `handle-missing-values-in-an-analysis`

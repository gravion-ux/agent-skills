---
name: segment-a-population-by-behaviour
description: Create behaviour-based segments with interpretable rules, sizes, and validation checks. Use when the user wants to group a population by observed behaviour.
domain: data-analysis
tags: [behavioural-segmentation, customer-grouping, validation]
triggers: ["behavioural segments", "segment population by behaviour", "create customer behaviour groups"]
---

# Create behaviour-based segments with interpretable rules, sizes, and validation checks

## Purpose

Create behaviour-based segments with interpretable rules, sizes, and validation checks.

## When to use

Use when the user wants to group a population by observed behaviour.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Choose the behavioural outcome and reference time window.
2. Define mutually exclusive segment rules using available events.
3. Assign records and count the size of every segment.
4. Compare key outcomes and test rule stability over time.
5. Validate segments with held-out data and a business review.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `analyse-a-survey-result`
- `analyse-a-text-corpus`
- `analyse-a-time-series`

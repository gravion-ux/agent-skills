---
name: compare-two-groups-statistically
description: Compare two populations with an effect size, uncertainty interval, and stated assumptions. Use when the user needs to determine whether two groups differ meaningfully.
domain: data-analysis
tags: [group-comparison, statistical-testing, effect-size]
triggers: ["compare two groups", "test difference between groups", "group comparison with effect size"]
---

# Compare two populations with an effect size, uncertainty interval, and stated assumptions

## Purpose

Compare two populations with an effect size, uncertainty interval, and stated assumptions.

## When to use

Use when the user needs to determine whether two groups differ meaningfully.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Define the groups, outcome, and comparison before testing.
2. Inspect overlap, balance, missingness, and gross outliers.
3. Run a test or interval that matches the data design and scale.
4. Report the effect size, confidence interval, and p-value together.
5. Explain assumptions, limitations, and practical significance.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `reconcile-two-different-data-sources`
- `analyse-a-survey-result`
- `analyse-a-text-corpus`

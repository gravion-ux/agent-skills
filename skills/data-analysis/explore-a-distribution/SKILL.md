---
name: explore-a-distribution
description: Describe a numeric or categorical distribution and identify shapes, gaps, and rare groups. Use when the user wants an initial view of how values are distributed.
domain: data-analysis
tags: [distribution-analysis, summary-statistics, exploratory-data]
triggers: ["distribution analysis", "explore a variable distribution", "summarize value distribution"]
---

# Describe a numeric or categorical distribution and identify shapes, gaps, and rare groups

## Purpose

Describe a numeric or categorical distribution and identify shapes, gaps, and rare groups.

## When to use

Use when the user wants an initial view of how values are distributed.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Select a table and plot that fit the variable type.
2. Summarise the centre, spread, shape, and observed range.
3. Inspect tails, missingness, gaps, and rare categories.
4. Compare meaningful segments without testing unplanned differences.
5. Record the main distributional features and their caveats.

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

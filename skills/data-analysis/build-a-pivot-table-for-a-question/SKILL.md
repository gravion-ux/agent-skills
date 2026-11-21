---
name: build-a-pivot-table-for-a-question
description: Build a pivot table that answers a specific question with clear rows, measures, and filters. Use when the user needs a pivot table organised around a specific analytical question.
domain: data-analysis
tags: [pivot-table, aggregation, tabulation]
triggers: ["pivot table for a question", "build pivot table", "summarize data in pivot rows"]
---

# Build a pivot table that answers a specific question with clear rows, measures, and filters

## Purpose

Build a pivot table that answers a specific question with clear rows, measures, and filters.

## When to use

Use when the user needs a pivot table organised around a specific analytical question.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Translate the question into row, column, and measure definitions.
2. Validate field types, category mappings, and aggregation rules.
3. Compute the measures with an explicit missing-value policy.
4. Add filters, totals, and readable category labels.
5. Cross-check subtotals and totals against the source data.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `choose-the-right-chart-for-a-question`
- `ask-a-clear-analytical-question`
- `build-a-funnel-analysis`

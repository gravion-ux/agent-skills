---
name: ask-a-clear-analytical-question
description: Frame a decision-focused analytical question with scope, metric, and decision owner. Use when the user has a vague topic but needs a question that can guide analysis.
domain: data-analysis
tags: [question-framing, analysis-planning, decision-support]
triggers: ["analytical question", "frame an analysis question", "define what the data should answer"]
---

# Frame a decision-focused analytical question with scope, metric, and decision owner

## Purpose

Frame a decision-focused analytical question with scope, metric, and decision owner.

## When to use

Use when the user has a vague topic but needs a question that can guide analysis.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Name the decision the analysis will inform.
2. Specify the population, period, and comparison the question covers.
3. Define the metric and the direction of the expected result.
4. State the acceptable uncertainty and any decision threshold.
5. Rewrite the request as one answerable question.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `build-a-pivot-table-for-a-question`
- `choose-the-right-chart-for-a-question`
- `analyse-a-survey-result`

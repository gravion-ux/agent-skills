---
name: analyse-a-survey-result
description: Analyze survey results with sampling caveats, subgroup checks, and question-level clarity. Use when the user needs to interpret responses collected through a survey.
domain: data-analysis
tags: [survey-analysis, respondent-data, subgroup-comparison]
triggers: ["survey result analysis", "analyse survey responses", "summarize survey findings"]
---

# Analyze survey results with sampling caveats, subgroup checks, and question-level clarity

## Purpose

Analyze survey results with sampling caveats, subgroup checks, and question-level clarity.

## When to use

Use when the user needs to interpret responses collected through a survey.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Inspect question wording, response rates, missingness, and coding.
2. Summarise response distributions and weighted measures when applicable.
3. Compare preplanned subgroups with uncertainty and overlap checks.
4. Review ambiguous wording, nonresponse patterns, and extreme answers.
5. Report findings without treating a convenience sample as representative.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `analyse-a-text-corpus`
- `analyse-a-time-series`
- `ask-a-clear-analytical-question`

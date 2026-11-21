---
name: calculate-a-cohort-retention-rate
description: Calculate cohort retention with explicit dates, denominators, and consistent return windows. Use when the user needs to measure retention across dated cohorts.
domain: data-analysis
tags: [cohort-analysis, retention-rate, date-cohorts]
triggers: ["cohort retention rate", "calculate cohort retention", "measure return by signup cohort"]
---

# Calculate cohort retention with explicit dates, denominators, and consistent return windows

## Purpose

Calculate cohort retention with explicit dates, denominators, and consistent return windows.

## When to use

Use when the user needs to measure retention across dated cohorts.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Define the cohort event, return event, and eligibility rules.
2. Assign records to cohorts and align dates to one calendar basis.
3. Measure returns within fixed periods after each cohort date.
4. Calculate and publish numerator, denominator, and retention rate.
5. Segment the result and document edge cases and late events.

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

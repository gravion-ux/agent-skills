---
name: profile-a-dataset-before-analysing
description: Profile rows, columns, types, ranges, and missingness before choosing an analysis method. Use when the user needs to assess a dataset before analysing it.
domain: data-analysis
tags: [data-profiling, data-quality, schema-inspection]
triggers: ["dataset profile", "profile data before analysis", "inspect dataset quality"]
---

# Profile rows, columns, types, ranges, and missingness before choosing an analysis method

## Purpose

Profile rows, columns, types, ranges, and missingness before choosing an analysis method.

## When to use

Use when the user needs to assess a dataset before analysing it.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Load a source snapshot and record its provenance.
2. Count rows, columns, unique records, and duplicate candidates.
3. Summarise column types, missing rates, ranges, and date coverage.
4. Inspect categorical frequencies and representative records.
5. Document quality caveats and filters before analysis begins.

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

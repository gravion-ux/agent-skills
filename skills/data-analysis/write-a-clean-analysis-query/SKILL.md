---
name: write-a-clean-analysis-query
description: Write a reproducible SQL query that returns the exact measure needed for the decision. Use when the user needs SQL that computes an analytical result correctly.
domain: data-analysis
tags: [sql-analysis, query-writing, data-validation]
triggers: ["clean analysis query", "write SQL for analysis", "build aggregation query"]
---

# Write a reproducible SQL query that returns the exact measure needed for the decision

## Purpose

Write a reproducible SQL query that returns the exact measure needed for the decision.

## When to use

Use when the user needs SQL that computes an analytical result correctly.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Translate the question into fields, grain, filters, and time window.
2. Inspect schemas, keys, nullability, and join cardinalities.
3. Write the select, join, filter, grouping, and ordering clauses.
4. Inspect row counts, duplicates, nulls, and unintended many-to-many joins.
5. Save the query with definitions and a short result explanation.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `automate-a-recurring-analysis-report`
- `build-a-funnel-analysis`
- `run-a-correlation-analysis`

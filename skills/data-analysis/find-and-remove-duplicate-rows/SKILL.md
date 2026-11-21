---
name: find-and-remove-duplicate-rows
description: Identify duplicate records with stable keys, compare their content, and remove confirmed copies. Use when the user needs to deduplicate rows without losing legitimate records.
domain: data-analysis
tags: [duplicate-records, deduplication, data-quality]
triggers: ["duplicate rows", "find duplicate records", "deduplicate a dataset"]
---

# Identify duplicate records with stable keys, compare their content, and remove confirmed copies

## Purpose

Identify duplicate records with stable keys, compare their content, and remove confirmed copies.

## When to use

Use when the user needs to deduplicate rows without losing legitimate records.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Define the entity and candidate key for each record.
2. Detect exact duplicates and key-based duplicate groups.
3. Compare conflicting fields and timestamps within each group.
4. Keep one record per group using a documented precedence rule.
5. Log removed counts and reasons, then rerun the duplicate check.

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

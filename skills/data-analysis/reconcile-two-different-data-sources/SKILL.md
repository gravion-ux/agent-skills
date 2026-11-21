---
name: reconcile-two-different-data-sources
description: Reconcile two data sources by aligning definitions, keys, periods, and unexplained differences. Use when the user needs to reconcile totals or records from two systems.
domain: data-analysis
tags: [data-reconciliation, source-comparison, metric-alignment]
triggers: ["reconcile two data sources", "compare mismatched data sources", "align totals across systems"]
---

# Reconcile two data sources by aligning definitions, keys, periods, and unexplained differences

## Purpose

Reconcile two data sources by aligning definitions, keys, periods, and unexplained differences.

## When to use

Use when the user needs to reconcile totals or records from two systems.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Document each source's definition, grain, coverage, and timing.
2. Normalize keys, units, filters, and date windows.
3. Compare record counts, totals, and distributions side by side.
4. Isolate bridge mismatches and quantify the remaining residual.
5. Agree the disposition of differences and document limitations.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `compare-two-groups-statistically`
- `prepare-data-for-a-stakeholder-review`
- `tell-a-data-story-in-a-narrative`

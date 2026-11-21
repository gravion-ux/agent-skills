---
name: validate-an-analysis-result
description: Validate an analytical result against source data, logic, and plausible boundaries. Use when the user wants confidence that an analytical output is correct.
domain: data-analysis
tags: [result-validation, reconciliation, quality-assurance]
triggers: ["validate analysis result", "check analytical output", "verify analysis numbers"]
---

# Validate an analytical result against source data, logic, and plausible boundaries

## Purpose

Validate an analytical result against source data, logic, and plausible boundaries.

## When to use

Use when the user wants confidence that an analytical output is correct.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Trace every output metric back to its source fields.
2. Recompute a sample or total with an independent method.
3. Check filters, joins, duplicates, grouping, and null handling.
4. Compare the result with a historical or external benchmark.
5. Document confirmed checks, unresolved issues, and confidence.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `build-an-interactive-analysis-dashboard`
- `handle-missing-values-in-an-analysis`
- `analyse-a-survey-result`

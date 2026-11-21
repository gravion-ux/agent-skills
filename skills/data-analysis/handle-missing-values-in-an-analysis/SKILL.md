---
name: handle-missing-values-in-an-analysis
description: Choose and justify missing-value treatment while preserving the analysis population. Use when the user must handle missing fields in an analysis without hiding data loss.
domain: data-analysis
tags: [missing-data, imputation, sensitivity-analysis]
triggers: ["missing values", "treat missing data in analysis", "impute missing fields"]
---

# Choose and justify missing-value treatment while preserving the analysis population

## Purpose

Choose and justify missing-value treatment while preserving the analysis population.

## When to use

Use when the user must handle missing fields in an analysis without hiding data loss.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Quantify missingness by field, group, and record age.
2. Distinguish structural unknowns from random and unavailable values.
3. Compare complete-case results with plausible imputation results.
4. Apply a documented treatment and flag every imputed value.
5. Report excluded counts and sensitivity to the chosen treatment.

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
- `quantify-uncertainty-in-an-estimate`
- `validate-an-analysis-result`

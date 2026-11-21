---
name: run-a-correlation-analysis
description: Measure pairwise associations with correlation, uncertainty, and confounding cautions. Use when the user wants to quantify relationships between variables.
domain: data-analysis
tags: [correlation, association-analysis, confounding]
triggers: ["correlation analysis", "measure association between variables", "check correlated columns"]
---

# Measure pairwise associations with correlation, uncertainty, and confounding cautions

## Purpose

Measure pairwise associations with correlation, uncertainty, and confounding cautions.

## When to use

Use when the user wants to quantify relationships between variables.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Select variables with compatible units and a plausible relationship.
2. Align records and address missing values and material outliers.
3. Compute the correlation appropriate for each variable pair.
4. Inspect scatterplots for nonlinear patterns and influential points.
5. Report coefficients with caveats and no causal interpretation.

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
- `write-a-clean-analysis-query`

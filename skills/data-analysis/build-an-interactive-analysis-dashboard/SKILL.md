---
name: build-an-interactive-analysis-dashboard
description: Build an interactive analysis dashboard with scoped metrics, controls, and performance checks. Use when the user wants a dashboard that supports repeatable analysis and exploration.
domain: data-analysis
tags: [dashboard-design, interactive-analysis, performance]
triggers: ["interactive analysis dashboard", "build analysis dashboard", "add dashboard filters and drill down"]
---

# Build an interactive analysis dashboard with scoped metrics, controls, and performance checks

## Purpose

Build an interactive analysis dashboard with scoped metrics, controls, and performance checks.

## When to use

Use when the user wants a dashboard that supports repeatable analysis and exploration.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Define the audience, decisions, and governed KPI definitions.
2. Assemble source data with refresh, lineage, and access constraints.
3. Implement filters and cross-filtering with explicit default states.
4. Optimize query latency, rendering time, and payload size.
5. Validate displayed totals and assign refresh and ownership duties.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `build-a-funnel-analysis`
- `handle-missing-values-in-an-analysis`
- `validate-an-analysis-result`

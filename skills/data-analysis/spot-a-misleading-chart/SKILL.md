---
name: spot-a-misleading-chart
description: Identify chart choices that distort comparisons and suggest a more honest representation. Use when the user suspects a chart exaggerates or conceals a comparison.
domain: data-analysis
tags: [chart-review, visualization-quality, misleading-graphics]
triggers: ["misleading chart", "check chart for distortion", "review misleading visualization"]
---

# Identify chart choices that distort comparisons and suggest a more honest representation

## Purpose

Identify chart choices that distort comparisons and suggest a more honest representation.

## When to use

Use when the user suspects a chart exaggerates or conceals a comparison.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Inspect axis scales, baselines, ranges, and units.
2. Check aggregation levels, denominator changes, and truncated axes.
3. Review labels, ordering, uncertainty, and omitted context.
4. Identify cherry-picked periods and unsupported visual emphasis.
5. Recommend a corrected chart and explain each distortion.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `choose-the-right-chart-for-a-question`
- `analyse-a-survey-result`
- `analyse-a-text-corpus`

---
name: measure-a-feature-launch-impact
description: Measure a feature launch impact with a defensible baseline, comparison, and rollout timeline. Use when the user needs to evaluate whether a released feature changed outcomes.
domain: data-analysis
tags: [feature-impact, launch-evaluation, experimentation]
triggers: ["feature launch impact", "measure feature rollout effect", "evaluate launch performance"]
---

# Measure a feature launch impact with a defensible baseline, comparison, and rollout timeline

## Purpose

Measure a feature launch impact with a defensible baseline, comparison, and rollout timeline.

## When to use

Use when the user needs to evaluate whether a released feature changed outcomes.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Define the launch date, eligible population, and success metric.
2. Reconstruct the prelaunch baseline and account for seasonality.
3. Select a credible comparison and document possible contamination.
4. Compare changes with uncertainty and inspect relevant segments.
5. Assess guardrails and recommend rollout adjustments.

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

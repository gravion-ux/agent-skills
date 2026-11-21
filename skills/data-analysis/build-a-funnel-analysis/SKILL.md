---
name: build-a-funnel-analysis
description: Build a funnel that measures stage-to-stage conversion, drop-off, and time to progress. Use when the user needs to understand conversion through an ordered process.
domain: data-analysis
tags: [funnel-analysis, conversion, dropoff]
triggers: ["funnel analysis", "build conversion funnel", "measure stage drop off"]
---

# Build a funnel that measures stage-to-stage conversion, drop-off, and time to progress

## Purpose

Build a funnel that measures stage-to-stage conversion, drop-off, and time to progress.

## When to use

Use when the user needs to understand conversion through an ordered process.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Define the eligible entry point and ordered funnel stages.
2. Map users to stages using consistent identity and timestamps.
3. Calculate stage reach, conversion, and drop-off rates.
4. Measure progression times and inspect consequential drop-off paths.
5. Document identity limits, re-entry rules, and anomalies.

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
- `build-a-pivot-table-for-a-question`
- `build-an-interactive-analysis-dashboard`

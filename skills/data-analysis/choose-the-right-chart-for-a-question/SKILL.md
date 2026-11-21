---
name: choose-the-right-chart-for-a-question
description: Choose a chart form that matches the question, comparison, and expected audience. Use when the user needs to select an appropriate chart for an analytical message.
domain: data-analysis
tags: [chart-selection, data-visualization, chart-design]
triggers: ["right chart for a question", "choose chart type", "select visualization for analysis"]
---

# Choose a chart form that matches the question, comparison, and expected audience

## Purpose

Choose a chart form that matches the question, comparison, and expected audience.

## When to use

Use when the user needs to select an appropriate chart for an analytical message.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Define the question, comparison, and audience takeaway.
2. Select a comparison, distribution, relationship, trend, or composition form.
3. Match marks, axes, scales, and encodings to the data.
4. Add accessible labels, legends, units, and direct annotations.
5. Test the reading order and note any visual caveats.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `build-a-pivot-table-for-a-question`
- `ask-a-clear-analytical-question`
- `prepare-data-for-a-stakeholder-review`

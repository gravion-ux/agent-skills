---
name: prepare-data-for-a-stakeholder-review
description: Prepare a stakeholder-ready data brief with decision context, evidence, and explicit caveats. Use when the user needs to present analytical evidence for a stakeholder decision.
domain: data-analysis
tags: [stakeholder-brief, decision-memo, data-communication]
triggers: ["data for stakeholder review", "prepare stakeholder data brief", "make analysis decision ready"]
---

# Prepare a stakeholder-ready data brief with decision context, evidence, and explicit caveats

## Purpose

Prepare a stakeholder-ready data brief with decision context, evidence, and explicit caveats.

## When to use

Use when the user needs to present analytical evidence for a stakeholder decision.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Restate the decision, audience, deadline, and acceptance criteria.
2. Select the minimum validated metrics and comparison needed.
3. Build concise charts and tables with shared definitions.
4. Separate observed findings, assumptions, limitations, and open questions.
5. Append provenance and state the recommended next action.

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
- `choose-the-right-chart-for-a-question`
- `tell-a-data-story-in-a-narrative`

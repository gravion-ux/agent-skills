---
name: tell-a-data-story-in-a-narrative
description: Tell a data-driven story with a defensible claim, evidence sequence, and clear ending. Use when the user wants to communicate an analytical finding as a narrative.
domain: data-analysis
tags: [data-storytelling, narrative-analysis, evidence-narrative]
triggers: ["data story narrative", "tell a story with data", "write analysis narrative"]
---

# Tell a data-driven story with a defensible claim, evidence sequence, and clear ending

## Purpose

Tell a data-driven story with a defensible claim, evidence sequence, and clear ending.

## When to use

Use when the user wants to communicate an analytical finding as a narrative.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Choose one audience, decision, and defensible central claim.
2. Establish the context, baseline, and stakes for the claim.
3. Sequence evidence from the finding through its practical implication.
4. Annotate uncertainty, assumptions, and contrary evidence.
5. End with the recommended action and an explicit confidence level.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `detect-outliers-in-a-numeric-column`
- `prepare-data-for-a-stakeholder-review`
- `analyse-a-survey-result`

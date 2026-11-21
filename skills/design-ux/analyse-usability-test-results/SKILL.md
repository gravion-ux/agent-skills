---
name: analyse-usability-test-results
description: Analyze usability findings and separate recurring problems from isolated observations. Use when the user needs to prioritize evidence from completed usability sessions.
domain: design-ux
tags: [usability-analysis, findings, evidence-synthesis, prioritization]
triggers: ["usability test analysis", "analyze usability test results", "synthesize usability findings"]
---

# Analyze usability findings and separate recurring problems from isolated observations

## Purpose

Analyze usability findings and separate recurring problems from isolated observations.

## When to use

Use when the user needs to prioritize evidence from completed usability sessions.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Clean session notes while preserving task identifiers and participant context.
2. Cluster observations by affected task, frequency, and severity.
3. Compare evidence with success criteria and note contradictory sessions.
4. Prioritize issues by user impact and confidence in the pattern.
5. Document evidence, open questions, and recommended follow-up tests.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `run-a-usability-test-session`
- `write-a-usability-test-script`
- `apply-design-tokens-to-a-ui`

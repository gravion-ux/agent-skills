---
name: write-a-user-flow-for-a-feature
description: Specify a feature flow with entry points, decisions, states, and recovery paths. Use when the user needs an end-to-end flow for a feature before design or build.
domain: design-ux
tags: [user-flow, feature-design, interaction-design, state-model]
triggers: ["feature user flow", "write a feature user flow", "map a feature flow"]
---

# Specify a feature flow with entry points, decisions, states, and recovery paths

## Purpose

Specify a feature flow with entry points, decisions, states, and recovery paths.

## When to use

Use when the user needs an end-to-end flow for a feature before design or build.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Map the trigger, preconditions, and success criteria for the feature.
2. List each screen, decision, transition, and terminal state in order.
3. Add empty, loading, error, and cancellation paths to the flow.
4. Attach accessibility notes and data-consent requirements to relevant steps.
5. Review the flow with product and engineering for missing transitions.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `run-a-user-interview-for-a-design-question`
- `write-microcopy-for-a-button`
- `create-a-wireframe-for-a-screen`

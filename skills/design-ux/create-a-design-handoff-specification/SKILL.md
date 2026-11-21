---
name: create-a-design-handoff-specification
description: Create a design handoff specification with flows, states, tokens, and accessibility notes. Use when the user needs to prepare a design for implementation and quality review.
domain: design-ux
tags: [design-handoff, implementation-spec, design-system, accessibility]
triggers: ["design handoff specification", "create a design handoff", "write a design implementation spec"]
---

# Create a design handoff specification with flows, states, tokens, and accessibility notes

## Purpose

Create a design handoff specification with flows, states, tokens, and accessibility notes.

## When to use

Use when the user needs to prepare a design for implementation and quality review.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Attach the user problem, success criteria, scope, and platform targets.
2. Document each flow and screen state, including empty, loading, and error states.
3. Specify components with existing token references and clear behaviour rules.
4. Record contrast, focus order, keyboard behavior, and responsive breakpoints.
5. Run an engineering review and resolve ambiguous interactions before approval.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `apply-design-tokens-to-a-ui`
- `create-a-visual-hierarchy`
- `create-a-wireframe-for-a-screen`

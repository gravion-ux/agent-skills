---
name: document-a-design-decision
description: Document a design decision with its context, alternatives, trade-offs, and consequences. Use when the user needs a durable record of why a product design choice was made.
domain: design-ux
tags: [design-decision, documentation, rationale, ux-decisions]
triggers: ["design decision record", "document a design decision", "record a ux design rationale"]
---

# Document a design decision with its context, alternatives, trade-offs, and consequences

## Purpose

Document a design decision with its context, alternatives, trade-offs, and consequences.

## When to use

Use when the user needs a durable record of why a product design choice was made.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Describe the user problem, constraints, and decision criteria.
2. State the chosen option and the alternatives considered.
3. Record the trade-offs, evidence, and expected consequences.
4. Identify review triggers, owners, and the next validation checkpoint.
5. Link the decision to affected flows, tokens, and implementation notes.

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
- `create-a-design-handoff-specification`
- `design-a-card-and-list-pattern`

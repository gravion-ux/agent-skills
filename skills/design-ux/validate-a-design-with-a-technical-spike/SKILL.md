---
name: validate-a-design-with-a-technical-spike
description: Validate a design with a focused technical spike that tests its riskiest assumption. Use when the user needs evidence that a proposed design is feasible before full implementation.
domain: design-ux
tags: [technical-spike, prototyping, feasibility, engineering-validation]
triggers: ["design technical spike", "validate a design with a technical spike", "run a design feasibility spike"]
---

# Validate a design with a focused technical spike that tests its riskiest assumption

## Purpose

Validate a design with a focused technical spike that tests its riskiest assumption.

## When to use

Use when the user needs evidence that a proposed design is feasible before full implementation.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. State the riskiest design assumption and the smallest test that can disprove it.
2. Define the platform constraints, success threshold, and timebox.
3. Build only the spike path needed to exercise the assumption.
4. Record results, limitations, and the recommended design adjustment.
5. Decide whether to proceed, revise, or run a follow-up spike.

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
- `choose-a-colour-system-with-contrast`
- `create-a-design-handoff-specification`

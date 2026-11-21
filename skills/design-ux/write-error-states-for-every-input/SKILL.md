---
name: write-error-states-for-every-input
description: Define precise error states for every input, including how each failure resolves. Use when the user needs field-level validation messages and recovery behavior.
domain: design-ux
tags: [error-states, validation, forms, accessibility]
triggers: ["input error states", "write error states for every input", "define form validation errors"]
---

# Define precise error states for every input, including how each failure resolves

## Purpose

Define precise error states for every input, including how each failure resolves.

## When to use

Use when the user needs field-level validation messages and recovery behavior.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Inventory each input, its format, limits, and failure modes.
2. Write one specific message for each actionable error.
3. Define where the message appears and which field receives focus.
4. Preserve valid entries and explain how to correct the error.
5. Check color, icon, and text communicate errors without relying on color alone.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `write-microcopy-for-an-error`
- `write-a-user-flow-for-a-feature`
- `write-microcopy-for-a-button`

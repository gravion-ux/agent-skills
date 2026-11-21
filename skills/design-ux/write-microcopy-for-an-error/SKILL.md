---
name: write-microcopy-for-an-error
description: Write error microcopy that states what failed, why, and how to recover. Use when the user needs clear corrective text for a failed interface action.
domain: design-ux
tags: [microcopy, error-copy, recovery-guidance, interface-writing]
triggers: ["error microcopy", "write microcopy for an error", "message a failed ui action"]
---

# Write error microcopy that states what failed, why, and how to recover

## Purpose

Write error microcopy that states what failed, why, and how to recover.

## When to use

Use when the user needs clear corrective text for a failed interface action.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Identify the user's failed goal and the actual system cause.
2. State the problem in plain language without blame or error codes.
3. Give one concrete recovery action and preserve the user's context.
4. Match the message severity to the impact and retry possibility.
5. Check the message beside the affected field or action for focus clarity.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `write-error-states-for-every-input`
- `write-microcopy-for-a-button`
- `design-a-navigation-model-for-an-app`

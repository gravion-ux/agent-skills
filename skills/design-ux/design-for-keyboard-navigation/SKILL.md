---
name: design-for-keyboard-navigation
description: Design a keyboard path with predictable focus order, visible focus, and useful shortcuts. Use when the user needs an interface to be fully operable without a pointer.
domain: design-ux
tags: [keyboard-navigation, focus-management, wcag, interaction-design]
triggers: ["keyboard navigation design", "design for keyboard navigation", "make a ui keyboard accessible"]
---

# Design a keyboard path with predictable focus order, visible focus, and useful shortcuts

## Purpose

Design a keyboard path with predictable focus order, visible focus, and useful shortcuts.

## When to use

Use when the user needs an interface to be fully operable without a pointer.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Map the logical reading and action order for every interactive region.
2. Define tab order, arrow-key movement, escape behavior, and focus return.
3. Specify a persistent high-contrast focus indicator for every control.
4. Define skip links and shortcuts without overriding browser or assistive behavior.
5. Test the primary task using only the keyboard and screen reader.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `design-a-navigation-model-for-an-app`
- `run-a-user-interview-for-a-design-question`
- `apply-design-tokens-to-a-ui`

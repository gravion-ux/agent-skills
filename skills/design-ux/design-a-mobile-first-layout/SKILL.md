---
name: design-a-mobile-first-layout
description: Design a mobile-first layout that prioritizes the primary task across small screens. Use when the user needs a responsive layout that works well on narrow touch screens.
domain: design-ux
tags: [mobile-first, responsive-design, touch-interface, layout]
triggers: ["mobile first layout", "design a mobile first layout", "create a responsive mobile layout"]
---

# Design a mobile-first layout that prioritizes the primary task across small screens

## Purpose

Design a mobile-first layout that prioritizes the primary task across small screens.

## When to use

Use when the user needs a responsive layout that works well on narrow touch screens.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Define the primary mobile task and its smallest useful content set.
2. Set spacing, type, and tap targets from the narrowest supported viewport.
3. Stack or progressively disclose secondary content without hiding core actions.
4. Add tablet and desktop enhancements as explicit breakpoint changes.
5. Check touch targets, reflow, zoom, and orientation changes.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `design-a-dashboard-layout`
- `apply-design-tokens-to-a-ui`
- `create-a-design-handoff-specification`

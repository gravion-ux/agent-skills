---
name: design-empty-and-loading-states
description: Design empty and loading states that explain what will appear and keep users oriented. Use when the user needs to define what a screen shows before, during, or without content.
domain: design-ux
tags: [empty-states, loading-states, feedback, content-states]
triggers: ["empty and loading states", "design empty states", "design loading states"]
---

# Design empty and loading states that explain what will appear and keep users oriented

## Purpose

Design empty and loading states that explain what will appear and keep users oriented.

## When to use

Use when the user needs to define what a screen shows before, during, or without content.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Classify each screen as loading, empty, partial, populated, or failed.
2. Write the empty-state purpose, next action, and explanatory copy.
3. Define skeleton, progress, and delayed-response feedback for loading states.
4. Specify partial-content and failure recovery for interrupted requests.
5. Verify that each state preserves navigation and accessible status updates.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `design-a-card-and-list-pattern`
- `design-a-search-and-filter-interface`
- `apply-design-tokens-to-a-ui`

---
name: design-a-notification-pattern
description: Design notifications that match urgency, deliver context, and avoid unnecessary interruption. Use when the user needs a consistent notification system for product events and user actions.
domain: design-ux
tags: [notifications, messaging, alert-design, user-preferences]
triggers: ["notification pattern", "design a notification pattern", "create a product notification system"]
---

# Design notifications that match urgency, deliver context, and avoid unnecessary interruption

## Purpose

Design notifications that match urgency, deliver context, and avoid unnecessary interruption.

## When to use

Use when the user needs a consistent notification system for product events and user actions.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Map each event to urgency, user relevance, and acceptable delivery channel.
2. Define the title, context, action, expiry, and deduplication rule.
3. Specify inbox, push, email, and in-product presentation differences.
4. Add grouping, muting, snoozing, and permission controls.
5. Check accessible announcement behavior and stale notification expiry.

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
- `apply-design-tokens-to-a-ui`
- `create-a-design-handoff-specification`

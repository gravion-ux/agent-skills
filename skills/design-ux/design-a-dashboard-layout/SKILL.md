---
name: design-a-dashboard-layout
description: Design a dashboard layout that prioritizes decisions, exceptions, and meaningful drill-downs. Use when the user needs a monitoring or analytics screen with multiple data regions.
domain: design-ux
tags: [dashboard, data-visualization, information-architecture, monitoring]
triggers: ["dashboard layout", "design a dashboard layout", "create an analytics dashboard layout"]
---

# Design a dashboard layout that prioritizes decisions, exceptions, and meaningful drill-downs

## Purpose

Design a dashboard layout that prioritizes decisions, exceptions, and meaningful drill-downs.

## When to use

Use when the user needs a monitoring or analytics screen with multiple data regions.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Map each audience goal to the decisions the dashboard must support.
2. Rank metrics by urgency, actionability, and frequency of use.
3. Define the grid, visual encoding, comparison period, and drill-down path.
4. Specify loading, partial-data, empty, and stale-data states.
5. Check that color alerts have labels and remain accessible.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `design-a-mobile-first-layout`
- `apply-design-tokens-to-a-ui`
- `create-a-design-handoff-specification`

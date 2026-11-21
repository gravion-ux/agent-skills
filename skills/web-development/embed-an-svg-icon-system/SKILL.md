---
name: embed-an-svg-icon-system
description: Embed a consistent SVG icon system with title text, sizing rules, and colour inheritance. Use when the user wants a set of vector icons embedded consistently across screens.
domain: web-development
tags: [svg, icons, component-system]
triggers: ["embed an svg icon system", "use svg icons across screens", "icon component library"]
---

# Embed a consistent SVG icon system with title text, sizing rules, and colour inheritance

## Purpose

Embed a consistent SVG icon system with title text, sizing rules, and colour inheritance.

## When to use

Use when the user wants a set of vector icons embedded consistently across screens.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Collect the icons the target screens use and assign one name to each.
2. Store each icon as a reusable component with explicit width and height.
3. Set decorative icons to be hidden from assistive technology and label meaningful ones.
4. Let icons inherit current colour and stroke width from their surrounding component.
5. Verify icons stay crisp at the smallest supported width and introduce no console errors.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-an-accessible-navigation-menu`
- `build-an-offline-first-web-app`
- `embed-a-video-player-responsively`

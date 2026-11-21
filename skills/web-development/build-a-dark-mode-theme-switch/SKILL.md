---
name: build-a-dark-mode-theme-switch
description: Build a dark mode switch that persists the chosen theme and respects the system colour preference. Use when the user wants a light and dark theme switch that survives page reloads.
domain: web-development
tags: [dark-mode, theming, accessibility]
triggers: ["dark mode theme switch", "add a light and dark theme toggle", "remember the chosen colour theme"]
---

# Build a dark mode switch that persists the chosen theme and respects the system colour preference

## Purpose

Build a dark mode switch that persists the chosen theme and respects the system colour preference.

## When to use

Use when the user wants a light and dark theme switch that survives page reloads.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Define theme tokens for light and dark values in the project's token layer.
2. Apply the system preference on first visit and the stored choice on later visits.
3. Toggle the theme attribute on the document root from the switch control.
4. Announce the active theme and keep the switch reachable by keyboard.
5. Recheck contrast in both themes and confirm the layout holds at the smallest supported width.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `add-dark-mode-to-a-site`
- `build-a-carousel-without-jank`
- `build-a-component-library`

---
name: build-an-accessible-navigation-menu
description: Build an accessible navigation menu with semantic controls, focus handling, and predictable keyboard behavior. Use when the user wants a website menu to be usable by keyboard and assistive technology.
domain: web-development
tags: [accessible-menu, focus-management, keyboard-navigation]
triggers: ["accessible web navigation menu", "build a keyboard-friendly navigation menu", "add accessible menu semantics to a site"]
---

# Build an accessible navigation menu with semantic controls, focus handling, and predictable keyboard behavior

## Purpose

Build an accessible navigation menu with semantic controls, focus handling, and predictable keyboard behavior.

## When to use

Use when the user wants a website menu to be usable by keyboard and assistive technology.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Use a navigation landmark and native links for the menu's primary destinations.
2. Give an expandable menu button an accessible name and an expanded state.
3. Support expected keys for opening, closing, and moving through menu items.
4. Return focus to the menu button when the expanded menu closes.
5. Test the full menu flow with a keyboard and an automated accessibility scan.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-a-dropdown-menu`
- `build-an-offline-first-web-app`
- `build-a-carousel-without-jank`

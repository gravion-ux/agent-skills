---
name: build-a-dropdown-menu
description: Build a dropdown menu with roving keyboard focus, correct expansion state, and menu semantics. Use when the user wants a dropdown menu that opens from a trigger and supports full keyboard use.
domain: web-development
tags: [dropdown, menu, keyboard-navigation]
triggers: ["build a dropdown menu", "dropdown with keyboard support", "accessible dropdown menu"]
---

# Build a dropdown menu with roving keyboard focus, correct expansion state, and menu semantics

## Purpose

Build a dropdown menu with roving keyboard focus, correct expansion state, and menu semantics.

## When to use

Use when the user wants a dropdown menu that opens from a trigger and supports full keyboard use.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Give the trigger an accessible name and bind the expanded state to aria-expanded.
2. Open the menu on activation and position it against the trigger element.
3. Move between menu items with the arrow keys and close on escape.
4. Close the menu when focus leaves or a menu item is selected.
5. Verify keyboard navigation reaches every item and that the build stays error-free.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-a-carousel-without-jank`
- `build-a-component-library`
- `build-a-dark-mode-theme-switch`

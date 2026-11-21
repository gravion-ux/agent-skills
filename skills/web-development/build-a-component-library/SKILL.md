---
name: build-a-component-library
description: Assemble a reusable, documented component library with typed props and consistent visual states. Use when the user wants a shared set of reusable interface components for a product.
domain: web-development
tags: [component-library, design-system, reuse]
triggers: ["build a component library", "create reusable ui components", "component library for our product"]
---

# Assemble a reusable, documented component library with typed props and consistent visual states

## Purpose

Assemble a reusable, documented component library with typed props and consistent visual states.

## When to use

Use when the user wants a shared set of reusable interface components for a product.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Inventory the repeated interface elements across the target screens.
2. Define each component's props, states, and accessibility behaviour in a written API table.
3. Implement the components in the project's chosen framework and rendering mode.
4. Add usage examples for the default, disabled, loading, and error states.
5. Run the build, lint, and keyboard navigation checks before publishing the library.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-a-tabs-component`
- `build-a-carousel-without-jank`
- `build-a-dark-mode-theme-switch`

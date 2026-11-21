---
name: manage-css-without-a-mess
description: Restructure scattered CSS into predictable layers, tokens, and modules without changing page behaviour. Use when the user wants an untidy frontend stylesheet to become easier to maintain.
domain: web-development
tags: [css-architecture, stylesheet-refactor, frontend-maintenance]
triggers: ["css architecture cleanup", "organize messy css stylesheets", "refactor a css codebase without duplication"]
---

# Restructure scattered CSS into predictable layers, tokens, and modules without changing page behaviour

## Purpose

Restructure scattered CSS into predictable layers, tokens, and modules without changing page behaviour.

## When to use

Use when the user wants an untidy frontend stylesheet to become easier to maintain.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Inventory selectors, utilities, component styles, and page-specific overrides.
2. Assign styles to reset, tokens, layout, components, and utilities by purpose.
3. Extract repeated declarations into tokens or a shared component rule.
4. Replace broad overrides with a scoped selector at the nearest owning component.
5. Run lint, build, and visual checks to confirm the cleanup preserved behaviour.

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
- `make-a-page-work-without-javascript`
- `manage-a-loading-skeleton`

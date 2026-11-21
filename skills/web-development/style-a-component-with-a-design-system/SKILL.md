---
name: style-a-component-with-a-design-system
description: Style a web component from design-system tokens so variants, states, and themes stay consistent. Use when the user wants a reusable web component to follow an existing design system.
domain: web-development
tags: [design-tokens, component-styling, design-system]
triggers: ["design system component styling", "style a web component from design tokens", "apply a component design system in css"]
---

# Style a web component from design-system tokens so variants, states, and themes stay consistent

## Purpose

Style a web component from design-system tokens so variants, states, and themes stay consistent.

## When to use

Use when the user wants a reusable web component to follow an existing design system.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Map each visual property in the component to an existing design token.
2. Implement the supported variants and interaction states with the component API.
3. Apply focus, disabled, loading, and error states without overriding token values.
4. Check text and component contrast against every supported theme.
5. Run the build and lint checks after removing one-off local styles.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-a-component-library`
- `build-a-form-with-inline-validation`
- `build-a-modal-dialog-with-focus-management`

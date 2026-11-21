---
name: build-a-modal-dialog-with-focus-management
description: Build an accessible modal dialog that traps focus, restores it on close, and reports errors. Use when the user wants a modal overlay that behaves correctly for keyboard and screen reader users.
domain: web-development
tags: [modal, focus-management, accessibility]
triggers: ["accessible modal dialog", "modal with focus trap", "build a dialog with focus management"]
---

# Build an accessible modal dialog that traps focus, restores it on close, and reports errors

## Purpose

Build an accessible modal dialog that traps focus, restores it on close, and reports errors.

## When to use

Use when the user wants a modal overlay that behaves correctly for keyboard and screen reader users.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Mark the overlay with the dialog role and reference its title and description.
2. Move focus into the dialog when it opens and cycle it within the panel.
3. Return focus to the invoking control when the dialog closes.
4. Close the dialog on the escape key and on backdrop activation.
5. Check that no console errors appear and that keyboard navigation stays inside the dialog.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-a-form-with-inline-validation`
- `build-a-search-box-with-debounced-results`
- `build-a-carousel-without-jank`

---
name: handle-a-form-with-server-actions
description: Handle a form with server actions, inline validation errors, and a protected resubmission path. Use when the user wants a form submitted through server actions with validation feedback.
domain: web-development
tags: [forms, server-actions, validation]
triggers: ["form with server actions", "submit a form to a server action", "server action form with errors"]
---

# Handle a form with server actions, inline validation errors, and a protected resubmission path

## Purpose

Handle a form with server actions, inline validation errors, and a protected resubmission path.

## When to use

Use when the user wants a form submitted through server actions with validation feedback.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Define the form fields, required rules, and the server action that receives them.
2. Validate the submitted values on the server and return field-level error messages.
3. Render the returned errors next to the matching fields with programmatic focus on failure.
4. Disable the submit control while the action is pending to block duplicate submissions.
5. Run the build and lint checks and confirm the page loads without console errors.

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
- `build-a-modal-dialog-with-focus-management`
- `build-a-search-box-with-debounced-results`

---
name: build-a-form-with-inline-validation
description: Add inline validation to a browser form with clear field errors and a submission summary. Use when the user wants a web form to explain invalid input before submission.
domain: web-development
tags: [form-validation, inline-errors, accessible-forms]
triggers: ["inline browser form validation", "build a form with inline validation messages", "validate a web form while the user types"]
---

# Add inline validation to a browser form with clear field errors and a submission summary

## Purpose

Add inline validation to a browser form with clear field errors and a submission summary.

## When to use

Use when the user wants a web form to explain invalid input before submission.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. State the purpose of every collected field before adding its input.
2. Use native input constraints as the baseline for required values and formats.
3. Validate a field after interaction and show its error beside the matching control.
4. Connect each error to its control with an identifier and an accessible description.
5. Summarize remaining errors after submission and verify keyboard navigation.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-a-modal-dialog-with-focus-management`
- `build-a-search-box-with-debounced-results`
- `handle-a-form-with-server-actions`

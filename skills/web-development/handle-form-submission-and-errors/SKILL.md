---
name: handle-form-submission-and-errors
description: Handle browser form submission states so pending, successful, and failed requests stay understandable. Use when the user wants a web form to report submission progress and failure clearly.
domain: web-development
tags: [form-submission, error-states, browser-forms]
triggers: ["web form submission errors", "handle a browser form submit failure", "show an error after form submission"]
---

# Handle browser form submission states so pending, successful, and failed requests stay understandable

## Purpose

Handle browser form submission states so pending, successful, and failed requests stay understandable.

## When to use

Use when the user wants a web form to report submission progress and failure clearly.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Validate the form before sending data and focus the first invalid control.
2. Disable the submit control while the request is pending and prevent duplicate sends.
3. Preserve safe user input after a server error without exposing credentials in the page.
4. Announce the success or error result in a live region with a recovery action.
5. Test a successful submission, a validation failure, and a network failure in the browser.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `handle-a-form-with-server-actions`
- `add-analytics-and-track-events`
- `build-a-form-with-inline-validation`

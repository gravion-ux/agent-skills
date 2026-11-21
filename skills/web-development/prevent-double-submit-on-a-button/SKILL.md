---
name: prevent-double-submit-on-a-button
description: Prevent double submissions by disabling the control during processing and rejecting repeat events. Use when the user wants a button that cannot be submitted twice while its action runs.
domain: web-development
tags: [forms, button, concurrency]
triggers: ["prevent double submit", "disable a button while submitting", "stop duplicate form submission"]
---

# Prevent double submissions by disabling the control during processing and rejecting repeat events

## Purpose

Prevent double submissions by disabling the control during processing and rejecting repeat events.

## When to use

Use when the user wants a button that cannot be submitted twice while its action runs.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Disable the button and mark it busy in the same update that starts the request.
2. Ignore repeat activation events while the request is pending.
3. Restore the button state in a finally branch for both success and failure.
4. Surface the request result near the control so the user sees what happened.
5. Verify with keyboard activation that only one request is sent per interaction.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `add-a-cookie-consent-banner`
- `add-a-service-worker-for-caching`
- `add-dark-mode-to-a-site`

---
name: handle-a-network-failure-gracefully
description: Handle a network failure with a clear error state, a retry action, and preserved user input. Use when the user wants a page that degrades gracefully when a request or asset fails to load.
domain: web-development
tags: [error-handling, network, resilience]
triggers: ["handle network failure", "graceful error state for a failed request", "retry when the request fails"]
---

# Handle a network failure with a clear error state, a retry action, and preserved user input

## Purpose

Handle a network failure with a clear error state, a retry action, and preserved user input.

## When to use

Use when the user wants a page that degrades gracefully when a request or asset fails to load.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Detect timeouts, offline status, and failed responses at the request boundary.
2. Replace the failed region with an error message that states what did not work.
3. Provide a retry action that repeats the same request without a full reload.
4. Keep form values and selected filters intact across the failure.
5. Log the failure with request context but no personal data or client secrets.

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
- `add-a-cookie-consent-banner`
- `add-a-service-worker-for-caching`

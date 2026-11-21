---
name: write-an-end-to-end-test-for-a-web-flow
description: Write an end-to-end test that drives a real browser through a complete user journey. Use when the user wants an end-to-end test covering a multi-step web flow.
domain: web-development
tags: [end-to-end, browser-testing, automation]
triggers: ["end to end web flow test", "browser test for a user journey", "write an e2e test for the checkout flow"]
---

# Write an end-to-end test that drives a real browser through a complete user journey

## Purpose

Write an end-to-end test that drives a real browser through a complete user journey.

## When to use

Use when the user wants an end-to-end test covering a multi-step web flow.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. List the user journey steps, the starting URL, and the final expected outcome.
2. Drive the flow through visible controls using accessible roles or labels.
3. Assert the resulting page content and the absence of console errors.
4. Capture a screenshot at the point where the flow is most likely to fail.
5. Run the test against the production build and record any timing-sensitive step.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `set-up-a-preview-deploy-for-a-web-app`
- `test-a-web-component-in-isolation`
- `add-a-service-worker-for-caching`

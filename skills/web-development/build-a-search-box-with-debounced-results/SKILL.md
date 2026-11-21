---
name: build-a-search-box-with-debounced-results
description: Build a search box that debounces requests, cancels stale responses, and announces result updates. Use when the user wants a website search field to avoid a request for every keystroke.
domain: web-development
tags: [search-ui, request-debounce, async-results]
triggers: ["debounced browser search box", "build a search box with debounced web results", "cancel stale browser search requests"]
---

# Build a search box that debounces requests, cancels stale responses, and announces result updates

## Purpose

Build a search box that debounces requests, cancels stale responses, and announces result updates.

## When to use

Use when the user wants a website search field to avoid a request for every keystroke.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Give the input a visible label and define the minimum characters before searching.
2. Wait for the configured debounce interval after the latest input event.
3. Abort the previous request and ignore any response that no longer matches the query.
4. Render a busy state and announce result counts or the empty state accessibly.
5. Test rapid typing, slow responses, empty results, and keyboard submission in the browser.

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
- `build-a-carousel-without-jank`

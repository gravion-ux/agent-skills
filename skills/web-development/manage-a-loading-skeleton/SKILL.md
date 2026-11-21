---
name: manage-a-loading-skeleton
description: Manage a loading skeleton that mirrors the final layout and disappears when data arrives. Use when the user wants a loading placeholder for content that is fetched asynchronously.
domain: web-development
tags: [loading-state, skeleton, performance]
triggers: ["loading skeleton placeholder", "show a skeleton while data loads", "manage loading placeholders"]
---

# Manage a loading skeleton that mirrors the final layout and disappears when data arrives

## Purpose

Manage a loading skeleton that mirrors the final layout and disappears when data arrives.

## When to use

Use when the user wants a loading placeholder for content that is fetched asynchronously.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Match the skeleton structure to the layout of the content it replaces.
2. Start the skeleton when the request begins and remove it once rendering completes.
3. Keep the skeleton below the fold from delaying the first meaningful paint.
4. Replace the skeleton with an error message when the request fails.
5. Check the placeholder does not shift the layout at the smallest supported width.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `manage-css-without-a-mess`
- `add-a-cookie-consent-banner`
- `add-a-service-worker-for-caching`

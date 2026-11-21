---
name: fetch-and-cache-data-in-a-browser
description: Cache browser-fetched data with explicit freshness, revalidation, and failure behavior. Use when the user wants a web client to reuse fetched data without showing stale or broken results.
domain: web-development
tags: [browser-cache, data-fetching, revalidation]
triggers: ["browser data caching", "cache fetched web data in the browser", "add stale-while-revalidate browser caching"]
---

# Cache browser-fetched data with explicit freshness, revalidation, and failure behavior

## Purpose

Cache browser-fetched data with explicit freshness, revalidation, and failure behavior.

## When to use

Use when the user wants a web client to reuse fetched data without showing stale or broken results.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Classify each request as cacheable, conditional, or sensitive to personal data.
2. Apply the server cache headers instead of inventing a separate expiry policy.
3. Store cache keys that exclude credentials and unnecessary personal information.
4. Revalidate stale entries in the background and replace them atomically.
5. Test cache hits, expiry, revalidation, and offline failure with the console open.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `render-a-chart-in-the-browser`
- `debug-a-cross-browser-layout-bug`
- `render-a-table-with-sorting-and-pagination`

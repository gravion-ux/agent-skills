---
name: lazy-load-below-the-fold-images
description: Lazy-load below-the-fold images while preserving dimensions and avoiding delays to primary content. Use when the user wants a webpage to defer images that appear below the initial viewport.
domain: web-development
tags: [lazy-loading, image-performance, layout-stability]
triggers: ["lazy-loaded below-fold images", "defer below-the-fold web images", "implement lazy image loading in the browser"]
---

# Lazy-load below-the-fold images while preserving dimensions and avoiding delays to primary content

## Purpose

Lazy-load below-the-fold images while preserving dimensions and avoiding delays to primary content.

## When to use

Use when the user wants a webpage to defer images that appear below the initial viewport.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Identify the primary above-the-fold image and exclude it from lazy loading.
2. Add native lazy loading to eligible images with explicit width and height values.
3. Use an intersection observer only when native support does not meet the browser target.
4. Preserve a meaningful fallback source for environments without lazy loading.
5. Compare page loading and layout shift before and after the change.

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
- `add-a-cookie-consent-banner`
- `add-a-service-worker-for-caching`

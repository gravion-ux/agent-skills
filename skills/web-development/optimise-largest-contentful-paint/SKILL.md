---
name: optimise-largest-contentful-paint
description: Improve largest contentful paint by measuring the real bottleneck and changing the critical render path. Use when the user wants a web page's largest visible content to render faster.
domain: web-development
tags: [lcp, render-performance, web-performance]
triggers: ["largest contentful paint optimization", "improve the lcp element on a web page", "speed up a page's largest contentful paint"]
---

# Improve largest contentful paint by measuring the real bottleneck and changing the critical render path

## Purpose

Improve largest contentful paint by measuring the real bottleneck and changing the critical render path.

## When to use

Use when the user wants a web page's largest visible content to render faster.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Record the largest contentful paint element and timing in a production-like profile.
2. Determine whether the delay comes from network, server, font, image, or render blocking.
3. Preload only the measured critical asset and give images explicit dimensions.
4. Remove render-blocking work or defer noncritical scripts from the critical path.
5. Compare repeated before-and-after traces and run the build and lint checks.

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
- `add-analytics-and-track-events`

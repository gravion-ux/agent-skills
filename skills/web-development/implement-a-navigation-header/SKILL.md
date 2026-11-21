---
name: implement-a-navigation-header
description: Build a site navigation header that exposes clear links, current-page state, and responsive placement. Use when the user wants a consistent navigation header across a website.
domain: web-development
tags: [site-header, site-navigation, responsive-ui]
triggers: ["web navigation header", "build a responsive site header", "implement a web header navigation"]
---

# Build a site navigation header that exposes clear links, current-page state, and responsive placement

## Purpose

Build a site navigation header that exposes clear links, current-page state, and responsive placement.

## When to use

Use when the user wants a consistent navigation header across a website.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Identify the primary routes and mark the current route with an accessible active state.
2. Add a labelled navigation landmark with links that work without custom JavaScript.
3. Place the site identity and actions in a stable header arrangement.
4. Move secondary links into a narrow-screen pattern without hiding keyboard focus.
5. Verify the header at desktop and mobile widths with no console errors.

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

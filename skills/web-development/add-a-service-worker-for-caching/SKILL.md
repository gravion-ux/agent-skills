---
name: add-a-service-worker-for-caching
description: Add a service worker that caches static assets with a versioned strategy and a safe fallback. Use when the user wants a service worker to cache front-end assets for repeat visits.
domain: web-development
tags: [service-worker, caching, offline-first]
triggers: ["service worker caching", "cache front end assets offline", "add a service worker to the app"]
---

# Add a service worker that caches static assets with a versioned strategy and a safe fallback

## Purpose

Add a service worker that caches static assets with a versioned strategy and a safe fallback.

## When to use

Use when the user wants a service worker to cache front-end assets for repeat visits.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Generate a cache name that changes with each deployed asset version.
2. Cache the app shell and hashed assets during the install step.
3. Serve cached assets first and refresh the cache in the background.
4. Return a cached fallback page when an offline navigation request fails.
5. Remove outdated caches during activation and verify the app loads without console errors.

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
- `add-dark-mode-to-a-site`
- `add-internationalisation-to-a-site`

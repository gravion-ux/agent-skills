---
name: build-an-offline-first-web-app
description: Build an offline-first web app that stores a working dataset locally and reconciles later. Use when the user wants a web app that remains usable without a network connection.
domain: web-development
tags: [offline-first, local-storage, sync]
triggers: ["offline first web app", "app that works without internet", "cache data for offline use"]
---

# Build an offline-first web app that stores a working dataset locally and reconciles later

## Purpose

Build an offline-first web app that stores a working dataset locally and reconciles later.

## When to use

Use when the user wants a web app that remains usable without a network connection.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Choose the local storage layer and define the records the app must cache.
2. Read from the local store first and refresh it from the network in the background.
3. Queue local changes with timestamps and replay them when connectivity returns.
4. Show the freshness of the data and mark unsynced records in the interface.
5. Test the offline path by disabling the network and confirm no console errors appear.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-an-accessible-navigation-menu`
- `set-up-a-preview-deploy-for-a-web-app`
- `write-an-end-to-end-test-for-a-web-flow`

---
name: build-a-toast-notification
description: Build a toast notification stack that announces messages, expires them, and respects motion settings. Use when the user wants transient success, warning, or error messages shown over the interface.
domain: web-development
tags: [toast, notifications, feedback]
triggers: ["toast notification stack", "show a transient toast message", "build toast notifications"]
---

# Build a toast notification stack that announces messages, expires them, and respects motion settings

## Purpose

Build a toast notification stack that announces messages, expires them, and respects motion settings.

## When to use

Use when the user wants transient success, warning, or error messages shown over the interface.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Define the toast types, dismissal timeout, and retry behaviour for each type.
2. Render the stack in a landmark region that announces new messages politely.
3. Expose a dismiss control in each toast and clear timers on hover or focus.
4. Suppress entrance animation when the user prefers reduced motion.
5. Check the stack does not overlap controls at the smallest supported width.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-a-carousel-without-jank`
- `build-a-component-library`
- `build-a-dark-mode-theme-switch`

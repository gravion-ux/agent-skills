---
name: build-a-carousel-without-jank
description: Build a carousel that advances smoothly, pauses on interaction, and stays within layout shift limits. Use when the user wants an image or card carousel that scrolls smoothly on constrained devices.
domain: web-development
tags: [carousel, animation, performance]
triggers: ["smooth carousel slides", "carousel without layout jank", "build a jank-free carousel"]
---

# Build a carousel that advances smoothly, pauses on interaction, and stays within layout shift limits

## Purpose

Build a carousel that advances smoothly, pauses on interaction, and stays within layout shift limits.

## When to use

Use when the user wants an image or card carousel that scrolls smoothly on constrained devices.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Reserve fixed space for each slide to prevent layout shift during rotation.
2. Animate slide transitions with transforms instead of changing slide dimensions.
3. Pause automatic advance while the carousel has focus or hover.
4. Expose previous and next controls that announce the current slide.
5. Measure frame timing during rotation and confirm the page builds without console errors.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-a-component-library`
- `build-a-dark-mode-theme-switch`
- `build-a-dropdown-menu`

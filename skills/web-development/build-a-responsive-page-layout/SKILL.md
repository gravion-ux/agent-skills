---
name: build-a-responsive-page-layout
description: Build a responsive page layout that reflows cleanly from the smallest supported width to desktop. Use when the user wants a web page to adapt across supported viewport widths.
domain: web-development
tags: [responsive-layout, css-grid, frontend-ui]
triggers: ["responsive web page layout", "build a breakpoint-based web layout", "make a web page adapt to mobile widths"]
---

# Build a responsive page layout that reflows cleanly from the smallest supported width to desktop

## Purpose

Build a responsive page layout that reflows cleanly from the smallest supported width to desktop.

## When to use

Use when the user wants a web page to adapt across supported viewport widths.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Choose the smallest supported width and breakpoint values from the target devices.
2. Map the page content into semantic header, main, and footer regions.
3. Implement fluid sizing with CSS grid or flexbox instead of fixed-width wrappers.
4. Verify the layout at the smallest width and at one desktop viewport.
5. Run the build, lint checks, and keyboard navigation pass before handoff.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `audit-a-page-for-accessibility`
- `build-a-carousel-without-jank`
- `build-a-component-library`

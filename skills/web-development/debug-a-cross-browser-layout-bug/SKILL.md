---
name: debug-a-cross-browser-layout-bug
description: Debug a cross-browser layout defect by reproducing it, isolating the CSS cause, and preventing regressions. Use when the user has a web layout that differs or breaks in one supported browser.
domain: web-development
tags: [cross-browser, layout-debugging, css-cascade]
triggers: ["cross-browser layout debugging", "debug a browser layout mismatch", "fix css that breaks in one browser"]
---

# Debug a cross-browser layout defect by reproducing it, isolating the CSS cause, and preventing regressions

## Purpose

Debug a cross-browser layout defect by reproducing it, isolating the CSS cause, and preventing regressions.

## When to use

Use when the user has a web layout that differs or breaks in one supported browser.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Reproduce the defect in every supported browser and record the exact viewport and input.
2. Compare computed styles, box dimensions, and the first divergent cascade rule.
3. Check standards-based sizing, overflow, and form-control differences before applying a fix.
4. Replace the workaround with the narrowest standards-compliant CSS correction.
5. Add a regression case and verify the layout, console, and keyboard flow in all browsers.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-a-responsive-page-layout`
- `fetch-and-cache-data-in-a-browser`
- `render-a-chart-in-the-browser`

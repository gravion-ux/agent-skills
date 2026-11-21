---
name: make-a-page-work-without-javascript
description: Make a web flow work without JavaScript by preserving server-rendered content and progressive enhancement. Use when the user wants a webpage to remain usable when scripts are unavailable.
domain: web-development
tags: [progressive-enhancement, no-javascript, server-rendering]
triggers: ["javascript-free web page", "make a webpage work without javascript", "add progressive enhancement to a web flow"]
---

# Make a web flow work without JavaScript by preserving server-rendered content and progressive enhancement

## Purpose

Make a web flow work without JavaScript by preserving server-rendered content and progressive enhancement.

## When to use

Use when the user wants a webpage to remain usable when scripts are unavailable.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Render essential content, links, and form controls in the server response.
2. Give forms valid action and method attributes for a non-script submission path.
3. Add JavaScript as an enhancement without removing the server-rendered baseline.
4. Provide a clear alternative when an enhanced interaction cannot run.
5. Disable JavaScript in the browser and verify every essential task still completes.

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
- `build-a-responsive-page-layout`

---
name: run-a-web-bundle-analysis
description: Run a bundle analysis that identifies the largest dependencies and the assets driving page weight. Use when the user wants to understand why a front-end bundle is large and trim it.
domain: web-development
tags: [bundle-analysis, performance, optimization]
triggers: ["analyse the web bundle", "why is our javascript bundle large", "bundle size report"]
---

# Run a bundle analysis that identifies the largest dependencies and the assets driving page weight

## Purpose

Run a bundle analysis that identifies the largest dependencies and the assets driving page weight.

## When to use

Use when the user wants to understand why a front-end bundle is large and trim it.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Build the application with source maps and bundle statistics enabled.
2. Record the total transferred size of each entry chunk and its dependencies.
3. Rank the largest modules and separate vendor code from first-party code.
4. Check for duplicated libraries, oversized images, and fonts loaded eagerly.
5. Report the savings from each proposed removal and confirm the build still passes lint.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `set-up-a-preview-deploy-for-a-web-app`
- `test-a-web-component-in-isolation`
- `write-an-end-to-end-test-for-a-web-flow`

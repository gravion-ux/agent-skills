---
name: reduce-javascript-bundle-size
description: Reduce a frontend JavaScript bundle by locating heavy modules and deferring noncritical code. Use when the user wants a website's JavaScript download or parse cost reduced.
domain: web-development
tags: [bundle-size, code-splitting, frontend-performance]
triggers: ["javascript bundle size reduction", "shrink a frontend javascript bundle", "split a large web javascript chunk"]
---

# Reduce a frontend JavaScript bundle by locating heavy modules and deferring noncritical code

## Purpose

Reduce a frontend JavaScript bundle by locating heavy modules and deferring noncritical code.

## When to use

Use when the user wants a website's JavaScript download or parse cost reduced.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Generate a production bundle report and rank modules by transferred size.
2. Remove unused exports and replace duplicate dependencies with the installed package.
3. Split route-level code into chunks that load only when their route opens.
4. Defer widgets and integrations that are not required for the first interaction.
5. Compare compressed bundle totals and verify each changed route without console errors.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `make-a-page-work-without-javascript`
- `run-a-web-bundle-analysis`
- `add-a-cookie-consent-banner`

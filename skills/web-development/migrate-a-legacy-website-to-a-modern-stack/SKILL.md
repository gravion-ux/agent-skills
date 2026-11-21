---
name: migrate-a-legacy-website-to-a-modern-stack
description: Migrate a legacy website to a modern stack while preserving routes, URLs, and search visibility. Use when the user wants a legacy site rebuilt on a current framework without losing traffic.
domain: web-development
tags: [migration, legacy-website, seo]
triggers: ["migrate a legacy website", "rebuild an old site on a modern stack", "move a legacy site to a new framework"]
---

# Migrate a legacy website to a modern stack while preserving routes, URLs, and search visibility

## Purpose

Migrate a legacy website to a modern stack while preserving routes, URLs, and search visibility.

## When to use

Use when the user wants a legacy site rebuilt on a current framework without losing traffic.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Inventory the existing routes, page templates, and indexed URLs.
2. Map legacy templates to modern components and identify behaviour that must be preserved.
3. Set up redirects from every retired URL to its closest equivalent.
4. Carry over metadata, structured data, and analytics tags page by page.
5. Compare rendered output and crawl results before switching the domain to the new stack.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `migrate-a-site-to-a-modern-framework`
- `add-dark-mode-to-a-site`
- `add-internationalisation-to-a-site`

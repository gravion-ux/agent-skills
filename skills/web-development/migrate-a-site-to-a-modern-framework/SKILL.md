---
name: migrate-a-site-to-a-modern-framework
description: Migrate a legacy website to a modern framework while preserving routes, assets, and behaviour. Use when the user wants an existing website moved to a modern frontend framework.
domain: web-development
tags: [framework-migration, legacy-website, route-parity]
triggers: ["modern web framework migration", "migrate a website to a modern frontend framework", "move a legacy site to a component framework"]
---

# Migrate a legacy website to a modern framework while preserving routes, assets, and behaviour

## Purpose

Migrate a legacy website to a modern framework while preserving routes, assets, and behaviour.

## When to use

Use when the user wants an existing website moved to a modern frontend framework.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Inventory routes, page templates, assets, forms, metadata, and existing analytics events.
2. Choose a migration boundary and define a rollback path before changing production code.
3. Port templates into framework components while preserving URLs and server capabilities.
4. Move secrets to server-only configuration and keep them out of client bundles.
5. Compare route parity and redirects, then run build, lint, link, and accessibility checks.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `migrate-a-legacy-website-to-a-modern-stack`
- `add-dark-mode-to-a-site`
- `add-internationalisation-to-a-site`

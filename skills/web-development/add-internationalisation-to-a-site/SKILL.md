---
name: add-internationalisation-to-a-site
description: Internationalise a website with locale-specific copy, formatting, fallbacks, and right-to-left support. Use when the user wants a website to support more than one language or locale.
domain: web-development
tags: [internationalisation, locale-formatting, translation]
triggers: ["internationalised web interface", "add multiple languages to a website", "format a web app for different locales"]
---

# Internationalise a website with locale-specific copy, formatting, fallbacks, and right-to-left support

## Purpose

Internationalise a website with locale-specific copy, formatting, fallbacks, and right-to-left support.

## When to use

Use when the user wants a website to support more than one language or locale.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Choose the supported locales and extract visible copy into locale message files.
2. Replace hard-coded dates, numbers, currencies, and names with locale-aware formatters.
3. Set a default locale and an explicit fallback for missing translations.
4. Apply logical spacing and directional styles for right-to-left locales.
5. Switch locales at runtime and verify translated layouts, dates, and keyboard behavior.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `add-dark-mode-to-a-site`
- `migrate-a-site-to-a-modern-framework`
- `add-a-cookie-consent-banner`

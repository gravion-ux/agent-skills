---
name: add-dark-mode-to-a-site
description: Apply a site-wide dark theme with system preference support, consistent tokens, and readable contrast. Use when the user wants an existing website to support a dark appearance.
domain: web-development
tags: [dark-theme, color-tokens, site-theming]
triggers: ["system dark mode for a website", "apply dark theme tokens across a site", "support prefers-color-scheme on a website"]
---

# Apply a site-wide dark theme with system preference support, consistent tokens, and readable contrast

## Purpose

Apply a site-wide dark theme with system preference support, consistent tokens, and readable contrast.

## When to use

Use when the user wants an existing website to support a dark appearance.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Map current color values to semantic light and dark theme tokens.
2. Apply the system color preference at the document level without flashing light colors.
3. Update form controls, images, charts, and shadows for the dark theme.
4. Check text, border, and focus contrast against every themed surface.
5. Verify both themes at the smallest supported width with no console errors.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `add-internationalisation-to-a-site`
- `build-a-dark-mode-theme-switch`
- `migrate-a-site-to-a-modern-framework`

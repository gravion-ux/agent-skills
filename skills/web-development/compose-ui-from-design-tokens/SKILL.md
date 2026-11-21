---
name: compose-ui-from-design-tokens
description: Compose interface screens from design tokens so spacing, colour, and typography stay consistent. Use when the user wants a screen assembled from an existing design token set.
domain: web-development
tags: [design-tokens, theming, styling]
triggers: ["compose ui from design tokens", "apply design tokens to a page", "build a screen with our tokens"]
---

# Compose interface screens from design tokens so spacing, colour, and typography stay consistent

## Purpose

Compose interface screens from design tokens so spacing, colour, and typography stay consistent.

## When to use

Use when the user wants a screen assembled from an existing design token set.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Map the target screen's elements to named spacing, colour, and typography tokens.
2. Apply tokens as the only source of spacing, colour, and type values.
3. Replace hard-coded values with token references in the component styles.
4. Check contrast and focus-ring visibility against the token palette.
5. Run the build and lint checks and confirm the layout holds at the smallest supported width.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `publish-a-static-site-from-a-source-folder`
- `style-a-component-with-a-design-system`
- `add-a-cookie-consent-banner`

---
name: choose-a-type-scale
description: Choose a type scale that supports hierarchy, readable body copy, and dense interfaces. Use when the user needs a consistent set of type sizes for a product interface.
domain: design-ux
tags: [type-scale, typography, readability, design-tokens]
triggers: ["type scale for a ui", "choose a type scale", "set ui typography sizes"]
---

# Choose a type scale that supports hierarchy, readable body copy, and dense interfaces

## Purpose

Choose a type scale that supports hierarchy, readable body copy, and dense interfaces.

## When to use

Use when the user needs a consistent set of type sizes for a product interface.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Define the base body size, line height, and maximum measure for each platform.
2. Create a small scale for headings, labels, body copy, and supporting text.
3. Map each scale step to its intended content role rather than decoration.
4. Check truncation, zoom, localization, and long-word behavior.
5. Document the token names and contrast requirements for each role.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `choose-a-colour-system-with-contrast`
- `apply-design-tokens-to-a-ui`
- `build-a-clickable-prototype`

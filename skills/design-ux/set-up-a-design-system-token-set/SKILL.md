---
name: set-up-a-design-system-token-set
description: Set up a design token set that names reusable visual and spacing decisions. Use when the user needs a shared foundation for consistent design and implementation.
domain: design-ux
tags: [design-tokens, design-system, foundations, naming]
triggers: ["design system token set", "set up design tokens", "create a design token set"]
---

# Set up a design token set that names reusable visual and spacing decisions

## Purpose

Set up a design token set that names reusable visual and spacing decisions.

## When to use

Use when the user needs a shared foundation for consistent design and implementation.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Audit existing colors, typography, spacing, radii, and elevation values.
2. Define semantic token names for purpose rather than raw appearance.
3. Assign primitive values and map each semantic token to one primitive.
4. Document fallback values, platform variants, and ownership.
5. Validate the set against current screens for missing or conflicting tokens.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `apply-design-tokens-to-a-ui`
- `choose-a-colour-system-with-contrast`
- `create-a-design-handoff-specification`

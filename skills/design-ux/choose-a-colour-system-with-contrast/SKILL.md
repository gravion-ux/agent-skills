---
name: choose-a-colour-system-with-contrast
description: Choose a colour system with semantic roles and contrast-safe foreground pairs. Use when the user needs a product palette that supports states and remains accessible.
domain: design-ux
tags: [colour-system, contrast, accessibility, design-tokens]
triggers: ["accessible colour system", "choose a colour system with contrast", "design an accessible product palette"]
---

# Choose a colour system with semantic roles and contrast-safe foreground pairs

## Purpose

Choose a colour system with semantic roles and contrast-safe foreground pairs.

## When to use

Use when the user needs a product palette that supports states and remains accessible.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Map each colour to a semantic role such as surface, text, border, or action.
2. Test every normal and state pair against the target contrast level.
3. Specify hover, focus, selected, disabled, and error treatments without colour alone.
4. Check both light and dark backgrounds before approving semantic tokens.
5. Document palette tokens and any colour-independent state indicators.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `choose-a-type-scale`
- `set-up-a-design-system-token-set`
- `validate-a-design-with-a-technical-spike`

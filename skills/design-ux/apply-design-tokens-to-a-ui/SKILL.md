---
name: apply-design-tokens-to-a-ui
description: Apply existing design tokens to a UI without introducing parallel visual values. Use when the user needs to migrate an interface to consistent shared design tokens.
domain: design-ux
tags: [design-tokens, ui-migration, consistency, design-system]
triggers: ["design token ui migration", "apply design tokens to a ui", "migrate a ui to design tokens"]
---

# Apply existing design tokens to a UI without introducing parallel visual values

## Purpose

Apply existing design tokens to a UI without introducing parallel visual values.

## When to use

Use when the user needs to migrate an interface to consistent shared design tokens.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Map each hard-coded value to an existing semantic token.
2. Replace component-specific values with the shared token references.
3. Request missing tokens from the design-system owner instead of inventing them.
4. Check spacing, states, and responsive breakpoints for token consistency.
5. Compare the migrated UI with the reference screens and record visual differences.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `create-a-design-handoff-specification`
- `design-a-card-and-list-pattern`
- `design-a-dark-mode-variant`

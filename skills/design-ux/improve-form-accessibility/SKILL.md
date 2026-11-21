---
name: improve-form-accessibility
description: Improve a form's accessible labels, validation, focus behavior, and completion support. Use when the user needs to make an existing form usable with assistive technology.
domain: design-ux
tags: [form-accessibility, wcag, screen-reader, keyboard-navigation]
triggers: ["form accessibility audit", "improve form accessibility", "make a form screen reader accessible"]
---

# Improve a form's accessible labels, validation, focus behavior, and completion support

## Purpose

Improve a form's accessible labels, validation, focus behavior, and completion support.

## When to use

Use when the user needs to make an existing form usable with assistive technology.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Associate each control with a persistent visible or accessible label.
2. Group related controls with fieldsets and descriptive legends.
3. Expose required state, instructions, and errors programmatically.
4. Move focus to the first invalid field and back to the summary after correction.
5. Test keyboard operation, screen reader names, zoom, and error recovery.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `design-a-form-that-converts`
- `analyse-usability-test-results`
- `apply-design-tokens-to-a-ui`

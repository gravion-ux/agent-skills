---
name: design-an-error-recovery-flow
description: Design an error recovery flow that preserves work and offers a clear next step. Use when the user needs a recoverable journey for a failed or interrupted task.
domain: design-ux
tags: [error-recovery, resilience, workflow, accessibility]
triggers: ["error recovery flow", "design an error recovery flow", "recover a failed user task"]
---

# Design an error recovery flow that preserves work and offers a clear next step

## Purpose

Design an error recovery flow that preserves work and offers a clear next step.

## When to use

Use when the user needs a recoverable journey for a failed or interrupted task.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Identify the failed action, retained data, and possible causes.
2. Place a plain-language notice near the task with a clear recovery action.
3. Offer retry, alternate route, or support based on the likely failure.
4. Prevent duplicate submission while preserving progress.
5. Test recovery with keyboard, screen reader, and slow-network conditions.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `design-an-onboarding-flow`
- `design-a-navigation-model-for-an-app`
- `design-an-upgrade-prompt`

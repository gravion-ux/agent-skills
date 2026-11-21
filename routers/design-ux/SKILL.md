---
name: router-design-ux
description: Route work in the Design and UX domain to the right leaf skill. Use when a task clearly belongs to design-ux.
domain: design-ux
tags: [router, routing, design-ux]
triggers: ["route a design-ux task", "which design-ux skill should I use"]
---

# Design and UX router

## Purpose

List every leaf skill in the design-ux domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside design-ux and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `analyse-usability-test-results` | Use when the user needs to prioritize evidence from completed usability sessions. |
| `apply-design-tokens-to-a-ui` | Use when the user needs to migrate an interface to consistent shared design tokens. |
| `build-a-clickable-prototype` | Use when the user needs to validate interaction behavior before engineering implementation. |
| `choose-a-colour-system-with-contrast` | Use when the user needs a product palette that supports states and remains accessible. |
| `choose-a-type-scale` | Use when the user needs a consistent set of type sizes for a product interface. |
| `create-a-design-handoff-specification` | Use when the user needs to prepare a design for implementation and quality review. |
| `create-a-visual-hierarchy` | Use when the user needs to clarify emphasis and reading order on a screen. |
| `create-a-wireframe-for-a-screen` | Use when the user needs to validate a screen layout before detailed visual design. |
| `design-a-card-and-list-pattern` | Use when the user needs a consistent component for browsing repeated content items. |
| `design-a-dark-mode-variant` | Use when the user needs to adapt an existing visual system to dark appearance. |
| `design-a-dashboard-layout` | Use when the user needs a monitoring or analytics screen with multiple data regions. |
| `design-a-form-that-converts` | Use when the user wants a form design that improves completion without deceptive pressure. |
| `design-a-mobile-first-layout` | Use when the user needs a responsive layout that works well on narrow touch screens. |
| `design-a-navigation-model-for-an-app` | Use when the user needs to structure navigation for a multi-section application. |
| `design-a-notification-pattern` | Use when the user needs a consistent notification system for product events and user actions. |
| `design-a-search-and-filter-interface` | Use when the user needs to find, refine, and understand results in a large collection. |
| `design-an-error-recovery-flow` | Use when the user needs a recoverable journey for a failed or interrupted task. |
| `design-an-onboarding-flow` | Use when the user needs a first-run journey that creates value before asking for commitment. |
| `design-an-upgrade-prompt` | Use when the user needs to prompt users at a meaningful product limit or feature boundary. |
| `design-empty-and-loading-states` | Use when the user needs to define what a screen shows before, during, or without content. |
| `design-for-keyboard-navigation` | Use when the user needs an interface to be fully operable without a pointer. |
| `document-a-design-decision` | Use when the user needs a durable record of why a product design choice was made. |
| `improve-form-accessibility` | Use when the user needs to make an existing form usable with assistive technology. |
| `prioritise-design-feedback-by-impact` | Use when the user needs to decide which design feedback to address first. |
| `run-a-heuristic-review-of-a-screen` | Use when the user wants an expert critique of an existing interface. |
| `run-a-usability-test-session` | Use when the user is moderating a live usability test of a product or prototype. |
| `run-a-user-interview-for-a-design-question` | Use when the user needs evidence to answer a specific design question. |
| `set-up-a-design-system-token-set` | Use when the user needs a shared foundation for consistent design and implementation. |
| `validate-a-design-with-a-technical-spike` | Use when the user needs evidence that a proposed design is feasible before full implementation. |
| `write-a-usability-test-script` | Use when the user needs a consistent script for evaluating a prototype or product flow. |
| `write-a-user-flow-for-a-feature` | Use when the user needs an end-to-end flow for a feature before design or build. |
| `write-error-states-for-every-input` | Use when the user needs field-level validation messages and recovery behavior. |
| `write-microcopy-for-a-button` | Use when the user needs concise labels for a specific interface action. |
| `write-microcopy-for-an-error` | Use when the user needs clear corrective text for a failed interface action. |

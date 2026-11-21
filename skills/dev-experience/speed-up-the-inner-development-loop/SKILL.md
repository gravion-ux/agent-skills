---
name: speed-up-the-inner-development-loop
description: Shorten the edit-to-feedback cycle by profiling and removing delays from the local build path. Use when the user experiences slow feedback while editing code in the repository.
domain: dev-experience
tags: [inner-loop, developer-feedback, performance]
triggers: ["speed up the inner development loop", "make local feedback faster", "reduce edit to feedback time"]
---

# Shorten the edit-to-feedback cycle by profiling and removing delays from the local build path

## Purpose

Shorten the edit-to-feedback cycle by profiling and removing delays from the local build path.

## When to use

Use when the user experiences slow feedback while editing code in the repository.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Time the edit, build, test, and refresh stages during one normal change.
2. Identify the slowest stage and the command that causes the delay.
3. Prototype the smallest change that shortens that stage.
4. Compare before-and-after timings using the same representative change.
5. Document the faster command and keep it on the normal developer path.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `set-up-a-local-development-environment`
- `clean-up-stale-preview-environments`
- `add-a-health-check-endpoint`

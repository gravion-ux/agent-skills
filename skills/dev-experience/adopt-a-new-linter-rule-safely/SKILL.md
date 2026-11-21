---
name: adopt-a-new-linter-rule-safely
description: Adopt a new linter rule through scoped detection, baseline comparison, and staged enforcement. Use when the user wants to enable a lint rule without disrupting unrelated development work.
domain: dev-experience
tags: [lint-rule, static-analysis, safe-rollout]
triggers: ["adopt a new linter rule safely", "enable a lint rule gradually", "introduce a new lint check"]
---

# Adopt a new linter rule through scoped detection, baseline comparison, and staged enforcement

## Purpose

Adopt a new linter rule through scoped detection, baseline comparison, and staged enforcement.

## When to use

Use when the user wants to enable a lint rule without disrupting unrelated development work.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Run the proposed rule in report-only mode and record its finding count.
2. Classify legitimate exceptions, new violations, and pre-existing violations.
3. Fix new violations and add narrowly scoped suppressions for justified exceptions.
4. Enable the rule on changed files before expanding it to the full repository.
5. Measure the before-and-after finding count and document the rollout status.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `onboard-a-new-developer-in-a-week`
- `scaffold-a-new-service-repository`
- `add-a-health-check-endpoint`

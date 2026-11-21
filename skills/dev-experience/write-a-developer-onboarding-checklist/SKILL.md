---
name: write-a-developer-onboarding-checklist
description: Assemble a day-one developer checklist with every prerequisite, verification, and first-change milestone. Use when the user is preparing an onboarding checklist for a new engineering hire.
domain: dev-experience
tags: [onboarding, checklist, developer-experience]
triggers: ["developer onboarding checklist", "new developer day-one checklist", "onboard an engineer checklist"]
---

# Assemble a day-one developer checklist with every prerequisite, verification, and first-change milestone

## Purpose

Assemble a day-one developer checklist with every prerequisite, verification, and first-change milestone.

## When to use

Use when the user is preparing an onboarding checklist for a new engineering hire.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. List required accounts, repositories, services, and local tools for day one.
2. Order each item by dependency and assign an owner for unresolved access needs.
3. Pair each setup item with a command or observable success signal.
4. Schedule a small first change that exercises the full workflow.
5. Review the checklist with a recent hire and remove unclear or duplicate steps.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `write-a-developer-cli-wrapper`
- `onboard-a-new-developer-in-a-week`
- `write-a-good-commit-message`

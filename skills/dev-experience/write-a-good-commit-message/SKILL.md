---
name: write-a-good-commit-message
description: Write a commit message that explains the change's purpose, impact, and verification. Use when the user wants a concise commit message for a completed code change.
domain: dev-experience
tags: [commit-message, version-control, code-review]
triggers: ["write a good commit message", "create a commit message for this change", "format a conventional commit message"]
---

# Write a commit message that explains the change's purpose, impact, and verification

## Purpose

Write a commit message that explains the change's purpose, impact, and verification.

## When to use

Use when the user wants a concise commit message for a completed code change.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Identify the user-visible or operational reason for the change.
2. Choose a concise subject that states the outcome in the imperative mood.
3. Describe the key implementation details and trade-offs only when they aid review.
4. Add the issue identifier and any required migration or rollout notes.
5. Check the message against the repository's subject-length and validation rules.

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
- `write-a-developer-onboarding-checklist`
- `write-a-task-runner-for-a-repo`

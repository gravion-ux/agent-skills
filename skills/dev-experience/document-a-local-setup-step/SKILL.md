---
name: document-a-local-setup-step
description: Document one local setup step with prerequisites, commands, expected output, and recovery guidance. Use when the user needs a reproducible setup instruction in the developer documentation.
domain: dev-experience
tags: [setup-documentation, developer-docs, local-setup]
triggers: ["document a local setup step", "write setup instructions for developers", "add a verified local setup guide step"]
---

# Document one local setup step with prerequisites, commands, expected output, and recovery guidance

## Purpose

Document one local setup step with prerequisites, commands, expected output, and recovery guidance.

## When to use

Use when the user needs a reproducible setup instruction in the developer documentation.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Identify the exact outcome the setup step must produce.
2. List its prerequisites, command, and expected success output.
3. Add a verification command that proves the step completed.
4. Document the most likely failure and the safe recovery action.
5. Place the step in the setup guide and test it from a clean environment.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `reset-a-broken-local-environment`
- `set-up-a-local-development-environment`
- `add-a-health-check-endpoint`

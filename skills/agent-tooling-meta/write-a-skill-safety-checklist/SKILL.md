---
name: write-a-skill-safety-checklist
description: Write a safety checklist for a skill that names the actions that need a confirmation. Use when the user wants to make the risky steps of a skill explicit.
domain: agent-tooling-meta
tags: [safety, checklist, confirmation]
triggers: ["write a skill safety checklist", "which actions need confirmation in my skill", "guardrails for an agent skill"]
---

# Write a safety checklist for a skill that names the actions that need a confirmation

## Purpose

Write a safety checklist for a skill that names the actions that need a confirmation.

## When to use

Use when the user wants to make the risky steps of a skill explicit.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. List the actions the skill performs that change something outside the working session.
2. Mark which of them are irreversible and which are hard to notice afterwards.
3. State what must be confirmed before each risky action and by whom.
4. State what the skill must never do on its own, such as widening permissions.
5. Write the fallback for when the confirmation is refused or is unavailable.

## Output contract

An improved skill, prompt, tool wrapper or evaluation that raises the observed failure rate down.

## Validation checklist

- [ ] The change is measured against the failure it targets
- [ ] The skill follows the repository's format exactly
- [ ] The generated artefacts are reproducible

## Safety notes

Never widen an agent's permissions to work around a skill bug, and never encode a secret in a prompt or skill.

## Related skills

- `write-a-migration-note-for-a-skill-change`
- `write-a-reusable-skill`
- `write-a-skill-regression-suite`

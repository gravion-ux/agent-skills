---
name: retire-a-skill-nobody-uses
description: Retire an unused skill without breaking the skills that point at it. Use when the user wants to remove a skill that is no longer earning its place.
domain: agent-tooling-meta
tags: [retirement, cleanup, maintenance]
triggers: ["retire a skill nobody uses", "remove an unused skill safely", "deprecate a skill in my catalogue"]
---

# Retire an unused skill without breaking the skills that point at it

## Purpose

Retire an unused skill without breaking the skills that point at it.

## When to use

Use when the user wants to remove a skill that is no longer earning its place.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Check the usage data over a period long enough to be meaningful.
2. Find every reference to the skill, including the related links and the routers.
3. Confirm the skill is not the only path to a capability that is still needed.
4. Remove the references first, then the skill itself.
5. Regenerate the catalogue and record the retirement with the reason.

## Output contract

An improved skill, prompt, tool wrapper or evaluation that raises the observed failure rate down.

## Validation checklist

- [ ] The change is measured against the failure it targets
- [ ] The skill follows the repository's format exactly
- [ ] The generated artefacts are reproducible

## Safety notes

Never widen an agent's permissions to work around a skill bug, and never encode a secret in a prompt or skill.

## Related skills

- `add-a-citation-to-a-skill`
- `build-a-skill-evaluation-harness`
- `create-a-skill-template`

---
name: compose-two-skills-into-a-chain
description: Compose two skills into a chain where the first produces what the second consumes. Use when the user wants two skills run in sequence to complete one larger task.
domain: agent-tooling-meta
tags: [chain, composition, orchestration]
triggers: ["compose two skills into a chain", "run skill a then skill b", "chain skills with a clean hand-off"]
---

# Compose two skills into a chain where the first produces what the second consumes

## Purpose

Compose two skills into a chain where the first produces what the second consumes.

## When to use

Use when the user wants two skills run in sequence to complete one larger task.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Name the artefact the first skill produces and the artefact the second one needs.
2. Check that the output contract of the first matches the input of the second exactly.
3. Write the hand-off as a named artefact rather than as a conversation between skills.
4. Add the check that confirms the first output is valid before the second starts.
5. Decide what happens when the first skill produces something the second cannot use.

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
- `audit-a-catalogue-for-gaps`
- `build-a-skill-evaluation-harness`

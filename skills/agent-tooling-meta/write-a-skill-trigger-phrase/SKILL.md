---
name: write-a-skill-trigger-phrase
description: Write trigger phrases that match how people actually ask for the task. Use when the user wants better trigger phrases so a skill gets picked up for the right requests.
domain: agent-tooling-meta
tags: [triggers, routing, phrasing]
triggers: ["write skill trigger phrases", "phrase that would make my skill match", "improve the triggers on a skill"]
---

# Write trigger phrases that match how people actually ask for the task

## Purpose

Write trigger phrases that match how people actually ask for the task.

## When to use

Use when the user wants better trigger phrases so a skill gets picked up for the right requests.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Collect the real requests that should reach this skill and the ones that should not.
2. Write the bare noun phrase first, the way it would appear in a list of options.
3. Write the verb-led variants using the words the requester actually used.
4. Check each phrase against the whole catalogue for a collision with another skill.
5. Remove any phrase that would also be a fair request for a different skill.

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

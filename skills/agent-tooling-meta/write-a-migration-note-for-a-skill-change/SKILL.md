---
name: write-a-migration-note-for-a-skill-change
description: Write a migration note that tells the people using a skill exactly what changed for them. Use when the user changes a skill in a way that alters how it should be called or used.
domain: agent-tooling-meta
tags: [migration-note, communication, changelog]
triggers: ["write a migration note for a skill change", "tell users what changed in my skill", "breaking change note for a skill"]
---

# Write a migration note that tells the people using a skill exactly what changed for them

## Purpose

Write a migration note that tells the people using a skill exactly what changed for them.

## When to use

Use when the user changes a skill in a way that alters how it should be called or used.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. State what changed in one sentence, in terms of the behaviour rather than the code.
2. List what still works exactly as before.
3. Show the old and the new call or trigger side by side.
4. State the date the change takes effect and what to do before that date.
5. Give the fallback for anyone who cannot make the change in time.

## Output contract

An improved skill, prompt, tool wrapper or evaluation that raises the observed failure rate down.

## Validation checklist

- [ ] The change is measured against the failure it targets
- [ ] The skill follows the repository's format exactly
- [ ] The generated artefacts are reproducible

## Safety notes

Never widen an agent's permissions to work around a skill bug, and never encode a secret in a prompt or skill.

## Related skills

- `design-a-router-for-a-skill-catalogue`
- `design-a-skill-for-a-multi-domain-task`
- `design-a-skill-for-a-repeated-task`

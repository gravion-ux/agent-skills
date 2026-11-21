---
name: design-a-skill-for-a-repeated-task
description: Design a skill for a repeated task only after confirming the repetition is real. Use when the user thinks a task happens often enough to justify a skill.
domain: agent-tooling-meta
tags: [design, reuse, analysis]
triggers: ["design a skill for a repeated task", "is this task worth a skill", "is this repetitive enough to automate"]
---

# Design a skill for a repeated task only after confirming the repetition is real

## Purpose

Design a skill for a repeated task only after confirming the repetition is real.

## When to use

Use when the user thinks a task happens often enough to justify a skill.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Count how often the task ran over the last few months and who ran it.
2. Check that the task has a stable shape rather than being different each time.
3. Write the smallest procedure that covers the common case correctly.
4. List the variations that need a branch rather than a new skill.
5. Decide how the skill will be retired if the repetition stops.

## Output contract

An improved skill, prompt, tool wrapper or evaluation that raises the observed failure rate down.

## Validation checklist

- [ ] The change is measured against the failure it targets
- [ ] The skill follows the repository's format exactly
- [ ] The generated artefacts are reproducible

## Safety notes

Never widen an agent's permissions to work around a skill bug, and never encode a secret in a prompt or skill.

## Related skills

- `design-a-skill-for-a-multi-domain-task`
- `design-a-router-for-a-skill-catalogue`
- `document-a-skill-for-another-agent`

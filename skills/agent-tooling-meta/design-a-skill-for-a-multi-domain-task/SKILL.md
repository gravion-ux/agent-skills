---
name: design-a-skill-for-a-multi-domain-task
description: Design a skill for a task that spans domains by splitting it at the hand-off between them. Use when the user wants one skill for a task that needs several kinds of expertise.
domain: agent-tooling-meta
tags: [multi-domain, decomposition, design]
triggers: ["design a skill for a multi domain task", "one task needing several kinds of skill", "split a cross domain task into a chain"]
---

# Design a skill for a task that spans domains by splitting it at the hand-off between them

## Purpose

Design a skill for a task that spans domains by splitting it at the hand-off between them.

## When to use

Use when the user wants one skill for a task that needs several kinds of expertise.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Write the end-to-end outcome the task must produce.
2. Mark the points where the work changes kind, such as from design to implementation.
3. Make each part a separate skill with its own output contract.
4. Write the coordinator that runs the parts in order and checks each hand-off.
5. Test the chain end to end, including the case where a middle part changes its output.

## Output contract

An improved skill, prompt, tool wrapper or evaluation that raises the observed failure rate down.

## Validation checklist

- [ ] The change is measured against the failure it targets
- [ ] The skill follows the repository's format exactly
- [ ] The generated artefacts are reproducible

## Safety notes

Never widen an agent's permissions to work around a skill bug, and never encode a secret in a prompt or skill.

## Related skills

- `design-a-skill-for-a-repeated-task`
- `design-a-router-for-a-skill-catalogue`
- `document-a-skill-for-another-agent`

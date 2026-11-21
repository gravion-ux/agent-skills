---
name: audit-a-catalogue-for-gaps
description: Audit a catalogue for gaps by comparing the domains of real work against the skills available. Use when the user wants to know what a skill catalogue is missing.
domain: agent-tooling-meta
tags: [audit, gaps, coverage]
triggers: ["audit a catalogue for gaps", "what skills are we missing", "check our skill coverage against real work"]
---

# Audit a catalogue for gaps by comparing the domains of real work against the skills available

## Purpose

Audit a catalogue for gaps by comparing the domains of real work against the skills available.

## When to use

Use when the user wants to know what a skill catalogue is missing.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Collect a sample of real tasks from across the organisation's work.
2. Map each task to the domain it belongs to and the skill that should cover it.
3. List the tasks that no skill covers, grouped by the domain they fall into.
4. Check the duplicate case, where several skills cover the same task.
5. Rank the gaps by frequency and propose the order to close them in.

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

---
name: plan-a-skill-catalogue-growth
description: Plan catalogue growth by finding the repeated tasks that are missing a skill. Use when the user wants to grow a skill catalogue in a way that pays for itself.
domain: agent-tooling-meta
tags: [growth, planning, catalogue]
triggers: ["plan skill catalogue growth", "which skills should we write next", "expand our skill library deliberately"]
---

# Plan catalogue growth by finding the repeated tasks that are missing a skill

## Purpose

Plan catalogue growth by finding the repeated tasks that are missing a skill.

## When to use

Use when the user wants to grow a skill catalogue in a way that pays for itself.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Collect the requests that were handled manually because no skill fitted.
2. Cluster them by the underlying task rather than by the wording.
3. Score each cluster by how often it happens and how long it takes.
4. Choose the clusters to write first and write the skill that covers the cluster.
5. Set a review point where the clusters that were not written are reconsidered.

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
- `add-a-citation-to-a-skill`
- `audit-a-catalogue-for-gaps`

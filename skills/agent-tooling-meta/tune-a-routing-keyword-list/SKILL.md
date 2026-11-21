---
name: tune-a-routing-keyword-list
description: Tune a routing keyword list by testing each term against the requests it should catch. Use when the user wants to improve the words a router matches on.
domain: agent-tooling-meta
tags: [keywords, tuning, routing]
triggers: ["tune a routing keyword list", "improve the terms my router matches on", "keywords for skill selection"]
---

# Tune a routing keyword list by testing each term against the requests it should catch

## Purpose

Tune a routing keyword list by testing each term against the requests it should catch.

## When to use

Use when the user wants to improve the words a router matches on.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. List the current terms with the requests each one is meant to catch.
2. Check every term against the requests it should not catch.
3. Remove the terms that match too broadly and add the ones the requests actually use.
4. Check that no two skills end up matched by the same term.
5. Measure the routing accuracy before and after the change and keep it only if it improved.

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

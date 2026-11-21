---
name: manage-skill-dependencies-between-domains
description: Manage cross-domain skill dependencies so a change in one domain cannot break another. Use when the user wants to change or review skills that depend on each other across domains.
domain: agent-tooling-meta
tags: [dependencies, cross-domain, coupling]
triggers: ["manage skill dependencies between domains", "one domain change breaks another", "reduce coupling between skill sets"]
---

# Manage cross-domain skill dependencies so a change in one domain cannot break another

## Purpose

Manage cross-domain skill dependencies so a change in one domain cannot break another.

## When to use

Use when the user wants to change or review skills that depend on each other across domains.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. List the dependencies between the skills and the artefact each one passes on.
2. Check whether the dependency is on a stable output contract or on incidental wording.
3. Make the dependent skills rely on the contract rather than on the exact phrasing.
4. Run the evaluation for both domains whenever either one changes.
5. Record the dependency in the catalogue so the next change knows it is there.

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

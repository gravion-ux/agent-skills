---
name: build-a-skill-evaluation-harness
description: Build an evaluation harness that runs a catalogue against labelled tasks and scores the result. Use when the user wants to measure the quality of a skill catalogue automatically.
domain: agent-tooling-meta
tags: [evaluation, harness, testing]
triggers: ["build a skill evaluation harness", "automatically score my skill catalogue", "regression harness for skill routing"]
---

# Build an evaluation harness that runs a catalogue against labelled tasks and scores the result

## Purpose

Build an evaluation harness that runs a catalogue against labelled tasks and scores the result.

## When to use

Use when the user wants to measure the quality of a skill catalogue automatically.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Define the task set with the expected skill and the expected output for each case.
2. Write the runner that loads the catalogue and invokes the routing path.
3. Score each run against the expected result with explicit pass and fail criteria.
4. Store the results per run so a regression is visible over time.
5. Set the thresholds that must pass before a change is accepted.

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
- `create-a-skill-template`
- `design-a-router-for-a-skill-catalogue`

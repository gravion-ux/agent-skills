---
name: migrate-a-skill-to-a-new-format
description: Migrate skills to a new format by transforming the source and regenerating the output. Use when the user changes the structure of the skill format and must move the existing catalogue.
domain: agent-tooling-meta
tags: [migration, format, conversion]
triggers: ["migrate a skill to a new format", "convert the catalogue to the new structure", "move skills to a new schema"]
---

# Migrate skills to a new format by transforming the source and regenerating the output

## Purpose

Migrate skills to a new format by transforming the source and regenerating the output.

## When to use

Use when the user changes the structure of the skill format and must move the existing catalogue.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Write the mapping from each old field to each new field, including what is dropped.
2. Convert the source files first, because the generated files follow from them.
3. Run the generator and check that the number of skills is unchanged.
4. Run the validator and the evaluation suite against the converted catalogue.
5. Compare the old and new outputs for a sample and explain every difference.

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

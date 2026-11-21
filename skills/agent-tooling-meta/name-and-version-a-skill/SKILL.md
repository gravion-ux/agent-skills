---
name: name-and-version-a-skill
description: Name and version a skill so its identity stays stable as its behaviour changes. Use when the user wants to name a new skill and decide how its version will move.
domain: agent-tooling-meta
tags: [naming, versioning, hygiene]
triggers: ["name and version a skill", "skill naming convention and semver", "how should I version this skill"]
---

# Name and version a skill so its identity stays stable as its behaviour changes

## Purpose

Name and version a skill so its identity stays stable as its behaviour changes.

## When to use

Use when the user wants to name a new skill and decide how its version will move.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Name the skill after the task it performs, in lowercase hyphenated form.
2. Check the name does not already exist in the catalogue or collide with a router.
3. Start the version at the first release and write down what that release does.
4. Increase the major version when the behaviour changes in a way a user would notice.
5. Record the version and the change in the same commit as the change itself.

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

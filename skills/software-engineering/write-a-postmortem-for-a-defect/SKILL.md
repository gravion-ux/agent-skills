---
name: write-a-postmortem-for-a-defect
description: Produce a blameless defect postmortem with evidence, contributing factors, owned actions, and follow-up dates. Use when the user wants a production defect analyzed and prevention actions assigned.
domain: software-engineering
tags: [postmortem, incident-review, reliability]
triggers: ["write a defect postmortem", "analyze a production defect blamelessly"]
---

# Produce a blameless defect postmortem with evidence, contributing factors, owned actions, and follow-up dates

## Purpose

Produce a blameless defect postmortem with evidence, contributing factors, owned actions, and follow-up dates.

## When to use

Use when the user wants a production defect analyzed and prevention actions assigned.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Build the incident timeline from logs, commits, and deploy records.
2. Quantify user impact, duration, and detection gaps.
3. Identify contributing system and process conditions without blame.
4. Define corrective actions with owners and due dates.
5. Link each action to a tracked ticket or review item.
6. Review the postmortem and publish the final record.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `configure-formatting-and-linting-for-a-repo`
- `prepare-a-pull-request-for-review`
- `prepare-code-for-a-code-freeze`

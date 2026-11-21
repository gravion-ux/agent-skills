---
name: reproduce-a-bug-in-a-local-sandbox
description: Reproduce a reported bug in a local sandbox with captured inputs, evidence, and a repeatable command. Use when the user needs a reported software defect reproduced safely outside production.
domain: software-engineering
tags: [bug-reproduction, sandbox, debugging]
triggers: ["reproduce bug in local sandbox", "capture repeatable software failure", "run defect outside production"]
---

# Reproduce a reported bug in a local sandbox with captured inputs, evidence, and a repeatable command

## Purpose

Reproduce a reported bug in a local sandbox with captured inputs, evidence, and a repeatable command.

## When to use

Use when the user needs a reported software defect reproduced safely outside production.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Record the expected result, actual result, environment, and minimal input.
2. Create an isolated local workspace with sanitized data and dependencies.
3. Capture the failing command, stack trace, and runtime observations.
4. Reduce the input and environment until the failure is repeatable.
5. Attach the reproduction command and findings to the bug report.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `handle-merge-conflicts-in-a-feature-branch`
- `triage-a-bug-report-with-a-reproducer`
- `work-in-a-legacy-codebase-without-tests`

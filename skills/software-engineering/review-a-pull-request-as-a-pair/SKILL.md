---
name: review-a-pull-request-as-a-pair
description: Review a pull request as a pair by finding defects, proving them, and separating blockers from suggestions. Use when the user wants a two-person review of a proposed repository change.
domain: software-engineering
tags: [code-review, pair-review, defect-analysis]
triggers: ["review pull request as pair", "pair review code changes", "find and prove review defects"]
---

# Review a pull request as a pair by finding defects, proving them, and separating blockers from suggestions

## Purpose

Review a pull request as a pair by finding defects, proving them, and separating blockers from suggestions.

## When to use

Use when the user wants a two-person review of a proposed repository change.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Read the ticket, design context, and full diff before judging individual lines.
2. Trace changed behavior through callers and compare it with acceptance criteria.
3. Reproduce each suspected defect with a focused test or command.
4. Discuss blockers separately from optional suggestions and record disagreements.
5. Verify proposed fixes and summarize evidence, rationale, and remaining risk.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `prepare-a-pull-request-for-review`
- `revive-a-stale-pull-request`
- `split-a-large-pull-request`

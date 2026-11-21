---
name: tidy-a-noisy-git-history
description: Rewrite a noisy local git history into reviewable commits while preserving the final tree. Use when the user wants a local branch history cleaned before review.
domain: software-engineering
tags: [git-history, commit-hygiene, history-rewrite]
triggers: ["tidy noisy git history", "rewrite commits into logical units", "clean messy local branch history"]
---

# Rewrite a noisy local git history into reviewable commits while preserving the final tree

## Purpose

Rewrite a noisy local git history into reviewable commits while preserving the final tree.

## When to use

Use when the user wants a local branch history cleaned before review.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Record the branch tip, tree hash, and worktree state before rewriting.
2. Exclude untracked user files from any cleanup operation.
3. Group changes into logical commits without mixing unrelated work.
4. Rewrite history with a non-interactive command and compare the final tree with the original.
5. Run the existing suite and record the old tip, new commits, and recovery command.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `add-structured-logging-to-a-code-path`
- `apply-solid-principles-to-a-class`
- `automate-a-repetitive-code-change`

---
name: router-code-quality
description: Route work in the Code quality domain to the right leaf skill. Use when a task clearly belongs to code-quality.
domain: code-quality
tags: [router, routing, code-quality]
triggers: ["route a code-quality task", "which code-quality skill should I use"]
---

# Code quality router

## Purpose

List every leaf skill in the code-quality domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside code-quality and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `add-typing-to-an-untyped-function` | Use when the user wants type annotations added to a public or error-prone function. |
| `apply-a-formatter-consistently` | Use when the user wants formatting normalized across files without changing behavior. |
| `audit-a-file-for-hidden-side-effects` | Use when the user suspects a file performs side effects hidden in helpers or imports. |
| `detect-and-remove-duplicate-utility-functions` | Use when the user wants overlapping helper functions found and merged safely. |
| `enable-strict-mode-on-a-module` | Use when the user wants strict type checking enabled for a single module. |
| `enforce-coding-standards-with-tooling` | Use when the user wants coding standards enforced automatically instead of through review reminders. |
| `improve-a-codebase-readme` | Use when the user wants a repository README corrected or expanded for contributors. |
| `keep-configuration-in-one-place` | Use when the user wants configuration values scattered across a codebase brought together. |
| `keep-functions-short-and-focused` | Use when the user wants an oversized function divided into smaller single-purpose units. |
| `make-error-messages-actionable` | Use when the user wants unclear exception or validation messages made easier to act on. |
| `name-things-well` | Use when the user wants variables functions or types renamed for clearer intent. |
| `reduce-a-modules-cyclomatic-complexity` | Use when the user wants a module with high cyclomatic complexity made easier to reason about. |
| `refactor-for-testability` | Use when the user wants difficult code refactored so its behavior can be tested reliably. |
| `remove-a-feature-flag-left-behind` | Use when the user wants a feature flag deleted after its rollout has finished. |
| `remove-a-temporary-workaround` | Use when the user wants an old workaround removed because its root cause has been fixed. |
| `remove-an-unsafe-cast` | Use when the user wants an unsafe type cast replaced with a provably safe alternative. |
| `remove-dead-dependencies-and-code` | Use when the user wants unreachable or unused code and dependencies deleted safely. |
| `remove-duplicated-code` | Use when the user wants repeated code consolidated into a smaller maintainable implementation. |
| `replace-a-flag-argument-with-two-functions` | Use when the user wants a boolean argument removed because it controls unrelated behavior. |
| `replace-magic-numbers-with-named-constants` | Use when the user wants unexplained numeric literals replaced with readable named constants. |
| `review-a-diff-for-correctness` | Use when the user wants a code diff reviewed for correctness before it is merged. |
| `review-a-pr-for-scope-discipline` | Use when the user wants a pull request checked for focus size and mixed concerns. |
| `review-dependency-hygiene` | Use when the user wants a project dependencies audited for hygiene and maintenance cost. |
| `run-a-weekly-quality-improvement-pass` | Use when the user wants an agent to run a repeatable weekly code quality improvement. |
| `simplify-a-complex-condition` | Use when the user wants a deeply nested or compound condition made easier to verify. |
| `spot-a-nullable-bug-by-reading-types` | Use when the user suspects a null dereference or missing-value bug in typed code. |
| `stop-catching-and-ignoring-errors` | Use when the user wants ignored exceptions or blanket error catches removed. |
| `tighten-a-loose-type-annotation` | Use when the user wants an any-like or overly broad annotation replaced precisely. |
| `write-a-code-smell-triage-list` | Use when the user wants code smells collected prioritized into an actionable backlog. |
| `write-self-documenting-code` | Use when the user wants stale comments and unclear code replaced with self-explanatory structure. |

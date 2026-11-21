---
name: remove-dead-dependencies-and-code
description: Remove unreachable modules unused imports and dead branches after proving they are unreferenced. Use when the user wants unreachable or unused code and dependencies deleted safely.
domain: code-quality
tags: [dead-code, dependencies, cleanup, code-quality]
triggers: ["remove dead code", "delete unused imports", "strip dead branches"]
---

# Remove unreachable modules unused imports and dead branches after proving they are unreferenced

## Purpose

Remove unreachable modules unused imports and dead branches after proving they are unreferenced.

## When to use

Use when the user wants unreachable or unused code and dependencies deleted safely.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Map imports callers and coverage to identify potentially dead code.
2. Confirm each candidate has no runtime entry point, reflection use, or external contract.
3. Delete the unused imports modules and dead branches in one focused change.
4. Run the full test suite and the configured static analysis.
5. Document exclusions for code that cannot be proven dead.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `detect-and-remove-duplicate-utility-functions`
- `remove-duplicated-code`
- `keep-functions-short-and-focused`

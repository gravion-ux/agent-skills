---
name: stop-catching-and-ignoring-errors
description: Stop swallowing errors by handling, propagating, or reporting them with explicit intent. Use when the user wants ignored exceptions or blanket error catches removed.
domain: code-quality
tags: [error-handling, exceptions, reliability, code-quality]
triggers: ["stop ignoring errors", "remove empty exception catch", "ignored exception cleanup"]
---

# Stop swallowing errors by handling, propagating, or reporting them with explicit intent

## Purpose

Stop swallowing errors by handling, propagating, or reporting them with explicit intent.

## When to use

Use when the user wants ignored exceptions or blanket error catches removed.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Find each blanket catch and record the errors it currently hides.
2. Choose to recover, translate, or propagate the exception explicitly.
3. Add context to the propagated error or report the ignored condition.
4. Delete the empty handler and its misleading cleanup code.
5. Run failure-path tests plus the linter and formatter.

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
- `keep-functions-short-and-focused`
- `remove-dead-dependencies-and-code`

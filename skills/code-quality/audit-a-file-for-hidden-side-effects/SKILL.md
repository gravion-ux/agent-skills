---
name: audit-a-file-for-hidden-side-effects
description: Audit a file for hidden side effects by tracing I/O globals state and network calls. Use when the user suspects a file performs side effects hidden in helpers or imports.
domain: code-quality
tags: [side-effects, audit, dependencies, code-quality]
triggers: ["hidden side effects", "audit file side effects", "find implicit io effects"]
---

# Audit a file for hidden side effects by tracing I/O globals state and network calls

## Purpose

Audit a file for hidden side effects by tracing I/O globals state and network calls.

## When to use

Use when the user suspects a file performs side effects hidden in helpers or imports.

## When NOT to use

Do not use this for a functional bug hunt; use testing-qa instead.

## Inputs required

- The files or modules in scope
- The rule or standard being applied
- The effort budget for the change

## Procedure

1. Trace every function and import that touches files globals clocks or networks.
2. Record each side effect with its trigger, target, and failure behavior.
3. Separate intentional effects from accidental ones and rank the risks.
4. Refactor only the accidental effect into an explicit dependency when approved.
5. Run focused tests and verify the diff contains no behavioral change.

## Output contract

A focused refactor with the behaviour preserved and the diff explained.

## Validation checklist

- [ ] Behaviour is unchanged and covered by tests
- [ ] The change is smaller than the debt it removes
- [ ] The linter and formatter are clean

## Safety notes

Never mix a behavioural fix with a large refactor in the same change.

## Related skills

- `review-a-diff-for-correctness`
- `review-a-pr-for-scope-discipline`
- `apply-a-formatter-consistently`

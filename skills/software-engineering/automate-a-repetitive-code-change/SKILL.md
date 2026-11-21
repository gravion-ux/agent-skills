---
name: automate-a-repetitive-code-change
description: Automate a repetitive source change with a bounded codemod that reports edits and preserves verified behavior. Use when the user wants a repeated repository-wide code edit handled by an agent or script.
domain: software-engineering
tags: [codemod, source-transformation, automation]
triggers: ["automate a repetitive code change", "write a bounded codemod"]
---

# Automate a repetitive source change with a bounded codemod that reports edits and preserves verified behavior

## Purpose

Automate a repetitive source change with a bounded codemod that reports edits and preserves verified behavior.

## When to use

Use when the user wants a repeated repository-wide code edit handled by an agent or script.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Define the exact pattern and the file scope for the change.
2. Write an AST-aware or syntax-aware transformation script.
3. Run the script in report-only mode and inspect the diff.
4. Apply the transformation only within the approved scope.
5. Format the output and run targeted and full tests.
6. Document the command, exclusions, and rollback procedure.

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
- `estimate-a-change-before-starting-it`
- `migrate-code-to-a-new-language-version`

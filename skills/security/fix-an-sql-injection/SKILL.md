---
name: fix-an-sql-injection
description: Close an SQL injection path with parameterised queries and a regression proof. Use when the user has identified a SQL injection in an application query.
domain: security
tags: [sql-injection, parameterised-queries, regression-testing]
triggers: ["fix an sql injection", "repair a vulnerable sql query", "parameterise an injectable sql statement"]
---

# Close an SQL injection path with parameterised queries and a regression proof

## Purpose

Close an SQL injection path with parameterised queries and a regression proof.

## When to use

Use when the user has identified a SQL injection in an application query.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Locate the vulnerable query and record the injectable parameter and sink.
2. Reproduce the injection with a harmless marker that cannot alter data.
3. Replace concatenated values with bound parameters or a validated query builder call.
4. Add a regression test that submits the marker and asserts the expected result.
5. Verify the query plan and application behaviour against the test database.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `fix-an-xss-vulnerability`
- `add-input-validation-to-an-endpoint`
- `enforce-authorisation-on-an-api`

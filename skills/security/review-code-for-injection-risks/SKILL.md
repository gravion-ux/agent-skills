---
name: review-code-for-injection-risks
description: Review code for injection paths and document reproducible fixes for each finding. Use when the user wants untrusted input paths reviewed for injection vulnerabilities.
domain: security
tags: [code-review, injection, taint-analysis]
triggers: ["review code for injection risks", "scan source code for injection", "find injection vulnerabilities in code"]
---

# Review code for injection paths and document reproducible fixes for each finding

## Purpose

Review code for injection paths and document reproducible fixes for each finding.

## When to use

Use when the user wants untrusted input paths reviewed for injection vulnerabilities.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Map each entry point to the sink it reaches and record the taint path in a review sheet.
2. Reproduce the unsafe path with a harmless test input and capture the exact code location.
3. Explain the attacker-controlled input and the impact of reaching the sink.
4. Propose a fix that removes the dangerous interpretation rather than masking the symptom.
5. Verify the fix with the reproduction test and an equivalent safe-input test.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `enable-audit-logging-for-a-cloud-account`
- `enforce-mfa-for-an-organisation`
- `fix-an-sql-injection`

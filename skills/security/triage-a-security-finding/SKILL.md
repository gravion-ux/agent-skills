---
name: triage-a-security-finding
description: Triage a security finding by confirming exploitability, impact, and the first safe fix. Use when the user has a new security finding that needs validation and prioritisation.
domain: security
tags: [finding-triage, severity-assessment, remediation]
triggers: ["triage a security finding", "validate and prioritise a vulnerability report", "decide the severity and fix order for a finding"]
---

# Triage a security finding by confirming exploitability, impact, and the first safe fix

## Purpose

Triage a security finding by confirming exploitability, impact, and the first safe fix.

## When to use

Use when the user has a new security finding that needs validation and prioritisation.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Record the affected asset, attacker precondition, affected component, and source of the report.
2. Reproduce the issue in a safe test environment and capture concise evidence.
3. Assign severity from verified impact and exposure rather than the reported severity alone.
4. Choose the first concrete fix that closes the path and name its verification test.
5. Track the owner, deadline, and residual risk until the fix passes its verification step.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `triage-a-bug-bounty-finding`
- `add-security-headers-to-a-web-app`
- `prepare-for-a-security-questionnaire`

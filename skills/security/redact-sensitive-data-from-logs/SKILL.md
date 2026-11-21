---
name: redact-sensitive-data-from-logs
description: Remove secrets and personal data from log output at the point of writing it. Use when the user wants to stop sensitive values reaching a log store or a third party collector.
domain: security
tags: [logging, redaction, privacy]
triggers: ["redact sensitive data from logs", "strip secrets from log output", "mask personal data before logging"]
---

# Remove secrets and personal data from log output at the point of writing it

## Purpose

Remove secrets and personal data from log output at the point of writing it.

## When to use

Use when the user wants to stop sensitive values reaching a log store or a third party collector.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Inventory the fields that can carry a token, credential or personal identifier.
2. Redact the value at the logging call site rather than after the fact.
3. Replace the value with a stable hash or a masked form that still allows correlation.
4. Search the existing log store for the same pattern and plan its cleanup.
5. Add a test that asserts the raw value never reaches the handler.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `audit-access-to-sensitive-data`
- `apply-data-classification-labels`
- `implement-data-retention-controls`

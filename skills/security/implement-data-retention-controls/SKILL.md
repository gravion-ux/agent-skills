---
name: implement-data-retention-controls
description: Apply retention rules so each data class is deleted on schedule and kept no longer. Use when the user wants records deleted automatically once the retention period ends.
domain: security
tags: [retention, deletion, policy]
triggers: ["implement data retention controls", "delete records on schedule automatically", "set a legal hold on retention rules"]
---

# Apply retention rules so each data class is deleted on schedule and kept no longer

## Purpose

Apply retention rules so each data class is deleted on schedule and kept no longer.

## When to use

Use when the user wants records deleted automatically once the retention period ends.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. List each data store and the retention rule that applies to its records.
2. Set the deletion trigger on the store itself rather than on a manual job.
3. Apply a legal hold that pauses deletion where an investigation is open.
4. Log each deletion with the store, the record count and the rule applied.
5. Test the rule on a copy of the data before it touches the live store.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `apply-data-classification-labels`
- `audit-access-to-sensitive-data`
- `implement-secure-file-uploads`

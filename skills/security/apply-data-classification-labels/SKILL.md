---
name: apply-data-classification-labels
description: Label data by sensitivity class so access, retention and sharing rules can follow the label. Use when the user wants to classify stored data and make the handling rules follow automatically.
domain: security
tags: [classification, data, governance]
triggers: ["apply data classification labels", "label data by sensitivity level", "set a data classification scheme"]
---

# Label data by sensitivity class so access, retention and sharing rules can follow the label

## Purpose

Label data by sensitivity class so access, retention and sharing rules can follow the label.

## When to use

Use when the user wants to classify stored data and make the handling rules follow automatically.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Define the classification levels and the examples that belong to each one.
2. Map each storage location to the class of data it holds.
3. Apply the label to every record, bucket and column that holds sensitive data.
4. Link each label to the access group and the retention period it implies.
5. Sample the estate to confirm no sensitive store is left unlabelled.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `apply-the-principle-of-least-privilege`
- `audit-access-to-sensitive-data`
- `implement-data-retention-controls`

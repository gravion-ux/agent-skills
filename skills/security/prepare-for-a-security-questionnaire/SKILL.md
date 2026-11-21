---
name: prepare-for-a-security-questionnaire
description: Answer a customer security questionnaire from evidence and record every gap you cannot close. Use when the user must complete a customer's security assessment questionnaire.
domain: security
tags: [questionnaire, compliance, evidence]
triggers: ["prepare for a security questionnaire", "complete a customer security assessment", "answer a vendor security questionnaire"]
---

# Answer a customer security questionnaire from evidence and record every gap you cannot close

## Purpose

Answer a customer security questionnaire from evidence and record every gap you cannot close.

## When to use

Use when the user must complete a customer's security assessment questionnaire.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Map each question to the control that answers it and the owner of that control.
2. Attach the existing evidence instead of restating the policy.
3. Mark every question that no evidence covers and name the gap.
4. Write the remediation plan and the owner for each open gap.
5. Have a security reviewer sign off the completed questionnaire.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `add-security-headers-to-a-web-app`
- `enable-audit-logging-for-a-cloud-account`
- `run-a-security-awareness-session`

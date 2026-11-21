---
name: run-a-security-awareness-session
description: Run a practical security awareness session that measures behaviour change and follow-up. Use when the user wants to teach a team secure everyday practices and verify their understanding.
domain: security
tags: [security-training, phishing-awareness, risk-culture]
triggers: ["run a security awareness session", "teach staff secure everyday behaviour", "deliver phishing and data handling training"]
---

# Run a practical security awareness session that measures behaviour change and follow-up

## Purpose

Run a practical security awareness session that measures behaviour change and follow-up.

## When to use

Use when the user wants to teach a team secure everyday practices and verify their understanding.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Set the session goal and choose realistic scenarios tied to the audience's daily responsibilities.
2. Demonstrate phishing, credential handling, data sharing, and incident-reporting behaviours.
3. Run scenario exercises and collect each participant's decisions without exposing real secrets.
4. Score the responses against explicit policy expectations and revisit missed safeguards.
5. Record attendance, assessment results, follow-up actions, and a date for reinforcement.

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
- `prepare-for-a-security-questionnaire`
- `run-a-compliance-gap-assessment`

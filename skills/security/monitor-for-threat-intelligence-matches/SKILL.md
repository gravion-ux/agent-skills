---
name: monitor-for-threat-intelligence-matches
description: Watch threat intelligence feeds and confirm each match against the actual estate. Use when the user wants new threat data checked against the systems they run.
domain: security
tags: [threat-intel, indicators, monitoring]
triggers: ["monitor for threat intelligence matches", "match threat indicators against your estate", "watch a threat feed for real hits"]
---

# Watch threat intelligence feeds and confirm each match against the actual estate

## Purpose

Watch threat intelligence feeds and confirm each match against the actual estate.

## When to use

Use when the user wants new threat data checked against the systems they run.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Subscribe to the intelligence sources that match the threat profile.
2. Match the indicators against the asset inventory rather than against raw logs.
3. Confirm each match on an affected host before raising it as a finding.
4. Record the indicator, the affected asset and the action taken.
5. Set the expiry for each indicator so old matches stop alerting.

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
- `prepare-for-a-security-questionnaire`

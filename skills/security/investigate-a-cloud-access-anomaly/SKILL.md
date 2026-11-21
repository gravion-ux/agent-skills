---
name: investigate-a-cloud-access-anomaly
description: Investigate a suspicious cloud sign-in by reconstructing the session and scoping the access taken. Use when the user reports an unfamiliar sign-in or unusual privilege use in a cloud account.
domain: security
tags: [investigation, cloud-access, sign-in]
triggers: ["investigate a suspicious cloud sign in", "review unusual cloud account activity", "trace an unknown cloud login"]
---

# Investigate a suspicious cloud sign-in by reconstructing the session and scoping the access taken

## Purpose

Investigate a suspicious cloud sign-in by reconstructing the session and scoping the access taken.

## When to use

Use when the user reports an unfamiliar sign-in or unusual privilege use in a cloud account.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Pull the sign-in and activity records for the account and the surrounding hour.
2. Reconstruct the source address, device and authentication method used in the session.
3. List the API calls made in the session and the resources they touched.
4. Compare the access with the account holder's normal pattern and assigned role.
5. Record the finding with evidence, impact and the containment step to take next.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `configure-a-cloud-firewall-baseline`
- `enable-audit-logging-for-a-cloud-account`
- `add-security-headers-to-a-web-app`

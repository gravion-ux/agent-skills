---
name: respond-to-a-ransomware-suspicion
description: Contain a suspected ransomware event by isolating affected hosts and preserving evidence first. Use when the user suspects encryption activity or destructive malware on production systems.
domain: security
tags: [ransomware, incident, containment]
triggers: ["respond to a ransomware suspicion", "contain suspected ransomware activity", "handle a suspected encryption attack"]
---

# Contain a suspected ransomware event by isolating affected hosts and preserving evidence first

## Purpose

Contain a suspected ransomware event by isolating affected hosts and preserving evidence first.

## When to use

Use when the user suspects encryption activity or destructive malware on production systems.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Isolate the affected hosts from the network without powering them off.
2. Preserve memory and disk artefacts from one representative infected host.
3. Check the identity provider for sessions and credentials created during the window.
4. Block the observed indicators at the endpoint, proxy and firewall layers.
5. Write the containment timeline and the restoration prerequisites for the response lead.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `respond-to-a-leaked-secret`
- `add-security-headers-to-a-web-app`
- `add-input-validation-to-an-endpoint`

---
name: configure-a-cloud-firewall-baseline
description: Set a cloud firewall baseline that blocks public access except to the ports the service needs. Use when the user wants a reviewed default deny firewall rule set for a cloud network.
domain: security
tags: [firewall, network, baseline]
triggers: ["cloud firewall baseline rules", "set a default deny cloud firewall", "configure a cloud ingress baseline"]
---

# Set a cloud firewall baseline that blocks public access except to the ports the service needs

## Purpose

Set a cloud firewall baseline that blocks public access except to the ports the service needs.

## When to use

Use when the user wants a reviewed default deny firewall rule set for a cloud network.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. List every service the network must reach and the port it uses.
2. Write one inbound allow rule per service and deny everything else.
3. Restrict each allow rule to the source ranges that legitimately need it.
4. Stage the rules in the account rule simulator before applying them.
5. Export the applied ruleset as the reviewed baseline artefact.

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
- `investigate-a-cloud-access-anomaly`
- `schedule-a-recurring-security-baseline-check`

---
name: patch-a-critical-cve
description: Patch a critical vulnerability by fixing the affected code or dependency and proving the path is closed. Use when the user wants to remediate a published critical vulnerability on a live system.
domain: security
tags: [cve, patching, remediation]
triggers: ["patch a critical cve", "fix a published critical vulnerability", "remediate a high severity security advisory"]
---

# Patch a critical vulnerability by fixing the affected code or dependency and proving the path is closed

## Purpose

Patch a critical vulnerability by fixing the affected code or dependency and proving the path is closed.

## When to use

Use when the user wants to remediate a published critical vulnerability on a live system.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Confirm the affected version really contains the vulnerable component and code path.
2. Choose the smallest fix that removes the vulnerable path rather than hiding the symptom.
3. Apply the fix to the dependency or the code and rebuild the artefact.
4. Run a test that exercises the previously vulnerable path and show it now fails safely.
5. Deploy through the normal path and record the residual risk and the deadline.

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
- `build-a-vulnerability-management-program`
- `configure-a-cloud-firewall-baseline`

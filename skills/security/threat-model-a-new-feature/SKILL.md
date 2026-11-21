---
name: threat-model-a-new-feature
description: Produce an evidence-based threat model for a new feature before release. Use when the user wants a new feature assessed for threats before implementation.
domain: security
tags: [threat-modeling, risk-assessment, design-review]
triggers: ["threat model a new feature", "feature threat model", "identify security threats for a feature"]
---

# Produce an evidence-based threat model for a new feature before release

## Purpose

Produce an evidence-based threat model for a new feature before release.

## When to use

Use when the user wants a new feature assessed for threats before implementation.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Record the feature assets, trust boundaries, and attacker capabilities in a threat-model table.
2. Enumerate abuse cases for each trust boundary using the STRIDE categories.
3. Rank each threat by likelihood and impact, then record the affected asset.
4. Choose a concrete control, an owning team, and a verification step for every high-risk threat.
5. Review the threat model with the system owner and archive it beside the feature design.

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

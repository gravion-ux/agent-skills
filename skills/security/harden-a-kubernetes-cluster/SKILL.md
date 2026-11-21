---
name: harden-a-kubernetes-cluster
description: Harden a Kubernetes cluster by tightening control plane settings and pod security defaults. Use when the user wants to raise the security posture of an existing Kubernetes cluster.
domain: security
tags: [kubernetes, cluster, hardening]
triggers: ["harden a kubernetes cluster", "apply pod security standards to a cluster", "tighten kubernetes control plane settings"]
---

# Harden a Kubernetes cluster by tightening control plane settings and pod security defaults

## Purpose

Harden a Kubernetes cluster by tightening control plane settings and pod security defaults.

## When to use

Use when the user wants to raise the security posture of an existing Kubernetes cluster.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Enable the audit log and ship it outside the cluster before changing anything.
2. Apply the restricted pod security standard to every namespace that can take it.
3. Disable automatic service account token mounting where it is not needed.
4. Restrict the cluster roles bound to the default service accounts.
5. Confirm the restrictions with a policy check run against the live cluster.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `harden-a-container-image`
- `harden-a-database-connection`
- `add-security-headers-to-a-web-app`

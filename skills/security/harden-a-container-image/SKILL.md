---
name: harden-a-container-image
description: Harden a container image by removing excess privileges and reducing its runtime attack surface. Use when the user wants a container image minimised for secure production execution.
domain: security
tags: [container-hardening, least-privilege, image-security]
triggers: ["harden a container image", "reduce container runtime privileges", "build a minimal non-root container image"]
---

# Harden a container image by removing excess privileges and reducing its runtime attack surface

## Purpose

Harden a container image by removing excess privileges and reducing its runtime attack surface.

## When to use

Use when the user wants a container image minimised for secure production execution.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Inventory the base image, installed packages, runtime user, and exposed ports in an image report.
2. Use a minimal supported base and remove package caches, build tools, and embedded credentials.
3. Run the workload as a non-root user with a read-only root filesystem and dropped capabilities.
4. Set explicit resource limits and prohibit privilege escalation in the container configuration.
5. Scan the final image and run it to verify that it starts without privileged access.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `scan-a-container-image-for-vulnerabilities`
- `harden-a-database-connection`
- `harden-a-kubernetes-cluster`

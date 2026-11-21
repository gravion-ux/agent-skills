---
name: harden-a-server-baseline
description: Apply a reviewed server baseline that closes common exposures and verifies each hardening control. Use when the user wants a cloud server aligned with a hardened security baseline.
domain: devops-cloud
tags: [hardening, baseline, security, server]
triggers: ["harden a server baseline", "apply host hardening baseline", "server security baseline check"]
---

# Apply a reviewed server baseline that closes common exposures and verifies each hardening control

## Purpose

Apply a reviewed server baseline that closes common exposures and verifies each hardening control.

## When to use

Use when the user wants a cloud server aligned with a hardened security baseline.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Load the approved baseline for the image, version, and workload type.
2. Diff the target host configuration against the baseline before applying changes.
3. Apply only the approved controls and keep a rollback copy of changed files.
4. Verify ssh, firewall, service account, logging, and patch settings explicitly.
5. Attach the before-and-after configuration diff to the change record.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `apply-a-cost-budget-to-cloud-resources`
- `automate-a-release-with-a-pull-request`
- `autoscale-a-kubernetes-workload`

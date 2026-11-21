---
name: scan-an-image-for-vulnerabilities
description: Scan a container image for known vulnerabilities and produce a severity-ranked remediation list. Use when the user wants a container image checked for vulnerabilities before it ships.
domain: devops-cloud
tags: [container-scan, vulnerability, image, sbom]
triggers: ["scan a container image for vulnerabilities", "image vulnerability scan report", "rank container image findings"]
---

# Scan a container image for known vulnerabilities and produce a severity-ranked remediation list

## Purpose

Scan a container image for known vulnerabilities and produce a severity-ranked remediation list.

## When to use

Use when the user wants a container image checked for vulnerabilities before it ships.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Pull the immutable image digest and record its source registry and build date.
2. Scan the image with the approved vulnerability database in an offline runner.
3. Group findings by package, severity, and whether a fixed version exists.
4. Fail the release for critical findings and document accepted high findings.
5. Attach the machine-readable scan report and the digest to the release record.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `write-a-runbook-for-an-on-call-engineer`
- `build-a-container-image`
- `pin-a-container-base-image`

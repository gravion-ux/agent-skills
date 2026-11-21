---
name: scan-a-container-image-for-vulnerabilities
description: Scan a container image for known vulnerabilities and produce a fix list ordered by exposure. Use when the user wants to check a built image for known vulnerabilities before shipping it.
domain: security
tags: [container, scanning, vulnerability]
triggers: ["find security flaws in a container image", "check a built image for known cves", "run an image vulnerability scan"]
---

# Scan a container image for known vulnerabilities and produce a fix list ordered by exposure

## Purpose

Scan a container image for known vulnerabilities and produce a fix list ordered by exposure.

## When to use

Use when the user wants to check a built image for known vulnerabilities before shipping it.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Scan the image by digest so the result matches the exact artefact that will run.
2. Export the findings to a machine readable report for the repository.
3. Group the findings by severity and by whether a running process reaches the vulnerable code.
4. Check whether a patched base image already resolves the findings.
5. Attach the report and the chosen fix to the release record.

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
- `scan-dependencies-for-known-vulnerabilities`
- `enable-audit-logging-for-a-cloud-account`

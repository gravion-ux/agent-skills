---
name: scan-dependencies-for-known-vulnerabilities
description: Scan project dependencies for known vulnerabilities and produce an evidence-backed fix list. Use when the user wants the repository's third-party dependencies checked for published flaws.
domain: security
tags: [dependency-scanning, supply-chain, vulnerability-management]
triggers: ["scan dependencies for known vulnerabilities", "find vulnerable packages in a lockfile", "audit third-party libraries for security flaws"]
---

# Scan project dependencies for known vulnerabilities and produce an evidence-backed fix list

## Purpose

Scan project dependencies for known vulnerabilities and produce an evidence-backed fix list.

## When to use

Use when the user wants the repository's third-party dependencies checked for published flaws.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Generate a dependency manifest from the lockfile and record each package's resolved version.
2. Run the configured vulnerability scanner and capture the advisory identifiers for each match.
3. Confirm the affected code path is reachable and distinguish exploitable matches from noise.
4. Recommend the minimal safe version upgrade or mitigation for each confirmed finding.
5. Re-run the scanner and test suite to verify that no confirmed high-risk match remains.

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
- `enable-audit-logging-for-a-cloud-account`
- `enforce-mfa-for-an-organisation`

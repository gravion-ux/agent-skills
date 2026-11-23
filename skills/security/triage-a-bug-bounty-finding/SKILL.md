---
name: triage-a-bug-bounty-finding
description: Gate a bug bounty finding through seven validation questions on scope, authorisation, reproducibility, demonstrated impact, duplicates, severity and evidence before any report is drafted. Use when the user has a candidate bug bounty finding and needs to decide whether it is worth reporting to a programme.
domain: security
tags: [bug-bounty, triage, validation-gate, severity]
triggers: ["triage a bug bounty finding", "should I report this bounty finding", "validate a finding before submitting it"]
---

# Gate a bug bounty finding through seven validation questions on scope, authorisation, reproducibility, demonstrated impact, duplicates, severity and evidence before any report is drafted

## Purpose

Gate a bug bounty finding through seven validation questions on scope, authorisation, reproducibility, demonstrated impact, duplicates, severity and evidence before any report is drafted.

## When to use

Use when the user has a candidate bug bounty finding and needs to decide whether it is worth reporting to a programme.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Confirm the affected asset and vulnerability class sit inside the programme's published scope and outside its exclusion list.
2. Confirm every test ran under the programme's authorisation, on accounts and data the researcher owns, with no third-party impact.
3. Reproduce the issue end to end from a clean state on the researcher's own test accounts and record the exact steps.
4. Demonstrate the concrete impact with captured evidence, such as another test account's data actually read or changed, rather than a theoretical claim.
5. Run the duplicate check against disclosed reports, known issues and the vendor's recent fixes, and record what was searched.
6. Assign a severity from the demonstrated impact and the programme's own severity guidance, not from the vulnerability class alone.
7. Close the finding as confirmed, ruled out or open proof gap, and name the single missing proof for any finding left open.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `triage-a-security-finding`
- `triage-a-dependency-confusion-risk`
- `add-security-headers-to-a-web-app`

---
name: hunt-verify-and-report-a-bug-bounty-finding
description: Run a complete bug bounty hunt on an authorised target — scope first, then testing from low to high severity, safe verification, duplicate checking, a replayable proof of concept and a submission-ready report, stopping whenever a step cannot be proven. Use when the user wants to hunt a bug bounty target end to end — finding, verifying, deduping and reporting real vulnerabilities without ever submitting an unproven claim.
domain: security
tags: [bug-bounty, end-to-end-hunt, verification, proof-of-concept]
triggers: ["hunt a bug bounty target end to end", "find verify and report a bug bounty bug", "complete bug bounty hunt with poc and report"]
---

# Run a complete bug bounty hunt on an authorised target — scope first, then testing from low to high severity, safe verification, duplicate checking, a replayable proof of concept and a submission-ready report, stopping whenever a step cannot be proven

## Purpose

Run a complete bug bounty hunt on an authorised target — scope first, then testing from low to high severity, safe verification, duplicate checking, a replayable proof of concept and a submission-ready report, stopping whenever a step cannot be proven.

## When to use

Use when the user wants to hunt a bug bounty target end to end — finding, verifying, deduping and reporting real vulnerabilities without ever submitting an unproven claim.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Read the programme brief before touching the target: record the in-scope assets, the account roles that are eligible for reward, the accepted and excluded vulnerability classes, the test-account rules and every testing restriction — and test nothing outside them.
2. Create the test accounts exactly as the programme prescribes (issued aliases, identifying headers or the official sandbox), seed each account with uniquely marked data of your own, and record which account owns what before sending a single test request.
3. Map the attack surface and rank the hunt by demonstrated impact: broken access control (IDOR/BOLA), authentication and session flaws, business-logic abuse and privilege escalation first, then injection, file handling and stored cross-site scripting, keeping low-severity issues only when they chain into real impact.
4. Test one hypothesis at a time with the smallest safe probe — inert markers instead of live payloads, one variable changed per request, and only ever your own accounts and data — capturing the exact request and response for every result.
5. Verify each candidate before believing it: reproduce it end to end from a clean state, run the negative control that must fail without the flaw's precondition, and confirm the response shows real data or a real state change rather than an echoed identifier or a no-op success code.
6. Dedupe before writing anything: search the programme's disclosed reports and known issues, the CVE and advisory record for the component and version, and the vendor's latest security fix — diffing that fix to prove the candidate is a different root cause, or an incomplete fix the patch missed.
7. Gate the finding — in scope, eligible role, demonstrated impact, reproducible from a clean account, not a duplicate, not an excluded class, fully evidenced — and only then write the report: replayable proof-of-concept steps, paired requests and responses, a CVSS score justified metric by metric, the root cause and a concrete remediation, deleting every claim the evidence does not prove.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `triage-a-bug-bounty-finding`
- `dedupe-a-vulnerability-report`
- `triage-a-security-finding`

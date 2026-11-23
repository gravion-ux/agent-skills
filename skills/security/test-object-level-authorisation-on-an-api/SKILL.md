---
name: test-object-level-authorisation-on-an-api
description: Test an API's object-level authorisation by replaying one test account's requests against another account's object identifiers and recording exactly which cross-account reads and writes succeed. Use when the user wants to check whether an API enforces per-object ownership — the broken object level authorisation (BOLA/IDOR) class — on a system they own or are authorised to test.
domain: security
tags: [bola, idor, api-security, authorisation-testing]
triggers: ["test object level authorisation", "check an api for idor", "bola test with two accounts"]
---

# Test an API's object-level authorisation by replaying one test account's requests against another account's object identifiers and recording exactly which cross-account reads and writes succeed

## Purpose

Test an API's object-level authorisation by replaying one test account's requests against another account's object identifiers and recording exactly which cross-account reads and writes succeed.

## When to use

Use when the user wants to check whether an API enforces per-object ownership — the broken object level authorisation (BOLA/IDOR) class — on a system they own or are authorised to test.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Set up two test accounts, A and B, each with its own seeded objects, and record the identifiers and shapes of the objects each one owns.
2. Capture account A's legitimate requests for its own objects as the baseline for method, path, headers and body.
3. Replay each baseline request with account B's credentials, changing nothing else, and record the status and body of every response.
4. Repeat the replay in the other direction and across read, update and delete verbs, including nested endpoints and bulk endpoints that accept lists of identifiers.
5. Try the identifier variants the API might accept instead of the canonical one: sequential ids, identifiers from other features, and ids embedded in exports or shared links.
6. Classify a cross-account success as a confirmed authorisation failure only when B actually received or changed A's data, not when the response merely echoes the requested id.
7. Report each confirmed failure with the paired requests and responses, the data reached, and the ownership check the endpoint is missing.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `enforce-authorisation-on-an-api`
- `add-input-validation-to-an-endpoint`
- `design-a-privilege-escalation-test`

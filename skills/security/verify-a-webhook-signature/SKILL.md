---
name: verify-a-webhook-signature
description: Verify webhook signatures against the raw payload before trusting any callback. Use when the user needs an inbound webhook endpoint to authenticate sender messages.
domain: security
tags: [webhooks, signature-verification, replay-protection]
triggers: ["verify a webhook signature", "authenticate inbound webhook calls", "validate webhook hmac signatures"]
---

# Verify webhook signatures against the raw payload before trusting any callback

## Purpose

Verify webhook signatures against the raw payload before trusting any callback.

## When to use

Use when the user needs an inbound webhook endpoint to authenticate sender messages.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Read the exact raw request bytes and identify the timestamp, nonce, and signature headers.
2. Compute the digest with the endpoint's agreed algorithm and shared secret from a secret store.
3. Compare the expected and supplied digests in constant time and validate the timestamp window.
4. Reject invalid, expired, replayed, or unsupported-signature requests before parsing business data.
5. Add tests for valid signatures, altered payloads, expired timestamps, and replayed deliveries.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `hunt-verify-and-report-a-bug-bounty-finding`
- `add-security-headers-to-a-web-app`
- `build-a-vulnerability-management-program`

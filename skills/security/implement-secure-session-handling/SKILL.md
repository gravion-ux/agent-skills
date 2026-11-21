---
name: implement-secure-session-handling
description: Implement session handling that resists fixation, theft, and unintended privilege changes. Use when the user needs server-side or token sessions secured across authentication events.
domain: security
tags: [session-management, cookies, authentication]
triggers: ["implement secure session handling", "harden session cookies", "prevent session fixation in an app"]
---

# Implement session handling that resists fixation, theft, and unintended privilege changes

## Purpose

Implement session handling that resists fixation, theft, and unintended privilege changes.

## When to use

Use when the user needs server-side or token sessions secured across authentication events.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Generate a cryptographically random session identifier of at least 128 bits.
2. Rotate the session identifier after login, privilege changes, and password resets.
3. Bind the session to the authenticated user and store only a secure session cookie.
4. Set Secure, HttpOnly, SameSite, and explicit lifetime attributes on the cookie.
5. Invalidate sessions on logout, account disablement, and suspected session theft.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `implement-secure-file-uploads`
- `implement-data-retention-controls`
- `run-a-security-awareness-session`

---
name: add-security-headers-to-a-web-app
description: Add and verify browser security headers that constrain framing, content, and transport. Use when the user wants a web application to send a hardened set of browser security headers.
domain: security
tags: [security-headers, csp, browser-security]
triggers: ["add security headers to a web app", "configure csp and frame protection headers", "harden browser response headers"]
---

# Add and verify browser security headers that constrain framing, content, and transport

## Purpose

Add and verify browser security headers that constrain framing, content, and transport.

## When to use

Use when the user wants a web application to send a hardened set of browser security headers.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Choose a policy for content security, frame ancestors, MIME sniffing, and referrer data.
2. Set each header at the edge or application response layer with the narrowest compatible values.
3. Report violations without including credentials or full sensitive page content in the logs.
4. Run the application under its expected cross-origin and embedded-resource workflows.
5. Verify each header in browser developer tools and record any intentional policy exceptions.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `add-input-validation-to-an-endpoint`
- `prepare-for-a-security-questionnaire`
- `respond-to-a-leaked-secret`

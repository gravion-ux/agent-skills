---
name: harden-a-database-connection
description: Harden a database connection by requiring TLS, restricting the source and rotating the credential. Use when the user wants to protect the path between an application and its database.
domain: security
tags: [database, tls, credentials]
triggers: ["harden a database connection", "require tls to the database server", "restrict database access to app hosts"]
---

# Harden a database connection by requiring TLS, restricting the source and rotating the credential

## Purpose

Harden a database connection by requiring TLS, restricting the source and rotating the credential.

## When to use

Use when the user wants to protect the path between an application and its database.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Require a TLS connection and verify the server certificate in the client.
2. Restrict the allowed source addresses to the application hosts only.
3. Grant the application account only the schema permissions it uses.
4. Move the credential into a secret store and rotate it on a schedule.
5. Prove the old credential no longer connects after the rotation.

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
- `harden-a-kubernetes-cluster`
- `add-security-headers-to-a-web-app`

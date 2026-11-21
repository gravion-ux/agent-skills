---
name: lock-down-an-ssh-server
description: Harden an SSH server by disabling password logins, restricting root access and limiting sources. Use when the user wants to reduce the exposure of an SSH server on a reachable network.
domain: security
tags: [ssh, hardening, linux]
triggers: ["harden an ssh server", "disable ssh password login", "restrict ssh access to key based logins"]
---

# Harden an SSH server by disabling password logins, restricting root access and limiting sources

## Purpose

Harden an SSH server by disabling password logins, restricting root access and limiting sources.

## When to use

Use when the user wants to reduce the exposure of an SSH server on a reachable network.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Create a key based access path for a non-root account before changing the configuration.
2. Set PasswordAuthentication to no and PermitRootLogin to no in sshd_config.
3. Restrict AllowUsers to the named accounts that need shell access.
4. Restrict the firewall to the source ranges that require SSH access.
5. Open a second session and confirm the new rules before closing the old one.

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
- `enforce-authorisation-on-an-api`
- `enforce-mfa-for-an-organisation`

---
name: triage-a-dependency-confusion-risk
description: Triage a dependency-confusion risk by inventorying internal package names, checking whether they resolve on public registries, and closing the namespace gaps that let an attacker publish a malicious namesake. Use when the user suspects their build pulls internal packages whose names could be claimed or shadowed on a public package registry.
domain: security
tags: [dependency-confusion, supply-chain, package-registry, build-security]
triggers: ["dependency confusion risk", "internal package name on a public registry", "could someone shadow our private packages"]
---

# Triage a dependency-confusion risk by inventorying internal package names, checking whether they resolve on public registries, and closing the namespace gaps that let an attacker publish a malicious namesake

## Purpose

Triage a dependency-confusion risk by inventorying internal package names, checking whether they resolve on public registries, and closing the namespace gaps that let an attacker publish a malicious namesake.

## When to use

Use when the user suspects their build pulls internal packages whose names could be claimed or shadowed on a public package registry.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Inventory every internal package name the build resolves, from lockfiles, private registry configuration and CI build logs.
2. Check each internal name against the public registries the toolchain uses and record whether the name is unclaimed, claimed by the organisation, or already published by a stranger.
3. Determine which registry wins when both a private and a public source offer the same name, using the resolver's actual precedence and version-selection rules.
4. Flag any case where a higher public version would outrank the internal one, because that is the exact path a confusion attack takes.
5. Close the gaps: scope or namespace internal names, pin the private registry for those scopes, and claim the public names before someone else does.
6. Add a build check that fails when an internal package name resolves from a public source, and alert on new public publications of watched names.
7. Record the verdict per package name — safe, exposed or already shadowed — with the registry evidence behind each one.

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
- `triage-a-security-finding`
- `add-security-headers-to-a-web-app`

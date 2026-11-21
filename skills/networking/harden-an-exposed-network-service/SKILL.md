---
name: harden-an-exposed-network-service
description: Harden an internet-facing service by shrinking its exposure and verifying each control. Use when the user needs to reduce attack surface on a service reachable from an untrusted network.
domain: networking
tags: [hardening, exposure, security, tls]
triggers: ["harden an exposed network service", "reduce the attack surface of this public service", "secure an internet facing network endpoint"]
---

# Harden an internet-facing service by shrinking its exposure and verifying each control

## Purpose

Harden an internet-facing service by shrinking its exposure and verifying each control.

## When to use

Use when the user needs to reduce attack surface on a service reachable from an untrusted network.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Inventory exposed listeners, versions, certificates, authentication, and current firewall scope.
2. Remove unused listeners and restrict each required service to the narrowest approved source.
3. Verify TLS configuration, authentication strength, rate limits, and bounded timeouts.
4. Scan the exposed endpoint from an external vantage point and confirm only intended ports answer.
5. Record every control applied, the scan evidence, and any risk accepted with an owner.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `configure-ipv6-for-a-service`
- `document-a-network-topology`
- `establish-an-ssh-tunnel`

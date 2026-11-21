---
name: configure-ipv6-for-a-service
description: Enable IPv6 for a service and verify dual-stack reachability without disrupting IPv4. Use when the user needs a service to accept traffic over IPv6 alongside existing IPv4 access.
domain: networking
tags: [ipv6, dual-stack, routing, configuration]
triggers: ["configure ipv6 for a service", "add ipv6 support to this host", "make this service reachable over ipv6"]
---

# Enable IPv6 for a service and verify dual-stack reachability without disrupting IPv4

## Purpose

Enable IPv6 for a service and verify dual-stack reachability without disrupting IPv4.

## When to use

Use when the user needs a service to accept traffic over IPv6 alongside existing IPv4 access.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Confirm the assigned IPv6 prefix, address allocation method, and authoritative DNS records.
2. Configure interface addressing, routing, and any required stateful or stateless translation settings.
3. Publish AAAA records and confirm the service listens on the intended IPv6 addresses.
4. Test IPv6 and IPv4 connectivity from both ends while recording negotiated addresses and latency.
5. Document the dual-stack configuration, firewall intent, and fallback behaviour if IPv6 fails.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `configure-a-firewall-rule`
- `configure-a-load-balancer-health-check`
- `configure-a-reverse-proxy`

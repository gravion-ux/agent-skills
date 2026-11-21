---
name: configure-a-firewall-rule
description: Add a narrowly scoped firewall rule and prove it blocks only the intended traffic. Use when the user needs controlled inbound or outbound access through a host or network firewall.
domain: networking
tags: [firewall, access-control, ports, security]
triggers: ["configure a firewall rule", "allow this port through the firewall", "block or permit traffic with a firewall rule"]
---

# Add a narrowly scoped firewall rule and prove it blocks only the intended traffic

## Purpose

Add a narrowly scoped firewall rule and prove it blocks only the intended traffic.

## When to use

Use when the user needs controlled inbound or outbound access through a host or network firewall.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Write the source, destination, port, protocol, direction, and business reason for the rule.
2. Check the current rule set for an existing match and identify any broader rule that overrides it.
3. Add the narrowest scoped rule and confirm it is enabled in the active configuration.
4. Test permitted and denied traffic from both ends while confirming logs show the expected decisions.
5. Record the rule identifier, verification results, and an expiry or review date for temporary access.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `configure-a-load-balancer-health-check`
- `configure-a-reverse-proxy`
- `configure-ipv6-for-a-service`

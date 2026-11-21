---
name: route-traffic-between-environments
description: Route traffic between environments through an explicit, logged, and reversible path. Use when the user needs controlled connectivity between development, test, and production networks.
domain: networking
tags: [routing, environments, access-control, network-policy]
triggers: ["route traffic between environments", "connect the test environment to production", "allow traffic from staging to prod"]
---

# Route traffic between environments through an explicit, logged, and reversible path

## Purpose

Route traffic between environments through an explicit, logged, and reversible path.

## When to use

Use when the user needs controlled connectivity between development, test, and production networks.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Document the source and destination environments, specific flows, and business justification.
2. Select the routing mechanism, trust boundaries, and enforcement point for the crossing.
3. Restrict access to the named hosts and ports with default-deny behaviour elsewhere.
4. Verify the permitted flows and confirm denied flows are logged and blocked.
5. Record the route, approving owner, expiry date, and the steps to remove the path.

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

---
name: migrate-a-service-to-a-new-load-balancer
description: Move a service to a new load balancer with reversible traffic and health verification. Use when the user must migrate live traffic from one load balancer to a replacement.
domain: networking
tags: [load-balancer, migration, traffic-shift, availability]
triggers: ["migrate a service to a new load balancer", "move traffic to a replacement load balancer", "cut over this service to the new balancer"]
---

# Move a service to a new load balancer with reversible traffic and health verification

## Purpose

Move a service to a new load balancer with reversible traffic and health verification.

## When to use

Use when the user must migrate live traffic from one load balancer to a replacement.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Inventory listeners, certificates, backends, health checks, timeouts, and traffic policies on the old balancer.
2. Build the replacement with matching routing and verified certificate configuration.
3. Test the new balancer directly with health checks and representative requests.
4. Shift a small share of traffic, compare health and latency, then increase the share in stages.
5. Restore the old balancer as standby until the change is confirmed and schedule its retirement.

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
- `configure-ipv6-for-a-service`
- `set-up-a-service-mesh-sidecar`

---
name: configure-a-load-balancer-health-check
description: Configure a load-balancer health check that reflects real service readiness. Use when the user needs a backend added, removed, or corrected based on health-check behaviour.
domain: networking
tags: [load-balancer, health-check, backend, availability]
triggers: ["configure a load balancer health check", "set up backend health checks", "why is my load balancer marking backends unhealthy"]
---

# Configure a load-balancer health check that reflects real service readiness

## Purpose

Configure a load-balancer health check that reflects real service readiness.

## When to use

Use when the user needs a backend added, removed, or corrected based on health-check behaviour.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Identify the backend address, port, protocol, and the signal the application exposes for readiness.
2. Choose the health endpoint, interval, timeout, and unhealthy threshold for the service.
3. Apply the check to the load-balancer backend pool without exposing the check endpoint publicly.
4. Verify checks pass and fail as expected while watching traffic distribution across healthy backends.
5. Record the check configuration, observed status transitions, and any deliberate exclusions.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `migrate-a-service-to-a-new-load-balancer`
- `configure-a-firewall-rule`
- `configure-a-reverse-proxy`

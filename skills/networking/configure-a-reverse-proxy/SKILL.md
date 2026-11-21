---
name: configure-a-reverse-proxy
description: Configure a reverse proxy with upstream health, TLS handling, and bounded request limits. Use when the user needs inbound traffic routed through a proxy to one or more backend services.
domain: networking
tags: [reverse-proxy, tls, routing, deployment]
triggers: ["configure a reverse proxy", "set up proxy routing to the backend", "add a reverse proxy in front of this service"]
---

# Configure a reverse proxy with upstream health, TLS handling, and bounded request limits

## Purpose

Configure a reverse proxy with upstream health, TLS handling, and bounded request limits.

## When to use

Use when the user needs inbound traffic routed through a proxy to one or more backend services.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Record the public hostname, listening port, upstream addresses, and expected request protocol.
2. Set TLS material, certificate hostname, and proxy headers to match the client contract.
3. Configure upstream health checks, request size limits, and explicit timeouts.
4. Verify host-based routing and upstream selection from outside the proxy network.
5. Document the routes, headers, limits, and the change window used for activation.

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
- `configure-ipv6-for-a-service`

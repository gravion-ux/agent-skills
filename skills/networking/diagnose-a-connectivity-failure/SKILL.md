---
name: diagnose-a-connectivity-failure
description: Isolate the failing hop in a network path and document the exact cause. Use when the user cannot reach a service and needs the broken hop identified.
domain: networking
tags: [connectivity, troubleshooting, network-path, diagnostics]
triggers: ["diagnose a connectivity failure", "find the broken network hop", "why can I not reach this host"]
---

# Isolate the failing hop in a network path and document the exact cause

## Purpose

Isolate the failing hop in a network path and document the exact cause.

## When to use

Use when the user cannot reach a service and needs the broken hop identified.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Record the source host, destination host, port, and protocol of the failed connection.
2. Compare the path from both ends using ping, traceroute, and TCP connection attempts.
3. Test DNS resolution, TLS negotiation, and firewall acceptance at the failing hop.
4. Identify the first hop that drops or rejects traffic and note its observed response.
5. Write the diagnosis with commands, outputs, and the smallest safe remediation to try.

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

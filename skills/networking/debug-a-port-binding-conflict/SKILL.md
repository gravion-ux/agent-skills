---
name: debug-a-port-binding-conflict
description: Resolve a port binding conflict by identifying the process holding the listener. Use when the user cannot start a service because another process already owns its port.
domain: networking
tags: [port-conflict, listeners, processes, debugging]
triggers: ["debug a port binding conflict", "address already in use on this port", "find which process is listening on the port"]
---

# Resolve a port binding conflict by identifying the process holding the listener

## Purpose

Resolve a port binding conflict by identifying the process holding the listener.

## When to use

Use when the user cannot start a service because another process already owns its port.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Record the intended host, port, protocol, and bind address for the failing service.
2. List all listeners on that port and identify the owning process on each relevant host.
3. Confirm the other process is legitimate and record its purpose before stopping anything.
4. Stop the conflicting process or move the new service to an approved free port.
5. Verify the intended listener starts correctly and record both process identities for support.

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

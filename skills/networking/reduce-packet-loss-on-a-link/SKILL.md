---
name: reduce-packet-loss-on-a-link
description: Reduce packet loss on a link by correcting its physical, capacity, or queueing cause. Use when the user measures packet loss on a link and needs the loss mechanism corrected.
domain: networking
tags: [packet-loss, link-quality, capacity, troubleshooting]
triggers: ["reduce packet loss on a link", "fix dropping packets on this connection", "diagnose interface packet loss"]
---

# Reduce packet loss on a link by correcting its physical, capacity, or queueing cause

## Purpose

Reduce packet loss on a link by correcting its physical, capacity, or queueing cause.

## When to use

Use when the user measures packet loss on a link and needs the loss mechanism corrected.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Measure loss at both ends and compare interface errors, drops, queue depth, and capacity use.
2. Check cabling, optics, duplex settings, and negotiated link parameters for physical faults.
3. Inspect congestion, bufferbloat, queue policy, and microburst behaviour under load.
4. Apply one scoped correction and repeat the same loss and latency measurements.
5. Record the cause, applied change, before and after results, and the rollback procedure.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `read-a-packet-capture`
- `configure-a-firewall-rule`
- `configure-a-load-balancer-health-check`

---
name: plan-a-network-capacity-upgrade
description: Plan a network capacity upgrade using measured demand, bottlenecks, and staged thresholds. Use when the user needs to size and sequence an upgrade before links or devices reach their limits.
domain: networking
tags: [capacity, upgrade, scaling, planning]
triggers: ["plan a network capacity upgrade", "size an upgrade for link utilisation", "our network needs more bandwidth capacity"]
---

# Plan a network capacity upgrade using measured demand, bottlenecks, and staged thresholds

## Purpose

Plan a network capacity upgrade using measured demand, bottlenecks, and staged thresholds.

## When to use

Use when the user needs to size and sequence an upgrade before links or devices reach their limits.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Collect utilisation, latency, loss, growth, and capacity data for each critical path.
2. Identify the first component projected to saturate and estimate the time until it does.
3. Compare upgrade options against required throughput, growth headroom, and failure tolerance.
4. Stage the upgrade with thresholds for validation, rollback, and full traffic adoption.
5. Document the chosen option, cost, dependencies, acceptance metrics, and review date.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `plan-a-network-segmentation`
- `document-a-network-topology`
- `configure-a-firewall-rule`

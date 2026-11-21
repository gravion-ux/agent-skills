---
name: plan-a-network-segmentation
description: Design network segments with trust boundaries, access paths, and enforced controls. Use when the user needs to divide a flat network into controlled zones for different trust levels.
domain: networking
tags: [segmentation, trust-boundaries, firewall, architecture]
triggers: ["plan a network segmentation", "design network zones and trust boundaries", "segment this flat network"]
---

# Design network segments with trust boundaries, access paths, and enforced controls

## Purpose

Design network segments with trust boundaries, access paths, and enforced controls.

## When to use

Use when the user needs to divide a flat network into controlled zones for different trust levels.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Inventory systems, data sensitivity, owners, and the required flows for each zone.
2. Group assets into zones and define which flows are allowed, denied, or monitored between them.
3. Assign enforcement points, default-deny boundaries, and monitoring requirements per crossing.
4. Document address space, routing, firewall intent, and accountable owner for every segment.
5. Validate the design against each required flow and obtain approval before enforcing rules.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `plan-a-network-capacity-upgrade`
- `document-a-network-topology`
- `configure-a-firewall-rule`

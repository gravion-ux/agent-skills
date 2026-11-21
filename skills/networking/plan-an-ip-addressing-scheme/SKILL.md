---
name: plan-an-ip-addressing-scheme
description: Plan an IP addressing scheme with unambiguous subnets, growth room, and ownership records. Use when the user needs to allocate address space across sites, segments, or environments.
domain: networking
tags: [ip-addressing, subnetting, addressing, planning]
triggers: ["plan an ip addressing scheme", "design subnet ranges for our sites", "allocate ip address space by segment"]
---

# Plan an IP addressing scheme with unambiguous subnets, growth room, and ownership records

## Purpose

Plan an IP addressing scheme with unambiguous subnets, growth room, and ownership records.

## When to use

Use when the user needs to allocate address space across sites, segments, or environments.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. List the locations, segments, environments, and expected device counts that need addresses.
2. Choose prefix sizes and reserve blocks for growth, infrastructure, and special-purpose use.
3. Map every block to its segment, purpose, owner, and allocation status.
4. Check the plan for overlaps, exhausted boundaries, and consistency with existing routing.
5. Publish the address inventory and register the plan before assigning any production addresses.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `establish-an-ssh-tunnel`
- `harden-an-exposed-network-service`
- `plan-a-network-capacity-upgrade`

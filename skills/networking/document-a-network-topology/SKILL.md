---
name: document-a-network-topology
description: Document a network topology that maps links, boundaries, owners, and verified paths. Use when the user needs an accurate record of how network components connect in production.
domain: networking
tags: [topology, documentation, network-map, inventory]
triggers: ["document a network topology", "create a diagram of our network", "map the connections between network devices"]
---

# Document a network topology that maps links, boundaries, owners, and verified paths

## Purpose

Document a network topology that maps links, boundaries, owners, and verified paths.

## When to use

Use when the user needs an accurate record of how network components connect in production.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Collect the authoritative device inventory, interface names, addressing, and ownership records.
2. Map physical and logical links, including gateways, tunnels, firewalls, and trust boundaries.
3. Trace each critical application path and record the verified route between its endpoints.
4. Annotate the diagram with protocols, ports, trust levels, and monitoring coverage.
5. Review the topology with system owners and store it with its review date and source records.

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
- `plan-a-network-segmentation`
- `configure-a-firewall-rule`

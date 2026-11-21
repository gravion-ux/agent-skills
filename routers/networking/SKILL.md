---
name: router-networking
description: Route work in the Networking and connectivity domain to the right leaf skill. Use when a task clearly belongs to networking.
domain: networking
tags: [router, routing, networking]
triggers: ["route a networking task", "which networking skill should I use"]
---

# Networking and connectivity router

## Purpose

List every leaf skill in the networking domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside networking and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `configure-a-firewall-rule` | Use when the user needs controlled inbound or outbound access through a host or network firewall. |
| `configure-a-load-balancer-health-check` | Use when the user needs a backend added, removed, or corrected based on health-check behaviour. |
| `configure-a-reverse-proxy` | Use when the user needs inbound traffic routed through a proxy to one or more backend services. |
| `configure-ipv6-for-a-service` | Use when the user needs a service to accept traffic over IPv6 alongside existing IPv4 access. |
| `debug-a-port-binding-conflict` | Use when the user cannot start a service because another process already owns its port. |
| `design-a-multicast-workflow` | Use when the user needs one-to-many distribution across a network with defined group membership. |
| `diagnose-a-connectivity-failure` | Use when the user cannot reach a service and needs the broken hop identified. |
| `document-a-network-topology` | Use when the user needs an accurate record of how network components connect in production. |
| `establish-an-ssh-tunnel` | Use when the user needs a temporary encrypted path to reach a service on a remote network. |
| `fix-a-dns-resolution-problem` | Use when the user gets wrong, missing, or inconsistent DNS answers for a hostname. |
| `harden-an-exposed-network-service` | Use when the user needs to reduce attack surface on a service reachable from an untrusted network. |
| `migrate-a-service-to-a-new-load-balancer` | Use when the user must migrate live traffic from one load balancer to a replacement. |
| `monitor-network-availability` | Use when the user needs recurring evidence that a network path or service stays reachable. |
| `plan-a-network-capacity-upgrade` | Use when the user needs to size and sequence an upgrade before links or devices reach their limits. |
| `plan-a-network-segmentation` | Use when the user needs to divide a flat network into controlled zones for different trust levels. |
| `plan-an-ip-addressing-scheme` | Use when the user needs to allocate address space across sites, segments, or environments. |
| `read-a-packet-capture` | Use when the user has a capture file and needs connection behaviour explained from packet evidence. |
| `reduce-packet-loss-on-a-link` | Use when the user measures packet loss on a link and needs the loss mechanism corrected. |
| `renew-an-expired-certificate` | Use when the user must recover a service whose TLS certificate has expired. |
| `route-traffic-between-environments` | Use when the user needs controlled connectivity between development, test, and production networks. |
| `set-up-a-service-mesh-sidecar` | Use when the user needs a workload connected to a service mesh for routing, telemetry, or policy. |
| `set-up-a-tls-certificate` | Use when the user needs to issue and deploy a certificate for a reachable TLS service. |
| `set-up-a-vpn-for-remote-access` | Use when the user needs authorised remote users to reach private network resources. |
| `test-end-to-end-network-connectivity` | Use when the user needs proof that a complete network path works between two endpoints. |
| `troubleshoot-a-latency-spike` | Use when the user observes a latency increase on a path and needs the responsible segment named. |
| `tune-tcp-congestion-control` | Use when the user wants to tune throughput or latency on a known client and server path. |

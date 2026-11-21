---
name: set-up-a-service-mesh-sidecar
description: Deploy a service-mesh sidecar with scoped traffic policy and verified service discovery. Use when the user needs a workload connected to a service mesh for routing, telemetry, or policy.
domain: networking
tags: [service-mesh, sidecar, traffic-policy, deployment]
triggers: ["set up a service mesh sidecar", "inject the sidecar proxy into this workload", "add this service to our service mesh"]
---

# Deploy a service-mesh sidecar with scoped traffic policy and verified service discovery

## Purpose

Deploy a service-mesh sidecar with scoped traffic policy and verified service discovery.

## When to use

Use when the user needs a workload connected to a service mesh for routing, telemetry, or policy.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Confirm the mesh control plane, workload namespace, identity, and required traffic policies.
2. Inject the sidecar with explicit proxy settings, resource limits, and egress restrictions.
3. Verify service discovery, identity certificates, and health registration for the workload.
4. Exercise inbound and outbound traffic and confirm the expected telemetry is collected.
5. Document the sidecar configuration, policy names, and rollback steps for the workload.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `set-up-a-tls-certificate`
- `set-up-a-vpn-for-remote-access`
- `configure-ipv6-for-a-service`

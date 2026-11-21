---
name: set-up-a-vpn-for-remote-access
description: Establish a secure remote-access VPN and verify tunnel reachability from a client. Use when the user needs authorised remote users to reach private network resources.
domain: networking
tags: [vpn, remote-access, tunneling, security]
triggers: ["set up a vpn for remote access", "configure vpn client connectivity", "give remote users access to the private network"]
---

# Establish a secure remote-access VPN and verify tunnel reachability from a client

## Purpose

Establish a secure remote-access VPN and verify tunnel reachability from a client.

## When to use

Use when the user needs authorised remote users to reach private network resources.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Document the required client subnets, routes, authentication method, and trust boundaries.
2. Select tunnel and transport parameters that match the target network and threat model.
3. Issue scoped client credentials and enable logging without weakening existing firewall controls.
4. Connect a test client and verify assigned addressing, selected routes, and DNS behaviour.
5. Test resource reachability from both the client and the server side, then record the configuration.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `set-up-a-service-mesh-sidecar`
- `set-up-a-tls-certificate`
- `configure-ipv6-for-a-service`

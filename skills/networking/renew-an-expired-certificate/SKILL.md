---
name: renew-an-expired-certificate
description: Replace an expired TLS certificate without dropping active connections. Use when the user must recover a service whose TLS certificate has expired.
domain: networking
tags: [tls, certificates, renewal, recovery]
triggers: ["renew an expired certificate", "replace an expired tls certificate", "fix a certificate expiry outage"]
---

# Replace an expired TLS certificate without dropping active connections

## Purpose

Replace an expired TLS certificate without dropping active connections.

## When to use

Use when the user must recover a service whose TLS certificate has expired.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Confirm the expiry, issuer, hostnames, and private key still match the deployed certificate.
2. Obtain a replacement certificate and validate its chain before changing the running service.
3. Stage the new key and chain in a temporary path with restricted permissions.
4. Reload the TLS service and verify the new certificate from an external client.
5. Remove the retired key material and update the renewal record with the next expiry date.

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
- `plan-an-ip-addressing-scheme`

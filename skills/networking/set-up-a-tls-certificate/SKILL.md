---
name: set-up-a-tls-certificate
description: Install a TLS certificate and verify its chain, hostname, and renewal dates. Use when the user needs to issue and deploy a certificate for a reachable TLS service.
domain: networking
tags: [tls, certificates, encryption, deployment]
triggers: ["set up a tls certificate", "install a certificate for this service", "issue and deploy a tls certificate"]
---

# Install a TLS certificate and verify its chain, hostname, and renewal dates

## Purpose

Install a TLS certificate and verify its chain, hostname, and renewal dates.

## When to use

Use when the user needs to issue and deploy a certificate for a reachable TLS service.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Confirm the service hostname, certificate authority, key type, and required subject names.
2. Generate a private key with restricted file permissions and keep it out of source control.
3. Request the certificate and install the full chain with the private key on the service host.
4. Verify hostname matching, issuer, expiry, and protocol support from a separate client.
5. Record the certificate location, issuer, expiry date, and owner responsible for renewal.

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
- `set-up-a-vpn-for-remote-access`
- `configure-a-firewall-rule`

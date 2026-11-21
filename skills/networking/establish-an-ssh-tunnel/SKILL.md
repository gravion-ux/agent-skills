---
name: establish-an-ssh-tunnel
description: Create a bounded SSH tunnel and confirm which hosts and ports it exposes. Use when the user needs a temporary encrypted path to reach a service on a remote network.
domain: networking
tags: [ssh, tunneling, remote-access, port-forwarding]
triggers: ["establish an ssh tunnel", "set up an ssh port forward", "tunnel through the jump host to this service"]
---

# Create a bounded SSH tunnel and confirm which hosts and ports it exposes

## Purpose

Create a bounded SSH tunnel and confirm which hosts and ports it exposes.

## When to use

Use when the user needs a temporary encrypted path to reach a service on a remote network.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Identify the jump host, target host, remote port, and local listener needed for the task.
2. Confirm the SSH key, host-key fingerprint, and account have approved access.
3. Start the tunnel with explicit bind address, port, and keepalive settings.
4. Verify the local listener forwards to the intended service and record the active session.
5. Close the tunnel when work ends and revoke any temporary forwarding permission.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `harden-an-exposed-network-service`
- `plan-an-ip-addressing-scheme`
- `renew-an-expired-certificate`

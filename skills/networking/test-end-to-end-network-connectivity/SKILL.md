---
name: test-end-to-end-network-connectivity
description: Run a documented end-to-end connectivity test across every hop and transport layer. Use when the user needs proof that a complete network path works between two endpoints.
domain: networking
tags: [connectivity, testing, end-to-end, verification]
triggers: ["test end to end network connectivity", "run a full path connectivity test", "verify connectivity across the whole network path"]
---

# Run a documented end-to-end connectivity test across every hop and transport layer

## Purpose

Run a documented end-to-end connectivity test across every hop and transport layer.

## When to use

Use when the user needs proof that a complete network path works between two endpoints.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Define the source, destination, port, protocol, expected response, and success threshold.
2. Test DNS resolution, TCP or UDP reachability, TLS negotiation, and application exchange in order.
3. Repeat the test from both ends and record timings, errors, and the tools used.
4. Confirm firewall and proxy behaviour from logs rather than only from client output.
5. Publish the test matrix with pass or fail status, timing baselines, and any failed hop.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `diagnose-a-connectivity-failure`
- `document-a-network-topology`
- `harden-an-exposed-network-service`

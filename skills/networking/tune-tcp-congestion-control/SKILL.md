---
name: tune-tcp-congestion-control
description: Select and validate a TCP congestion-control setting for a measured network path. Use when the user wants to tune throughput or latency on a known client and server path.
domain: networking
tags: [tcp, congestion-control, throughput, performance]
triggers: ["tune tcp congestion control", "change the tcp congestion algorithm", "optimise tcp throughput on this link"]
---

# Select and validate a TCP congestion-control setting for a measured network path

## Purpose

Select and validate a TCP congestion-control setting for a measured network path.

## When to use

Use when the user wants to tune throughput or latency on a known client and server path.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Measure baseline throughput, round-trip time, retransmission rate, and link utilisation.
2. List the congestion-control algorithms available on both endpoints and record their defaults.
3. Change one algorithm setting on a test path and repeat the same measurements.
4. Compare latency, throughput, and retransmissions against the baseline across representative traffic.
5. Apply the winning setting only to the intended scope and document the rollback value.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `configure-a-firewall-rule`
- `configure-a-load-balancer-health-check`
- `configure-a-reverse-proxy`

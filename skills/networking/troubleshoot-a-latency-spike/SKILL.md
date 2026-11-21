---
name: troubleshoot-a-latency-spike
description: Locate the source of a latency spike by comparing path measurements across endpoints. Use when the user observes a latency increase on a path and needs the responsible segment named.
domain: networking
tags: [latency, performance, monitoring, troubleshooting]
triggers: ["troubleshoot a latency spike", "find the source of network delay", "why did ping latency jump"]
---

# Locate the source of a latency spike by comparing path measurements across endpoints

## Purpose

Locate the source of a latency spike by comparing path measurements across endpoints.

## When to use

Use when the user observes a latency increase on a path and needs the responsible segment named.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Capture baseline latency, loss, and throughput from both ends of the affected path.
2. Compare timestamped latency samples across the link, intermediate hops, and application.
3. Check saturation, retransmissions, routing changes, and remote host resource pressure.
4. Identify the interval where the delay begins and the hop or component that correlates with it.
5. Report the evidence, likely cause, and a mitigation or rollback for the affected segment.

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

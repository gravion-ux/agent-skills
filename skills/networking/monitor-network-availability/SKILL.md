---
name: monitor-network-availability
description: Monitor network availability with scheduled probes and actionable failure thresholds. Use when the user needs recurring evidence that a network path or service stays reachable.
domain: networking
tags: [monitoring, availability, probes, alerting]
triggers: ["monitor network availability", "set up network uptime monitoring", "alert me when this network path goes down"]
---

# Monitor network availability with scheduled probes and actionable failure thresholds

## Purpose

Monitor network availability with scheduled probes and actionable failure thresholds.

## When to use

Use when the user needs recurring evidence that a network path or service stays reachable.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Select the critical endpoints, ports, protocols, and check intervals for the monitored path.
2. Configure probes that record success, latency, and failure type for each target.
3. Set thresholds and notification routing that distinguish brief blips from sustained outages.
4. Test the monitor by introducing a controlled failure on a non-production target.
5. Document the dashboard, alert owners, and the procedure used to triage each alert.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `document-a-network-topology`
- `harden-an-exposed-network-service`
- `plan-a-network-capacity-upgrade`

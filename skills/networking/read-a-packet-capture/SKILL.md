---
name: read-a-packet-capture
description: Read a packet capture to find handshake failures, retransmissions, and dropped traffic. Use when the user has a capture file and needs connection behaviour explained from packet evidence.
domain: networking
tags: [packet-capture, tcp, diagnostics, traffic-analysis]
triggers: ["read a packet capture", "analyse this pcap file", "inspect captured network packets"]
---

# Read a packet capture to find handshake failures, retransmissions, and dropped traffic

## Purpose

Read a packet capture to find handshake failures, retransmissions, and dropped traffic.

## When to use

Use when the user has a capture file and needs connection behaviour explained from packet evidence.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Filter the capture to the affected host pair, port, and protocol before reviewing packets.
2. Follow the TCP or UDP handshake and record missing or out-of-order packets.
3. Measure retransmissions, retransmit timeouts, and the observed round-trip latency.
4. Inspect DNS, TLS, or application exchanges when the transport layer completed normally.
5. Report the first anomalous packet with its timestamp, direction, and supporting packet numbers.

## Output contract

A reachable, diagnosed and documented network path with the failing hop named.

## Validation checklist

- [ ] The path was tested from both ends
- [ ] DNS, TLS and firewall behaviour are recorded
- [ ] Timeouts and retries are bounded

## Safety notes

Never open a public port or weaken a firewall rule without explicit approval.

## Related skills

- `reduce-packet-loss-on-a-link`
- `configure-a-firewall-rule`
- `configure-a-load-balancer-health-check`

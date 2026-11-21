---
name: fix-a-dns-resolution-problem
description: Repair a DNS resolution fault and confirm the corrected answer from every resolver. Use when the user gets wrong, missing, or inconsistent DNS answers for a hostname.
domain: networking
tags: [dns, resolution, nameservers, troubleshooting]
triggers: ["fix a dns resolution problem", "dns lookup returns the wrong address", "troubleshoot hostname resolution"]
---

# Repair a DNS resolution fault and confirm the corrected answer from every resolver

## Purpose

Repair a DNS resolution fault and confirm the corrected answer from every resolver.

## When to use

Use when the user gets wrong, missing, or inconsistent DNS answers for a hostname.

## When NOT to use

Do not use this for application-level endpoint design; use api-design instead.

## Inputs required

- The endpoints, protocols and ports involved
- The network path and trust boundaries
- The latency and throughput targets

## Procedure

1. Capture the failing lookup, resolver addresses, record type, and expected answer.
2. Query the authoritative nameservers directly and compare their answers with the recursive result.
3. Check TTLs, delegation, split-horizon views, and stale cache entries for the affected record.
4. Correct the authoritative record or resolver configuration and flush only the affected cache.
5. Verify the answer, TTL, and record type from both ends of the application path.

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

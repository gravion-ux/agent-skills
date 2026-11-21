---
name: router-observability
description: Route work in the Observability and operations domain to the right leaf skill. Use when a task clearly belongs to observability.
domain: observability
tags: [router, routing, observability]
triggers: ["route a observability task", "which observability skill should I use"]
---

# Observability and operations router

## Purpose

List every leaf skill in the observability domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside observability and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `add-a-health-and-readiness-probe` | Use when the user needs platform probes for a deployed service. |
| `add-a-synthetic-check-for-a-critical-path` | Use when the user needs continuous proof that a critical journey still works. |
| `add-structured-request-logging` | Use when the user needs searchable logs for incoming service requests. |
| `audit-a-service-for-missing-telemetry` | Use when the user needs to find missing observability coverage in an existing service. |
| `build-a-capacity-forecast-from-metrics` | Use when the user needs to estimate future resource needs from observed telemetry. |
| `build-a-latency-dashboard` | Use when the user needs a shared view of request latency across a service. |
| `build-a-usage-report-for-a-team` | Use when the user needs recurring evidence of how a team or feature is being used. |
| `build-an-error-rate-alert` | Use when the user needs a threshold alert for rising request or job failures. |
| `correlate-logs-metrics-and-traces` | Use when the user needs to connect multiple telemetry types for one incident. |
| `create-a-log-search-for-a-failure` | Use when the user needs to find request failures in a log service. |
| `define-service-level-indicators` | Use when the user needs to define measurable reliability indicators for a service. |
| `detect-a-silent-failure` | Use when the user needs to find a failure that logs no errors but loses work. |
| `implement-a-distributed-trace` | Use when the user needs to follow a request across multiple services. |
| `instrument-a-code-path-with-metrics` | Use when the user needs visibility into how often and how slowly a code path runs. |
| `instrument-a-queue-consumer` | Use when the user needs visibility into message consumption and backlog health. |
| `measure-a-background-job-success-rate` | Use when the user needs a reliable success rate for scheduled or asynchronous jobs. |
| `measure-tail-latency-not-just-averages` | Use when the user needs to find slow requests hidden by average latency metrics. |
| `plan-an-on-call-dashboard` | Use when the user needs to prepare the primary dashboard used during on-call shifts. |
| `report-on-the-reliability-of-a-dependency` | Use when the user needs a current reliability assessment for an upstream or downstream service. |
| `retire-a-noisy-alert` | Use when the user needs to remove an alert that fires too often to be useful. |
| `set-up-a-dead-letter-alert` | Use when the user needs visibility into messages routed to a dead-letter queue. |
| `trace-a-slow-third-party-call` | Use when the user needs to find where time is lost in an external dependency call. |
| `track-a-request-across-services` | Use when the user needs to follow a specific request through downstream services. |
| `write-a-service-level-objective` | Use when the user needs to set a reliability target for a service or API. |
| `write-an-alert-that-a-human-can-act-on` | Use when the user needs to reduce alert fatigue and make notifications actionable. |
| `write-an-slo-burn-rate-alert` | Use when the user needs an alert tied to service level objective consumption. |

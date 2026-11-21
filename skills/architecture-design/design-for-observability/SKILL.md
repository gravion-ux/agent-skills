---
name: design-for-observability
description: Define observability signals, service objectives, dashboards, and actionable alerts for a system. Use when the user needs a monitoring and troubleshooting plan for a service or architecture.
domain: architecture-design
tags: [observability, service-objectives, alerting]
triggers: ["system observability design", "add service monitoring", "architecture alerting plan"]
---

# Define observability signals, service objectives, dashboards, and actionable alerts for a system

## Purpose

Define observability signals, service objectives, dashboards, and actionable alerts for a system.

## When to use

Use when the user needs a monitoring and troubleshooting plan for a service or architecture.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Map each critical user journey to its service-level indicators and error-budget owner.
2. Instrument structured logs, metrics, and traces with shared identifiers across boundaries.
3. Define thresholds, evaluation windows, severity, and routing for each actionable alert.
4. Create dashboards that show demand, errors, latency, saturation, and dependency health.
5. Link every alert to a runbook with diagnosis, containment, and recovery steps.
6. Record observability assumptions, blind spots, and review dates with the operating team.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `design-a-data-model-for-a-feature`
- `design-a-batch-processing-pipeline`
- `design-a-caching-layer`

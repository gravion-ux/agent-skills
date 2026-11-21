---
name: router-architecture-design
description: Route work in the Architecture and system design domain to the right leaf skill. Use when a task clearly belongs to architecture-design.
domain: architecture-design
tags: [router, routing, architecture-design]
triggers: ["route a architecture-design task", "which architecture-design skill should I use"]
---

# Architecture and system design router

## Purpose

List every leaf skill in the architecture-design domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside architecture-design and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `assess-a-technical-proposal` | Use when the user needs a critical architecture review of a proposed technical change. |
| `choose-a-message-queue` | Use when the user needs to select messaging infrastructure for a system workflow. |
| `choose-between-a-modular-monolith-and-microservices` | Use when the user must choose a service architecture for a new or evolving application. |
| `define-service-boundaries` | Use when the user needs to split a system into cohesive, independently owned services. |
| `design-a-batch-processing-pipeline` | Use when the user needs to process large input volumes reliably through scheduled or streaming jobs. |
| `design-a-caching-layer` | Use when the user needs to introduce caching into a data-access or service path. |
| `design-a-data-model-for-a-feature` | Use when the user needs a concrete data model for a new feature or a change to existing data. |
| `design-a-failover-strategy` | Use when the user needs a service or data store to continue operating during a component failure. |
| `design-a-file-upload-and-processing-flow` | Use when the user needs users or systems to upload files that are then validated and processed. |
| `design-a-multi-tenant-data-model` | Use when the user needs to store data for multiple customers in one system. |
| `design-a-permission-model` | Use when the user needs to control which identities can perform actions on protected resources. |
| `design-a-public-api-contract` | Use when the user needs a stable contract for an API consumed by clients outside the team. |
| `design-a-rate-limit-and-quota-policy` | Use when the user needs to protect an API or service from excessive or unfair usage. |
| `design-an-event-driven-workflow` | Use when the user needs to coordinate asynchronous work through published events. |
| `design-an-idempotent-api` | Use when the user needs an operation that clients can retry without duplicate side effects. |
| `design-for-observability` | Use when the user needs a monitoring and troubleshooting plan for a service or architecture. |
| `evaluate-a-third-party-service` | Use when the user is considering an external service as part of a system design. |
| `plan-a-decomposition-of-a-god-service` | Use when the user needs to split a large service that has unclear or excessive responsibilities. |
| `plan-a-read-write-split` | Use when the user needs to offload reads from a primary database or service tier. |
| `plan-a-schema-evolution-strategy` | Use when the user needs to change a shared schema without breaking existing clients or services. |
| `plan-a-strangler-fig-migration` | Use when the user needs to replace a legacy capability without a risky cutover. |
| `plan-a-zero-downtime-schema-change` | Use when the user needs to alter a live database schema while services remain available. |
| `review-an-architecture-diagram` | Use when the user needs to check whether a diagram accurately represents a proposed architecture. |
| `write-a-migration-rollback-plan` | Use when the user needs a safe retreat path for a production migration or launch. |
| `write-a-system-design-document` | Use when the user needs a reviewed design for a new or substantially changed system. |
| `write-an-architecture-decision-record` | Use when the user needs to document a consequential technical choice for future reviewers. |

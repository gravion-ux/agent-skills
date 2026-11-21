---
name: choose-a-message-queue
description: Choose a message queue using delivery, ordering, latency, throughput, and operating constraints. Use when the user needs to select messaging infrastructure for a system workflow.
domain: architecture-design
tags: [message-queue, throughput, delivery-semantics]
triggers: ["message queue selection", "choose a message broker", "compare queue technologies"]
---

# Choose a message queue using delivery, ordering, latency, throughput, and operating constraints

## Purpose

Choose a message queue using delivery, ordering, latency, throughput, and operating constraints.

## When to use

Use when the user needs to select messaging infrastructure for a system workflow.

## When NOT to use

Do not use this for a local implementation detail; use software-engineering instead.

## Inputs required

- The functional and non-functional requirements
- The constraints on scale, budget and timeline
- The existing systems the design must fit

## Procedure

1. Quantify message volume, size, latency target, retention, and consumer concurrency.
2. List delivery, ordering, deduplication, replay, and cross-region requirements.
3. Compare the candidate queues against those requirements and team operating capacity.
4. Estimate the cost of infrastructure, support, upgrades, and failure recovery.
5. Validate the chosen queue with representative load and failure scenarios.
6. Record the assumptions, lock-in risks, and the trigger for revisiting the selection.

## Output contract

A design with components, interfaces, data flows, failure modes and a migration path.

## Validation checklist

- [ ] Every requirement maps to a component
- [ ] Failure and rollback paths are described
- [ ] The trade-offs behind the choice are written down

## Safety notes

Never present a design as final without stating the assumptions it depends on.

## Related skills

- `choose-between-a-modular-monolith-and-microservices`
- `assess-a-technical-proposal`
- `design-a-batch-processing-pipeline`

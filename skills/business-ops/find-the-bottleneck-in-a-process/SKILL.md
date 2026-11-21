---
name: find-the-bottleneck-in-a-process
description: Find the process bottleneck by comparing queue time, capacity, and downstream impact. Use when the user needs to identify the constraint that limits a process.
domain: business-ops
tags: [bottleneck, capacity, process-efficiency]
triggers: ["find process bottleneck", "locate the process constraint", "reduce process queue time"]
---

# Find the process bottleneck by comparing queue time, capacity, and downstream impact

## Purpose

Find the process bottleneck by comparing queue time, capacity, and downstream impact.

## When to use

Use when the user needs to identify the constraint that limits a process.

## When NOT to use

Do not use this for a single customer conversation; use communication instead.

## Inputs required

- The process being run
- The inputs and who supplies them
- The service level the process must meet

## Procedure

1. Measure queue time, throughput, and work-in-progress for each stage.
2. Compare arrival rate with effective capacity at every stage.
3. Trace the slowest handoff to the work it blocks downstream.
4. Test whether adding capacity at the constraint improves total throughput.
5. Route any funded remedy to the process owner for approval.
6. Document the chosen remedy, owner, cost, and target cycle time.

## Output contract

A documented operating procedure with owners, inputs, steps and the metrics it is judged on.

## Validation checklist

- [ ] Every step has an owner
- [ ] The failure path is documented
- [ ] The metric that proves the process works is named

## Safety notes

Never change a financial, legal or contractual step without the owner's approval.

## Related skills

- `check-compliance-with-a-process`
- `document-a-business-process`
- `map-a-process-from-start-to-finish`

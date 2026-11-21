---
name: write-a-benchmark-report
description: Write a benchmark report that states the method, the environment and the limits of the result. Use when the user has performance measurements and wants to publish them.
domain: technical-writing
tags: [benchmark, performance, reporting]
triggers: ["write a benchmark report", "publish these performance measurements", "performance results with methodology"]
---

# Write a benchmark report that states the method, the environment and the limits of the result

## Purpose

Write a benchmark report that states the method, the environment and the limits of the result.

## When to use

Use when the user has performance measurements and wants to publish them.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. Describe the hardware, the software versions and the configuration of the test.
2. State exactly what was measured and how the measurement was taken.
3. Give the numbers with a variance figure and the number of runs.
4. Note the workloads that were not tested and any known bias.
5. Say plainly what the results do not prove.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `write-a-comparison-of-two-approaches`
- `write-a-migration-plan-for-users`
- `write-a-postmortem`

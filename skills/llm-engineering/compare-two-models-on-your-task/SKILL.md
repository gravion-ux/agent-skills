---
name: compare-two-models-on-your-task
description: Compare two models on representative tasks with matched prompts, metrics, cost, and latency. Use when the user wants evidence for choosing between two LLMs for a specific workload.
domain: llm-engineering
tags: [model-comparison, benchmarks, cost, latency]
triggers: ["compare two models", "llm model bakeoff", "benchmark models on my task"]
---

# Compare two models on representative tasks with matched prompts, metrics, cost, and latency

## Purpose

Compare two models on representative tasks with matched prompts, metrics, cost, and latency.

## When to use

Use when the user wants evidence for choosing between two LLMs for a specific workload.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Create one fixed evaluation set that reflects the production workload.
2. Run both models with equivalent prompts, decoding settings, and tool access.
3. Record output quality, failure rate, token usage, latency, and total cost.
4. Inspect wins and losses by task slice instead of relying only on averages.
5. Select a model only when it clears the agreed quality and cost thresholds.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `build-a-model-router-by-task-difficulty`
- `retry-on-a-malformed-model-response`
- `add-typed-function-definitions-for-tools`

---
name: write-a-model-cost-dashboard
description: Write a model cost dashboard that breaks spend down by feature, model, latency, and budget variance. Use when the user wants a dashboard that tracks LLM usage and spend against a defined budget.
domain: llm-engineering
tags: [cost, dashboard, monitoring, budgeting]
triggers: ["model cost dashboard", "llm spend tracking", "llm budget dashboard"]
---

# Write a model cost dashboard that breaks spend down by feature, model, latency, and budget variance

## Purpose

Write a model cost dashboard that breaks spend down by feature, model, latency, and budget variance.

## When to use

Use when the user wants a dashboard that tracks LLM usage and spend against a defined budget.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Define the budget period, cost model, and acceptable allocation granularity.
2. Collect token usage, cached tokens, request counts, and provider prices.
3. Normalize spend into one reporting currency and reconcile provider invoices.
4. Segment cost and latency by feature, model, route, and customer tier.
5. Add budget thresholds, anomaly flags, and links to drill into failing requests.

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
- `build-a-retrieval-pipeline-for-a-model`
- `build-a-shadow-deployment-for-a-model`

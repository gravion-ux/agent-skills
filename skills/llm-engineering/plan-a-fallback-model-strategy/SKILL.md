---
name: plan-a-fallback-model-strategy
description: Plan a fallback model strategy with health signals, routing rules, budget limits, and recovery tests. Use when the user wants an LLM workflow to remain available when its primary model fails.
domain: llm-engineering
tags: [fallbacks, resilience, routing, cost]
triggers: ["fallback model strategy", "plan llm failover", "route around model failures"]
---

# Plan a fallback model strategy with health signals, routing rules, budget limits, and recovery tests

## Purpose

Plan a fallback model strategy with health signals, routing rules, budget limits, and recovery tests.

## When to use

Use when the user wants an LLM workflow to remain available when its primary model fails.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Classify failures as transient, capacity, policy, or quality related.
2. Define fallback triggers using timeout, error rate, and quality thresholds.
3. Select fallback models by task compatibility, latency, and cost constraints.
4. Bound retry volume and total spend to prevent fallback cascades.
5. Run outage drills and confirm primary recovery without double processing.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `plan-a-multi-step-model-workflow`
- `build-a-model-router-by-task-difficulty`
- `build-a-retrieval-pipeline-for-a-model`

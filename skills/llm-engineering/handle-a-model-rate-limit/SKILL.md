---
name: handle-a-model-rate-limit
description: Absorb provider rate limits with retry timing, request controls, and observable backpressure. Use when the user needs a model integration to survive provider throttling.
domain: llm-engineering
tags: [rate-limit, backoff, resilience]
triggers: ["handle llm rate limits", "llm retry after backoff", "llm rate limit resilience"]
---

# Absorb provider rate limits with retry timing, request controls, and observable backpressure

## Purpose

Absorb provider rate limits with retry timing, request controls, and observable backpressure.

## When to use

Use when the user needs a model integration to survive provider throttling.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Read the provider's rate-limit headers and remaining quota before retrying.
2. Honor the retry delay and apply exponential backoff with jitter within the timeout budget.
3. Cap retries per request and preserve idempotency across repeated attempts.
4. Apply concurrency limits and queue excess work instead of amplifying traffic.
5. Measure throttling rate, recovery time, token cost, latency, and documented failure modes.

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

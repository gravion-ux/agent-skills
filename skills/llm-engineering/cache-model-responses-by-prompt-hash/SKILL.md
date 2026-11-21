---
name: cache-model-responses-by-prompt-hash
description: Cache model responses by normalized prompt hash while preserving privacy and invalidation rules. Use when the user wants to reuse repeated LLM responses without serving stale or unsafe results.
domain: llm-engineering
tags: [caching, prompt-hash, privacy, cost]
triggers: ["cache responses by prompt hash", "prompt hash llm cache", "cache repeated model requests"]
---

# Cache model responses by normalized prompt hash while preserving privacy and invalidation rules

## Purpose

Cache model responses by normalized prompt hash while preserving privacy and invalidation rules.

## When to use

Use when the user wants to reuse repeated LLM responses without serving stale or unsafe results.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Normalize the request into the fields that affect model output.
2. Create a versioned cache key from the model version and normalized request hash.
3. Store only redacted responses with a configurable retention period.
4. Return a cached response only when the key, policy, and model version match.
5. Expose hit rate, age, and invalidation events in cache metrics.

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

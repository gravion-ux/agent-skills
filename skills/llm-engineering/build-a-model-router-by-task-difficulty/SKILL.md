---
name: build-a-model-router-by-task-difficulty
description: Route requests to models based on measured task difficulty while controlling quality and cost. Use when the user wants to choose among several models for each request.
domain: llm-engineering
tags: [model-routing, difficulty, cost-optimization]
triggers: ["route llm by task difficulty", "llm model router", "choose llm model by difficulty"]
---

# Route requests to models based on measured task difficulty while controlling quality and cost

## Purpose

Route requests to models based on measured task difficulty while controlling quality and cost.

## When to use

Use when the user wants to choose among several models for each request.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Define the request contract and the signals available before generation.
2. Label fixed evaluation requests with their difficulty and required quality.
3. Route each request with a tested rule or lightweight classifier.
4. Send ambiguous requests to the higher-capability route and handle failures explicitly.
5. Measure routing accuracy, answer quality, token cost, latency, and failure modes.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `build-a-retrieval-pipeline-for-a-model`
- `build-a-shadow-deployment-for-a-model`
- `build-a-batch-inference-pipeline`

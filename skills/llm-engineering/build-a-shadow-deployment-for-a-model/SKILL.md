---
name: build-a-shadow-deployment-for-a-model
description: Build a shadow deployment that scores candidate model traffic without affecting live responses. Use when the user wants to evaluate a new LLM safely against production-shaped traffic.
domain: llm-engineering
tags: [shadow-deployment, production, monitoring, safety]
triggers: ["build model shadow deployment", "shadow llm traffic", "test model without serving it"]
---

# Build a shadow deployment that scores candidate model traffic without affecting live responses

## Purpose

Build a shadow deployment that scores candidate model traffic without affecting live responses.

## When to use

Use when the user wants to evaluate a new LLM safely against production-shaped traffic.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Mirror sanitized production requests into an isolated shadow pipeline.
2. Run the candidate model with a strict timeout and token ceiling.
3. Score both live and shadow outputs with the same evaluation checks.
4. Store paired results and latency metrics without changing live responses.
5. Review agreement, cost, and failure slices before deciding whether to promote.

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
- `build-a-model-router-by-task-difficulty`
- `chunk-a-long-document-for-a-model`

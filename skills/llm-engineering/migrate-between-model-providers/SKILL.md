---
name: migrate-between-model-providers
description: Migrate an LLM integration between providers while preserving contracts, safety, and evaluation quality. Use when the user wants to move an existing model integration to a different provider.
domain: llm-engineering
tags: [migration, providers, integration, evaluation]
triggers: ["migrate llm providers", "switch model provider", "move llm integration provider"]
---

# Migrate an LLM integration between providers while preserving contracts, safety, and evaluation quality

## Purpose

Migrate an LLM integration between providers while preserving contracts, safety, and evaluation quality.

## When to use

Use when the user wants to move an existing model integration to a different provider.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Capture the current request, response, error, and usage contracts.
2. Map provider-specific tools, structured output, and token parameters to a common interface.
3. Run the existing evaluation suite against both providers with matched inputs.
4. Add provider-specific failure handling and migrate telemetry without logging raw prompts.
5. Promote the new provider only when quality, latency, and cost thresholds pass.

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

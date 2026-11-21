---
name: retry-on-a-malformed-model-response
description: Detect malformed model responses and recover them with bounded, observable retries. Use when the user needs an integration to recover from invalid model output.
domain: llm-engineering
tags: [retry, malformed-output, response-validation]
triggers: ["llm malformed response retry", "retry invalid llm json", "repair malformed model output"]
---

# Detect malformed model responses and recover them with bounded, observable retries

## Purpose

Detect malformed model responses and recover them with bounded, observable retries.

## When to use

Use when the user needs an integration to recover from invalid model output.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Validate each response against the required format before parsing it.
2. Record the error class, attempt count, and model identifier without logging raw prompts.
3. Retry with a targeted repair instruction up to the configured attempt limit.
4. Escalate to a fallback path after the final failed attempt.
5. Measure recovery rate, token cost, latency, and documented failure modes on a fixed evaluation set.

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

---
name: call-a-model-with-streaming-output
description: Stream model output over the transport protocol and measure the first-token and total latency. Use when the user wants incremental model output in an application interface.
domain: llm-engineering
tags: [streaming, sse, latency]
triggers: ["stream llm output", "llm streaming api", "llm server sent events output"]
---

# Stream model output over the transport protocol and measure the first-token and total latency

## Purpose

Stream model output over the transport protocol and measure the first-token and total latency.

## When to use

Use when the user wants incremental model output in an application interface.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Open the provider's streaming request with the required request contract.
2. Decode events in order and append only complete content chunks.
3. Handle cancellation, disconnects, and incomplete streams without corrupting output.
4. Record time to first token, total latency, token usage, and stream errors.
5. Verify final output accuracy against a fixed evaluation set and document failure modes.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `constrain-a-model-output-to-json-schema`
- `build-a-model-router-by-task-difficulty`
- `build-a-retrieval-pipeline-for-a-model`

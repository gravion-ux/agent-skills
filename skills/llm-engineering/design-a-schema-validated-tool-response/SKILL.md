---
name: design-a-schema-validated-tool-response
description: Design a schema-validated response contract so tool results remain valid across every model turn. Use when the user wants tool results constrained to a predictable machine-readable schema.
domain: llm-engineering
tags: [schema, tool-calls, structured-output, contracts]
triggers: ["design tool response schema", "schema validated tool response", "validate tool result contract"]
---

# Design a schema-validated response contract so tool results remain valid across every model turn

## Purpose

Design a schema-validated response contract so tool results remain valid across every model turn.

## When to use

Use when the user wants tool results constrained to a predictable machine-readable schema.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Define the response schema from downstream consumer requirements.
2. Separate required fields, optional fields, and explicit null semantics.
3. Validate every tool result against the schema before returning it.
4. Include a stable error object when execution fails.
5. Test valid, partial, and invalid results against the same schema.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `build-a-tool-calling-loop`
- `constrain-a-model-output-to-json-schema`
- `design-a-model-in-the-loop-classifier`

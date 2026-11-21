---
name: add-typed-function-definitions-for-tools
description: Add typed function definitions that expose each tool's purpose, arguments, and result clearly. Use when the user wants model-facing tool definitions with explicit parameter types.
domain: llm-engineering
tags: [function-definitions, type-safety, tool-calling, api-design]
triggers: ["add typed function definitions", "typed tool function schema", "define model tool parameters"]
---

# Add typed function definitions that expose each tool's purpose, arguments, and result clearly

## Purpose

Add typed function definitions that expose each tool's purpose, arguments, and result clearly.

## When to use

Use when the user wants model-facing tool definitions with explicit parameter types.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Write a one-line purpose statement for each tool.
2. Define each parameter with its type, required flag, and semantic constraint.
3. Specify the result shape and the failure cases the tool can return.
4. Generate the provider function-definition payload from one typed source.
5. Reject duplicate tool names and validate every definition against the model schema.

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
- `choose-embeddings-for-a-corpus`

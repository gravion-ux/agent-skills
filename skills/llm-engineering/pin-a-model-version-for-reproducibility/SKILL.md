---
name: pin-a-model-version-for-reproducibility
description: Pin model, prompt, and decoding versions so a production result can be reproduced exactly. Use when the user needs repeatable LLM outputs across development, testing, and production.
domain: llm-engineering
tags: [versioning, reproducibility, configuration, llm]
triggers: ["pin model version", "reproducible llm configuration", "freeze model and prompt versions"]
---

# Pin model, prompt, and decoding versions so a production result can be reproduced exactly

## Purpose

Pin model, prompt, and decoding versions so a production result can be reproduced exactly.

## When to use

Use when the user needs repeatable LLM outputs across development, testing, and production.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Record the provider and exact model version for every request.
2. Store the prompt version, decoding parameters, and tool definitions with the result.
3. Resolve aliases to immutable identifiers before deploying the configuration.
4. Run a fixed regression set and compare outputs after any version change.
5. Document whether provider updates can alter behavior despite the pinned version.

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
- `chunk-a-long-document-for-a-model`

---
name: cut-prompt-tokens-without-losing-accuracy
description: Reduce prompt tokens with measured edits that preserve accuracy on a fixed evaluation set. Use when the user has an llm prompt that exceeds its token budget.
domain: llm-engineering
tags: [prompt-compression, token-budget, cost-optimization]
triggers: ["cut llm prompt tokens", "reduce llm prompt cost", "llm prompt compression"]
---

# Reduce prompt tokens with measured edits that preserve accuracy on a fixed evaluation set

## Purpose

Reduce prompt tokens with measured edits that preserve accuracy on a fixed evaluation set.

## When to use

Use when the user has an llm prompt that exceeds its token budget.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Profile prompt sections by token count and observed contribution to accuracy.
2. Remove duplication, stale examples, and instructions that produce no measurable effect.
3. Compress or summarize context while retaining facts needed for the request contract.
4. Run the candidate on the same evaluation set used for the baseline.
5. Accept only versions that preserve quality while reporting token savings and latency changes.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `build-a-system-prompt-with-guardrails`
- `cache-model-responses-by-prompt-hash`
- `structure-a-prompt-with-context-and-instructions`

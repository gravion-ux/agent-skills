---
name: run-an-offline-evaluation-suite
description: Run a fixed offline evaluation suite and report quality, latency, cost, and failure changes. Use when the user wants to verify a prompt or model change against a stable evaluation set.
domain: llm-engineering
tags: [evaluation, regression, metrics, llm]
triggers: ["run offline evaluation suite", "evaluate llm changes offline", "llm regression evaluation"]
---

# Run a fixed offline evaluation suite and report quality, latency, cost, and failure changes

## Purpose

Run a fixed offline evaluation suite and report quality, latency, cost, and failure changes.

## When to use

Use when the user wants to verify a prompt or model change against a stable evaluation set.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Freeze a representative evaluation dataset with reference outputs and labels.
2. Record the candidate prompt or model configuration beside each case.
3. Run every case and save outputs, errors, tokens, and elapsed latency.
4. Compute aggregate quality metrics and stratified failure breakdowns.
5. Compare results with the baseline and flag regressions beyond the agreed threshold.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `run-an-ab-test-between-prompts`
- `build-an-agentic-rag-loop`
- `design-a-rag-evaluation-set`

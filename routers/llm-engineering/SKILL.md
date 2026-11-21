---
name: router-llm-engineering
description: Route work in the LLM application engineering domain to the right leaf skill. Use when a task clearly belongs to llm-engineering.
domain: llm-engineering
tags: [router, routing, llm-engineering]
triggers: ["route a llm-engineering task", "which llm-engineering skill should I use"]
---

# LLM application engineering router

## Purpose

List every leaf skill in the llm-engineering domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside llm-engineering and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `add-typed-function-definitions-for-tools` | Use when the user wants model-facing tool definitions with explicit parameter types. |
| `build-a-batch-inference-pipeline` | Use when the user wants to process many LLM requests reliably without overwhelming the provider. |
| `build-a-model-router-by-task-difficulty` | Use when the user wants to choose among several models for each request. |
| `build-a-retrieval-pipeline-for-a-model` | Use when the user wants to connect a document corpus to a model application. |
| `build-a-shadow-deployment-for-a-model` | Use when the user wants to evaluate a new LLM safely against production-shaped traffic. |
| `build-a-system-prompt-with-guardrails` | Use when the user needs a system prompt that constrains model behavior in production. |
| `build-a-tool-calling-loop` | Use when the user wants a model to call tools safely through a controlled execution loop. |
| `build-an-agentic-rag-loop` | Use when the user wants an LLM agent to retrieve, verify, and use documents before answering. |
| `cache-model-responses-by-prompt-hash` | Use when the user wants to reuse repeated LLM responses without serving stale or unsafe results. |
| `call-a-model-with-streaming-output` | Use when the user wants incremental model output in an application interface. |
| `choose-between-a-chain-and-a-router` | Use when the user needs to select between a fixed LLM pipeline and a model-based router. |
| `choose-embeddings-for-a-corpus` | Use when the user needs to choose an embedding model for a document collection. |
| `chunk-a-long-document-for-a-model` | Use when the user needs to process a document larger than the model context window. |
| `compare-two-models-on-your-task` | Use when the user wants evidence for choosing between two LLMs for a specific workload. |
| `constrain-a-model-output-to-json-schema` | Use when the user needs structured model output that downstream code can parse. |
| `cut-prompt-tokens-without-losing-accuracy` | Use when the user has an llm prompt that exceeds its token budget. |
| `design-a-model-in-the-loop-classifier` | Use when the user wants an LLM to classify incoming records on a fixed taxonomy. |
| `design-a-rag-evaluation-set` | Use when the user needs a repeatable benchmark for a retrieval-augmented application. |
| `design-a-schema-validated-tool-response` | Use when the user wants tool results constrained to a predictable machine-readable schema. |
| `detect-hallucination-in-a-generated-answer` | Use when the user needs to assess unsupported claims in an llm answer. |
| `fall-back-to-a-second-model-provider` | Use when the user needs provider failover for an llm application. |
| `ground-a-response-in-retrieved-citations` | Use when the user wants a model answer that links claims to source material. |
| `handle-a-model-rate-limit` | Use when the user needs a model integration to survive provider throttling. |
| `implement-a-multi-turn-tool-conversation` | Use when the user wants an LLM chat flow to use results from earlier tool calls. |
| `log-model-inputs-and-outputs-safely` | Use when the user wants observability for LLM calls without exposing sensitive customer data. |
| `measure-retrieval-quality` | Use when the user needs objective metrics for retrieval quality. |
| `measure-token-usage-and-cost` | Use when the user needs visibility into llm usage and spending. |
| `migrate-between-model-providers` | Use when the user wants to move an existing model integration to a different provider. |
| `parse-structured-tool-arguments` | Use when the user needs to validate model-generated arguments before passing them to a tool. |
| `pin-a-model-version-for-reproducibility` | Use when the user needs repeatable LLM outputs across development, testing, and production. |
| `plan-a-fallback-model-strategy` | Use when the user wants an LLM workflow to remain available when its primary model fails. |
| `plan-a-multi-step-model-workflow` | Use when the user wants to design a staged LLM workflow with several dependent model or tool steps. |
| `rank-retrieved-chunks-before-generation` | Use when the user has noisy retrieval results that must be ordered for generation. |
| `redact-personal-data-before-sending-to-a-model` | Use when the user wants to remove personal information from text sent to an external LLM. |
| `retry-on-a-malformed-model-response` | Use when the user needs an integration to recover from invalid model output. |
| `run-an-ab-test-between-prompts` | Use when the user wants to determine which prompt performs better for a live model workflow. |
| `run-an-offline-evaluation-suite` | Use when the user wants to verify a prompt or model change against a stable evaluation set. |
| `score-output-quality-with-rubrics` | Use when the user needs a consistent way to grade open-ended LLM outputs. |
| `structure-a-prompt-with-context-and-instructions` | Use when the user wants a prompt with unambiguous sections and boundaries. |
| `summarise-a-long-conversation-in-context` | Use when the user needs to keep a long chat within the model context limit. |
| `use-few-shot-examples-in-a-prompt` | Use when the user wants a prompt to learn a task from demonstrations. |
| `write-a-good-completion-prompt` | Use when the user needs a clear baseline prompt for a text completion. |
| `write-a-model-cost-dashboard` | Use when the user wants a dashboard that tracks LLM usage and spend against a defined budget. |
| `write-a-regression-test-for-prompt-changes` | Use when the user wants to prevent a prompt change from degrading production behavior. |

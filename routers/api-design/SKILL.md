---
name: router-api-design
description: Route work in the API design domain to the right leaf skill. Use when a task clearly belongs to api-design.
domain: api-design
tags: [router, routing, api-design]
triggers: ["route a api-design task", "which api-design skill should I use"]
---

# API design router

## Purpose

List every leaf skill in the api-design domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside api-design and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for internal function signatures; use software-engineering instead.

## Inputs required

- The consumers and what they need
- The resources and the operations involved
- The versioning, auth and rate-limit policy

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A documented contract with endpoints, payloads, error shapes and versioning rules.

## Validation checklist

- [ ] Every error has a stable machine-readable code
- [ ] Pagination, filtering and idempotency are defined
- [ ] The contract is versioned and backward compatible

## Safety notes

Never change an existing response shape without a version bump and a migration note.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `choose-pagination-for-a-collection` | Use when the user needs a collection endpoint to return stable, navigable results. |
| `design-a-bulk-endpoint` | Use when the user needs clients to submit or update many items in one request. |
| `design-a-graphql-schema` | Use when the user needs a GraphQL schema that exposes a coherent domain model. |
| `design-a-rest-resource-model` | Use when the user needs to shape a REST API around domain resources and consumer workflows. |
| `design-a-search-endpoint` | Use when the user needs an endpoint that finds resources by user-supplied criteria. |
| `design-a-webhook-delivery-contract` | Use when the user needs an API to notify external systems about domain events. |
| `design-an-authentication-flow` | Use when the user needs an API to authenticate clients safely. |
| `design-an-authorization-model` | Use when the user needs to control which clients and users may perform API actions. |
| `design-an-error-response-format` | Use when the user needs clients to handle API failures predictably. |
| `design-an-event-streaming-api` | Use when the user needs a streaming API for ordered domain events. |
| `design-api-key-scopes` | Use when the user needs to issue API keys that expose only intended capabilities. |
| `design-api-observability-headers` | Use when the user needs clients and operators to correlate requests across services. |
| `design-api-versioning-strategy` | Use when the user needs to evolve an API without silently breaking existing consumers. |
| `design-idempotency-keys` | Use when the user needs clients to retry unsafe API mutations without duplicates. |
| `design-long-running-operations` | Use when the user needs an API action that may outlive a normal request timeout. |
| `plan-an-api-deprecation` | Use when the user needs to retire an API version without leaving consumers stranded. |
| `plan-an-api-gateway-policy` | Use when the user needs to enforce cross-cutting traffic rules at an API gateway. |
| `rate-limit-an-api-endpoint` | Use when the user needs to protect an endpoint from excessive or abusive requests. |
| `review-an-api-change-for-clients` | Use when the user needs to assess how a proposed contract change affects existing consumers. |
| `review-an-api-for-consistency` | Use when the user wants an existing API checked for contract consistency. |
| `write-an-openapi-specification` | Use when the user needs an executable or implementation-ready description of an HTTP API. |
| `write-api-documentation-examples` | Use when the user needs examples that help developers use an API correctly. |

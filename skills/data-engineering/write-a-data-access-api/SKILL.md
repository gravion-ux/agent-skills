---
name: write-a-data-access-api
description: Write a data access API that serves documented datasets with pagination, authentication and clear errors. Use when the user wants an application to read curated warehouse data through a stable endpoint.
domain: data-engineering
tags: [data-api, rest-api, access-control]
triggers: ["data access api", "serve warehouse data endpoint", "build api for curated data"]
---

# Write a data access API that serves documented datasets with pagination, authentication and clear errors

## Purpose

Write a data access API that serves documented datasets with pagination, authentication and clear errors.

## When to use

Use when the user wants an application to read curated warehouse data through a stable endpoint.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Define the resource schema, pagination model and versioned endpoint paths.
2. Read credentials from the secret store and reject anonymous requests.
3. Apply row filters from the caller's claims before the query runs.
4. Return typed errors with a request id and a documented status code.
5. Publish an OpenAPI file and test one successful and one denied call.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `build-a-raw-to-curated-data-layer`
- `cost-optimise-a-data-pipeline`
- `document-a-data-pipeline`

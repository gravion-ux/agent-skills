---
name: test-a-migration-on-a-copy-of-production-data
description: Test a database migration against a sanitised copy of production data in a disposable database. Use when the user wants confidence that a schema migration works on real-world data.
domain: testing-qa
tags: [migration-testing, database, data-safety]
triggers: ["test a migration on a production data copy", "dry run a schema migration", "verify migration on real data"]
---

# Test a database migration against a sanitised copy of production data in a disposable database

## Purpose

Test a database migration against a sanitised copy of production data in a disposable database.

## When to use

Use when the user wants confidence that a schema migration works on real-world data.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Copy and sanitise production data into a disposable database instance.
2. Run the migration against the copy and record row counts before and after.
3. Verify constraints, indexes, and backfilled values with targeted queries.
4. Restore the database from the migration backup and confirm the rollback path.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `build-a-data-driven-test-table`
- `design-a-test-data-strategy`
- `run-a-test-of-the-test-suite`

---
name: router-devops-cloud
description: Route work in the DevOps and cloud infrastructure domain to the right leaf skill. Use when a task clearly belongs to devops-cloud.
domain: devops-cloud
tags: [router, routing, devops-cloud]
triggers: ["route a devops-cloud task", "which devops-cloud skill should I use"]
---

# DevOps and cloud infrastructure router

## Purpose

List every leaf skill in the devops-cloud domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside devops-cloud and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `apply-a-cost-budget-to-cloud-resources` | Use when the user wants to control or predict cloud spending. |
| `audit-cloud-permissions` | Use when the user wants to review cloud access permissions for privilege and exposure risks. |
| `automate-a-release-with-a-pull-request` | Use when the user wants the release preparation steps to run from a reviewed pull request. |
| `autoscale-a-kubernetes-workload` | Use when the user wants a Kubernetes workload to scale with traffic. |
| `back-up-and-restore-a-cloud-data-store` | Use when the user wants a protected backup and a proven restore for a managed cloud datastore. |
| `build-a-container-image` | Use when the user wants to package a service as a container image for deployment. |
| `configure-a-load-balancer` | Use when the user needs to put a load balancer in front of a service or fleet. |
| `configure-a-load-test-environment` | Use when the user wants to test a service under production-like load. |
| `design-a-blue-green-deployment` | Use when the user wants to release infrastructure or application changes with a blue-green strategy. |
| `drift-detect-infrastructure-changes` | Use when the user wants scheduled or on-demand detection of cloud configuration drift. |
| `gate-a-deployment-on-quality-checks` | Use when the user wants a ci pipeline to prevent low-quality builds from reaching production. |
| `harden-a-server-baseline` | Use when the user wants a cloud server aligned with a hardened security baseline. |
| `implement-blue-green-traffic-shifting` | Use when the user wants to release infrastructure changes through a blue-green deployment. |
| `manage-a-service-on-a-managed-cloud-platform` | Use when the user wants to run a service on a managed cloud application platform. |
| `manage-configuration-across-environments` | Use when the user wants one controlled configuration source shared across deployment environments. |
| `manage-cost-with-a-scheduled-scale-down` | Use when the user wants predictable infrastructure savings without risking service availability. |
| `manage-environments-with-infrastructure-pipelines` | Use when the user wants infrastructure changes promoted from development to production. |
| `manage-feature-flags-across-environments` | Use when the user wants to enable or disable a feature independently in each environment. |
| `manage-secrets-in-a-cloud-account` | Use when the user needs to manage secrets, keys or credentials inside a cloud account. |
| `migrate-a-workload-to-a-managed-service` | Use when the user wants to replace a self-run service with a managed cloud equivalent. |
| `patch-a-host-without-downtime` | Use when the user needs to patch a live server while keeping its service available. |
| `pin-a-container-base-image` | Use when the user wants to remove mutable image tags from a container build. |
| `plan-a-cloud-migration-wave` | Use when the user needs to plan an incremental migration of many workloads to the cloud. |
| `promote-a-build-through-environments` | Use when the user wants to move the same tested build through successive release environments. |
| `provision-a-cloud-environment` | Use when the user needs a new isolated environment created in a cloud account. |
| `reduce-a-container-image-size` | Use when the user wants a smaller or faster-to-pull container image. |
| `respond-to-a-service-outage` | Use when the user needs to coordinate recovery from an active production service outage. |
| `right-size-cloud-compute-resources` | Use when the user wants to reduce cloud waste or improve instance sizing. |
| `roll-back-a-bad-deployment` | Use when the user needs to roll back a deployment that broke the service. |
| `rotate-a-service-account-key` | Use when the user needs to rotate a cloud service account key safely. |
| `run-a-canary-release-with-metrics` | Use when the user wants to validate a new build in production before a full rollout. |
| `run-a-disaster-recovery-drill` | Use when the user wants to rehearse regional failure recovery for critical infrastructure. |
| `run-a-service-in-kubernetes` | Use when the user wants to run a service on a Kubernetes cluster. |
| `scale-a-worker-queue` | Use when the user needs to tune worker concurrency because a cloud queue is falling behind. |
| `scan-an-image-for-vulnerabilities` | Use when the user wants a container image checked for vulnerabilities before it ships. |
| `set-up-a-canary-environment-for-testing` | Use when the user wants a temporary cloud environment for validating a release before production. |
| `set-up-a-cd-pipeline-with-safe-rollouts` | Use when the user wants a continuous delivery pipeline that deploys safely. |
| `set-up-a-ci-pipeline-for-a-service` | Use when the user wants a continuous integration pipeline for a service. |
| `set-up-a-virtual-network-and-subnets` | Use when the user needs to design or create a cloud network and its subnets. |
| `sign-and-verify-build-artifacts` | Use when the user wants proof that a build artifact came from a trusted pipeline and was not altered. |
| `test-a-backup-restore-safely` | Use when the user wants proof that backups restore cleanly without risking the live environment. |
| `triage-an-alert-fire` | Use when the user receives a burst of monitoring alerts and must decide what needs action. |
| `verify-a-deployment-after-release` | Use when the user wants post-release verification that a deployment completed correctly. |
| `write-a-dockerfile-for-a-service` | Use when the user needs a Dockerfile for a new or existing service. |
| `write-a-kubernetes-manifest` | Use when the user needs a Kubernetes manifest for a new workload. |
| `write-a-runbook-for-an-on-call-engineer` | Use when the user needs an operational runbook for a service someone else will maintain. |
| `write-an-incident-report` | Use when the user wants a clear incident review document after an outage or degradation. |
| `write-infrastructure-as-code-for-a-service` | Use when the user wants a service's cloud resources defined as code. |

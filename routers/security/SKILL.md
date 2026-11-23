---
name: router-security
description: Route work in the Security engineering domain to the right leaf skill. Use when a task clearly belongs to security.
domain: security
tags: [router, routing, security]
triggers: ["route a security task", "which security skill should I use"]
---

# Security engineering router

## Purpose

List every leaf skill in the security domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside security and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `add-input-validation-to-an-endpoint` | Use when the user wants an API endpoint to reject malformed or out-of-range input. |
| `add-security-headers-to-a-web-app` | Use when the user wants a web application to send a hardened set of browser security headers. |
| `apply-data-classification-labels` | Use when the user wants to classify stored data and make the handling rules follow automatically. |
| `apply-the-principle-of-least-privilege` | Use when the user wants service, user, or role permissions narrowed to justified access. |
| `audit-access-to-sensitive-data` | Use when the user wants to review who accessed sensitive records and identify risky behaviour. |
| `audit-third-party-security-posture` | Use when the user wants to review the controls a supplier applies to your data. |
| `authenticate-service-to-service-calls` | Use when the user needs one backend service to call another with a trusted identity. |
| `build-a-vulnerability-management-program` | Use when the user wants a repeatable way to handle findings across many teams. |
| `configure-a-cloud-firewall-baseline` | Use when the user wants a reviewed default deny firewall rule set for a cloud network. |
| `configure-cors-safely` | Use when the user needs browser cross-origin requests controlled on an API service. |
| `dedupe-a-vulnerability-report` | Use when the user wants to know whether a vulnerability has already been reported, disclosed or fixed before spending effort on a report. |
| `design-a-privilege-escalation-test` | Use when the user wants to test whether a low-privilege account can reach higher privileges. |
| `detect-secret-leaks-in-ci` | Use when the user wants pipelines to stop committing or publishing exposed credentials. |
| `enable-audit-logging-for-a-cloud-account` | Use when the user wants proof that administrative actions are recorded for later investigation. |
| `enforce-authorisation-on-an-api` | Use when the user needs API endpoints to enforce per-user and per-resource access. |
| `enforce-mfa-for-an-organisation` | Use when the user wants to roll out mandatory second factors across an organisation. |
| `fix-an-sql-injection` | Use when the user has identified a SQL injection in an application query. |
| `fix-an-xss-vulnerability` | Use when the user has found cross-site scripting in a web response or browser interface. |
| `harden-a-container-image` | Use when the user wants a container image minimised for secure production execution. |
| `harden-a-database-connection` | Use when the user wants to protect the path between an application and its database. |
| `harden-a-kubernetes-cluster` | Use when the user wants to raise the security posture of an existing Kubernetes cluster. |
| `implement-data-retention-controls` | Use when the user wants records deleted automatically once the retention period ends. |
| `implement-secure-file-uploads` | Use when the user needs an application to accept user files without exposing unsafe content. |
| `implement-secure-session-handling` | Use when the user needs server-side or token sessions secured across authentication events. |
| `investigate-a-cloud-access-anomaly` | Use when the user reports an unfamiliar sign-in or unusual privilege use in a cloud account. |
| `lock-down-an-ssh-server` | Use when the user wants to reduce the exposure of an SSH server on a reachable network. |
| `manage-encryption-keys` | Use when the user needs an encryption key lifecycle designed for production use. |
| `monitor-for-threat-intelligence-matches` | Use when the user wants new threat data checked against the systems they run. |
| `offboard-an-employee-securely` | Use when the user needs to revoke every access path for someone who is leaving. |
| `patch-a-critical-cve` | Use when the user wants to remediate a published critical vulnerability on a live system. |
| `plan-a-penetration-test` | Use when the user wants a security testing engagement scoped for safe authorised execution. |
| `prepare-for-a-security-questionnaire` | Use when the user must complete a customer's security assessment questionnaire. |
| `protect-a-service-with-a-rate-limit` | Use when the user wants an endpoint or service shielded from excessive or abusive request volume. |
| `protect-secrets-in-a-cicd-pipeline` | Use when the user wants to stop credentials leaking through a build pipeline. |
| `redact-sensitive-data-from-logs` | Use when the user wants to stop sensitive values reaching a log store or a third party collector. |
| `respond-to-a-leaked-secret` | Use when the user reports a credential exposed in code, logs, chat, or a public repository. |
| `respond-to-a-ransomware-suspicion` | Use when the user suspects encryption activity or destructive malware on production systems. |
| `review-code-for-injection-risks` | Use when the user wants untrusted input paths reviewed for injection vulnerabilities. |
| `review-permissions-in-an-iam-policy` | Use when the user wants an identity policy checked for excessive permissions before deployment. |
| `review-privileged-access-requests` | Use when the user must decide whether to grant temporary elevated access. |
| `rotate-a-compromised-api-key` | Use when the user needs an exposed API key revoked and replaced safely. |
| `run-a-compliance-gap-assessment` | Use when the user wants to find where a standard is not yet met. |
| `run-a-security-awareness-session` | Use when the user wants to teach a team secure everyday practices and verify their understanding. |
| `scan-a-container-image-for-vulnerabilities` | Use when the user wants to check a built image for known vulnerabilities before shipping it. |
| `scan-dependencies-for-known-vulnerabilities` | Use when the user wants the repository's third-party dependencies checked for published flaws. |
| `schedule-a-recurring-security-baseline-check` | Use when the user wants configuration drift against the security baseline detected on a schedule. |
| `scope-a-penetration-test` | Use when the user needs to authorise an external security test against named systems. |
| `secure-a-ci-pipeline-with-oidc` | Use when the user wants the build system to reach cloud resources without a stored access key. |
| `secure-a-public-api-surface` | Use when the user wants to harden an API that is reachable without a signed agreement. |
| `set-up-a-vulnerability-scanning-gate` | Use when the user wants dependency and code scanning to stop a risky change from merging. |
| `sign-an-artifact-for-provenance` | Use when the user wants a released artefact protected against tampering and substitution. |
| `store-passwords-safely` | Use when the user wants user passwords stored and verified without exposing plaintext. |
| `test-backup-restores-for-recovery-readiness` | Use when the user wants evidence that the backup set can be restored in practice. |
| `test-object-level-authorisation-on-an-api` | Use when the user wants to check whether an API enforces per-object ownership — the broken object level authorisation (BOLA/IDOR) class — on a system they own or are authorised to test. |
| `threat-model-a-new-feature` | Use when the user wants a new feature assessed for threats before implementation. |
| `triage-a-bug-bounty-finding` | Use when the user has a candidate bug bounty finding and needs to decide whether it is worth reporting to a programme. |
| `triage-a-dependency-confusion-risk` | Use when the user suspects their build pulls internal packages whose names could be claimed or shadowed on a public package registry. |
| `triage-a-security-finding` | Use when the user has a new security finding that needs validation and prioritisation. |
| `verify-a-webhook-signature` | Use when the user needs an inbound webhook endpoint to authenticate sender messages. |
| `verify-software-supply-chain-integrity` | Use when the user wants evidence that a released artefact came from the expected source. |
| `write-a-network-policy` | Use when the user wants to restrict pod-to-pod traffic inside a Kubernetes namespace. |
| `write-a-security-architecture-review` | Use when the user wants a design checked for security before it is built. |
| `write-a-security-test-case` | Use when the user wants a repeatable test for a specific security control or vulnerability. |
| `write-a-vulnerability-report` | Use when the user has a confirmed vulnerability and needs a report a triager can reproduce and act on without follow-up questions. |
| `write-an-incident-response-playbook` | Use when the user needs a repeatable response plan for a specific security incident type. |

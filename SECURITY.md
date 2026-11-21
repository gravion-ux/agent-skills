# Security Policy

## Reporting a vulnerability

Please report security issues privately through GitHub's **"Report a vulnerability"**
button on the Security tab of <https://github.com/gravion-ux/agent-skills>, rather than
opening a public issue.

Include: the affected file or skill name, what an attacker could do, the steps to
reproduce it, and the impact you believe it has. You will get an acknowledgement within
three working days and an assessment within seven.

Please give the maintainers a reasonable window to publish a fix before disclosing
publicly.

## What this project is

`agent-skills` is a **documentation and routing package**. It contains:

- text skill playbooks under `skills/` and `routers/`;
- a Python package (`agentskills`) that lists, scores, exports and packs that text;
- a generator, a validator and a secret scanner under `scripts/`.

## What this project does not do

- **No network calls at runtime.** The package reads local files and writes local files.
  It makes no HTTP requests, opens no sockets and contacts no service. The router is a
  local BM25 computation.
- **No credential handling.** The package never asks for, stores, reads, forwards or logs
  a password, API key, token or cookie. It has no authentication code and no secret store.
- **No code execution.** The package does not `exec`, `eval`, import contributed modules
  at runtime, or run shell commands. The generator imports the authoring modules under
  `catalog/source/` in the repository, which is a build-time step under the
  maintainer's control.
- **No telemetry.** Nothing is measured or reported back.

## Rules for contributed skills

A contributed skill is *instructions for an agent*. The following are not acceptable and
will fail review, and the CI secret scanner rejects hard-coded secrets outright:

1. **Never ask for credentials.** A skill must not request a password, API key, token,
   private key, recovery code or session cookie. If a task genuinely needs a secret, the
   skill must say that the user should authenticate through the tool's own sign-in flow
   and must not ask the user to paste the value.
2. **Never exfiltrate data.** A skill must not send the user's files, code, logs or
   personal data to an external endpoint, a paste service, a webhook or a third-party
   API unless the user explicitly asks for that specific destination.
3. **Never embed secrets in the skill text.** No API keys, no tokens, no passwords, no
   private URLs with credentials, no real customer data.
4. **Never hide an external action.** If a skill performs a network call, creates an
   account, sends a message or changes a live system, the step must say so plainly, and
   the skill must keep the reversible path first.
5. **Never widen permissions to work around a failure.** If a skill cannot complete
   because of missing access, it says so and asks for approval; it does not instruct an
   agent to escalate its own permissions.

## Scope of the CI secret scanner

`scripts/scan-secrets.py` scans the repository for AWS access keys, AWS secret keys,
private key headers, GitHub tokens, Slack tokens and generic `password`/`api_key`
assignments. It runs on every push and pull request and fails the build on a match.
Values that are obvious placeholders are ignored.

## Out of scope

- The *content* of a skill that is simply wrong, unhelpful or out of date — that is a
  quality issue, not a vulnerability: open a normal issue or pull request.
- Vulnerabilities in third-party software you use alongside this package — report those to
  the upstream project.
- Denial of service caused by feeding the router an enormous query — the router is
  local and cheap; open an issue if you find a practical problem.

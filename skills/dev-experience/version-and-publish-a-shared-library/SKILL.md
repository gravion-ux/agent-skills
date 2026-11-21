---
name: version-and-publish-a-shared-library
description: Version and release a shared library through reproducible builds, compatibility checks, and clear upgrade notes. Use when the user is preparing a versioned release of a shared code library.
domain: dev-experience
tags: [library-release, versioning, package-publishing]
triggers: ["version and publish a shared library", "release a shared code package", "cut a versioned library release"]
---

# Version and release a shared library through reproducible builds, compatibility checks, and clear upgrade notes

## Purpose

Version and release a shared library through reproducible builds, compatibility checks, and clear upgrade notes.

## When to use

Use when the user is preparing a versioned release of a shared code library.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Confirm the release scope and compatibility guarantees for the next version.
2. Run the full test, build, and artifact inspection checks on a clean checkout.
3. Publish the immutable artifact to the configured registry and verify its checksum.
4. Create release notes with breaking changes and migration examples.
5. Announce the version through the existing developer release channel.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `create-a-code-snippet-library`
- `add-a-health-check-endpoint`
- `add-editor-support-files-to-a-repo`

---
name: upload-a-file-with-progress
description: Upload a file with progress feedback, cancellation, and validation before transfer starts. Use when the user wants a file upload that reports progress and can be cancelled.
domain: web-development
tags: [file-upload, progress, resilience]
triggers: ["file upload with progress", "show upload progress for a file", "cancelable file upload"]
---

# Upload a file with progress feedback, cancellation, and validation before transfer starts

## Purpose

Upload a file with progress feedback, cancellation, and validation before transfer starts.

## When to use

Use when the user wants a file upload that reports progress and can be cancelled.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Validate the file type and size against the stated limit before uploading.
2. Send the file to the upload endpoint and stream progress events to a progress bar.
3. Expose a cancel control that aborts the request and clears partial state.
4. Show distinct success, failure, and retry states for the upload.
5. Avoid collecting personal file contents unless the upload purpose is stated in the interface.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-a-form-with-inline-validation`
- `build-a-modal-dialog-with-focus-management`
- `build-a-search-box-with-debounced-results`

# Publication and Privacy Review Control

**Status:** CONTROLLING — publication-risk control

This repository contains sensitive health information, clinician/institutional correspondence and material prepared for a counsel-facing evidential project. Public availability creates risks that are separate from evidential relevance.

## Governing rule

> **Public usefulness does not by itself justify publication of every source detail.**

The repository should distinguish between:

- **public redacted corpus** — material necessary to permit independent verification of the published argument;
- **private counsel exhibit bundle** — native files, metadata, complete identifiers, unredacted correspondence and other material not necessary for public verification.

## Review questions before publication

For every public source or analytical page ask:

1. Is the information necessary to verify a material proposition?
2. Does the page contain unnecessary third-party personal information?
3. Are email addresses, telephone numbers, addresses, identifiers or signatures exposed?
4. Does the page reproduce health detail that is not needed for the evidential issue?
5. Is the item a transcript/publication representation rather than a native exhibit, and is that distinction visible?
6. Is the patient knowingly choosing public identification for this material?
7. Could a redacted version serve the verification purpose equally well?
8. Does Git history contain an earlier unredacted version even if the current page is redacted?

## Git-history caution

Deleting or redacting the current version of a file does not necessarily remove data from prior commits, forks, caches or search-engine indexes.

Where historical exposure is identified, treat it as a separate remediation issue rather than assuming a new commit erases prior publication.

## Third-party data

The public corpus should minimise personal information about people who are not necessary actors in the evidential record. Where a third party is relevant only as a witness, recipient, administrator or family member, use the minimum identifying detail needed to preserve provenance.

## Native-document handling

Native exhibits should not automatically be placed in the public repository merely because a redacted transcript is public. A private preservation copy may retain:

- original PDF/image/email container;
- metadata;
- full pagination;
- cryptographic checksum;
- chain-of-custody notes;
- unredacted identifiers where legally and professionally appropriate.

The public manifest should state whether the native exhibit is held without necessarily publishing it.

## Publication review record

Before any large publication rotation, record:

- reviewer/date;
- files added or materially changed;
- redaction check completed;
- source/native-status check completed;
- third-party-data check completed;
- whether Git-history remediation is required;
- whether the material belongs in the public corpus or private counsel bundle.

## Current repository consequence

Reliability engineering and privacy engineering should proceed together. Better provenance should not be achieved by exposing more private information than is necessary.

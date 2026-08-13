# Repository Reliability Implementation Plan

**Status:** CONTROLLING — repository engineering plan

The next phase is verification infrastructure rather than additional case-theory expansion.

## Current priorities

### 1. Atomic fact layer

`clean_case_evidential_fact_register_v09.md` is referenced historically but is not present on `main`.

Until recovered, the repository must not present F0001–F0283 as directly inspectable. Primary-source citation remains controlling.

### 2. Source/exhibit control

Use `evidence/SOURCE_EXHIBIT_MANIFEST.md` as the source-ID and provenance layer. Expand it across the source corpus as each source is checked.

The manifest must distinguish:

- native exhibit held;
- transcript/publication representation;
- partial versus full transcription;
- redaction status;
- preservation checksum where available;
- evidential role;
- limitations.

### 3. Proposition control

Use `evidence/SOURCE_PROPOSITION_MATRIX.md` for propositions that matter to the operative argument.

Every proposition should expose contrary material, inference level and expert dependence rather than merely collecting supportive quotations.

### 4. Chronology control

Use `evidence/KNOWLEDGE_DECISION_RECONSIDERATION_CHRONOLOGY.md` to test when information entered the record, what decision opportunity existed and whether a local treatment change or historical reclassification followed.

### 5. Analytical-document status

Use `evidence/ANALYTICAL_DOCUMENT_STATUS_REGISTER.md` to prevent older drafts from silently competing with later work.

Status migration should proceed from the most visible counsel-facing pages outward. Superseded pages should retain their historical content but receive a prominent warning linking to the controlling replacement.

### 6. Citation repair

Repair relative links in the central audits first. In particular, files inside `docs/` should not prefix links with `docs/` when doing so creates `docs/docs/...` targets.

### 7. Source-status repair

Search for stale statements that acquired material remains missing. The 12 September 2017 Healy response is now substantively acquired as a directly inspected photographed source with a partial transcript. A preservation-quality native/redacted exhibit may remain desirable; that is a different proposition.

### 8. Automated validation

Add CI only after the repository's status and source conventions are stable enough to encode deterministically. The validator should check links, source IDs, status declarations, stale missing-source statements and transcript provenance.

CI should never adjudicate contested clinical or legal conclusions.

### 9. Privacy/publication control

Apply `evidence/PUBLICATION_AND_PRIVACY_REVIEW.md` before large public rotations. Public verification and private exhibit preservation are separate functions.

## Completion condition

This phase is complete when a new reader can start from a material proposition and, without accepting the case theory in advance, determine:

1. the exact source relied upon;
2. whether that repository item is native or representational;
3. what the source directly establishes;
4. what inference is being drawn;
5. what contrary evidence exists;
6. whether expert evidence is required;
7. whether a later document supersedes the analysis;
8. which important source gaps remain.

That is the repository standard: not maximum argument, but maximum auditability of the argument that survives.

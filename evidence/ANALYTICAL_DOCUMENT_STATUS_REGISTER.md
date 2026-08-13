# Analytical Document Status Register

**Status:** CONTROLLING — document governance

## Status vocabulary

Every analytical document should ultimately carry one of these labels:

- **CONTROLLING** — current operative synthesis or evidential infrastructure.
- **SUPPORTING** — current analysis supporting a controlling proposition but not the front-door statement.
- **SUPERSEDED** — preserved for provenance; a later document controls.
- **HYPOTHESIS** — proposition under active testing; not an established conclusion.
- **PROMPT/METHODOLOGY** — research instructions or test design, not substantive evidence.
- **ARCHIVED** — historical project state no longer operative.

## Current priority classification

| Path | Status | Reason / controlling replacement |
|---|---|---|
| `CASE_ARGUMENT_AND_SURVIVING_RECORD_2026-08-13.md` | CONTROLLING | Current contracted case argument; must remain bounded by proposition matrix |
| `evidence/FACT_REGISTER_STATUS.md` | CONTROLLING | Truthful status of missing referenced v0.9 fact register |
| `evidence/SOURCE_EXHIBIT_MANIFEST.md` | CONTROLLING | Source provenance and citation infrastructure |
| `evidence/SOURCE_PROPOSITION_MATRIX.md` | CONTROLLING | Proposition-level bridge from source to prose |
| `evidence/KNOWLEDGE_DECISION_RECONSIDERATION_CHRONOLOGY.md` | CONTROLLING | Neutral chronology for cumulative-knowledge testing |
| `docs/CONTRACTED_CASE_ARGUMENT_2026-08-13.md` | SUPPORTING | Earlier contraction note; root controlling brief is later and broader |
| `docs/GOOD_UNDERSTANDING_RELIABILITY_RULING_2026-08-13.md` | SUPPORTING; filename terminology to neutralise | Useful evidential analysis; `RULING` should not be treated as adjudicative status |
| `docs/ORGANISING_MOTIVE_RULING_2026-08-13.md` | HYPOTHESIS; filename terminology to neutralise | State-of-mind analysis remains inferential and should not control source presentation |
| `docs/PATIENT_CENTRED_CAUSAL_RULING_FEET_LEVODOPA_2021_2025.md` | HYPOTHESIS/SUPPORTING; filename terminology to neutralise | Causal contribution and counterfactual timing require expert evidence |
| `docs/MANAGEMENT_PLAN_INVARIANCE_AUDIT_2017_2026.md` | SUPPORTING | Strong documentary audit; citations require path repair before counsel-facing reliance |
| `docs/COUNTERFACTUAL_IMPEACHMENT_AUDIT_CORROBORATED_BEDSIDE_PROTEST_2017_2026.md` | HYPOTHESIS | Express counterfactual; citations require path repair |
| `DEEP_DIVE_REPO_AUDIT_2026-08-12.md` | ARCHIVED | Branch/repository-state observations are historical |
| `INDEPENDENT_GPT_POLARITY_AUDIT_PROMPT_2026-08-12.md` | PROMPT/METHODOLOGY | Test design, not evidence or conclusion |
| `CONTROLLING_RECONSTRUCTION_2026-08-12.md` | SUPERSEDED | Later `CASE_ARGUMENT_AND_SURVIVING_RECORD_2026-08-13.md` controls |
| `CONTROLLING_RECONSTRUCTION_SUPPLEMENT_REASONING_2026-08-12.md` | SUPERSEDED | Later contracted case and matrices control |
| `CURRENT_CASE_POSITION_2026-08-13.md` | SUPPORTING | Broad case state; not the current front door |

## Mandatory banner for superseded material

Where practical, a superseded document should begin:

> **STATUS: SUPERSEDED — preserved for provenance. Do not rely on this document as the current case statement. See `CASE_ARGUMENT_AND_SURVIVING_RECORD_2026-08-13.md` and `evidence/SOURCE_PROPOSITION_MATRIX.md`.**

## Naming rule going forward

Counsel/expert-facing filenames should prefer neutral evidential terms such as:

- `..._EVIDENTIAL_ANALYSIS`
- `..._RELIABILITY_ANALYSIS`
- `..._CONTINUITY_AUDIT`
- `..._CAUSAL_HYPOTHESIS`

Avoid `RULING`, `KNOWING`, `RECKLESS`, `MOTIVE` or `IMPEACHMENT` in new counsel-facing filenames unless the document is expressly an internal adversarial test and labelled as such.

Existing filenames should not be deleted merely for terminology. Preserve provenance; create neutral successor documents or add status banners when substantive editing is next undertaken.

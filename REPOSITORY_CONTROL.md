# Repository Control

**Status:** CONTROLLING — evidential repository governance
**Effective date:** 13 August 2026

## Governing order

> **Preserve first, normalise second, analyse third.**

The original or best available source remains controlling. A repository representation, transcription, normalised text, consolidated corpus, evidence unit, proposition or analytical document never silently replaces it.

## Evidential chain

> **No analytical sentence without a proposition; no proposition without identified evidence units; no evidence unit without a source; no source representation mistaken for the native exhibit.**

This is the target state. Legacy analysis that predates EUID assignment remains usable only with its present source citations and status label while migration continues.

## Layer controls

| Layer | Function | Controlling rule |
|---|---|---|
| `sources/original-private-reference/` | Private-reference register only | Never commit an unredacted native exhibit to this public repository. |
| `sources/public-representations/` | Stable public redacted representations | A representation must state whether it is native text, OCR, transcription or partial transcription. |
| `sources/normalized/` | Search/readability derivative | Every alteration from verbatim text must appear in a change log. |
| `sources/consolidated/` | Ordered derived corpora | Every corpus must declare inputs, order, representation type, generation date, commit and hashes. |
| `evidence/atomic-units/` | Permanent EUID ledger | Assigned IDs never change or disappear without a deprecation record. |
| `evidence/fact-register/` | Atomic documentary facts | No legal, clinical or state-of-mind conclusion is permitted as an atomic fact. |
| `evidence/proposition-matrix/` | Tested propositions | Each material proposition must expose support, contrary material, inference level and expert dependence. |
| `analysis/` | Interpretation | Every document must declare a governance status. |

The existing `docs/source-records/` directory remains the controlling public representation location during migration. It is not duplicated merely to make the target hierarchy look complete. `sources/public-representations/README.md` maps that transitional state.

## Page-locator rule

Unverified page claims are prohibited.

- Use `Native page: UNMAPPED` until a native exhibit has been independently mapped.
- A page identified by the patient must be recorded as `Patient-supplied locator: p.X; pending verification against the native exhibit.`
- Use `Native page: p.X (VERIFIED)` only when the manifest identifies the mapped native exhibit and verification record.
- Repository line locators may be retained because they point to a fixed representation, but they are not native pagination.

No literal `Printed p. X` locator was found outside the archive when this control was installed. The validator prevents one being introduced silently.

## Source IDs and EUIDs

Source IDs are permanent documentary identifiers. EUIDs identify statement units, not grammatical sentences.

Canonical EUID syntax:

```text
SOURCE-DATE_OR_SECTION-SEQUENCE[INSERTION]
```

Examples:

```text
DS17-GEN-0001
N18-20180424-0034
N18-20180424-0034A
N25-20250310-0023
REB25-20250325-0048
```

The sequence is four digits. An omitted unit restored later receives an uppercase insertion suffix; later units are not renumbered. A deprecated EUID remains in `evidence/atomic-units/deprecations.csv` and must state its successor or clerical reason.

## Verbatim and normalised text

`verbatim` preserves spelling, syntax, punctuation, OCR damage, meaningful headings and fragments. `normalized` exists only for search and readability. Clinically significant wording is never silently repaired. The `display` layer may redact but must not alter meaning.

## Analytical boundary

EUID metadata is clerical. It must not contain conclusions about negligence, causation, dishonesty, motive, clinical correctness or legal effect. Those belong in the proposition and analysis layers.

The reported bedside protest remains patient evidence requiring its own EUID when the underlying later account is materialised. Absence from the accessible discharge representation is not proof that the protest did not occur; lack of independent contemporaneous corroboration is a separate evidential limitation.

## Preservation and change control

1. Existing source representations are not deleted or overwritten to create a consolidated corpus.
2. Every consolidated corpus declares that originals and source representations remain controlling.
3. Every source used by a consolidated unit must appear in the machine-readable manifest.
4. Every normalized alteration must have a change-log entry.
5. Every analytical document must be classified under the status vocabulary in `evidence/ANALYTICAL_DOCUMENT_STATUS_REGISTER.md`.
6. Public-site updates follow evidence-layer validation, not the reverse.

## Current generated products

- `sources/consolidated/evidence-corpus.md` — all 47 registered source representations with EUIDs.
- `sources/consolidated/clinical-corpus.md` — clinical subset in controlled chronological order.
- `evidence/chronology/medication-chronology.csv` — clerically extracted medication events requiring source-level verification before analytical use.
- `evidence/chronology/knowledge-chronology.csv` — actor/source receipt and recording events without inference of subjective reading or agreement.
- `evidence/narrative-comparison/comparison-corpus.csv` — manually calibrated literal comparisons linked to analysis elsewhere.

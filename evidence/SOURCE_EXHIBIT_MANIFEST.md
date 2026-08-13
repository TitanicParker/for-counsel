# Source and Exhibit Manifest

**Status:** CONTROLLING — provenance and citation infrastructure  
**Created:** 13 August 2026

## Purpose

This manifest is the bridge between repository source pages and analytical propositions. It distinguishes a repository transcript/publication page from the native exhibit and prevents either from silently acquiring evidential status it does not possess.

A source ID identifies a documentary source, not a conclusion.

## Citation rule

Counsel-facing analysis should cite:

> **Source ID — native page/section if known — repository representation**

Where native pagination is not presently recoverable, say so rather than inventing it.

## Core source spine

| Source ID | Date / author / recipient | Native document held? | Repository representation | Transcription / publication status | Integrity reference | Direct evidential role | Principal limitation |
|---|---|---|---|---|---|---|---|
| GP-2017-REF | c. 29 Jun 2017; GP → hospital | Not established by this manifest | `docs/source-records/gp-referral.html` | Redacted publication/transcript page | Git blob `16a9129631c6b2f6bdd5d8e3b77704230ecfe950` | What the GP referral presented to hospital: gait/tone/dexterity/functional concerns | Repository page is not itself proof of native-file custody or completeness |
| DS-2017 | Jul 2017; GUH discharge summary / patient-GP communication | Native-source custody not established here | `docs/source-records/discharge-summary.html` | Redacted documentary publication page preserving clinical sequence | Git blob `b9f5f21e23015648e0b452852ecf619812bf3c27` | Contemporaneous discharge reasoning, findings, treatment architecture, patient-position wording | Redacted/transcribed representation; native page numbering and preservation exhibit still need explicit mapping |
| MH-2017 | 2017; Monaghan → Healy | Source image located and visually inspected; preservation-quality exhibit not yet mirrored | `docs/source-records/clinician-to-healy-2017-myself-and-tim.md` | Faithful redacted transcription of visible correspondence | Git blob `706f70163b9dee56d729a464660afc7d42b3ebab` | Pre-existing Galway position; request for genetics/second opinion; wording of question to Healy | Exact date not visible on reproduced page; image remains controlling |
| HEALY-2017 | 12 Sep 2017; Healy → Monaghan | Photographed signed/typed letter supplied and visually inspected; preservation-quality exhibit not yet mirrored | `docs/source-records/healy-response-2017-09-12.md` | Redacted **partial** transcription of clearly legible passages | Git blob `e182f90e484b33d38d9d8a90a7cd70a6b73f973b` | Healy's own probable-PARK-II assessment, testing recommendation, and dopamine-replacement wording | Partial transcript; photographed original controls unclear/untranscribed passages |
| N18 | 2018; Neurology record | Native custody not established here | `docs/source-records/neurology-notes-2018.html` | Redacted source publication/transcript | Repository path is controlling representation pending manifest checksum expansion | Procyclidine withdrawal/restoration history, suspected PARK2/PRKN, treatment reasoning | Must distinguish clinician observation from patient-reported medication effects |
| N20 | 2020; Neurology record | Native custody not established here | `docs/source-records/neurology-notes-2020.html` | Redacted source publication/transcript | Repository path | Recorded foot-throw/parkinsonian assessment and contemporaneous clinical state | Clinical opinion is evidence of the opinion, not automatic proof of mechanism |
| N21 | 2021; Neurology record | Native custody not established here | `docs/source-records/neurology-notes-2021.html` | Redacted source publication/transcript | Repository path | Sinemet initiation/titration and contemporaneous constraints | Does not by absence alone prove that no unrecorded foot-centred reasoning occurred |
| N23 | 2023; Neurology record | Native custody not established here | `docs/source-records/neurology-notes-2023.html` | Redacted source publication/transcript | Repository path | OFF/dystonia/undertreatment and clinician-patient causal `misalignment` material | Mixed source types within notes require proposition-level attribution |
| N25 | 2025; Neurology record | Native custody not established here | `docs/source-records/neurology-notes-2025.html` | Redacted source publication/transcript | Repository path | Morning/overnight foot history, Sinemet response, CR prescribing | Treatment response does not by itself prove a unitary neurological generator |
| MON-2025-MC | 29 Jul 2025; Monaghan → Medical Council | Repository representation held; native exhibit status to be verified | `docs/source-records/medical-council-monaghan-response-2025-07-29.md` | Redacted source representation | Repository path | Later clinician account of history, rationale and responsibility | Primary for what was represented in 2025; derivative for earlier historical events |
| COUN-2025 | 7 May 2025; Counihan response | Repository representation held; native exhibit status to be verified | `docs/source-records/counihan-response-2025-05-07.md` | Redacted source representation | Git blob `676631b1320e84507fd9740b0ee7e6b0245a3063` | Counihan's later account of his involvement | Later representation; does not independently prove scope of 2017 involvement |
| SIMT-2025 | Sep 2025; SIMT outcome | Repository representation held; native exhibit status to be verified | `docs/source-records/simt-outcome-signed-2025-09-01.md` and `docs/source-records/simt-outcome-2025-09-03.md` | Redacted institutional source representation | Repository paths | Institutional outcome and reasoning at that date | Does not independently validate historical facts unless source independence is demonstrated |
| PRKN-2026 | 4 Feb 2026; genetics result | Repository representation held; native exhibit status to be verified | `docs/source-records/genetics-prkn-2026-02-04.md` | Redacted source representation | Repository path | 2026 genetic result | Cannot be imposed retrospectively as proof of what clinicians should have known in 2017 |

## Manifest expansion rule

Every source used in a controlling proposition should eventually receive a row containing:

- stable Source ID;
- date, author and recipient;
- native document custody status;
- exact repository representation;
- transcript status: full / partial / OCR / manually checked;
- redaction categories;
- native page count and cited page if known;
- SHA-256 of the preservation file where a native/redacted binary is held;
- Git blob SHA of the repository representation;
- direct evidential role;
- express limitations;
- supersession/acquisition status.

Git blob SHAs are repository-integrity references. They are **not substitutes for SHA-256 hashes of native exhibits**.

## Native-versus-transcript rule

A transcript may be primary evidence of what the project transcribed, but the underlying native image/PDF remains controlling where available. Unclear text must be marked unclear; it must not be silently regularised to fit an analytical proposition.

## Source-genealogy rule

A later letter, regulator decision or institutional report can be primary evidence of what that later actor said or decided. It is not independent proof of an earlier event merely because it repeats an earlier clinician account.

## Acquisition status

The Healy substantive response is **acquired** as a directly inspected photographed source and partial transcript. It must no longer be described as a missing substantive source. A preservation-quality native/redacted exhibit remains outstanding.

The original written Podiatry referral and native Podiatry service records remain distinct acquisition questions; the 6 July 2017 GP Podiatry note does not substitute for them.

## Next manifest work

This table should be expanded source-by-source before the final counsel memorandum. No analytical conclusion should be weakened or strengthened merely to fill a manifest field: unknown provenance must remain `unknown / not established` until verified.

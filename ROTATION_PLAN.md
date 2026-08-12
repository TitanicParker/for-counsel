# Counsel Site Rotation Plan

**Status:** active migration plan  
**Branch:** `agent/counsel-site-rotation`  
**Starting point:** `agent/source-extraction-genealogy` at `240033c423f81e1b1d239bc5225a586cf3de07ca`  
**Default branch protected during build:** `main` remains unchanged until the replacement presentation and archive paths are both complete and verified.

## Purpose

The repository is being rotated from a first-generation counsel presentation into a second-generation counsel instrument.

The first-generation site on `main` contains useful human-facing prose and conceptual language, but it predates the source-genealogy work, the expanded source library, the current evidential discipline, and the proposition-level fact architecture. The source-extraction branch contains the evidential machinery, but it is not itself an appropriate landing experience for counsel.

The target state combines the strengths of both:

> **Readable prose at the surface; proposition-level proof underneath; full source genealogy beneath that.**

Counsel should be able to read the case naturally without holding a taxonomy in memory. A sceptical reader should also be able to descend from any consequential proposition to its fact IDs, then to the controlling source and source-status notes.

## Non-negotiable migration rule: no intentional 404 stage

No currently public path is to be removed before both of the following are true:

1. its preserved archival destination exists and resolves; and
2. its replacement or compatibility page exists and resolves.

The sequence is therefore always:

**create destination → verify destination → create replacement/compatibility route → verify route → only then retire or repurpose the former page.**

Where a historical page is replaced at the same URL, the old page will first be copied into the visible archive. Where practical, old URLs will remain as compatibility pages rather than disappearing.

## Evidential writing rule

The presentation layer will be built in this order:

**SOURCE → FACT → PROPOSITION → PROSE**

The 283-fact register is the factual substrate. It is not the reader-facing narrative. The presentation will derive a smaller set of controlling propositions, each expressly mapped to supporting and qualifying fact IDs.

No narrative proposition may silently outrun the source architecture.

The prose may be compelling. It must also remain capable of distinguishing:

- documentary fact;
- patient account;
- clinical opinion;
- inference;
- adverse/qualifying fact;
- expert question;
- unknown/source required.

## Governing narrative direction

The second-generation site will not open by asking the reader to learn an abstract theory such as “corrigibility.” It will begin with the documentary sequence.

The present central formulation is:

> The case concerns what happened when a clinically plausible Parkinsonian diagnosis became the operative framework for care while important questions within the same presentation — particularly aetiology and the relationship of the painful foot/lower-limb syndrome to the neurological disorder — remained unresolved. The completed record later gathered additional evidence into that framework. The question for expert and legal review is whether the resulting classification remained sufficiently provisional and capable of reconsideration as the evidence developed.

The key structural concept is **premature administrative crystallization**, used as a hypothesis to test rather than a concluded breach:

- severe Parkinsonism was recognised;
- Parkinson's disease became the operative framework;
- significant aetiological and foot/lower-limb uncertainty remained in the same record;
- podiatry became an operative pathway while the neurological relationship was recorded as “Not clear”;
- treatment deferral, LTI, work advice, follow-up and patient-facing explanation were organised inside the Parkinsonian framework;
- the final discharge artefact is cumulative and includes later information, including post-discharge DaTSCAN material;
- later treatment-response and genetic evidence provide reasons to ask when the unresolved classification should have been reconsidered.

This is not to be written as proof that Parkinsonism was false, that all foot pain was dystonia, that podiatry was necessarily wrong, that levodopa deferral was negligent, or that any clinician acted dishonestly.

## Target repository layers

### 1. Human-facing counsel presentation

Primary pages under `docs/` should form a continuous reading path rather than a dashboard of arguments.

Provisional structure:

- `docs/index.html` — orientation / opening narrative
- `docs/the-case.html` — concise full case narrative
- `docs/2017-hinge.html` — referral, inpatient assessment, cumulative discharge artefact, operative diagnosis, podiatry hinge
- `docs/treatment-response.html` — 2017 withdrawal / 2018 record and later pharmacological modifiability
- `docs/longitudinal-return.html` — 2020–2024 re-entry of feet/lower limbs into neurology
- `docs/march-2025.html` — severe morning foot problem, deliberate Sinemet CR intervention, experienced response, complaint/knowledge event
- `docs/genetics.html` — early PRKN hypothesis and later 2026 confirmation, with strict hindsight boundary
- `docs/institutional-response.html` — complaint, IMF/PAR/SIMT and what source architecture is or is not presently demonstrated
- `docs/evidence-that-qualifies.html` — strongest adverse and qualifying evidence
- `docs/issues-for-counsel.html` — questions requiring legal/expert determination
- `docs/evidence-map.html` — controlling propositions with fact IDs
- `docs/fact-register.html` — human-facing access to the full fact substrate
- `docs/source-library.html` — route into source records

Navigation should remain sparse and human:

**The Case · Evidence · Issues for Counsel · Evidence That Qualifies · Source Library · Fact Register**

Long-form pages should end with a simple next-page continuation so the reader can trace the case without deciding where to go next.

### 2. Proposition layer

Create a proposition map between the atomic fact register and the narrative.

Likely controlling propositions include:

1. the feet were within the accepted presenting problem;
2. severe Parkinsonism was genuinely established;
3. the neurological relationship of the painful foot/lower-limb syndrome remained expressly unresolved in the 2017 record;
4. podiatry became an operative pathway during that unresolved state;
5. the discharge artefact is cumulative rather than a single decision-state snapshot;
6. treatment caution was deliberate and clinically reasoned;
7. PRKN/PARK2 was a contemporaneous causal possibility, not a hindsight invention;
8. at least part of the foot/lower-limb phenomenon demonstrated neurological pharmacological modifiability early in the course;
9. later years contain mixed evidence and do not support a blanket all-foot-pain dystonia theory;
10. by 2023 the record expressly recognises interpretive misalignment around the feet;
11. the March 2025 Sinemet CR intervention was deliberately directed to the severe morning experience including pain;
12. the March 2025 response changed the patient's understanding and is relevant to knowledge/limitation chronology;
13. the 2026 PRKN result supplies later etiological coherence to Parkinsonism and dystonia without deciding every historical foot symptom;
14. later governance outcomes presently lack a fully available proposition-level source architecture because the complete PAR/SIMT source pack is not held;
15. significant adverse/qualifying evidence remains and must be visible to counsel.

Every proposition will identify support, qualification, source limitations, and any expert dependency.

### 3. Source library

`docs/source-records/` remains evidence, not advocacy.

Existing source pages are not to be stylistically rewritten to improve the case. Where an item is only an abstract/index entry rather than a faithful transcript, that status must be made explicit.

The original/native source remains controlling wherever the repository contains a transcript, reproduction or derivative source bundle.

### 4. Audit layer

`evidence-audit/` remains the engine room and is not the default counsel landing experience.

It will continue to contain:

- source inventory;
- source genealogy;
- source packs/chains;
- acquisition status;
- knowledge/gaps;
- migration/source-structure material.

`PROJECT_ORIENTATION.md` remains an internal/editorial navigation document.

## Archive strategy

The first-generation Main presentation will be preserved visibly under:

`archive/main-presentation-pre-rotation-2026-08-11/`

The archive will contain the former presentation pages and an `ARCHIVE_NOTE.md` explaining:

- what the archive is;
- the commit from which it was preserved;
- that it is superseded presentation/analysis, not a primary evidence source;
- that useful language may have been harvested into later pages only after revalidation against the source/fact architecture.

Primary source records will **not** be duplicated merely to make the archive self-contained. Historical presentation pages may link to the live source library where sensible.

The archive is for provenance, not for maintaining a second competing evidential corpus.

## What is salvageable from the first-generation Main presentation

The following ideas may be retained after revalidation and, where necessary, softened:

- this is not a simple hindsight-misdiagnosis case;
- documentation is not the same thing as corrigibility;
- plausibility of Parkinsonism is not proof that the foot/podiatry question was resolved;
- the patient was extensively documented and counselled rather than simply ignored;
- patient-facing specialist information matters to reliance and knowledge;
- PRKN was within the early diagnostic architecture;
- DBS should be analysed as information actually supplied, without assuming the patient was necessarily a DBS candidate;
- later evidence raises a reopening-threshold question;
- the strongest case must visibly include the evidence that cuts the other way.

The following formulations are not to be carried forward as factual conclusions without a separately supported proposition:

- “containment” as motive or proved institutional mechanism;
- “refused to reopen”;
- “premature closure” as an already-established breach;
- claims that Procyclidine proves the feet were neurological in their entirety;
- claims that the record itself proves negligence;
- claims that later genetics proves what clinicians should have known in 2017;
- claims of dishonesty, bad faith, conspiracy or concealment.

## Presentation style

The intended reader is a human professional.

Pages should therefore use:

- continuous explanatory prose;
- clear chronological transitions;
- quotations only where the original words carry genuine evidential force;
- restrained callouts;
- generous reading width and typography;
- evidence notes immediately adjacent to consequential propositions;
- no requirement that the reader memorise labels, rails, locks or a taxonomy before the chronology is intelligible.

The prose should repeatedly tell the reader what a source **does not** prove where that boundary is important, without drowning documentary facts in generic caveats.

## Evidence annotation model

A consequential paragraph should be able to carry a discreet reference such as:

`Evidence: F0023 · F0024 · F0033`

The fact IDs should lead to a human-facing fact view containing:

- exact proposition;
- fact type/status;
- source;
- source-status/provenance note;
- qualification/adverse evidence;
- link to the source page.

The narrative should never be replaced by fact-ID algebra. The fact system is a proof layer beneath prose.

## Migration phases

### Phase 1 — Freeze and plan

- create this plan;
- create the rotation branch from the consolidated evidential branch;
- make no change to `main` yet.

### Phase 2 — Preserve Main presentation

- inventory every presentation page currently exposed on `main`;
- copy those pages into the visible archive path;
- create archive note/index;
- verify archived destinations before any public page is replaced.

### Phase 3 — Install factual/proposition substrate

- materialise the controlling F0001–F0283 register in the repository if not already present as a permanent file;
- create proposition map;
- create fact-to-source index;
- link the substrate from `PROJECT_ORIENTATION.md` and the audit README.

### Phase 4 — Build second-generation counsel pages

- draft chronology-led pages on the rotation branch;
- map every consequential passage to proposition/fact support;
- include qualifying/adverse evidence in the narrative rather than leaving it hidden in audit notes;
- build source-library and fact-register landing pages;
- keep compatibility with existing public URLs wherever possible.

### Phase 5 — Link and route verification

- inspect all internal links;
- verify new paths and archive paths exist;
- ensure every former public URL either remains live or resolves to a compatibility page;
- do not remove a path merely because its content has moved.

### Phase 6 — Review before Main rotation

Before any merge/update of `main`, conduct a source-discipline review asking:

- Does any prose convert inference into fact?
- Is any institutional repetition being treated as independent corroboration?
- Is the podiatry hinge overstated before the SAR is received?
- Is 2026 genetics being back-projected?
- Is March 2025 knowledge/limitation evidence visible?
- Is the 2023 off-medication adverse evidence visible?
- Are reasonable treatment-caution explanations visible?
- Does the SIMT section distinguish a no-deficit outcome from demonstrated independent proposition-level revalidation?
- Are source abstracts labelled honestly?

### Phase 7 — Rotate Main

Only after the archive and replacement site are complete:

- preserve the pre-rotation Main presentation under the archive path;
- replace the public presentation with the second-generation pages;
- retain compatibility routes for old URLs;
- keep source/audit paths stable;
- verify the live tree immediately after rotation.

## Current high-value source gaps

The migration is not dependent on pretending these records exist. They remain explicit evidence-acquisition gaps:

- original 2017 Podiatry referral;
- complete Podiatry pathway and closure/disposition record;
- complete PAR and source schedule/attachments;
- SIMT agenda/minutes/source pack;
- native EHR/discharge version history;
- native Complex Case Meeting material;
- any separate Dan Healy reply/report not already reproduced;
- internal Article 18 operational/audit trail;
- any separately held trainee/teaching records.

If any arrive during the rotation, they are to be ingested first through source preservation/fact extraction and only then allowed to change the narrative.

## Definition of done

The rotation is complete when:

1. the first-generation Main presentation is visibly archived;
2. no intentionally retired public URL returns 404;
3. the source library remains stable and directly accessible;
4. the full fact register is permanently stored and accessible;
5. the controlling proposition map is complete;
6. the counsel site can be read linearly by a human professional without needing the audit files;
7. consequential prose can be traced back through proposition → fact → source;
8. adverse evidence is presented with the case rather than concealed;
9. missing evidence is identified as missing rather than assumed absent;
10. `main` is changed only after the complete replacement has been verified on the rotation branch.

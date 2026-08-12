# Independent GPT Polarity Audit Prompt — 12 August 2026

Use this prompt with an independent GPT that has access to the GitHub repository `TitanicParker/for-counsel`.

---

You are being asked to perform an **independent documentary polarity audit** of a medical-neurology case repository.

Repository: `TitanicParker/for-counsel`

Do not assume the repository's case theory is correct. Do not adopt its conclusions merely because they are written there. Treat the repository as an evidential corpus containing primary-source transcriptions, patient-source material, propositions, analysis and public-facing prose of differing evidential weight.

Your task is to determine whether the documents themselves disclose a meaningful **polarity, tension, unresolved contradiction or path-dependent split** between the treating neurologist's evolving etiological understanding and the treatment architecture that governed the patient.

## Core situation to test

A 39-year-old patient presents to Neurology for the first time in July 2017 after a possible long symptom history. The admission documents severe young-onset, markedly symmetrical Parkinsonism and a lower-limb/gait abnormality described as partly dystonic-looking. Structural foot disease is also present and the relationship between the feet/lower limbs and the neurological syndrome is recorded as `Not clear`.

Very early in the admission, a conservative treatment position is adopted: levodopa/dopamine replacement is to be held back because of the patient's young age and concern about dyskinesia, impulse-control disorder and dopamine dysregulation. Contemporaneous correspondence from the treating neurologist to Prof Daniel Healy says:

`Myself and Tim are keen to hold back on Levodopa insofar as maybe possible unless you'd advise otherwise?`

No levodopa challenge occurs during that admission.

By 6 July 2017 the GP record says Podiatry has been telephoned and the case will be prioritised `as Parkinson's`. By 9 July Parkinson's disease is already being used administratively for Long Term Illness certification. On 13 July the DaTSCAN is abnormal `as was expected`; the referral itself had already described the walk as `almost dystonically unusual` and suspected autosomal-recessive Parkinsonism.

In September 2017 Prof Healy personally reviews the patient and writes:

`I think probably has Park II and I would suggest testing that initially. If it is negative I would go on to test a panel.`

He also writes that PARK II patients:

`tend to manage quite well for long periods of time with relatively low doses of Dopamine replacement therapy. They can become quite dyskinetic if over-used.`

Do not automatically label this a direct instruction to start levodopa. Determine for yourself whether this is materially different from the pre-existing policy of holding dopamine replacement back insofar as possible.

In April 2018 the treating neurologist records that PARK2/PRKN is what `we/Prof Healy suspect is the cause` and opens the genetics discussion with:

`Obviously I'd be particularly interested to know`

but also records:

`It doesn't particularly change current management - so there is no great loss in "not knowing" currently right now.`

The same 2018 record says the patient could `obviously ... be very much better` if levodopa or another dopamine agonist were given, while also saying:

`we do not want to do that - at least for quite some time.`

In March 2025 the treating neurologist's complaint response states that the belief and understanding is that the patient has **idiopathic Parkinson's disease**.

In February 2026 St Vincent's reports two pathogenic Parkin variants and states that the patient's **Parkinsonism and dystonia are due to compound heterozygous mutations in the Parkin gene**.

## What you must do

Read the repository broadly before answering. At minimum inspect:

- `docs/source-records/discharge-summary.html`
- `docs/source-records/clinician-to-healy-2017-myself-and-tim.md`
- `docs/source-records/healy-response-2017-09-12.md`
- `docs/source-records/gp-podiatry-2017-07-06.md`
- `docs/source-records/neurology-notes-2018.html`
- `docs/source-records/official-rebuttal.html`
- `docs/source-records/genetics-prkn-2026-02-04.md`
- `evidence/CURRENT_DOCUMENTARY_FACTS_AND_EXPERT_QUESTIONS_2026-08-12.md`
- `evidence/PROPOSITION_MAP.md`
- `CONTROLLING_RECONSTRUCTION_2026-08-12.md`

Also inspect contrary/qualifying evidence and do not assume every historical foot symptom was dystonia or Parkinsonian.

## Questions to answer

1. Does the documentary record show a genuine polarity between **etiological pull toward PARK2/PRKN** and **management continuity under a pre-existing levodopa-deferral policy**?

2. If yes, identify the exact documents and wording that create that polarity. Separate contemporaneous primary-source wording from later retrospective wording.

3. Is the treating neurologist's 2018 position medically/documentarily coherent as a legitimate separation between `what disease is this?` and `how should I treat it?`, or does the record show that the etiological answer was being treated as management-neutral in a way that requires explanation?

4. Does Healy's September 2017 treatment wording amount to:
   - endorsement of the existing hold-back policy;
   - a materially different cautious-treatment model;
   - a counter-recommendation;
   - or something too ambiguous to classify?
   Explain why.

5. Does the record show that Healy's September 2017 opinion was **ignored**, or is the safer proposition that there is no presently visible documented process showing how it was reconciled with the earlier policy? Be exact.

6. Once levodopa was deliberately excluded from the admission, did that decision alter the **epistemic environment** by preventing dopaminergic-response information from being generated? Distinguish what the documents prove from what requires expert opinion.

7. Does the 6 July Podiatry entry `as Parkinson's`, combined with the unresolved `Not clear` foot/lower-limb relationship, reveal an unusual operational split between diagnostic uncertainty and pathway certainty?

8. What is the strongest explanation **for** the clinicians' conduct that preserves medical coherence? Give the best benign/defensive interpretation.

9. What is the strongest explanation **against** the clinicians' conduct if the documents are read as a path-dependent failure to reopen the original decision?

10. Does the March 2025 assertion of idiopathic Parkinson's disease create a separate polarity against the earlier `probably PARK II` / `we/Prof Healy suspect is the cause` record? Is there any documented bridge explaining that transition?

11. Is there evidence that the treating neurologist is, in effect, `talking out of both sides of his mouth`, or is that phrase too loaded? Translate the issue into neutral forensic language and state whether the documents support it.

12. Identify the single strongest documentary passage for each of these four states:
   - early treatment lock;
   - etiological pull toward PARK2;
   - management-indifference to knowing the genotype;
   - later retrospective IPD certainty.

## Output format

Start with a one-paragraph conclusion headed **Independent finding**.

Then provide:

### A. Documentary polarity detected / not detected
State yes, no, or indeterminate and explain briefly.

### B. The two poles
Set out the strongest source-grounded formulation of each pole.

### C. Chronology of the polarity
Trace July 2017 → September 2017 → April 2018 → March 2025 → February 2026.

### D. Best benign interpretation
Give the strongest medically coherent explanation for why a clinician could suspect PARK2 yet regard confirmation as not changing current management.

### E. Best critical interpretation
Give the strongest source-disciplined explanation for why the treatment architecture may have become insulated from new etiological information.

### F. Missing bridge
Identify what document, note, meeting record, test result or specialist reasoning would be expected if the apparent polarity had actually been reconciled.

### G. Expert questions
List the medical questions that cannot be resolved from documents alone.

### H. Confidence and boundaries
State what is established, what is inference, and what remains unproven.

## Important discipline

Do not infer dishonesty, motive, concealment or bad faith from inconsistency alone.

Do not say PRKN was `missed` if the documents show it was suspected.

Do not say Healy ordered levodopa unless the source actually says that.

Do not say all foot symptoms were dystonia.

Do not treat the DaTSCAN as a genetic discriminator between idiopathic Parkinson's disease and PRKN disease.

Do not treat later genetic confirmation as proof of the 2017 standard of care.

The core issue to test is narrower:

> **Did an early conservative treatment decision become sufficiently controlling that subsequent etiological information — including a specialist opinion of probable PARK2 — was absorbed without reopening the treatment architecture, leaving the treating neurologist simultaneously interested in proving PARK2 and treating the answer as not materially relevant to current management?**

Answer from the documents, not from the repository's rhetoric.

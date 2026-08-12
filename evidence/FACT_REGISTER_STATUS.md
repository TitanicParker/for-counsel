# Evidential Fact Register — Control Note

**Controlling register:** `clean_case_evidential_fact_register_v09.md`  
**Current fact range:** F0001–F0283  
**Status:** provisional fact-extraction freeze  
**Freeze date:** 11 August 2026

## Role in the rotated counsel site

The fact register is the atomic documentary substrate for the second-generation counsel presentation.

It is not a pleading, narrative or case theory. Its job is to record the smallest proposition an identified source supports at the level actually established, while preserving source genealogy, qualification, adverse material and missing-source boundaries.

The presentation layer is to be generated in the following order:

**SOURCE → DOCUMENTARY FACT → TESTED PROPOSITION → PROSE**

No new analytical writing is itself a reason to create a new fact ID.

## Controlling discipline

The register distinguishes:

- source-native documentary fact from substantive truth;
- direct observation from patient-reported history;
- clinical opinion from objective result;
- later representation from the earlier event it describes;
- institutional act from the historical facts relied upon;
- independent evidential origin from repetition;
- missing source from proof of non-occurrence.

The default substantive status remains `DOCUMENTARY_ONLY` unless an entry expressly carries a stronger status.

## Freeze rule

Absent a genuinely new source, newly materialised native version, or disclosure that changes source genealogy, the fact-extraction phase is provisionally frozen at **F0283**.

The principal anticipated source event capable of reopening this layer materially is the outstanding Podiatry disclosure. Other high-value disclosure-only gaps remain the complete PAR/SIMT source architecture, native EHR/version history, Complex Case material, any separate Healy response/report, Article 18 operational records and any separately held trainee/teaching material.

## Migration note

The full v0.9 register was supplied to the project as a standalone source file and is the controlling working register for the rotation. Until it is mirrored here byte-for-byte, this control note prevents any intermediate proposition map or counsel prose from being mistaken for the full atomic register.

When the full register is mirrored into this repository, preserve the F0001–F0283 IDs exactly. Do not renumber, collapse or silently rewrite entries.

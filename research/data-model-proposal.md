# Data model proposal: sources, disclosure events, claims, findings

Status: proposal for decision by the project owner, 17 November 2026. Nothing here changes existing files; a first draft of the new layer is in [cases/covid-origins/disclosures.csv](../cases/covid-origins/disclosures.csv) with machine-readable metadata in [disclosures.csv-metadata.json](../cases/covid-origins/disclosures.csv-metadata.json).

## Problem

The project's subject is the process by which evidence reaches the public. The repository records that process in three places that overlap:

1. **Dossier layer:** `findings/*.md` (narrative), `data/claims.csv` (C-IDs) and `sources/register.json` (S-IDs).
2. **Audit layer:** `framework/controls.csv` (D-controls) and `cases/covid-origins/findings.csv` (F-IDs, graded against controls).
3. **Disclosure events:** proposed, not yet built.

Dates of release, release routes and claims of novelty appear in prose (`docs/timeline.md`, `research/slack-release-provenance.md`), in source `limitations` fields and in finding text. Nothing records them as data. So the project can't yet answer process questions such as "which evidence became public only through a third party?" or "what is still outstanding, and since when?"

## Proposed model

```
source (S) ──documents──▶ disclosure event (DE) ──supports──▶ claim (C) ──graded as──▶ finding (F) ──against──▶ control (D)
                              │                                                         ▲
                              └──────────────────────engages─────────────────────────────┘
```

| Layer | What one record is | ID scheme | Canonical file |
| --- | --- | --- | --- |
| Source | A document as published: bibliographic data, access and review notes | `S01`… (existing, unchanged) | `sources/register.json` |
| Disclosure event | One release action, correction or documented unmet request: when and how evidence became public, or did not | `DE-YYYY-NNN` (new) | `cases/<case>/disclosures.csv` |
| Claim | A statement the project says the evidence supports, with its limits | `C01`… (existing) | `data/claims.csv` (see migration) |
| Finding | One actor's performance against one control, graded | `F01`… (existing) | `cases/<case>/findings.csv` |
| Control | A reusable disclosure obligation | `D.n.n` (existing) | `framework/controls.csv` |

The narrative files (`findings/*.md`, `docs/timeline.md`) become **views**. They cite IDs, and they are not canonical for any date, grade or status.

### Disclosure event fields

The fields are listed in the order of the CSV columns:

- **Identity:** `id`, `case`, `title`, `event_type` (`disclosure` | `correction` | `non-disclosure` | `statement-about-disclosure`).
- **What and who:** `evidence_described` (documents or data sets, never their content), `evidence_holder`, `releasing_party`.
- **How:** `channel` (how it reached the public: `voluntary-publication`, `official-statement`, `audit`, `administrative-action`, `legislative-release`, `court-record`, `foia`, `leak`, `journalism`, `journal-correction`, `data-repository`, `none`, `unknown`). `acquisition_route` (how the releaser got it from the holder: `own-record`, `voluntary-production`, `oversight-request`, `subpoena`, `foia`, `leak`, `unknown`). These are separate fields because a committee release (channel) may rest on voluntary production, a subpoena or a leak (route), and the record usually does not say which.
- **When:** `evidence_created`, `date_requested` and `date_disclosed`, each at its known precision (`YYYY`, `YYYY-MM` or `YYYY-MM-DD`). `date_disclosed_qualifier` (`on` | `by` | `on-or-after` | `approx` | `unknown`). `lag_days` is filled only when it can be computed exactly and is never estimated.
- **Quality of the release:** `completeness` (`full` | `partial` | `excerpt` | `summary` | `redacted` | `none` | `unknown`), `resistance` (`none-recorded` | `delayed` | `contested` | `compelled` | `refused` | `unknown`).
- **Claims about the release:** `release_claim` (what the releaser said about novelty or completeness, quoted with its source) and `release_claim_accuracy` (`accurate` | `partly-accurate` | `inaccurate` | `unverified` | `n/a`).
- **Relations:** `source_ids`, `related_event_ids` (overlapping or responsive releases), `control_ids`. During the transition also `claim_ids` and `finding_ids` (see below).
- **Housekeeping:** `status` (`public` | `partly-public` | `outstanding` | `withdrawn`), `notes` (every material unknown explained here), `reviewed_on`.

Granularity: **one event per release action**. One action may release several documents, as with the two 2025 debarment notices. Item-level matching, such as which 2026 Slack messages were already public, belongs in a child table keyed `DE-2026-001.0001`. That table would be built by the comparison in [slack-release-provenance.md](slack-release-provenance.md). The release-level event should not be split to do that work.

Non-disclosure events record documented requests that were not met, such as the WIV records and the data SAGO requested. For these, `releasing_party` is empty, `channel` is `none` and `status` is `outstanding`. They are recorded only where a body with a remit documented the request. The project's own wish for a document does not create one.

### ID scheme

`DE-YYYY-NNN`, in the spirit of CVE:

- `YYYY` is the year of disclosure. For a non-disclosure, it is the year the unmet request was first publicly documented in a registered source.
- `NNN` is assigned in registration order. It carries no meaning and is never reused or renumbered. A rejected event keeps its ID with `status` `withdrawn`.
- IDs are global across cases. The `case` column scopes them, so an event that matters to two cases is recorded once.
- Existing IDs (`S`, `C`, `F`, `D`) are kept unchanged. Where a reference crosses cases, qualify it as `covid-origins:F07`. Claim and finding IDs are case-local; source and control IDs are global.

### Direction of relations

Each relation should be stored once, on the later layer, pointing back to the earlier one:

- an event stores `source_ids`
- a claim gains `disclosure_ids`, next to its existing `source_ids`
- a finding gains `disclosure_ids`, next to its existing `evidence_source_ids` and `control_id`

The draft `disclosures.csv` also carries `claim_ids` and `finding_ids`, because it was written without editing the other files. Those two columns are **transitional**. Once claims and findings carry `disclosure_ids`, they should be dropped, or generated, to avoid two-way drift.

## Analogy with CWE / CVE / CVSS

| Security registry | Here | Notes |
| --- | --- | --- |
| CWE (weakness class) | Control (`D.n.n`) | A reusable class of process failure, independent of any case |
| CVE (specific instance with stable ID) | Disclosure event (`DE-YYYY-NNN`) | A dated, sourced instance. Non-disclosure events resemble a published vulnerability with no fix available. |
| CVE references | `source_ids` | |
| Vendor advisory / response | `actor_response` in findings | |
| CVSS (severity vector) | Optional disclosure-gap score | See below |
| Audit finding against a control | Finding (`F`) | The ISO 27001 layer; joins events to controls for one actor |

The analogy has limits. A CVE describes a flaw in a product. A disclosure event describes an act, or an omission, by a party with interests, and the record of it is often incomplete. Recording a case does not imply wrongdoing, and an event can be a positive observation, such as the OIG audit or SAGO's recorded dissent.

### Optional: disclosure-gap vector

This is optional, and it is not recommended for the first iteration. If it is built, it should be a **vector string**, like CVSS, and not a single number until the weights have been calibrated on several cases. A numeric score invites false precision about matters the project itself grades as "not evidenced".

`DGV:0.1/L:x/C:x/R:x/A:x/V:x/M:x`

| Metric | Values |
| --- | --- |
| **L** Lag (creation or request to disclosure) | N < 30 days, S < 1 year, M 1–3 years, H > 3 years, O outstanding, U unknown |
| **C** Completeness | F full, P partial or excerpt, R redacted or summary, N none, U unknown |
| **R** Resistance | N none recorded, D delayed, X contested, P compelled, F refused, U unknown |
| **A** Release-claim accuracy | A accurate, P partly accurate, I inaccurate, U unverified, X n/a |
| **V** Route | O own or voluntary, S oversight-compelled, T third party (leak or journalism), U unknown |
| **M** Materiality to an open question | H, M, L, a project judgement that must cite the open question |

Almost every metric is derivable from the CSV columns, so the vector can be generated rather than hand-entered. M is the exception, and it is the most subjective metric, which is why it is kept separate.

## Machine-readable schema: CSVW chosen over JSON Schema

The draft uses a **CSV on the Web (W3C CSVW)** metadata file, `disclosures.csv-metadata.json`. That name follows the CSVW discovery convention for `disclosures.csv`.

Why CSVW for this file:

- The canonical data is CSV, and CSVW describes CSV directly. That includes the dialect, the header and, importantly, `separator: ";"` for the list columns (`source_ids`, `control_ids`). JSON Schema validates a JSON object, so it would need a conversion step that decides how to split lists, and the schema would then describe that conversion, not the file.
- It declares the primary key, datatypes, required columns and regex formats for IDs, dates and controlled vocabularies.
- It is a W3C standard with a defined CSV-to-RDF/JSON mapping (`aboutUrl`). Events can therefore be published as linked data later without changing the CSV.
- The same approach extends to `claims.csv`, `findings.csv` and `controls.csv` as a CSVW table group.

Trade-offs: CSVW tooling is thinner than JSON Schema tooling. The Python `csvw` package validated the draft (14 rows, and invalid IDs and values are rejected). CSVW also cannot express references into `sources/register.json`, and foreign keys on list-valued columns are poorly supported. Reference integrity (S, C, F, D and DE IDs) therefore needs a short check script in CI either way. JSON Schema remains the better fit for `sources/register.json` itself, and it would be reasonable to add one there.

## Trade-offs of the model

- **Another table means more upkeep.** The upkeep buys queryable process data, which is the project's stated focus. Mitigation: a CI check, and the timeline generated from `disclosures.csv` rather than maintained by hand.
- **Unknowns dominate.** In the first draft, `lag_days` is empty for every row, `acquisition_route` is `unknown` for all five committee and journalistic releases, and no novelty or completeness claim is verified. That shows where research is needed: creation dates, request dates and how committees obtained material. The gaps should not be filled with estimates.
- **The line between event and finding.** An event records what happened in a release. A finding grades an actor against a control. Release-claim accuracy sits on the event as a fact or `unverified`. Grading the releaser for it (D.6.2) stays in findings.
- **Per-case versus global storage.** Per-case files keep cases independent. Global IDs keep cross-case references stable. The proposal takes both.

## Recommendation

1. Adopt the four-layer model. Make `disclosures.csv` canonical for *when and how evidence became public*, `sources/register.json` for *documents*, `claims.csv` for *what the evidence supports* and `findings.csv` for *grades*. Treat Markdown as views.
2. Keep every existing ID. Add `DE-YYYY-NNN` as specified.
3. Use CSVW metadata for the CSV layers, plus a short reference-integrity script.
4. Defer the disclosure-gap vector until at least one more case exists.

## Migration path (preserves existing IDs)

1. **Now:** review and correct the draft `disclosures.csv`. It cites only existing S, C, F and D IDs.
2. Add an optional `disclosure_ids` column to `cases/covid-origins/findings.csv` and to `data/claims.csv`, filled from the transitional columns. No existing column changes.
3. Add the reference-integrity check to CI, covering S, C, F, D and DE references across all files.
4. Move `data/claims.csv` to `cases/covid-origins/claims.csv` when a second case starts, keeping a stub or a note at the old path. C-IDs are unchanged.
5. Drop the transitional `claim_ids` and `finding_ids` from `disclosures.csv`, or regenerate them from the other files.
6. Generate the dated rows of `docs/timeline.md` from `disclosures.csv`. Hand-written commentary stays in Markdown.
7. Build the item-level Slack comparison as a child table of `DE-2026-001`, as described in `research/slack-release-provenance.md`.

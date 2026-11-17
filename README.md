# Wuhan Logs

A source-based log of how evidence about the origins of COVID-19 reached the public: disclosure, research oversight and public communication, tracked over time.

The case is named after the place where the pandemic was first recognised. The project takes no position on whether it began through animal spillover or a research-related incident; it tracks how evidence bearing on both was disclosed.

The disclosure controls and grading used here are in [framework/](framework/), and the graded COVID findings in [cases/covid-origins/](cases/covid-origins/). They are written to be reusable for other cases.

**Institutions should account for failures we can document, disclose relevant evidence, correct overstatements and explain how they will prevent recurrence.** These responsibilities remain whether the pandemic began through animal spillover or a research-related incident.

This initial edition was assembled on **14 November 2026**. It includes evidence, editorial assessments and proposed actions, each identified as such. It is a starting research dossier, not a completed scientific review.

## Start here

- [Timeline](docs/timeline.md): what was published, challenged and changed.
- [Evidence register](data/claims.csv): claims, status, sources and limits in a reusable table.
- [Sources](sources/README.md): annotated links, with [structured metadata](sources/register.json).
- [Open questions](research/open-questions.md): priorities and what would resolve them.

## Accountability dossiers

| Subject | Focus |
| --- | --- |
| [WHO](findings/who.md) | The 2021 assessment, subsequent corrections and institutional accountability |
| [Chinese authorities and Wuhan laboratories](findings/china-and-wuhan-labs.md) | Access to records and independent verification |
| [EcoHealth Alliance and NIH](findings/ecohealth-and-nih.md) | Reporting, oversight, responses and administrative findings |
| [Journals and Proximal Origin authors](findings/journals-and-authors.md) | Disclosure, strength of conclusions and editorial review |
| [Wikipedia](findings/wikipedia.md) | Specific updates and accurate representation of uncertainty |

## Concrete proposals

- [WHO accountability requests and acknowledgment criteria](proposals/who-accountability-requests.md)
- [Wikipedia additions and attribution fixes](proposals/wikipedia-edits.md)
- [Questions institutions should answer](proposals/accountability-questions.md)
- [Provenance of the 2023 and 2026 Slack releases](research/slack-release-provenance.md)

## What the evidence currently supports

WHO's latest assessment reviewed here continues to favour zoonotic spillover on available scientific evidence, while leaving the origin unresolved. SAGO could not adequately evaluate a laboratory-related event because key information was unavailable. That does not assign equal probabilities to the hypotheses. [S07] [S09]

The HHS inspector general documented oversight deficiencies involving NIH and EcoHealth. Those findings justify accountability independently of any claim about the pandemic's cause. [S13]

Slack messages from February to April 2020 were publicly available by July 2023. The July 2026 Senate release covers 30 April 2020 to June 2023, and a comparison found almost none of its 11,305 messages in the two 2023 collections. [S19] [S21] [S22] See the [comparison](research/slack-release-provenance.md#comparison-result-17-november-2026).

## What this project does not establish

- That SARS-CoV-2 was engineered or escaped from a named laboratory.
- That an identified individual deliberately concealed the actual origin.
- That every private doubt demonstrates a knowingly false public statement.
- That WHO never reconsidered its assessment.
- That Wikipedia omits all discussion of WHO's reassessment.
- That unavailable evidence proves what the evidence would show.
- That every message in the 2026 release was first disclosed in 2026: only the two 2023 collections were compared.

These are limits of the present record. New evidence should change the project when warranted.

## How to use this project

Read the [method](docs/methodology.md) before citing a finding. Every factual claim should lead to a source; every recommendation should be recognisable as a recommendation. Record contrary evidence and corrections with the same care as supporting evidence.

The Wikipedia text and institutional statements here are drafts. Their inclusion does not mean they have been submitted, adopted or endorsed by the organisations concerned.

Contributions: see [CONTRIBUTING.md](CONTRIBUTING.md). Changes: see [CHANGELOG.md](CHANGELOG.md).

## Maintenance

Wuhan Logs is maintained by Michiel de Jong ([michielbdejong](https://github.com/michielbdejong)). It is independent and not affiliated with any of the institutions it examines.

Dynamic sources, such as Wikipedia revisions, debarment status and outstanding data requests, are rechecked monthly. Changes are recorded in [CHANGELOG.md](CHANGELOG.md), and the source register records when each source was last reviewed.

The initial edition was AI-assisted and is being verified against its sources; see the [method](docs/methodology.md).

## Licence and citation

The repository's own text and data are licensed under [CC BY 4.0](LICENSE). Linked and quoted third-party material is not covered: it retains its original copyright and licensing terms (see [Citation and reuse](docs/methodology.md#citation-and-reuse)).

To cite the project, use the metadata in [CITATION.cff](CITATION.cff), for example: Michiel de Jong, *Wuhan Logs* (dataset, version 2026-11-17), https://github.com/michielbdejong/wuhan-logs. Cite the original sources for any factual claim.

[S07]: https://cdn.who.int/media/docs/default-source/documents/epp/sago/independent-assessment-of-the-origins-of-sars-cov-2-by-sago.pdf
[S09]: https://www.who.int/publications/m/item/covid-19-global-risk-assessment--version-10
[S13]: https://oig.hhs.gov/reports/all/2023/the-national-institutes-of-health-and-ecohealth-alliance-did-not-effectively-monitor-awards-and-subawards-resulting-in-missed-opportunities-to-oversee-research-and-other-deficiencies/
[S19]: https://oversight.house.gov/release/wenstrup-releases-alarming-new-report-on-proximal-origin-authors-nih-suppression-of-the-covid-19-lab-leak-hypothesis/
[S21]: https://www.public.news/p/covid-origins-scientist-denounces
[S22]: https://www.hsgac.senate.gov/media/reps/new-doc-drop-slack-messages-reveal-proximal-origin-authors-privately-doubted-the-science-behind-their-own-paper-coordinated-with-intelligence-community-and-nih/

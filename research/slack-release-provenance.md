# Proximal Origin Slack messages: release provenance

## Established chronology

**11 July 2023:** the House majority's dated announcement says its report included previously unrevealed Slack messages and emails. The report reproduces message excerpts. This establishes public availability by that date, without claiming the earliest disclosure of every individual message. [S19] [S20]

**20 July 2023:** Public announced publication of its cache and provided links labelled Proximal Origin Slack (47 MB) and Proximal Origin Emails (184 MB). The description of a full cache does not establish completeness of all communications. [S21]

**22 July 2026:** the Senate HSGAC majority's page announces another release. That is the page's publication date; some related reporting uses 21 July. The project has not reconciled the exact release time or compared every document. [S22]

## Comparison result (17 November 2026)

The three collections were retrieved and hashed; URLs, byte sizes, SHA-256 hashes and page counts are in the [collections manifest](../sources/collections.csv). The files themselves are not stored in this repository. [S20] [S93] [S94] [S95]

| Collection | Format | Messages dated |
| --- | --- | --- |
| Public, "Proximal Origin Slack" (20 July 2023), 140 pages | Screenshots of the channel `paper-2020-nature_medicine-proximal_origin`; no text layer, so text was extracted by OCR | 1 February to 30 April 2020 |
| House majority report (11 July 2023), 55 pages | Report quoting Slack messages | Dated Slack citations found are from February 2020 |
| Senate HSGAC majority, main file (July 2026), 1,123 pages | Text export, Bates-numbered SLACK_000216 to SLACK_001337; 11,305 messages from four authors | 30 April 2020 to 28 June 2023 |
| Senate HSGAC majority, excerpt file (July 2026), 15 pages | 140 messages | All 140 also in the main file |

**Method.** Each Senate message was parsed into timestamp, author and text. For the 9,636 messages long enough to compare (at least three five-word sequences), the share of their five-word sequences found in each 2023 collection was measured. Messages with a share of 0.5 or more (16 in all) were inspected by hand; the remaining 1,669 short messages were not compared individually. The script is in [tools/slack-compare](../tools/slack-compare/compare.py) and the candidate assessments are in [slack-comparison-candidates.csv](slack-comparison-candidates.csv).

**Result.** Two Senate messages, both from 30 April 2020, also appear in Public's 2023 cache, on the last day it covers. The other 14 candidates were coincidental: shared links, short stock phrases, or later messages quoting earlier text. One July 2020 message quotes a February 2020 message that is itself in the 2023 cache. No message dated after 30 April 2020 was found in either 2023 collection.

The 2026 main file starts at page SLACK_000216. Pages SLACK_000001 to SLACK_000215 are not in the 2026 release, and this project has not established what they contain.

**What this establishes.** The 2026 release consists almost entirely of messages that are not in the two 2023 collections compared. It continues the record from the point where Public's cache ends. The Senate page's description of the documents as newly released is consistent with this comparison.

**Limits.** OCR errors can hide matches, especially in short messages, and the Public screenshots crop some long lines. Only the two 2023 collections were compared: other publications between 2023 and 2026, such as later congressional reports or press articles quoting individual messages, were not checked. The finding is "not found in the 2023 collections", not "first disclosed in 2026". No item was classified as newly unredacted, because the two sets barely overlap.

## Citation-ready correction

> Slack messages between the Proximal Origin authors from February to April 2020 were publicly available by July 2023, through a congressional report on 11 July and Public's cache on 20 July. The Senate HSGAC majority's July 2026 release covers 30 April 2020 to June 2023; in a comparison of the two 2023 collections, almost none of its 11,305 messages appeared in them.

## Comparison method (as planned)

1. Retrieve the collections from their publishing sources.
2. Record URLs, byte sizes, download dates and SHA-256 hashes.
3. Separate message date from document release date.
4. Extract text while retaining page images for visual verification.
5. Match author, timestamp, channel and surrounding messages.
6. Classify each item as previously public, newly disclosed, newly unredacted, reformatted or unmatched.
7. Publish a page-level comparison with uncertainty flags.

Do not infer newness from a press-release headline or completeness from a publisher's description.

## Interpretation

Release dates are better established than claims about intent. A full-message review should include authors' responses, changes in evidence and the difference between preliminary debate and a final public claim.

[S19]: https://oversight.house.gov/release/wenstrup-releases-alarming-new-report-on-proximal-origin-authors-nih-suppression-of-the-covid-19-lab-leak-hypothesis/
[S20]: https://oversight.house.gov/wp-content/uploads/2023/07/Final-Report-7.pdf
[S21]: https://www.public.news/p/covid-origins-scientist-denounces
[S93]: https://www.hsgac.senate.gov/wp-content/uploads/slack-drop-AM.pdf
[S94]: https://www.hsgac.senate.gov/wp-content/uploads/slack-drop-pm.pdf
[S95]: https://public.substack.com/api/v1/file/05ecf4cf-3ef2-47d1-9505-661a13df0756.pdf
[S22]: https://www.hsgac.senate.gov/media/reps/new-doc-drop-slack-messages-reveal-proximal-origin-authors-privately-doubted-the-science-behind-their-own-paper-coordinated-with-intelligence-community-and-nih/

# Disclosure controls

Status: draft framework, 17 November 2026. Machine-readable copy: [controls.csv](controls.csv). Applicability by actor type: [applicability.csv](applicability.csv). Grading and follow-up: [grading.md](grading.md).

## Purpose

This catalogue describes how evidence about events that threaten humanity's security should reach the public. Its subject is the disclosure process: records, data sharing, timeliness, interests, communication of uncertainty, handling of dissent, correction, response to audit and the provenance of released material. It does not assess the underlying science or which explanation of an event is correct.

The controls are written to be domain-neutral. "The actor" may be a public-health agency, a government, a research funder, a laboratory, a grant recipient, a journal, an author, a reference work, a legislative committee or an AI developer. Not every control applies to every actor; the [statement of applicability](applicability.csv) records which do, partly or not at all. "The event" means any event or risk of collective harm whose evidence the public needs: a pandemic, a dangerous research incident, a serious AI capability or failure, or another global risk.

## The ISO/IEC 27001 analogy

The structure borrows from information-security management audits. ISO/IEC 27001 pairs a catalogue of controls (its Annex A) with a statement of applicability. Certification audits against it look for evidence that controls operate, grade findings as major or minor nonconformities (with observations and opportunities for improvement in common audit practice), issue corrective-action requests and return for periodic surveillance audits. Those parts carry over usefully: a fixed catalogue makes findings comparable across actors and events, applicability stops controls being applied to actors who never held the duty, and graded findings with follow-up dates keep accountability from ending at the first publication.

The analogy breaks in three places, and the framework is adjusted accordingly.

- **No consenting auditee.** A certification audit is commissioned by the organisation audited, which opens its records to the auditor. This observatory audits from outside, using public sources. It often cannot see whether a control operated. It therefore distinguishes **not evidenced** (we could not see the control operating) from a **nonconformity** (evidence shows it failed). Absence of a published record is not itself proof of failure.
- **No management authority.** In ISO practice, top management accepts responsibility for corrective action. Here, corrective-action requests are published requests. An actor may ignore, rebut or reject them; each outcome is recorded, and a reasoned rebuttal can close a finding.
- **No certification body.** Nothing is certified, suspended or withdrawn. Grades describe the evidence available at a stated date and are revised when the evidence changes. They are this project's assessments, not determinations by an accredited body, and should be cited as such.

Two further differences matter in practice. Many relevant actors are individuals or volunteer communities, not organisations with a management system. And some actors audited here, such as legislative committees, are also sources of evidence for other findings; their releases are graded under the same controls as everyone else's.

## Using the controls

Each control has an identifier, a statement of what the actor does, a rationale, the evidence that would show it operating and the kinds of failure it covers. Findings cite a control identifier and source identifiers from the project's [source register](../sources/register.json). A finding about a control does not establish anything about the event's cause; a records failure, for example, does not show what the records would contain (see the [method](../docs/methodology.md)).

## D.1 Records and preservation

### D.1.1 Contemporaneous records

**Control.** The actor creates and retains dated records of the decisions, data, analyses and communications that bear materially on an event threatening public security, for a defined period that outlasts foreseeable inquiry.

**Rationale.** Later accountability depends on records made at the time. Without them, disputes about who knew what, and when, cannot be settled by evidence.

**Evidence of operation.** A retention policy covering the relevant record types; records produced on inquiry that carry contemporaneous dates; version histories for public documents.

**Failures covered.** Unrecorded decisions; destruction or loss of records; reliance on ephemeral or private channels for official business; undated revisions.

### D.1.2 Production of original records

**Control.** The actor produces original records, not summaries, to bodies with a legitimate oversight or investigative remit within a stated period, or gives itemised reasons for any withholding.

**Rationale.** Oversight that rests on the auditee's own summaries cannot verify them. Itemised reasons make the withholding itself reviewable.

**Evidence of operation.** Records supplied in response to dated requests; a log of requests received and answered; itemised reasons for withholding (privacy, security, legal privilege) rather than blanket refusal.

**Failures covered.** Refusal or non-response; summaries supplied in place of originals; unexplained delay; blanket withholding.

### D.1.3 Register of evidence requests

**Control.** The actor maintains a dated register of material evidence requests it has made or received, recording the recipient, the response and what remains outstanding, and publishes it where confidentiality permits.

**Rationale.** Missing evidence is easily mentioned once as a caveat and then forgotten. A register keeps outstanding requests visible and separates 'not provided' from 'does not exist'.

**Evidence of operation.** A published or producible register; entries that match requests cited in reports; dated updates.

**Failures covered.** Outstanding requests visible only as scattered caveats; inability to say what was asked, of whom and when; implied enforcement powers the actor does not have.

## D.2 Data sharing, access and reporting

### D.2.1 Timely release of primary data

**Control.** The actor releases primary data material to understanding the event promptly, with metadata sufficient for independent analysis, and publicly explains any delay.

**Rationale.** Absent data shape early public understanding by their absence. Late release cannot undo conclusions drawn in the meantime.

**Evidence of operation.** Release dates close to collection dates; metadata and documentation adequate for re-analysis; dated explanations of any delay.

**Failures covered.** Delayed or partial release; release without usable metadata; unexplained or selective withholding.

### D.2.2 Access for independent verification

**Control.** The actor permits independent parties with a legitimate remit to verify material claims about its activities, through access to sites, systems, people or records, and states the legitimate limits on that access.

**Rationale.** Claims that cannot be checked cannot carry much weight, however sincere. Stated limits let observers distinguish legitimate restriction from refusal.

**Evidence of operation.** Completed verification visits, audits or evaluations by independent parties; published terms of access; stated reasons where access was limited.

**Failures covered.** Refused or obstructed access; access on terms that prevent independent conclusions; verification by parties lacking independence.

### D.2.3 Access rights through the chain

**Control.** Where the actor funds, contracts or delegates work, it secures enforceable rights to the records of those it engages, monitors their use, and acts when access fails.

**Rationale.** Disclosure duties that stop at the first contract boundary leave the most relevant records out of reach. Funders and principals can secure access before work begins.

**Evidence of operation.** Agreements containing record-access terms; monitoring records; documented escalation and sanctions when access was refused.

**Failures covered.** No access terms in agreements; terms not exercised; no escalation when a subrecipient or contractor withholds records.

### D.2.4 Mandatory reporting and follow-up

**Control.** The actor submits reports owed to funders, regulators or oversight bodies on time and escalates reportable events promptly; where the actor receives such reports, it follows up late, missing or anomalous reports without undue delay.

**Rationale.** Reporting duties are the routine channel through which unexpected developments reach those responsible for oversight. A duty that is not followed up when breached operates in name only.

**Evidence of operation.** Reports submitted by their due dates; documented escalation criteria; records of follow-up when reports were late or raised issues.

**Failures covered.** Late or missing reports; reportable events not escalated; recipients not pursuing late reports; unclear escalation rules.

## D.3 Interests and independence

### D.3.1 Disclosure of relevant interests

**Control.** The actor discloses financial, institutional, research and personal relationships relevant to the subject when it contributes to an assessment, publication or public statement, not only when challenged later.

**Rationale.** Readers weigh a contribution partly by who makes it and what they stand to gain or lose. A disclosure made after publication arrives when the contribution has already been read.

**Evidence of operation.** Disclosure statements published with the contribution; disclosures consistent with independently known relationships; no later material additions.

**Failures covered.** Omitted or incomplete disclosures; disclosure only after challenge; a narrow reading of what counts as relevant.

### D.3.2 Review and management of declared interests

**Control.** The actor that convenes, publishes or relies on contributions reviews declared interests against information available to it, records how material conflicts were managed, and publishes contributors' roles.

**Rationale.** Self-declaration alone places the whole burden on the person with the interest. Convening and publishing bodies can check and manage conflicts, and a recorded decision makes the management reviewable.

**Evidence of operation.** A published conflict policy; records of review and management decisions (recusal, disclosure, exclusion); published roles of assessment-body members.

**Failures covered.** Reliance on unchecked self-declaration; conflicted members in decisive roles without recorded management; undisclosed roles.

## D.4 Communication of uncertainty and dissent

### D.4.1 Confidence proportionate to evidence

**Control.** The actor expresses confidence in public conclusions no more strongly than the evidence and access available support, and states material limitations with the same prominence as the conclusions.

**Rationale.** Headlines, summaries and briefings travel further than caveats. Confidence that outruns the evidence is hard to withdraw once it has shaped public understanding.

**Evidence of operation.** Summaries and press materials that carry the limitations stated in the full text; calibrated confidence language; conclusions attributed to those who reached them.

**Failures covered.** Overstated confidence; limitations confined to body text or annexes; conclusions stated in an unattributed, categorical voice.

### D.4.2 Missing evidence distinguished from contrary evidence

**Control.** The actor distinguishes evidence that is unavailable from evidence that weighs against a possibility, and explains how unavailable evidence affected its conclusions.

**Rationale.** Lack of access is easily read as lack of support. Treating the two alike quietly turns an incomplete inquiry into a negative finding.

**Evidence of operation.** Explicit statements of what could not be assessed and why; conclusions qualified accordingly.

**Failures covered.** Unavailable evidence mentioned only as a caveat; an incomplete inquiry presented as an exclusion.

### D.4.3 Dissent recorded and disclosed

**Control.** The actor records material disagreement within its assessment bodies and leadership and discloses its substance and how it was resolved.

**Rationale.** Disclosed dissent tells the public that a conclusion was contested and by whom. Undisclosed dissent tends to surface later as a problem of credibility.

**Evidence of operation.** Minority statements or recorded dissents in reports; leadership statements noting disagreement; an account of how disagreement was resolved.

**Failures covered.** Unrecorded dissent; a contested conclusion presented as unanimous; dissent disclosed without an account of its handling.

### D.4.4 Documented basis for headline judgments

**Control.** The actor documents how headline judgments (rankings, probability terms, risk levels) were selected and approved, including the evidence standard applied, and makes that account available.

**Rationale.** Headline judgments are what most people remember. Without a documented basis, neither critics nor the actor can show whether the judgment followed the evidence.

**Evidence of operation.** A published method for confidence language; approval records; an account linking the evidence base to the terms chosen.

**Failures covered.** Undocumented choice of headline terms; no identifiable approval step; no stated evidence standard.

## D.5 Correction and learning

### D.5.1 Correction at the point of original publication

**Control.** When an earlier public statement of the actor is superseded, qualified or shown to be incomplete, the actor publishes a dated correction or contextual note linked from the original, without altering the historical record.

**Rationale.** Readers usually meet the original, not the later qualification. A note at the original keeps the record intact while preventing it from being mistaken for the current position.

**Evidence of operation.** Dated corrections, addenda or notes attached to or linked from the original; original text preserved.

**Failures covered.** Later positions published separately with no link from the original; silent alteration; corrections that do not state what changed.

### D.5.2 Reasoned response to substantive criticism

**Control.** The actor publishes a reasoned response to specific, substantive criticism of its statements or processes within a stated period, whether it accepts, partly accepts or rebuts the criticism.

**Rationale.** A response, including a rebuttal, lets the public weigh both sides. Silence leaves criticism standing or invites over-reading of it.

**Evidence of operation.** Published responses that address the specific points raised; a stated process for handling formal criticism.

**Failures covered.** No response; responses that do not address the points made; a process opaque to the critic.

### D.5.3 Independent audit and corrective action

**Control.** The actor submits its handling of material events to independent audit or review, states whether it accepts each finding and why, and reports implementation of corrective actions with dated evidence.

**Rationale.** Concurrence with recommendations is a commitment, not a result. Reported implementation is what lets others check that a failure will not recur.

**Evidence of operation.** A published audit with the actor's responses; recommendation-by-recommendation implementation reports; follow-up audits.

**Failures covered.** No independent review; findings rejected without reasons; concurrence without reported implementation.

### D.5.4 Currency of standing summaries

**Control.** The actor that maintains standing summaries (reference articles, guidance pages, fact sheets, risk assessments) updates them within a reasonable period when a later authoritative assessment supersedes their content, and dates historical positions.

**Rationale.** Standing summaries are consulted long after events. A summary that stops at an earlier assessment presents a historical position as current.

**Evidence of operation.** Revisions reflecting later assessments; dated statements of historical positions; a review cycle.

**Failures covered.** Summaries frozen at superseded assessments; prominent sections lagging less prominent ones; undated historical positions.

## D.6 Release provenance

### D.6.1 Provenance and integrity of released material

**Control.** The actor that releases documents identifies their source and custodian, how they were obtained, the release date and any redactions, and keeps a stable, versioned copy with integrity data such as hashes.

**Rationale.** Released material is cited for years. Without provenance and a fixed version, later readers cannot establish what was public, when, and in what form.

**Evidence of operation.** Release notes stating source and custodian; stable URLs; version identifiers or hashes; redaction logs.

**Failures covered.** Unversioned or silently replaced files; near-identical versions without explanation; unstated source or redactions.

### D.6.2 Accurate novelty and completeness claims

**Control.** The actor claims that released material is new, previously undisclosed or complete only where the claim is accurate, and specifies it item by item when a release mixes new and previously public material.

**Rationale.** Novelty claims shape whether a release is reported as a revelation. Completeness claims shape whether readers look for what is missing.

**Evidence of operation.** Item-level statements of what is newly disclosed, newly unredacted or previously public; scope statements for collections.

**Failures covered.** Blanket 'new' or 'full' claims for mixed or partial collections; omission of earlier publication.

### D.6.3 Exhibits separated from interpretation

**Control.** The actor that publishes primary material alongside its own interpretation presents the material distinctly, with enough dating and surrounding context for readers to form their own view.

**Rationale.** Excerpts embedded in advocacy are hard to evaluate independently. Separation lets readers check the interpretation against the exhibit.

**Evidence of operation.** Exhibits reproduced in full or with marked excisions; dates and surrounding messages included; interpretation clearly labelled.

**Failures covered.** Excerpts without context; interpretation presented as the content of the record; selective quotation.

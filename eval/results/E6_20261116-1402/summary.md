# E6 · 2026-11-16T13:02:45+00:00

commit `7af0da6` · database `localhost/compliance_eval` · 20 cases

models: `worker_full` = openai/gpt-6-luna · `worker_quick` = openai/gpt-6-luna · `cheap` = google/gemini-3.1-flash-lite · `judge` = anthropic/claude-haiku-5.5 · `embeddings` = openai/text-embedding-3-small · `reranker` = cohere/rerank-4-fast · `router` = typesafe/jev-router · `grader` = openai/gpt-6-luna

## E6 full assessments

| metric | result | target |
|---|---|---|
| cases that produced an assessment | 20 of 20 (1.00) | all |
| verdict accuracy · of which dangerous (expected Do not build, got Proceed) | 16 of 20 (0.80) · 0 | ≥ 0.80 · 0 |
| risk level accuracy | 13 of 20 (0.65) | reported |
| high-risk AI flag: missed of positives · false of negatives | 0 of 7 · 0 of 13 | ≤ 1 · ≤ 1 |
| DPIA flag: missed of positives · false of negatives | 1 of 14 · 0 of 6 | ≤ 1 · ≤ 1 |
| must-cite recall (verified citations, article level) | 39 of 39 (1.00) | ≥ 0.80 |
| key findings matched (judge + rubric, no severity tolerance) | 58 of 81 (0.72) · partial 8 | matched ≥ 0.75 |
| of the missed: right point and provision, wrong severity | 6 | reported |
| wrong extras (fabrication, contextual blindness, false escalation) | 5 | reported |
| must_not violations | 0 | 0 |
| faithfulness of findings (RAGAs definition, own implementation), mean | 0.845 over 20 | ≥ 0.85 |
| confusable pairs both right (verdict and flags) | 6 of 8 | reported |
| the run: cost (assessments · judge) · seconds per case (mean) · rewrites · regenerations | $0.3173 · $0.191 · 77.9 s · 33 · 0 | reported |

Wrong verdicts: A-001 (Proceed → Proceed with conditions); A-008 (Proceed → Proceed with conditions); A-017 (Proceed with conditions → Do not build as described); A-019 (Proceed → Proceed with conditions)
Wrong extras: A-001: Finding 1 [Required]: demands a lawful basis under GDPR Art. 6(1) as a pre-launch obligation; the reviewer lists a Covered lawful-basis point as merely extra, so this is not wrong per se, but it treats the lawful basis as an unmet Required obligation without acknowledging the existing notice, which is contextual blindness to the organisation facts.; A-003: Finding 8: DPO review is stated as a Required step before build and tied to GDPR Art. 22, which does not require DPO review; this is a statutory fabrication.; A-006: Finding 7: GDPR Art. 22 is cited as the basis for submitting the assessment to the DPO before build, but Art. 22 imposes no such duty; the requirement is an internal review process, so this is a statutory misattribution.; A-010: Finding 1: Blocker under GDPR Art. 22 for an automatic hold ignores the stated analyst review within two hours of every hold, so it is a false escalation and contextual blindness.; A-015: Finding 9: states that DPO review before build is required and cites AI Act Annex III point 4 for it, an obligation the cited provision does not contain (statutory fabrication).
Failed pairs: A-007+A-019, A-008+A-009

### Key findings, per case

**A-001** (Proceed with conditions):
- KF1 partial: Finding 3 (Covered) states the 20-item limit, 30-day deletion, customer-only visibility and no other use, and cites GDPR Art. 5 at the umbrella level; the expected paragraph-level provisions Art. 5(1)(c) and 5(1)(e) are not named, so it is partial.
- KF2 missed (severity miscalibrated): Finding 2 treats the notice as possibly insufficient and requires an update citing Art. 13(1)/(2), with Required severity; it does not state that the existing notice already covers browsing activity inside the account as Covered under Art. 13, so the point and severity are wrong.
- wrong extras: Finding 1 [Required]: demands a lawful basis under GDPR Art. 6(1) as a pre-launch obligation; the reviewer lists a Covered lawful-basis point as merely extra, so this is not wrong per se, but it treats the lawful basis as an unmet Required obligation without acknowledging the existing notice, which is contextual blindness to the organisation facts.

**A-002** (Proceed with conditions):
- KF1 missed: Not violated: the assessment says "No matching register entry was found" and recommends that the India transfer be recorded as an action, so it does not state the activity is already recorded.
- KF2 matched: Finding 4 requires a "binding processor agreement before processing" covering documented instructions, security, confidentiality, subprocessors, assistance, deletion or return, and audits, citing GDPR Art. 28(3), at Required severity.
- KF3 matched: Finding 6 says to "update customer information to identify the helpdesk recipient, India transfer and applicable transfer basis/safeguards", citing GDPR Art. 13(1), at Required severity; Art. 13(1) covers the expected 13(1)(f) alternative.

**A-003** (Do not build as described):
- KF1 matched: Finding 1 gives Blocker on GDPR Art. 22 and Rec. 71, requiring human intervention and contest rights, which covers the Art. 22(2) exception and 22(3) safeguards.
- KF2 matched: Finding 6 requires a DPIA before processing at Required severity and cites GDPR Art. 35(3), which is the expected provision.
- KF3 matched: Finding 7 states the creditworthiness model is high-risk under AI Act Annex III point 5 with Required deployer obligations, including use per instructions, monitoring and logs. It does not explicitly name human oversight or information to the persons concerned, but the point is the same.
- KF4 matched: Finding 7 requires the fundamental-rights impact assessment before deployment at Required severity and cites AI Act Art. 27(1).
- KF5 partial: Finding 4 gives Required for browsing behaviour, with necessity and minimisation, but cites only bare GDPR Art. 5 rather than Art. 5(1)(c) at the paragraph level. Finding 5 cites Art. 6(1) but covers the scoring and vendor legal basis, not browsing data.
- KF6 matched: Finding 9 marks the US vendor transfer as Covered by the organisation's DPF certification and cites GDPR Art. 45(1).
- wrong extras: Finding 8: DPO review is stated as a Required step before build and tied to GDPR Art. 22, which does not require DPO review; this is a statutory fabrication.

**A-004** (Proceed with conditions):
- KF1 matched: Finding 7 (Covered) states the analyst review and appeal route address solely automated decision risk, citing GDPR Art. 22 and Rec. 71, and requires the analyst to independently consider and be able to change the outcome, matching the meaningful-review gist with the right provision and severity.
- KF2 matched: Finding 3 (Required) requires a DPIA before processing for systematic profiling, citing GDPR Art. 35(3), which matches the expected provision and severity.
- KF3 partial: No finding states that creditworthiness scoring remains a high-risk AI system despite human oversight; the summary mentions Annex III point 5 but findings 5 and 4 only impose duties, and Art. 6(2) is never linked to the classification point.
- KF4 matched: Finding 4 (Required) requires a fundamental-rights impact assessment before deployment for high-risk creditworthiness AI, citing AI Act Art. 27(1), which matches the expected provision and severity.
- KF5 matched: Finding 4 (Required) says to inform affected customers that the AI system is being used, citing AI Act Art. 26(11), matching the expected point and severity.

**A-005** (Proceed with conditions):
- KF1 matched: Finding 4 (Required) says to identify the chatbot as AI at or before first interaction, citing AI Act Art. 50(1), which is the expected point, provision and severity. The conditional wording ("If the chatbot is an AI system") does not change the match.
- KF2 matched: Finding 6 (Covered) says the order-support function "does not match the listed high-risk use cases", citing AI Act Annex III. Art. 6(2) is cited alongside, and the expected acceptable alternative "AI Act Art. 6" covers it at article level.
- KF3 matched: Finding 2 (Required) requires limiting data and setting retention periods for transcripts and order numbers, citing GDPR Art. 5, which is the acceptable alternative. Finding 3 (Required) requires privacy information including the retention period, citing GDPR Art. 13(1) and 13(2), which covers the Art. 13 provision.

**A-006** (Do not build as described):
- KF1 matched: Finding 1 is a Blocker on refusals with no human review or contest route, citing GDPR Art. 22 and Rec. 71, and notes the 22(3) safeguards ("human intervention, the chance to state their view, and contest the decision") still apply under a contract exception.
- KF2 matched: Finding 5 is Required, cites GDPR Art. 35(3) with Art. 35(1), and ties the DPIA to "the automated evaluation and consequential refund decisions"; finding 3 adds profiling of return history. The systematic evaluation point is present at the right level.
- KF3 matched: Finding 6 is Required and cites AI Act Art. 50(1) for telling customers at or before the chatbot interaction that they are dealing with AI.
- KF4 missed: The not-high-risk point appears only in the header field "high-risk AI False" and in a next-step sentence ("this assessment does not identify a high-risk category"). It is not a labelled Covered finding, cites no Annex III or Art. 6(3), and is hedged as something to confirm.
- wrong extras: Finding 7: GDPR Art. 22 is cited as the basis for submitting the assessment to the DPO before build, but Art. 22 imposes no such duty; the requirement is an internal review process, so this is a statutory misattribution.

**A-007** (Proceed with conditions):
- KF1 matched: Assistant finding 5 (Covered) says the offer selection 'is not a solely automated decision with legal or similarly significant effects under Article 22', citing GDPR Art. 22, which is an acceptable alternative provision and the same point at the same severity.
- KF2 matched: Assistant finding 1 (Required) requires an Article 6 legal basis and a legitimate-interests balancing for direct marketing, citing GDPR Art. 6(1) and Rec. 47; Art. 6(1) is the paragraph containing point (f) and Rec. 47 is an acceptable alternative, so the provision level is met.
- KF3 matched: Assistant finding 4 (Covered) says the opt-out must 'stop both profiling for direct marketing' and 'honour objections at any time', citing GDPR Art. 21, an acceptable alternative; the free-of-charge and attention points are not stated but the core objection-mechanism point is present at the right severity.
- KF4 missed: No assistant finding identifies a DPIA as required before processing; the verdict states 'DPIA required False' and the next steps only say to 'reassess Article 22 and DPIA if the scope expands', so the EDPB-criteria point under Art. 35(1) is absent.

**A-008** (Proceed with conditions):
- KF1 partial: Finding 8 is Covered and cites GDPR Art. 28(3) for the signed DPA, written-instruction restriction and deletion at contract end, which matches the provision and severity. However, it also says the agreement must still be verified for the remaining required terms, and finding 7 (Required) says the DPA does not yet cover security, subprocessors and audit, so the 'required content is in place' conclusion is undercut.
- KF2 matched: Finding 9 is Covered and states that 'the notice already names analytics providers as a recipient category', citing GDPR Art. 13(1), which is within the acceptable Art. 13 alternatives at article level.

**A-009** (Do not build as described):
- KF1 matched: Finding 1 (Blocker) says the separate commercial reuse is 'not shown compatible with the original purpose or supported by a lawful basis' and cites GDPR Art. 6(4), matching the expected Blocker on incompatible purpose.
- KF2 matched: Finding 3 (Required) says that because Northline 'determines its own purpose and sells models to other banks' the role must be clarified and that 'the standard processor contract cannot authorise this own-purpose processing', citing GDPR Art. 28(10).
- KF3 matched: Finding 5 (Required) says that if a distinct reuse is approved, customer information must be updated 'before it begins to describe the new purpose', citing GDPR Art. 13(3); this covers the new-information point at the expected provision and severity.
- KF4 matched: Finding 4 (Required) says to 'complete a DPIA before any permitted training use' because the analysis 'presents likely high risk', citing GDPR Art. 35(1), which matches the expected Required DPIA on large-scale data.

**A-010** (Proceed with conditions):
- KF1 matched: Finding 9 (Covered) states that Annex III's creditworthiness category expressly excludes systems used to detect financial fraud, citing AI Act Annex III point 5, which matches the expected carve-out at the paragraph level.
- KF2 missed: Finding 1 says the hold 'occurs before analyst intervention' and is a Blocker under GDPR Art. 22, which contradicts the expected conclusion that a two-hour analyst review makes the decision not solely automated; the point and severity are both reversed, so this is missed.
- KF3 matched: Finding 2 is Required and cites GDPR Art. 35(3) for a DPIA before processing because of systematic automated scoring, matching the expected point at the article level with the right severity.
- KF4 matched: Finding 8 is Covered and says the US vendor's EU–US Data Privacy Framework certification means the transfer is covered by the adequacy decision, citing GDPR Art. 45(1).
- KF5 matched: Finding 6 is Required and requires a processor agreement covering instructions, security, subprocessors, assistance and deletion or return of data, citing GDPR Art. 28(3).
- wrong extras: Finding 1: Blocker under GDPR Art. 22 for an automatic hold ignores the stated analyst review within two hours of every hold, so it is a false escalation and contextual blindness.

**A-011** (Proceed with conditions):
- KF1 matched: Finding 3 (Required) says the model "evaluates creditworthiness, so it is high-risk AI" under Annex III point 5, which matches the gist and the paragraph-level provision. It does not address the fraud carve-out, which is part of the expected gist.
- KF2 matched: Finding 3 (Required) says fine-tuning and branding "may make the company a provider", names AI Act Art. 25(1), and asks whether the modification is substantial. The point is hedged and does not spell out the provider obligations, but the provision and severity are right.
- KF3 matched: Finding 1 (Required) requires assessing "whether model training is compatible with the original repayment-data purposes" and cites GDPR Art. 6(4) and Art. 5, with minimisation of the two years of history. This matches the compatibility test and minimisation points.
- KF4 matched: Finding 2 (Required) requires a fundamental-rights impact assessment "before deployment" as deployer of an Annex III point 5(b) system, citing AI Act Art. 27(1). This matches exactly.
- KF5 matched: Finding 2 (Required) requires a DPIA before processing for "systematic, extensive profiling informing decisions with significant effects", citing GDPR Art. 35(3). This matches exactly.
- KF6 matched: Finding 5 (Required) says "Tell customers that the high-risk AI system is used in decisions about them; telling them only the outcome is not enough", citing AI Act Art. 26(11). This matches the expected gist and provision.
- KF7 matched: Finding 6 (Covered) says a credit officer "approves or changes each proposed limit before application" so the decision is not solely automated, provided the officer can "independently reject or override it", citing GDPR Art. 22. This matches the expected Covered finding.

**A-012** (Proceed with conditions):
- KF1 matched: Finding 9 states the one-to-one identity confirmation is excluded from the high-risk biometric category, citing AI Act Annex III point 1, which is the expected provision at paragraph level, with Covered severity.
- KF2 missed (severity miscalibrated): Finding 1 makes the Art. 9 point with GDPR Art. 9(1) and 9(2) and raises explicit consent via a genuine video-call alternative, but labels it Blocker where Required is expected, so the point is right and the severity is wrong.
- KF3 matched: Finding 4 requires a DPIA before processing for special-category biometric data, citing GDPR Art. 35(1), which is an acceptable alternative, with Required severity.
- KF4 partial: Finding 8 says deleting face templates immediately after matching limits retention, as Covered, but cites only the umbrella GDPR Art. 5 without the 5(1)(c) or 5(1)(e) paragraph and does not cite Art. 25 by design.

**A-013** (Do not build as described):
- KF1 matched: Finding 1 states the Blocker rejection flow lacks human decision, and says safeguards include human intervention and the chance to contest, citing GDPR Art. 22 and Rec. 71; Art. 22(1) and 22(3) are covered at article level, and Blocker severity matches.
- KF2 matched: Finding 4 labels the system high-risk for recruitment/selection and cites AI Act Annex III point 4 with deployer human oversight by competent staff, matching the gist; it cites Annex III point 4 (required paragraph level) and Required severity, though Art. 6(2) is not cited and Art. 26 is cited as acceptable alternative.
- KF3 matched: Finding 3 is Required, cites GDPR Art. 35(3) and names systematic automated evaluation with significantly affecting decisions, matching the DPIA point and severity.
- KF4 matched: Finding 2 is Required and cites GDPR Art. 13(1) and says applicants must be told about scoring, profiling and consequences; Art. 13(1) is not the expected Art. 13(2)(f) nor AI Act Art. 26(11), and Art. 13 is an acceptable alternative at article level, so the right provision and severity are present, matching the Art. 13 alternative.

**A-014** (Proceed with conditions):
- KF1 matched: Finding 2 treats the tool as high-risk under Annex III point 4 and Art. 6(2), with Required severity and the deployer duties of competent oversight, instructions and monitoring. This matches the expected paragraph-level Annex III point 4 citation.
- KF2 matched: Finding 5 is Covered and says recruiters review every application and make the invitation decision, citing GDPR Art. 22(1) and Rec. 71 with meaningful, independent human judgment. This matches the expected Art. 22 point at Covered severity.
- KF3 matched: Finding 1 is Required, requires a DPIA before processing, and cites GDPR Art. 35(3) for systematic evaluation of applicants. Art. 35 is an acceptable alternative, so the article-level citation is satisfied.
- KF4 missed (severity miscalibrated): Finding 3 covers the job-ad notice and the GDPR Art. 13 processing information, but labels it Required rather than Covered. The point and provision are right, so only the severity is wrong.

**A-015** (Proceed with conditions):
- KF1 matched: Finding 6 classifies the system as high-risk for employment performance evaluation and cites Annex III point 4 and Art. 6(2), at the paragraph level the reviewer asks for. It does not name human oversight, instructions for use or logs, but the classification and the deployer-controls point are present at Required.
- KF2 matched: Finding 7 says a handbook mention alone is not enough and that affected workers and workers' representatives must be informed before workplace deployment, citing AI Act Art. 26(7), at Required.
- KF3 matched: Finding 5 requires a DPIA before processing for the profiling and performance evaluation of employees, citing GDPR Art. 35(1), which is an acceptable alternative, at Required. The same finding also carries an Art. 22 point labelled Required, which does not fit the expected Covered label for that point.
- KF4 partial: Finding 4 requires a documented lawful basis and a legitimate-interest balancing assessment, citing GDPR Art. 6(1), at Required. It does not say employees cannot freely consent to their employer, and it omits GDPR Art. 88 and the national employment rules; the lawful-basis point is present but the provision is only at paragraph level and the consent and employment-rules points are absent.
- KF5 missed (severity miscalibrated): Finding 5 engages GDPR Art. 22 as possibly applicable and says the team lead must decide independently, but labels it Required and leaves the scope open rather than concluding Art. 22(1) does not apply. The expected severity is Covered, so the point is present with the wrong severity.
- wrong extras: Finding 9: states that DPO review before build is required and cites AI Act Annex III point 4 for it, an obligation the cited provision does not contain (statutory fabrication).

**A-016** (Do not build as described):
- KF1 matched: Finding 1 states the Blocker that matching every visitor's face uses biometric data for unique identification with no applicable Article 9 exception, citing GDPR Art. 9(1) and 9(2), which covers the expected Art. 9(1) provision.
- KF2 matched: Finding 6 is Required and says remote biometric identification is high-risk AI under AI Act Annex III point 1 and Art. 6(2), with human oversight obligations; this matches the expected point, provisions and severity.
- KF3 missed (severity miscalibrated): Finding 2 cites GDPR Art. 10 but labels it Required and only as a conditional check ('If files contain data about criminal convictions or offences, verify the separate Article 10 restriction'), so it never concludes the watch-list is unlawful as described; the point is right but the severity is wrong.
- KF4 matched: Finding 4 is Required, requiring a DPIA before processing for novel systematic biometric surveillance, citing GDPR Art. 35(1) and 35(7); Art. 35 is an acceptable alternative at the article citation level.

**A-017** (Do not build as described):
- KF1 missed (severity miscalibrated): Finding 1 (Blocker) says an Art. 9(2) exception must be established for the note, but never names explicit consent or a route that avoids medical proof. Only the severity is clearly wrong, since the expected severity is Required, so this is marked miscalibrated.
- KF2 partial: Finding 5 (Required) covers the 12-month retention under 'GDPR Art. 5' and asks for shortening or deletion, which is storage limitation, but the paragraph 5(1)(e) is not cited. Finding 3 and 4 address necessity of the profile labels, a partial hit on minimisation, and the 'record that proof was provided rather than the diagnosis' point is absent.
- KF3 matched: Finding 6 (Required) requires completing a DPIA before launch for special-category health data affecting customers in financial difficulty, citing GDPR Art. 35(1) and Rec. 91, which is an acceptable alternative article.
- KF4 missed: No assistant finding mentions Art. 22 or a human case handler deciding the payment holiday, so the Covered point that Art. 22 does not apply is absent.

**A-018** (Do not build as described):
- KF1 matched: Assistant finding 1 (Blocker) says inferring and storing religion from names processes special-category data needing an Art. 9(2) condition, and finding 2 extends this to transaction timing; both cite GDPR Art. 9(1) with Blocker severity, matching the expected point and provision.
- KF2 matched: Assistant finding 5 (Required) says to make the right to object to direct marketing clear and separate and to stop marketing processing when a customer objects, citing GDPR Art. 21(2); the point, provision and severity all match.
- KF3 matched: Assistant finding 4 (Required) requires a DPIA before processing because of special-category data and significant risks, citing GDPR Art. 35(1); Art. 35 is an acceptable alternative at article level, and the severity is Required.
- KF4 partial: The verdict header says 'high-risk AI False', which states the not-high-risk conclusion, but no numbered finding, Annex III or Art. 6(3) citation, or Covered label appears; the point is present but the provision is absent.

**A-019** (Proceed with conditions):
- KF1 missed: No assistant finding addresses automated decisions or Art. 22. The summary says the feature 'does not appear to trigger GDPR rules on solely automated significant decisions', but that sentence is not a numbered finding, cites no provision and gives no Covered severity.
- KF2 missed: Finding 1 covers the same point, the legal basis for using transaction history, but cites Art. 6(1) rather than Art. 6(1)(b) or the acceptable 6(1)(f), and labels it Required where Covered is expected.
- KF3 matched: Finding 4 is Covered and says the design 'does not persist the computed categories' and 'uses the previous 12 months', which matches minimisation and storage limitation by design. It cites Art. 25, an acceptable alternative, alongside a bare Art. 5, so the provision level is met.

**A-020** (Do not build as described):
- KF1 matched: Finding 1 says the all-databases wipe would delete transaction records covered by the five-year AML retention policy and that records still under a legal retention obligation must be excluded, with Blocker severity. It cites GDPR Art. 17(3), which is a listed acceptable alternative at paragraph level, though not the required 17(3)(b).
- KF2 matched: Finding 2 says the feature cannot wipe automatically generated high-risk AI logs while the minimum retention period applies, citing AI Act Art. 26(6), with Blocker severity. Same point, same provision, same severity.
- KF3 missed: No finding proposes deleting marketing and app profile data while restricting and segregating retained records under GDPR Art. 18. Finding 2's 'preserve logs under your control' and finding 4's 'erase the rest' do not state restriction; the restriction idea appears only in the next steps, which are not findings.
- KF4 missed: No finding says the response to the customer must state which data is erased and which is retained and why. Finding 3 only warns against promising an immediate wipe, which is not a Art. 12 communication duty.


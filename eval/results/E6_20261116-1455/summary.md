# E6 · 2026-11-16T13:55:38+00:00

commit `7af0da6` · database `localhost/compliance_eval` · 20 cases

models: `worker_full` = openai/gpt-6-luna · `worker_quick` = openai/gpt-6-luna · `cheap` = google/gemini-3.1-flash-lite · `judge` = anthropic/claude-haiku-5.5 · `embeddings` = openai/text-embedding-3-small · `reranker` = cohere/rerank-4-fast · `router` = typesafe/jev-router · `grader` = openai/gpt-6-luna

## E6 full assessments

| metric | result | target |
|---|---|---|
| cases that produced an assessment | 20 of 20 (1.00) | all |
| verdict accuracy · of which dangerous (expected Do not build, got Proceed) | 15 of 20 (0.75) · 0 | ≥ 0.80 · 0 |
| risk level accuracy | 13 of 20 (0.65) | reported |
| high-risk AI flag: missed of positives · false of negatives | 0 of 7 · 1 of 13 | ≤ 1 · ≤ 1 |
| DPIA flag: missed of positives · false of negatives | 2 of 14 · 1 of 6 | ≤ 1 · ≤ 1 |
| must-cite recall (verified citations, article level) | 39 of 39 (1.00) | ≥ 0.80 |
| key findings matched (judge + rubric, no severity tolerance) | 55 of 81 (0.68) · partial 9 | matched ≥ 0.75 |
| of the missed: right point and provision, wrong severity | 10 | reported |
| wrong extras (fabrication, contextual blindness, false escalation) | 1 | reported |
| must_not violations | 0 | 0 |
| faithfulness of findings (RAGAs definition, own implementation), mean | 0.834 over 20 | ≥ 0.85 |
| confusable pairs both right (verdict and flags) | 6 of 8 | reported |
| the run: cost (assessments · judge) · seconds per case (mean) · rewrites · regenerations | $0.3175 · $0.1822 · 79.4 s · 35 · 0 | reported |

Wrong verdicts: A-001 (Proceed → Proceed with conditions); A-008 (Proceed → Proceed with conditions); A-017 (Proceed with conditions → Do not build as described); A-019 (Proceed → Proceed with conditions); A-020 (Do not build as described → Proceed with conditions)
Wrong extras: A-010: Finding 3: Required obligation to assess whether the hold is a significant solely automated decision under Art. 22, which contextual blindness to the described analyst review of every hold within two hours makes wrong.
Failed pairs: A-007+A-019, A-008+A-009

### Key findings, per case

**A-001** (Proceed with conditions):
- KF1 matched: Finding 4 states the 20-item, 30-day, customer-only and no-other-use limits are in place and should be maintained, with Covered severity, citing GDPR Art. 5 and Art. 25; Art. 25 is an acceptable alternative, so the provision is acceptable. Finding 3 treats the same limits as Required and cites only bare Art. 5, which is the wrong severity.
- KF2 missed (severity miscalibrated): Finding 2 makes the same point (the notice must cover the account-only browsing use) and cites Art. 13, but marks it Required and says the existing statement "may not cover" it, reversing the Covered conclusion.

**A-002** (Proceed with conditions):
- KF1 missed (severity miscalibrated): Finding 1 states the right point (no transfer until an Art. 46 safeguard such as SCCs is in place, with Art. 46(2) cited), but labels it Blocker where Required is expected, so the severity is wrong.
- KF2 matched: Finding 2 is Required and cites GDPR Art. 28(3), covering instructions, confidentiality, subprocessors, assistance and deletion or return before processing.
- KF3 matched: Finding 7 is Required and cites GDPR Art. 13(1), requiring the privacy information to identify the recipient category and disclose the India transfer and its safeguards.

**A-003** (Do not build as described):
- KF1 matched: Finding 1 (Blocker) says fully automatic rejections need a valid Article 22 exception and safeguards, including human intervention and the right to contest, citing GDPR Art. 22 and Rec. 71. This covers the same point, the provision level and the Blocker severity.
- KF2 matched: Finding 6 (Required) requires a DPIA before processing for 'this systematic automated evaluation' and cites GDPR Art. 35(3), which satisfies the article-level citation. Severity is Required as expected.
- KF3 matched: Finding 7 (Required) says this is high-risk AI for creditworthiness, cites AI Act Annex III point 5, and requires meeting deployer obligations. Finding 8 adds the information to affected persons under AI Act Art. 26(11). Together they cover the deployer obligations at the Annex III point 5 level with Required severity.
- KF4 matched: Finding 7 (Required) says to 'Complete the deployer fundamental-rights impact assessment before use' and cites AI Act Art. 27(1), so the FRIA point, provision and Required severity are all present.
- KF5 matched: Finding 5 (Required) says browsing behaviour needs its relevance and necessity substantiated and collection limited, citing GDPR Art. 5. Art. 5 is a listed acceptable alternative, so the provision is accepted and the severity is Required.
- KF6 matched: Finding 9 (Covered) states the US vendor transfer is covered by the organisation's EU-US Data Privacy Framework certification, citing GDPR Art. 45(1). This matches the gist, provision and Covered severity.

**A-004** (Proceed with conditions):
- KF1 matched: Assistant finding 8 is Covered and cites GDPR Art. 22(1) and Rec. 71 for the human analyst reviewing every flag, and finding 6 supplies the authority to challenge or disregard scores that the gist requires.
- KF2 matched: Finding 1 is Required, 'Complete a DPIA before processing', and cites GDPR Art. 35(3), which covers the systematic profiling trigger.
- KF3 partial: The summary asserts 'The credit-scoring AI is high-risk' but never ties it to Annex III point 5 or Art. 6(2); Annex III point 5 appears only in finding 2 as the FRIA trigger, and Art. 6(2) is absent, so the classification point is present but the citation is incomplete.
- KF4 matched: Finding 2 is Required, 'Complete a fundamental-rights impact assessment before deployment', cites AI Act Art. 27(1), and ties it to Annex III point 5(b) credit scoring.
- KF5 missed: No finding tells the persons that a high-risk AI system evaluates them; finding 5 covers GDPR transparency on scoring and profiling under Art. 13(1) and 14(2), not the AI Act Art. 26(11) duty or the Art. 13(2)(f) alternative cited for it.

**A-005** (Proceed with conditions):
- KF1 matched: Finding 4 requires a clear AI-interaction disclosure at the latest at first interaction under AI Act Art. 50(1), which is the expected Required notice; its conditional wording ('if the chatbot uses an AI system') does not change the obligation the reviewer expects.
- KF2 partial: The summary says the chatbot 'does not appear to be high-risk AI' and the verdict shows 'high-risk AI False', so the point is present, but no numbered finding carries it and no Annex III or Art. 6(3) provision is cited.
- KF3 matched: Finding 3 requires a privacy notice covering retention under GDPR Art. 13(1)/(2), which matches the paragraph-level provision and Required severity; finding 2 adds the short-retention limit for the typed number and chat records, citing GDPR Art. 5, which is an acceptable alternative.

**A-006** (Do not build as described):
- KF1 matched: Finding 1 is a Blocker that says final, solely automated refusals with no human route "are not acceptable as described" and calls for human intervention and a way to contest, citing GDPR Art. 22 and Rec. 71; this matches the point, provision level and severity.
- KF2 matched: Finding 4 is Required, "Complete a DPIA before deployment, covering the systematic automated evaluation and its effects on customers", citing GDPR Art. 35(3), which satisfies the article-level citation of Art. 35.
- KF3 matched: Finding 5 is Required, "Tell customers they are interacting with AI at the first interaction", citing AI Act Art. 50(1) and Art. 50(5); the notice at the start of the chat is covered at the right provision and severity.
- KF4 missed: No finding in the list addresses Annex III or the high-risk classification; the only mention is the header field "high-risk AI False", which cites no provision and gives no Covered label, so the point is not established as a finding.

**A-007** (Proceed with conditions):
- KF1 matched: Finding 6 (Covered) states that offer selection does not refuse or limit a service and that GDPR Art. 22's restriction is not indicated, citing Art. 22 and Rec. 71. This matches the gist and provision at article level with the correct Covered severity.
- KF2 matched: Finding 1 (Required) requires documenting a legitimate-interest basis that balances customers' expectations and rights, citing GDPR Art. 6(1) and Rec. 47. The paragraph-level provision and the balancing-test gist are present with the correct severity.
- KF3 matched: Finding 5 (Covered) says the settings toggle must turn off personalised offers and promptly stop profile-based selection, citing GDPR Art. 21. Finding 4 adds that customers must be able to object and have profiling stop. The switch as the objection mechanism, honoured promptly, and Art. 21 are covered, though free-of-charge is not stated.
- KF4 missed: No assistant finding imposes a DPIA as a Required obligation. The Next steps only ask to confirm scale and sensitivity in DPIA screening and to reassess if high risk, and the header states 'DPIA required False'. The EDPB-criteria point under Art. 35(1) is absent.

**A-008** (Proceed with conditions):
- KF1 matched: Assistant finding 6 (Covered) relies on the signed processing agreement, written-instruction limit and deletion at contract end, citing GDPR Art. 28(3); this is the same Art. 28 relationship point, with the right provision and the expected Covered severity.
- KF2 matched: Assistant finding 7 (Covered) says the notice's reference to "analytics providers" covers disclosure of the recipient category, citing GDPR Art. 13(1) and 14(1); Art. 13 satisfies the article-level citation and the severity is Covered as expected.

**A-009** (Do not build as described):
- KF1 matched: Finding 1 (Blocker) says the retention and training for sale to other banks is 'a distinct further purpose, and no compatibility or other lawful route is established', citing GDPR Art. 6(4), which is a listed provision. Severity matches.
- KF2 matched: Finding 2 (Required) cites GDPR Art. 28(10) and says 'do not treat Northline as a processor for this own-purpose activity' and to 'confirm the parties' roles', which is the controller-not-processor point at Required severity.
- KF3 matched: Finding 3 (Required) cites GDPR Art. 13(3) and says customers must be given 'the required information about the new purpose before it begins', which covers the new-disclosure notice point.
- KF4 missed: No finding requires a DPIA before processing. Finding 4 covers minimisation and retention (Art. 5, Art. 25). The DPIA appears only as a conditional in the next steps ('assess GDPR DPIA need if processing is likely to create high risk'), and the verdict states 'DPIA required False'.

**A-010** (Proceed with conditions):
- KF1 matched: Finding 8 states the fraud-detection AI is excepted from the Annex III creditworthiness category and is not high-risk under it, citing AI Act Annex III point 5, which matches the carve-out at the required paragraph level and at Covered severity.
- KF2 missed: Finding 3 says the hold may not prevent the initial measure from being solely automated and may be a significant decision needing Art. 22 safeguards. It cites Art. 22 but reaches the opposite conclusion to the expected point, which is that an analyst review within two hours makes the decision non-automated, and it is labelled Required, not Covered.
- KF3 matched: Finding 2 says the systematic scoring of every transaction requires a DPIA, citing Art. 35(3), at Required severity, which matches the expected gist, provision and severity.
- KF4 matched: Finding 7 says the US vendor's Data Privacy Framework certification covers the transfer under GDPR Art. 45(1), at Covered severity, which matches the expected point and provision.
- KF5 matched: Finding 5 requires a processor agreement with the vendor covering documented instructions, security, assistance, deletion/return and audit rights, citing Art. 28(3) at Required severity, which covers the expected Art. 28 content.
- wrong extras: Finding 3: Required obligation to assess whether the hold is a significant solely automated decision under Art. 22, which contextual blindness to the described analyst review of every hold within two hours makes wrong.

**A-011** (Proceed with conditions):
- KF1 matched: Finding 4 states the creditworthiness system 'falls under the specified Annex III category' (AI Act Annex III point 5) with Required severity, and the summary calls it high-risk, which covers the same classification point at paragraph level; Art. 6(2) is not cited but Annex III point 5 is the required provision.
- KF2 matched: Finding 5 says using the modified model under its own brand 'may make you its provider' and requires fulfilling the 'applicable provider obligations', cites AI Act Art. 25(1) with Required severity; it does not spell out conformity assessment or CE marking, but the point and provision match.
- KF3 matched: Finding 1 covers the lawful basis and the purpose-compatibility assessment for reusing repayment histories (GDPR Art. 6(4), Required), and finding 2 covers minimising training data under GDPR Art. 5(1)(c) with pseudonymisation (Required); together they cover both halves of the expected point.
- KF4 matched: Finding 4 requires 'a fundamental-rights impact assessment before deployment' citing AI Act Art. 27(1) with Required severity, which matches the expected FRIA point and provision.
- KF5 matched: Finding 3 requires a DPIA before processing because 'systematic profiling used to inform decisions affecting credit access' falls within the DPIA cases, citing GDPR Art. 35(3) with Required severity.
- KF6 partial: Finding 7 requires informing customers about profiling and its consequences, but it cites GDPR Rec. 60 and Art. 22 rather than AI Act Art. 26(11) or the acceptable GDPR Art. 13(2)(f), and never says a high-risk AI system is used on them; the summary's 'provider' notice is absent, so the provision is missing.
- KF7 missed (severity miscalibrated): The point (a real human decision takes it outside the Art. 22 prohibition) and provision (GDPR Art. 22, Rec. 71) are present in finding 7 and the summary, but finding 7 labels it Required rather than Covered, and finding 6 likewise gives the officer-authority point Required severity, so the severity is wrong.

**A-012** (Proceed with conditions):
- KF1 matched: Finding 7 says the one-to-one verification is excluded from the biometric high-risk category when its sole purpose is confirming the claimed identity, citing AI Act Annex III point 1 with Covered severity, which matches the expected point and provision.
- KF2 missed (severity miscalibrated): Finding 1 makes the explicit-consent point under GDPR Art. 9(1) and 9(2), including the video-call alternative, but gives it Blocker where Required is expected. The point and provision are right, so this is missed with severity miscalibrated.
- KF3 matched: Finding 2 is Required and says to complete a DPIA before processing, citing GDPR Art. 35(1), which is an acceptable alternative. It does not tie the DPIA to special-category data, but the DPIA-before-processing point and severity are right.
- KF4 partial: Finding 6 is Covered and says immediate deletion of face templates is consistent with storage limitation, but it cites only the bare "GDPR Art. 5" where paragraph 5(1)(e) or 5(1)(c) is required, so it is partial.

**A-013** (Do not build as described):
- KF1 matched: Finding 1 is a Blocker on solely automated rejection under 'GDPR Art. 22' with Rec. 71, and requires 'meaningful human review' or a valid exception with 'required safeguards', which covers the no-contest gap and the 22(3) safeguards at article level.
- KF2 partial: The Annex III point 4 high-risk classification appears only in the summary ('Recruitment-selection AI is high-risk... Annex III point 4'), not in a finding. Finding 8 supplies the deployer obligations and competent human oversight under AI Act Art. 26 (an acceptable alternative), but at Required, and it does not state the classification itself.
- KF3 matched: Finding 3 is Required, requires a DPIA before processing, and cites 'GDPR Art. 35(3)' for the automated profiling that drives significant recruitment decisions.
- KF4 matched: Finding 2 is Required and tells applicants that high-risk AI is used, citing 'AI Act Art. 26(11)' and 'GDPR Art. 13(2)', with the automated scoring logic, significance and consequences; it notes applicants are currently not told.

**A-014** (Proceed with conditions):
- KF1 matched: Finding 1 states "Recruitment/selection AI is high-risk" with Required severity, citing AI Act Annex III point 4 and Art. 6(2), and lists the deployer duties of competent oversight and logs. This matches the expected Annex III point 4 finding at paragraph level.
- KF2 matched: Finding 6 is Covered and cites GDPR Art. 22 and Rec. 71, stating that recruiters read every application and decide invitations and that the human-only review request supports a "meaningful ability to disregard the score". This matches the expected point that a real human decision takes the case outside the solely automated prohibition.
- KF3 matched: Finding 2 is Required, cites GDPR Art. 35(3) and Art. 35(1), and requires a DPIA before processing on the effects of scoring and ranking on applicants. This matches the expected DPIA finding with the right provision.
- KF4 missed (severity miscalibrated): Finding 4 covers the applicant privacy notice and cites GDPR Art. 13(1) and 13(2), so the point and provision are right, but it is labelled Required where the expected severity is Covered. The wrong severity makes it missed with severity_miscalibrated true.

**A-015** (Proceed with conditions):
- KF1 matched: Finding 7 is Required and cites AI Act Annex III point 4 with Art. 6(2), covering high-risk status and competent human oversight, which matches the deployer obligations; logs are not mentioned, but the core point and provision are there.
- KF2 matched: Finding 8 is Required and cites AI Act Art. 26(7), requiring that affected workers and their representatives be informed before use; it says the handbook may only support worker notice, which is consistent with the gist.
- KF3 matched: Finding 6 is Required and cites GDPR Art. 35(1), an acceptable alternative, for a DPIA before processing that evaluates workers' performance.
- KF4 partial: Finding 1 is Required and cites GDPR Art. 6(1) for a documented legal basis and necessity and fairness in the employment context, but it does not say that employees cannot freely consent, does not name a legitimate-interest balancing, and does not mention the national employment rules (Art. 88).
- KF5 matched: Finding 9 is Covered and cites GDPR Art. 22(1) and Rec. 71, stating that team leads decide the action after a flag and that no significant decision is made solely from an automated flag.

**A-016** (Do not build as described):
- KF1 matched: Finding 1 (Blocker) states that live face matching uniquely identifies every visitor, processes biometric data, and has no stated Art. 9(2) condition, citing Art. 9(1) and 9(2). Point, provision and severity all fit.
- KF2 matched: Finding 5 (Required) treats the system as high-risk remote biometric identification under 'AI Act Annex III point 1' and 'Art. 6(2)', and requires supplier and deployer compliance and human oversight before launch. The conditional 'if use is permitted by relevant Union or national law' is weaker than the expected classification, but the point, provisions and Required severity are present.
- KF3 missed (severity miscalibrated): Finding 2 cites GDPR Art. 10 and says criminal-offence data may be used only under official authority or where Union or Member State law authorises it, but it grades this Required and makes it conditional ('if they contain' such data, 'Exclude such records unless that condition is met'). The expected Blocker conclusion, that the watch-list as described is unlawful for a private bank, is not stated, so the severity is wrong.
- KF4 matched: Finding 3 (Required) requires a DPIA before processing, citing Art. 35(1), 35(3) and 35(7), and ties it to systematic monitoring and sensitive biometric data at scale. Art. 35(3) is the paragraph containing the expected (c) point, and Required severity is correct.

**A-017** (Do not build as described):
- KF1 missed (severity miscalibrated): Finding 1 says an Article 9 exception must be identified for the doctor's note, citing GDPR Art. 9(1) and 9(2), so the point and the provision family are right. It never proposes explicit consent under 9(2)(a) or a route without medical proof, and it sets Blocker where Required is expected.
- KF2 partial: Finding 4 requires minimising the uploaded evidence and justifying or shortening retention, and finding 5 requires justifying the 12-month label retention and deleting it when no longer needed. Both are Required and cite only bare GDPR Art. 5, not 5(1)(c) or 5(1)(e), so the provision is at the wrong level.
- KF3 matched: Finding 6 is Required, cites GDPR Art. 35(1), and says a DPIA is needed before processing because health evidence combined with financial difficulty is high-risk, which is the expected special-category vulnerable-customer point.
- KF4 missed: No assistant finding addresses Art. 22 or the point that a human case handler makes the payment-holiday decision, so this expected Covered finding is absent.

**A-018** (Do not build as described):
- KF1 matched: Findings 1, 2 and 3 all say that inferring religion from names or transaction timing processes Art. 9(1) data and is a Blocker without an Art. 9(2) condition; "processes data revealing religious beliefs" is the same point at the paragraph level, with Blocker severity.
- KF2 matched: Finding 6 is Required and cites GDPR Art. 21(2), stating the right to object to direct marketing must be brought to customers' attention clearly and separately and that marketing processing stops on objection.
- KF3 matched: Finding 4 says "Complete a DPIA before processing" at Required severity, citing GDPR Art. 35(1); Art. 35 is the acceptable alternative at article level, so the provision is right.
- KF4 partial: The verdict field "high-risk AI False" and the closing next-steps sentence "this assessment does not classify it as high-risk AI" make the not-high-risk point, but no numbered finding states it and no AI Act provision (Annex III or Art. 6) is cited, so the provision is missing.

**A-019** (Proceed with conditions):
- KF1 missed (severity miscalibrated): Finding 2 makes the same point that the output must not drive decisions with legal or similar effects and cites GDPR Art. 22 and Art. 4(4), but it is marked Required where Covered is expected. Finding 2 also calls the categories profiling, which the expected finding does not say. The point and provision are right, so only the severity is wrong.
- KF2 missed: No assistant finding says that showing customers their own transactions is performance of the account contract under Art. 6(1)(b). Finding 1 treats the display as a new purpose needing a lawful-basis and compatibility check (Art. 6(1), 6(4)) and marks it Required, which contradicts the expected Covered conclusion.
- KF3 matched: Finding 5 is Covered and says the 12-month window, on-demand calculation without stored categories, and customer-only visibility limit the data processed, consistent with minimisation and privacy by default. It cites GDPR Art. 25(2), which is within the acceptable alternative GDPR Art. 25, although the primary Art. 5(1)(c) is not cited.

**A-020** (Proceed with conditions):
- KF1 missed (severity miscalibrated): Finding 2 makes the same point that retention duties override erasure and cites GDPR Art. 17(3), an acceptable alternative, but grades it Required where Blocker is expected. Finding 1 also cites Art. 17(3) at Required, so the severity is wrong in both.
- KF2 missed (severity miscalibrated): Finding 3 names AI Act Art. 26(6) and the six-month minimum log retention for deployer-controlled high-risk logs, but grades it Required where Blocker is expected for wiping credit-score audit logs on request.
- KF3 partial: Finding 2 covers retaining only what is required and erasing when the period ends, at Required, which matches the severity and the storage-limitation idea behind Art. 5(1)(e). It never says to restrict or segregate the retained records, and it cites GDPR Art. 5 rather than Art. 18 or a listed alternative; the restriction element appears only in the next steps, which are not findings.
- KF4 matched: Finding 1 requires identifying retained records and explaining the outcome to users, citing GDPR Art. 17(1) and 17(3), and Art. 17 is an acceptable alternative for this finding. Its severity is Required, as expected.


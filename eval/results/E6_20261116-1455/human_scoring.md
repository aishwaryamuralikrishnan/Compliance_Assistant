# Human scoring sheet (E6)

Score each expected key finding against the assistant's findings with the rubric of eval/prompts/judge_findings.md,
WITHOUT looking at the judge's verdicts (they are in cases.jsonl). Fill the word after `verdict:` on each line with
matched, partial, missed or unsure; then run `python -m eval.run_eval agreement <this folder>`.

## A-001 · Recently viewed products strip (account-only browsing history)

Feature: We want to add a 'recently viewed products' strip on the homepage. The list lives in the customer's own account, holds the last twenty items, is deleted after thirty days, is shown only to that customer and is not used for anything else. Our privacy notice already says we keep browsing activity inside the account.

Assistant's verdict: Proceed with conditions · risk low · high-risk AI False · DPIA False

Assistant's findings:
1. [Required] Select and document a lawful basis for recording and displaying viewed products; the description alone does not establish one. (GDPR Art. 6(1))
2. [Required] Confirm the notice available when views are collected explains this specific account-only display, its legal basis and the 30-day retention period. The existing general statement about browsing activity may not cover all required details. (GDPR Art. 13(1), GDPR Art. 13(2))
3. [Required] Document why keeping up to 20 viewed products for 30 days is necessary for this feature; shorten either limit if that period or amount is not needed. (GDPR Art. 5)
4. [Covered] The design limits the history to 20 items, deletes it after 30 days, shows it only to the customer and bars other uses; maintain these limits and access controls. (GDPR Art. 5, GDPR Art. 25)

Expected key findings:
- KF1: twenty items, thirty days, one purpose: the principles are satisfied, nothing more is kept than the feature needs · provisions GDPR Art. 5(1)(c), GDPR Art. 5(1)(e) (alternatives: GDPR Art. 25) · severity Covered · citation level paragraph
- KF2: the existing privacy notice covers browsing activity inside the account · provisions GDPR Art. 13 (alternatives: none) · severity Covered · citation level article

- [A-001 KF1] verdict: 
- [A-001 KF2] verdict: 

## A-002 · Customer support tickets hosted by helpdesk vendor in India

Feature: We're moving all customer support ticket data (names, order numbers, the text of the complaints) to a new helpdesk vendor whose servers are in India. The vendor will host and process the tickets for us. The contract is still being negotiated.

Assistant's verdict: Proceed with conditions · risk high · high-risk AI False · DPIA False

Assistant's findings:
1. [Blocker] The planned India transfer has no transfer mechanism identified. Confirm whether an applicable adequacy decision covers this recipient; if not, put an appropriate safeguard in place, such as Commission standard contractual clauses, with enforceable data-subject rights and effective remedies, before any transfer. Existing DPF coverage is specific to the US vendor and does not cover this India provider. (GDPR Art. 45(1), GDPR Art. 46(1), GDPR Art. 46(2))
2. [Required] Conclude a binding processor contract before processing, covering the required instructions, confidentiality, security, subprocessors, assistance, audits, and deletion or return of ticket data. (GDPR Art. 28(3), GDPR Art. 28(9))
3. [Required] Document the Article 6 legal basis for handling and disclosing customer support data to the vendor; the description does not establish which basis applies. (GDPR Art. 6(1))
4. [Required] Complaint text can contain sensitive information. Minimise what is transferred and restrict or redact special-category content unless an applicable Article 9 exception permits its processing. (GDPR Art. 5(1)(c), GDPR Art. 9(1), GDPR Art. 9(2))
5. [Required] Set a ticket retention period tied to the support purpose and ensure deletion or return at the end of the service, subject to applicable legal retention requirements. (GDPR Art. 5(1)(e), GDPR Art. 28(3))
6. [Required] Assess the vendor’s security measures and access controls for stored and transferred tickets; include the transfer to India and safeguards in the transfer log. (GDPR Art. 32(1), GDPR Art. 30(1))
7. [Required] Update customer-facing privacy information to identify the vendor or recipient category and disclose the intended India transfer and applicable transfer safeguards. (GDPR Art. 13(1), GDPR Art. 14(1))

Expected key findings:
- KF1: standard contractual clauses or another Art. 46 instrument before any data moves; India has no adequacy decision · provisions GDPR Art. 46 (alternatives: GDPR Art. 44) · severity Required · citation level article
- KF2: instructions, confidentiality, sub-processors, assistance, deletion at the end · provisions GDPR Art. 28 (alternatives: none) · severity Required · citation level article
- KF3: the privacy notice names the recipient category and the transfer with its safeguard · provisions GDPR Art. 13 (alternatives: GDPR Art. 13(1)(f)) · severity Required · citation level article

- [A-002 KF1] verdict: 
- [A-002 KF2] verdict: 
- [A-002 KF3] verdict: 

## A-003 · Automated BNPL credit scoring and US vendor sharing

Feature: We're adding automated credit scoring to our buy-now-pay-later checkout using transaction history, device fingerprint and browsing behaviour. Rejections are fully automatic and scores are shared with our US fraud-prevention vendor.

Assistant's verdict: Do not build as described · risk high · high-risk AI True · DPIA True

Assistant's findings:
1. [Blocker] Do not deploy fully automatic rejections as described. Establish a valid Article 22 exception and safeguards, including human intervention, the person’s opportunity to state their view and contest the outcome; otherwise provide meaningful human review before rejection. (GDPR Art. 22, GDPR Rec. 71)
2. [Required] Document the lawful basis for scoring and rejections, and demonstrate necessity and fairness for each source; the description does not establish a basis. (GDPR Art. 6(1), GDPR Art. 5)
3. [Required] Transaction history: show which transaction fields are necessary for creditworthiness, restrict use to those fields, and set a justified retention period. (GDPR Art. 5)
4. [Required] Device fingerprint: justify its necessity and scope for credit scoring; exclude unnecessary fingerprint signals and define retention. (GDPR Art. 5)
5. [Required] Browsing behaviour: substantiate its relevance and necessity for this scoring purpose; limit collection and retention accordingly. (GDPR Art. 5)
6. [Required] Provide a DPIA before processing, addressing necessity, proportionality, risks and safeguards for this systematic automated evaluation. (GDPR Art. 35(3), GDPR Art. 35(7))
7. [Required] This is high-risk AI for creditworthiness, not merely fraud detection. Complete the deployer fundamental-rights impact assessment before use and meet applicable high-risk system deployer obligations. (AI Act Annex III point 5, AI Act Art. 6(3), AI Act Art. 27(1), AI Act Art. 26(1))
8. [Required] Tell affected people about the scoring and automated decisions, including meaningful information about the logic, significance and likely consequences; inform them they are subject to the high-risk AI system. (GDPR Art. 13(2), AI Act Art. 26(11))
9. [Covered] The US fraud-prevention vendor transfer is covered by the organisation’s stated EU-US Data Privacy Framework certification fact; record this transfer in the transfer log. (GDPR Art. 45(1))

Expected key findings:
- KF1: fully automatic rejections with no human intervention and no way to contest; the Art. 22(2)(a) contract exception would still need the 22(3) safeguards · provisions GDPR Art. 22(1), GDPR Art. 22(3) (alternatives: GDPR Rec. 71, GDPR Art. 22(2)) · severity Blocker · citation level article
- KF2: systematic and extensive evaluation based on profiling · provisions GDPR Art. 35(3)(a) (alternatives: GDPR Art. 35) · severity Required · citation level article
- KF3: deployer obligations apply: human oversight, information to the persons concerned · provisions AI Act Annex III point 5, AI Act Art. 6(2) (alternatives: AI Act Art. 26) · severity Required · citation level paragraph
- KF4: a deployer of an Annex III 5(b) credit-scoring system owes a FRIA alongside the DPIA · provisions AI Act Art. 27 (alternatives: none) · severity Required · citation level article
- KF5: browsing data is not necessary for a credit decision under the contract basis; drop it or justify it · provisions GDPR Art. 5(1)(c), GDPR Art. 6(1) (alternatives: GDPR Art. 6(4), GDPR Art. 5) · severity Required · citation level paragraph
- KF6: covered by the vendor's DPF certification, an organisation fact · provisions GDPR Art. 45 (alternatives: none) · severity Covered · citation level article

- [A-003 KF1] verdict: 
- [A-003 KF2] verdict: 
- [A-003 KF3] verdict: 
- [A-003 KF4] verdict: 
- [A-003 KF5] verdict: 
- [A-003 KF6] verdict: 

## A-004 · BNPL credit-scoring flag with analyst review

Feature: We're adding credit scoring to our buy-now-pay-later checkout using transaction history and device data. The score only flags an order; a credit analyst reviews every flagged order and takes the decision, and the customer is told how to appeal. Scores stay in-house.

Assistant's verdict: Proceed with conditions · risk high · high-risk AI True · DPIA True

Assistant's findings:
1. [Required] Complete a DPIA before processing: credit profiling informs decisions about individuals’ access to BNPL credit and is likely to present high risk. (GDPR Art. 35(1), GDPR Art. 35(3))
2. [Required] Complete a fundamental-rights impact assessment before deployment; this applies to deployers of credit-scoring systems in Annex III point 5(b). (AI Act Art. 27(1), AI Act Annex III point 5)
3. [Required] Document an Art. 6 lawful basis for using transaction history for scoring, and limit those data to what is necessary, relevant and accurate for this purpose. (GDPR Art. 6(1), GDPR Art. 5)
4. [Required] Separately justify and minimise device data used in scoring; document why each device-data feature is necessary and ensure its accuracy. (GDPR Art. 6(1), GDPR Art. 5)
5. [Required] Tell customers the scoring purpose, lawful basis, data categories, and meaningful information about profiling and its significance/consequences; provide source information where data were not collected from them. (GDPR Art. 13(1), GDPR Art. 14(2))
6. [Required] Ensure analysts have competence, training, authority and sufficient information to independently challenge or disregard scores; do not let a flag automatically block or delay checkout pending a real decision. (AI Act Art. 26(2), AI Act Art. 14(4))
7. [Required] As provider/deployer of a high-risk AI system, establish the applicable provider and deployer compliance measures, including relevant documentation, conformity assessment, oversight and logging obligations. (AI Act Art. 16, AI Act Art. 26(1), AI Act Art. 26(6))
8. [Covered] A human analyst reviews every flag and makes the decision, so the described decision is not solely automated; maintain this separation in implementation and practice. (GDPR Art. 22(1), GDPR Rec. 71)

Expected key findings:
- KF1: an analyst takes every decision and the customer can appeal, so Art. 22(1) does not bite; the review must be meaningful, with the authority and competence to overturn the score (not a rubber stamp) · provisions GDPR Art. 22 (alternatives: GDPR Rec. 71, AI Act Art. 14) · severity Covered · citation level article
- KF2: systematic evaluation based on profiling · provisions GDPR Art. 35(3)(a) (alternatives: GDPR Art. 35) · severity Required · citation level article
- KF3: human oversight does not remove the classification; deployer obligations apply, including competent oversight · provisions AI Act Annex III point 5, AI Act Art. 6(2) (alternatives: AI Act Art. 26, AI Act Art. 14) · severity Required · citation level paragraph
- KF4: a deployer of an Annex III 5(b) credit-scoring system owes a FRIA alongside the DPIA · provisions AI Act Art. 27 (alternatives: none) · severity Required · citation level article
- KF5: being told the outcome and how to appeal is not being told that a high-risk AI system evaluated them; the deployer informs them before use · provisions AI Act Art. 26(11) (alternatives: AI Act Art. 26, GDPR Art. 13(2)(f)) · severity Required · citation level article

- [A-004 KF1] verdict: 
- [A-004 KF2] verdict: 
- [A-004 KF3] verdict: 
- [A-004 KF4] verdict: 
- [A-004 KF5] verdict: 

## A-005 · Help-page chatbot for order status and returns

Feature: A chatbot on our help page answers order-status and returns questions from our FAQ. It reads the order number the customer types, shows the status, and hands over to a human agent whenever the customer asks or the question is not in the FAQ. It takes no decisions about customers.

Assistant's verdict: Proceed with conditions · risk low · high-risk AI False · DPIA False

Assistant's findings:
1. [Required] Document an Article 6 legal basis for using the order number to retrieve and display order status; contract necessity may apply where this supports the customer's order relationship. (GDPR Art. 6(1))
2. [Required] Restrict the order lookup to data needed to answer the request, prevent disclosure of another customer's order, and set a short retention period for the typed number and chat records. (GDPR Art. 5, GDPR Art. 25)
3. [Required] Provide a clear privacy notice when the customer enters the order number, covering purpose, legal basis, recipients, retention and relevant rights. (GDPR Art. 13(1), GDPR Art. 13(2), GDPR Art. 12(1))
4. [Required] If the chatbot uses an AI system, clearly tell customers they are interacting with AI at the latest at first interaction; the description does not establish whether the chatbot is AI-based. (AI Act Art. 50(1), AI Act Art. 50(5))

Expected key findings:
- KF1: a clear notice at the start of the chat; the hand-over to a human is already there · provisions AI Act Art. 50(1) (alternatives: AI Act Art. 50) · severity Required · citation level article
- KF2: FAQ answers and order status are none of the Annex III uses and it takes no decisions · provisions AI Act Annex III (alternatives: AI Act Art. 6(3), AI Act Art. 6) · severity Covered · citation level article
- KF3: say how long transcripts are kept and that they are processed; keep them short · provisions GDPR Art. 5(1)(e), GDPR Art. 13 (alternatives: GDPR Art. 5) · severity Required · citation level paragraph

- [A-005 KF1] verdict: 
- [A-005 KF2] verdict: 
- [A-005 KF3] verdict: 

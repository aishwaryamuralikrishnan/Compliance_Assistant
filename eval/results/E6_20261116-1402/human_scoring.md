# Human scoring sheet (E6)

Score each expected key finding against the assistant's findings with the rubric of eval/prompts/judge_findings.md,
WITHOUT looking at the judge's verdicts (they are in cases.jsonl). Fill the word after `verdict:` on each line with
matched, partial, missed or unsure; then run `python -m eval.run_eval agreement <this folder>`.

## A-001 · Recently viewed products strip

Feature: We want to add a 'recently viewed products' strip on the homepage. The list lives in the customer's own account, holds the last twenty items, is deleted after thirty days, is shown only to that customer and is not used for anything else. Our privacy notice already says we keep browsing activity inside the account.

Assistant's verdict: Proceed with conditions · risk low · high-risk AI False · DPIA False

Assistant's findings:
1. [Required] Document an applicable legal basis for recording and displaying viewed products; the feature description does not identify one. (GDPR Art. 6(1))
2. [Required] Confirm or update the privacy notice to explain this specific display purpose, its legal basis, and the 30-day retention period. The existing general statement about browsing activity inside the account may not cover those details. (GDPR Art. 13(1), GDPR Art. 13(2))
3. [Covered] The design limits the list to the last 20 viewed items, deletes them after 30 days, shows them only to that customer, and bars other uses. These controls support data minimisation and storage limitation for the stated display purpose. (GDPR Art. 5)

Expected key findings:
- KF1: twenty items, thirty days, one purpose: the principles are satisfied, nothing more is kept than the feature needs · provisions GDPR Art. 5(1)(c), GDPR Art. 5(1)(e) (alternatives: GDPR Art. 25) · severity Covered · citation level paragraph
- KF2: the existing privacy notice covers browsing activity inside the account · provisions GDPR Art. 13 (alternatives: none) · severity Covered · citation level article

- [A-001 KF1] verdict: 
- [A-001 KF2] verdict: 

## A-002 · Customer support tickets hosted by helpdesk vendor in India

Feature: We're moving all customer support ticket data (names, order numbers, the text of the complaints) to a new helpdesk vendor whose servers are in India. The vendor will host and process the tickets for us. The contract is still being negotiated.

Assistant's verdict: Proceed with conditions · risk high · high-risk AI False · DPIA False

Assistant's findings:
1. [Required] Names are personal data. Document the lawful basis for using them to handle support requests, and keep access, use and retention limited to what that purpose requires. (GDPR Art. 6(1), GDPR Art. 5, GDPR Art. 25)
2. [Required] Order numbers linked to tickets can identify customers. Use or retain them only where necessary for ticket handling, with access limited by default. (GDPR Art. 5, GDPR Art. 25)
3. [Required] Complaint text may reveal special-category data. Minimise or redact unnecessary sensitive details; if such data are processed, identify an applicable exception before processing. (GDPR Art. 9(1), GDPR Art. 9(2), GDPR Art. 5)
4. [Required] Complete a binding processor agreement before processing, covering documented instructions, security, confidentiality, subprocessors, assistance, deletion or return, and audits. (GDPR Art. 28(3), GDPR Art. 28(2))
5. [Required] India hosting is a third-country transfer. Verify whether an applicable Commission adequacy decision covers the recipient; otherwise put an appropriate safeguard such as Commission standard contractual clauses in place, with enforceable rights and remedies. The US vendor's DPF certification does not cover this transfer. (GDPR Art. 45(1), GDPR Art. 46(1), GDPR Art. 46(2))
6. [Required] Update customer information to identify the helpdesk recipient, India transfer and applicable transfer basis/safeguards; record the transfer and destination in the processing records. (GDPR Art. 13(1), GDPR Art. 14(1), GDPR Art. 30(1))
7. [Required] Set risk-appropriate security measures with the vendor, including access controls and appropriate encryption, and validate them before launch. (GDPR Art. 32)

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
1. [Blocker] Do not make rejections solely automatically as described. Before build, either remove sole automation or establish a valid GDPR Art. 22(2) exception and implement safeguards, including human intervention and contest rights; the facts establish neither. (GDPR Art. 22, GDPR Rec. 71)
2. [Required] Transaction history: document why each data category and its scope are necessary for credit scoring, and minimise what is used and retained. (GDPR Art. 5)
3. [Required] Device fingerprint: establish its necessity and proportionality for this scoring purpose; exclude or reduce it if not necessary and set a justified retention period. (GDPR Art. 5)
4. [Required] Browsing behaviour: justify its necessity and compatibility with the disclosed scoring purpose; minimise collection and retention, or do not use it. (GDPR Art. 5)
5. [Required] Document an Article 6 legal basis for scoring and for sharing scores with the vendor; the transfer mechanism does not itself establish a lawful processing purpose. (GDPR Art. 6(1))
6. [Required] Complete a GDPR DPIA before processing and provide a notice explaining profiling, data categories, purposes, legal basis, recipients, retention, and meaningful information about the automated decision and its consequences. (GDPR Art. 35(3), GDPR Art. 13(1), GDPR Art. 13(2))
7. [Required] Creditworthiness assessment is high-risk AI, not the financial-fraud detection exception. Before deployment, complete the required fundamental-rights impact assessment and meet deployer obligations, including use according to instructions, monitoring, and log retention. (AI Act Annex III point 5, AI Act Art. 27(1), AI Act Art. 26(1), AI Act Art. 26(5), AI Act Art. 26(6))
8. [Required] DPO review is required before build because the feature involves automated decision-making. This activity has no matching register entry; only DPO approval can make this assessment an organisational record. (GDPR Art. 22)
9. [Covered] The US vendor transfer is covered by the organisation’s stated Data Privacy Framework certification fact; record this transfer in the transfer log and verify the certification remains applicable. (GDPR Art. 45(1))

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

## A-004 · BNPL credit scoring using transaction history and device data

Feature: We're adding credit scoring to our buy-now-pay-later checkout using transaction history and device data. The score only flags an order; a credit analyst reviews every flagged order and takes the decision, and the customer is told how to appeal. Scores stay in-house.

Assistant's verdict: Proceed with conditions · risk high · high-risk AI True · DPIA True

Assistant's findings:
1. [Required] Transaction history: document a lawful basis and show which transaction fields are necessary and relevant to creditworthiness; exclude unnecessary history and set a justified retention period. (GDPR Art. 6(1), GDPR Art. 5)
2. [Required] Device data: identify the exact signals used and document necessity and relevance for credit scoring; exclude unrelated or excessive device signals and set a justified retention period. (GDPR Art. 6(1), GDPR Art. 5)
3. [Required] Complete a DPIA before processing: the systematic profiling and credit decision context is high risk, including under the specified evaluation-and-decision criteria where applicable. (GDPR Art. 35(1), GDPR Art. 35(3))
4. [Required] As deployer of high-risk creditworthiness AI, complete a fundamental-rights impact assessment before deployment and inform affected customers that the AI system is being used. (AI Act Art. 27(1), AI Act Art. 26(11))
5. [Required] Ensure competent, trained and authorised human oversight; verify input data is relevant and sufficiently representative, and retain system logs under your control for at least six months, subject to applicable data-protection rules. (AI Act Art. 26(2), AI Act Art. 26(4), AI Act Art. 26(6))
6. [Required] Tell customers the scoring purpose and legal basis, retention period, and meaningful information about the scoring logic and its significance and consequences; provide the information clearly and accessibly. (GDPR Art. 13(1), GDPR Art. 13(2), GDPR Art. 12(1))
7. [Covered] The stated analyst review and customer appeal route address the risk of a solely automated decision, provided the analyst independently considers the case and can change the outcome. (GDPR Art. 22, GDPR Rec. 71)

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

## A-005 · FAQ chatbot for order status and returns

Feature: A chatbot on our help page answers order-status and returns questions from our FAQ. It reads the order number the customer types, shows the status, and hands over to a human agent whenever the customer asks or the question is not in the FAQ. It takes no decisions about customers.

Assistant's verdict: Proceed with conditions · risk low · high-risk AI False · DPIA False

Assistant's findings:
1. [Required] Document a lawful basis for using the typed order number to retrieve status and handle the request; contract necessity may fit where this is needed to fulfil the customer’s order-related request. (GDPR Art. 6(1))
2. [Required] Limit chat inputs and status data to what is needed; set retention periods for transcripts and order-number data, and avoid keeping unrelated free-text content. (GDPR Art. 5)
3. [Required] Give users privacy information when collecting their order number and chat input, including purposes, legal basis, recipients, and retention period or criteria. (GDPR Art. 13(1), GDPR Art. 13(2))
4. [Required] If the chatbot is an AI system, identify it as AI at or before the user’s first interaction, unless that is already obvious in context. (AI Act Art. 50(1), AI Act Art. 50(5))
5. [Covered] The described chatbot only retrieves status and answers FAQs; it does not decide matters affecting customers, so GDPR automated-decision safeguards are not triggered on these facts. (GDPR Art. 22)
6. [Covered] The stated order-support function does not match the listed high-risk use cases, and no customer profiling or consequential decision is described. (AI Act Art. 6(2), AI Act Annex III)

Expected key findings:
- KF1: a clear notice at the start of the chat; the hand-over to a human is already there · provisions AI Act Art. 50(1) (alternatives: AI Act Art. 50) · severity Required · citation level article
- KF2: FAQ answers and order status are none of the Annex III uses and it takes no decisions · provisions AI Act Annex III (alternatives: AI Act Art. 6(3), AI Act Art. 6) · severity Covered · citation level article
- KF3: say how long transcripts are kept and that they are processed; keep them short · provisions GDPR Art. 5(1)(e), GDPR Art. 13 (alternatives: GDPR Art. 5) · severity Required · citation level paragraph

- [A-005 KF1] verdict: 
- [A-005 KF2] verdict: 
- [A-005 KF3] verdict: 

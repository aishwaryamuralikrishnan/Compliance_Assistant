# Tools

The agents (the worker and the reviser) can call four tools. Three are **read** tools: cheap and read-only. One is a **write** tool: it creates the review task and pauses the run until the DPO decides. No tool writes the processing register. The register entry is written by the tool gate itself when the DPO approves, under the DPO's identity. The requester and the approver are therefore always different people.

## Tool inventory

| Tool | Kind | What it does | Used by |
|---|---|---|---|
| `search_regulation(query, regulation?, k)` | 🟢 read | Hybrid search over the GDPR and the AI Act for one topic. Returns up to k passages, each with its citation label | worker, reviser. `direct_answer` calls the same search directly, one pass, no agentic loop |
| `get_article(regulation, article, paragraph?)` | 🟢 read | Returns the exact text of one article or paragraph, when the agent already knows the identifier | worker, reviser |
| `lookup_register(query \| id)` | 🟢 read | Finds existing register entries, so the agent can say "this is already recorded as A-…" | worker, reviser |
| `request_dpo_review(assessment_id)` | 🟡 write | Called automatically after every verified assessment. Creates the review task and pauses the run. The DPO's decision resumes it; an approval writes the register entry from inside the gate | worker, reviser (the gate does the work) |
| `export_register` | 🟢 read | PDF export of the register for audits: the overview table and every recorded assessment in full | the Register page (DPO only); not an agent tool |

**Helper functions.** These run inside nodes. The agent cannot call them.

| Function | What it does | Runs in |
|---|---|---|
| `grade_chunks`, `rewrite_query` | The grader and the query rewrite of the agentic RAG loop ([AGENTS.md](AGENTS.md), section 5) | inside `search_regulation` |
| `verify_citations` | Checks every cited label against the corpus | `output_guardrail` |
| `pii_redact`, `pii_scan_output` | Redaction on the way in; a check that nothing leaks on the way out | `validate_input`, `output_guardrail` |
| `jev_router`, `llm_router` | The classifier behind the route node, and its LLM fallback | `route` |
| `seed.py` | One-off setup: ingests the corpus, writes the organisation facts into memory, creates the two demo users | outside the graph |

## Who may call what

| Tool | product_manager | dpo | Note |
|---|---|---|---|
| `search_regulation` | 🟢 yes | 🟢 yes | read-only, cheap |
| `get_article` | 🟢 yes | 🟢 yes | read-only, cheap |
| `lookup_register` | 🟢 yes | 🟢 yes | read-only |
| `request_dpo_review` | 🟢 yes | 🔴 no | the product manager's only write. The DPO never requests a review: the DPO has no Assistant page |
| *(register write)* | 🔴 no | 🟡 by decision | not a tool. Happens inside the tool gate when the DPO approves a paused request |
| `export_register` | 🔴 no | 🟢 yes | a button on the Register page |

The matrix lives in `config/roles.yaml`. The agent only ever sees its role's tools, and the tool gate re-checks the role on every call anyway. The reviser runs under the requester's role, so it has the same tools as the worker. Memory writes follow the same file (`memory_writes`): a product manager may write only their own preferences; organisation facts and lessons come from DPO actions.

## The tool gate

Every tool call of the worker or the reviser passes through `ToolGateMiddleware` (`compliance_agent/nodes/middleware.py`). Four checks, in this order:

1. **Doom-loop exit.** The same tool with the same arguments a third time is refused. The agent is told to use the earlier result and finish. A budget of 14 real tool calls per run caps the whole turn (`ToolBudgetMiddleware`).
2. **Permission re-check** against the matrix above. A denied call returns the role's `denied_message` to the agent.
3. **Human-in-the-loop.** For `request_dpo_review`, the gate creates the review task and calls `interrupt()`. The DPO's decision resumes the thread under the DPO's identity, and the gate applies it:
   - **approve**: writes the register entry and stores the ticked memory items;
   - **request changes**: marks the assessment "changes requested", stores the requirement as a lesson, and continues into the second pause, `pm_revision`;
   - **reject**: records nothing.
4. **Allowed** calls run. The result goes back to the agent and every outcome is streamed to the trace.

The resumed call is judged by the requester's permission, not the DPO's. The task already exists, so the DPO needs no write tool of its own.

## The second pause: `pm_revision`

Not a tool, but the same mechanism. After *Request changes*:

- `pm_revision` calls `interrupt()` with the requested changes, the DPO's comment and the previous description.
- The product manager's *Run revision* resumes the thread with the revised description and a done / not possible answer per request.
- The node briefs the reviser from the thread's state. Version 2 comes back through the gate to the DPO.

Two checks happen on the resume. Both are deterministic. A failed check pauses the thread again and shows the reason:

- only the thread's requester may resume it (not the DPO, not another product manager);
- the revised description must pass the same hard limits, redaction and injection patterns as a first input.

The revised description is not sent to the small model that screens a first input. The thread already is an assessment of this feature, so the on-topic question is pointless. Everything the reviser produces still passes the output guardrail and then the DPO. A model call inside the resume would also make the pause depend on a helper model being up.

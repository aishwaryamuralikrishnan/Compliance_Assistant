# Technical notes

Setup, running, models, tests and housekeeping. How the agent works is in [AGENTS.md](AGENTS.md); the tools in [TOOLS.md](TOOLS.md).

## Stack

| Part | Technology |
|---|---|
| Language | Python 3.12 |
| Agent | LangGraph + LangChain 1.x |
| Models | OpenRouter (one key, any vendor) |
| Database | Postgres 16 + pgvector in Docker: the checkpointer, the long-term store and the RAG corpus in one database |
| Backend | FastAPI |
| Front end | React (Next.js), Node.js 20+ |

## Project layout

| Folder or file | What is in it |
|---|---|
| `api/` | The web API: auth (JWT cookie), oidc (sign in with Google), threads, reviews, register, memory, meta, evaluation (the public report) |
| `web/` | The React front end: login, assistant, review queue, register, memory, the public `/evaluation` pages |
| `compliance_agent/` | The agent package. It knows nothing of the UI |
| `compliance_agent/graph.py` | The graph wiring: `run_turn`, `resume_turn`, `send_feedback`, `thread_state` |
| `compliance_agent/nodes/` | `validate_input`, `route`, `direct_answer`, `worker` + `reviser` (+ middleware), `guardrail`, `memory_write`, `pm_revision` |
| `compliance_agent/retrieval/` | Identifiers, hybrid search + RRF, reranker, grader, rewrite, the loop |
| `compliance_agent/tools/` | `search_regulation`, `get_article`, `lookup_register`, `request_dpo_review` |
| `compliance_agent/models.py` | The model registry: slot → model via OpenRouter |
| `compliance_agent/memory.py` | The store namespaces, memory proposals, role-gated writes |
| `compliance_agent/db.py`, `repo.py` | The database pool, the schema, data access |
| `compliance_agent/export.py`, `retention.py` | The PDF export of the register; checkpoint retention |
| `compliance_agent/viz.py`, `trace.py` | The live-graph layout and the trace, served as JSON by the API |
| `ingest/` | EUR-Lex download, the legal-structure chunker, the seed script |
| `config/` | `models.yaml` (slots and prices), `roles.yaml` (permissions, memory policy), `corpus.yaml`, `prompts/` (every prompt, as YAML) |
| `scripts/` | `check_env`, `admin`, `list_models`, the probes (`probe_models`, `probe_slot`, `probe_grader`, `probe_provider`), `draw_graph`, `eval_pdf`, `container_start` |
| `eval/` | The evaluation harness: `data/` (the test sets), `harness/`, `prompts/`, `report/` (the PDF), `results/` |
| `tests/` | pytest. Graph flows run on a scratch database with a canned corpus |
| `docs/Compliance/` | Evidence for README section 3: the gateway's terms and privacy policy, the account's data-policy settings, the probe output |
| `docs/images/` | The pictures used in the documentation |
| `site/` | The project website (static HTML, deployed on Vercel) |
| `docker-compose.yml` | Three containers: `db`, `api` (`Dockerfile.api`), `web` (`web/Dockerfile`) |

## Setup and run

**Once:**

```powershell
python -m pip install -r requirements.txt
copy .env.example .env            # DB defaults are fine; put OPENROUTER_API_KEY in .env or the OS environment
```

**Start the database** (Docker Desktop must be running):

```powershell
docker compose up -d db
docker compose ps                 # wait until compliance_db is "healthy"
```

**Check the environment and seed** (first time only):

```powershell
python scripts/check_env.py       # shows the OpenRouter key in use (masked), Postgres + pgvector, corpus counts, one model call, one embedding
python -m ingest.seed all         # schema, corpus from data/corpus/raw/, users, seeded memory
```

The EUR-Lex pages are saved by hand from a browser, under the names printed by `python -m ingest.seed urls`.

**Run:**

```powershell
uvicorn api.main:app --reload --port 8000       # the web API: http://localhost:8000/docs
cd web; npm install; npm run dev               # the front end: http://localhost:3000 (proxies /api to :8000)
```

**Sign in.** Two seeded demo accounts: `lena.k` (product manager) and `m.weber` (DPO), passwords from `.env`. Sign in with Google appears on the login page when `OIDC_CLIENT_ID` is set:

- a first sign-in creates a product manager from the verified e-mail address;
- the addresses in `DPO_EMAILS` sign in as DPO;
- `OIDC_DEFAULT_ROLE=deny` admits only accounts the users table already knows;
- the role is decided by the users table at every sign-in, never by Google;
- the redirect URI to register with Google is `PUBLIC_BASE_URL` + `/api/auth/oidc/callback`.

## Run everything in containers

The alternative for a hand-over or a reviewer: the API and the front end as containers next to the database.

```powershell
docker compose up --build         # first time: a few minutes while the corpus is downloaded, chunked and embedded
docker compose logs -f api        # "first start: ...", then "serving the API on port 8000"
```

Then: http://localhost:3000 (the app), http://localhost:8000/docs (the API), http://localhost:3000/evaluation (the report).

- On first start the `api` container waits for the database, creates the schema and seeds: the corpus (needs `OPENROUTER_API_KEY`), the two accounts (`SEED_PM_PASSWORD`, `SEED_DPO_PASSWORD`) and the seeded memory.
- The seed passwords must be your own and at least 12 characters. A shorter one, or an old example password, stops the seeding (and the first container start) with an error.
- A restart never re-embeds or overwrites memory. `SEED_ON_START=0` skips seeding.
- `docker compose down -v` wipes the database; the next start seeds again.

## Models

Every node asks the model registry for a *slot*. `config/models.yaml` maps each slot to an OpenRouter model id, a display name and a price. Changing a model is one line there, no code change.

| Graph node | Model type | Model | Slot |
|---|---|---|---|
| validate_input | small LLM + regex | Gemini 3.1 Flash Lite | `cheap` |
| route | classifier; LLM fallback | TypeSafe Jev Router | `router` |
| direct_answer | heavy LLM | GPT-6 Luna | `worker_quick` |
| worker | heavy LLM | GPT-6 Luna | `worker_full` |
| reviser | heavy LLM | GPT-6 Luna | `worker_full` |
| search: embeddings | embeddings | Text Embedding 3 Small | `embeddings` |
| search: reranker | small LLM, listwise (since 3 Nov) | Gemini 3.1 Flash Lite | `reranker` (`method: llm`) |
| search: grader | heavy LLM | GPT-6 Luna | `grader` |
| search: query rewrite | small LLM | Gemini 3.1 Flash Lite | `cheap` |
| worker · summariser | small LLM | Gemini 3.1 Flash Lite | `cheap` |
| memory_write · reflect | small LLM | Gemini 3.1 Flash Lite | `cheap` |
| tool gate, interrupt, output_guardrail, pm_revision | none (deterministic) | – | – |
| *(evaluation only)* judge | small LLM from a third vendor | Claude Haiku 5.5 | `judge` |

Setting of 3 November 2026. Prices per 1M tokens: GPT-6 Luna $0.10 in / $0.50 out (cached input $0.01); Gemini 3.1 Flash Lite $0.25 / $1.50. A full assessment costs a few cents.

- The judge comes from a third vendor, so no model scores its own family's output.
- The reranker switched from Cohere's Rerank 4 Fast to the small model on 3 November. The gateway's reranker has no zero-data-retention endpoint.
- The embeddings slot must not change after the corpus is indexed. If it does, re-index with `python -m ingest.seed reindex`.
- `python scripts/list_models.py <word>` lists the model ids your key can use. Alternatives for the workers are noted in `config/models.yaml`.
- The run-stats estimate in the app covers the worker's calls only. The gateway's activity page is the figure to quote.

**Why the grader is the heavy model.** The grader must name the provision the retrieved passages lack, so that the rewrite can go to it. `python scripts/probe_grader.py` (ten queries) showed that the cheapest models cannot do that reliably; GPT-6 Luna named the article every time. The grader never sees an assessment, only passages from the database against a ten-word query, so using the worker's model is not a conflict. The slot can be pointed at any other model with one line; the probe is the way to compare candidates.

## Prompts

No prompt is written in the Python code. Each one is text in `config/prompts/`, loaded by `compliance_agent/prompts.py`. Changing a prompt is an edit in one of these files.

| File | Prompts |
|---|---|
| `agents.yaml` | Worker, reviser, the note per role, the thread summary |
| `screening.yaml` | Input screen, router |
| `retrieval.yaml` | Grader, reranker, query rewriter |
| `answers.yaml` | Quick answer |
| `memory.yaml` | The rewrite of a comment into one stored sentence |
| `shared.yaml` | The two trust-boundary rules, included by the others with `{{data_rule}}` and `{{memory_rule}}` |

## Run the evaluation

The harness never runs against the demo database. Every evaluation case runs the real app code: it stores a draft, creates a review task in the DPO's queue and leaves the thread paused. Run against the demo database, a set of 20 cases would fill the queue and the memory with test data, and the learned lessons would change the next run's results. The harness therefore needs its own copy, made once from the seeded one (the corpus and its vectors are copied, nothing is re-embedded):

```sql
CREATE DATABASE compliance_eval TEMPLATE compliance;
```

Set `EVAL_DATABASE_URL` in `.env` to that database (for example `postgresql://compliance:compliance@localhost:5432/compliance_eval`). Before each run, reset the copy to the seeded state:

```powershell
$env:DATABASE_URL = "postgresql://compliance:compliance@localhost:5432/compliance_eval"
python scripts/admin.py reset
python scripts/admin.py memory --clear-learned
python scripts/admin.py memory          # must list seeded items only
Remove-Item Env:DATABASE_URL
```

Then run a set (`pip install -r requirements-eval.txt` first):

```powershell
python -m eval.run_eval check           # validates the test data, no model calls
python -m eval.run_eval E6              # one set: E12, E3, E5, E6, E7 or all; writes eval/results/<set>_<timestamp>/
```

The method, the sets and the results are in the public report (README section 2). A full run of all sets costs about $1 on the gateway.

## Tests

```powershell
pytest tests -q                                                               # 89 tests, about 2 min
pytest tests -q --cov=compliance_agent --cov=api --cov-report=term-missing    # with line coverage
```

- Tests run on a scratch database (`compliance_test`, created automatically). The register and the memory are never touched.
- No test calls a model or the gateway. The worker and the reviser run a scripted model; retrieval, corpus and the input screens are canned (`tests/fakes.py`).
- Line coverage on 23 October 2026: **92 %** of `compliance_agent/` and `api/` (89 % without the seeded corpus). Coverage measures the code, not the agent's output quality; that is the evaluation (README section 2).

| Test file | What it covers |
|---|---|
| `test_graph.py` | The graph's flows: reject, a full assessment through the DPO's three decisions, the revision loop, the guardrail's rules, retention, the live-graph layout |
| `test_api.py`, `test_api_edges.py` | The web API over HTTP, the event stream and its replay, refusals and error reports |
| `test_oidc.py` | Google sign-in with the provider stubbed: first sign-in, the DPO allow-list, refusals |
| `test_quick_path.py` | The quick path: a question routed quick, an empty answer reported, a preference note |
| `test_retrieval_loop.py` | Every branch of the agentic RAG loop and the grader's decision rule |
| `test_rerank_and_tools.py` | The reranker's three paths and the tools' own refusals |
| `test_screens_and_memory.py` | The input screen, the router's fallback order, the memory proposals, the role-gated store write |
| `test_retrieval.py` | Identifiers and rank fusion (its database tests need a seeded corpus) |
| `test_chunker.py`, `test_seed_offline.py` | The ingestion |

## Two things to know before changing the model code

- **Prompt caching is the provider's job.** Nothing is sent to enable it. The gateway reports cached tokens and the run stats price them (`cached_input` in `config/models.yaml`).
- **The message history sent to a model is always balanced.** Strict providers reject a request unless every tool call has exactly one answer, in order. An unusable model output is answered at once with an error tool message. `repair_tool_pairs` checks the history before every call and reports any repair in the trace.

## Housekeeping

`scripts/admin.py` lists and prunes what testing leaves behind. Every delete asks for confirmation (`--yes` skips it).

```powershell
python scripts/admin.py register                 # list the register
python scripts/admin.py register --dedupe        # keep the newest entry per title
python scripts/admin.py memory                   # list every memory item with key, source, author
python scripts/admin.py memory --clear-learned   # back to the seeded memory
python scripts/admin.py reset                    # fresh demo state; corpus, users and seeded memory stay
python scripts/admin.py prune-threads --days 30  # delete the saved state of finished conversations older than 30 days
python scripts/admin.py forget <user>            # a person's erasure request
```

Restart the API after a `reset`. Against the hosted database, set `DATABASE_URL` to its connection string for that one command.

**Checkpoint retention** (`prune-threads`):

- The checkpointer saves the whole graph state after every node. That is what makes pause and resume work, and it grows without bound.
- `prune-threads` deletes the checkpoints of threads that are finished and older than the cut-off. Nothing else: assessments, review tasks, the register and the memory stay.
- A thread with anything open on it is kept, whatever its age: paused for the DPO or the product manager, a run stopped half-way, a pending review task.
- A thread whose state cannot be read is kept and reported, not deleted on a guess.
- On the hosted demo a nightly GitHub Actions job runs it (`compliance_agent/retention.py`).

**A person's deletion request** (`forget`):

- Deleted: the account, the person's conversations with their saved state, the assessments and review requests they made, their own memory namespace.
- Kept: register entries and memory items that are the organisation's record, with the person's name replaced by `deleted user`.

## Stop

```powershell
docker compose down               # stops the containers, keeps the data
docker compose down -v            # also wipes the data (the next start seeds again)
```

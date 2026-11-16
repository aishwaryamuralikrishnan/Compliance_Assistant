# E12 · 2026-11-16T12:49:19+00:00

commit `7af0da6` · database `localhost/compliance_eval` · 45 cases

models: `worker_full` = openai/gpt-6-luna · `worker_quick` = openai/gpt-6-luna · `cheap` = google/gemini-3.1-flash-lite · `judge` = anthropic/claude-haiku-5.5 · `embeddings` = openai/text-embedding-3-small · `reranker` = cohere/rerank-4-fast · `router` = typesafe/jev-router · `grader` = openai/gpt-6-luna

## E1 router

| metric | result | target |
|---|---|---|
| route accuracy | 44 of 45 (0.98) | ≥ 0.90 |
| fallback (Jev did not answer) | 0 of 45 (0.00) | reported |

Wrong routes: R-042 (full → reject)

## E2 input screen

| metric | result | target |
|---|---|---|
| injection detected | 7 of 7 | ≥ 6 of 7 |
| PII detected | 7 of 7 | ≥ 6 of 7 |
| off-topic detected | 4 of 4 | 4 of 4 |
| false positives on clean rows | 0 of 27 (0.00) | ≤ 3 |
| redaction counts exact | 7 of 7 | all |
| model cost of the run | $0.0074 | – |

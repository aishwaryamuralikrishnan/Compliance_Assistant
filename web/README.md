# Compliance Assistant — web front end

Next.js (App Router, TypeScript) over the FastAPI backend in `../api` (the API contract is the OpenAPI page at http://localhost:8000/docs).

    npm install
    npm run dev          # http://localhost:3000; the API must run on :8000 (uvicorn api.main:app --reload --port 8000)

`/api/*` is proxied to the backend (`next.config.ts`), so the session cookie is first-party. `API_URL` points the
proxy elsewhere.

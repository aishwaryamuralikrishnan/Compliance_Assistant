"""Rate limits (slowapi). One limiter for the whole API; the limits are per client IP and kept in memory,
so they are per process and start again when the API restarts."""
from __future__ import annotations

from fastapi import Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

LOGIN_LIMIT = "5/minute"          # password guesses on POST /api/auth/login, per client IP

limiter = Limiter(key_func=get_remote_address)


def too_many_requests(request: Request, exc: RateLimitExceeded) -> JSONResponse:
    """429 in the same shape as the API's other errors (`detail`), so the login page can show it."""
    return JSONResponse(status_code=429, content={"detail": "Too many login attempts. Wait a minute and try again."})

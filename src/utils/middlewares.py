from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class AddAsyncSessionToRequiestMiddleware(BaseHTTPMiddleware):
    ...
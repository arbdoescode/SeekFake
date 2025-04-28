from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class CheckValueMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, skip_paths: list[str] = None):
        super().__init__(app)
        self.skip_paths = skip_paths or []

    async def dispatch(self, request: Request, call_next):
        if request.url.path in self.skip_paths:
            return await call_next(request)

        check_value = request.headers.get("token_valid")
        if check_value != "expected_token":
            return JSONResponse(
                status_code=400,
                content={"error": "Invalid or missing token"},
            )

        return await call_next(request)

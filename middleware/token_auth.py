from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from config.databaseAzure import conn
import asyncio

# class CheckValueMiddleware(BaseHTTPMiddleware):
#     def __init__(self, app, skip_paths: list[str] = None):
#         super().__init__(app)
#         self.skip_paths = skip_paths or []

#     async def dispatch(self, request: Request, call_next):
#         if request.url.path in self.skip_paths:
#             return await call_next(request)

#         check_value = request.headers.get("token_valid")
#         if check_value != "expected_token":
#             return JSONResponse(
#                 status_code=400,
#                 content={"error": "Invalid or missing token"},
#             )

#         return await call_next(request)
    

class CheckValueMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, skip_paths: list[str] = None):
        super().__init__(app)
        self.skip_paths = skip_paths or []

    async def dispatch(self, request: Request, call_next):
        if request.url.path in self.skip_paths:
            return await call_next(request)

        token = request.headers.get("token")
        if not token:
            return JSONResponse(status_code=400, content={"error": "Missing token"})

        username = await asyncio.to_thread(self.get_username_from_token, token)

        if not username:
            return JSONResponse(status_code=401, content={"error": "Invalid token"})

        request.state.username = username
        return await call_next(request)

    def get_username_from_token(self, token: str):
        cursor = conn.cursor()
        cursor.execute("SELECT Username FROM [Session] WHERE Token = ?", (token,))
        row = cursor.fetchone()
        cursor.close()
        return row[0] if row else None
        


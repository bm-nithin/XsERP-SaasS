from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
import logging
import json
from auth.request_handler import RequestHandler
from auth.views import logout
from settings import CURRENT_VERSION
from util.api_util import session_timeout

logger = logging.getLogger("middleware")

# List of URLs that do not require authentication
LOGIN_EXEMPT_URLS = (
    "/broadcast", "/version-info", "/json-login", "/auth/change-password", "/auth/forget-password",
    "/auth/register-enterprise", "/validate-and-register-enterprise", "/send-sign-up-mail", "/erp/css/",
    "/site-media", "/erp/login/", "/erp/public/contact/", "/erp/sales/sales_estimate/client_status/",
)


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        request_handler = RequestHandler(request)

        # Exempt certain URLs from authentication
        if any(path.startswith(exempt) for exempt in LOGIN_EXEMPT_URLS):
            logger.info(f"Request exempted from authentication - {path}")
            return await call_next(request)

        # Check if session is active
        if request_handler.isSessionActive():
            return await call_next(request)

        # If session expired, return response
        if "/json/" in path:
            return Response(json.dumps(session_timeout()), media_type="application/json")

        return Response(
            json.dumps({"message": "Your session has expired!", "current_version": CURRENT_VERSION}),
            media_type="application/json",
            status_code=401
        )

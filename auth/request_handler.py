from datetime import datetime, timedelta
import jwt
from fastapi import Request
from core.config import settings
import logging

logger = logging.getLogger("auth")


class RequestHandler:
    def __init__(self, request: Request):
        self.request = request

    def getSessionAttribute(self, key):
        return self.request.session.get(key, None)

    def isSessionActive(self):
        """
        Checks if the user session is active using JWT or session attributes.
        """
        try:
            token = self.getSessionAttribute("LOGIN_TOKEN")
            if not token:
                return False

            decoded_token = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
            expired_on = datetime.strptime(decoded_token['expired_on'], "%Y-%m-%d %H:%M:%S")

            if expired_on > datetime.now():
                return True
        except Exception as e:
            logger.error(f"Session expired: {e}")
        return False

    def generateJwtToken(self, user_id, enterprise_id):
        """
        Generates a JWT token for authentication.
        """
        login_on = datetime.now()
        expired_on = login_on + timedelta(seconds=settings.SESSION_COOKIE_AGE)

        token = {
            "user_id": user_id,
            "enterprise_id": enterprise_id,
            "login_on": login_on.strftime("%Y-%m-%d %H:%M:%S"),
            "expired_on": expired_on.strftime("%Y-%m-%d %H:%M:%S"),
        }
        return jwt.encode(token, settings.JWT_SECRET, algorithm="HS256")

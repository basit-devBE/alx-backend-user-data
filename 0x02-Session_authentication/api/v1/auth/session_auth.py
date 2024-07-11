#!/usr/bin/env python3
""" Module of Session Authentication
"""

from api.v1.auth.auth import Auth
from models.user import User
import uuid
import os


class SessionAuth(Auth):
    """ Session Authentication class
    """
    user_id_by_session_id: dict = {}

    def __init__(self) -> None:
        """ SessionAuth constructor
        """
        pass
        """ Session ID to User ID mapping """
    def create_session(self, user_id: str = None) -> str:
        """Creates a session ID for a user ID
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
    

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name)

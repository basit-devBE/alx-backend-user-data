from flask import request
from typing import List

class Auth:
    """a class to control authentication for the api
    """
    def __init__(self) -> None:
        pass

    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks if a path requires authentication
        """
        return True
    
    def authorization_header(self, request=None) -> str:
        """checks the authorization header
        """
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """returns the current user
        """
        return None

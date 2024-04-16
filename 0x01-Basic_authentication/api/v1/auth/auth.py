#!/usr/bin/env python3
''' Auth class module
'''


from typing import List, TypeVar
from flask import request


class Auth:
    ''' class to manage the API authentication
    '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for the given path.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Get the authorization header from the flask request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Get the current user based on the request.
        """
        return None

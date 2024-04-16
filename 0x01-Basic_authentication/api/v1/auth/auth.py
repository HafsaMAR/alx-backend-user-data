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
        Returns True if the path is not in the list of excluded_paths.
        Returns True if path is None or excluded_paths is None or empty.
        Returns False if path is in excluded_paths.
        """
        if path is None or not excluded_paths:
            return True
        for excluded_path in excluded_paths:
            if path.startswith(excluded_path):
                return False
        return True

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

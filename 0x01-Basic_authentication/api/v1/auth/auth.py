#!/usr/bin/env python3
''' Auth class module
'''


import re
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
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Get the authorization header from the flask request.
        Returns None if request is None or
        if the header key Authorization is not present.
        Otherwise, returns the value of the Authorization header.
        """
        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Get the current user based on the request.
        """
        return None

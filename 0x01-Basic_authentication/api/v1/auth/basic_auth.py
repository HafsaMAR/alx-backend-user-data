#!/usr/bin/env python3
"""Basic authentication module for the API.
"""
import re
import base64
import binascii
from typing import Tuple, TypeVar

from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Basic authentication class.
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header
        for a Basic Authentication.
        """
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            match = re.fullmatch(pattern, authorization_header.strip())
            if match is not None:
                return match.group('token')
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        ''' decode the base64 string
        '''
        if base64_authorization_header is None or type(
                base64_authorization_header) != str:
            return None

        try:
            # decode the base64-encoded to bytes
            decoded_bytes = base64.b64decode(base64_authorization_header)
            # decode the bytes to a UTF-8 string
            decoded_string = decoded_bytes.decode('utf_8')
            return decoded_string
        except binascii.Error:
            # decoding actually failed
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> Tuple[(str, str)]:

        ''' Return the credentials of the user
        '''
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None
        username, password = decoded_base64_authorization_header.split(':', 1)
        return username.strip(), password.strip()

    def user_object_from_credentials(
            self,
            user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        '''get user object from input credentials'''
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        # seqrch for User instance with the given email
        matching_users = User.search({'email': user_email})
        if not matching_users:
            return None
        for user in matching_users:
            # use the is_valid_password User class method
            if user.is_valid_password(user_pwd):
                return user
        return None

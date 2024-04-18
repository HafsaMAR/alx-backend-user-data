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

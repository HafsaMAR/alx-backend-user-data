#!/usr/bin/env python3
'''authentication module and hashing
'''

import bcrypt
from db import DB
from user import User
import uuid
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''register a new user using email and pswd
        '''
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            pass
        hashed_password = _hash_password(password)
        user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        '''check credentials
        '''
        user = None
        try:
            user = self._db.find_user_by(email=email)
            hashed_password = user.hashed_password
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
        except NoResultFound:
            return False
        return False
    
    def _generate_uuid() -> str:
        '''Generate a new UUID string representation
        '''
        new_uuid = uuid.uuid4()

        uuid_string = str(new_uuid)
        return uuid_string

#!/usr/bin/env python3
'''DB module
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session


from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        '''add a new user object to the db based on
        its email and hashedpassword
        '''
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            new_user = None
        return new_user

    def find_user_by(self, **kwargs) -> User:
        '''Find a user in the database based on input arguments

        args:
            **kwargs: Arbitrary keyword arguments to filter the query
        '''

        # construct a query to select users based on input
        query = self._session.query(User)
        # apply input arguments as filter to the query
        query = query.filter_by(**kwargs)
        if query is None:
            raise InvalidRequestError()
        # Retrieve the first result found
        user = query.first()
        if user is None:
            raise NoResultFound()
        return user

from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)
        
        user = self._user_repository.find_by_username(username)
        if user:
            raise UserInputError("Username is in use")

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        for c in username:
            if re.match('[a-z]', c) == None:
                raise UserInputError("Username should consist of characters a-z")
        if len(username) < 3:
            raise UserInputError("Username should be at least 3 characters")
        
        if len(password) < 8:
            raise UserInputError("Password should be at least 8 characters")
        fnd = False
        for c in password:
            if re.match('[a-z]', c) == None:
                fnd = True
        if not fnd:
            raise UserInputError("Password should not consist solely of characters")
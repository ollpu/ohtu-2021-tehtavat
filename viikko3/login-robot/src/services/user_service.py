import re
from entities.user import User


class UserInputError(Exception):
    pass

class AuthenticationError(Exception):
    pass

class RegistrationError(Exception):
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

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        if not re.match("^[a-z]+$", username):
            raise RegistrationError("Username contains invalid characters")
        if not re.match(".*[^a-z].*", password):
            raise RegistrationError("Password should not consist of only lowercase characters")
        if len(username) < 3:
            raise RegistrationError("Username is too short")
        if len(password) < 8:
            raise RegistrationError("Password is too short")

        if self._user_repository.find_by_username(username):
            raise RegistrationError("Username already in use")

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

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        if len(username) < 3:
            raise UserInputError("Username has to be atleast 3 characters long.")
        pattern = re.compile("^[a-z]+$")
        if pattern.match(username) == False:
            raise UserInputError("Username can only contain letters and numbers.")
        if len(password) < 8 or password.isalpha():
            raise UserInputError("Password has to be 8 characters long and can't only include letters and numbers")
        

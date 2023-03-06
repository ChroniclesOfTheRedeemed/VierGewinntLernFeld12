import random

from constants import Api
from persistenceapi import Persistence

import bcrypt


# Declaring our password


class UserManagement:

    def __init__(self):
        self.db = Persistence()
        self.sessions = {}

    # returns Auth Token
    def login(self, username, password_unhashed):
        status = "ok"
        user = self.db.load_user(username)
        if user and user.password == str(self.hash_password(password_unhashed)):
            token = str(self.generate_random_token())
            self.sessions[token] = username
            return status, token
        else:
            return "invalid", "0"

    def logout(self, token):
        print(self.sessions)
        del self.sessions[token]
        return Api.Json.ok

    def get_user_profile(self, username):
        user = self.db.load_user(username)
        return user.profile

    def add_user(self, username, password):
        if self.db.load_user(username):
            return "user already exists", "0"
        self.db.create_user(username, self.hash_password(password))
        return self.login(username, password)

    def hash_password(self, password: str):
        return bcrypt.hashpw(password.encode('utf-8'), b'$2b$12$X50ynTmqfshhtC59ZFpcv.')

    def generate_random_token(self):
        return random.getrandbits(128)

    def validate_token(self, token) -> bool:
        return token in self.sessions


user_manager = UserManagement()

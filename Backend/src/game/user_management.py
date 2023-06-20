import random
from datetime import datetime

import bcrypt

from src.game.constants import Api
from src.game.persistence_api import Persistence


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
            # log out if he was previously logged in
            previous_token = self.get_token_by_user(user.username)
            if previous_token:
                self.logout(previous_token)
                # datetime object containing current date and time
            now = datetime.now()
            # dd/mm/YY H:M:S
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            new_token = dt_string + " " + str(self.generate_random_token())
            self.sessions[new_token] = username
            return status, new_token
        else:
            return "invalid", "0"

    def logout(self, token):
        del self.sessions[token]
        return Api.Json.ok

    def add_user(self, username, password):
        if self.db.load_user(username):
            return "user already exists", "0"
        self.db.create_user(username, self.hash_password(password))
        return self.login(username, password)

    def get_user_profile(self, username):
        user = self.db.load_user(username)
        return user.profile

    def hash_password(self, password: str):
        return bcrypt.hashpw(password.encode('utf-8'), b'$2b$12$X50ynTmqfshhtC59ZFpcv.')

    def generate_random_token(self):
        return random.getrandbits(128)

    def validate_token(self, token) -> bool:
        return token in self.sessions

    def get_token_by_user(self, user: str):
        array = [key for key, value in self.sessions.items() if value == user]
        return array[0] if len(array) > 0 else None

    def get_online_list(self):
        return "ok", list(self.sessions.values())


user_manager = UserManagement()

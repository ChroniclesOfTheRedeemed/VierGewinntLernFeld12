
import random

from persistenceapi import Persistence

import bcrypt

# Declaring our password




class UserManagement:

    def __init__(self):
        self.db = Persistence()
        self.sessions = {}

    # returns Auth Token
    def login(self, username, password_unhashed):
        user = self.db.load_user(username)
        if user.password == str(self.hash_password(password_unhashed)):
            token = self.generate_random_token()
            self.sessions[username] = token
            return token
        else:
            return "invalid"

    def logout(self, username):
        del self.sessions[username]

    def get_user_profile(self, username):
        user = self.db.load_user(username)
        return user.profile

    def add_user(self, username, password):
        self.db.create_user(username, self.hash_password(password))

    def hash_password(self, password: str):
        return bcrypt.hashpw(password.encode('utf-8'), b'$2b$12$X50ynTmqfshhtC59ZFpcv.')

    def generate_random_token(self):
        return random.getrandbits(128)

    def validate_token(self, token, user) -> bool:
        if user in self.sessions:
            return self.sessions[user] == token
        else:
            return False

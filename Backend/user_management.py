
import random


print("hash value: %032x" % hash)

class UserManagement:

    def __init__(self):
        self.sessions = {}

    # returns Auth Token
    def login(self, username, password):
        pass

    def generate_random_token(self):
        return random.getrandbits(128)

    def validate_token(self, token, user) -> bool:
        if user in self.sessions:
            return self.sessions[user] == token
        else:
            return False

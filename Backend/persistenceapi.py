from json_storer import Storer


class Persistence:

    def __init__(self):
        pass

    def load_user(self, username):
        x = Storer.load("users")
        if username in x:
            return x[username]
        else:
            return "couldn't find user"

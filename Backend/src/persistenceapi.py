from src.json_storer import Storer

user_file = "users"


class User:

    def __init__(self, username, password, wins=0):
        self.username = username
        self.password = password
        self.wins = wins
        self.profile = {
            "wins": wins
        }

    def user_to_dict(self):
        return {
            "password": self.password,
            "profile": {
                "wins": self.wins
            }
        }

    @staticmethod
    def load_user(username, dict):
        password = dict["password"]
        wins = dict["profile"]["wins"]
        return User(username, password, wins)


class Persistence:

    def __init__(self):
        pass

    def load_user(self, username) -> User:
        x = Storer.load(user_file)
        print(x)
        if username in x:
            return User.load_user(username, x[username])

    def create_user(self, username, password):
        x = Storer.load(user_file)
        x[username] = {
            "password": str(password),
            "profile": {
                "wins": 0
            }
        }
        Storer.store(user_file, x)

    def delete_user(self, username):
        x = Storer.load(user_file)
        del x[username]
        Storer.store(user_file, x)

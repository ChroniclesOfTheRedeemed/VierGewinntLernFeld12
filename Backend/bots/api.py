import requests

base_url = "http://basicuser256.pythonanywhere.com"


def login(username, password):
    try:
        print("logging in")
        response = requests.post(base_url + "/login", json={"username": username, "password": password})
        data = response.json()
        print(data["status"])
        print(data["token"])
        return data
    except Exception as e:
        print(e)
        raise e


def create_account(username, password):
    try:
        print("API call to create an account")
        response = requests.post(base_url + "/create_user", json={"username": username, "password": password})
        data = response.json()
        print(data["status"])
        print(data["token"])
        return data
    except Exception as e:
        print(e)
        raise e


def logout(token):
    try:
        print("API call to log off")
        response = requests.post(base_url + "/logout", json={"token": token})
        data = response.json()
        print(data["status"])
        return data
    except Exception as e:
        print(e)
        raise e


def fetch_challengers(token):
    try:
        print("API call to fetch challengers")
        response = requests.post(base_url + "/fetch_challengers", json={"token": token})
        data = response.json()
        print(data["status"])
        print(data["challengers"])
        return data
    except Exception as e:
        print(e)
        raise e


def challenge(token, username):
    try:
        print("API call to challenge")
        response = requests.post(base_url + "/request_game", json={"token": token, "username": username})
        data = response.json()
        print(data["status"])
        return data
    except Exception as e:
        print(e)
        raise e


def get_state(token):
    try:
        print("API call to state")
        response = requests.post(base_url + "/state", json={"token": token})
        data = response.json()
        print(data["status"])
        return data
    except Exception as e:
        print(e)
        raise e


def move(token, column_number):
    try:
        print("API call to move")
        response = requests.post(base_url + "/move", json={"token": token, "coloumnNumber": int(column_number)})
        data = response.json()
        print(str(data))
        return data
    except Exception as e:
        print(e)
        raise e


def forfeit_game(token):
    try:
        print("API call to forfeit Game")
        response = requests.post(base_url + "/forfeit_game", json={"token": token})
        data = response.json()
        print(data["status"])
        return data
    except Exception as e:
        print(e)
        raise e


def fetch_online_users(token):
    try:
        print("API call to fetch Online Users")
        response = requests.post(base_url + "/fetch_online_users", json={"token": token})
        data = response.json()
        print(data["status"])
        return data
    except Exception as e:
        print(e)
        raise e


function_map = {
    "login": login,
    "create": create_account,
    "logout": logout,
    "view-challenges": fetch_challengers,
    "challenge": challenge,
    "view-game": get_state,
    "move": move,
    "forfeit": forfeit_game,
    "view-online-users": fetch_online_users
}

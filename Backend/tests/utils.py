from flask.testing import FlaskClient

from src.constants import Api


class GameResponse:
    def __init__(self, game_response):
        print(game_response)
        game_field = game_response[Api.Json.game_field] if Api.Json.game_field in game_response else {}
        double_array_game_field = []
        for column_name, column in game_field.items():
            double_array_game_field.append(column)
        self.game_field = double_array_game_field
        self.player1 = game_response[Api.Json.player1] if Api.Json.player1 in game_response else ""
        self.player2 = game_response[Api.Json.player2] if Api.Json.player2 in game_response else ""
        self.game_status = game_response[Api.Json.game_finish] if Api.Json.game_finish in game_response else ""
        self.last_move = game_response[Api.Json.last_move] if Api.Json.last_move in game_response else (-5, -5)
        self.player1turn = game_response[Api.Json.player1turn] if Api.Json.player1turn in game_response else None
        self.status = game_response[Api.Json.status_name]  # imposter


class ApiAbUser:
    def __init__(self, user_name: str, password: str, client: FlaskClient):
        self.name = user_name
        self.client = client
        login_response = self.client.post(Api.Url.login, json={
            Api.Json.username: user_name,
            Api.Json.password: password
        }).json
        self.token = login_response[Api.Json.token]

    def challenge(self, user_name):
        game_response = self.client.post(Api.Url.challenge, json={
            Api.Json.token: self.token,
            Api.Json.username: user_name
        }).json
        return game_response

    def move(self, move) -> GameResponse:
        move_response = self.client.post(Api.Url.move, json={
            Api.Json.token: self.token,
            Api.Json.move: move
        }).json
        return GameResponse(move_response)

    def fetch_game(self) -> GameResponse:
        game_response = self.client.get(Api.Url.state, json={
            Api.Json.token: self.token
        })
        return GameResponse(game_response.json)

    def fetch_challengers_util(self) -> []:
        game_response = self.client.get(Api.Url.fetch_challengers, json={
            Api.Json.token: self.token
        }).json
        return game_response[Api.Json.challengers]

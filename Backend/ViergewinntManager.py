import random

from persistenceapi import Persistence

import bcrypt

# Declaring our password
from user_management import user_manager
from vergewinntspiel import Viergewinnt


class GameObserver:

    def gameOver(self, player1wins):
        pass


class GameManagement(GameObserver):

    def __init__(self):
        self.db = Persistence()
        self.player1_sessions = {}
        self.player2_sessions = {}

    def fetch_state(self, token):

        if token in self.player1_sessions:
            game = self.player1_sessions[token]
        elif token in self.player2_sessions:
            game = self.player2_sessions[token]
        else:
            return "error"

        token1, token2 = self.get_tokens_by_game_id(game.id)
        return game.State, user_manager.sessions[token1], user_manager.sessions[token2]

    def request_solo_game(self, token):
        game = Viergewinnt(self)
        self.player1_sessions[token] = game
        self.player2_sessions[token] = game

        token1, token2 = self.get_tokens_by_game_id(game.id)
        return game.State, user_manager.sessions[token1], user_manager.sessions[token2]

    def make_move(self, token, move):
        # check validity
        # return vg4state
        pass

    def fetch_invites(self):
        pass

    def accept_invite(self):
        pass

    def get_game_by_token(self, token) -> Viergewinnt:
        if token in self.player1_sessions:
            return self.player1_sessions[token]
        if token in self.player2_sessions:
            return self.player2_sessions[token]

    def get_tokens_by_game_id(self, game_id):
        token_player_1 = "player_not_found"
        token_player_2 = "player_not_found"
        for token, game in self.player1_sessions.items():
            if game_id == game.id:
                token_player_1 = token

        for token, game in self.player2_sessions.items():
            if game_id == game.id:
                token_player_2 = token

        return token_player_1, token_player_2

    def gameOver(self, player1wins, game_id):
        print("GAMMEEEE OVEEEER")
        pass


game_manager = GameManagement()

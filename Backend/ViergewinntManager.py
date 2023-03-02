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
        user_name = user_manager.sessions[token]
        status = "ok"
        if user_name in self.player1_sessions:
            game = self.player1_sessions[user_name]
        elif user_name in self.player2_sessions:
            game = self.player2_sessions[user_name]
        else:
            return "no game found", None, None, None

        token1, token2 = self.get_usernames_by_game_id(game.id)
        return status, game.State, user_manager.sessions[token1], user_manager.sessions[token2]

    def request_solo_game(self, token):
        game = Viergewinnt(self)
        user_name = user_manager.sessions[token]
        self.player1_sessions[user_name] = game
        self.player2_sessions[user_name] = game
        token1, token2 = self.get_usernames_by_game_id(game.id)
        return "ok", game.State, user_manager.sessions[token1], user_manager.sessions[token2]

    def make_move(self, token, move):
        status = "ok"
        user_name = user_manager.sessions[token]
        player1_moved = False
        game = None
        if user_name in self.player1_sessions:
            game = self.player1_sessions[user_name]
            if game.State.player1turn:
                try:
                    game.playerMadeMove(move)
                    player1_moved = True
                except:
                    status = "bad move"
        if user_name in self.player2_sessions and not player1_moved:
            game = self.player2_sessions[user_name]
            if not game.State.player1turn:
                try:
                    game.playerMadeMove(move)
                except:
                    status = "bad move"
        if not game:
            status = "there is no game going on"
            return status, None, None, None
        else:
            token1, token2 = self.get_usernames_by_game_id(game.id)
            return status, game.State, user_manager.sessions[token1], user_manager.sessions[token2]


    def fetch_invites(self):
        pass

    def accept_invite(self):
        pass

    def get_game_by_user(self, user_name) -> Viergewinnt:
        if user_name in self.player1_sessions:
            return self.player1_sessions[user_name]
        if user_name in self.player2_sessions:
            return self.player2_sessions[user_name]

    def get_usernames_by_game_id(self, game_id):
        user_name_1 = "player_not_found"
        user_name_2 = "player_not_found"
        for token, game in self.player1_sessions.items():
            if game_id == game.id:
                user_name_1 = token

        for token, game in self.player2_sessions.items():
            if game_id == game.id:
                user_name_2 = token

        return user_name_1, user_name_2

    def get_userame_from_token(self, token):
        return user_manager.sessions[token]

    def gameOver(self, player1wins, game_id):
        print("GAMMEEEE OVEEEER")
        pass


game_manager = GameManagement()

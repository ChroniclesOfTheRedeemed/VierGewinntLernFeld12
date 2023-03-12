from src import V4State
from src.persistenceapi import Persistence
from src.user_management import user_manager
from src.vergewinntspiel import Viergewinnt


# Declaring our password


# exclude datatype logic from business logic / how to access objects -> capsule in getter

class GameObserver:

    def gameOver(self, player1wins):
        pass


class GameManagement(GameObserver):

    # session data format:
    # sessions =  {
    #   user1: game1,
    #   user2: game1}
    # challenges data format:
    # challenges = {
    #   token1:[challenger_username1, challenger2_username1]
    def __init__(self):
        self.db = Persistence()
        self.player1_sessions = {}
        self.player2_sessions = {}
        self.challenges = {}

    # check opponent is online
    #   check opponent is not in game
    #       check if I have been challenged by opponent already
    #           -> start game
    #       if not
    #           add challenges on enemy
    def challenge(self, token, opponent):
        opponent_token = user_manager.get_token_by_user(opponent)
        status = "ok"
        challenger = user_manager.sessions[token]
        if opponent_token:
            game = self.check_ongoing_game(opponent_token)
            if game:
                status = "Opponent is busy"
            else:
                if self.is_challenged(token, opponent):
                    self.start_game(challenger, opponent)
                    pass
                else:
                    if opponent_token in self.challenges:
                        self.challenges[opponent_token].append(user_manager.sessions[token])
                    else:
                        self.challenges[opponent_token] = [challenger]
        else:
            status = "Opponent is not available."
        # check opponent available
        # add to self challenges
        return status

    def is_challenged(self, token, by_user):
        return by_user in self.challenges[token] if token in self.challenges else False

    def fetch_challenges(self, token):
        return self.challenges[token] if token in self.challenges else []

    def forfeit_match(self, token):
        # some game over logic maybe?
        # also maybe don't access state value directly but use function to forfeit :D
        game = self.check_ongoing_game(token)
        user = user_manager.sessions[token]
        if game:
            if user in self.player1_sessions:
                game.State.result = V4State.player2wins
            if user in self.player2_sessions:
                game.State.result = V4State.player1wins
            return "ok"
        else:
            return "no ongoing game found"

    def check_ongoing_game(self, token):
        game: Viergewinnt
        user = user_manager.sessions[token]
        if user in self.player1_sessions:
            game = self.player1_sessions[user]
        elif user in self.player2_sessions:
            game = self.player2_sessions[user]
        else:
            return None
        if game.State.result != V4State.player1wins \
                and game.State.result != V4State.player2wins \
                and game.State.result != V4State.draw:
            return game

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
        return status, game.State, token1, token2

    # def request_solo_game(self, token):
    #     game = Viergewinnt(self)
    #     user_name = user_manager.sessions[token]
    #     self.player1_sessions[user_name] = game
    #     self.player2_sessions[user_name] = game
    #     token1, token2 = self.get_usernames_by_game_id(game.id)
    #     return "ok", game.State, token1, token2

    # start game
    #    add session to both users
    #   init game
    #   remove challenges on both users
    def start_game(self, user1, user2):
        game = Viergewinnt()
        self.remove_challenges(user_manager.get_token_by_user(user1))
        self.remove_challenges(user_manager.get_token_by_user(user2))
        self.player1_sessions[user1] = game
        self.player2_sessions[user2] = game
        return "ok"

    def remove_challenges(self, token):
        self.challenges[token] = []

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
                except V4State.BadMoveException:
                    status = "bad move"
                except V4State.GameEndedException:
                    status = "game has concluded already"
        if user_name in self.player2_sessions and not player1_moved:
            game = self.player2_sessions[user_name]
            if not game.State.player1turn:
                try:
                    game.playerMadeMove(move)
                except V4State.BadMoveException:
                    status = "bad move"
                except V4State.GameEndedException:
                    status = "game has concluded already"
        if not game:
            status = "there is no game going on"
            return status, None, None, None
        else:
            token1, token2 = self.get_usernames_by_game_id(game.id)
            return status, game.State, token1, token2

    def get_game_by_user(self, user_name) -> Viergewinnt:
        if user_name in self.player1_sessions:
            return self.player1_sessions[user_name]
        if user_name in self.player2_sessions:
            return self.player2_sessions[user_name]

    def get_usernames_by_game_id(self, game_id):
        user_name_1 = "player_not_found"
        user_name_2 = "player_not_found"
        for username, game in self.player1_sessions.items():
            if game_id == game.id:
                user_name_1 = username

        for username, game in self.player2_sessions.items():
            if game_id == game.id:
                user_name_2 = username

        return user_name_1, user_name_2

    def get_userame_from_token(self, token):
        return user_manager.sessions[token]



game_manager = GameManagement()

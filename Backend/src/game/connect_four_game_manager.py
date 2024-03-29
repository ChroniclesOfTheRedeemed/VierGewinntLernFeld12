from src.game import connect_four_state
from src.game.constants import Api
from src.game.player_integrations import player_integration_list
from src.game.user_management import user_manager
from src.game.connect_four_game import ConnectFourGame


class GameManagement:

    def __init__(self):
        self.player1_sessions = {}
        self.player2_sessions = {}
        self.challenges = {}

    def challenge(self, token, opponent_name):
        status = Api.StatusNames.ok
        opponent_token = self.get_token_by_name(opponent_name)
        challenger = user_manager.sessions[token]
        if opponent_token:
            game = self.check_ongoing_game(opponent_token)
            if game:
                status = Api.StatusNames.opponent_busy
            else:
                if self.is_challenged(token, opponent_name):
                    self.start_game(challenger, opponent_name)
                    pass
                else:
                    if opponent_token in self.challenges:
                        self.challenges[opponent_token].append(user_manager.sessions[token])
                    else:
                        self.challenges[opponent_token] = [challenger]
        else:
            status = Api.StatusNames.opponent_not_available
        return status

    def is_challenged(self, token, by_user):
        return by_user in self.challenges[token] if token in self.challenges else False

    def fetch_challengers(self, token):
        uhh = (Api.StatusNames.ok, self.challenges[token]) if token in self.challenges else (Api.StatusNames.ok, [])
        return uhh

    def forfeit_match(self, token):
        # some game over logic maybe?
        # also maybe don't access state value directly but use function to forfeit :D
        game = self.check_ongoing_game(token)
        user = user_manager.sessions[token]
        if game:
            if user in self.player1_sessions:
                game.State.result = connect_four_state.player2wins
            if user in self.player2_sessions:
                game.State.result = connect_four_state.player1wins
            return Api.StatusNames.ok
        else:
            return Api.StatusNames.there_is_no_game

    def check_ongoing_game(self, token):
        game: ConnectFourGame
        user = user_manager.sessions[token]
        if user in self.player1_sessions:
            game = self.player1_sessions[user]
        elif user in self.player2_sessions:
            game = self.player2_sessions[user]
        else:
            return None
        if game.State.result != connect_four_state.player1wins \
                and game.State.result != connect_four_state.player2wins \
                and game.State.result != connect_four_state.draw:
            return game

    def fetch_state(self, token):
        user_name = user_manager.sessions[token]
        status = Api.StatusNames.ok
        if user_name in self.player1_sessions:
            game = self.player1_sessions[user_name]
        elif user_name in self.player2_sessions:
            game = self.player2_sessions[user_name]
        else:
            return Api.StatusNames.no_game_found, None, None, None

        token1, token2 = self.get_usernames_by_game_id(game.id)
        return status, game.State, token1, token2

    def start_game(self, user1, user2):
        game = ConnectFourGame()
        self.remove_challenges(self.get_token_by_name(user1))
        self.remove_challenges(self.get_token_by_name(user2))
        if user1 in self.player2_sessions:
            del self.player2_sessions[user1]
        if user2 in self.player1_sessions:
            del self.player1_sessions[user2]
        self.player1_sessions[user1] = game
        self.player2_sessions[user2] = game
        return Api.StatusNames.ok

    def remove_challenges(self, token):
        self.challenges[token] = []

    def make_move(self, token, move):
        status = Api.StatusNames.not_your_turn
        user_name = user_manager.sessions[token]
        player1_moved = False
        game = None
        if user_name in self.player1_sessions:
            game = self.player1_sessions[user_name]
            if game.State.player1turn:
                try:
                    status = Api.StatusNames.ok
                    game.player_made_move(move)
                    player1_moved = True
                except connect_four_state.BadMoveException:
                    status = Api.StatusNames.bad_move
                except connect_four_state.GameEndedException:
                    status = Api.StatusNames.game_has_concluded_already
        if user_name in self.player2_sessions and not player1_moved:
            game = self.player2_sessions[user_name]
            if not game.State.player1turn:
                try:
                    status = Api.StatusNames.ok
                    game.player_made_move(move)
                except connect_four_state.BadMoveException:
                    status = Api.StatusNames.bad_move
                except connect_four_state.GameEndedException:
                    status = Api.StatusNames.game_has_concluded_already
        if not game:
            status = Api.StatusNames.there_is_no_game
            return status, None, None, None
        else:
            token1, token2 = self.get_usernames_by_game_id(game.id)
            return status, game.State, token1, token2

    def get_game_by_user(self, user_name) -> ConnectFourGame:
        if user_name in self.player1_sessions:
            return self.player1_sessions[user_name]
        if user_name in self.player2_sessions:
            return self.player2_sessions[user_name]

    def get_usernames_by_game_id(self, game_id):
        user_name_1 = Api.StatusNames.player_not_found
        user_name_2 = Api.StatusNames.player_not_found
        for username, game in self.player1_sessions.items():
            if game_id == game.id:
                user_name_1 = username

        for username, game in self.player2_sessions.items():
            if game_id == game.id:
                user_name_2 = username

        return user_name_1, user_name_2

    def get_userame_from_token(self, token):
        return user_manager.sessions[token]

    def get_token_by_name(self, name):
        if name in player_integration_list:
            # TODO make sure names do not clash with user tokens
            return name
        else:
            return user_manager.get_token_by_user(name)


game_manager = GameManagement()

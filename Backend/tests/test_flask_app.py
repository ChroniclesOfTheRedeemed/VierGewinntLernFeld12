from unittest import TestCase

from unittest import TestCase

from flask.testing import FlaskClient

from src import V4State
from src.constants import Api
from src.flask_app import find_properties_in_answer, app
from tests import utils
from tests.utils import ApiAbUser


class Test(TestCase):
    def test_find_properties_in_answer(self):
        args = ["token", "username", "your_mother", "yikers"]
        json = {
            "token": "geoisfdkvnpserb",
            "username": "cool",
            "your_mother": 328409,
            "yikers": True
        }
        print(find_properties_in_answer(args, json))
        r = find_properties_in_answer(args, json)
        a, b, c, d = r
        print(a, b, c, d)


class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.player1 = ApiAbUser("admin", "admins", self.app)
        self.player2 = ApiAbUser("admina", "admins", self.app)

    def test_game_forfeit(self):
        self.start_game_test(self.player1, self.player2)
        # two players play set of moves
        self.play_a_set_of_moves_test(self.player2, self.player1, utils.games_and_expectations.ongoing_game_1)
        self.forfeit_the_game_test(self.player1, self.player2, True)
        self.make_sure_game_ended([self.player1, self.player2])

        # interpret result

    def test_duel_integration_test(self):
        self.start_game_test(self.player1, self.player2)
        self.play_a_set_of_moves_test(self.player2, self.player1, utils.games_and_expectations.player2_vertical_win)
        self.make_sure_game_ended([self.player1, self.player2])

    # theoretically I only need loser
    # I can get winner by finding opponent through game
    # I can also get the player position through the game
    # choose this because I don't care, it's fine for now
    def forfeit_the_game_test(self, loser: ApiAbUser, winner: ApiAbUser, loser_is_player1):
        # basic forfeit logic
        self.assertEqual(loser.fetch_game().game_status, V4State.ongoing)
        response = loser.forfeit_util()
        result_after_ff = V4State.player1wins if loser_is_player1 else V4State.player2wins
        self.assertEqual(response, Api.Json.ok)
        self.assertEqual(loser.fetch_game().game_status, result_after_ff)

    def make_sure_game_ended(self, players: [ApiAbUser]):
        for player in players:
            game_result = player.fetch_game().game_status
            self.assertNotEqual(game_result, V4State.ongoing)
            self.assertNotEqual(player.move(8), "ok")
            response = player.forfeit_util()
            self.assertNotEqual(player.move(1), "ok")
            self.assertEqual(player.fetch_game().game_status, game_result)
            self.assertNotEqual(response, Api.Json.ok)

    def start_game_test(self, user1: ApiAbUser, user2: ApiAbUser, first_game=True):

        # verify not challenged yet
        print(f"Expect {user1.name} not to be in {user2.fetch_challengers_util()}")
        self.assertNotIn(user1.name, user2.fetch_challengers_util())
        # challenge
        user1.challenge(user2.name)
        # verify challenged
        print(f"Expect {user1.name} to be in {user2.fetch_challengers_util()}")
        self.assertIn(user1.name, user2.fetch_challengers_util())

        # verify not challenged yet
        print(f"Expect {user2.name} not to be in {user1.fetch_challengers_util()}")
        self.assertNotIn(user2.name, user1.fetch_challengers_util())
        # challenge
        user2.challenge(user1.name)

        # verify both challenges disappear
        print(f"Expect {user2.name} not to be in {user1.fetch_challengers_util()}")
        self.assertNotIn(user2.name, user1.fetch_challengers_util())
        print(f"Expect {user1.name} not to be in {user2.fetch_challengers_util()}")
        self.assertNotIn(user1.name, user2.fetch_challengers_util())
        # verify fetch game returns last move -1 -1
        self.assertEqual(user1.fetch_game().last_move, [-1, -1])
        self.assertEqual(user1.fetch_game().player1turn, True)
        self.assertEqual(user1.fetch_game().player1, user2.name)
        self.assertEqual(user1.fetch_game().player2, user1.name)

        self.assertEqual(user2.fetch_game().last_move, [-1, -1])
        self.assertEqual(user2.fetch_game().player1turn, True)
        self.assertEqual(user2.fetch_game().player1, user2.name)
        self.assertEqual(user2.fetch_game().player2, user1.name)
        # have player 2 attempt to make a move
        self.assertNotEqual(user1.move(3).status, "ok")

    def play_a_set_of_moves_test(self, user1: ApiAbUser, user2: ApiAbUser, game_with_expectations: {}):
        for index in range(0, len(game_with_expectations[utils.moves_player1])):
            user1.move(game_with_expectations[utils.moves_player1][index])
            self.assertEqual(user2.fetch_game().last_move[0], game_with_expectations[utils.moves_player1][index])
            self.assertNotEqual(user1.move(3).status, "ok")
            if index < len(game_with_expectations[utils.moves_player2]):
                user2.move(game_with_expectations[utils.moves_player2][index])
                self.assertEqual(user2.fetch_game().last_move[0], game_with_expectations[utils.moves_player2][index])
                self.assertNotEqual(user2.move(3).status, "ok")

    def login_test(self, user: ApiAbUser = None, user_name=None, password=None):
        if user:
            self.assertNotEqual(user.logout(), Api.Json.ok)
            self.assertEqual(user.login(), Api.Json.ok)
        else:
            user = ApiAbUser(user_name, password, self.app)

        self.assertNotEqual(user.login("kokoko", "eheheh"), Api.Json.ok)
        self.assertEqual(user.login(), Api.Json.ok)

        return user

    def logout_test(self, user: ApiAbUser):
        self.assertEqual(user.logout(), Api.Json.ok)
        self.assertNotEqual(user.logout(), Api.Json.ok)
        self.assertNotEqual(user.challenge("admin"), Api.Json.ok)

    # TODO test solo challenge
    def test_duel_session_integration_test(self):
        self.logout_test(self.player1)
        self.login_test(self.player1)
        self.start_game_test(self.player1, self.player2)
        self.play_a_set_of_moves_test(self.player2, self.player1, utils.games_and_expectations.player2_vertical_win)
        self.make_sure_game_ended([self.player1, self.player2])

        self.start_game_test(self.player2, self.player1)
        self.play_a_set_of_moves_test(self.player1, self.player2,
                                      utils.games_and_expectations.first_half_vertical_win_player_1)

        self.logout_test(self.player1)
        self.logout_test(self.player2)
        self.login_test(self.player1)
        self.login_test(self.player2)

        self.play_a_set_of_moves_test(self.player1, self.player2,
                                      utils.games_and_expectations.second_half_vertical_win_player_1)
        self.make_sure_game_ended([self.player1, self.player2])

        self.logout_test(self.player1)
        self.login_test(self.player1)

        self.start_game_test(self.player2, self.player1)

        self.play_a_set_of_moves_test(self.player1, self.player2,
                                      utils.games_and_expectations.first_half_vertical_win_player_1)

        self.logout_test(self.player1)
        self.forfeit_the_game_test(self.player2, self.player1, True)
        self.login_test(self.player1)
        self.make_sure_game_ended([self.player1, self.player2])

        self.start_game_test(self.player1, self.player2)
        self.play_a_set_of_moves_test(self.player2, self.player1, utils.games_and_expectations.player2_vertical_win)
        self.make_sure_game_ended([self.player1, self.player2])
    # idea is to check if states and datatypes properly support multiple games without application restart

    def test_large_multi_user_session_integration_test(self):
        pass
        # 5 user login
        # 2 duels, 1 solo
    # iterate fetch challenges and fetch games state spammingly

    # when / how often do I test bad api usage + in what way?

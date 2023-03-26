from unittest import TestCase

from unittest import TestCase

from flask.testing import FlaskClient

from src import V4State
from src.constants import Api
from src.flask_app import find_properties_in_answer, app
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
        moves_double_array = [[1, 2, 1, 2, 1, 5],
                              [2, 3, 3, 5, 2, 1]]
        self.play_a_set_of_moves_test(self.player2, self.player1, moves_double_array)
        self.forfeit_the_game_test(self.player1, self.player2, True)

        # interpret result

    # theoretically I only need loser
    # I can get winner by finding opponent through game
    # I can also get the player position through the game
    # choose this because I don't care, it's fine for now
    def forfeit_the_game_test(self, loser: ApiAbUser, winner: ApiAbUser, loser_is_player1):
        self.assertEqual(loser.fetch_game().game_status, V4State.ongoing)
        response = loser.forfeit_util()
        result_after_ff = V4State.player1wins if loser_is_player1 else V4State.player2wins
        self.assertEqual(response, Api.Json.ok)
        self.assertEqual(loser.fetch_game().game_status, result_after_ff)
        response = winner.forfeit_util()
        self.assertEqual(winner.fetch_game().game_status, result_after_ff)
        self.assertNotEqual(response, Api.Json.ok)
        response = loser.forfeit_util()
        self.assertEqual(winner.fetch_game().game_status, result_after_ff)
        self.assertNotEqual(response, Api.Json.ok)

        self.assertNotEqual(loser.move(1), "ok")
        self.assertNotEqual(winner.move(1), "ok")

    def start_game_test(self, user1: ApiAbUser, user2: ApiAbUser):
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

    def play_a_set_of_moves_test(self, user1: ApiAbUser, user2: ApiAbUser, moves_double_array: []):
        for index in range(0, len(moves_double_array[0])):
            user1.move(moves_double_array[0][index])
            self.assertEqual(user2.fetch_game().last_move[0], moves_double_array[0][index])
            self.assertNotEqual(user1.move(3).status, "ok")
            if index < len(moves_double_array[1]):
                user2.move(moves_double_array[1][index])
                self.assertEqual(user2.fetch_game().last_move[0], moves_double_array[1][index])
                self.assertNotEqual(user2.move(3).status, "ok")

    def test_duel_integration_test(self):
        pass
        # 2 user login
        # challenge each other
        # meanwhile always checking fetch state
        # do moves once fetch state returns game
        # check game end start moving
        # always check for game end
        # check post game functionalites

    def test_duel_session_integration_test(self):
        pass
        # 2 user login
        # challenge each other
        # meanwhile always checking fetch state
        # do moves once fetch state returns game
        # check game end start moving
        # always check for game end
        # check post game functionalites

    # surrender some games
    # log in and out between games

    # idea is to check if states and datatypes properly support multiple games without application restart

    def test_large_multi_user_session_integration_test(self):
        pass

    # iterate fetch challenges and fetch games state spammingly

    # when / how often do I test bad api usage + in what way?

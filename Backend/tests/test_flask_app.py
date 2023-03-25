from unittest import TestCase

from unittest import TestCase

from flask.testing import FlaskClient

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

    def test_thing(self):
        response = self.app.post('/login', json={
            "username": "admin",
            "password": "admins"
        })
        print(response)

        # test game start -

    def test_game_forfeit(self):
        self.start_game(self.player1, self.player2)
        # two players play set of moves

        # forfeit game

        # interpret result

    def start_game(self, user1: ApiAbUser, user2: ApiAbUser):
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
        #self.assertNotEqual(user2.move(3).status, "ok")
        print("-------")
        print("-------")
        print("-------")
        print("-------")
        print("-------")
        self.assertNotEqual(user1.move(3).status, "ok")

    def play_a_set_of_moves(self, user1: ApiAbUser, user2: ApiAbUser, moves_double_array: []):

        moves_double_array = [[1, 2, 1, 2, 1, 1],
                 [2, 3, 3, 5, 2, 1]]
        for index in range(0, len(moves_double_array[0])):
            user1.move(moves_double_array[0][index])
            user1.move(3)
            if index < len(moves_double_array[1]):
                user2.move(moves_double_array[1][index])
                user2.move(2)

        # player 2 tries to make first move
        # player 1 makes first move
        # player iterating over move set -> everytime same players tries to make an additional move

    def test_logoff_during_game(self):
        pass

    def test_large_duel_integration_test(self):
        pass
        # 2 user login
        # challenge each other
        # meanwhile always checking fetch state
        # do moves once fetch state returns game
        # check game end start moving
        # always check for game end
        # check post game functionalites

    def test_large_duel_session_integration_test(self):
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

from unittest import TestCase

from src.ViergewinntManager import game_manager
from src.user_management import user_manager


class TestGameManagement(TestCase):

    def setUp(self):
        user_manager.sessions = {}
        game_manager.player1_sessions = {}
        game_manager.player2_sessions = {}
        game_manager.challenges = {}

    def test_challenge(self):
        status, token = user_manager.login("admin", "admins")

        print("challenges: ", game_manager.fetch_challengers(token))
        self.assertFalse("admin" in game_manager.fetch_challengers(token)[1])

        game_manager.challenge(token, "admin")

        print("Ongoing game: ", game_manager.check_ongoing_game(token))
        self.assertIsNone(game_manager.check_ongoing_game(token))

        print("challenges: ", game_manager.fetch_challengers(token))
        self.assertTrue("admin" in game_manager.fetch_challengers(token)[1])

        game_manager.challenge(token, "admin")

        print("Ongoing game: ", game_manager.check_ongoing_game(token))
        self.assertIsNotNone(game_manager.check_ongoing_game(token))

    def test_challenge_2(self):
        status, token = user_manager.login("admin", "admins")
        status2, token2 = user_manager.login("admina", "admins")

        # one-sided challenge active
        game_manager.challenge(token, "admina")

        print("challenges: ", game_manager.fetch_challengers(token2))
        self.assertTrue("admin" in game_manager.fetch_challengers(token2)[1])

        print("Ongoing game: ", game_manager.check_ongoing_game(token))
        self.assertIsNone(game_manager.check_ongoing_game(token))

        print("challenges: ", game_manager.fetch_challengers(token))
        self.assertFalse("admin" in game_manager.fetch_challengers(token)[1])

        # both sided activates game
        game_manager.challenge(token2, "admin")

        print("challenges: ", game_manager.fetch_challengers(token2))
        self.assertTrue(len(game_manager.fetch_challengers(token)[1]) == 0)

        print("challenges: ", game_manager.fetch_challengers(token2))
        self.assertFalse("admina" in game_manager.fetch_challengers(token)[1])

        print("Ongoing game: ", game_manager.check_ongoing_game(token))
        self.assertIsNotNone(game_manager.check_ongoing_game(token))

        print(game_manager.make_move(token, 3)[1].result)
        print(game_manager.make_move(token2, 2))
        print(game_manager.make_move(token2, 2))
        print(game_manager.fetch_state(token))
        print(game_manager.fetch_state(token2))
        print(game_manager.make_move(token, 3)[1].result)
        print(game_manager.make_move(token2, 2))
        print(game_manager.make_move(token, 3)[1].result)
        print(game_manager.make_move(token2, 2))
        print(game_manager.make_move(token, 3)[1].result)
        print(game_manager.make_move(token2, 2))
        print(game_manager.make_move(token, 3)[1].result)
        print(game_manager.make_move(token2, 2))
        print(game_manager.fetch_state(token)[1].result)
        print(game_manager.fetch_state(token2)[1].result)

    def test_challenge_3(self):
        status, token = user_manager.login("admin", "admins")
        status2, token2 = user_manager.login("admina", "admins")
        game_manager.challenge(token, "admina")
        game_manager.challenge(token2, "admin")
        print(game_manager.fetch_challengers(token2), "chall")
        print(game_manager.fetch_challengers(token), "chall")

        print(game_manager.check_ongoing_game(token))

        print(game_manager.make_move(token, 3)[1].result)
        print(game_manager.make_move(token2, 2))
        print(game_manager.make_move(token2, 2))
        print(game_manager.make_move(token, 3)[1].result)
        print(game_manager.make_move(token2, 2))
        print(game_manager.make_move(token, 3)[1].result)
        print(game_manager.make_move(token2, 2))
        print(game_manager.make_move(token, 3)[1].result)
        print(game_manager.make_move(token2, 2))
        print(game_manager.make_move(token, 3)[1].result)
        print(game_manager.make_move(token2, 2))

        # coverage run --source=./src -m unittest discover -s tests/ && coverage html
        # coverage run --source=./src -m unittest discover -s tests/ && coverage report

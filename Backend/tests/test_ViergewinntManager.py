from unittest import TestCase

from ViergewinntManager import game_manager
from user_management import user_manager


class TestGameManagement(TestCase):
    def test_request_solo_game(self):
        token = user_manager.login("admin", "admins")
        print(game_manager.request_solo_game(token))

    def test_fetch_state(self):
        token = user_manager.login("admin", "admins")
        print(game_manager.request_solo_game(token))
        print()
        print(game_manager.fetch_state(token))

    def test_viergewinnt(self):
        token = user_manager.login("admin", "admins")
        print(game_manager.request_solo_game(token))
        print()
        print(game_manager.fetch_state(token))
        print(game_manager.make_move(token, 1))
        print(game_manager.make_move(token, 2))
        print(game_manager.make_move(token, 1))
        print(game_manager.make_move(token, 2))
        print(game_manager.make_move(token, 1))
        print(game_manager.make_move(token, 2))
        print(game_manager.make_move(token, 1))
        print(game_manager.make_move(token, 2))
        print(game_manager.make_move(token, 1))
        print(game_manager.make_move(token, 2))

    def test_check_ongoing_game(self):
        status, token = user_manager.login("admin", "admins")
        game_manager.request_solo_game(token)

        print(game_manager.check_ongoing_game(token))
        game_manager.forfeit_match(token)
        print(game_manager.check_ongoing_game(token))

    def test_challenge(self):
        status, token = user_manager.login("admin", "admins")
        game_manager.challenge(token, "admin")

        print(game_manager.check_ongoing_game(token))

        print(game_manager.fetch_challenges(token), "chall")
        game_manager.challenge(token, "admin")

        print(game_manager.check_ongoing_game(token))

    def test_challenge_2(self):
        status, token = user_manager.login("admin", "admins")
        status2, token2 = user_manager.login("admina", "admins")
        game_manager.challenge(token, "admina")

        print(game_manager.check_ongoing_game(token))

        print(game_manager.fetch_challenges(token2), "chall")
        game_manager.challenge(token2, "admin")
        print(game_manager.fetch_challenges(token2), "chall")
        print(game_manager.fetch_challenges(token), "chall")

        print(game_manager.check_ongoing_game(token))

    def test_challenge_3(self):
        status, token = user_manager.login("admin", "admins")
        status2, token2 = user_manager.login("admina", "admins")
        game_manager.challenge(token, "admina")

        print(game_manager.check_ongoing_game(token))

        print(game_manager.fetch_challenges(token2), "chall")
        game_manager.challenge(token2, "admin")
        print(game_manager.fetch_challenges(token2), "chall")
        print(game_manager.fetch_challenges(token), "chall")

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
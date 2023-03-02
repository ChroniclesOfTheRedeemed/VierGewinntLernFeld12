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

from unittest import TestCase

from ViergewinntManager import game_manager
from user_management import user_manager


class TestGameManagement(TestCase):
    def test_request_solo_game(self):
        token = user_manager.login("admin", "admin")
        print(game_manager.request_solo_game(token))

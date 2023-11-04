from unittest import TestCase

from src.game import connect_four_state
from src.game.connect_four_state import GameEndedException
from src.game.connect_four_game import ConnectFourGame
from tests import utils
from tests.utils import normal_wins, json_message


class TestViergewinnt(TestCase):
    game: ConnectFourGame

    @classmethod
    def setUpClass(cls):
        print("Starting all the tests.")

    def setUp(self):
        self.game = ConnectFourGame()

    def game_ended(self, game):
        if game.State.result == connect_four_state.ongoing:
            return False
        try:
            game.player_made_move(3)
        except GameEndedException:
            return True
        else:
            return False

    def test_standard_win(self):
        for test_case in normal_wins:
            game = ConnectFourGame()
            for index, move in enumerate(test_case[utils.moves_player1]):
                self.assertFalse(self.game_ended(game), test_case[utils.json_message] + " move " + str(move))
                game.player_made_move(move)
                if index < len(test_case[utils.moves_player2]):
                    move = test_case[utils.moves_player2][index]
                    self.assertFalse(self.game_ended(game), test_case[utils.json_message] + " move " + str(move))
                    game.player_made_move(move)

            self.assertTrue(self.game_ended(game), test_case[json_message])
            self.assertTrue(self.game_ended(game), test_case[json_message])
            self.assertTrue(self.game_ended(game), test_case[json_message])

# add draw win

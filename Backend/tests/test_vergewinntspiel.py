from unittest import TestCase

from src import V4State
from src.V4State import GameEndedException
from src.vergewinntspiel import Viergewinnt
from tests import utils
from tests.utils import normal_wins, json_message


class TestViergewinnt(TestCase):
    game: Viergewinnt

    @classmethod
    def setUpClass(cls):
        print("Starting all the tests.")

    def setUp(self):
        self.game = Viergewinnt()

    def game_ended(self, game):
        if game.State.result == V4State.ongoing:
            return False
        try:
            game.playerMadeMove(3)
        except GameEndedException:
            return True
        else:
            return False

    def test_standard_win(self):
        for test_case in normal_wins:
            game = Viergewinnt()
            for index, move in enumerate(test_case[utils.moves_player1]):
                self.assertFalse(self.game_ended(game), test_case[utils.json_message] + " move " + str(move))
                game.playerMadeMove(move)
                if index < len(test_case[utils.moves_player2]):
                    move = test_case[utils.moves_player2][index]
                    self.assertFalse(self.game_ended(game), test_case[utils.json_message] + " move " + str(move))
                    game.playerMadeMove(move)

            self.assertTrue(self.game_ended(game), test_case[json_message])
            self.assertTrue(self.game_ended(game), test_case[json_message])
            self.assertTrue(self.game_ended(game), test_case[json_message])

# add draw win

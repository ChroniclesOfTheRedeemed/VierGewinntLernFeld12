from unittest import TestCase

from src import V4State
from src.V4State import GameEndedException
from src.vergewinntspiel import Viergewinnt

expected_result = "game result"
json_game = "game"
json_message = "message"


class TestViergewinnt(TestCase):
    game: Viergewinnt

    games_and_expectations = [
        {
            json_message: "vertical win for player 1",
            json_game: [
                1, 2, 1, 2, 1, 2, 1
            ],
            expected_result: V4State.player1wins
        },
        {
            json_message: "horizontal win for player 1",
            json_game: [
                1, 1, 2, 2, 3, 3, 4
            ],
            expected_result: V4State.player1wins
        },
        {
            json_message: "diagonal win for player 1",
            json_game: [
                1, 2, 2, 3, 3, 4, 3, 4, 1, 4, 4
            ],
            expected_result: V4State.player1wins
        },
        {
            json_message: "vertical win for player 2",
            json_game: [
                5, 1, 2, 1, 2, 1, 2, 1
            ],
            expected_result: V4State.player2wins
        },
        {
            json_message: "horizontal win for player 2",
            json_game: [
                5, 1, 1, 2, 2, 3, 3, 4
            ],
            expected_result: V4State.player2wins
        },
        {
            json_message: "diagonal win for player 2",
            json_game: [
                6, 1, 2, 2, 3, 3, 4, 3, 4, 1, 4, 4
            ],
            expected_result: V4State.player2wins
        },
    ]

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
        for test_case in self.games_and_expectations:
            game = Viergewinnt()
            for move in test_case[json_game]:
                self.assertFalse(self.game_ended(game), test_case[json_message] + " move " + str(move))
                game.playerMadeMove(move)
            self.assertTrue(self.game_ended(game), test_case[json_message])
            self.assertTrue(self.game_ended(game), test_case[json_message])
            self.assertTrue(self.game_ended(game), test_case[json_message])


 # add draw win
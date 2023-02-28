from unittest import TestCase

from V4GState import GameObserver
from vergewinntspiel import Viergewinnt


class customObserver(GameObserver):
    def gameOver(self, player1wins):
        print("Player 1 won?: " + str(player1wins))

class TestViergewinnt(TestCase):
    def test_get_game_state(self):
        observer = customObserver()
        game = Viergewinnt()
        game.playerMadeMove()

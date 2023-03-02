from unittest import TestCase

from V4State import GameObserver
from vergewinntspiel import Viergewinnt


class customObserver(GameObserver):
    def gameOver(self, player1wins):
        print("Player 1 won?: " + str(player1wins))

class TestViergewinnt(TestCase):
    def test_player1wins_vertically(self):
        observer = customObserver()
        game = Viergewinnt(observer)
        game.playerMadeMove(4)
        game.playerMadeMove(3)
        game.playerMadeMove(4)
        game.playerMadeMove(3)
        game.playerMadeMove(4)
        game.playerMadeMove(3)
        game.playerMadeMove(4)
        game.playerMadeMove(3)

    def test_player2wins_vertically(self):
        observer = customObserver()
        game = Viergewinnt(observer)
        game.playerMadeMove(1)
        game.playerMadeMove(3)
        game.playerMadeMove(4)
        game.playerMadeMove(3)
        game.playerMadeMove(4)
        game.playerMadeMove(3)
        game.playerMadeMove(4)
        game.playerMadeMove(3)

    def test_player1wins_horizontally(self):
        observer = customObserver()
        game = Viergewinnt(observer)
        game.playerMadeMove(1)
        game.playerMadeMove(1)
        game.playerMadeMove(2)
        game.playerMadeMove(2)
        game.playerMadeMove(3)
        game.playerMadeMove(3)
        game.playerMadeMove(4)
        game.playerMadeMove(4)

    def test_player2wins_horizontally(self):
        observer = customObserver()
        game = Viergewinnt(observer)
        game.playerMadeMove(6)
        game.playerMadeMove(1)
        game.playerMadeMove(1)
        game.playerMadeMove(2)
        game.playerMadeMove(2)
        game.playerMadeMove(3)
        game.playerMadeMove(3)
        game.playerMadeMove(4)
        game.playerMadeMove(4)

    def test_player1wins_diagonally(self):
        observer = customObserver()
        game = Viergewinnt(observer)
        game.playerMadeMove(1)
        game.playerMadeMove(2)
        game.playerMadeMove(2)
        game.playerMadeMove(3)
        game.playerMadeMove(3)
        game.playerMadeMove(4)
        game.playerMadeMove(3)
        game.playerMadeMove(4)
        game.playerMadeMove(1)
        game.playerMadeMove(4)
        game.playerMadeMove(4)

    def test_player2wins_diagonally(self):
        observer = customObserver()
        game = Viergewinnt(observer)
        game.playerMadeMove(6)
        game.playerMadeMove(1)
        game.playerMadeMove(2)
        game.playerMadeMove(2)
        game.playerMadeMove(3)
        game.playerMadeMove(3)
        game.playerMadeMove(4)
        game.playerMadeMove(3)
        game.playerMadeMove(4)
        game.playerMadeMove(1)
        game.playerMadeMove(4)
        game.playerMadeMove(4)
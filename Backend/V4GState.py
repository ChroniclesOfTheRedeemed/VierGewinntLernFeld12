class V4GState:
    SpielFeld = []
    player1turn = True
    # change


class GameObserver:

    def gameOver(self, player1wins):
        pass


class BadMoveException(Exception):
    pass

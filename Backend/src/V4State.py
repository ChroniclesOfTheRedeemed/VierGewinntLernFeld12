player1wins = "player1wins"
player2wins = "player2wins"
draw = "draw"
ongoing = "ongoing"


class Status4G:

    def __init__(self):
        self.SpielFeld = []
        self.player1turn = True
        self.result = ongoing
        self.last_move = (-1, -1)


class BadMoveException(Exception):
    pass


class GameEndedException(Exception):
    pass

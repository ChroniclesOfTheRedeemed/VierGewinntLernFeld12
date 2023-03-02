player1wins = "player1wins"
player2wins = "player1wins"
draw = "draw"
ongoing = "ongoing"

class Status:

    def __init__(self):
        self.SpielFeld = []
        self.player1turn = True
        self.result = "not_started"



class GameObserver:

    def gameOver(self, player1wins, game_id):
        pass


class BadMoveException(Exception):
    pass

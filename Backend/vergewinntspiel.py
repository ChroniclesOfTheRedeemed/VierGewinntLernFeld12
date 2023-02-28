import copy

from V4GState import V4GState, BadMoveException, GameObserver


class Viergewinnt:

    def __init__(self, observer: GameObserver):
        self.breite = 7
        self.hoehe = 6
        self.feldleer = 0
        self.spieler1mark = 1
        self.spieler2mark = 2
        self.four = 4
        self.maxMoves = self.breite * self.hoehe
        self.FirstMove = -1
        self.movesDone = 0
        self.State = V4GState()
        self.game_observer = observer
        self.State.SpielFeld = [[self.feldleer for item in range(0, self.hoehe)] for item in range(0, self.breite)]

    def getGameState(self):
        newState = V4GState()
        newState.SpielFeld = copy.deepcopy(self.State.SpielFeld)
        newState.player1turn = self.State.player1turn
        return newState

    async def playerMadeMove(self, move, client):
        self.checkMove(move)
        levelOfMove = self.updateSpielFeld(move)
        await self.updateGameStatus(move=move, levelOfMove=levelOfMove, client=client)
        return levelOfMove

    def checkMove(self, move):
        if 0 <= move < self.breite:
            if self.State.SpielFeld[move][self.hoehe - 1] is not self.feldleer:
                raise BadMoveException()
        else:
            raise BadMoveException()

    def gameWon(self, move, level):
        Mark = self.getMarkOfLastMove(move)
        if self.wonThroughVertically(move=move, level=level, mark=Mark):
            print("WON VERTICALLY")
            return True
        else:
            result = self.wonNotVertically(move=move, level=level, mark=Mark)
        return result

    def wonThroughVertically(self, move, level, mark):
        connect = 1
        print("level = " + str(level))
        for row in range(level - 1, -1, -1):
            print("row = " + str(row))
            if self.State.SpielFeld[move][row] is mark:
                print(str(connect) + " for the gutter")
                connect += 1
            else:
                break

        return connect >= self.four

    def wonNotVertically(self, move, level, mark):
        directions = 3

        for direction in range(0, directions):
            connect = 1
            increaseC = 1
            increaseR = direction - 1
            coordinateC = move + increaseC
            coordinateR = level + increaseR

            for i in range(0, self.four - 1):
                if self.inBoundaries(coloumn=coordinateC, row=coordinateR) \
                        and self.State.SpielFeld[coordinateC][coordinateR] is mark:
                    connect += 1
                    coordinateC += increaseC
                    coordinateR += increaseR
                else:
                    break
            if connect is self.four:
                print("WON ELSE")
                print("dir " + str(direction))
                return True
            increaseC = -increaseC
            increaseR = -increaseR
            coordinateC = move + increaseC
            coordinateR = level + increaseR
            for i in range(0, self.four - 1):
                if self.inBoundaries(coloumn=coordinateC, row=coordinateR) \
                        and self.State.SpielFeld[coordinateC][coordinateR] is mark:
                    connect += 1
                    coordinateC += increaseC
                    coordinateR += increaseR
                else:
                    break
            if connect >= self.four:
                print("WON ELSE")
                print("dir " + str(direction))
                return True
        return False

    def gameDraw(self):
        return self.movesDone >= self.maxMoves

    def getMarkOfLastMove(self, move):
        mark = 0
        for row in range(0, self.hoehe):
            if self.State.SpielFeld[move][row] is self.feldleer:
                break
            else:
                mark = self.State.SpielFeld[move][row]
        return mark

    def updateSpielFeld(self, checkedMove):
        if self.State.player1turn:
            mark = self.spieler1mark
        else:
            mark = self.spieler2mark

        level = 0
        for level in range(0, self.hoehe):
            if self.State.SpielFeld[checkedMove][level] is self.feldleer:
                self.State.SpielFeld[checkedMove][level] = mark
                break
        self.movesDone += 1
        self.State.player1turn = not self.State.player1turn
        return level

    async def updateGameStatus(self, move, levelOfMove, client):
        won = 0
        if self.gameWon(move=move, level=levelOfMove):
            won = self.getMarkOfLastMove(move=move)
        else:
            if not self.gameDraw():
                return
        await client.gameOver(player1wins=won)

    def inBoundaries(self, coloumn, row):
        return 0 <= coloumn < self.breite and 0 <= row < self.hoehe

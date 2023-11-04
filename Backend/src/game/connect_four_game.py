import copy

from src.game import connect_four_state
from src.game.connect_four_state import BadMoveException, Status4G


class ConnectFourGame:
    ids = 0

    def __init__(self):
        self.id = ConnectFourGame.ids + 1
        ConnectFourGame.ids += 1
        self.field_width = 7
        self.field_height = 6
        self.empty_field = 0
        self.player_1_mark = 1
        self.player_2_mark = 2
        self.four = 4
        self.maxMoves = self.field_width * self.field_height
        self.FirstMove = -1
        self.movesDone = 0
        self.State = Status4G()
        self.State.spiel_field = [[self.empty_field for _ in range(0, self.field_height)] for _ in
                                  range(0, self.field_width)]

    def get_game_state(self):
        new_state = Status4G()
        new_state.spiel_field = copy.deepcopy(self.State.spiel_field)
        new_state.player1turn = self.State.player1turn
        return new_state

    def player_made_move(self, move):
        if self.State.result == connect_four_state.ongoing:
            self.check_move(move)
            level_of_move = self.update_playing_field(move)
            self.update_game_status(move=move, level_of_move=level_of_move)
            return level_of_move
        else:
            raise connect_four_state.GameEndedException()

    def check_move(self, move):
        if 0 <= move < self.field_width:
            if self.State.spiel_field[move][self.field_height - 1] is not self.empty_field:
                raise BadMoveException()
        else:
            raise BadMoveException()

    def game_won(self, move, level):
        mark = self.get_mark_of_last_move(move)
        if self.won_through_vertically(move=move, level=level, mark=mark):
            return True
        else:
            result = self.won_not_vertically(move=move, level=level, mark=mark)
        return result

    def won_through_vertically(self, move, level, mark):
        connect = 1
        for row in range(level - 1, -1, -1):
            if self.State.spiel_field[move][row] is mark:
                connect += 1
            else:
                break

        return connect >= self.four

    def won_not_vertically(self, move, level, mark):
        directions = 3

        for direction in range(0, directions):
            connect = 1
            increase_c = 1
            increase_r = direction - 1
            coordinate_c = move + increase_c
            coordinate_r = level + increase_r

            for i in range(0, self.four - 1):
                if self.in_boundaries(column=coordinate_c, row=coordinate_r) \
                        and self.State.spiel_field[coordinate_c][coordinate_r] is mark:
                    connect += 1
                    coordinate_c += increase_c
                    coordinate_r += increase_r
                else:
                    break
            if connect is self.four:
                return True
            increase_c = -increase_c
            increase_r = -increase_r
            coordinate_c = move + increase_c
            coordinate_r = level + increase_r
            for i in range(0, self.four - 1):
                if self.in_boundaries(column=coordinate_c, row=coordinate_r) \
                        and self.State.spiel_field[coordinate_c][coordinate_r] is mark:
                    connect += 1
                    coordinate_c += increase_c
                    coordinate_r += increase_r
                else:
                    break
            if connect >= self.four:
                return True
        return False

    def game_draw(self):
        return self.movesDone >= self.maxMoves

    def get_mark_of_last_move(self, move):
        mark = 0
        for row in range(0, self.field_height):
            if self.State.spiel_field[move][row] is self.empty_field:
                break
            else:
                mark = self.State.spiel_field[move][row]
        return mark

    def update_playing_field(self, checked_move):
        if self.State.player1turn:
            mark = self.player_1_mark
        else:
            mark = self.player_2_mark

        level = 0
        for level in range(0, self.field_height):
            if self.State.spiel_field[checked_move][level] is self.empty_field:
                self.State.spiel_field[checked_move][level] = mark
                self.State.last_move = (checked_move, level)
                break
        self.movesDone += 1
        self.State.player1turn = not self.State.player1turn
        return level

    def update_game_status(self, move, level_of_move):
        won = 0
        if self.game_won(move=move, level=level_of_move):
            won = self.get_mark_of_last_move(move=move)
        else:
            if not self.game_draw():
                return
        self.State.result = connect_four_state.player1wins if won else connect_four_state.player2wins

    def in_boundaries(self, column, row):
        return 0 <= column < self.field_width and 0 <= row < self.field_height

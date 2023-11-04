def won_not_vertically(move, level, mark, spiel_field):
    directions = 3
    four = 4
    for direction in range(0, directions):
        connect = 1
        increase_c = 1
        increase_r = direction - 1
        coordinate_c = move + increase_c
        coordinate_r = level + increase_r

        for i in range(0, four - 1):
            if in_boundaries(column=coordinate_c, row=coordinate_r) \
                    and spiel_field[coordinate_c][coordinate_r] is mark:
                connect += 1
                coordinate_c += increase_c
                coordinate_r += increase_r
            else:
                break
        if connect is four:
            return True
        increase_c = -increase_c
        increase_r = -increase_r
        coordinate_c = move + increase_c
        coordinate_r = level + increase_r
        for i in range(0, four - 1):
            if in_boundaries(column=coordinate_c, row=coordinate_r) \
                    and spiel_field[coordinate_c][coordinate_r] is mark:
                connect += 1
                coordinate_c += increase_c
                coordinate_r += increase_r
            else:
                break
        if connect >= four:
            return True
    return False

def won_through_vertically(move, level, mark, spiel_field):
    four = 4
    connect = 1
    for row in range(level - 1, -1, -1):
        if spiel_field[move][row] is mark:
            connect += 1
        else:
            break

    return connect >= four


def in_boundaries(column, row, field_width, field_height):
    return 0 <= column < field_width and 0 <= row < field_height

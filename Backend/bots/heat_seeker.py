# https://youtu.be/OegyYwm6rqE
from bots.util import in_boundaries, get_level_of_move, return_x_highest_of_array, get_my_mark, \
    randomize_values


# counts as much near as possible


def non_vertical_heat_values(move, level, mark, spiel_field) -> list:
    directions = 3
    four = 4
    list_of_three = []
    for direction in range(0, directions):
        connect = 1
        increase_c = 1
        increase_r = direction - 1
        coordinate_c = move + increase_c
        coordinate_r = level + increase_r

        for i in range(0, four - 1):
            if in_boundaries(column=coordinate_c, row=coordinate_r) \
                    and spiel_field["coloumn_" + str(coordinate_c)][coordinate_r] is mark:
                connect += 1
                coordinate_c += increase_c
                coordinate_r += increase_r
            else:
                break
        if connect is four:
            list_of_three.append(connect)
            break
        increase_c = -increase_c
        increase_r = -increase_r
        coordinate_c = move + increase_c
        coordinate_r = level + increase_r
        for i in range(0, four - 1):
            if in_boundaries(column=coordinate_c, row=coordinate_r) \
                    and spiel_field["coloumn_" + str(coordinate_c)][coordinate_r] is mark:
                connect += 1
                coordinate_c += increase_c
                coordinate_r += increase_r
            else:
                break
        list_of_three.append(connect)
    return list_of_three


def vertical_heat_value(move, level, mark, spiel_field) -> int:
    connect = 1
    for row in range(level - 1, -1, -1):
        if spiel_field["coloumn_" + str(move)][row] is mark:
            connect += 1
        else:
            break
    return connect


def get_heat_array(game_state, player_name):
    spielfeld = game_state["game_field"]
    heat_values = []
    mark = get_my_mark(player_name, game_state)
    enemy_mark = get_my_mark("not-" + player_name, game_state)
    for column in range(0, 7):
        level = get_level_of_move(column, spielfeld)
        if level != -1:
            column_heat_value = 0

            column_heat_value += calculate_own_heat_value(column, level, mark, spielfeld)
            if column_heat_value >= 1:
                heat_values.append(column_heat_value)
                break
            column_heat_value += calculate_opponent_heat_value(column, level, enemy_mark, spielfeld)
            heat_values.append(column_heat_value)

    return heat_values


def calculate_own_heat_value(column, level, own_mark, spielfeld):
    column_heat_value = 0
    my_heat_array = non_vertical_heat_values(column, level, own_mark, spielfeld)
    my_heat_array.append(vertical_heat_value(column, level, own_mark, spielfeld))
    for heat_val in my_heat_array:
        if heat_val >= 4:
            return 1
        elif heat_val == 3:
            column_heat_value += 1 / 16
        elif heat_val == 2:
            column_heat_value += 1 / 32
    return column_heat_value


def calculate_opponent_heat_value(column, level, opponent_mark, spielfeld):
    column_heat_value = 0
    opponent_heat_array = non_vertical_heat_values(column, level, opponent_mark, spielfeld)
    opponent_heat_array.append(vertical_heat_value(column, level, opponent_mark, spielfeld))
    for heat_val in opponent_heat_array:
        if heat_val >= 4:
            return 0.9
        elif heat_val == 3:
            column_heat_value += 1 / 17
        elif heat_val == 2:
            column_heat_value += 1 / 33
    return column_heat_value


def get_hotness_move(game_state, player_name):
    heat_values = get_heat_array(game_state, player_name)
    heat_values = randomize_values(heat_values, 0.05, 0)

    result = return_x_highest_of_array(heat_values, 1)
    return result[0][0]  # first element, index



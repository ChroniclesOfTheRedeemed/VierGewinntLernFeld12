import numpy

field_height = 6
field_width = 7
empty_field = 0
player_1_mark = 1
player_2_mark = 2


def get_random_array():
    return list(numpy.random.rand(7))


def in_boundaries(column, row):
    return 0 <= column < field_width and 0 <= row < field_height


def return_x_highest_of_array(array, x):
    highest = get_highest(array, x)
    return [(array.index(high), high) for high in highest]


def filter_x_highest_of_array(array, x):
    highest = get_highest(array, x)
    return [(element if element in highest else 0) for element in array]


def get_highest_of_threshold(array, threshold):
    highest = get_highest(array, 1)[0]
    return [(element if element + threshold > highest else -1) for element in array]


def get_highest(array, x):
    highest = array[0:x]
    highest.sort()
    for e in array[x:]:
        if e > highest[0]:
            highest.pop(0)
            highest.append(e)
            highest.sort()
    return highest


# technically wrong since duplicated options only return the first index
# let chatgpt fix that


def get_level_of_move(checked_move, spiel_field):
    level = 0
    for level in range(0, field_height):
        if spiel_field["coloumn_" + str(checked_move)][level] is empty_field:
            break
    if spiel_field["coloumn_" + str(checked_move)][level] is empty_field:
        return level
    else:
        return -1


def get_my_mark(my_name, game_field):
    i_am_player1 = game_field["player1"] == my_name
    return 1 if i_am_player1 else 2


def is_it_my_turn(my_name, game_field):
    i_am_player1 = game_field["player1"] == my_name
    return i_am_player1 and game_field["player1turn"] or not i_am_player1 and not game_field["player1turn"]


print(get_highest_of_threshold([5, 3, 7, 1, 9, 7, 4], 3))


def randomize_values(heat_values, threshold, lower_bound):
    array = get_highest_of_threshold(heat_values, threshold)
    random_array = get_random_array()
    result_array = []
    for i in range(0, len(array)):
        result_array.append(array[i] + random_array[i] if array[i] >= lower_bound else lower_bound)
    return result_array

import random

import numpy

from bots.util import return_x_highest_of_array, get_level_of_move


def get_random_array():
    return list(numpy.random.rand(7))


def randy_move(game_state, player_name):
    result = 3
    random_array = get_random_array()
    for e in range(1, 7):
        result = return_x_highest_of_array(random_array, e)[0][0]
        if get_level_of_move(result, game_state["game_field"]) != -1:
            break

    return result

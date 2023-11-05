import random

import numpy

from bots.util import return_x_highest_of_array


def get_random_array():
    return list(numpy.random.rand(7))


def randy_move(game_state):
    result = return_x_highest_of_array(get_random_array(), 1)
    return result[0][0]  # first element, index

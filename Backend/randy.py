# if error on any try to log back in

from bots.api import login, fetch_challengers, challenge, get_state, move
from bots.heat_seeker import get_hotness_move
from bots.randy import randy_move
from src.game.constants import Api


# in game toggle

# check for challenges

# if challenged, accept / toggle in game

# if in game toggled, check for gameState

# if game State says my turn, make valid move

# if in game state says game over toggle in game and wait for challenges






if __name__ == "__main__":
    start_bot("randy", "randy4refjpodsre03tfwf", get_hotness_move)

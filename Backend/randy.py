# if error on any try to log back in
import random
import time

from bots.api import login, fetch_challengers, challenge, get_state, move
from src.constants import Api


# in game toggle

# check for challenges

# if challenged, accept / toggle in game

# if in game toggled, check for gameState

# if game State says my turn, make valid move

# if in game state says game over toggle in game and wait for challenges

def main():
    in_game = True
    password = "randy4refjpodsre03tfwf"
    name = "randy"
    token = ""
    while True:
        try:
            while True:
                if not in_game:
                    time.sleep(10)
                    data = fetch_challengers(token)
                    if data[Api.Json.challengers]:
                        challenge(token, data[Api.Json.challengers][0])
                        in_game = True
                else:
                    time.sleep(5)
                    game_state = get_state(token)
                    if game_state["status"] != "ok":
                        raise Exception
                    if game_state["game_state"] != "ongoing":
                        in_game = False
                    elif game_state["player1turn"]:
                        move(token, random.choice([0, 1, 2, 3, 4, 5, 6]))
        except Exception as e:
            data = login(name, password)
            token = data[Api.Json.token]
            # Handle login errors and retry
            print(f"Error during login: {e}")
            continue


if __name__ == "__main__":
    main()

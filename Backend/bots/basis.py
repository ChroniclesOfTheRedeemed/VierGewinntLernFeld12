import time

from bots.api import fetch_challengers, challenge, get_state, login, move
from src.game.constants import Api


def start_bot(name, password, bot_move):
    in_game = True
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
                    if game_state["status"] == "no game found":
                        in_game = False
                        continue
                    if game_state["game_state"] != "ongoing":
                        in_game = False
                    elif game_state["player1turn"]:
                        move_made = bot_move(game_state, name)
                        print("made move ", move_made)
                        move(token, move_made)
        except Exception as e:
            data = login(name, password)
            token = data[Api.Json.token]
            # Handle login errors and retry
            print(f"Error during login: {e}")
            continue

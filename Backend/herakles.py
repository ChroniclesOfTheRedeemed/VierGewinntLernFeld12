from bots.basis import start_bot
from bots.heat_seeker import get_hotness_move

if __name__ == "__main__":
    start_bot("herakles", "bot_herakles", get_hotness_move)

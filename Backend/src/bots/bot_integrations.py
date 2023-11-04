from src.game.player_integrations import PlayerIntegration


class RandyIntegration(PlayerIntegration):

    def make_move(self) -> int:
        pass


    # read in move into game

    # for all possible moves
    # check all sides

    # give 1 if 3 of own
    # give 0.999 if 3 of enemy
    # 7 times 1 is 100% chance win 0 is neutral, -1 is 100% chance of loss
    # give 1/8 for each 2 of own or enemy
    # give 1/16 for each 1 of own or enemy




    # make move and read into game
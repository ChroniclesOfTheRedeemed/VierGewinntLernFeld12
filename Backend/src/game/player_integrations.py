from abc import abstractmethod


class PlayerIntegration:

    @abstractmethod
    def make_move(self) -> int:
        pass

player_integration_list = {}
player_integration_list["Randy"] = None

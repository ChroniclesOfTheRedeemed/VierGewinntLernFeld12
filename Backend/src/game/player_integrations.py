from abc import abstractmethod

PlayerIntegrations = [

]

class PlayerIntegration:

    @abstractmethod
    def make_move(self) -> int:
        pass

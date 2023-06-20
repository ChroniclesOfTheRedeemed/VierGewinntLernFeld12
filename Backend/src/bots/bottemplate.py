from abc import abstractmethod


class BotTemplate:

    @abstractmethod
    def examine_state(self) -> list:
        pass

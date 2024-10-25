from abc import ABC, abstractmethod


class Turky(ABC):

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def gobble(self):
        pass

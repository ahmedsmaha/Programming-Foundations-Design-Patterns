from abc import ABC, abstractmethod


class Duck(ABC):

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def quack(self):
        pass

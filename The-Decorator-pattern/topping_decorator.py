from pizza import Pizza
from abc import ABC, abstractmethod


class ToppingDecorator(Pizza, ABC):
    @abstractmethod
    def get_description(self):
        pass

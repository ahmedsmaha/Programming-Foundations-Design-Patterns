from abc import ABC, abstractmethod


class Pizza(ABC):
    description = "Unknown pizza"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass

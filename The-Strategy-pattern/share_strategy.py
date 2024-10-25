from abc import ABC, abstractmethod


class ShareStrategy(ABC):

    @abstractmethod
    def share(self):
        pass

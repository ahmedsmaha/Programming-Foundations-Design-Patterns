from abc import ABC, abstractmethod


class PhoneCameraApp(ABC):

    def setShareStrategy(self, share_strategy):
        self.__share_strategy = share_strategy

    def share(self):
        return self.__share_strategy.share()

    def take(self):
        print("Taking the photo")

    def save(self):
        print("Saving the photo")

    @abstractmethod
    def edit(self):
        pass

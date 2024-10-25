from abc import ABC, abstractmethod


class Drone(ABC):

    @abstractmethod
    def beep(self):
        pass

    @abstractmethod
    def spin_rotors(self):
        pass

    @abstractmethod
    def take_off(self):
        pass

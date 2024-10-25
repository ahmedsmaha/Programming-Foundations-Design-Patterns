from abc import ABC, abstractmethod


class Display(ABC):

    @abstractmethod
    def display(self):
        """Class representing a person"""

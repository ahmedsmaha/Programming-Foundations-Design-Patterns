from abc import ABC, abstractmethod


class CustomCalendar(ABC):
    def __init__(self, zone_factory):
        self.zone_factory = zone_factory

    def print_calendar(self):
        print(f"--- {self.zone_factory.get_display_name()} Calendar ---")
        print(f"Offset from GMT: {self.zone_factory.get_offset()}")

    @abstractmethod
    def create_calendar(self):
        pass

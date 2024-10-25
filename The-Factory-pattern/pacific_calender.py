from custom_calender import CustomCalendar


class PacificCalendar(CustomCalendar):
    def __init__(self, zone_factory):
        self.zone_factory = zone_factory.create_zone("US/Central")

    def create_calendar(self):
        print("Making the calendar")

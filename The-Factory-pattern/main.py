from datetime import datetime
from pacific_calender import PacificCalendar
from zone_factory import ZoneFactory


if __name__ == "__main__":
    zone_factory = ZoneFactory()
    calendar = PacificCalendar(zone_factory)
    calendar.create_calendar()
    calendar.print_calendar()

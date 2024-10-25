from zone_eastern import ZoneEastern
from zone_central import ZoneCentral


class ZoneFactory:
    def create_zone(self, zone_id):
        zone = None
        if zone_id == "US/Central":
            zone = ZoneCentral()
        elif zone_id == "US/Eastern":
            zone = ZoneEastern()
        return zone

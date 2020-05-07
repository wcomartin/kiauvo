import re
from datetime import datetime, timezone


class AuthToken(object):
    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token


class Vehicle(object):
    hood_open = False
    trunk_open = False
    front_left_open = False
    front_right_open = False
    back_left_open = False
    back_right_open = False

    door_lock_state = True

    engine = False

    last_updated = None

    def __init__(self, vehicle, status, maintenance, engine_start_presets):
        self.vehicle = vehicle
        self.status = status
        self.maintenance = maintenance
        self.engine_start_presets = engine_start_presets

        self.hood_open = status["hoodOpen"]
        self.trunk_open = status["trunkOpen"]
        self.front_left_open = status["doorOpen"]["frontLeft"] == 1
        self.front_right_open = status["doorOpen"]["frontRight"] == 1
        self.back_left_open = status["doorOpen"]["backLeft"] == 1
        self.back_right_open = status["doorOpen"]["backRight"] == 1

        self.door_lock = status["doorLock"]

        self.engine = status["engine"]

        m = re.match(r"(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})", status["lastStatusDate"])
        time = datetime(
            year=int(m.group(1)),
            month=int(m.group(2)),
            day=int(m.group(3)),
            hour=int(m.group(4)),
            minute=int(m.group(5)),
            second=int(m.group(6)),
            tzinfo=timezone.utc
        )

        self.last_updated = time.isoformat()

    @property
    def all_doors_closed(self):
        return not (self.hood_open
                    or self.trunk_open
                    or self.front_left_open
                    or self.front_right_open
                    or self.back_left_open
                    or self.back_right_open)

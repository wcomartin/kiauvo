class AuthToken(object):
    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token


class Vehicle(object):
    def __init__(self, vehicle, status):
        self.vehicle = vehicle
        self.status = status

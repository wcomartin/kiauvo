import requests
import json

from KiaUvo.models import AuthToken, Vehicle


class KiaUvo(object):
    default_headers = {
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'host': 'www.myuvo.ca',
        'origin': 'https://www.myuvo.ca',
        'referer': 'https://www.myuvo.ca/login',
        'from': 'CWP',
        'language': '0',
        'offset': '0',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin'
    }

    base_url = 'https://www.myuvo.ca/tods/api/'

    def __init__(self, username, password):
        self.auth = self.login(username, password)
        self.verify_token()

    def login(self, username, password):
        url = self.base_url + 'lgn'
        payload = {'loginId': username, 'password': password}
        headers = self.default_headers

        req = requests.post(url, data=json.dumps(payload), headers=headers)
        print(json.dumps(req.json(), indent=4, sort_keys=True))

        xhr = req.json()

        return AuthToken(xhr['result']['accessToken'], xhr['result']['refreshToken'])

    def verify_token(self):
        url = self.base_url + 'vrfytnc'
        headers = self.default_headers.copy()
        headers.update({
            'accessToken': self.auth.access_token
        })

        req = requests.post(url, headers=headers, data=json.dumps({}))
        print(json.dumps(req.json(), indent=4, sort_keys=True))

        return req.json()['result']

    def get_vehicle_list(self):
        url = self.base_url + 'vhcllst'
        headers = self.default_headers.copy()
        headers.update({
            'accessToken': self.auth.access_token
        })

        req = requests.post(url, headers=headers, data=json.dumps({}))
        print(json.dumps(req.json(), indent=4, sort_keys=True))

        return [self.get_vehicle_status(x['vehicleId']) for x in req.json()['result']['vehicles']]

    def get_vehicle_status(self, vehicle_id):
        url = self.base_url + 'sltvhcl'
        headers = self.default_headers.copy()
        headers.update({
            'accessToken': self.auth.access_token,
            'vehicleId': vehicle_id
        })

        req = requests.post(url, headers=headers, data=json.dumps({}))
        print(json.dumps(req.json(), indent=4, sort_keys=True))
        result = req.json()['result']

        return Vehicle(result['vehicle'], result['status'])

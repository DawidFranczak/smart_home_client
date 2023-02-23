from datetime import datetime
import requests
import json

from .mod import check_aqua
from const.const import SERVER_URL, CLIENT_URL, AQUARIUM_GET_ALL, AQUARIUM_UPDATE


def aquasCheck():
    """Get all aquas from the server then check if they aren't up to date
        return new values fluolamp and leds"""

    old_minutes = datetime.now().minute

    # while True:
    # new_minutes = datetime.now().minute

    # if old_minutes != new_minutes:
    if True:

        data = {"url": CLIENT_URL}
        aquas = requests.post(
            SERVER_URL + AQUARIUM_GET_ALL, data=data)
        aquas = aquas.json()
        print(aquas)
        test = [check_aqua(aqua['led_start'], aqua['led_stop'],
                           aqua['fluo_start'], aqua['fluo_stop'], aqua['ip'], aqua['port']) for aqua in aquas if not aqua['mode']]

        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json'}

        data['settings'] = test
        requests.post(
            SERVER_URL+AQUARIUM_UPDATE, data=json.dumps(data), headers=headers)

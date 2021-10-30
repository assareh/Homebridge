#!/usr/bin/env python

""" This script fades the specified lamp from one color state to another """

import os
import time
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# function that gets the current state of the lamp
def current_state():
    """ This function returns the current color parameters """
    
    URL = "http://localhost:5000/api/" + API_KEY + "/lights/4"
    current = requests.request("GET", URL, verify=False)
    x = current.json()['state']['xy'][0]
    y = current.json()['state']['xy'][1]
    bri = current.json()['state']['bri']
    hue = current.json()['state']['hue']
    sat = current.json()['state']['sat']
    return {'x': x, 'y': y, 'bri': bri, 'hue': hue, 'sat': sat}


# function that given begin state, end state and time delay performs the crossfade
def crossfade(begin_state, end_state):
    """ This function fades the specified lamp from one color state to another """

    num_stops = 125

    # calculate deltas (1.0 * to make it a float for accuracy)
    delta_bri = 1.0 * (end_state['bri'] - begin_state['bri']) / num_stops
    delta_hue = 1.0 * (end_state['hue'] - begin_state['hue']) / num_stops
    delta_sat = 1.0 * (end_state['sat'] - begin_state['sat']) / num_stops
    delta_x = (end_state['x'] - begin_state['x']) / num_stops
    delta_y = (end_state['y'] - begin_state['y']) / num_stops
    # print "DELTAS:", delta_bri, delta_hue, delta_sat, delta_x, delta_y

    for i in range(1, num_stops+1): # 1..250
        temp_bri = begin_state['bri'] + delta_bri * i
        temp_hue = begin_state['hue'] + delta_hue * i
        temp_sat = begin_state['sat'] + delta_sat * i
        temp_x = begin_state['x'] + delta_x * i
        temp_y = begin_state['y'] + delta_y * i
        # print "TEMP_VALS", temp_bri, temp_hue, temp_sat, temp_x, temp_y

        temp_payload = "{\n    \"on\": true,\n    \"xy\": [\n            " + str(temp_x) + \
             ",\n            " + str(temp_y) + "\n        ],\n    \"sat\":" + \
                 str(int(temp_sat)) + ",\n    \"bri\":" + str(int(temp_bri)) + \
                     ",\n    \"hue\":" + str(int(temp_hue)) + "\n}"
        requests.request("PUT", URL4, data=temp_payload, verify=False)
        time.sleep(0.1)


# Read the API key
API_KEY = os.environ['HUE_API_KEY']

# Initialize other variables
URL4 = "http://localhost:5000/api/" + API_KEY + "/lights/4/state"

# state definitions
# BEGIN_STATE = {'x': 0.4444, 'y': 0.4053, 'bri': 127, 'hue': 8496, 'sat': 118}
BEGIN_STATE = current_state()
END_STATE = {'x': 0.6922, 'y': 0.3076, 'bri': 2, 'hue': 0, 'sat': 254}

# initialize lights to storytime
# PAYLOAD = "{\n    \"on\": true,\n    \"xy\": [\n            " + str(BEGIN_STATE['x'])\
#     + ",\n            " + str(BEGIN_STATE['y']) + "\n        ],\n    \"sat\":" + \
#         str(BEGIN_STATE['sat']) + ",\n    \"bri\":" + str(BEGIN_STATE['bri']) + \
#             ",\n    \"hue\":" + str(BEGIN_STATE['hue']) + "\n}"
# requests.request("PUT", URL4, data=PAYLOAD, verify=False)

crossfade(BEGIN_STATE, END_STATE)

# end lights at bedtime
PAYLOAD = "{\n    \"on\": true,\n    \"xy\": [\n            " + str(END_STATE['x']) + \
    ",\n            " + str(END_STATE['y']) + "\n        ],\n    \"sat\":" + \
        str(END_STATE['sat']) + ",\n    \"bri\":" + str(END_STATE['bri']) + \
            ",\n    \"hue\":" + str(END_STATE['hue']) + "\n}"
requests.request("PUT", URL4, data=PAYLOAD, verify=False)

# Clear the flag to turn it off in HomeKit
os.remove(os.path.join(os.path.dirname(__file__), 'bedtime') + '.pid')

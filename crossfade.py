#!/usr/bin/env python

""" This script cycles the color lamp through the rainbow
    Requires a command line argument of lamp number
    4 is Leo's Lamp
    3 is Office
    2 is Living Room Color """

import os
import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Read the API key
API_KEY = os.environ['HUE_API_KEY']

# Initialize other variables
ON_PAYLOAD = "{\"on\":true, \"sat\":254, \"bri\":254,\"hue\":0}"
OFF_PAYLOAD = "{\n \"on\": false,\n \"xy\": [\n 0.4351,\n 0.4064\n],\n \
                \"sat\":254,\n \"bri\":254,\n \"hue\":0\n}"
URL4 = "http://hue-bridge.service.consul/api/" + API_KEY + "/lights/" + sys.argv[1] + "/state"

# Send the on payload to turn on the lamp
requests.request("PUT", URL4, data=ON_PAYLOAD, verify=False)

# Cycle the hue
for j in range(0, 20):
    for i in range(0, 132):
        PAYLOAD = "{\"hue\":" + str(i*500) + "}"
        requests.request("PUT", URL4, data=PAYLOAD, verify=False)
    j = j + 1

# Send the off payload to turn off the lamp
requests.request("PUT", URL4, data=OFF_PAYLOAD, verify=False)

# Clear the flag to turn it off in HomeKit
if sys.argv[1] == '4':
    os.remove(os.path.join(os.path.dirname(__file__), 'crossfade_leo') + '.pid')
elif sys.argv[1] == '2':
    os.remove(os.path.join(os.path.dirname(__file__), 'crossfade_lr') + '.pid')

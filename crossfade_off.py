#!/usr/bin/env python

""" This script powers off the specified lamp
    Requires a command line argument of lamp number
    4 is Leo's Lamp
    2 is Living Room Color """

import os
import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Read the API key
API_KEY = os.environ['HUE_API_KEY']

# Initialize other variables
OFF_PAYLOAD = "{\n \"on\": false,\n \"xy\": [\n 0.4351,\n 0.4064\n],\n \
                \"sat\":254,\n \"bri\":254,\n \"hue\":0\n}"
URL4 = "http://hue-bridge.service.consul/api/" + API_KEY + "/lights/" + sys.argv[1] + "/state"

requests.request("PUT", URL4, data=OFF_PAYLOAD, verify=False)

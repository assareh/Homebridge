#!/usr/bin/env python

""" This script powers on the specified lamp to a specified color
    3 is Office """

import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# Read the API key
API_KEY = os.environ['HUE_API_KEY']

# Read the API URL
API_URL = os.environ['HUE_API_URL']

# Initialize other variables
ON_PAYLOAD = "{\n \"on\": true,\n \"xy\": [\n 0.2796,\n 0.1612\n],\n \
                \"sat\":254,\n \"bri\":254,\n \"hue\":0\n}"
URL = API_URL + API_KEY + "/lights/3/state"


def turn_on(url):
    ''' turn on light
        accepts the url of the light as parameter '''
    requests.request("PUT", url, data=ON_PAYLOAD, verify=False)


# initialize lights
turn_on(URL)

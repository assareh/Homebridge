#!/usr/bin/env python

""" This script powers off the specified lamp to a specified color
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
OFF_PAYLOAD = "{\n \"on\": false}"
API_KEY = os.environ['HUE_API_KEY']
URL = API_URL + API_KEY + "/lights/3/state"


def turn_off(url):
    ''' turn off light
        accepts the url of the light as parameter '''
    requests.request("PUT", url, data=OFF_PAYLOAD, verify=False)


turn_off(URL)

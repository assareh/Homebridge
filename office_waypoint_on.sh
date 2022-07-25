#!/bin/sh
python3 /homebridge/scripts/office_waypoint.py &
echo  >/homebridge/scripts/office_waypoint.pid
echo "Started $!"

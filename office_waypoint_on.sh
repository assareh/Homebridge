#!/bin/sh
python /homebridge/scripts/office_waypoint.py &
echo  >/homebridge/scripts/office_waypoint.pid
echo "Started $!"

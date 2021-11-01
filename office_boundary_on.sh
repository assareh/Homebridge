#!/bin/sh
python /homebridge/scripts/office_boundary.py &
echo  >/homebridge/scripts/office_boundary.pid
echo "Started $!"

#!/bin/sh
python3 /homebridge/scripts/office_boundary.py &
echo  >/homebridge/scripts/office_boundary.pid
echo "Started $!"

#!/bin/sh
python3 /homebridge/scripts/office_nomad.py &
echo  >/homebridge/scripts/office_nomad.pid
echo "Started $!"

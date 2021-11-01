#!/bin/sh
python /homebridge/scripts/office_nomad.py &
echo  >/homebridge/scripts/office_nomad.pid
echo "Started $!"

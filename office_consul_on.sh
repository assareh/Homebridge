#!/bin/sh
python3 /homebridge/scripts/office_consul.py &
echo  >/homebridge/scripts/office_consul.pid
echo "Started $!"

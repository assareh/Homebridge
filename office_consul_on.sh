#!/bin/sh
python /homebridge/scripts/office_consul.py &
echo  >/homebridge/scripts/office_consul.pid
echo "Started $!"

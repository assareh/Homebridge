#!/bin/sh
python3 /homebridge/scripts/office_vagrant.py &
echo  >/homebridge/scripts/office_vagrant.pid
echo "Started $!"

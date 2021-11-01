#!/bin/sh
python /homebridge/scripts/office_vagrant.py &
echo  >/homebridge/scripts/office_vagrant.pid
echo "Started $!"

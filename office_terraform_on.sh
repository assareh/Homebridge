#!/bin/sh
python /homebridge/scripts/office_terraform.py &
echo  >/homebridge/scripts/office_terraform.pid
echo "Started $!"

#!/bin/sh
python3 /homebridge/scripts/office_terraform.py &
echo  >/homebridge/scripts/office_terraform.pid
echo "Started $!"

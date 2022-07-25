#!/bin/sh
python3 /homebridge/scripts/office_packer.py &
echo  >/homebridge/scripts/office_packer.pid
echo "Started $!"

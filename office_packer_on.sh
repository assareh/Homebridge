#!/bin/sh
python /homebridge/scripts/office_packer.py &
echo  >/homebridge/scripts/office_packer.pid
echo "Started $!"

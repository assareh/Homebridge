#!/bin/sh
python /homebridge/scripts/office_vault.py &
echo  >/homebridge/scripts/office_vault.pid
echo "Started $!"
